# attsis-learn — Global Attsis
**Motto:** Reliable · Efficient · Accurate · Factual · No Hallucination · Streamlined
**Template version:** 1.2.0
**GitHub:** Arvint89/attsis-learn
**Born:** 2026-05-15

---

## SESSION START (3 steps only)
1. Read `docs/product/PRODUCT.md` — know what we build and who we teach
2. Read `PENDING_TASKS.md` — execute HIGH priority first
3. Run `python scripts/smoke_test.py` — ALL checks must pass before any code

---

## BEFORE ANY CODE — 4-LAYER SDLC GATE
```
L4 PRE-BUILD  □ User story (who/what/why)  □ UX states (happy/empty/error)
              □ Risk level (LOW/MED/HIGH)   □ Test name written first
L1 UX         □ Entry → Response → Next action → Error mapped
L2 CODE       □ TDD: test file first → red → implement → green
              □ No hardcoded secrets  □ UTF-8 everywhere
L0 OPS        □ Restarts cleanly  □ Errors log to file + alert  □ Smoke test
```

---

## BEFORE ANY ACTION — PROACTIVE NOT REACTIVE
```
STOP. Before starting any task, ask:
  □ Do I know exactly what BT wants — or am I assuming?
  □ Does this action affect anything outside this local repo? (post, publish, deploy)
  □ Is this reversible? If NO → ask first, always.
  □ Am I about to do more than what was asked?

If any box is uncertain → ask one clear question before proceeding.
NEVER fill in the blanks with assumptions. ALWAYS surface the ambiguity first.
```

---

## REPO PURPOSE
attsis-learn is a static GitHub Pages site for the Attsis Learn robotics and engineering program.
- Audience: parents of children ages 6–14 in London, Ontario
- Goal: WhatsApp inquiry → free session booking
- Tech: Pure HTML + CSS + vanilla JS. No frameworks. No npm. No build tools.
- GitHub Pages source: `site/` folder on `main` branch

---

## 5 HARD RULES — NON-NEGOTIABLE
1. **No hallucination** — all course descriptions are from `content/` source files
2. **No secrets hardcoded** — `os.getenv()` only; any keys in `.env` only
3. **UTF-8 everywhere** — `encoding='utf-8'` on every `open()`
4. **PageSpeed 90+** — validate before marking any site task complete
5. **No external post without approval** — never publish without BT's explicit YES

---

## RISK GATE
| Level | Condition | Required |
|-------|-----------|----------|
| LOW | Local HTML/CSS edits, content markdown | Auto-approve |
| MEDIUM | Push to main (triggers Pages deploy) | BT reviews before push |
| HIGH | Any public-facing copy or CTA changes | BT explicit YES |

---

## COMPUTE BOUNDARY
**LOCAL (autonomous):** HTML edits, content markdown, smoke test
**CLAUDE CODE (BT session):** course plan changes, new pages, CTA updates, any public copy

---

## TREE NAVIGATION
```
site/          ← GitHub Pages source (index.html + css + js + assets)
docs/          ← internal docs (product, architecture, brief, vault)
content/       ← course session markdown (source of truth, not rendered)
memory/        ← session logs
scripts/       ← smoke_test.py
```

*Related: [[HOME]] | [[docs/product/PRODUCT]] | [[PENDING_TASKS]]*
