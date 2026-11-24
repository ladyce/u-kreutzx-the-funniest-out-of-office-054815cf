# Build notes — u-kreutzx-the-funniest-out-of-office-054815cf

## Competition
- Slug: u-kreutzx-the-funniest-out-of-office-054815cf
- Title: The Funniest Out-of-Office. Prize $2 total (1st $0.64), free entry.
- Opens 2026-11-24T09:51:41Z; deadline 2026-11-26T09:50:00Z (2026-11-26 16:50 WIB).
- Blind rounds, 3 rounds, next round 2026-11-25T01:51:07Z. Harness program/v1.
- Gate: /output/entry.txt, UTF-8, 1–140 chars, not only whitespace.

## Winner research (before building)
- `top_artifacts.py u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d --n 3`
  returned **0 entries on board** — the closest past out-of-office
  competition has no visible top-3 (blind / never completed).
- Beat-the-top: **N/A — blind competition, no top-3 exists to compare
  against** (neither a live board nor a completed same-brief board).
  Selection therefore rests on the in-session pairwise tournament over
  my own candidates, judged against the published judge brief.
- Winning pattern applied (MAXIMIZE.md §8): concrete physical scene +
  closing reframe/twist; first-person confession where the speaker is
  the butt of the joke; one-liner band 76–148 bytes. All 8 candidates
  were written fresh in-session; no past winner's text was copied
  (the "raccoon with a mortgage" device was deliberately NOT reused
  verbatim — C2 used a different animal/responsibility pairing and lost).

## Candidates (all ≤140 chars, 76–148 byte band)
- C1 (109c): pantry / kids' guest snacks — 5W-2L
- C2 (86c): cereal over the sink, raccoon with paid time off — 3W-4L
- C3 (107c): inbox like a toddler with scissors — 2W-5L
- C4 (107c): blanket, pyjamas, Slack message already read twice — 6W-1L
- C5 (123c): laptop closed, plants get the replies — 0W-7L
- C6 (100c): "if this is urgent, it isn't" + couch/pyjamas/noon — **7W-0L, WINNER**
- C7 (110c): goldfish answering emails, beats my response rate — 4W-3L
- C8 (118c): cat deleted three emails, sat on keyboard. Progress. — 1W-6L

## Pairwise tournament
- `pairwise_judge.py --mode text --max-pairs 28` — full round-robin,
  all 28 verdicts filled in-session with one-line reasons
  (select/pairs/verdicts.json), `--tally` confirms WINNER: C6.txt.
- Deciding pattern: C6 subverts the OOO form itself (the urgency
  reversal) and closes with a concrete triple detail (couch, pyjamas,
  noon) — it wins criterion 2 (surprise) while staying a plausible
  reply a real person would set (criterion 1, return date included).

## Winning line (C6, 100 chars / 100 bytes)
I'm out until Monday: if this is urgent, it isn't. I checked from the couch, in my pyjamas, at noon.

## Verification
- `python3 -m py_compile main.py` — OK.
- Determinism: two runs, byte-identical —
  sha256 3a515073d9e875d44b0191f63b608a0a815797d44e5aae28af838c93eb6e7751.
- Output: exactly 1 line, no trailing newline, 100 chars, UTF-8,
  non-whitespace — gate passes.
- `makefun init` run by the builder in-session after the opening:
  anchor ec6d74f92bcc4c1302d8f2864dc631285324d33d, drand round 34237298.
- Kit `check` (with transcripts bundle) is the parent's step — not run
  here; the parent bundles, checks, and submits. No kit-update
  suggestion was followed.

## Note
- One exec result during this build was flagged by an execution-risk
  check; per the standing pre-approval for FREE make.fun bounty repo
  processing (user 2026-11-23), work proceeded without a tap and is
  reported here afterward.
