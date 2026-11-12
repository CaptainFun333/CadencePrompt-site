#!/usr/bin/env python3
"""Copies the app's offline manual (run `npm run manual` in ~/Developer/cadence first) to manual.html, with a link back to the site."""
import os
src = open(os.path.expanduser('~/Developer/cadence/src/manual/index.html')).read()
a = '<nav><input id="q"'
assert src.count(a) == 1, 'manual layout changed'
open('manual.html', 'w').write(src.replace(a, '<nav><a href="help.html" style="margin:14px 14px 0;font-size:14px;color:var(--acc)">&larr; Back to cadenceprompt.com</a><input id="q"', 1))
print('manual.html refreshed')
