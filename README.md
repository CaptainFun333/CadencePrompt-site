# Cadence Prompt website

Static site for cadenceprompt.com. No build step for hosting: GitHub Pages serves these files as they are.

- `build.py` regenerates the pages from shared parts (`python3 build.py`). Edit copy in `build.py`, styles in `style.css`.
- `assets/` holds the outlined brand SVGs. `CNAME` points the site at cadenceprompt.com.
- Placeholder boxes and `[brackets]` mark copy, screenshots and decisions still to come (pricing, installer format).

## Hosting
Enable GitHub Pages (Settings, Pages, deploy from `main` / root). At GoDaddy keep the domain, and set DNS: four `A` records for `@` to GitHub Pages' IPs and a `CNAME` for `www` to `<account>.github.io`. Confirm the current IPs in GitHub's Pages documentation.
