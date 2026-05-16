---
level: 2
session: 03
title: Meet the Microcontroller
ages: 10–14
duration: 75 min
status: draft
---

# Session 03 — Meet the Microcontroller

## Learning objective
Students understand what a microcontroller is, navigate the Arduino IDE, write and upload their first sketch, and can control an LED from code.

## Key concepts
- Microcontroller vs computer: no OS, runs one program, real-time
- Arduino UNO: pin layout, digital vs analog, power pins, USB
- Arduino sketch structure: `setup()` runs once, `loop()` runs forever
- Digital output: `pinMode()`, `digitalWrite()`, `HIGH` / `LOW`
- `delay()`: blocking time

## Activities
1. **What is a microcontroller?** (10 min) — where they appear: microwave, car ABS, thermostat, cardiac pacemaker
2. **IDE tour** (10 min) — open IDE, verify board + port, compile the built-in Blink example
3. **Blink it** (15 min) — upload Blink to board; LED blinks; students modify delay values and observe
4. **External LED** (20 min) — wire an external LED on breadboard; control from pin 13; write the sketch from scratch (no copy-paste)
5. **Traffic light challenge** (20 min) — three LEDs (red, yellow, green); write a traffic light sequence with correct timing

## Materials
- Arduino UNO + USB cable (1 per student)
- Breadboard, LEDs, 330Ω resistors, jumper wires

## Instructor notes
No copy-paste allowed. If students type it, they read it. Typos are learning opportunities — let them find their own before helping.

## Next session
Session 04 — Reading Sensors (analog and digital inputs)
