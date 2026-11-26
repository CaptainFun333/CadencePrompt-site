"""Drawn pictures for the Features page: still, simplified recreations of what each page is about.
Each function returns one inline SVG; colors come from the site's tokens (style.css :root) so a change there reaches them."""

V, S, G, A, B = "var(--cue-video)", "var(--cue-slide)", "var(--cue-general)", "var(--cue-audio)", "var(--cue-bookmark)"
PANEL, PANEL2, LINE, FG, MUTE, BG = "var(--panel)", "var(--panel2)", "var(--line)", "var(--fg)", "var(--mute)", "var(--bg)"


def _svg(label, body, h=300):
    return (f'<figure class="art"><svg viewBox="0 0 480 {h}" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="Hanken Grotesk,system-ui,sans-serif">{body}</svg></figure>')


def _lines(x, y, widths, gap=9, fill=MUTE, opacity=.55, h=4):
    return "".join(f'<rect x="{x}" y="{y + i * gap}" width="{w}" height="{h}" rx="2" fill="{fill}" opacity="{opacity}"/>' for i, w in enumerate(widths))


def prep():
    files = ""
    for i, (tag, col) in enumerate([("DOCX", G), ("PDF", V), ("KEY", S)]):
        y = 34 + i * 74
        files += (f'<rect x="22" y="{y}" width="108" height="62" rx="6" fill="{PANEL2}" stroke="{LINE}"/>'
                  f'<rect x="32" y="{y + 10}" width="34" height="16" rx="3" fill="{col}" opacity=".9"/>'
                  f'<text x="49" y="{y + 22}" font-size="10" font-weight="700" fill="#101417" text-anchor="middle">{tag}</text>'
                  + _lines(32, y + 34, [84, 70, 78], 8))
    arrows = ('<path d="M138 170h46" stroke="%s" stroke-width="2" stroke-linecap="round"/>'
              '<path d="M178 162l10 8-10 8" fill="none" stroke="%s" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>' % (FG, FG))
    sweep = ''.join(f'<circle cx="{150 + i * 14}" cy="146" r="2.5" fill="{c}"/>' for i, c in enumerate([G, A, S]))
    script = (f'<rect x="196" y="22" width="262" height="256" rx="8" fill="{BG}" stroke="{LINE}"/>'
              f'<text x="214" y="48" font-size="12" font-weight="700" fill="{G}">HOST</text>' + _lines(214, 56, [210, 186, 120], 10, FG, .8, 5) +
              f'<rect x="214" y="96" width="132" height="20" rx="4" fill="none" stroke="{S}" stroke-width="1.5"/>'
              f'<text x="224" y="110" font-size="10" font-weight="700" fill="{S}">SLIDE 4 · Title</text>'
              f'<text x="214" y="142" font-size="12" font-weight="700" fill="{A}">ANA</text>' + _lines(214, 150, [220, 160, 196, 90], 10, FG, .8, 5) +
              f'<text x="214" y="212" font-size="11" font-style="italic" fill="{V}">[ Applause, video rolls ]</text>'
              f'<rect x="214" y="224" width="118" height="20" rx="4" fill="none" stroke="{V}" stroke-width="1.5"/>'
              f'<text x="224" y="238" font-size="10" font-weight="700" fill="{V}">VIDEO · Sizzle</text>'
              f'<g transform="translate(386 246)"><rect width="60" height="22" rx="11" fill="{PANEL2}" stroke="{LINE}"/>'
              f'<text x="30" y="15" font-size="10" font-weight="600" fill="{FG}" text-anchor="middle">&#8630; Undo</text></g>')
    return _svg("Three raw files, a Word document, a PDF and a Keynote file, flow into one script with colored speaker names, a slide cue and a video cue.",
                files + sweep + arrows + script)


def run_show():
    deck = f'<rect x="40" y="16" width="400" height="268" rx="18" fill="{PANEL2}" stroke="{LINE}" stroke-width="2"/>'
    keys = [("PLAY", FG), ("SNAP\nNEXT", G), ("CUE", G), ("VIDEO", V),
            ("BOOK\nMARK", B), ("SLIDE", S), ("AUDIO", A), ("END", V)]
    for i, (lab, col) in enumerate(keys):
        x, y = 62 + (i % 4) * 92, 34 + (i // 4) * 70
        deck += f'<rect x="{x}" y="{y}" width="76" height="60" rx="9" fill="{BG}" stroke="{col}" stroke-width="2.5"/>'
        for j, part in enumerate(lab.split("\n")):
            ty = y + 36 + (j - (len(lab.split("\n")) - 1) / 2) * 13
            deck += f'<text x="{x + 38}" y="{ty}" font-size="12" font-weight="700" fill="{col}" text-anchor="middle">{part}</text>'
    deck += (f'<rect x="62" y="176" width="356" height="34" rx="6" fill="{BG}" stroke="{LINE}"/>'
             f'<text x="80" y="199" font-size="17" font-weight="700" fill="{FG}" font-family="JetBrains Mono,monospace">12:30</text>'
             f'<text x="156" y="199" font-size="11" fill="{A}" font-family="JetBrains Mono,monospace">-0:12 under</text>'
             f'<rect x="270" y="188" width="132" height="8" rx="4" fill="{LINE}"/><rect x="270" y="188" width="84" height="8" rx="4" fill="{G}"/>')
    for i, lab in enumerate(["SPEED", "TEXT SIZE", "BOOKMARK", "Q2Q"]):
        cx = 100 + i * 92
        deck += (f'<circle cx="{cx}" cy="246" r="20" fill="{BG}" stroke="{MUTE}" stroke-width="2"/>'
                 f'<path d="M{cx} 246l0-14" stroke="{FG}" stroke-width="3" stroke-linecap="round" transform="rotate({[35, -20, 70, -50][i]} {cx} 246)"/>'
                 f'<text x="{cx}" y="277" font-size="8.5" fill="{MUTE}" text-anchor="middle">{lab}</text>')
    return _svg("A Stream Deck Plus: eight color-framed keys for play, snap, cues, bookmark and end, a touch strip showing the clock and the estimate, and four dials for speed, text size, bookmarks and cue to cue.", deck)


def time_cues():
    def device(x, y, w, h, r, screen):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{PANEL2}" stroke="{LINE}" stroke-width="2"/>'
                f'<rect x="{x + 6}" y="{y + 6}" width="{w - 12}" height="{h - 12}" rx="{max(r - 4, 2)}" fill="{BG}"/>' + screen(x + 6, y + 6, w - 12, h - 12))

    def clock(cx, cy, size, col=FG):
        return f'<text x="{cx}" y="{cy}" font-size="{size}" font-weight="700" fill="{col}" text-anchor="middle" font-family="JetBrains Mono,monospace">12:30</text>'

    def laptop(x, y, w, h):
        return (device(x, y, w, h, 8, lambda sx, sy, sw, sh: clock(sx + sw / 2, sy + 40, 34, A) +
                f'<text x="{sx + sw / 2}" y="{sy + 58}" font-size="10" fill="{MUTE}" text-anchor="middle">CEO keynote · -0:12</text>' +
                ''.join(f'<circle cx="{sx + 22}" cy="{sy + 78 + i * 16}" r="4" fill="{c}"/><rect x="{sx + 34}" y="{sy + 75 + i * 16}" width="{[56, 40, 66][i]}" height="6" rx="3" fill="{MUTE}" opacity=".5"/>'
                        f'<text x="{sx + sw - 8}" y="{sy + 82 + i * 16}" font-size="9" fill="{MUTE}" text-anchor="end">{["0:42", "1:15", "2:08"][i]}</text>' for i, c in enumerate([G, S, V]))) +
                f'<path d="M{x - 24} {y + h + 10}h{w + 48}l-8 10h-{w + 32}z" fill="{PANEL2}" stroke="{LINE}" stroke-width="2"/>')

    def phone(x, y):
        return device(x, y, 84, 150, 14, lambda sx, sy, sw, sh: _lines(sx + 8, sy + 12, [sw - 16, sw - 26, sw - 40], 9, FG, .8, 4) +
                      f'<rect x="{sx + 8}" y="{sy + 44}" width="{sw - 24}" height="14" rx="3" fill="none" stroke="{S}" stroke-width="1.3"/>' +
                      _lines(sx + 8, sy + 70, [sw - 16, sw - 30, sw - 22, sw - 44], 9, FG, .8, 4) +
                      f'<rect x="{sx + 8}" y="{sy + sh - 22}" width="{sw - 16}" height="14" rx="7" fill="{PANEL2}" stroke="{LINE}"/>'
                      f'<text x="{sx + sw / 2}" y="{sy + sh - 12}" font-size="8" fill="{MUTE}" text-anchor="middle">Suggest</text>')

    def sheet(x, y):
        return device(x, y, 110, 98, 6, lambda sx, sy, sw, sh: ''.join(
            f'<rect x="{sx + 8}" y="{sy + 10 + i * 18}" width="9" height="9" rx="2" fill="{A if i != 2 else "none"}" stroke="{A if i != 2 else V}" stroke-width="1.3"/>'
            f'<rect x="{sx + 24}" y="{sy + 12 + i * 18}" width="{[58, 46, 62, 40][i]}" height="5" rx="2.5" fill="{[G, S, V, A][i]}" opacity=".75"/>' for i in range(4)))

    links = (f'<g stroke="{MUTE}" stroke-width="1.6" stroke-dasharray="2 6" stroke-linecap="round" fill="none" opacity=".8">'
             '<path d="M170 140C150 140 120 140 110 130"/><path d="M310 140C340 140 356 140 364 148"/><path d="M240 218C240 246 240 250 240 262"/></g>')
    cloud = (f'<g transform="translate(404 6)"><path d="M12 30a10 10 0 0 1 2-19 14 14 0 0 1 27 4 8 8 0 0 1-1 15z" fill="{PANEL2}" stroke="{LINE}" stroke-width="2"/>'
             f'<text x="26" y="54" font-size="9" fill="{MUTE}" text-anchor="middle">Anywhere</text></g>')
    body = (laptop(170, 62, 140, 130) + phone(24, 42) + sheet(364, 100) + links + cloud +
            f'<g transform="translate(180 244)"><rect width="120" height="32" rx="8" fill="{PANEL2}" stroke="{LINE}"/>'
            f'<circle cx="18" cy="16" r="6" fill="{A}"/><text x="32" y="20" font-size="11" fill="{FG}">Sign everyone out</text></g>')
    return _svg("One clock shared to a laptop, a phone showing the live script with a Suggest button, and a crew cue sheet with Ready boxes, with an Anywhere link for people off site.", body)


def better_read():
    body = f'<rect x="22" y="14" width="436" height="272" rx="12" fill="{BG}" stroke="{LINE}" stroke-width="2"/>'
    body += f'<line x1="44" y1="30" x2="44" y2="270" stroke="{LINE}" stroke-dasharray="3 5"/><line x1="436" y1="30" x2="436" y2="270" stroke="{LINE}" stroke-dasharray="3 5"/>'
    # dimmed stanza above
    body += _lines(70, 32, [250, 226], 14, FG, .25, 7)
    # reading line and marker
    body += f'<path d="M30 112l16 10-16 10z" fill="{S}"/>'
    # active stanza, bold
    body += (f'<text x="70" y="124" font-size="19" font-weight="700" fill="{G}" font-family="Hanken Grotesk,sans-serif">CHOIR</text>'
             f'<text x="70" y="154" font-size="20" font-weight="600" fill="{FG}">Hold the line, the morning comes,</text>'
             f'<text x="70" y="180" font-size="20" font-weight="600" fill="{FG}">carried on a thousand drums,</text>'
             f'<text x="70" y="206" font-size="20" font-weight="600" fill="{FG}">every voice a rising sun.</text>')
    # stop marks in the margin
    for y, lab in [(112, "START"), (162, ""), (200, "LAST")]:
        body += (f'<g transform="translate(436 {y})"><rect x="6" y="0" width="3" height="16" fill="{S}"/><path d="M-2 0l8 8-8 8" fill="none" stroke="{S}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></g>')
        if lab:
            body += f'<text x="{428 - len(lab) * 7.6}" y="{y + 12}" font-size="9" font-weight="700" fill="{S}" letter-spacing="1">{lab}</text>'
    # next stanza waiting, dim
    body += _lines(70, 232, [236, 200], 14, FG, .25, 7)
    # pronunciation respelling
    body += f'<text x="232" y="154" font-size="0"></text>'
    body += f'<rect x="298" y="232" width="150" height="40" rx="8" fill="{PANEL2}" stroke="{LINE}"/><text x="310" y="249" font-size="10" fill="{MUTE}">Siobhan</text><text x="310" y="264" font-size="13" font-weight="700" fill="{A}">shi-VAWN</text>'
    # margin brackets
    body += (f'<g stroke="{MUTE}" stroke-width="1.4" fill="none"><path d="M22 280h22M22 276v8M44 276v8"/><path d="M436 280h22M436 276v8M458 276v8"/></g>')
    return _svg("The prompter text with a yellow reading marker beside the line being read, a stanza marked START and LAST in the margin with the next stanza dimmed below, wide margins, and a pronunciation respelling.", body)
