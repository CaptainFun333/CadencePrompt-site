import os

# ---- site structure -------------------------------------------------------
NAV = [("index.html", "Home"), ("features.html", "Features"), ("download.html", "Download"),
       ("help.html", "Help"), ("about.html", "About"), ("changelog.html", "Changelog"), ("support.html", "Support")]
CHEV = '<svg class="chev" viewBox="963 238 262 565" aria-hidden="true"><path fill="currentColor" d="M963 238L1225 521L963 803V606L1042 520L963 434Z"/></svg>'
SITE = "https://cadenceprompt.com/"


def page(fn, title, desc, body, cur=None):
    cur = cur or fn
    nav = "".join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == cur else "", t) for h, t in NAV)
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
        slug='prep', name='Prep', audiences='Operator · Crew',
        h1="From the writer's file to the prompter, in a fraction of the time.",
        lede='A whole new script lands the night before, and the crew waits in overtime while it is formatted. Scripts arrive in all kinds of states. Cadence takes the prep off your hands and keeps your own work safe when the rewrite comes.',
        card="From the writer's file to the prompter, in a fraction of the time.",
        feats=[
            ('Import & Prep', 'Raw script in, prompter-ready out.',
             'Bring in Word, PowerPoint or Keynote notes, PDF, Pages, Google Docs and Slides, or a shared folder on Drive, Dropbox, OneDrive or Box. One click finds the speakers, colors the stage directions and sweeps for cues, and one undo takes the whole run back. A script is ready to rehearse in a fraction of the time.',
             '', 'live'),
            ('Prepare script', 'One click, one undo.',
             'Prepare walks a script through six steps: set aside the production lines, clean up the spacing, find the speakers, color the stage directions and sweep for cues. Apply the sure ones all at once or look at each. Client profiles remember your choices for each client, and one undo takes the whole run back.',
             '', 'live'),
            ('Bring in a new version', 'The late rewrite stops costing a re-format.',
             'The client keeps editing their own document. When the new version arrives, Cadence shows what they changed, what you changed and what you both did, and your own edits survive. Nothing is applied silently, and Versions keeps every one and can put an earlier one back.',
             '', 'live'),
            ('Pictures in the script', "A slide's picture, beside its cue.",
             "Drop a picture into a line or onto a line of its own, and it scrolls with the words. Slide pictures from a folder put each slide's picture beside its cue, so the operator and the crew see what is on screen. Pictures carry through to Word and PDF.",
             '', 'live'),
            ('Script tools', 'Clean up a script in minutes.',
             'Convert paragraphs, strip to plain text, and find and replace across the script, while your styles and cues stay untouched.',
             'A before-and-after of a pasted script: raw text on the left, clean styled script with cues on the right.', 'live'),
        ]),
    dict(
        slug='run-the-show', name='Run the show', audiences='Operator',
        h1='Run the show with your hands on it.',
        lede='Everything the operator needs during the live moment is in the same place, so you can say yes to the last-minute change. Cadence runs without a Stream Deck. It runs best with one. Start with a mirrored screen and smooth scrolling, and grow into the full set of tools when the show calls for it.',
        card='Calm, fast control for the person at the desk.',
        feats=[
            ('Stream Deck', 'Hands-on control, built in.',
             'Cadence runs without a Stream Deck. It runs best with one. Set up and edit your rig inside Cadence: the keys, the pages and the dials, with the actions listed beside the deck. Any Stream Deck works for keys; a model with dials, the Stream Deck + or + XL, gives you speed, size and bookmarks under your fingers. Every key and dial has a function key or a button that does the same thing.',
             '', 'live'),
            ('Edit on the fly', 'There is no edit mode.',
             'Click anywhere and type while the script scrolls. Edit below the reading line and the prompter does not jump: the presenter sees the change when it gets there. Jump here sends the prompter to your cursor, so you can show the presenter exactly where.',
             '', 'live'),
            ('The live bar', 'Everything for the live moment.',
             'Play, speed, invert, prompt view and the armed indicator sit in one bar across the top. It looks the same whether you are running two screens or mirrored.',
             'The full operator window with the live bar clearly visible across the top.', 'live'),
            ('Command palette', 'Type what you want to do.',
             'Press Command-K and type. Cadence searches every action, shows where it lives and its shortcut, and runs it on Enter.',
             'The command palette open with a half-typed search and three results, each with its shortcut.', 'live'),
            ('Organized controls', 'Controls grouped by job.',
             'Prepare, Text, Prompter, Timer, Runlist, Collaboration, Show and Stream Deck each have a tab on the left rail, and the editor stays as large as possible.',
             'The ribbon with the Timer tab open beside the script.', 'live'),
            ('Any display setup', 'Works with the rig you have.',
             'Choose Auto, Extended or Mirrored, mirror or flip the picture, and invert it for a beam-splitter. A checklist helps you confirm everything before you go live.',
             'The Show tab with the three display-mode icons, plus the Before you go live checklist.', 'live'),
            ('Runlists', 'Many scripts, one continuous scroll.',
             'Line up the scripts for a whole event and let the reading flow from one into the next, with no stopping to load the next file. A key, a button or a shortcut jumps to the next script.',
             '', 'live'),
            ('Bookmarks', 'Hop to a place, and back up smoothly.',
             'Drop a bookmark at the cursor, hop between them, and see the whole list. If a presenter repeats a line, the speed passes through zero and the script scrolls backward without a jump.',
             '', 'live'),
            ('Never lose the script', 'A crash does not cost you the show.',
             'Cadence autosaves as you type to a recovery file, keeps a Backups folder, and keeps every version you bring in. Before you go live, a checklist walks through do not disturb, notifications and power.',
             '', 'live'),
        ]),
    dict(
        slug='time-and-cues', name='Time and cues', audiences='Crew · Presenter',
        h1='Everyone sees where the show is, and what is next.',
        lede='How much longer do they have? How long did that segment take? Now the whole crew can see for themselves, because timers and cues live in the script and everyone works from the same clock.',
        card='One clock and one cue list for the whole room.',
        feats=[
            ('Speaker timer', 'A clock the presenter can trust.',
             'The time remaining, the segment name, and an estimate that says plainly whether the segment is running over or under. The presenter never has to do the arithmetic.',
             'The speaker timer page: Time remaining as the large clock on the right half; real time, the estimate (for example -0:12), Coming up and pace on the left.', 'live'),
            ('Coming up', 'See the next cue before it arrives.',
             'A live list of the cues ahead of the reading line, each with the time until it. It moves up as the reading crosses each one, so crew know what is next without reading the script.',
             'The operator window with the Coming up list under the timer card, showing four or five cues in different colors with times.', 'live'),
            ('Timer cues in the script', 'Timer events fire from the script.',
             'Set, start and finish cues sit right in the text. An indicator on the live bar shows how many are armed and turns red if they are off, and pressing Play arms them, so a cue you scroll past starts the clock by itself. Pause disarms them and stops the clock. If a segment finishes with time to spare, the clock stops and turns green.',
             'Two crops of the live bar side by side: Armed 5 in green and OFF 5 in red. Optionally the green finished clock.', 'live'),
            ('Share the speaker timer', 'Put the clock on any screen.',
             'Switch on sharing and Cadence lists an address for each network you are on. Crew on the same venue network open it in a browser, with no extra cables or software. The Time remaining half is a clean clock that other systems can use.',
             'The Share on the network switch with the listed addresses and viewer count, next to the timer page open in a browser window.', 'live'),
            ('Cue colors', 'Cues you can read from across the room.',
             'Video, slides, general, audio and bookmarks each have a color from the start, and you can add custom cues of your own. Change any color to match how your crew already works.',
             'The script editor with all five cue types visible in a few lines of a realistic script.', 'live'),
            ('The cue sheet', 'The show as a rundown.',
             "View, then Cue sheet, lists every cue in the script as a rundown, and across a runlist, every script. Save it as a PDF or copy it. A stage manager's rundown, made from the script itself.",
             '', 'live'),
            ('Print, PDF and Word', 'A readable copy in a few clicks.',
             'Print the script, or save it as a PDF, a Word document or plain text, at a comfortable reading size, in print-safe colors, with each speaker named and page numbers in place. A whole runlist can go out as one PDF.',
             '', 'live'),
            ('Pull the script', 'The crew gets the current script without asking.',
             'With sharing on, the crew page has a Pull script button, protected by an Edit PIN, that hands over the script as a PDF, Word or text file on their own phone or laptop. No one has to ask the operator to send a file.',
             '', 'live'),
            ('Cue audiences', 'Show each person only what they need.',
             "Mark a cue for the crew, the presenter or both, so presenter-only direction stays off the crew's list.",
             '', 'soon'),
        ]),
    dict(
        slug='a-better-read', name='A better read', audiences='Presenter',
        h1='The best prompter is the one your presenter never notices.',
        lede='When the prompter does its job, the presenter connects with the audience instead of the screen. Style, margins, marker and speed are set once per presenter and saved.',
        card='Comfortable for the presenter, and every name said right.',
        feats=[
            ('Styles', 'Every speaker in their own style.',
             'Give each style a name, a color and a size. Lines pick up the style of whoever is speaking, and you can save your choices as the defaults for new scripts.',
             'The Styles sheet with three styles, their swatches and sizes, and the sample preview.', 'live'),
            ('The reading marker', 'A marker you can see and a line you can follow.',
             "Choose the marker's shape, side, color and size, and where the reading line sits. Save it as your default.",
             'The Marker and margins sheet showing the marker shape tiles, the swatches and the reading-line setting.', 'live'),
            ('Margins and alignment', 'Text set where the presenter wants it.',
             'Tight, Normal or Wide to start, or your own numbers for the left and right margins. Align the script left, centered or right.',
             'The margins settings in the Prompter tab, and the Text tab showing alignment.', 'live'),
            ('Back up smoothly', 'Go backward as easily as forward.',
             'Turn the speed past zero and the script scrolls backward, so a presenter can repeat a line without a jump.',
             'The live bar speed control, and a short screen recording of the script scrolling backward.', 'live'),
            ('Pronunciation helper', 'Hard names, said right the first time.',
             'Add a respelling for a name once, and it shows with the word in the script, the first time it appears or every time. Your list is kept, for the names and terms that trip people up.',
             '', 'live'),
            ('Per-presenter alignment', 'A different alignment for one presenter.',
             'Align a selection differently without changing the rest of the script.',
             '', 'soon'),
        ]),
]


# Real screenshots, by feature title: (file in assets/shots, alt text). A feature with no entry keeps its placeholder.
# All were captured from the app with a fictional sample script; see docs/screenshots in the Cadence repo.
SHOTS = {
    "Speaker timer": ("time-speaker-timer.png", "The speaker timer page: the time remaining as a large clock on the right with the next segment, and on the left the real time, Coming up with the time to each cue, and the pace."),
    "Coming up": ("time-coming-up.png", "Coming up in the operator window: audio, video and general cues, then the CEO keynote timer set and its slides, each with its kind, name and the time until it."),
    "Timer cues in the script": ("time-timer-cues.png", "The live bar indicator reading Armed in green, and the same indicator reading OFF in red when the cues are disarmed."),
    "Share the speaker timer": ("time-share.png", "The Collaboration tab with Share on the network and the View and Edit PINs, next to the speaker timer page it shares."),
    "Cue colors": ("time-cue-colors.png", "The script editor with a bookmark mark and general, audio, slide and video cues each in its own color, above a timer cue and the first lines of the script."),
    "Styles": ("read-speaker-styles.png", "The Styles sheet: each style with a name, color, size, alignment and spacing, the collection they belong to, and a sample at each speaker's color."),
    "The reading marker": ("read-marker.png", "The Marker group of the Prompter tab: the marker shapes, its side, its color, its size and the bookmark color."),
    "Margins and alignment": ("read-margins-alignment.png", "The Prompter tab with the text size, line spacing, the Normal and Custom margins with left and right numbers, and the settings new scripts start with."),
    "Back up smoothly": ("read-backward.mp4", "The script scrolling forward, then backward, as the speed passes through zero."),
    "The live bar": ("show-live-bar.png", "The full operator window with the live bar across the top: play, speed, zoom, the Armed indicator, bookmarks and page jumps."),
    "Command palette": ("show-palette.png", "The command palette open with find typed, listing the find commands, with their shortcuts."),
    "Organized controls": ("show-ribbon-timer.png", "The operator window with the Timer tab open at the left, beside the script, the preview and the timer card."),
    "Any display setup": ("show-display-checklist.png", "The Show tab with the Auto, Extended and Mirrored display buttons, and the Before you go live buttons, beside the Before you go live checklist."),
    "Import & Prep": ("prep-import-window.png", "The Import & Prep window with a raw client script pasted in: speaker names typed inline, notes in brackets and uneven spacing, with the steps Text, Prepare and Check along the top."),
    "Prepare script": ("prep-prepare-window.png", "The Prepare step of the Import & Prep window: six steps along the top, the step Clean up spacing with what it does, what to look at and its choices, and Apply and Next at the bottom."),
    "Bring in a new version": ("prep-new-version.png", "The Bring in a new version screen listing the client's changes, each marked Theirs or Same, with your script, the client's change and the result side by side."),
    "Pictures in the script": ("prep-pictures.png", "A slide's picture on a line of its own in the script, with the words of the script above and below it."),
    "Pronunciation helper": ("read-pronunciations.png", "The Pronunciations dialog."),
    "The cue sheet": ("time-cue-sheet.png", "The cue sheet: every cue of the script as a row with its planned time, kind and name, tick boxes, and segments with the pace they need."),
    "Print, PDF and Word": ("prep-print.png", "Page one of a printed script: speaker names above their lines, cues in boxes in print-safe colors, and the date and page number in the margins."),
    "Pull the script": ("time-pull-phone.png", "The pull page on a phone: the script now in the prompter with PDF, Word and Text buttons, and sections for a runlist and a crew folder."),
    "Never lose the script": ("show-checklist.png", "The Before you go live checklist: Do Not Disturb, notification settings, AirDrop and chat apps, each with a box to tick."),
    "Script tools": ("docs-before-after.png", "A script pasted in as it arrived, with speaker names and notes typed inline, next to the same passage after Prepare, with colored speakers and cues."),
}


def shot_media(title):
    src, alt = SHOTS[title]
    if src.endswith(".mp4"):
        poster = src.replace(".mp4", "-poster.png")
        return (f'<figure class="shotfig"><video autoplay loop muted playsinline controls preload="metadata" poster="assets/shots/{poster}" aria-label="{alt}">'
                f'<source src="assets/shots/{src}" type="video/mp4"></video></figure>')
    return f'<figure class="shotfig"><a href="assets/shots/{src}"><img src="assets/shots/{src}" alt="{alt}" loading="lazy"></a></figure>'


def feat_block(f):
    title, head, copy, shot, status = f
    badge = '<span class="badge">Coming soon</span>' if status == "soon" else ""
    media = (shot_media(title) if title in SHOTS else (ph("Capture: " + shot, 240) if shot else "")) if status == "live" else ""
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
    hero("You do not have to live with it.",
         "We keep putting up with the same prompter pain points because we assume they come with the job. They do not. Cadence Prompt is the prompter, rebuilt for the whole room: prep in minutes, run the show with your hands on it, and a crew that sees the same clock you do.") +
    f'<section class="wrap shot"><figure class="shotfig hero-shot"><a href="assets/shots/home-hero.png"><img src="assets/shots/home-hero.png" alt="The Cadence Prompt operator window: the live bar across the top, the ribbon at left, the script with colored speakers and cues, and the preview, timer card and Coming up in the side column."></a></figure></section>'
    '<section class="wrap live"><h2>Sound familiar?</h2><ul class="pains">'
    '<li>Hours of formatting a script by hand. <a href="prep.html">Import &amp; Prep takes it from raw to prompter-ready.</a></li>'
    '<li>A whole new script arrives, and you start over. <a href="prep.html">Version two arrives at five o\'clock. Fine.</a></li>'
    '<li>The crew asks how much longer, and nobody can say. <a href="time-and-cues.html">Now they can see it for themselves.</a></li>'
    '<li>A clunky control, and a quiet "why did it do that?" <a href="run-the-show.html">Your hands on it.</a></li></ul>'
    '<p class="built">I built Cadence Prompt after years of working around the same bugs. <a href="about.html">Read why &rarr;</a></p></section>'
    '<section class="wrap three"><h2>Three promises, one room</h2><div class="cols">'
    '<article><h3><a href="run-the-show.html">Operators</a></h3><p>Prep in minutes. Run the show with your hands on it. A clean interface built around the live bar, a command palette and Stream Deck control.</p></article>'
    '<article><h3><a href="a-better-read.html">Presenters</a></h3><p>Walk on knowing your words, your pace and your time: each speaker in their own style, a marker you can follow, and a clock you can trust.</p></article>'
    '<article><h3><a href="time-and-cues.html">Crews</a></h3><p>One show, one source of truth: timers, a live list of the cues coming up, and faster script handling that saves time and money.</p></article>'
    '</div></section>'
    '<section class="wrap prose"><h2>Run it with a Stream Deck.</h2><p>Cadence runs without a Stream Deck. It runs best with one. Keys for the tools you reach for, dials for speed, text size and bookmarks, a touch strip for the clock: your hands stay on the show. Any model works, the Stream Deck, XL, + and + XL, and the two with dials give you the full set. Every key and dial has a function key or a button that does the same thing.</p></section>'
    '<section class="wrap prose"><h2>Learn it on the prompter.</h2><p>Cadence Prompt teaches itself. Two Welcome scripts come with the app: you read them on the prompter and try each feature at a practice stop, with a Help search and a built-in manual behind them.</p>'
    '<figure class="shotfig"><img src="assets/shots/help-search.png" alt="Help search with cue sheet typed in: the matching commands, menu items and manual page, each with where to find it." loading="lazy"></figure></section>'
    f'<section class="wrap"><h2>What makes it different</h2><div class="cols">{pillar_cards}</div></section>'
    '<section class="wrap cta"><h2>Try it on your next show.</h2><p><a class="btn" href="download.html">' + CHEV + 'Download</a></p></section>')

P["features.html"] = ("Features | Cadence Prompt", "What Cadence Prompt does differently.",
    hero("What is different", "Four places to start, built around the three people in the room.", False) +
    '<section class="wrap stack">' + "".join(
        f'<article class="feat feat-text"><div><p class="eyebrow">{p["audiences"]}</p><h2><a href="{p["slug"]}.html">{p["name"]}</a></h2><p>{p["lede"]}</p>'
        f'<p><a class="link0" href="{p["slug"]}.html">See {p["name"].lower()} &rarr;</a></p></div></article>' for p in PILLARS) + "</section>")

P["download.html"] = ("Get Cadence Prompt | Cadence Prompt", "Ask for a beta access code for Cadence Prompt.",
    hero("Get Cadence Prompt", "Cadence Prompt is in beta, and a beta access code opens it. Ask for one and I will send it. [Price and trial length to decide.]", False) +
    f'<section class="wrap cols dl"><article><h2>Ask for a beta code</h2><p>Tell me your name and what you run, and I will send a code and the installer.</p><p><a class="btn" href="mailto:CadencePrompt@gmail.com?subject=Cadence%20Prompt%20beta%20code">{CHEV}Request a beta code</a></p><p class="note">Codes work offline and last for the beta.</p></article>'
    '<article><h2>Download the beta</h2><p>Get the installer for your computer, then ask for a code to open it.</p><ul><li><a href="https://github.com/CaptainFun333/CadencePrompt-site/releases/download/beta-0.1.1/Cadence-Prompt-0.1.1-Mac-Apple-Silicon.dmg">Mac, Apple Silicon (M1 and later)</a></li><li><a href="https://github.com/CaptainFun333/CadencePrompt-site/releases/download/beta-0.1.1/Cadence-Prompt-0.1.1-Mac-Intel.dmg">Mac, Intel</a></li><li><a href="https://github.com/CaptainFun333/CadencePrompt-site/releases/download/beta-0.1.1/Cadence-Prompt-0.1.1-Windows-Setup.exe">Windows</a></li></ul><p class="note">The beta installers are not signed yet, so your computer will warn you. On a Mac, right-click the app and choose Open the first time. On Windows, choose More info, then Run anyway.</p></article></section>'
    '<section class="wrap prose"><h2>What you need</h2><p>A Mac or a Windows computer. [Minimum versions to write.] A Stream Deck is not required: Cadence runs without one. It runs best with one.</p><h2>Trial and pricing</h2><p>Every feature is in the trial. After it, a subscription keeps Cadence Prompt supported and improving, and I will always be clear about what it pays for. [Price and trial length to decide.]</p></section>')
P["help.html"] = ("Help | Cadence Prompt", "Get started and find answers.",
    hero("Help", "Start here. The full manual will grow from the in-app help.", False) +
    '<section class="wrap cols"><article><h3>Quick start</h3><p>[5 steps from script to show]</p></article><article><h3>Stream Deck</h3><p>[setup]</p></article><article><h3>Timers and cues</h3><p>[how they work]</p></article><article><h3>Keyboard shortcuts</h3><p>[the key map]</p></article></section>')
P["changelog.html"] = ("Changelog | Cadence Prompt", "What changed in each version.",
    hero("Changelog", "Every release, in plain language.", False) + '<section class="wrap prose"><h2>[version] · [date]</h2><ul><li>[note]</li></ul><p class="note">Generated from the app changelog at release time.</p></section>')
P["support.html"] = ("Support | Cadence Prompt", "Contact and support.",
    hero("Support", "Tell us what you ran into.", False) + '<section class="wrap prose"><p>Email <a href="mailto:CadencePrompt@gmail.com">CadencePrompt@gmail.com</a>. Include your version and what you were doing.</p><p>Tell me what is working and what needs fixing. If it needs fixing, Ready to make it right. Share your wins too: they tell me what to protect.</p><p class="note">Move to support@cadenceprompt.com once domain email is set up.</p></section>')
P["about.html"] = ("About | Cadence Prompt", "Why Cadence Prompt exists.",
    hero("Why I built Cadence Prompt", "Eighteen years of shows, and one tool I kept working around.", False) +
    '<section class="wrap prose"><p class="note">Draft in Brad\'s voice, built from the founder survey. To rewrite in his own words before it goes live.</p>'
    '<p>I have worked in live events for eighteen years. I started by cleaning the office of a neighbor who ran a teleprompter company, and I ended up running graphics and media servers on shows of every size. I still run prompter today.</p>'
    '<p>The software I used most was a great tool once. Over the years I learned its bugs by heart. I built shortcuts around them with a Stream Deck and a pile of macros. Then I caught myself building tools to make a broken tool work, and I decided to build the right tool instead.</p>'
    '<p>The first thing I fixed was coloring text. It took five clicks for every cue. Now it takes one. That is how Cadence Prompt started: one small, annoying thing, fixed for real.</p>'
    '<h2>What I am here to do</h2>'
    '<p>To make events better for presenters, operators and crews, so much better that none of them can imagine a show without the ease and connectedness Cadence Prompt brings.</p>'
    '<p>I want a prompter as good for the crew behind the scenes as it is for the presenter on stage. If it does its job, nobody notices it. I am not trying to be the loudest tool in the room. I want to be the one that is there, every show, doing what I said it would.</p>'
    '<h2>What I hold to</h2>'
    '<ul class="values">'
    '<li><strong>Accuracy before speed.</strong> A late change is only fast if it is right. Cadence shows you what changed and applies nothing silently.</li>'
    '<li><strong>Calm in the moment.</strong> The screen should never add to the pressure.</li>'
    '<li><strong>Every seat in the room matters.</strong> The operator, the presenter and the crew each get something built for them.</li>'
    '<li><strong>Honest by default.</strong> If it is not built, it says coming soon. If it is a claim, it is checked.</li>'
    '<li><strong>Built from real shows.</strong> Every feature starts with a problem someone lived.</li>'
    '<li><strong>Solve what you thought you had to live with.</strong> Add value without being asked.</li></ul>'
    '<h2>What I will do for you</h2>'
    '<p>Tell me what is working and what needs fixing. Ready to make it right. Share your wins too: they tell me what to protect.</p></section>')
P["privacy.html"] = ("Privacy | Cadence Prompt", "What Cadence Prompt keeps, what leaves your computer, and what the optional Anywhere service handles.", hero("Privacy", "Cadence Prompt works on your computer. Nothing leaves it unless you switch something on. Last updated 11 November 2026.", False) + """<section class="wrap prose">
<h2>The app on your computer</h2>
<p>Your scripts, run sheets, pictures, settings and cue lists stay on your computer. Cadence Prompt does not send usage statistics, and an access code is checked on your computer, without contacting anyone.</p>
<p>Two things reach the internet only when you ask. If you import from a Google Docs or Drive link, Cadence fetches that link from Google. If you switch on Anywhere (below), the show goes through the online service.</p>
<h2>Sharing on the venue network</h2>
<p>When you switch on sharing, other devices on the same network can open the crew pages from your computer. That traffic stays on the local network and does not go through any service of mine.</p>
<h2>Anywhere (optional)</h2>
<p>Anywhere lets people who are not on the venue network open the crew pages (the clocks and, if you choose, the script) from a link or QR code. It is off every time Cadence starts. Nothing goes anywhere until you switch it on.</p>
<h3>What passes through the service</h3>
<ul>
<li>While someone is watching from outside: the timer clocks and segment names. The script text and the place you are reading go through only if Share the script text is on.</li>
<li>From viewers: ticks and notes on the cue sheet (with the Edit PIN), and suggestions on lines (with the Notes or Edit PIN).</li>
<li>PINs are kept only as salted hashes. The service cannot tell you a PIN and cannot recover one.</li>
<li>For each access code and month, the service keeps only counts: shows opened, viewers let in, and minutes. It keeps no content, no names, and no addresses of viewers.</li>
</ul>
<h3>What is not kept</h3>
<ul>
<li>The show is removed when you switch Anywhere off or quit Cadence, and by an automatic clean-up within a few minutes if Cadence goes quiet. The clock data is removed as soon as the last outside viewer leaves.</li>
<li>I do not log or read the content. While a show runs it is held by Google's Firebase (Realtime Database and Cloud Functions, in the United States), under Google's own terms. The service passes through Google's servers.</li>
</ul>
<h3>What you are responsible for</h3>
<ul>
<li>You decide what to share and with whom. Share the link and PINs only with your crew. Anyone who has the link and a PIN can see what that PIN allows, until you switch Anywhere off.</li>
<li>Four-digit PINs are a convenience, not strong security. After eight wrong guesses in five minutes a show refuses further guesses for the rest of that window, and a show lets in 15 viewers at once. Do not put secrets in a script you share this way.</li>
<li>Anywhere is provided as is. It can be unavailable, and sharing on the venue network keeps working without it.</li>
<li>An access code may be refused for misuse, or when the online services included with it have ended. The app itself keeps working.</li>
</ul>
<h2>This website</h2>
<p>This site is hosted on GitHub Pages, which may keep ordinary server logs of visits. It loads its fonts from Google Fonts. It has no analytics and sets no cookies of its own.</p>
<h2>Questions</h2>
<p>Write to <a href="mailto:CadencePrompt@gmail.com">CadencePrompt@gmail.com</a> with a question or a request to remove something.</p>
</section>""")
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
