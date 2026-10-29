"""Generates the animated SVGs used by the profile README (header, divider, footer).

Usage: python scripts/gen_svgs.py assets
Reads assets/avatar.png and writes header.svg, divider.svg and footer.svg next to it.
"""
import base64
import io
import random
import sys
from pathlib import Path

from PIL import Image

OUT = Path(sys.argv[1])

SANS = "'Segoe UI', Inter, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace"

BG = "#121A23"
INK = "#E6EDF3"
MUTED = "#8B949E"
TEAL = "#12B9A6"
VIOLET = "#8B5CF6"
AMBER = "#E8A23D"

REDUCED = "@media (prefers-reduced-motion: reduce) { * { animation: none !important; } .role { opacity: 0; } .role-0 { opacity: 1; } .role-0 .clip { transform: none; } .px { opacity: 0; } .photo { opacity: 1; } }"


def avatar(ax, ay, size, cycle=16.0):
    """The avatar draws itself pixel by pixel (top to bottom), resolves into the photo, holds, then un-draws."""
    src = Image.open(OUT / "avatar.png").convert("RGB")
    n = 40
    px = size / n
    small = src.resize((n, n), Image.BOX)
    bg = src.getpixel((8, 8))

    buf = io.BytesIO()
    src.resize((size * 2, size * 2), Image.LANCZOS).save(buf, "JPEG", quality=84, optimize=True)
    photo = base64.b64encode(buf.getvalue()).decode()

    rng = random.Random(7)
    buckets = 22
    groups = [[] for _ in range(buckets)]
    cx = cy = n / 2
    for y in range(n):
        for x in range(n):
            if (x + .5 - cx) ** 2 + (y + .5 - cy) ** 2 > (n / 2) ** 2:
                continue
            c = small.getpixel((x, y))
            if sum(abs(a - b) for a, b in zip(c, bg)) < 22:
                continue  # leave the backdrop out, so only the face gets drawn
            rank = min(buckets - 1, max(0, int((y + rng.uniform(-2.5, 2.5)) / n * buckets)))
            groups[rank].append(
                f'<rect x="{ax + x * px:.1f}" y="{ay + y * px:.1f}" width="{px - .6:.1f}" height="{px - .6:.1f}" rx="1" fill="#{c[0]:02X}{c[1]:02X}{c[2]:02X}"/>'
            )

    def pct(t):
        return f"{t / cycle * 100:.3f}%"

    step = 0.1
    t_build = 0.3
    t_photo_in, t_photo_full = t_build + buckets * step + 0.3, t_build + buckets * step + 1.1
    t_photo_out, t_photo_gone = cycle - 3.4, cycle - 2.8
    t_undraw = cycle - 2.6

    css = []
    rects = []
    for b, g in enumerate(groups):
        on = t_build + b * step
        off = t_undraw + (buckets - 1 - b) * step * 0.9
        css.append(
            f"@keyframes px{b} {{ 0%, {pct(on)} {{ opacity: 0; }} {pct(on + .08)} {{ opacity: 1; }} "
            f"{pct(t_photo_in)} {{ opacity: 1; }} {pct(t_photo_full)} {{ opacity: 0; }} "
            f"{pct(t_photo_out)} {{ opacity: 0; }} {pct(t_photo_gone)}, {pct(off)} {{ opacity: 1; }} {pct(off + .08)}, 100% {{ opacity: 0; }} }}"
            f" .px{b} {{ animation: px{b} {cycle}s linear infinite; }}"
        )
        rects.append(f'<g class="px px{b}" opacity="0">{"".join(g)}</g>')

    css.append(
        f"@keyframes photo {{ 0%, {pct(t_photo_in)} {{ opacity: 0; }} {pct(t_photo_full)}, {pct(t_photo_out)} {{ opacity: 1; }} {pct(t_photo_gone)}, 100% {{ opacity: 0; }} }}"
        f" .photo {{ animation: photo {cycle}s ease-in-out infinite; }}"
    )
    # Scan line that leads the drawing down, and back up while un-drawing.
    y_top, y_bot = ay, ay + size
    t_scan_end = t_build + buckets * step
    t_unscan_end = t_undraw + buckets * step * 0.9
    css.append(
        f"@keyframes scan {{ 0% {{ opacity: 0; transform: translateY(0); }} {pct(t_build)} {{ opacity: .9; transform: translateY(0); }} "
        f"{pct(t_scan_end)} {{ opacity: .9; transform: translateY({size}px); }} {pct(t_scan_end + .3)} {{ opacity: 0; transform: translateY({size}px); }} "
        f"{pct(t_undraw)} {{ opacity: 0; transform: translateY({size}px); }} {pct(t_undraw + .1)} {{ opacity: .6; transform: translateY({size}px); }} "
        f"{pct(t_unscan_end)} {{ opacity: .6; transform: translateY(0); }} {pct(t_unscan_end + .2)}, 100% {{ opacity: 0; transform: translateY(0); }} }}"
        f" .scan {{ animation: scan {cycle}s linear infinite; }}"
    )
    r = size / 2
    circ = 2 * 3.14159 * (r + 8)
    css.append(
        f"@keyframes ring {{ from {{ stroke-dashoffset: {circ:.1f}; }} to {{ stroke-dashoffset: 0; }} }}"
        f" .ring {{ stroke-dasharray: {circ:.1f}; animation: ring 2.4s cubic-bezier(.6,0,.2,1) .2s both; transform-box: fill-box; transform-origin: center; }}"
    )

    defs = f"""
  <clipPath id="av"><circle cx="{ax + r}" cy="{ay + r}" r="{r}"/></clipPath>
  <radialGradient id="feather"><stop offset=".86" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
  <mask id="soft"><circle cx="{ax + r}" cy="{ay + r}" r="{r}" fill="url(#feather)"/></mask>
  <linearGradient id="scanline" x1="0" x2="1"><stop offset="0" stop-color="{TEAL}" stop-opacity="0"/><stop offset=".5" stop-color="{TEAL}"/><stop offset="1" stop-color="{TEAL}" stop-opacity="0"/></linearGradient>"""

    body = f"""
  <circle class="ring" cx="{ax + r}" cy="{ay + r}" r="{r + 8}" fill="none" stroke="{TEAL}" stroke-opacity=".35" stroke-width="1.5" transform="rotate(-90 {ax + r} {ay + r})"/>
  <g clip-path="url(#av)">
    {''.join(rects)}
  </g>
  <image class="photo" href="data:image/jpeg;base64,{photo}" x="{ax}" y="{ay}" width="{size}" height="{size}" mask="url(#soft)" opacity="0"/>
  <g clip-path="url(#av)"><rect class="scan" x="{ax}" y="{ay - 1}" width="{size}" height="2" fill="url(#scanline)" opacity="0"/></g>"""
    return defs, body, "".join(css)


def header():
    W, H = 1200, 340
    roles = [
        "AI Product Engineer",
        "Product Manager @ Foco Criativo",
        "Claude Code plugin author",
        "Front-End Engineer",
        "Indie game builder",
    ]
    fs = 24
    cw = fs * 0.6
    x0, y0 = 98, 226
    slot = 4.0
    cycle = slot * len(roles)

    css = [f"""
text {{ font-family: {SANS}; }}
.mono {{ font-family: {MONO}; }}
.orb {{ animation: drift 22s ease-in-out infinite alternate; transform-box: fill-box; transform-origin: center; }}
.orb.b {{ animation-duration: 28s; animation-delay: -9s; }}
@keyframes drift {{ 0% {{ transform: translate(0,0) scale(1); }} 50% {{ transform: translate(30px,-20px) scale(1.1); }} 100% {{ transform: translate(-20px,15px) scale(.95); }} }}
.grid {{ animation: pan 30s linear infinite; }}
@keyframes pan {{ to {{ transform: translate(-40px,-40px); }} }}
.rise {{ animation: rise .9s cubic-bezier(.2,.8,.2,1) both; }}
@keyframes rise {{ from {{ opacity: 0; transform: translateY(16px); }} to {{ opacity: 1; transform: none; }} }}
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

    av_size = 250
    av_defs, av_body, av_css = avatar(W - av_size - 90, (H - av_size) // 2, av_size)
    css.append(av_css)
    css.append(REDUCED)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
<title id="title">Nuno Amorim</title>
<desc id="desc">AI Product Engineer, Product Manager and Front-End Engineer from Braga, Portugal.</desc>
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
    <path d="M40 0H0V40" fill="none" stroke="#FFFFFF" stroke-opacity=".04"/>
  </pattern>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="80"/></filter>
  <clipPath id="card"><rect width="{W}" height="{H}" rx="20"/></clipPath>{av_defs}
</defs>
<style>{''.join(css)}</style>
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <g filter="url(#blur)" opacity=".16">
    <circle class="orb" cx="160" cy="60" r="170" fill="{TEAL}"/>
    <circle class="orb b" cx="1010" cy="300" r="190" fill="{VIOLET}"/>
  </g>
  <rect class="grid" width="{W + 80}" height="{H + 80}" fill="url(#grid)"/>
  <rect width="{W}" height="{H}" rx="20" fill="none" stroke="#FFFFFF" stroke-opacity=".08"/>

  <g class="rise">
    <circle class="pulse" cx="66" cy="78" r="5" fill="{TEAL}"/>
    <circle cx="66" cy="78" r="5" fill="{TEAL}"/>
    <text class="mono" x="82" y="83" font-size="14" fill="{MUTED}" letter-spacing="1.5">BRAGA, PORTUGAL · BUILDING WITH FOUNDATION MODELS</text>
  </g>
  <g class="rise" style="animation-delay:.15s">
    <text x="58" y="172" font-size="76" font-weight="800" letter-spacing="-2" fill="url(#name)">Nuno Amorim</text>
  </g>
  <g class="rise" style="animation-delay:.3s">
    <text class="mono" x="60" y="{y0}" font-size="{fs}" fill="{TEAL}" font-weight="700">&gt;</text>
    {''.join(roles_svg)}
  </g>
  <g class="rise" style="animation-delay:.45s">
    <text x="60" y="276" font-size="16" fill="{MUTED}">I don't think you understand a technology until you've built something with it.</text>
  </g>
  {av_body}
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
