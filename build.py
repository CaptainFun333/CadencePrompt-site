import hashlib
import os
import art
ART = {'prep': art.prep, 'run-the-show': art.run_show, 'time-and-cues': art.time_cues, 'a-better-read': art.better_read}

# ---- site structure -------------------------------------------------------
NAV = [("index.html", "Home"), ("features.html", "Features"), ("learn.html", "Learn"), ("download.html", "Download"),
       ("help.html", "Help"), ("about.html", "About"), ("changelog.html", "Changelog"), ("support.html", "Support")]
CHEV = '<svg class="chev" viewBox="963 238 262 565" aria-hidden="true"><path fill="currentColor" d="M963 238L1225 521L963 803V606L1042 520L963 434Z"/></svg>'
SITE = "https://cadenceprompt.com/"
CSS_V = hashlib.md5(open("style.css", "rb").read()).hexdigest()[:8]   # a changed stylesheet gets a new address, so no one keeps the old one


NOINDEX = {"send-a-script.html"}      # built and reachable by its address, but unlinked and kept out of search while the page is developed


def page(fn, title, desc, body, cur=None):
    cur = cur or fn
    robots = '<meta name="robots" content="noindex">' if fn in NOINDEX else ""
    nav = "".join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == cur else "", t) for h, t in NAV)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">{robots}
<link rel="icon" href="assets/cp-mark-small-white.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@600;700&family=Hanken+Grotesk:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&display=swap">
<link rel="stylesheet" href="style.css?v={CSS_V}"></head><body>
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
         f'<a class="link" href="features.html">See what&rsquo;s different</a></p>') if cta else ""
    return f'<section class="hero"><div class="wrap">{e}<h1>{h}</h1><p class="sub">{sub}</p>{c}</div></section>'


# ---- the four pillars ------------------------------------------------------
# Each feature: (title, headline, copy, shot-description, status) with status "live" or "soon".
# "soon" features are shown with a Coming soon badge and no screenshot.
# "beta" features are built but not yet tried by hand: a Beta badge, no screenshot yet.
PILLARS = [
    dict(
        slug='prep', name='Prep', audiences='Operator · Crew',
        h1="From the writer's file to the prompter, in a fraction of the time.",
        lede="A brand-new script lands the night before, and the crew sits in overtime while it gets formatted. Scripts arrive in every shape imaginable. Cadence takes the repetitive prep off your hands and protects your work when the late rewrite hits.",
        card="From the writer's rough doc to show-ready script, in a fraction of the time.",
        feats=[
            ('Import & Prep', 'Raw script in, show-ready out.',
             "Bring in Word docs, PowerPoint or Keynote speaker notes, PDFs, Pages files, Google Docs and Slides, or a shared folder on Drive, Dropbox, OneDrive, or Box. One click finds the speakers, colors the stage directions, and sweeps for cues. One undo takes the entire pass back. A script is ready to rehearse in a fraction of the time, and each import opens in its own tab so multiple files can sit side by side.",
             '', 'live'),
            ('Insert from another script', 'Borrow lines from an older script.',
             "Open an earlier script in a read-only viewer right beside the one you're editing. Find the lines you need, copy them, and paste them straight across. Cues and speaker styles come along for the ride, and Cadence only asks about slide numbering if the sequence doesn't already line up. Reads Word, PowerPoint, Keynote, Pages, PDF, and Telescript.",
             '', 'beta'),
            ('Prepare tab', 'One click, one undo, for every file.',
             "Prepare lives in its own tab right beside your script. Walk through each of the six clean-up steps: Set aside, Spacing, Readability, Speakers, Stage directions, and Cues. Apply the sure findings to every file at once or step through them individually. Anything Cadence isn't sure about goes to a short review list instead of changing behind your back. Send files into your script one at a time or all at once, in order. Client profiles remember your preferences for each recurring client, and one undo rolls the entire pass back.",
             '', 'beta'),
            ('Bring in a new version', 'The late rewrite stops costing a full re-format.',
             "Let the client keep editing their own document. When the new draft lands, it opens in its own tab. Cadence shows you exactly what they changed, what you changed, and where you both edited the same line. Your prep work survives, nothing gets applied silently, and Versions keeps every draft on file so you can roll back anytime.",
             '', 'live'),
            ('Pictures in the script', 'See every slide right beside its cue.',
             "Drop any image inline or onto its own line, and it scrolls smoothly alongside the words. Pull slide thumbnails from a folder, or import a PowerPoint or Keynote deck__BETA__ to attach each slide image straight to its matching Slide cue. A slide range cue covers slides without spoken script, and bringing in a new version of the deck matches slides one by one. You, the presenter, and the crew always know what's on screen, and every picture carries cleanly through to Word and PDF exports.",
             '', 'live'),
            ('More than one language', 'One script per language, one click to choose.',
             "Clients send multilingual scripts three ways: a Word table with one column per language, one section per language in a single file, or a separate file for each. Cadence detects the languages, asks which one to import (or builds a script for each), and flags anything it left out, like footnotes or mixed-language lines. Slide images sitting in a column beside the text can become Slide-cue pictures automatically.",
             '', 'beta'),
            ('Master script', 'Multiple scripts, one master document.',
             "Stitch every script for an event into a single document, complete with a segment cue and a named bookmark for each. Number them in your runlist, or let the crew tap the rows they need on the pull page to download one combined PDF, Word, or plain text master.",
             '', 'beta'),
            ('Script tools', 'Clean up a script in minutes.',
             'Convert paragraphs, strip to plain text, and run find and replace across your script while keeping every speaker style and cue completely untouched.',
             'A before-and-after of a pasted script: raw text on the left, clean styled script with cues on the right.', 'live'),
        ]),
    dict(
        slug='run-the-show', name='Run the show', audiences='Operator',
        h1='Run the show with your hands on it.',
        lede="Everything you need in the live moment sits in one place, so you can say yes to the last-minute change. Cadence runs great without a Stream Deck, but best with one. It never sacrifices a smooth scroll. Start with what you already know, and pick up the full toolkit as you go. Whenever a show calls for something new, the built-in Learn series will walk you through it.",
        card="Calm, tactile control built for the person sitting behind the console.",
        feats=[
            ('The live bar', 'Everything for the live moment.',
             "One clean bar across the top handles everything that moves the prompter: Play, Speed, bookmark stepping, cue to cue, page jumps, Jump here, Snap back and Snap next, and Zoom, with Top and End marked in red at the far right. The Armed indicator sits right above the script. The tools that change the script at your cursor (Add cue, Segment +, the timer cues, Add bookmark, Bookmark list, Q2Q stops, and Number Slides) live in a separate bar along the bottom, so your live controls stay clear of accidental clicks.",
             'Both bars of the operator window in one picture, the top bar labeled moves the prompter and the bottom bar labeled changes the script at your cursor.', 'live'),
            ('Stream Deck', 'Hands-on control, built right in.',
             "Build and edit your rig right inside Cadence: keys, pages, and dials, with every available action listed beside your deck. You'll want a Stream Deck + or + XL for the dials, which put speed, text size, and bookmarks right under your fingers, though any model works for keys. Keys are color-framed by category, and the Plus XL comes with a one-page starter layout ready to go. Rearrange it however you like: the pictures show a Stream Deck + and a + XL set up the way I run them. If you're ever traveling light, nearly every key has a shortcut, a menu row, or an on-screen button that does the same thing.",
             'A Stream Deck + beside a Stream Deck + XL, both set up for Cadence.', 'live'),
            ('Edit on the fly', 'There is no edit mode.',
             "Click anywhere and start typing, even while the script is actively scrolling. Edit below the reading line and the prompter won't jump an inch. The presenter simply sees the updated words when they get there. Hit Jump here on the top bar to snap the prompter straight to your cursor and show the presenter an exact spot.",
             'The editor with a new edit in it and the Editor \u00b7 held strip showing the Resume following button.', 'live'),
            ('One search box', 'Just type what you want to do.',
             "Press Command-K (or click Search on the bottom bar) and start typing. Cadence searches every action, menu item, and manual page at once, shows you where it lives and its shortcut, and runs it when you hit Enter. Settings open right in place, so you never have to go hunting through drawers. It even forgives small slips like \"and\" for \"&\", missing hyphens or words run together.",
             'The command palette open with a half-typed search and three results, each with its shortcut.', 'live'),
            ('Organized controls', 'Tools grouped by the job.',
             "Prepare, Text, Prompter, Timer, Runlist, Collaboration, Show, and Controllers each live in their own drawer along the left rail, keeping your editor as big as possible. The menu bar mirrors those drawers, every setting shows its scope (this script, this computer, or new scripts), and a click on the reset arrow puts a changed setting right back. File \u25b8 Defaults compares every setting against your defaults and Cadence's own. The Show, Timer, Prompter, and Controllers menus jump straight to the matching drawer and tray, with NDI tucked inside the Show drawer.",
             'The rail and the Timer drawer open beside the script.', 'live'),
            ('Any display setup', 'Works with the rig you have.',
             'Pick Auto, Extended, or Mirrored mode. Mirror or flip the output for a beam-splitter, or invert it for dark text on white. A built-in Before you go live checklist helps you verify every detail before doors open.',
             'The Show tab with the three display-mode icons, plus the Before you go live checklist.', 'live'),
            ('Runlists', 'Multiple scripts, one continuous scroll.',
             'Line up every script for the event in show order and let the reading flow seamlessly from one into the next, with no stopping to open the next file. One key, button, or shortcut jumps cleanly to the next script.',
             '', 'live'),
            ('Bookmarks', 'Hop to any spot.',
             'Drop a bookmark right at your cursor, jump cleanly between them, and view your full list at a glance.',
             '', 'live'),
            ('Settings that travel', 'Carry your setup to any machine.',
             'Export Settings saves your entire configuration into a single file. Import Settings loads it straight onto another Mac or PC, so your backup machine or a second desk runs exactly the way you expect.',
             '', 'beta'),
            ('Phone remote', 'Play, pause, and speed control from your phone.',
             "Turn on the phone remote, set a PIN, and scan the QR code. Play, pause, speed, rewind, fast forward, and bookmark jumps work right from your phone over the venue network, and your phone keeps its screen awake while you're running.",
             '', 'beta'),
            ('Cue to cue', 'Jump straight from cue to cue.',
             'Q2Q hops to the previous or next cue of the types you pick (starting with slides and videos), letting you fly through technical rehearsals without endless scrolling.',
             '', 'beta'),
            ('NDI output', 'Send your prompter and timer as NDI sources.',
             "Put the live prompter feed and the speaker timer onto the network as NDI sources for switchers, multiviewers, or streams. Choose a transparent or chroma-key green background, toggle Timer on NDI right from the Timer drawer, and run Check this machine before showtime to make sure your computer handles the load. Mac first. Windows hasn't been tested yet.",
             '', 'beta'),
            ('Never lose the script', 'A crash won\'t cost you the show.',
             "Cadence autosaves continuously to a recovery file as you type, maintains a dedicated Backups folder, and preserves every version you import. Before doors open, the checklist walks you through Do Not Disturb, notifications, and power settings. Even save and close prompts use Cadence's own dialog box, so a hidden system pop-up can never freeze behind the prompter.",
             '', 'live'),
        ]),
    dict(
        slug='time-and-cues', name='Time, Cues, and Collaboration', audiences='Crew · Presenter',
        h1="Everyone sees where the show is, and what's coming next.",
        lede="How much longer do they have? How long did that segment actually take? Is this the latest script? Now the whole crew can see for themselves. Timers and cues live right inside the script, everyone works off the exact same clock, and the room stays in sync without a single text thread.",
        fcard="How much longer do they have? How long did that segment actually take? Now the whole crew can see for themselves. Timers and cues live right inside the script, and everyone works off the exact same clock. The presenter gets a live pace estimate once they've been reading a minute, and a gentle nudge if they fall behind.",
        card="One live clock and one up-to-date cue sheet for the entire room.",
        feats=[
            'Time',
            ('Speaker timer', 'A clock the presenter can trust.',
             "The time remaining, the segment name, and a live pace estimate that says plainly whether they're running over or under. The presenter never has to do mental math on stage.",
             'The speaker timer page: Time remaining as the large clock on the right half; real time, the estimate (for example -0:12), Coming up and pace on the left.', 'live'),
            ('Timer cues in the script', 'Timer events fire right from the text.',
             "Set, start, and finish cues live directly inside the script. An indicator above the editor shows how many cues are armed and turns red if they're off. Pressing Play arms them automatically, so scrolling past a Start cue kicks off the clock by itself. Pressing Pause disarms them and stops the clock. If a segment wraps with time to spare, the clock stops and turns green.",
             'Two crops of the live bar side by side: Armed 5 in green and OFF 5 in red. Optionally the green finished clock.', 'live'),
            ('Clock colors', 'A timer that shows its state at a glance.',
             'Five states (Running, Warning, Over time, Paused, and Finished early) each get their own color, saved right with the script.',
             '', 'beta'),
            'Cues',
            ('Coming up', 'See the next cue before it hits.',
             'A live list of upcoming cues ahead of the reading line, each showing the exact time until it lands. As you scroll past each cue, the list advances automatically, so you always know what\'s next without hunting through the script.',
             'The operator window with the Coming up list under the timer card, showing four or five cues in different colors with times.', 'live'),
            ('Cue colors', 'Cues you can read from across the room.',
             'Video, slides, general, audio, and bookmarks each come color-coded out of the box, and you can build custom cues of your own. Adjust any color to match the system your crew already uses.',
             'The script editor with all five cue types visible in a few lines of a realistic script.', 'live'),
            ('The cue sheet', 'The whole show as a live rundown.',
             "The cue sheet opens in a tab for you, or on a live page for the crew, turning every cue in your script (or across an entire runlist) into a clean rundown. Every row starts checked Ready. Uncheck one to flag a missing asset or an item to confirm, and the row turns red for the whole crew. Export it as a PDF or spreadsheet, or copy it straight into an email. It's a stage manager's rundown, built automatically from the script itself.",
             '', 'live'),
            'Collaboration',
            ('Share the show', 'Put the clock, cues, and script on any screen.',
             "Flip sharing on to open the speaker timer, the cue sheet, and the live script__BETA__ in any browser, with no extra cables or software. Crew on the venue network can follow the script in its actual colors as it tracks the reading line, adjust their own text size, and use an Edit PIN to tap a line or highlight words and send suggestions straight to your Prepare tab. Need to loop in someone off-site? Even if they're not in the building, or even in the country, Cadence can share a link that works right over the internet. When the session wraps, Sign everyone out in the Collaboration drawer clears every crew login at once.",
             'The Share on the network switch with the listed addresses and viewer count, next to the timer page open in a browser window.', 'live'),
            ('Pull the script', 'The crew grabs the latest draft without asking.',
             'When sharing is on, the crew page includes a Pull script button protected by an Edit PIN. Crew members can download the current script as a PDF, Word, or text file right onto their own phone or laptop. Nobody has to tap you on the shoulder mid-show for the latest file.',
             '', 'live'),
            ('Print, PDF, and Word', 'Clean hard copies in a few clicks.',
             'For anyone in the room who still trusts paper, print the script or export it as a PDF, a Word document, or plain text. Everything lands at a comfortable reading size in print-safe colors, with speaker names and page numbers in place. You can even export a whole runlist as one combined PDF.',
             '', 'live'),
        ]),
    dict(
        slug='a-better-read', name='A better read', audiences='Presenter',
        h1='The best prompter is the one your presenter never notices.',
        lede="When the prompter does its job, the presenter connects with the audience instead of struggling to read the screen. Tricky words and names get built-in pronunciation help. Style, margins, reading marker, and speed are dialed in once and saved.",
        card="A natural read for the presenter, with built-in help to get hard words, names, and pace right.",
        feats=[
            ('Speaker Style', 'Every speaker in their own style.',
             "The Speaker Style tab lists every style in the script, and each row has its own name, color, size, alignment, line spacing, and snap setting. Collections keep a saved set of styles for each client or show, and the Default collection is what a new script starts with. Select lines and pick a style in the Text drawer, or let Prepare find the speaker names in the script and give each one a color. The color palettes are built to read cleanly against black, whether the color goes on the text or serves as a background highlight.",
             'The Speaker Style tab with three styles, their swatches and sizes, and the sample preview.', 'live'),
            ('The reading marker', 'A marker you can see and a line you can follow.',
             "Pick the marker's shape, side, color, and size, along with exactly where the reading line sits on the prompter. Save it once as your default.",
             'The Marker and margins sheet showing the marker shape tiles, the swatches and the reading-line setting.', 'live'),
            ('Margins and alignment', 'Text placed right where the presenter wants it.',
             'Start with Tight, Normal, or Wide margins, or dial in your own exact left and right numbers. Align the script left, centered, or right.',
             'The margins settings in the Prompter tab, and the Text tab showing alignment.', 'live'),
            ('Snap to stanza', 'Verses and lyrics that move a stanza at a time.',
             "Choose which lines snap: turn on Snap for a speaker style (like \"Choir\"), select specific lines and press Snap, or apply it to the whole script. The prompter glides one stanza to the top of the display while the next waits below it. Any stanza taller than the screen gets page stops of its own, and Find page breaks suggests the cleanest places to split the lines. Every stop appears as a mark in the margin, and you can add stops by hand whenever you want them at precise moments. Once you scroll into a run of stanzas, step through one stop at a time using Snap next on the top bar, a Stream Deck, or even the phone remote. While a run plays, the marker rides high so each stanza lands level with it, then glides back down after the last one.",
             'Three or more lines of a snapped stanza, with the START chevron mark, a mid mark and LAST in the margin.', 'beta'),
            ('Back up smoothly', 'Go backward just as easily as forward.',
             "Turn the speed dial past zero and the script scrolls smoothly in reverse. If a presenter repeats a line, you can back right up without a jarring jump. Need to move a little faster without touching the dial? Hit Rewind to zip back, or use Fast Forward to glide ahead.",
             'The live bar speed control, and a short screen recording of the script scrolling backward.', 'live'),
            ('Pronunciation helper', 'Hard names, said right the first time.',
             "Add a phonetic respelling once in the Pronunciations tab or from the right-click menu. It appears right beside the word in the script, either on its first appearance or every time it shows up. Cadence keeps your personal list ready for the names and industry terms that always trip people up.",
             '', 'live'),
            ('Per-presenter alignment', 'Custom alignment for a single presenter.',
             'Align a selected passage differently without affecting the rest of the script.',
             '', 'live'),
        ]),
]


# Real screenshots, by feature title: (file in assets/shots, alt text). A feature with no entry keeps its placeholder.
# All were captured from the app with a fictional sample script; see docs/screenshots in the Cadence repo.
SHOTS = {
    "Speaker timer": ("time-speaker-timer.png", "Two screens side by side. What the speaker sees: the prompter text with the clock and a small green estimate, 19 seconds under. What the crew sees: the speaker timer page with the estimate under time, Coming up with the time to each cue, the time remaining as a large clock, and the next segment."),
    "Coming up": ("time-coming-up.png", "Coming up in the operator window: audio, video, and general cues, then the CEO keynote timer set and its slides, each with its kind, name, and the time until it."),
    "Timer cues in the script": ("time-timer-cues.png", "The live bar indicator reading Armed in green, and the same indicator reading OFF in red when the cues are disarmed."),
    "Share the show": ("time-share.png", "The Collaboration drawer with Sharing on the local network and the View and Edit PINs, next to the speaker timer page it shares."),
    "Cue colors": ("time-cue-colors.png", "The script editor with a bookmark mark and general, audio, slide, and video cues each in its own color, above a timer cue and the first lines of the script."),
    "Stream Deck": ("run-stream-deck.png", "The Stream Deck + beside the Stream Deck + XL, both running Cadence: color-framed keys by category, a touch strip with live readouts for bookmark, timer cues, text size, and speed, and dials underneath. The + XL shows 36 keys and six dials."),
    "Snap to stanza": ("snap-marks.png", "A snapped hymn on the prompter: a START mark beside the first stanza, a smaller mark at the next stop and LAST beside the final stanza, with the reading marker at the left edge."),
    "Speaker Style": ("read-speaker-styles.png", "The Speaker Style tab: each style with a name, color, size, alignment, spacing, and snap, the collection they belong to, and a sample at each speaker's color."),
    "The reading marker": ("read-marker.png", "The Marker group of the Prompter tab: the marker shapes, its side, its color, its size, and the bookmark color."),
    "Margins and alignment": ("read-margins-alignment.png", "The Prompter tab with the text size, line spacing, the Normal and Custom margins with left and right numbers, and the settings new scripts start with."),
    "Back up smoothly": ("read-backward.mp4", "The script scrolling forward, then backward, as the speed passes through zero."),
    "The live bar": ("show-live-bar.png", "The operator window with both bars: the live bar across the top (play, speed, zoom, bookmarks, cue to cue, page jumps, snap, and the Armed indicator) moves the prompter, and the bar under the script (Add cue, Segment, Set, Start, Finish, bookmarks, Edit size) changes the script at your cursor."),
    "Edit on the fly": ("edit-held.png", "The operator window while the script plays and the editor is held: the strip above the script reads Editor held with a Resume following button, the prompter still leads, and the cursor sits in the line being changed."),
    "One search box": ("show-palette.png", "The search box open with find typed, listing the find commands, with their shortcuts."),
    "Organized controls": ("show-ribbon-timer.png", "The operator window with the Timer drawer open at the left, with its Clock colors fold, beside the script, the preview, and the timer card."),
    "Any display setup": ("show-display-checklist.png", "The Show tab with the Auto, Extended, and Mirrored display buttons, and the Before you go live buttons, beside the Before you go live checklist."),
    "Import & Prep": ("prep-import-window.png", "The Prepare tab beside Script, with the Working on list at left (This script marked LIVE, and a staged Import & Prep file) and a raw client script pasted in: speaker names typed inline, notes in brackets, and uneven spacing."),
    "Prepare tab": ("prep-prepare-window.png", "The Prepare tab on the same file: the six steps along the top (Set aside, Spacing, Readability, Speakers, Stage directions, Cues), what Clean up the spacing does and its choices, with Apply, Next, and Send on at the bottom."),
    "Bring in a new version": ("prep-new-version.png", "The Bring in a new version screen listing the client's changes, each marked Theirs or Same, with your script, the client's change, and the result side by side."),
    "Pictures in the script": ("prep-pictures.png", "A slide's picture on a line of its own in the script, with the words of the script above and below it."),
    "Pronunciation helper": ("read-pronunciations.png", "The Pronunciations tab."),
    "The cue sheet": ("time-cue-sheet.png", "The cue sheet on its live page for the crew: every cue as a row with its time, kind, name, and length, segments with the pace they need, and Copy, Print, and Plan and last run buttons."),
    "Print, PDF, and Word": ("prep-print.png", "Page one of a printed script: speaker names above their lines, cues in boxes in print-safe colors, and the date and page number in the margins."),
    "Pull the script": ("time-pull-phone.png", "The pull page on a phone: the script now in the prompter with PDF, Word, and Text buttons, and sections for a runlist and a crew folder."),
    "Never lose the script": ("show-checklist.png", "The Before you go live checklist: Do Not Disturb, notification settings, AirDrop, and chat apps, each with a box to tick."),
    "Script tools": ("docs-before-after.png", "A script pasted in as it arrived, with speaker names and notes typed inline, next to the same passage after Prepare, with colored speakers and cues."),
}


def shot_media(title):
    src, alt = SHOTS[title]
    if src.endswith(".mp4"):
        poster = src.replace(".mp4", "-poster.png")
        return (f'<figure class="shotfig"><video autoplay loop muted playsinline controls preload="metadata" poster="assets/shots/{poster}" aria-label="{alt}">'
                f'<source src="assets/shots/{src}" type="video/mp4"></video></figure>')
    return f'<figure class="shotfig"><a href="assets/shots/{src}"><img src="assets/shots/{src}" alt="{alt}" loading="lazy"></a></figure>'


BETA_NOTE = '<p class="note">Features marked <span class="badge">Beta</span> are built and tested, but they haven&rsquo;t been battle-tested by hand on a live show yet. They&rsquo;re included in the 0.2.2 beta.</p>'


BETA_WITH_PICTURE = {"Snap to stanza", "Prepare tab"}   # Beta cards that show their picture anyway

def feat_block(f):
    if isinstance(f, str):
        return f'<h2 class="group">{f}</h2>'
    title, head, copy, shot, status = f
    copy = copy.replace("__BETA__", ' <span class="badge">Beta</span>')
    badge = {"soon": '<span class="badge">Coming soon</span>', "beta": '<span class="badge">Beta</span>'}.get(status, "")
    media = (shot_media(title) if title in SHOTS else (ph("Capture: " + shot, 240) if shot else "")) if (status == "live" or title in BETA_WITH_PICTURE) else ""
    cls = "feat" if media else "feat feat-text"
    return (f'<article class="{cls}"><div><p class="eyebrow">{title}{badge}</p><h2>{head}</h2><p>{copy}</p></div>{media}</article>')


def jump_strip(cur=None, pos="top"):
    cur_attr = ' aria-current="page"'
    links = "".join(f'<a href="{q["slug"]}.html"{cur_attr if q["slug"] == cur else ""}>{q["name"]}</a>' for q in PILLARS)
    return f'<nav class="jump j{pos}" aria-label="Feature pages"><div class="wrap">{links}</div></nav>'


def pillar_page(i, p):
    body = (jump_strip(p["slug"]) + hero(p["h1"], p["lede"], False, f'<a class="crumb" href="features.html">Features</a> / {p["name"]} · {p["audiences"]}') +
            '<section class="wrap stack">' + BETA_NOTE * any(not isinstance(f, str) and (f[4] == "beta" or "__BETA__" in f[2]) for f in p["feats"]) + "".join(feat_block(f) for f in p["feats"]) + "</section>" +
            '<section class="wrap cta"><h2>Try it on your next show.</h2><p><a class="btn" href="download.html">' + CHEV + 'Download</a></p></section>' + jump_strip(p["slug"], "bottom"))
    return (p["slug"] + ".html", f'{p["name"]} | Cadence Prompt', p["lede"], body)


P = {}
for i, p in enumerate(PILLARS):
    fn, t, d, b = pillar_page(i, p)
    P[fn] = (t, d, b)

pillar_cards = "".join(
    f'<article><p class="eyebrow">{p["audiences"]}</p><h3><a href="{p["slug"]}.html">{p["name"]}</a></h3><p>{p["card"]}</p></article>' for p in PILLARS)

P["index.html"] = ("Cadence Prompt: teleprompter software for the whole show",
    "Teleprompter software built for the presenter, the operator, and the crew.",
    hero("You don&rsquo;t have to live with it.",
         "We keep putting up with the same prompter pain points because we assume they come with the job. They don&rsquo;t. Cadence Prompt is the prompter, rebuilt for the whole room: prep in minutes, run the show with your hands on it, and a crew that sees the same clock you do.") +
    f'<section class="wrap shot"><figure class="shotfig hero-shot"><a href="assets/shots/home-hero.png"><img src="assets/shots/home-hero.png" alt="The Cadence Prompt operator window: the live bar across the top, the ribbon at left, the script with colored speakers and cues, and the preview, timer card, and Coming up in the side column."></a></figure></section>'
        '<section class="wrap live"><h2>Sound familiar?</h2><ul class="pains">'
    '<li><a class="pain" href="prep.html"><span class="prob">Hours spent formatting a script by hand.</span>' + CHEV + '<span class="sol">Import &amp; Prep takes it from raw doc to show-ready in minutes.</span></a></li>'
    '<li><a class="pain" href="prep.html"><span class="prob">A brand-new script lands at five o\'clock, and you\'re back at square one.</span>' + CHEV + '<span class="sol">Drop it in, see every change side by side, and keep your prep intact.</span></a></li>'
    '<li><a class="pain" href="time-and-cues.html"><span class="prob">The crew keeps asking how much time is left, and nobody knows.</span>' + CHEV + '<span class="sol">Now everyone in the room can see the exact same clock.</span></a></li>'
    '<li><a class="pain" href="run-the-show.html"><span class="prob">A clunky controller and a quiet, &ldquo;Why did it just do that?&rdquo;</span>' + CHEV + '<span class="sol">Smooth, predictable control, right under your fingertips.</span></a></li>'
    '<li><a class="pain" href="time-and-cues.html"><span class="prob">Script notes arrive in a group text, and half of them get buried.</span>' + CHEV + '<span class="sol">Crew suggest changes right on the script, and every note lands cleanly in Prepare. <span class="badge">Beta</span></span></a></li>'
    '</ul><p class="built">I built Cadence Prompt after years of working around the exact same headaches. <a href="about.html">Read why &rarr;</a></p></section>'
    '<section class="wrap three"><h2>Three promises, one room</h2><div class="cols">'
    '<article><h3><a href="run-the-show.html">Operators</a></h3><p>Prep in minutes, then run the show with every control right under your hands. A clean interface built around the live bar, a command palette, and full Stream Deck control. Plus a phone remote <span class="badge">Beta</span> for the moments you need to step away from the desk.</p></article>'
    '<article><h3><a href="a-better-read.html">Presenters</a></h3><p>They walk on stage knowing their words, their pace, and their time. Every speaker can have their own style, a reading line that&rsquo;s effortless to follow, and a clock they can trust without looking away from the script.</p></article>'
    '<article><h3><a href="time-and-cues.html">Crews</a></h3><p>One show, one source of truth. Your crew is tired of asking, &ldquo;What&rsquo;s next? How long is left? Is that the latest?&rdquo; With Cadence, everyone sees the same clock, cues, and script in any browser or phone <span class="badge">Beta</span>. Notes land on the script instead of in a text thread <span class="badge">Beta</span>, and rewrites take minutes, not overtime.</p></article>'
    '</div></section>'
    '<section class="wrap prose"><h2>Run it with a Stream Deck.</h2><p>Cadence runs great without a Stream Deck, but best with one. Dedicated keys for the tools you reach for most, dials for speed, text size, and bookmarks, and a touch strip for the clock keep your hands right on the show. You&rsquo;ll want a Stream Deck + or + XL for the dials, though any model works. If you&rsquo;re ever traveling light, nearly every key and dial has a shortcut, a menu row, or an on-screen button that does the same thing.</p></section>'
    '<section class="wrap prose"><h2>Learn it on the prompter.</h2><p>Cadence Prompt teaches itself. Three hands-on series come built into the app: Getting Started, Prep Like a Pro, and The Whole Room. You read each module straight off the prompter and pause to try the features live. Instant Help search and a built-in manual are right there whenever you need a quick answer. <a href="learn.html">See what&rsquo;s inside &rarr;</a></p>'
    '<figure class="shotfig"><img src="assets/shots/help-search.png" alt="Help search with cue sheet typed in: the matching commands, menu items, and manual page, each with where to find it." loading="lazy"></figure></section>'
    f'<section class="wrap"><h2>What makes it different</h2><div class="cols">{pillar_cards}</div></section>'
    '<section class="wrap cta"><h2>Try it on your next show.</h2><p><a class="btn" href="download.html">' + CHEV + 'Download</a></p></section>')

P["features.html"] = ("Features | Cadence Prompt", "What Cadence Prompt does differently.",
    jump_strip() + hero("What&rsquo;s different", "Four places to start, built around the three people in the room.", False) +
    '<section class="wrap stack">' + "".join(
        f'<article class="feat"><div><p class="eyebrow">{p["audiences"]}</p><h2><a href="{p["slug"]}.html">{p["name"]}</a></h2><p>{p.get("fcard", p["lede"])}</p>'
        f'<p><a class="link0" href="{p["slug"]}.html">See {p["name"].lower()} &rarr;</a></p></div>{ART[p["slug"]]()}</article>' for p in PILLARS) + "</section>")

P["download.html"] = ("Get Cadence Prompt | Cadence Prompt", "Ask for a beta access code for Cadence Prompt.",
    hero("Get Cadence Prompt", "Cadence Prompt is currently in beta, and an access code unlocks it. Reach out for a code and I&rsquo;ll send one your way.", False) +
    f'<section class="wrap cols dl"><article><h2>Ask for a beta code</h2><p>Tell me your name and what kind of rig you run, and I&rsquo;ll send over an access code and the installer.</p><p><a class="btn" href="mailto:CadencePrompt@gmail.com?subject=Cadence%20Prompt%20beta%20code">{CHEV}Request a beta code</a></p><p class="note">Access codes work completely offline and stay active throughout the beta.</p></article>'
    '<article><h2>Download the beta</h2><p><strong>Current version: 0.3.0</strong> (November 28, 2026)</p><p>Grab the installer for your machine, then request a code to unlock it.</p><ul><li><a href="https://github.com/CaptainFun333/CadencePrompt-site/releases/download/beta-0.3.0/Cadence-Prompt-0.3.0-Mac-Apple-Silicon.dmg">Mac, Apple Silicon (M1 and later), 0.3.0</a></li><li><a href="https://github.com/CaptainFun333/CadencePrompt-site/releases/download/beta-0.3.0/Cadence-Prompt-0.3.0-Mac-Intel.dmg">Mac, Intel, 0.3.0</a></li><li><a href="https://github.com/CaptainFun333/CadencePrompt-site/releases/download/beta-0.3.0/Cadence-Prompt-0.3.0-Windows-Setup.exe">Windows, 0.3.0</a></li></ul><p class="note">Because the beta installers aren&rsquo;t code-signed yet, your computer will show a security warning the first time. On a Mac, right-click the app and choose Open. On Windows, click More info, then Run anyway.</p></article></section>'
    '<section class="wrap prose"><h2>What you need</h2><p>A Mac or Windows computer. You don&rsquo;t need a Stream Deck to run Cadence. It works great without one, and even better with one.</p><h2>Trial and pricing</h2><p>Every single feature is unlocked during the trial. After that, a simple subscription keeps Cadence Prompt supported and improving, and I&rsquo;ll always be upfront about what it pays for.</p></section>')
P["help.html"] = ("Help | Cadence Prompt", "Read the Cadence Prompt manual and find answers.",
    hero("Help", "Dive into the manual, or learn right on the prompter with the built-in practice series that come with the app.", False) +
    '<section class="wrap cols"><article><h3>The manual</h3><p>The exact same manual built into the app, complete with instant search. It covers the Learn series, Edit view and Prompt view, Prepare, Speaker Style, Runlists, the Speaker timer, the Cue sheet, the crew pages, NDI feeds, Snap to stanza, and a reference for every drawer.</p><p><a class="btn" href="manual.html">' + CHEV + 'Read the manual</a></p></article>'
    '<article><h3>In the app</h3><p>Press Command-Shift-/ (Control-Shift-/ on Windows) and type what you&rsquo;re looking for. Help search shows you right where the control lives and gives you its shortcut. The built-in Learn series walk you through each feature live at a practice stop.</p></article>'
    '<article><h3>Still stuck?</h3><p>Email <a href="mailto:CadencePrompt@gmail.com">CadencePrompt@gmail.com</a> anytime. If you&rsquo;re running a beta build, you can also go to Help, then Report a Problem or Request a Feature right inside the app. <a href="support.html">Support</a></p></article></section>'
    '<section class="wrap"><p class="note">The manual tracks the newest beta build, so a few pages cover features still marked Beta on the feature pages. NDI support is Mac first.</p></section>')
P["changelog.html"] = ("Changelog | Cadence Prompt", "What changed in each version.",
    hero("Changelog", "Every release, in plain language.", False) + '<section class="wrap prose">'
    '<h2>0.3.0 · November 28, 2026</h2><ul>'
    '<li>Prepare as one tab (Beta): Clean-up works on the open script and on the files waiting in Import &amp; Prep from one tab. Each card has one status line and Scan again, long lists show the rows that need a decision first, and Apply the sure ones can run on every file at once.</li>'
    '<li>Tools as tabs: Clean-up, Speaker Style, Pronunciations, New version, the cue sheet, and the Stream Deck layout open as tabs beside Script, in the Extended window and the Mirrored Edit view. Play brings Script forward.</li>'
    '<li>Import &amp; Prep in tabs: each import opens as a tab in one window, with keys to step between them and Move to New Window.</li>'
    '<li>More than one language (Beta): a Word file with a column or a section per language can become one script per language, Cadence asks about languages before tables, and the import summary says what it left out, like footnotes.</li>'
    '<li>More file types: Word .docm, .dotx, and .dotm, PowerPoint .ppsx, and Fountain and Final Draft screenplays.</li>'
    '<li>Settings: a &#8634; beside any changed setting puts it back in one click, and &#8984;Z takes that back. A Defaults window holds your own defaults, and File, then Options, can save your settings and bring them in on another computer.</li>'
    '<li>Speaker Style (the old Styles window) finds the names that start each turn, remembers what it applied, and has its own manual page.</li>'
    '<li>The bars: the top bar holds the reading controls and the bottom bar holds cues, timer cues, and bookmarks. The speed starts at 0, and its readout is colored by play state (green forward, yellow reverse, red playing at zero).</li>'
    '<li>Snap: a landing can take the reading line high while playing and glide back after LAST (Beta), Full dims nothing, and long scripts with many stops scroll more smoothly.</li>'
    '<li>Speaker timer: one calm pace that counts only moving time and leaves stage directions out of word counts. +1, &minus;1, and Add change the segment&rsquo;s target and keep the clock running.</li>'
    '<li>Crew: Sign everyone out in Collaboration forgets every crew login, Coming up scrolls with a Now chip, and the shared script no longer jumps on a redraw.</li>'
    '<li>Cadence&rsquo;s own boxes replace most system dialogs, and &#8984;K and Help search forgive typos. The Mirrored window gains the NDI settings and spell check in its Edit view, and pressing the Reading line dial puts the line back to your default.</li>'
    '</ul>'
    '<h2>0.2.1 · November 21, 2026</h2><ul>'
    '<li>Slide pictures at import on a PC (Beta): when PowerPoint is installed, importing a PowerPoint deck with Include slide pictures has PowerPoint draw the slides, and the pictures come in with the cues. Choose a PDF of the slides is only offered if PowerPoint cannot do it.</li></ul>'
    '<h2>0.2.0 · November 20, 2026</h2><ul>'
    '<li>Learn series (new): Cadence now opens on Getting Started the first time you run it. Getting Started (ten modules), Prep Like a Pro (nine modules), and The Whole Room (nine modules) are practice scripts that teach each feature at a stop on the prompter. They have their own <a href="learn.html">Learn pages</a>, and the old Welcome items leave the Help menu.</li>'
    '<li>Insert from another script (Beta): open an older script in a read-only viewer beside the one you are editing, then copy lines from it and paste them in. Cues and speaker styles come along, and Cadence asks how to number slides only when they do not already follow on. Works in both the Extended and Mirrored windows, reads Word, PowerPoint, Keynote, Pages, PDF, and Telescript, has its own Find, and can send selected lines to Import &amp; Prep.</li>'
    '<li>Stops (Beta): Snap marks are now called stops, drawn as a chevron-and-bar mark in the margin of the prompter and the edit pane. START and LAST mark the ends of a run. Add stop here places a stop by hand on any line.</li>'
    '<li>Hold at snap (Beta): playing into a run of snapping stanzas drops the speed to zero and glides the stanza to the top. The wheel and speed dial are ignored for a moment so a hand still turning the speed does not raise it again.</li>'
    '<li>Snap keys and buttons (Beta): Snap back and Snap next step one stanza stop at a time, on the top bar and as Stream Deck keys. The top bar buttons read SNAP and are greyed until some line snaps. The Q2Q buttons read Q2Q up and Q2Q down.</li>'
    '<li>Search and navigation: &#8984;K is one search box for every setting and command, with choices opened in place. The menu bar now mirrors the drawers, NDI moves into the Show drawer, the Stream Deck drawer becomes Controllers, and each settings tray says how far it reaches. A dot marks settings changed from the default.</li>'
    '<li>Slide pictures at import (Beta): importing a PowerPoint or Keynote deck can bring in the slide pictures, which show on the prompter too. A slide range cue covers slides that have no script, and Bring in a new version matches slides by number.</li>'
    '<li>Prepare: stage directions inside a running sentence go to the review list instead of being colored, a list breaks at its commas, a new After a dash switch breaks at an em dash, and repeated lines can be set the same way in one step.</li>'
    '<li>Mark That Moment: one press (&#8984;&#8997;J, or a Stream Deck key) stamps the run history when something goes wrong, so you can find it after the show. The run history can be saved as a PDF.</li>'
    '<li>Stream Deck: keys are framed in the color of their type, and there is a one-page Plus XL starter. Rewind and Fast Forward show a double chevron when paused. Credit time remaining moves to &#8984;&#8997;G.</li>'
    '<li>Crew pages: the shared script marks the line being read, a click on the percentage resets the text size, and the Cue sheet\'s tick box is now Ready. The Join page says what to check when it cannot connect, and the phone PIN screen is no longer covered by the clocks.</li>'
    '<li>Text and fonts: Libre Franklin is bundled and listed in the Font menu, and the Tilt script now uses it. Edit zoom changes only the edit pane. A color highlight keeps its words readable, and Invert keeps a run\'s own color.</li>'
    '<li>Fixes: the Timer count toggle no longer resets the clock. Opening a script clears the old bookmarks from the deck and knob. Opening a runlist now closes the open script first. Menu items like Import &amp; Prep keep their ampersand.</li></ul>'
    '<h2>0.1.2 · November 11, 2026</h2><ul>'
    '<li>Snap to stanza (Beta): a line, or a whole style, can snap, so the page keys stop at stanzas; a stanza taller than the display gets page stops of its own, and Cadence offers to find the best page breaks.</li>'
    '<li>Viewer pages (Beta): the Timer, Cue sheet, and Script pages share one navigation, with a phone layout and separate View and Edit PINs.</li>'
    '<li>NDI Prompter picture (Beta): Opaque, Transparent, or Green background, with an outline, for a keyer. The prompter display has a Green background too.</li>'
    '<li>A key struck twice inside 0.3 seconds now does its job once, for the page keys, cue to cue, and bookmarks.</li>'
    '<li>Drawers: the Prompter drawer has folds that remember if they are open, and Network is split into NDI and Collaboration. Help search now points at the control it finds.</li>'
    '<li>The Stream Deck page has shorter key captions, new VIEW MARKS, VIEW CUES, and SNAP keys, and a Coming up dial.</li>'
    '<li>The Text roll is no longer part of this build.</li></ul>'
    '<h2>0.1.1 · October 31, 2026</h2><ul>'
    '<li>Help, then Report a Problem or Request a Feature, gathers what you tell it with your app and computer details, a fixed list of settings and script sizes, to copy or save as a file. It is in beta builds only.</li>'
    '<li>Mark That Moment (Command-Option-J, or Control-Alt-J on Windows) stamps a short record kept in memory, so a report can show when the scroll jumped. Nothing is written to disk.</li></ul>'
    '<h2>0.1.0 · October 30, 2026</h2><ul><li>The first beta, for Mac (Apple Silicon and Intel) and Windows: Import &amp; Prep, the live bar, runlists, timer cues, the speaker timer and crew pages, Stream Deck control, and the presenter settings described on the feature pages.</li></ul>'
    '<p class="note">New beta builds are listed here the day they go out.</p></section>')
P["support.html"] = ("Support | Cadence Prompt", "Contact and support.",
    hero("Support", "Run into a snag? Tell me what happened.", False) + '<section class="wrap prose"><p>Email <a href="mailto:CadencePrompt@gmail.com">CadencePrompt@gmail.com</a> and include your app version along with what you were doing when it came up.</p><p>Tell me what&rsquo;s working and what still needs fixing. If something&rsquo;s broken, I&rsquo;m ready to make it right. Share your wins too. Hearing what saved you on a real show tells me exactly what to protect.</p></section>')
P["about.html"] = ("About | Cadence Prompt", "Why Cadence Prompt exists.",
    hero("Why I built Cadence Prompt", "Eighteen years of live shows, and one tool I got tired of working around.", False) +
    '<section class="wrap prose">'
    '<p>I&rsquo;ve worked in live events for eighteen years. I got my start cleaning the office for a neighbor who ran a teleprompter company, and before long I was running prompter, presentation graphics, and media servers on shows of every size.</p>'
    '<p>The software I used most was a great tool once. Over the years, I learned every one of its quirks and bugs by heart. I built workarounds with a Stream Deck and a long list of ways to make things more efficient, most of them using apps outside the prompter. Then one day I caught myself building tools just to make a broken tool behave, and I decided to build the right tool instead.</p>'
    '<p>The very first thing I fixed was coloring text. It used to take four or five clicks just to color a single cue: select the text, right-click, pick color, choose text or background, hit OK. Doing that for an entire script was maddening. Now it takes one click. That&rsquo;s how Cadence Prompt started: one small, annoying headache, fixed for real.</p>'
    '<p>I named it Cadence for the feel of movement, rhythm, and pace. When a prompter does its job, the presenter stops reading and starts connecting.</p>'
    '<h2>What I&rsquo;m here to do</h2>'
    '<p>I want to make live events better for presenters, operators, and crews. Better enough that none of them can imagine running a show without the calm and connection Cadence Prompt brings to the room.</p>'
    '<p>In live events, clients are sometimes under-prepared, and the clock never stops moving. The answer isn&rsquo;t to stress about it. It&rsquo;s to be over-prepared enough to handle whatever lands at five o&rsquo;clock. I wanted a prompter that&rsquo;s just as good for the crew behind the scenes as it is for the presenter on stage. I&rsquo;m not trying to build the loudest tool in the room. I want to build the one that shows up on every gig and does exactly what it promised.</p>'
    '<h2>What I hold to</h2>'
    '<ul class="values">'
    '<li><strong>Accuracy before speed.</strong> A late change is only fast if it&rsquo;s right. Cadence shows you what changed and applies nothing silently.</li>'
    '<li><strong>Calm in the moment.</strong> The screen should never add to the pressure.</li>'
    '<li><strong>Every seat in the room matters.</strong> The operator, the presenter, and the crew each get something built for them.</li>'
    '<li><strong>Honest by default.</strong> If it&rsquo;s not built, it says coming soon. If it&rsquo;s a claim, it&rsquo;s checked.</li>'
    '<li><strong>Built from real shows.</strong> Every feature starts with a problem someone lived.</li>'
    '<li><strong>Solve what you thought you had to live with.</strong> Add value without being asked.</li></ul>'
    '<h2>What I&rsquo;ll do for you</h2>'
    '<p>Tell me what&rsquo;s working and what still needs fixing. If something&rsquo;s broken, I&rsquo;m ready to make it right. Share your wins too. Hearing what saved you on a real show tells me exactly what to protect.</p></section>')
P["privacy.html"] = ("Privacy | Cadence Prompt", "What Cadence Prompt keeps, what leaves your computer, and what the optional Anywhere service handles.", hero("Privacy", "Cadence Prompt works on your computer. Nothing leaves it unless you switch something on. Last updated 11 November 2026.", False) + """<section class="wrap prose">
<h2>The app on your computer</h2>
<p>Your scripts, run sheets, pictures, settings, and cue lists stay on your computer. Cadence Prompt does not send usage statistics, and an access code is checked on your computer, without contacting anyone.</p>
<p>Two things reach the internet only when you ask. If you import from a Google Docs or Drive link, Cadence fetches that link from Google. If you switch on Anywhere (below), the show goes through the online service.</p>
<h2>Sharing on the venue network</h2>
<p>When you switch on sharing, other devices on the same network can open the crew pages from your computer. That traffic stays on the local network and does not go through any service of mine.</p>
<h2>Anywhere (optional)</h2>
<p>Anywhere lets people who are not on the venue network open the crew pages (the clocks and, if you choose, the script) from a link or QR code. It is off every time Cadence starts. Nothing goes anywhere until you switch it on.</p>
<h3>What passes through the service</h3>
<ul>
<li>While someone is watching from outside: the timer clocks and segment names. The script text and the place you are reading go through only if Share the script text is on.</li>
<li>From viewers: ticks and notes on the cue sheet (with the Edit PIN), and suggestions on lines (with the Edit PIN).</li>
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
P["terms.html"] = ("Terms | Cadence Prompt", "The terms for using Cadence Prompt: the beta, your scripts, sharing, the trial, and the limits of what I can promise.", hero("Terms", "The plain version of how Cadence Prompt works between us. Last updated November 27, 2026.", False) + """<section class="wrap prose">
<h2>Who operates Cadence Prompt</h2>
<p>Cadence Prompt is made and run by Brad, an independent developer and working prompter operator. &ldquo;I&rdquo; means me, and &ldquo;you&rdquo; means whoever uses the app, this website, or the optional Anywhere service. Questions about any of this can be sent to <a href="mailto:CadencePrompt@gmail.com">CadencePrompt@gmail.com</a>.</p>
<h2>This is a beta</h2>
<p>Cadence Prompt is currently in beta. It is built and tested, but features marked Beta have not been battle-tested on a live show yet, and any build can have bugs. Rehearse with it, keep a backup plan for anything that matters, and let me know when something breaks. Features may be changed, renamed, or removed while the beta runs.</p>
<h2>Your access code and the app</h2>
<p>An access code unlocks the app on the computers of the person or team it was issued to. It works offline. Do not post an access code publicly or share it with people it was not issued to. You have the right to use Cadence Prompt for your own work, including paid shows. You may not copy it to resell or redistribute, reverse-engineer or take it apart to build a competing product, or remove its notices.</p>
<h2>Your scripts are yours</h2>
<p>You own your scripts, pictures, settings, and everything else you create. They stay on your computer. I do not receive a copy, I do not claim any rights in them, and you are responsible for having the right to use whatever you put in them. What leaves your computer, and when, is described on the <a href="privacy.html">Privacy</a> page.</p>
<h2>Sharing and Anywhere</h2>
<p>Sharing is off until you switch it on. When you share, you decide who gets the link and the PINs, and anyone with both can see what that PIN allows until you turn sharing off or use Sign everyone out. Four-digit PINs are a convenience, not strong security, so do not share a script that would be harmful in the wrong hands. The Anywhere service runs on Google&rsquo;s Firebase and is offered as is. It can be slow, interrupted, or changed, so never make it the only way the room can see a cue.</p>
<h2>Trial and pricing</h2>
<p>Every feature is unlocked during the trial. After that, a simple subscription keeps Cadence Prompt supported and improving. Pricing and subscription terms will be stated clearly before anything is charged, and nothing is charged during the beta.</p>
<h2>Disclaimers and limits of liability</h2>
<p>I will fix what I can, as fast as I can, but I cannot promise Cadence Prompt will be error-free or always available. It is provided &ldquo;as is,&rdquo; without warranties of any kind, express or implied. To the extent the law allows, I am not liable for indirect, incidental, or consequential losses, such as a lost show, a missed cue, or lost income. My total liability for anything related to Cadence Prompt is limited to what you paid me in the twelve months before the problem, or $50 if you have not paid anything. Nothing here limits anything the law does not allow to be limited.</p>
<h2>Third-party names</h2>
<p>Cadence Prompt is not affiliated with or endorsed by Elgato (Stream Deck), Bitfocus (Companion), Microsoft, Apple, Google, or NDI. Those names belong to their respective owners and are used only to describe compatibility.</p>
<h2>Ending, changing, and governing law</h2>
<p>You can stop using Cadence Prompt anytime. I may disable an access code that is being misused. If these terms change, I will update the date at the top, and for significant changes I will notify beta users by email. Continuing to use the app after a change means you accept the updated terms. These terms are governed by the laws of the State of Utah, without regard to conflict-of-law rules. If any part of these terms is found unenforceable, the rest still applies.</p></section>""")

P["send-a-script.html"] = ("Send us a script in more than one language | Cadence Prompt", "How to prepare a script in two or more languages so Cadence can read each one as its own script.",
    hero("Sending a script in more than one language", "Three ways that work, and three rules for all of them.", False) + """<section class="wrap prose">
<p>When a show runs in more than one language, Cadence reads each language as a script of its own, kept in step line for line. The easier the file is to read, the less anyone has to prepare by hand. Here is what works best, in order.</p>
<h2>The three rules</h2>
<ul>
<li><strong>The same cue numbers in every language</strong> (<code>[001]</code>, <code>[002]</code>, and so on).</li>
<li><strong>The same number of lines in every language</strong>, in the same order. If one language really has an extra announcement, that is fine: Cadence says so plainly and carries on.</li>
<li><strong>Say which language is which</strong>: in the file name, in a heading row, or in a heading.</li>
</ul>
<h2>1. One file for each language (best)</h2>
<p>Send <code>Summit_EN.docx</code>, <code>Summit_ES.docx</code>, and so on, with the same cue numbers in each. Nothing special is needed on our side: each file is a normal import. <a href="assets/samples/Summit_EN.docx">Sample, English</a> · <a href="assets/samples/Summit_ES.docx">Sample, Spanish</a></p>
<h2>2. One table, a column for each language</h2>
<p>A heading row that names each language (<em>English</em>, <em>Español</em>), and one row for each beat. Put the speaker and the cue number in their own column (<code>[001] HOST</code>). A column of visuals or notes on the left is fine, and a row across the whole table can carry a scene title. Please do not merge the language cells. <a href="assets/samples/Summit_table_EN_ES.docx">Sample table</a></p>
<h2>3. One file, a section for each language</h2>
<p>Put each language under its own heading on a line of its own, such as <em>ENGLISH (EN)</em> and <em>ESPAÑOL (ES)</em> (Heading 1 is best). Anything before the first heading, like the title, goes into every language. Repeat the same cue numbers in each section. <a href="assets/samples/Summit_sections_EN_ES.docx">Sample sections</a></p>
<h2>Anything else</h2>
<p>Send it as it is and tell us which language you need. Cadence can still import it, but someone has to prepare it by hand.</p>
<h2>Please avoid</h2>
<p>Facing pages (one language on the left page, one on the right), translations hidden in footnotes or comments, and languages switched off through Word styles. They are hard to read without guessing. Any of the three ways above is easy to send instead.</p>
</section>""")

import learn
P.update(learn.pages(hero))

# pillar pages highlight "Features" in the nav
for fn, (t, d, b) in P.items():
    cur = "features.html" if fn in [p["slug"] + ".html" for p in PILLARS] else ("learn.html" if fn.startswith("learn-") else fn)
    open(fn, "w").write(page(fn, t, d, b, cur))

open("CNAME", "w").write("cadenceprompt.com\n")
open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
open(".nojekyll", "w").write("")
urls = "".join(f"<url><loc>{SITE}{'' if fn == 'index.html' else fn}</loc></url>" for fn in sorted(list(P) + ["manual.html"]) if fn not in NOINDEX)
open("sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
print(len(P), "pages")
