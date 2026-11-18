"""The Learn pages: the app's Welcome series (its outlines in ~/Developer/cadence/tools/welcome) as web pages, one page for each series and a Learn page that lists them.
build.py calls pages(); pictures are copied from the app's tools/welcome-art into assets/learn/. Nothing here is edited by hand: change the outline in the app and run build.py."""
import html
import json
import os
import re
import shutil
import struct

APP = os.path.expanduser('~/Developer/cadence')
WELCOME = os.path.join(APP, 'tools', 'welcome')
ART = os.path.join(APP, 'tools', 'welcome-art')
OUT = os.path.join('assets', 'learn')
COLORS = {'timer': '#ff9f40', 'video': '#ff5a5a', 'slide': '#ffe14d', 'audio': '#66ff66', 'cue': '#66ccff'}
SHOWS = re.compile(r'\{show:([^|}]+)\|[^}]+\}')
INLINE = re.compile(r'(\[[^\]]+\]|\{img:[a-z0-9/-]+(?:@[\d.]+)?\}|\{show:[^|}]+\|[^}]+\})')
e = html.escape


def png_size(path):
    with open(path, 'rb') as f:
        b = f.read(24)
    return struct.unpack('>II', b[16:24])


def asset(key):
    """Copies one picture of the app and returns (its address on the site, width, height)."""
    src = os.path.join(ART, key + '.png')
    if not os.path.exists(src):
        raise SystemExit('There is no picture ' + key + ' in the app (tools/welcome-art).')
    os.makedirs(OUT, exist_ok=True)
    name = key.replace('/', '-') + '.png'
    shutil.copyfile(src, os.path.join(OUT, name))
    w, h = png_size(src)
    return 'assets/learn/' + name, w, h


def cue_color(t):
    t = t.lower()
    for k in ('timer', 'video', 'slide', 'audio'):
        if t.startswith(k):
            return COLORS[k]
    return COLORS['cue']


def inline(s):
    out = []
    for part in INLINE.split(s):
        if not part:
            continue
        m = re.fullmatch(r'\[([^\]]+)\]', part)
        i = re.fullmatch(r'\{img:([a-z0-9/-]+)(?:@([\d.]+))?\}', part)
        sh = re.fullmatch(r'\{show:([^|}]+)\|[^}]+\}', part)
        if m:
            out.append('<span class="lcue" style="--c:%s">%s</span>' % (cue_color(m.group(1)), e(m.group(1))))
        elif i:
            src, w, h = asset(i.group(1))
            lines = float(i.group(2)) if i.group(2) else (1 if i.group(1).startswith('cue-') else 1.25)
            out.append('<img class="lkey" src="%s" alt="" style="height:%.2fem" width="%d" height="%d" loading="lazy">' % (src, lines * 1.15, w, h))
        elif sh:
            out.append('<strong class="lshow">%s</strong>' % e(sh.group(1)))
        else:
            out.append(e(part))
    return ''.join(out)


def module_html(text, num):
    """One outline as HTML: chapters (a '=' line) are headings, a thought is a paragraph, a YOUR TURN is a call-out."""
    meta = {'title': '', 'minutes': ''}
    body, para, chap, n = [], [], False, [0]

    def flush():
        if para:
            body.append('<p class="l%s">%s</p>' % (para[0][0], '<br>'.join(p for _, p in para)))
            para.clear()
    for raw in text.split('\n'):
        line = raw.rstrip()
        if not line or line.startswith('#'):
            continue
        m = re.match(r'^% (title|minutes) (.+)$', line)
        if m:
            meta[m.group(1)] = m.group(2)
            continue
        if re.match(r'^% ', line) or re.match(r'^- ?\d*$', line):
            continue
        m = re.match(r'^= (.+)$', line)
        if m:
            flush()
            if chap:
                body.append('</section>')
            n[0] += 1
            body.append('<section class="lchap"><h3>%s</h3>' % e(m.group(1)))
            chap = True
            continue
        m = re.match(r'^([ABC])([:+]) (.*)$', line)
        if m:
            if m.group(2) == ':':
                flush()
            para.append((m.group(1), inline(m.group(3))))
            continue
        m = re.match(r'^~:? (.*)$', line)
        if m:
            flush()
            para.append(('N', inline(m.group(1))))
            flush()
            continue
        m = re.match(r'^@img ([a-z0-9/-]+)(?: ([\d.]+))?$', line)
        if m:
            flush()
            src, w, h = asset(m.group(1))
            lines = float(m.group(2) or 1.25)
            wide = w / h > 6 or m.group(1) in ('logo',) 
            if m.group(1) == 'logo':
                continue
            style = '' if wide else ' style="max-height:%dpx"' % min(380, int(lines * 40))
            body.append('<figure class="lfig"><img src="%s" alt="" width="%d" height="%d" loading="lazy"%s></figure>' % (src, w, h, style))
            continue
        m = re.match(r'^! (.*)$', line)
        if m:
            flush()
            body.append('<p class="lturn"><b>Your turn</b> %s</p>' % e(re.sub(r'^YOUR TURN\s*-\s*', '', m.group(1))))
            continue
        m = re.match(r'^@ (.*)$', line)
        if m:
            t = m.group(1)
            if re.match(r'timer (set|start|finish)', t, re.I):
                continue
            flush()
            body.append('<p class="lN"><span class="lcue" style="--c:%s">%s</span></p>' % (cue_color(t), e(t)))
            continue
        raise SystemExit('Cannot read this outline line: ' + line)
    flush()
    if chap:
        body.append('</section>')
    return meta, ''.join(body)


def pages(hero, ph=None):
    """{file name: (title, description, body)} for Learn and each series."""
    spec = json.load(open(os.path.join(WELCOME, 'series.json')))['series']
    shutil.rmtree(OUT, ignore_errors=True)
    P, cards = {}, []
    for sr in spec:
        mods, toc, total = [], [], 0
        for i, name in enumerate(sr['modules'], 1):
            meta, body = module_html(open(os.path.join(WELCOME, sr['id'], name + '.txt')).read(), i)
            toc.append('<li><a href="#m%d">%s</a> <span class="lmin">%s min</span></li>' % (i, e(meta['title']), e(meta['minutes'])))
            mods.append('<article class="lmod" id="m%d"><header><span class="lnum">Module %d</span><h2>%s</h2><span class="lmin">About %s minutes</span></header>%s</article>' % (i, i, e(meta['title']), e(meta['minutes']), body))
        fn = 'learn-%s.html' % sr['id']
        intro = '<section class="wrap lintro"><p>These are the scripts you read on the prompter inside Cadence Prompt, shown as a page. In the app you press Play, read, and try each <b>Your turn</b> as you go. Practice is optional.</p><ol class="ltoc">%s</ol><p><a class="link" href="learn.html">&larr; All the series</a></p></section>' % ''.join(toc)
        P[fn] = ('%s | Learn | Cadence Prompt' % sr['title'], sr['about'], hero(sr['title'], sr['about'], False, 'Learn') + intro + '<div class="wrap lmods">' + ''.join(mods) + '</div>')
        cards.append('<a class="lcard" href="%s"><h3>%s</h3><p>%s</p><span class="lmin">%d modules</span></a>' % (fn, e(sr['title']), e(sr['about']), len(sr['modules'])))
    order = ''.join(cards)
    P['learn.html'] = ('Learn | Cadence Prompt', 'Learn Cadence Prompt, and how to run a prompter, one short module at a time.',
                       hero('Learn Cadence Prompt', 'Short modules that teach one or two things at a time. Start from the beginning, or jump to the series you need.', False, 'Learn')
                       + '<section class="wrap lgrid">%s</section>' % order
                       + '<section class="wrap lintro"><p>Inside the app, the same series are under <b>Help &rsaquo; Learn</b>. You read each one on the prompter, press Play, and try things as you go. Some features in these lessons are marked as new and untried: they are built, and not yet checked on real gear.</p></section>')
    return P
