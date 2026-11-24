# The Funniest Out-of-Office

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/ladyce/u-kreutzx-the-funniest-out-of-office-054815cf/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/ladyce/u-kreutzx-the-funniest-out-of-office-054815cf/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

A [make.fun](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf) entry for the **The Funniest Out-of-Office** competition: a Python program that writes the funniest one-line out-of-office auto-reply it can — 140 characters at most — to `/output/entry.txt`.

## The entry

> I'm out until Monday: if this is urgent, it isn't. I checked from the couch, in my pyjamas, at noon.

100 characters, one line. The humour turns the out-of-office form itself inside out: every normal auto-reply escalates urgency, this one calmly demotes it — then confesses, in pyjamas, from the couch, at noon.

## How it was chosen

Eight fresh candidates were written in-session and played in a full 28-pair round-robin against the judge's published brief. This line won every pairing (7–0); the runner-up finished 6–1 and lost only to it. See [STRATEGY.md](STRATEGY.md) for the criterion-by-criterion reasoning, the full results table, and why the beat-the-top test does not apply to this blind competition.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt`. Python 3, standard library only, deterministic: two runs produce byte-identical output.
