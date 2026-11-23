# NOTES.md — Variant B (structured Python)

## What was built
`main.py` (Python 3, stdlib only) — a structured variant of the same fixed
output as variants A and C. It defines a `USERNAME` constant
(`"coral-stork-74"`), a `validate()` function that checks the text against
the sealed scorer gate before writing, and a `main()` entry point that
creates `/output` if needed and writes the username with `newline=""`
so no newline is ever added.

## Why this structured form
Variant A is plain and minimal (constant + write). Variant B adds a
defensive layer: if the constant were ever mistyped (extra space, newline,
over 30 chars), the program fails loudly instead of silently submitting an
invalid entry that scores 0. The validation mirrors the gate exactly —
1–30 chars, not only whitespace, single word (no whitespace at all),
valid UTF-8 — plus an explicit no-newline check and an ASCII guard, since
our handle is plain ASCII and any multi-byte character would change the
byte count the tie-break uses. Same 14 bytes out, but the build is
self-checking.

## Validation results
Environment: Python 3.12.3. Note: `xxd` is not installed in this sandbox;
byte dumps below use `od -c` and a Python `repr()` check instead.

Run 1 (first version, clean /output):
- `rm -rf /output && python3 main.py` → `/output/entry.txt` = 14 bytes
- `od -c` → `c o r a l - s t o r k - 7 4`, no trailing `\n`
- `repr` → `b'coral-stork-74'`, length 14

Run 2 (same version, clean /output): identical 14 bytes,
`cmp` run1 vs run2 → identical. Two-run byte-identical: YES.

Genuine revision after the first successful run: strengthened `validate()`
— added an explicit `\n`/`\r` rejection and an `isascii()` guard.

Run 3 (revised version, clean /output): 14 bytes, same `od -c` output.
Run 4 (revised version, clean /output): 14 bytes, `cmp` run3 vs run4 →
identical. Two-run byte-identical after revision: YES.
`cmp` run1 vs run3 → identical: the revision changed validation only,
the output is unchanged (`b'coral-stork-74'`, 14 bytes, no newline).

## Files
- `main.py` — entrypoint (root)
- `README.md` — official template, 3 live make.fun badges, run `python3 main.py`
- `LICENSE` — line 1 `SPDX-License-Identifier: MIT`, then full MIT text
- `.makefun/owner.json` — wallet FT1ect39XkeTprHy44WyUFprgHZbEUxAvQkWKspfiuPH
- `NOTES.md` — this file

Committed locally with git; NOT pushed, no GitHub repo created.
No bundling, no submission — builder only.
