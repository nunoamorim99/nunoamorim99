"""Generates the stack tile rows used by the profile README, one SVG per category.

Usage: python scripts/gen_stack.py assets
Logos come from simple-icons (pinned) or the vendor's own SVG; a few have no logo and get a drawn glyph.
"""
import base64
import json
import re
import sys
import urllib.request
from pathlib import Path

OUT = Path(sys.argv[1]) / "stack"
SI = "https://cdn.jsdelivr.net/npm/simple-icons@15.0.0"
SANS = "'Segoe UI', Inter, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"

TILE, GAP, ICON, PAD, TOP = 64, 22, 32, 12, 8
CELL = TILE + GAP

# Glyphs for tools without a published mark, drawn on a 24x24 grid.
GLYPHS = {
    "phaser": ("#A78BFA", '<path d="M7 7h10a5 5 0 0 1 5 5v2a4 4 0 0 1-7 2.6L13.8 15h-3.6L9 16.6A4 4 0 0 1 2 14v-2a5 5 0 0 1 5-5Z" fill="none" stroke="{c}" stroke-width="1.8" stroke-linejoin="round"/><path d="M7 9.5v4M5 11.5h4" stroke="{c}" stroke-width="1.8" stroke-linecap="round"/><circle cx="16" cy="10.5" r="1.2" fill="{c}"/><circle cx="18" cy="13" r="1.2" fill="{c}"/>'),
    "webaudio": ("#E8A23D", '<path d="M2 12h3l2-6 3 12 3-15 3 18 2-9h4" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'),
    "canvas": ("#22D3EE", '<rect x="3" y="4" width="18" height="13" rx="2" fill="none" stroke="{c}" stroke-width="1.8"/><path d="M8 21l4-4 4 4" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M7 13l3-3 2.5 2.5L17 8" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'),
    "gsap": ("#88CE02", '<text x="12" y="15.5" text-anchor="middle" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="9" fill="{c}">GSAP</text>'),
    "agile": ("#12B9A6", '<rect x="3" y="3" width="5" height="18" rx="1.5" fill="none" stroke="{c}" stroke-width="1.6"/><rect x="9.5" y="3" width="5" height="18" rx="1.5" fill="none" stroke="{c}" stroke-width="1.6"/><rect x="16" y="3" width="5" height="18" rx="1.5" fill="none" stroke="{c}" stroke-width="1.6"/><rect x="4.5" y="5" width="2" height="3" rx=".5" fill="{c}"/><rect x="4.5" y="9.5" width="2" height="3" rx=".5" fill="{c}"/><rect x="11" y="5" width="2" height="3" rx=".5" fill="{c}"/><rect x="17.5" y="5" width="2" height="3" rx=".5" fill="{c}"/><rect x="17.5" y="9.5" width="2" height="3" rx=".5" fill="{c}"/><rect x="17.5" y="14" width="2" height="3" rx=".5" fill="{c}"/>'),
}

# Brand colours that vanish on a dark tile.
RECOLOUR = {"pwa": "A78BFA"}

# Vendor SVGs, with recolours so dark parts stay visible on a dark tile.
VENDOR = {
    "playwright": ("https://playwright.dev/img/playwright-logo.svg", {"#2D4552": "#A9B8C3"}),
    "dokploy": ("https://raw.githubusercontent.com/Dokploy/dokploy/canary/apps/dokploy/public/logo.svg", {"<svg": '<svg fill="#E6EDF3"'}),
}

ROWS = {
    "languages": [("typescript", "TypeScript"), ("javascript", "JavaScript"), ("python", "Python"), ("html5", "HTML"), ("css", "CSS")],
    "frontend": [("vuedotjs", "Vue"), ("react", "React"), ("react", "React Native"), ("expo", "Expo"), ("nextdotjs", "Next.js"),
                 ("vite", "Vite"), ("tailwindcss", "Tailwind"), ("vuetify", "Vuetify"), ("gsap", "GSAP"), ("pwa", "PWA")],
    "games": [("threedotjs", "three.js"), ("phaser", "Phaser"), ("webaudio", "Web Audio"), ("canvas", "Canvas 2D")],
    "backend": [("nodedotjs", "Node.js"), ("hono", "Hono"), ("zod", "Zod"), ("postgresql", "PostgreSQL"), ("supabase", "Supabase")],
    "delivery": [("vitest", "Vitest"), ("playwright", "Playwright"), ("docker", "Docker"), ("githubactions", "GH Actions"),
                 ("cloudflare", "Cloudflare"), ("hetzner", "Hetzner"), ("dokploy", "Dokploy"), ("git", "Git")],
    "product": [("claude", "Claude Code"), ("figma", "Figma"), ("jira", "Jira"), ("agile", "Scrum/Kanban")],
}


def fetch(url):
    with urllib.request.urlopen(url, timeout=30) as r:
        return r.read().decode("utf-8")


def readable(hex_):
    r, g, b = (int(hex_[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b > 0.2


def icon_markup(slug, colours, x, y):
    if slug in GLYPHS:
        c, g = GLYPHS[slug]
        s = ICON / 24
        return f'<g transform="translate({x} {y}) scale({s})">{g.replace("{c}", c)}</g>'
    if slug in VENDOR:
        url, swaps = VENDOR[slug]
        svg = fetch(url)
        for a, b in swaps.items():
            svg = svg.replace(a, b, 1) if a == "<svg" else svg.replace(a, b)
        data = base64.b64encode(svg.encode()).decode()
        return f'<image href="data:image/svg+xml;base64,{data}" x="{x}" y="{y}" width="{ICON}" height="{ICON}"/>'
    path = re.search(r' d="([^"]+)"', fetch(f"{SI}/icons/{slug}.svg")).group(1)
    hex_ = RECOLOUR.get(slug, colours[slug])
    fill = f"#{hex_}" if readable(hex_) else "#E6EDF3"
    s = ICON / 24
    return f'<path transform="translate({x} {y}) scale({s})" d="{path}" fill="{fill}"/>'


def row(items, colours):
    W, H = CELL * len(items) - GAP + 2 * PAD, TOP + TILE + 26
    tiles, css = [], []
    for i, (slug, label) in enumerate(items):
        x = PAD + i * CELL
        css.append(f".t{i} {{ animation-delay: {i * .07:.2f}s; }} .t{i} .bob {{ animation-delay: {i * .18 - 3:.2f}s; }}")
        tiles.append(f"""
<g class="t t{i}"><g class="bob">
  <rect x="{x + .5}" y="{TOP + .5}" width="{TILE - 1}" height="{TILE - 1}" rx="15" fill="#161B22" stroke="#30363D"/>
  {icon_markup(slug, colours, x + (TILE - ICON) / 2, TOP + (TILE - ICON) / 2)}
  <text class="label" x="{x + TILE / 2}" y="{TOP + TILE + 18}" text-anchor="middle">{label}</text>
</g></g>""")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{', '.join(l for _, l in items)}">
<style>
.label {{ font-family: {SANS}; font-size: 11.5px; fill: #8B949E; }}
.t {{ animation: pop .6s cubic-bezier(.2,.9,.3,1.25) both; transform-box: fill-box; transform-origin: center; }}
.bob {{ animation: bob 4s ease-in-out infinite; }}
@keyframes pop {{ from {{ opacity: 0; transform: scale(.6); }} to {{ opacity: 1; transform: none; }} }}
@keyframes bob {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-3px); }} }}
{' '.join(css)}
@media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
</style>{''.join(tiles)}
</svg>
"""


data = json.loads(fetch(f"{SI}/data/simple-icons.json"))
icons = data if isinstance(data, list) else data["icons"]
colours = {}
for ic in icons:
    slug = ic.get("slug") or re.sub(r"[^a-z0-9]", "", ic["title"].lower().replace("+", "plus").replace(".", "dot").replace("&", "and"))
    colours[slug] = ic["hex"]

OUT.mkdir(parents=True, exist_ok=True)
for name, items in ROWS.items():
    (OUT / f"{name}.svg").write_text(row(items, colours), encoding="utf-8")
    print(name, len(items))
