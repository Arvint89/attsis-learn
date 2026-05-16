# /commit

Run smoke test, stage all tracked files, commit with a conventional message.

```bash
python scripts/smoke_test.py && git add -u && git status
```

Then write commit message following: `type: short description`
Types: feat | fix | content | site | docs | chore
