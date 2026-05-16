---
level: 2
session: 04
title: Reading Sensors
ages: 10–14
duration: 75 min
status: draft
---

# Session 04 — Reading Sensors

## Learning objective
Students read analog and digital sensor data into the Arduino, display it on Serial Monitor, and write their first conditional response to sensor input.

## Key concepts
- Digital input: HIGH or LOW (button, limit switch)
- Analog input: 0–1023 (potentiometer, LDR, temperature sensor)
- `digitalRead()`, `analogRead()`
- Serial Monitor: debugging tool for embedded systems
- `if / else`: decision making based on sensor value

## Activities
1. **Push-button input** (15 min) — wire button to pin 2; read state; print to Serial Monitor; LED mirrors button
2. **Potentiometer** (15 min) — wire pot to A0; read 0–1023; map to 0–255; control LED brightness via `analogWrite()`
3. **Temperature sensor** (20 min) — wire TMP36 to A1; convert raw ADC value to °C using formula; print temperature every second
4. **Smart thermostat challenge** (25 min) — if temp > 28°C, turn on fan (motor); below 28°C, turn off; students write the full sketch

## Materials
- Arduino UNO, breadboard, jumpers
- Tactile button, 10kΩ pull-down resistor
- 10kΩ potentiometer
- TMP36 temperature sensor
- Small DC motor + transistor (2N2222) + flyback diode

## Instructor notes
TMP36 voltage-to-temperature formula: `tempC = (voltage - 0.5) * 100`. Walk through the derivation — don't just give the formula.

## Next session
Session 05 — Making Things Move (servo motors, PWM, robotic arm)
