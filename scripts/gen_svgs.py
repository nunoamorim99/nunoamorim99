"""Generates the animated SVGs used by the profile README. Usage: python scripts/gen_svgs.py assets"""
import sys
from pathlib import Path

OUT = Path(sys.argv[1])

SANS = "'Segoe UI', Inter, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace"

BG = "#0B0F14"
INK = "#E6EDF3"
MUTED = "#8B949E"
TEAL = "#12B9A6"
VIOLET = "#8B5CF6"
AMBER = "#E8A23D"
CYAN = "#22D3EE"

REDUCED = "@media (prefers-reduced-motion: reduce) { * { animation: none !important; } .role { opacity: 0; } .role-0 { opacity: 1; } .role-0 .clip { transform: none; } .dot { opacity: 1; } }"


def header():
    W, H = 1200, 360
    roles = [
        "AI Product Engineer",
        "Product Manager @ Foco Criativo",
        "Claude Code plugin author",
        "Front-End Engineer",
        "Indie game builder",
    ]
    fs = 24
    cw = fs * 0.6
    x0, y0 = 98, 214
    slot = 4.0
    cycle = slot * len(roles)

    css = [f"""
text {{ font-family: {SANS}; }}
.mono {{ font-family: {MONO}; }}
.orb {{ animation: drift 18s ease-in-out infinite alternate; transform-box: fill-box; transform-origin: center; }}
.orb.b {{ animation-duration: 22s; animation-delay: -6s; }}
.orb.c {{ animation-duration: 26s; animation-delay: -12s; }}
@keyframes drift {{ 0% {{ transform: translate(0,0) scale(1); }} 50% {{ transform: translate(40px,-25px) scale(1.15); }} 100% {{ transform: translate(-30px,20px) scale(.95); }} }}
.grid {{ animation: pan 30s linear infinite; }}
@keyframes pan {{ to {{ transform: translate(-40px,-40px); }} }}
.rise {{ animation: rise .9s cubic-bezier(.2,.8,.2,1) both; }}
@keyframes rise {{ from {{ opacity: 0; transform: translateY(16px); }} to {{ opacity: 1; transform: none; }} }}
.cursor {{ animation: blink 1s steps(1) infinite; }}
@keyframes blink {{ 50% {{ opacity: 0; }} }}
.chip {{ animation: float 6s ease-in-out infinite; }}
.chip.c2 {{ animation-delay: -2s; }}
.chip.c3 {{ animation-delay: -4s; }}
@keyframes float {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-8px); }} }}
.pulse {{ animation: pulse 2s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
@keyframes pulse {{ 0%,100% {{ opacity: 1; transform: scale(1); }} 50% {{ opacity: .35; transform: scale(1.8); }} }}
"""]

    # Typewriter: each role owns one slot of the cycle; a clip rect scales open in steps, holds, then erases.
    # Offsets are baked into each role's keyframes (no animation-delay), so idle roles stay hidden.
    t_type, t_hold, t_erase = 1.3 / cycle * 100, (slot - 0.6) / cycle * 100, (slot - 0.15) / cycle * 100
    roles_svg = []
    for i, r in enumerate(roles):
        w = len(r) * cw
        n = len(r)
        off = i * slot / cycle * 100
        # One keyframe per character so steps(1) reads as typing, then a quicker per-character erase.
        frames_t, frames_m = ["0% { transform: scaleX(0); }"], ["0% { opacity: 0; transform: translateX(0); }"]
        for k in range(n + 1):
            p = off + t_type * k / n
            frames_t.append(f"{p:.3f}% {{ transform: scaleX({k / n:.4f}); }}")
            frames_m.append(f"{p:.3f}% {{ opacity: 1; transform: translateX({cw * k:.1f}px); }}")
        span = t_erase - t_hold
        for k in range(1, n + 1):
            p = off + t_hold + span * k / n
            frames_t.append(f"{p:.3f}% {{ transform: scaleX({(n - k) / n:.4f}); }}")
            frames_m.append(f"{p:.3f}% {{ opacity: 1; transform: translateX({cw * (n - k):.1f}px); }}")
        end = off + slot / cycle * 100
        frames_t.append(f"{end - 0.01:.3f}%, 100% {{ transform: scaleX(0); }}")
        frames_m.append(f"{end - 0.01:.3f}%, 100% {{ opacity: 0; transform: translateX(0); }}")
        if i == 0:
            frames_t.pop(0)
            frames_m.pop(0)
        css.append(
            f"""
.role-{i} .clip {{ animation: type-{i} {cycle}s steps(1) infinite; transform-box: fill-box; transform-origin: left; }}
.role-{i} .cur {{ animation: move-{i} {cycle}s steps(1) infinite; }}
@keyframes type-{i} {{ {' '.join(frames_t)} }}
@keyframes move-{i} {{ {' '.join(frames_m)} }}
"""
        )
        roles_svg.append(f"""
  <g class="role role-{i}">
    <clipPath id="clip-{i}"><rect class="clip" x="{x0}" y="{y0 - fs}" width="{w:.1f}" height="{fs * 1.5}" transform="scale(0 1)"/></clipPath>
    <text class="mono" x="{x0}" y="{y0}" font-size="{fs}" fill="{INK}" textLength="{w:.1f}" lengthAdjust="spacingAndGlyphs" clip-path="url(#clip-{i})">{r}</text>
    <rect class="cur" x="{x0 + 2}" y="{y0 - fs + 3}" width="{cw * 0.75:.1f}" height="{fs + 2}" fill="{TEAL}" opacity="0"/>
  </g>""")

    # Biscuit trail with a chomper running along the bottom (a nod to Beagle Chomp).
    trail_y = 318
    tx0, tx1 = 60, 1140
    run = 9.0
    period = 11.0
    css.append(f"""
.chomper {{ animation: run {period}s linear infinite; }}
@keyframes run {{ 0% {{ transform: translateX(0); }} {run / period * 100:.2f}% {{ transform: translateX({tx1 - tx0 + 40}px); }} 100% {{ transform: translateX({tx1 - tx0 + 40}px); }} }}
.jaw-top {{ animation: chomp-top .32s ease-in-out infinite alternate; transform-origin: 0 0; }}
.jaw-bot {{ animation: chomp-bot .32s ease-in-out infinite alternate; transform-origin: 0 0; }}
@keyframes chomp-top {{ from {{ transform: rotate(-32deg); }} to {{ transform: rotate(-2deg); }} }}
@keyframes chomp-bot {{ from {{ transform: rotate(32deg); }} to {{ transform: rotate(2deg); }} }}
.ear {{ animation: flop .32s ease-in-out infinite alternate; transform-origin: -4px -12px; }}
@keyframes flop {{ from {{ transform: rotate(-6deg); }} to {{ transform: rotate(8deg); }} }}
""")
    dots = []
    n_dots = 36
    for i in range(n_dots):
        x = tx0 + 40 + i * (tx1 - tx0 - 40) / (n_dots - 1)
        eaten = (x - tx0) / (tx1 - tx0 + 40) * run / period * 100
        big = i in (11, 27)
        css.append(f"@keyframes eat-{i} {{ 0%, {eaten:.2f}% {{ opacity: 1; }} {eaten + 0.01:.2f}%, 97% {{ opacity: 0; }} 100% {{ opacity: 1; }} }} .d{i} {{ animation: eat-{i} {period}s linear infinite; }}")
        if big:
            dots.append(f'<rect class="dot d{i}" x="{x - 7:.1f}" y="{trail_y - 3}" width="14" height="6" rx="3" fill="#F5E6C8"/>')
        else:
            dots.append(f'<circle class="dot d{i}" cx="{x:.1f}" cy="{trail_y}" r="3" fill="{AMBER}" opacity=".85"/>')

    chips = [
        ("c1", 812, 70, VIOLET, "5", "Claude Code plugins", "agile · ideas · docs · security"),
        ("c2", 852, 146, AMBER, "3", "browser games shipped", "three.js · Canvas · Phaser"),
        ("c3", 812, 222, TEAL, "4", "roles at Foco Criativo", "intern → engineer → PO → PM"),
    ]
    chips_svg = []
    for cls, x, y, color, big, label, sub in chips:
        chips_svg.append(f"""
  <g class="chip {cls}">
    <g class="rise" style="animation-delay:{0.5 + 0.15 * int(cls[1])}s">
      <rect x="{x}" y="{y}" width="320" height="62" rx="14" fill="#11161D" stroke="{color}" stroke-opacity=".45"/>
      <rect x="{x}" y="{y + 14}" width="3" height="34" rx="1.5" fill="{color}"/>
      <text x="{x + 22}" y="{y + 42}" font-size="30" font-weight="800" fill="{color}">{big}</text>
      <text x="{x + 64}" y="{y + 28}" font-size="15" font-weight="600" fill="{INK}">{label}</text>
      <text class="mono" x="{x + 64}" y="{y + 48}" font-size="12" fill="{MUTED}">{sub}</text>
    </g>
  </g>""")

    css.append(REDUCED)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
<title id="title">Nuno Amorim</title>
<desc id="desc">AI Product Engineer, Product Manager and Front-End Engineer from Braga, Portugal. Builder of Claude Code plugins and browser games.</desc>
<defs>
  <linearGradient id="name" x1="0" y1="0" x2="600" y2="0" gradientUnits="userSpaceOnUse" spreadMethod="reflect">
    <stop offset="0" stop-color="{INK}"/>
    <stop offset=".45" stop-color="{INK}"/>
    <stop offset=".6" stop-color="{TEAL}"/>
    <stop offset=".75" stop-color="{INK}"/>
    <stop offset="1" stop-color="{INK}"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="-600 0" to="600 0" dur="6s" repeatCount="indefinite"/>
  </linearGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="#FFFFFF" stroke-opacity=".045"/>
  </pattern>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
  <clipPath id="card"><rect width="{W}" height="{H}" rx="20"/></clipPath>
</defs>
<style>{''.join(css)}</style>
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <g filter="url(#blur)" opacity=".55">
    <circle class="orb" cx="180" cy="80" r="150" fill="{TEAL}"/>
    <circle class="orb b" cx="980" cy="300" r="170" fill="{VIOLET}"/>
    <circle class="orb c" cx="640" cy="40" r="110" fill="{AMBER}" opacity=".6"/>
  </g>
  <rect class="grid" width="{W + 80}" height="{H + 80}" fill="url(#grid)"/>
  <rect width="{W}" height="{H}" rx="20" fill="none" stroke="#FFFFFF" stroke-opacity=".08"/>

  <g class="rise">
    <circle class="pulse" cx="66" cy="66" r="5" fill="{TEAL}"/>
    <circle cx="66" cy="66" r="5" fill="{TEAL}"/>
    <text class="mono" x="82" y="71" font-size="14" fill="{MUTED}" letter-spacing="1.5">BRAGA, PORTUGAL · BUILDING WITH FOUNDATION MODELS</text>
  </g>
  <g class="rise" style="animation-delay:.15s">
    <text x="58" y="160" font-size="76" font-weight="800" letter-spacing="-2" fill="url(#name)">Nuno Amorim</text>
  </g>
  <g class="rise" style="animation-delay:.3s">
    <text class="mono" x="60" y="{y0}" font-size="{fs}" fill="{TEAL}" font-weight="700">&gt;</text>
    {''.join(roles_svg)}
  </g>
  <g class="rise" style="animation-delay:.45s">
    <text x="60" y="262" font-size="16" fill="{MUTED}">I don't think you understand a technology until you've built something with it.</text>
  </g>
  {''.join(chips_svg)}

  <line x1="{tx0}" y1="{trail_y + 14}" x2="{tx1}" y2="{trail_y + 14}" stroke="#FFFFFF" stroke-opacity=".06" stroke-dasharray="2 6"/>
  {''.join(dots)}
  <g class="chomper">
    <g transform="translate({tx0} {trail_y})">
      <path class="jaw-top" d="M0 0 L13 0 A13 13 0 0 0 -13 0 Z" fill="{AMBER}"/>
      <path class="jaw-bot" d="M0 0 L13 0 A13 13 0 0 1 -13 0 Z" fill="{AMBER}"/>
      <circle cx="2" cy="-6.5" r="1.8" fill="{BG}"/>
      <path class="ear" d="M-4 -12 C-14 -12 -18 -2 -15 8 C-12 6 -8 0 -4 -12 Z" fill="#7A4A26"/>
    </g>
  </g>
</g>
</svg>
"""


def divider():
    W, H = 1200, 24
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="divider">
<defs>
  <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{TEAL}" stop-opacity="0"/>
    <stop offset=".5" stop-color="{TEAL}"/>
    <stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/>
  </linearGradient>
</defs>
<style>
.beam {{ animation: sweep 5s cubic-bezier(.6,0,.4,1) infinite; }}
@keyframes sweep {{ from {{ transform: translateX(-320px); }} to {{ transform: translateX({W}px); }} }}
{REDUCED}
</style>
<rect x="0" y="11.5" width="{W}" height="1" fill="#8B949E" opacity=".25"/>
<rect class="beam" x="0" y="11" width="320" height="2" rx="1" fill="url(#g)"/>
</svg>
"""


def footer():
    W, H = 1200, 120
    waves = []
    for i, (color, op, amp) in enumerate([(TEAL, .9, 14), (VIOLET, .7, 20), (AMBER, .5, 10)]):
        mid = 82
        d = f"M0 {mid} " + " ".join(
            f"Q {150 + 300 * k} {mid - amp if k % 2 == 0 else mid + amp} {300 + 300 * k} {mid}" for k in range(8)
        )
        waves.append(f'<path class="w w{i}" d="{d}" fill="none" stroke="{color}" stroke-opacity="{op}" stroke-width="2"/>')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Thanks for stopping by">
<style>
.w {{ animation: flow 9s linear infinite; }}
.w1 {{ animation-duration: 13s; animation-direction: reverse; }}
.w2 {{ animation-duration: 17s; }}
@keyframes flow {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-600px); }} }}
text {{ font-family: {MONO}; }}
{REDUCED}
</style>
<clipPath id="c"><rect width="{W}" height="{H}" rx="20"/></clipPath>
<g clip-path="url(#c)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  {''.join(waves)}
</g>
<text x="{W / 2}" y="34" text-anchor="middle" font-size="14" fill="{INK}" letter-spacing="2">THANKS FOR STOPPING BY</text>
</svg>
"""


OUT.mkdir(parents=True, exist_ok=True)
(OUT / "header.svg").write_text(header(), encoding="utf-8")
(OUT / "divider.svg").write_text(divider(), encoding="utf-8")
(OUT / "footer.svg").write_text(footer(), encoding="utf-8")
print("ok")
