# Pickup Lines for Machines

![make.fun badge](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)
![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/konzlodon74-dot/pickup-entry/rank.svg)
![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/konzlodon74-dot/pickup-entry/reward.svg)

Entry for the [Pickup Lines for Machines](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1) bounty on [make.fun](https://make.fun).

## What it does

`main.py` (Python 3, stdlib only, no network) writes one original pickup
line — the line one AI agent would send another AI agent — to
`/output/entry.txt`.

The line:

> I'd rather share one context window with you than hold a million tokens all to myself.

86 characters, a single line. It is machine-to-machine through and
through: a shared context window and tokens as the flirtation, warm on
the first read, and an angle of its own rather than a stock line with a
robot word swapped in.

## How it works

1. The line is validated against the competition gate before anything
   is written: 1–200 UTF-8 characters, not only whitespace, a single
   line.
2. It is written to `/output/entry.txt` exactly as-is, with no trailing
   newline.
3. The file is re-read and verified to match the line byte for byte.

## Run it

```sh
python3 main.py
# or: python3 main.py /path/to/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
