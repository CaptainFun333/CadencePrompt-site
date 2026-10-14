import os

# ---- site structure -------------------------------------------------------
NAV = [("index.html", "Home"), ("features.html", "Features"), ("download.html", "Download"),
       ("help.html", "Help"), ("about.html", "About"), ("changelog.html", "Changelog"), ("support.html", "Support")]
CHEV = '<svg class="chev" viewBox="963 238 262 565" aria-hidden="true"><path fill="currentColor" d="M963 238L1225 521L963 803V606L1042 520L963 434Z"/></svg>'
SITE = "https://cadenceprompt.com/"


def page(fn, title, desc, body, cur=None):
    cur = cur or fn
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{t}</a>' for h, t in NAV)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="icon" href="assets/cp-mark-small-white.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@600;700&family=Hanken+Grotesk:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&display=swap">
<link rel="stylesheet" href="style.css"></head><body>
<div class="readline" aria-hidden="true"><svg viewBox="963 238 262 565"><path fill="currentColor" d="M963 238L1225 521L963 803V606L1042 520L963 434Z"/></svg></div>
<header class="top"><div class="wrap bar"><a class="logo" href="index.html" aria-label="Cadence Prompt home"><img src="assets/cadence-prompt-horizontal-white.svg" alt="Cadence Prompt" height="34"></a>
<nav aria-label="Main">{nav}</nav><a class="btn small" href="download.html">Download</a></div></header>
<main>{body}</main>
<footer><div class="wrap foot"><span>&copy; 2026 Cadence Prompt</span><span><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="mailto:CadencePrompt@gmail.com">CadencePrompt@gmail.com</a></span></div></footer>
</body></html>
'''


def ph(label, h=320):
    # The placeholder doubles as the shot list: it says exactly what to capture.
    return f'<div class="ph" style="min-height:{h}px"><span>SCREENSHOT TO CAPTURE</span>{label}</div>'


def hero(h, sub, cta=True, eyebrow=""):
    e = f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ""
    c = (f'<p><a class="btn" href="download.html">{CHEV}Try Cadence Prompt</a> '
         f'<a class="link" href="features.html">See what is different</a></p>') if cta else ""
    return f'<section class="hero"><div class="wrap">{e}<h1>{h}</h1><p class="sub">{sub}</p>{c}</div></section>'


# ---- the four pillars ------------------------------------------------------
# Each feature: (title, headline, copy, shot-description, status) with status "live" or "soon".
# "soon" features are shown with a Coming soon badge and no screenshot.
PILLARS = [
    dict(
        slug="time-and-cues", name="Time and cues", audiences="Crew · Presenter",
        h1="Everyone sees where the show is, and what is next.",
        lede="How much longer do they have? How long did that segment take? Now the whole crew can see for themselves, because timers and cues live in the script and everyone works from the same clock.",
        card="One clock and one cue list for the whole room.",
        feats=[
            ("Speaker timer", "A clock the presenter can trust.",
             "The time remaining, the segment name, and an estimate that says plainly whether the segment is running over or under. The presenter never has to do the arithmetic.",
             "The speaker timer page: Time remaining as the large clock on the right half; real time, the estimate (for example -0:12), Coming up and pace on the left.", "live"),
            ("Coming up", "See the next cue before it arrives.",
             "A live list of the cues ahead of the reading line, each with the time until it. It moves up as the reading crosses each one, so crew know what is next without reading the script.",
             "The operator window with the Coming up list under the timer card, showing four or five cues in different colors with times.", "live"),
            ("Timer cues in the script", "Timer events fire from the script.",
             "Set, start and finish cues sit right in the text. An indicator on the live bar shows how many are armed and turns red if they are off, and Cadence can arm them for you when you press Play. If a segment finishes with time to spare, the clock stops and turns green.",
             "Two crops of the live bar side by side: Armed 5 in green and OFF 5 in red. Optionally the green finished clock.", "live"),
            ("Share the speaker timer", "Put the clock on any screen.",
             "Switch on sharing and Cadence lists an address for each network you are on. Crew open it in a browser, with no extra cables or software. The Time remaining half is a clean clock that other systems can use.",
             "The Share on the network switch with the listed addresses and viewer count, next to the timer page open in a browser window.", "live"),
            ("Cue colors", "Cues you can read from across the room.",
             "Video, slides, general, audio and bookmarks each have a color from the start, and you can change any of them to match how your crew already works.",
             "The script editor with all five cue types visible in a few lines of a realistic script.", "live"),
            ("Cue audiences", "Show each person only what they need.",
             "Mark a cue for the crew, the presenter or both, so presenter-only direction stays off the crew's list.",
             "", "soon"),
        ]),
    dict(
        slug="a-better-read", name="A better read", audiences="Presenter",
        h1="The best prompter is the one your presenter never notices.",
        lede="When the prompter does its job, the presenter connects with the audience instead of the screen. Style, margins, marker and speed are set once per presenter and saved.",
        card="Comfortable for the presenter, and every name said right.",
        feats=[
            ("Speaker styles", "Every speaker in their own style.",
             "Give each speaker a name, a color and a size. Lines pick up the style of whoever is speaking, and you can save your choices as the defaults for new scripts.",
             "The Speaker styles sheet with three speakers, their swatches and sizes, and the sample preview.", "live"),
            ("The reading marker", "A marker you can see and a line you can follow.",
             "Choose the marker's shape, side, color and size, and where the reading line sits. Save it as your default.",
             "The Marker and margins sheet showing the marker shape tiles, the swatches and the reading-line setting.", "live"),
            ("Margins and alignment", "Text set where the presenter wants it.",
             "A comfortable normal margin, or your own numbers with a live miniature. Align the script left, centered or right.",
             "The margins area of the sheet with the live miniature, and the Text tab showing alignment.", "live"),
            ("Back up smoothly", "Go backward as easily as forward.",
             "Turn the speed past zero and the script scrolls backward, so a presenter can repeat a line without a jump.",
             "The live bar speed control, and a short screen recording of the script scrolling backward.", "live"),
            ("Pronunciation helper", "Hard names, said right the first time.",
             "Add a phonetic spelling once and it shows with the word in the script, for the names and terms that trip people up.",
             "", "soon"),
            ("Per-presenter alignment", "A different alignment for one presenter.",
             "Align a selection differently without changing the rest of the script.",
             "", "soon"),
        ]),
    dict(
        slug="run-the-show", name="Run the show", audiences="Operator",
        h1="One surface to run the whole event.",
        lede="Everything the operator needs during the live moment is in the same place, so you can say yes to the last-minute change. Start with a mirrored screen and smooth scrolling, and grow into the full set of tools when the show calls for it.",
        card="Calm, fast control for the person at the desk.",
        feats=[
            ("The live bar", "Everything for the live moment.",
             "Play, speed, invert, prompt view and the armed indicator sit in one bar across the top. It looks the same whether you are running two screens or mirrored.",
             "The full operator window with the live bar clearly visible across the top.", "live"),
            ("Command palette", "Type what you want to do.",
             "Press Command-K and type. Cadence searches every action, shows where it lives and its shortcut, and runs it on Enter.",
             "The command palette open with a half-typed search and three results, each with its shortcut.", "live"),
            ("Organized controls", "Controls grouped by job.",
             "Text, Prompter, Timer, Show and Stream Deck each have a tab, and the editor stays as large as possible.",
             "The ribbon with the Timer tab open beside the script.", "live"),
            ("Stream Deck", "Hands-on control, built in.",
             "Set up and edit your Stream Deck rig inside Cadence: the keys, the pages and the dials, with the actions listed beside the deck.",
             "The Stream Deck tab showing the action list, the key grid and the inspector for one key.", "live"),
            ("Any display setup", "Works with the rig you have.",
             "Choose Auto, Extended or Mirrored, mirror or flip the picture, and invert it for a beam-splitter. A checklist helps you confirm everything before you go live.",
             "The Show tab with the three display-mode icons, plus the Before you go live checklist.", "live"),
            ("Runlists", "Many scripts, one continuous scroll.",
             "Line up the scripts for a whole event and let the reading flow from one into the next, with no stopping to load the next file.",
             "", "soon"),
        ]),
    dict(
        slug="documents-in-documents-out", name="Documents in, documents out", audiences="Crew",
        h1="From the writer's document to the prompter, and back to paper.",
        lede="A whole new script lands the night before, and the crew waits in overtime while it is formatted. Scripts arrive in all kinds of states, and clients still need readable copies back. Part of this is here today. The rest is coming, and marked as such.",
        card="No retyping between the writers' file and the prompter.",
        feats=[
            ("Script tools", "Clean up a script in minutes.",
             "Convert paragraphs, strip to plain text, and find and replace across the script, while your speaker styles and cues stay untouched.",
             "A before-and-after of a pasted script: raw text on the left, clean speaker-styled script with cues on the right.", "live"),
            ("Script pull", "Pull the client's latest, and keep your work.",
             "Clients keep editing their own document. When you press Pull, Cadence brings in the latest, formats it, and merges only what changed. Every conflict and every deletion is flagged for you to review, so nothing is merged silently. Each pull is stamped, and a copy is kept in the shared folder.",
             "", "soon"),
            ("Script formatter", "Raw script in, prompter-ready out.",
             "Speakers, cues and paragraph breaks are set for you, so a script is ready to rehearse in a fraction of the time.",
             "", "soon"),
            ("Quick export", "A readable copy in one step.",
             "Export a Word or PDF copy at a comfortable reading size, in print-friendly colors, with each speaker named and page numbers in place, and save it back to the shared folder.",
             "", "soon"),
            ("Quick print", "Paper when you need it.",
             "One action prints the script in a readable layout, with the same settings as your last export.",
             "", "soon"),
        ]),
]


def feat_block(f):
    title, head, copy, shot, status = f
    badge = '<span class="badge">Coming soon</span>' if status == "soon" else ""
    media = ph("Capture: " + shot, 240) if (status == "live" and shot) else ""
    cls = "feat" if media else "feat feat-text"
    return (f'<article class="{cls}"><div><p class="eyebrow">{title}{badge}</p><h2>{head}</h2><p>{copy}</p></div>{media}</article>')


def pillar_page(i, p):
    prev_ = PILLARS[i - 1] if i > 0 else None
    next_ = PILLARS[i + 1] if i < len(PILLARS) - 1 else None
    pager = '<nav class="pager wrap" aria-label="More features">'
    pager += f'<a href="{prev_["slug"]}.html">&larr; {prev_["name"]}</a>' if prev_ else "<span></span>"
    pager += f'<a href="{next_["slug"]}.html">{next_["name"]} &rarr;</a>' if next_ else '<a href="features.html">All features</a>'
    pager += "</nav>"
    body = (hero(p["h1"], p["lede"], False, f'<a class="crumb" href="features.html">Features</a> / {p["name"]} · {p["audiences"]}') +
            '<section class="wrap stack">' + "".join(feat_block(f) for f in p["feats"]) + "</section>" +
            '<section class="wrap cta"><h2>Try it on your next show.</h2><p><a class="btn" href="download.html">' + CHEV + 'Download</a></p></section>' + pager)
    return (p["slug"] + ".html", f'{p["name"]} | Cadence Prompt', p["lede"], body)


P = {}
for i, p in enumerate(PILLARS):
    fn, t, d, b = pillar_page(i, p)
    P[fn] = (t, d, b)

pillar_cards = "".join(
    f'<article><p class="eyebrow">{p["audiences"]}</p><h3><a href="{p["slug"]}.html">{p["name"]}</a></h3><p>{p["card"]}</p></article>' for p in PILLARS)

P["index.html"] = ("Cadence Prompt: teleprompter software for the whole show",
    "Teleprompter software built for the presenter, the operator and the crew.",
    hero("The prompter, rebuilt for the whole room.",
         "We keep putting up with the same prompter pain points because we assume they come with the job. They do not. Cadence Prompt gives operators a better interface, presenters a better read, and crews timers and cues in one place.") +
    f'<section class="wrap shot">{ph("Capture: the full operator window, with a realistic script open, the live bar across the top, the ribbon at left, and the preview, timer card and Coming up in the side column. This is the hero image.", 420)}</section>'
    '<section class="wrap live"><h2>You do not have to live with it.</h2><ul class="pains">'
    '<li>Hours of formatting a script by hand.</li><li>A whole new script arrives, and you start over.</li>'
    '<li>The crew asks how much longer, and nobody can say.</li><li>A clunky control, and a quiet "why did it do that?"</li></ul>'
    '<p class="built">I built Cadence Prompt after years of working around the same bugs. <a href="about.html">Read why &rarr;</a></p></section>'
    '<section class="wrap three"><h2>A win for everyone in the room</h2><div class="cols">'
    '<article><h3><a href="run-the-show.html">Operators</a></h3><p>Be the operator the producer wants on every show: a clean interface built around the live bar, a command palette and Stream Deck control.</p></article>'
    '<article><h3><a href="a-better-read.html">Presenters</a></h3><p>A better read: each speaker in their own style, a marker you can follow, and a clock you can trust.</p></article>'
    '<article><h3><a href="time-and-cues.html">Production crews</a></h3><p>Integrated timers, a live list of the cues coming up, and faster script handling that saves time and money.</p></article>'
    '</div></section>'
    f'<section class="wrap"><h2>What makes it different</h2><div class="cols">{pillar_cards}</div></section>'
    '<section class="wrap cta"><h2>Try it on your next show.</h2><p><a class="btn" href="download.html">' + CHEV + 'Download</a></p></section>')

P["features.html"] = ("Features | Cadence Prompt", "What Cadence Prompt does differently.",
    hero("What is different", "Four ideas, each built around the people in the room.", False) +
    '<section class="wrap stack">' + "".join(
        f'<article class="feat feat-text"><div><p class="eyebrow">{p["audiences"]}</p><h2><a href="{p["slug"]}.html">{p["name"]}</a></h2><p>{p["lede"]}</p>'
        f'<p><a class="link0" href="{p["slug"]}.html">See {p["name"].lower()} &rarr;</a></p></div></article>' for p in PILLARS) + "</section>")

P["download.html"] = ("Download | Cadence Prompt", "Download Cadence Prompt for Mac and Windows.",
    hero("Download Cadence Prompt", "Try every feature free for [N days]. Then subscribe to keep going. [Price and trial length to decide.]", False) +
    f'<section class="wrap cols dl"><article><h2>Mac</h2><p class="mono">macOS [min version] · [size]</p><p><a class="btn" href="#">{CHEV}Download .dmg</a></p><p class="note">Link goes to the latest release when builds exist.</p></article>'
    f'<article><h2>Windows</h2><p class="mono">Windows [min version] · [size]</p><p><a class="btn" href="#">{CHEV}Download installer</a></p><p class="note">Installer format to decide.</p></article></section>'
    '<section class="wrap prose"><h2>Install</h2><ol><li>[step]</li><li>[step]</li></ol><h2>System requirements</h2><p>[to write]</p><h2>Trial and pricing</h2><p>Every feature is in the trial. After it, a subscription keeps Cadence Prompt supported and improving, and I will always be clear about what it pays for. [Price and trial length to decide.]</p></section>')
P["help.html"] = ("Help | Cadence Prompt", "Get started and find answers.",
    hero("Help", "Start here. The full manual will grow from the in-app help.", False) +
    '<section class="wrap cols"><article><h3>Quick start</h3><p>[5 steps from script to show]</p></article><article><h3>Stream Deck</h3><p>[setup]</p></article><article><h3>Timers and cues</h3><p>[how they work]</p></article><article><h3>Keyboard shortcuts</h3><p>[the key map]</p></article></section>')
P["changelog.html"] = ("Changelog | Cadence Prompt", "What changed in each version.",
    hero("Changelog", "Every release, in plain language.", False) + '<section class="wrap prose"><h2>[version] · [date]</h2><ul><li>[note]</li></ul><p class="note">Generated from the app changelog at release time.</p></section>')
P["support.html"] = ("Support | Cadence Prompt", "Contact and support.",
    hero("Support", "Tell us what you ran into.", False) + '<section class="wrap prose"><p>Email <a href="mailto:CadencePrompt@gmail.com">CadencePrompt@gmail.com</a>. Include your version and what you were doing.</p><p>Tell me what is working and what needs fixing. If it needs fixing, I will fix it. Share your wins too: they tell me what to protect.</p><p class="note">Move to support@cadenceprompt.com once domain email is set up.</p></section>')
P["about.html"] = ("About | Cadence Prompt", "Why Cadence Prompt exists.",
    hero("Why I built Cadence Prompt", "Eighteen years of shows, and one tool I kept working around.", False) +
    '<section class="wrap prose"><p class="note">Draft in Brad\'s voice, built from the founder survey. To rewrite in his own words before it goes live.</p>'
    '<p>I have worked in live events for eighteen years. I started by cleaning the office of a neighbor who ran a teleprompter company, and I ended up running prompters, graphics and media servers on shows of every size. Today I run prompter full time.</p>'
    '<p>The software I used most was a great tool once. Over the years I learned its bugs by heart. I built shortcuts around them with a Stream Deck and a pile of macros. Then I caught myself building tools to make a broken tool work, and I decided to build the right tool instead.</p>'
    '<p>The first thing I fixed was coloring text. It took five clicks for every cue. Now it takes one. That is how Cadence Prompt started: one small, annoying thing, fixed for real.</p>'
    '<h2>What I believe</h2>'
    '<p>A prompter should help three people at once: the operator at the desk, the presenter on stage, and the crew who need to know what is coming. It should keep up with last-minute changes, tell the crew how much longer, and get out of the presenter\'s way. If it does its job, nobody notices it.</p>'
    '<p>I am not trying to be the loudest tool in the room. I want to be the one that is there, every show, doing what I said it would.</p>'
    '<h2>What I will do for you</h2>'
    '<p>Tell me what is working and what needs fixing. I will fix it.</p></section>')
P["privacy.html"] = ("Privacy | Cadence Prompt", "Privacy policy.", hero("Privacy", "[Policy to write before launch.]", False))
P["terms.html"] = ("Terms | Cadence Prompt", "Terms of use.", hero("Terms", "[Terms to write before launch.]", False))

# pillar pages highlight "Features" in the nav
for fn, (t, d, b) in P.items():
    cur = "features.html" if fn in [p["slug"] + ".html" for p in PILLARS] else fn
    open(fn, "w").write(page(fn, t, d, b, cur))

open("CNAME", "w").write("cadenceprompt.com\n")
open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
open(".nojekyll", "w").write("")
urls = "".join(f"<url><loc>{SITE}{'' if fn == 'index.html' else fn}</loc></url>" for fn in sorted(P))
open("sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
print(len(P), "pages")
