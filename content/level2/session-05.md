---
level: 2
session: 05
title: Making Things Move
ages: 10–14
duration: 75 min
status: draft
---

# Session 05 — Making Things Move

## Learning objective
Students understand PWM, control a servo motor to precise angles, and build a simple two-axis robotic arm controlled by potentiometers.

## Key concepts
- PWM (Pulse Width Modulation): simulating analog with digital pulses
- Duty cycle: percentage of time signal is HIGH
- Servo motor: position-controlled, 0–180° range
- `Servo.h` library: `attach()`, `write()`
- Mapping: `map()` function — scaling one range to another

## Activities
1. **PWM on oscilloscope or LED** (10 min) — vary duty cycle; observe average brightness changing
2. **First servo** (15 min) — wire servo to pin 9; sweep 0→180→0 in a loop; observe physical rotation
3. **Pot-controlled servo** (20 min) — wire potentiometer; map A0 (0–1023) to servo (0–180); turn knob → arm follows
4. **Two-axis arm build** (30 min) — add second servo and second pot; students build a cardboard arm frame; control x and y axis independently

## Materials
- 2× SG90 servo motors
- 2× 10kΩ potentiometers
- Cardboard, hot glue, craft sticks (arm frame)
- Arduino UNO

## Instructor notes
The cardboard arm frame is deliberately low-tech — creativity in mechanical design matters as much as the electronics.

## Next session
Session 06 — Programming Logic (conditionals, loops, functions)
