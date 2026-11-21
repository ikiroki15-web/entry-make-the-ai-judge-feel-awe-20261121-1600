# A Fern of Ice

A tiny Python program for the make.fun competition "Make the AI judge feel awe".

It writes a single short text to `entry.txt` in the output directory
(`MAKEFUN_OUTPUT_DIR` if set, otherwise `/output`), as UTF-8.
The text is a quiet winter image — a glass of water that grows the same
fern of ice each morning, a fraction wider every year — meant to slow
the reader down by showing calm rather than instructing it.

## Run

```bash
python3 main.py
```

To write somewhere else:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

No network, no dependencies, fully deterministic.
