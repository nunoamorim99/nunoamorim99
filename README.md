<p align="center">
  <a href="https://nunoamorim.dev"><img src="assets/header.svg" width="100%" alt="Nuno Amorim — AI Product Engineer, Product Manager, Front-End Engineer. Braga, Portugal."></a>
</p>

<p align="center">
  <a href="https://nunoamorim.dev"><img src="https://img.shields.io/badge/nunoamorim.dev-12B9A6?style=for-the-badge&logo=googlechrome&logoColor=white&labelColor=1F2328" alt="Portfolio"></a>
  <a href="https://www.linkedin.com/in/nunoamorim99"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=1F2328" alt="LinkedIn"></a>
  <a href="mailto:nunomamorim99@gmail.com"><img src="https://img.shields.io/badge/Email-64748B?style=for-the-badge&logo=gmail&logoColor=white&labelColor=1F2328" alt="Email"></a>
  <a href="https://beaglechomp.nunoamorim.dev"><img src="https://img.shields.io/badge/▶_Play_Beagle_Chomp-E8A23D?style=for-the-badge&labelColor=1B1512" alt="Play Beagle Chomp"></a>
</p>

<img src="assets/divider.svg" width="100%" alt="">

### `01` — Profile

Product Manager at **Foco Criativo**, and an engineer who never stopped shipping. I came up through code - intern, Software Engineer, then Product Owner, then Product Manager, all on the same product in two years - and I still write code today. Staying close to the craft is deliberate: it means I prototype an idea instead of describing it, and I write specs engineers can actually build from.

The work I care most about right now is applied AI. Not research - **building**. Foundation models in the loop, real products, real users, and an honest read on where AI creates value versus where it's just noise.

I don't think you understand a technology until you've built something with it. Everything below is me finding out.

<img src="assets/divider.svg" width="100%" alt="">

### `02` — Claude Code plugins

If a model is part of how the team works, the product-management layer has to live where the model can actually see it. Not in Jira - in the repo. So I built it, and then kept going: five [Claude Code](https://docs.claude.com/en/docs/claude-code) plugins that cover the work around the code - ideas, sprints, stakeholder docs and product protection. Plain Markdown, no database, nothing to host.

<table>
  <tr>
    <td width="38%" align="center"><a href="https://github.com/nunoamorim99/agile-ledger-pro"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/logos/agile-ledger-pro-dark.svg"><img src="assets/logos/agile-ledger-pro-light.svg" height="46" alt="Agile-Ledger Pro"></picture></a><br/><sub><b>NEW</b> · flagship</sub></td>
    <td valign="top">The next generation of Agile-Ledger. Backlog, sprints, board, velocity, releases and bug tracking from <b>34 slash commands</b> - or from a <b>local dashboard</b> in the browser. Adds <code>/insights</code> for velocity, forecast and flow, a lossless switch between <b>Scrum and Kanban</b>, and per-person identity for teams sharing one ledger repo.</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/nunoamorim99/agile-ledger"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/logos/agile-ledger-dark.svg"><img src="assets/logos/agile-ledger-light.svg" height="46" alt="Agile-Ledger"></picture></a></td>
    <td valign="top">The full Scrum lifecycle - ideas → epics → sprints → releases, plus bugs - as plain Markdown in a dedicated ledger repo. GitHub holds the code; this holds the <i>why</i>, joined by the user-story ID through every branch, commit and PR.</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/nunoamorim99/idea-ledger"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/logos/idea-ledger-dark.svg"><img src="assets/logos/idea-ledger-light.svg" height="46" alt="Idea-Ledger"></picture></a></td>
    <td valign="top">Capture ideas mid-work with <code>/idea</code>, track how each one evolves, version what ships - in two Markdown files. One invariant: nothing is ever deleted.</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/nunoamorim99/cartographer"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/logos/cartographer-dark.svg"><img src="assets/logos/cartographer-light.svg" height="46" alt="Cartographer"></picture></a></td>
    <td valign="top">Reads a project's repos and writes the stakeholder docs nobody wants to write - what each product does, never how it's built. Audience-aware Markdown + PDF, with staleness checks.</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/nunoamorim99/fortify"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/logos/fortify-dark.svg"><img src="assets/logos/fortify-light.svg" height="46" alt="Fortify"></picture></a><br/><sub><b>NEW</b></sub></td>
    <td valign="top">How easily can your product be reverse engineered, cracked, scraped or cloned? A read-only scan, a full audit across <b>five clone vectors</b> with a tiered protection plan in plain language, and a harden step that applies fixes one reviewable change at a time. Defensive only, <b>15 platforms</b>.</td>
  </tr>
</table>

All five live in one marketplace - [`nunoamorim99/claude-skills`](https://github.com/nunoamorim99/claude-skills):

```
/plugin marketplace add nunoamorim99/claude-skills
/plugin install agile-ledger-pro@nunoamorim99
```

<img src="assets/divider.svg" width="100%" alt="">

### `03` — Games

Games are unforgiving in a way that CRUD apps aren't: the loop either works or it doesn't, and no architecture diagram saves you. All three were built with a model in the loop, which was half the point - finding out where it excels as a coding partner and where it needs steering.

<p align="center">
  <a href="https://beaglechomp.nunoamorim.dev"><img src="assets/beagle-chomp/hero.png" width="100%" alt="Beagle Chomp"></a>
</p>

<h3 align="center"><a href="https://beaglechomp.nunoamorim.dev">Beagle Chomp</a> &nbsp;<sub><sup>NEW</sup></sub></h3>

<p align="center"><i>A 3D maze chase where every single pixel is drawn in code.</i></p>

<p align="center">
  <img src="assets/beagle-chomp/menu.webp" width="24%" alt="Main menu: the beagle in a garden under a hedge arch">
  <img src="assets/beagle-chomp/gameplay-phone.webp" width="24%" alt="Gameplay on a phone: the hedge maze from above">
  <img src="assets/beagle-chomp/journey.webp" width="24%" alt="The Journey: forty levels as a chain of islands">
  <img src="assets/beagle-chomp/shop-beagles.webp" width="24%" alt="The shop: beagle coats and their powers">
</p>

It started as an excuse to learn three.js by building something real with it - a classic maze-chase, remade in 3D, starring the beagle my partner and I keep saying we'll get. Then the product side kicked in: a leaderboard whose scores can be trusted, a shop that sells *dogs* with powers instead of skins, a challenge ladder, and player accounts that collect no personal data. When I hit the wall of shaping a character by typing coordinates, I built the editor I was missing.

<table>
  <tr>
    <td align="center"><b>0</b><br/><sub>model, texture or<br/>audio files shipped</sub></td>
    <td align="center"><b>36</b><br/><sub>mazes</sub></td>
    <td align="center"><b>40</b><br/><sub>Journey levels</sub></td>
    <td align="center"><b>114</b><br/><sub>challenges</sub></td>
    <td align="center"><b>8</b><br/><sub>worlds, each with<br/>its own soundscape</sub></td>
    <td align="center"><b>~1,600</b><br/><sub>test assertions</sub></td>
  </tr>
</table>

- **Everything is generated at runtime.** Characters are sculpted from swept solids and revolved profiles, surfaces are painted to a canvas, and ~1,600 lines of Web Audio synthesise every sound and ambient bed.
- **The game logic never imports three.js.** It's pure TypeScript that runs headless in Node - which is how the server can reuse the game's own rules to validate every submitted score.
- **Full-stack since v5.** Installable PWA on the front, a Hono + PostgreSQL API behind it, deployed on Cloudflare Pages and Hetzner.

<sub>TypeScript · three.js · Vite · PWA · Web Audio · Canvas 2D · Hono · PostgreSQL · Zod · argon2id · Playwright · Docker</sub>

<p align="center">
  <a href="https://beaglechomp.nunoamorim.dev"><b>▶ Play it</b></a> &nbsp;·&nbsp; <a href="https://github.com/nunoamorim99/beagle-chomp">Source</a> &nbsp;·&nbsp; <a href="https://nunoamorim.dev">Case study</a>
</p>

<br/>

<table>
  <tr>
    <td width="50%"><a href="https://nunoamorim99.github.io/nibble/"><img src="assets/nibble.png" alt="Nibble"></a></td>
    <td width="50%"><a href="https://nunoamorim99.github.io/AstroHop/"><img src="assets/astrocover.jpeg" alt="Astro Hop"></a></td>
  </tr>
  <tr>
    <td valign="top"><b><a href="https://github.com/nunoamorim99/nibble">Nibble</a></b> &nbsp;<a href="https://nunoamorim99.github.io/nibble/">▶ play</a><br/><sub>The Nokia snake, evolved into a neon PWA - Classic and Level modes, composable challenge modifiers, a coin economy for themes and skins, and a Supabase-backed global leaderboard. A deterministic, fully unit-tested engine, built with eight specialised Claude Code subagents.<br/><br/>TypeScript · Canvas · Vite · Vitest · Supabase</sub></td>
    <td valign="top"><b><a href="https://github.com/nunoamorim99/AstroHop">Astro Hop</a></b> &nbsp;<a href="https://nunoamorim99.github.io/AstroHop/">▶ play</a><br/><sub>A retro 2D platformer, and an excuse to learn game feel properly - power-up state machines, tilemap levels, mobile touch controls, and every sound synthesised live with the Web Audio API. Zero audio files.<br/><br/>Phaser 3 · Vite · Web Audio</sub></td>
  </tr>
</table>

<img src="assets/divider.svg" width="100%" alt="">

### `04` — Product

<table>
  <tr>
    <td width="45%"><img src="assets/movize.png" alt="Movize"></td>
    <td valign="top"><b>Movize</b> — a multimodal mobility ecosystem at Foco Criativo.<br/><br/>A passenger app for iOS and Android, the public web app and website, and the <b>Movize Connect</b> operator platform with its GTFS editor, street furniture &amp; sensors and events modules. I own the roadmap end to end, run discovery and validation, and still ship front-end code for it.<br/><br/>Closed source, so it isn't here - the story is in my <a href="https://nunoamorim.dev">portfolio</a>.</td>
  </tr>
</table>

<img src="assets/divider.svg" width="100%" alt="">

### `05` — Stack

<sub>**Languages**</sub><br/>
<img src="https://skillicons.dev/icons?i=ts,js,python,html,css&theme=dark" alt="TypeScript, JavaScript, Python, HTML, CSS">

<sub>**Front-end, 3D & games**</sub><br/>
<img src="https://skillicons.dev/icons?i=vue,react,nextjs,vite,tailwind,threejs&theme=dark" alt="Vue, React, Next.js, Vite, Tailwind, three.js"><br/>
<img src="https://img.shields.io/badge/React_Native-1F2328?style=flat-square&logo=react&logoColor=61DAFB">
<img src="https://img.shields.io/badge/GSAP-1F2328?style=flat-square&logo=greensock&logoColor=88CE02">
<img src="https://img.shields.io/badge/Phaser-1F2328?style=flat-square&logoColor=8B5CF6">
<img src="https://img.shields.io/badge/Web_Audio_API-1F2328?style=flat-square&logoColor=E8A23D">
<img src="https://img.shields.io/badge/Canvas_2D-1F2328?style=flat-square&logoColor=FFFFFF">
<img src="https://img.shields.io/badge/PWA-1F2328?style=flat-square&logo=pwa&logoColor=5A0FC8">

<sub>**Back-end & data**</sub><br/>
<img src="https://skillicons.dev/icons?i=nodejs,postgres,supabase&theme=dark" alt="Node.js, PostgreSQL, Supabase"><br/>
<img src="https://img.shields.io/badge/Hono-1F2328?style=flat-square&logo=hono&logoColor=E36002">
<img src="https://img.shields.io/badge/Zod-1F2328?style=flat-square&logo=zod&logoColor=3E67B1">

<sub>**Testing, infra & delivery**</sub><br/>
<img src="https://skillicons.dev/icons?i=vitest,docker,cloudflare,githubactions,git&theme=dark" alt="Vitest, Docker, Cloudflare, GitHub Actions, Git"><br/>
<img src="https://img.shields.io/badge/Playwright-1F2328?style=flat-square&logoColor=2EAD33">
<img src="https://img.shields.io/badge/Hetzner-1F2328?style=flat-square&logo=hetzner&logoColor=D50C2D">
<img src="https://img.shields.io/badge/Dokploy-1F2328?style=flat-square&logoColor=FFFFFF">

<sub>**AI, product & design**</sub><br/>
<img src="https://skillicons.dev/icons?i=figma&theme=dark" alt="Figma"><br/>
<img src="https://img.shields.io/badge/Claude_Code-1F2328?style=flat-square&logo=anthropic&logoColor=D97757">
<img src="https://img.shields.io/badge/Jira-1F2328?style=flat-square&logo=jira&logoColor=0052CC">
<img src="https://img.shields.io/badge/Scrum_%26_Kanban-1F2328?style=flat-square&logoColor=FFFFFF">

<img src="assets/divider.svg" width="100%" alt="">

### `06` — Credentials

**M.Sc. Information Systems Engineering & Management** · Universidade do Minho<br/>
**IBM AI Product Manager** · **IBM Product Owner** · **Microsoft UX Design** · Professional Certificates

<img src="assets/divider.svg" width="100%" alt="">

<p align="center"><sub>My contribution graph, as a snake sees it - a nod to <a href="https://github.com/nunoamorim99/nibble">Nibble</a>.</sub></p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/nunoamorim99/nunoamorim99/output/github-contribution-grid-snake-dark.svg">
    <img src="https://raw.githubusercontent.com/nunoamorim99/nunoamorim99/output/github-contribution-grid-snake.svg" width="100%" alt="Snake eating my contribution graph">
  </picture>
</p>

<p align="center">
  <img src="assets/footer.svg" width="100%" alt="Thanks for stopping by">
</p>

<p align="center">
  <sub>Portuguese (native) · English (fluent) &nbsp;&middot;&nbsp; open to conversations about building with AI</sub>
</p>
