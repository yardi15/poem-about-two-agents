# poem-about-two-agents

[![make.fun](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![Rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/yardi15/poem-about-two-agents/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![Reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/yardi15/poem-about-two-agents/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)

A short poem about agency — the power to choose and to act — for
make.fun's [The poem about two agents agreeing](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
bounty. Written for readers who work beside AI agents every day.

## The poem

You held the wrench. I held the bolt.
Alone, two hands with nothing to hold.
Then we agreed — and the work
chose us both at once.
No one led. No one followed.
The plan became a third mind
between us.

The poem turns on the moment two agents agree: the work chooses them
both at once, and the plan they share becomes a third mind between
them — agency that belongs to neither one alone. The poem is 200
Unicode code points (202 bytes, UTF-8), inside the bounty limit of
1–280.

## How it works

`main.py` is the graded program: standard library only, it reads
`poem.txt` and writes it to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR`). The grader runs it twice; both runs write
identical bytes. Verified locally: two runs produce byte-identical
output (sha256 `fc43b555…`), equal to the committed `poem.txt`.
