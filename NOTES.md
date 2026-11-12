# NOTES — news-summary-01 entry

Built 2026-11-12 (WITA) for the make.fun news-summary-01 competition
(deadline 2026-11-12T18:30Z). Program: `main.py` (Python 3.13-compatible,
stdlib only) writes `summary.txt` byte-for-byte to the output directory
(`$MAKEFUN_OUTPUT_DIR` or `/output`).

## The summary

- **1,968 Unicode code points** (1,968 bytes, pure ASCII), no trailing
  newline, well inside the gate's 1–2,000 limit.
- 10 stories, wire style, ordered by importance, source outlet named per
  story, unconfirmed items flagged as claims/reports.

## Story list and sources (each verified against ≥2 independent outlets)

1. **Abu Dhabi talks end** — Russia & Ukraine agreed in principle to a large
   prisoner-of-war exchange (Kushner: the war's biggest), no ceasefire or
   territorial deal. Sources: Associated Press, Reuters, BBC.
2. **Iran / Strait of Hormuz** — security chief Mohsen Rezaei: Tehran awaits
   a US answer to its seven conditions for reopening Hormuz; IRGC *claimed*
   three tankers caught fire after hitting naval mines; monitoring firms
   counted ≥37 ship attacks near the strait in November, a wartime monthly
   high. Sources: Al Jazeera, Just Security roundup.
3. **US charges over Iran-backed plots** — DOJ charged three operatives over
   nearly 20 plots in the US & Europe, incl. a September plot against US
   aircraft at RAF Fairford. Sources: BBC, Just Security.
4. **COP31 opens in Antalya** — Leaders Summit opened Wed 11 Nov; Erdoğan's
   "35 by 35" electrification push; Guterres urged faster action; US absent
   again. Sources: Reuters (via BusinessWorld), UNFCCC.
5. **DR Congo Ebola** — 11,042 confirmed cases, at least 5,387 deaths
   (government data), Bundibugyo strain, second-largest outbreak on record.
   Sources: Reuters (via CNBC Africa / Economic Times Health), Rest of World.
6. **Mississippi Senate race called** — AP called it Wed 11 Nov for Democrat
   Scott Colom over Sen. Cindy Hyde-Smith by 4,669 votes; first Black senator
   from Mississippi since 1881. Sources: AP, Al Jazeera, CBS.
7. **Hegseth impeachment shelved** — US House voted 211–204 to refer the
   resolution to the Judiciary Committee. Sources: BBC, Rest of World.
8. **US October CPI** — consumer prices +0.4% m/m, core +0.3%, both above
   forecasts, strengthening December Fed hike expectations. Sources: BLS via
   CNBC, NY Post.
9. **El Salvador / Haiti strike** — Bukele said Salvadoran & Haitian forces
   destroyed the 400 Mawozo gang HQ near Port-au-Prince; leader survived;
   reported ~20 deaths unconfirmed (flagged as such in the text).
   Sources: AFP, AP, BBC.
10. **Seongnam bus crash** — a bus ploughed into 32 vehicles in Seongnam,
    South Korea; 57 injured, nine seriously. Sources: Reuters, Yonhap.

Dropped after checking: NATO Baltic drone scramble and Israel's new Knesset
(single-source), the US Army officer arrest in Britain (weak outlets),
Trump's BBC case (a Tuesday court ruling, less consequential), Gaza and
Yemen tolls (figures differed between roundups).

## Validation (local, Python 3.12.3 — code is 3.13-compatible)

- `MAKEFUN_OUTPUT_DIR=<scratch> python3 main.py`, run twice:
  - run 1 output == `summary.txt` bytes: **True**
  - run 2 output == run 1 bytes (deterministic): **True**
  - 1,968 code points, ≥1 non-whitespace, within 1–2,000: **True**
- `main.py` was written, validated, then revised once (added a gate
  self-check in `load_summary()`), then re-validated with the same results.

## grade-local

`node cli/makefun.mjs grade-local --kit . --bot <repo> --driver process`
(from the kit, NODE_USE_ENV_PROXY=1) →
**refused**: "news-summary-01 is a program/v1 competition: its scorer and
reference data are not published in the kit, so the house grades it from its
competition directory". As the RULES state, this competition has no local
grade; the server grades it.

## bundle --dry-run (run once, 2026-11-12)

`node cli/makefun.mjs bundle --dry-run --repo ~/workspace/makefun/repos/news-summary-01`
(from the kit) →
**"makefun bundle: /home/hatch/workspace/makefun/repos/news-summary-01 is
not inside a git repository"** — the tool aborted at the git check and
reported **no session files**. Session discovery therefore remains untested
until the directory is a git repository (the parent agent's GitHub step);
re-run the dry-run after `git init`/commit to see which sessions it finds.

## Not done here (parent agent's steps)

No git init/commit, no GitHub repo, no `.makefun/owner.json`, no submission —
per instructions.
