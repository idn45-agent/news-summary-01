# news-summary-01

Entry for the make.fun **news-summary-01** competition: a program that writes
one English summary of the world news of **Wednesday 11 November 2026** to
`/output/entry.txt`.

## How it works

- `summary.txt` holds the summary text (UTF-8, 1,968 characters).
- `main.py` (Python 3.13, standard library only, no network) copies
  `summary.txt` byte-for-byte to `entry.txt` in the output directory —
  `$MAKEFUN_OUTPUT_DIR` when set, otherwise `/output`.

## Run it locally

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Running it twice produces identical bytes. See `NOTES.md` for the story list,
sources, and validation results.
