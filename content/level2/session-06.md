---
level: 2
session: 06
title: Programming Logic
ages: 10–14
duration: 75 min
status: draft
---

# Session 06 — Programming Logic

## Learning objective
Students write well-structured Arduino sketches using functions, loops, and nested conditionals; understand why functions reduce repetition; and read and debug unfamiliar code.

## Key concepts
- `for` loop: repeating actions a known number of times
- `while` loop: repeating until a condition changes
- Functions: defining, calling, parameters, return values
- Nested `if`: multi-condition decision trees
- Code readability: naming variables and functions for humans, not just compilers

## Activities
1. **Refactor challenge** (20 min) — students receive a working but repetitive 60-line sketch; refactor into functions in under 20 lines; both must produce identical behaviour
2. **Loop patterns** (15 min) — `for` loop: LED counts from 1 to 10 in binary on 4 LEDs; discuss binary representation
3. **State machine intro** (20 min) — traffic light rewritten as a state machine using `switch/case`; students compare to their Session 03 version
4. **Debug race** (20 min) — instructor introduces three bugs (one syntax, one logic, one off-by-one); pairs race to find all three and explain each root cause

## Materials
- Arduino UNO, 4 LEDs, resistors
- Printed "refactor challenge" code listing

## Instructor notes
The refactor challenge is more valuable than new hardware. Writing clean code is a professional skill — treat it that way.

## Next session
Session 07 — Design Challenge (two-session project build begins)
