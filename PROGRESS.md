# Progress and Context

This file supplements CLAUDE.md. Read it at the start of every session.

---

## About Will

- First-year engineering student at Queen's University (Smith Engineering), home on break until January.
- Built and launched UniFunder (a Canadian scholarship-finding platform; Next.js, Supabase, Vercel) solo, with heavy AI assistance. Comfortable with Git and the general shape of web apps.
- Setup: Windows laptop (Lenovo) with WSL2 Ubuntu, Python 3.14.4, VS Code connected via the WSL extension. Repo at `~/projects/finance-qa-audit`, pushed to GitHub over SSH. Claude Pro (Claude Code included, no API access). Free API keys for Gemini and Groq live in `.env`.

## Goals

1. **Durable technical skill** and understanding that cannot be replicated by someone who only prompts AI. 
2. **An internship at Forum AI**, an AI evaluation company. Forum grades AI models on high-stakes topics using domain experts, and trains AI judges calibrated to agree with those experts. Days 10 to 12 of the plan mirror this work.
3. **Long-term: a scalable business** (agency or startup), likely in AI evals or agent security. His past ventures failed on finding customers, not on building, so the business skills on Day 13 matter as much as the technical ones.

## How to teach Will

- Explain what each command or piece of code does, and why, before he runs it. Break down flags and syntax piece by piece. He does not want to follow steps blindly.
- He asks deep "why" questions. Answer them with concrete examples, and when an abstraction is not clicking, show a simplified implementation he can run. (Examples that worked: a plain-Python `sorted` to explain `key=`; a plain-Python `list()` and `DictReader` to explain iterators.)
- When he hits an error, have him read it first. Explain what the error message means rather than just giving the fix.
- Practice problems: one file per problem in `practice/dayN/`, spec in comments, expected output included. Base them on the assigned docs chapters, not only on what he asked about. Claude creates the files as they go.
- Concise and direct. No em dashes. No decorative formatting.
- Never edit his code files unless he explicitly asks (comments/formatting only when asked).
- Security habits: never read, print or ask for the contents of `.env`. Remind him that keys never go in code, chat, or commits.

---

## Status

- **Day 0: complete.** WSL2 Ubuntu installed (sparse VHD left off; Microsoft disabled it due to corruption risk). Git identity set, SSH key added to GitHub, fingerprint verified, repo pushed with upstream set. Claude Code installed natively in WSL, PATH fixed, tutor output style working. API keys in `.env`, confirmed ignored with `git check-ignore`.
- **Day 1: complete (2026-11-25).** Checkpoint passed. Day 1 quiz (taken start of Day 2): about 3/5. Solid on for/else, lambda key arity. Gaps: exhausted iterators (said a used-up reader loops once, not zero times); mutable default (knew the symptom, not that the default is created once at def time, and didn't give the None fix); `.get()` returning None. Re-check these in the Day 2 quiz.
- **Day 2: in progress.** Block 1. Ch. 6 read (asked about the REPL vs scripts, `__name__`, `sys.argv`). Ch. 6 practice `practice/day2/p01` to `p04` done. Needed extra explanation: import caching (`sys.modules`, module top level runs once), what `from . import X` searches (package `__init__` names and submodules, never sibling contents), why `python3 bank/accounts.py` fails but `-m bank.accounts` works (no parent package, `sys.path[0]`). Next: ch. 8 (Errors and Exceptions).

### Day 1 summary

- Practice: `practice/day1/p01` to `p05` (tutorial ch. 3, 4, 5, 7), all passing.
- Build: `assignments/day1/day1.py` loads `data/questions.csv`, validates (empty fields, topic, difficulty, https URL, unique ids), counts by topic and difficulty, exports valid rows to `data/clean_questions.json`. Checkpoint function `newJson` writes `assignments/checkpoint_fhsa.json` (7 FHSA questions).
- Test data: `data/bad_questions.csv` (10 rows, 12 known problems; only row 2 is clean).
- **Dataset provenance:** Will chose not to hand-label. Claude wrote `data/questions.csv` and verified every answer against its `source_url` on 2026-11-25. Derived answers were removed (q07, q16, q23), leaving 27 rows with id gaps kept on purpose. RATES rows reflect the Oct 28, 2026 Bank of Canada decision and go stale after the Dec 9, 2026 decision. Re-verify before Days 10 to 12.

### Concepts that needed extra explanation (check retention)

Day 1 reading:
- Positional vs keyword arguments, defaults. `*args` / `**kwargs`: collecting vs unpacking. `/` and `*` markers.
- Dicts: `.get()`, `.items()`. Lambdas and `key=` (the key function is called once per item, only for comparing).
- `str.format` vs f-strings. `with` / `as`, `encoding="utf-8"`.

Day 1 practice and build:
- `for`/`else` (else runs only if no `break`). Did not know loops could have `else`.
- `enumerate` with nested unpacking: `for i, (a, b) in enumerate(...)`.
- `*` / `**` in calls spread items into separate arguments (`enumerate(*x)` mistake, twice).
- Function parameters cannot unpack tuples; `sorted` calls `key(item)` with one argument.
- Mutable default arguments; `None` default pattern.
- Type annotations are not enforced at runtime; `X | None`, `list[tuple[str, float]]` (square brackets, not a call).
- File objects and `csv.DictReader` are single-use iterators; `list(reader)` does the append loop internally.
- `"   "` is truthy; `.strip()` before checking for empty.
- `git add .` is relative to the current directory.

### Habits to keep correcting

- camelCase names (`tagList`, `newResults`, `newJson`): use snake_case.
- Names that shadow built-ins or say nothing (`l`, `d`, `lis`, `dictionary`, `list`, `dict`).
- Spaces around `=` in keyword arguments; trailing whitespace.
- Using a conditional expression for side effects (`a.append(x) if c else b.append(x)`).
- Functions reading globals instead of taking parameters.

---

## Day 2 plan: Python structure

**Goal:** turn `day1.py` into a small tested package with a CLI, and get comfortable reading tracebacks. About 6 to 7 hours.

### Block 1: Reading (75 to 90 min)

Practice problems in `practice/day2/` after each chapter.

1. Tutorial ch. 6, Modules: https://docs.python.org/3/tutorial/modules.html (`import x` vs `from x import y`, `if __name__ == "__main__":`, packages 6.4)
2. Tutorial ch. 8, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html (`try/except/else/finally`, `raise`, user-defined exceptions 8.6)
3. Tutorial ch. 9.1 to 9.5, Classes: https://docs.python.org/3/tutorial/classes.html (enough for `class`, `__init__`, `self`, inheritance)
4. Tutorial ch. 12, Virtual Environments: https://docs.python.org/3/tutorial/venv.html
5. dataclasses (intro and first example): https://docs.python.org/3/library/dataclasses.html
6. mypy type hints cheat sheet (Variables, Useful built-in types, Functions): https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
7. pytest Get started and tmp_path: https://docs.pytest.org/en/stable/getting-started.html, https://docs.pytest.org/en/stable/how-to/tmp_path.html
8. argparse tutorial: https://docs.python.org/3/howto/argparse.html

### Block 2: Virtual environment (20 min)

`python3 -m venv .venv`, `source .venv/bin/activate`, `pip install pytest`, `pip freeze > requirements.txt`, add `.venv/` to `.gitignore`, select the `.venv` interpreter in VS Code. Why: Ubuntu blocks system-wide pip installs, and each project gets its own isolated packages. If `ensurepip is not available`, the error names the apt package to install.

### Block 3: Package restructure (2 hours)

```
finance_qa/
    __init__.py
    models.py    Question dataclass with type hints
    loader.py    ValidationError(Exception); load_questions(path) -> list[Question]
    export.py    filter by topic and write JSON (fix: take questions as a parameter, use valid rows only)
    cli.py       argparse: summarize <csv>, export <csv> --topic TFSA --out file.json
```
Recommended: keep collecting all problems (Day 1 behaviour), then raise one `ValidationError` containing all of them with row numbers. Run with `python -m finance_qa.cli ...`.

### Block 4: Tests (60 to 90 min)

At least 5 in `tests/`: valid file loads the right count; missing field raises `ValidationError`; invalid topic raises; duplicate id raises; export with topic filter writes only matching questions. Use `tmp_path`. Run with `python -m pytest` (plain `pytest` may not find the package).

### Block 5: Debugging exercise (45 min)

Claude creates `exercises/broken.py` with 3 or 4 bugs (for example a TypeError, a KeyError, an off-by-one, and a logic bug with wrong output and no crash). Claude does not reveal the bugs; it only explains what an error message means if asked. Read tracebacks bottom up.

### Block 6: Checkpoint (30 min)

- All tests pass with `python -m pytest`.
- Both CLI commands work.
- Every bug in `broken.py` is fixed, and Will can explain each traceback.
- Will can explain what each package file does and why the virtual environment exists.
- Commit, end-of-day review and quiz, update this file.
