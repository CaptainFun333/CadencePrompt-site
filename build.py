import os
NAV=[("index.html","Home"),("features.html","Features"),("download.html","Download"),("help.html","Help"),("changelog.html","Changelog"),("support.html","Support")]
CHEV='<svg class="chev" viewBox="963 238 262 565" aria-hidden="true"><path fill="currentColor" d="M963 238L1225 521L963 803V606L1042 520L963 434Z"/></svg>'
def page(fn,title,desc,body,cur=None):
    nav="".join(f'<a href="{h}"{" aria-current=\"page\"" if h==fn else ""}>{t}</a>' for h,t in NAV)
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
def ph(label,h=320): return f'<div class="ph" style="min-height:{h}px"><span>PLACEHOLDER</span>{label}</div>'
def hero(h,sub,cta=True):
    c=f'<p><a class="btn" href="download.html">{CHEV}Try Cadence Prompt</a> <a class="link" href="features.html">See what is different</a></p>' if cta else ''
    return f'<section class="hero"><div class="wrap"><h1>{h}</h1><p class="sub">{sub}</p>{c}</div></section>'
P={}
P["index.html"]=("Cadence Prompt: teleprompter software for the whole show","Teleprompter software built for the presenter, the operator and the crew.",
 hero("The prompter, rebuilt for the whole room.","Most prompter software has not had a real upgrade in years. Cadence Prompt gives operators a better interface, presenters a better read, and crews timers and cues in one place.")+
 f'<section class="wrap shot">{ph("Hero image or short clip: the operator window with the live bar, ribbon and Coming up list",420)}</section>'
 '<section class="wrap three"><h2>A win for everyone in the room</h2><div class="cols">'
 '<article><h3>Operators</h3><p>A cleaner interface built around the live bar, the command palette and Stream Deck control. <em>[copy to write]</em></p></article>'
 '<article><h3>Presenters</h3><p>A better reading experience and faster script delivery. <em>[copy to write]</em></p></article>'
 '<article><h3>Production crews</h3><p>Integrated timers, a live Coming up list of cues, and quicker script formatting that saves time and money. <em>[copy to write]</em></p></article>'
 '</div></section>'
 '<section class="wrap"><h2>What makes it different</h2><div class="cols">'
 f'<article>{ph("Screenshot: speaker timer page",200)}<h3>Integrated timers</h3><p>[copy]</p></article>'
 f'<article>{ph("Screenshot: Coming up list",200)}<h3>Cues coming up</h3><p>[copy]</p></article>'
 f'<article>{ph("Screenshot: script with colored cues",200)}<h3>Fast script formatting</h3><p>[copy]</p></article>'
 '</div></section>'
 '<section class="wrap cta"><h2>Try it on your next show.</h2><p><a class="btn" href="download.html">'+CHEV+'Download</a></p></section>')
P["features.html"]=("Features | Cadence Prompt","What Cadence Prompt does differently.",
 hero("What is different","One page for each idea. Show it, then say it in one sentence.",False)+
 '<section class="wrap stack">'+"".join(f'<article class="feat"><div><h2>{t}</h2><p>[copy to write]</p></div>{ph("Screenshot or clip",240)}</article>' for t in ["Integrated timers","Cues coming up","Cue colors you control","Script formatting that saves time","Stream Deck control","Share the speaker timer on the network"])+'</section>')
P["download.html"]=("Download | Cadence Prompt","Download Cadence Prompt for Mac and Windows.",
 hero("Download Cadence Prompt","[Trial or free tier wording to decide. Pricing is not set.]",False)+
 f'<section class="wrap cols dl"><article><h2>Mac</h2><p class="mono">macOS [min version] · [size]</p><p><a class="btn" href="#">{CHEV}Download .dmg</a></p><p class="note">Link goes to the latest release when builds exist.</p></article>'
 f'<article><h2>Windows</h2><p class="mono">Windows [min version] · [size]</p><p><a class="btn" href="#">{CHEV}Download installer</a></p><p class="note">Installer format to decide.</p></article></section>'
 '<section class="wrap prose"><h2>Install</h2><ol><li>[step]</li><li>[step]</li></ol><h2>System requirements</h2><p>[to write]</p><h2>Trial and pricing</h2><p>[undecided: trial or freemium]</p></section>')
P["help.html"]=("Help | Cadence Prompt","Get started and find answers.",
 hero("Help","Start here. The full manual will grow from the in-app help.",False)+
 '<section class="wrap cols"><article><h3>Quick start</h3><p>[5 steps from script to show]</p></article><article><h3>Stream Deck</h3><p>[setup]</p></article><article><h3>Timers and cues</h3><p>[how they work]</p></article><article><h3>Keyboard shortcuts</h3><p>[the key map]</p></article></section>')
P["changelog.html"]=("Changelog | Cadence Prompt","What changed in each version.",
 hero("Changelog","Every release, in plain language.",False)+'<section class="wrap prose"><h2>[version] · [date]</h2><ul><li>[note]</li></ul><p class="note">Generated from the app changelog at release time.</p></section>')
P["support.html"]=("Support | Cadence Prompt","Contact and support.",
 hero("Support","Tell us what you ran into.",False)+'<section class="wrap prose"><p>Email <a href="mailto:CadencePrompt@gmail.com">CadencePrompt@gmail.com</a>. Include your version and what you were doing.</p><p class="note">Move to support@cadenceprompt.com once domain email is set up.</p></section>')
P["privacy.html"]=("Privacy | Cadence Prompt","Privacy policy.",hero("Privacy","[Policy to write before launch.]",False))
P["terms.html"]=("Terms | Cadence Prompt","Terms of use.",hero("Terms","[Terms to write before launch.]",False))
for fn,(t,d,b) in P.items(): open(fn,"w").write(page(fn,t,d,b))
open("CNAME","w").write("cadenceprompt.com\n")
open("robots.txt","w").write("User-agent: *\nAllow: /\n")
open(".nojekyll","w").write("")
print(len(P),"pages")
