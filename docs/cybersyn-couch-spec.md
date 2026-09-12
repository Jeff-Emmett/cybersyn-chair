# Cybersyn Couch — Comprehensive Specification & Build Plan

> A two-seater cybernetically controlled couch inspired by the Cybersyn Operations Room,
> with dual independent joysticks, a shared control dashboard, and programmable
> easter egg systems. Designed for two operators who can each drive their side
> independently — or swap control at the flick of a switch.

```
  ╔══════════════════════════════════════════════════════════════════════╗
  ║                     CYBERSYN COUCH — TOP VIEW                      ║
  ║                                                                     ║
  ║   LEFT ARM            SHARED CENTER             RIGHT ARM           ║
  ║  ┌─────────┐     ┌──────────────────┐      ┌─────────┐            ║
  ║  │ ◎ JOY-L │     │  DASHBOARD PANEL │      │ JOY-R ◎ │            ║
  ║  │         │     │  [🔊][💡][🎵][⚡]│      │         │            ║
  ║  │ [BTN]×4 │     │  ┌──OLED─────┐  │      │ [BTN]×4 │            ║
  ║  │ [SWITCH]│     │  │ STATUS    │  │      │[SWITCH] │            ║
  ║  │         │     │  └───────────┘  │      │         │            ║
  ║  └────┬────┘     │  [SWAP L↔R]     │      └────┬────┘            ║
  ║       │          │  [MODE SELECT]  │           │                 ║
  ║  ┌────┴──────────┴──────┬──────────┴───────────┴────┐            ║
  ║  │                      │                           │            ║
  ║  │    SEAT - LEFT       │      SEAT - RIGHT         │            ║
  ║  │    OCCUPANT          │      OCCUPANT              │            ║
  ║  │                      │                           │            ║
  ║  └──────────────────────┴───────────────────────────┘            ║
  ║                         │                                        ║
  ║                    ┌────┴────┐                                   ║
  ║                    │PEDESTAL │                                   ║
  ║                    │  BASE   │                                   ║
  ║                    └─────────┘                                   ║
  ╚══════════════════════════════════════════════════════════════════════╝
```

---

## Table of Contents

1. [Design Philosophy](#1-design-philosophy)
2. [Physical Specifications](#2-physical-specifications)
3. [Joystick System](#3-joystick-system)
4. [Control Dashboard](#4-control-dashboard)
5. [Electronics Architecture](#5-electronics-architecture)
6. [Software Architecture](#6-software-architecture)
7. [Easter Egg System](#7-easter-egg-system)
8. [Bill of Materials](#8-bill-of-materials)
9. [Build Phases](#9-build-phases)
10. [Manufacturing](#10-manufacturing)
11. [Safety & Power](#11-safety--power)

---

## 1. Design Philosophy

### Core Principles

| Principle | Description |
|-----------|-------------|
| **Dual Sovereignty** | Each occupant has full, independent control of their joystick side |
| **Democratic Switching** | Either person can propose a control swap; both must confirm (or one button overrides) |
| **Cybernetic Feedback** | Every action produces multimodal feedback: visual (LEDs), auditory (clicks/tones), haptic (vibration) |
| **No Dead Controls** | Every button does *something* — even if it's a hidden easter egg |
| **Accessible by Default** | Large buttons, intuitive joystick, no keyboard needed (honoring the original Cybersyn ethos) |
| **Modular & Hackable** | All modules hot-swappable, all protocols open, all firmware flashable |

### Aesthetic Language

- **Shell**: White or off-white fiberglass with smooth compound curves
- **Upholstery**: Burnt orange (Pantone 1665 C) — faithful to the original Opsroom
- **Controls**: Backlit buttons in amber/orange, with contrasting dark bezels
- **Displays**: Monochrome OLED with green-on-black (retro terminal aesthetic)
- **Joysticks**: Matte black anodized aluminum shafts, orange silicone grip boots
- **Accent Lighting**: Addressable RGB LED strips under armrests and base (default: warm amber)

---

## 2. Physical Specifications

### Overall Dimensions

```
                    ← ─ ─ ─ 1800mm (71") ─ ─ ─ →

              ┌──────────────────────────────────────┐  ─┬─
              │         BACKREST (curved)             │   │
              │                                      │   │ 850mm
  200mm arm → ├──┐                              ┌──┤   │ (33")
  width       │  │     SEAT SURFACE             │  │   │ seat height
              │  │  ┌────────────────────────┐  │  │   │ 420mm
              │  │  │                        │  │  │   │
              │  ├──┤    800mm seat depth     ├──┤  │  ─┴─
              └──┘  └────────────────────────┘  └──┘
                    ← ─ ─ 1400mm seating ─ ─ →
```

| Dimension | Measurement | Notes |
|-----------|-------------|-------|
| **Overall width** | 1800 mm (71") | Includes armrests |
| **Seating width** | 1400 mm (55") | Two adults comfortably |
| **Seat depth** | 500 mm (20") | Standard loveseat depth |
| **Seat height** | 420 mm (16.5") | From floor to seat surface |
| **Backrest height** | 850 mm (33.5") | From floor to top of backrest |
| **Armrest height** | 620 mm (24.4") | From floor to armrest top surface |
| **Armrest width** | 200 mm (7.9") | Wide enough for joystick + buttons |
| **Armrest depth** | 450 mm (17.7") | Front edge to backrest junction |
| **Center console width** | 250 mm (9.8") | Between seats, houses dashboard |
| **Base diameter** | 700 mm (27.5") | Pedestal footprint |
| **Weight (target)** | 45-55 kg (100-120 lbs) | Including all electronics |

### Shell Construction

The couch shell is a single fiberglass monocoque with five integrated zones:

```
  ┌─────────────────────────────────────────────────────┐
  │                                                     │
  │  1. BACKREST                                        │
  │     • Gentle S-curve lumbar support                 │
  │     • 15° recline angle                             │
  │     • Internal cable routing channels               │
  │                                                     │
  ├───┐                                           ┌───┤
  │ 2.│  3. LEFT SEAT    4. RIGHT SEAT            │ 5.│
  │ARM│     • Independent     • Independent       │ARM│
  │ L │       cushion           cushion            │ R │
  │   │                                           │   │
  │   │           CENTER CONSOLE                  │   │
  │   │           (raised 30mm above seat)        │   │
  └───┴───────────────────────────────────────────┴───┘
```

**Zone 2 & 5 (Armrests)** each contain:
- Joystick mount cavity (100 × 100 × 80mm deep)
- Button panel recess (150 × 120 × 15mm deep)
- Electronics bay (200 × 150 × 60mm deep, accessed from underside)
- Cable channel to center console & base

**Center Console (between zones 3 & 4)** contains:
- Dashboard panel recess (220 × 180mm)
- OLED display mount
- Main swap/mode switches
- Shared cup holder (removable, covers electronics bay when needed)

---

## 3. Joystick System

### Overview

Each armrest has a 2-axis analog joystick with a pushbutton top. The joysticks control
independent "sides" by default but can be swapped, merged, or remapped.

### Joystick Hardware

| Spec | Value |
|------|-------|
| **Type** | Hall-effect 2-axis analog + push button |
| **Travel** | ±25° from center |
| **Shaft** | 120mm tall, 12mm diameter, anodized aluminum |
| **Grip** | 35mm diameter knob, orange silicone overmold |
| **Mounting** | M4 bolt pattern, 60mm square, drop-in from above |
| **Output** | 2× analog (0-3.3V per axis), 1× digital (push) |
| **Centering** | Spring-return to center (adjustable tension) |
| **Recommended part** | Megatron MJ series industrial joystick, or RobotShop 2-axis hall-effect |
| **DIY option** | 2× KY-023 modules in gimbal housing (budget path) |

### Control Modes

```
┌──────────────────────────────────────────────────────────────┐
│                    JOYSTICK CONTROL MODES                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  MODE 1: INDEPENDENT (default)                               │
│  ┌─────────┐                          ┌─────────┐           │
│  │ JOY-L   │ → controls LEFT side     │ JOY-R   │→ RIGHT   │
│  │ (Seat A)│   (lights zone L,        │ (Seat B)│  side    │
│  │         │    music channel L,      │         │          │
│  │         │    display L)            │         │          │
│  └─────────┘                          └─────────┘           │
│                                                              │
│  MODE 2: SWAPPED                                             │
│  ┌─────────┐                          ┌─────────┐           │
│  │ JOY-L   │ → controls RIGHT side    │ JOY-R   │→ LEFT    │
│  │ (Seat A)│   (cross-control)        │ (Seat B)│  side    │
│  └─────────┘                          └─────────┘           │
│                                                              │
│  MODE 3: MERGED (cooperative)                                │
│  ┌─────────┐                          ┌─────────┐           │
│  │ JOY-L   │ → X axis (pan)          │ JOY-R   │→ Y axis  │
│  │         │                          │         │  (tilt)  │
│  └─────────┘                          └─────────┘           │
│  Both joysticks control the SAME output as a merged 2D input │
│                                                              │
│  MODE 4: PILOT / CO-PILOT                                    │
│  ┌─────────┐                          ┌─────────┐           │
│  │ JOY-L   │ → FULL CONTROL          │ JOY-R   │→ override│
│  │ (PILOT) │   of all outputs        │(CO-PLT) │  only    │
│  └─────────┘                          └─────────┘           │
│  Co-pilot joystick only activates if deflected >80%          │
│                                                              │
│  MODE 5: CUSTOM (user-programmable)                          │
│  Arbitrary axis-to-function mapping via config file or UI    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Swap Mechanism

The **SWAP** button lives on the center dashboard. Behavior:

1. **Single press**: Initiates swap request — LED blinks on both armrests
2. **Second person confirms** (presses their joystick button within 3 seconds): Swap executes
3. **Timeout (no confirm)**: Swap cancelled, brief buzz feedback
4. **Double-press by same person**: Force-swap (override, for solo use)
5. **Hold 3 seconds**: Cycle to next mode (Independent → Swapped → Merged → Pilot → Custom)

State indicated by OLED display and armrest LED color:
- **Amber** = Independent (default)
- **Blue** = Swapped
- **Green** = Merged
- **Red** = Pilot mode (red on co-pilot side, green on pilot side)
- **Purple** = Custom mapping active

### What the Joysticks Control

The joystick outputs are abstract — what they *do* depends on the active application layer:

| Application | X-Axis | Y-Axis | Push Button |
|-------------|--------|--------|-------------|
| **Lighting** | Color temperature (warm↔cool) | Brightness (dim↔bright) | Toggle zone on/off |
| **Music** | Track skip (prev/next) | Volume (down/up) | Play/Pause |
| **Display Navigation** | Scroll horizontal | Scroll vertical | Select/Enter |
| **Motorized Features** | Seat recline angle | Footrest extension | Lock position |
| **Fun Mode** | Spaceship steering | Throttle | Fire lasers (LED effect) |
| **Camera/Projector** | Pan | Tilt | Shutter/toggle |

Active application selected via the **MODE** rotary encoder on the center dashboard.

---

## 4. Control Dashboard

### Center Console Layout

```
┌────────────────────────────────────────────────┐
│              CENTER DASHBOARD PANEL             │
│            (250mm × 180mm surface)              │
├────────────────────────────────────────────────┤
│                                                │
│  ┌──────────────────────────────────────────┐  │
│  │          1.3" OLED STATUS DISPLAY        │  │
│  │  ┌────────────────────────────────────┐  │  │
│  │  │ MODE: Independent    🔋 98%        │  │  │
│  │  │ L: Lighting  R: Music              │  │  │
│  │  │ ♪ Track: Solar Sailer - Daft Punk  │  │  │
│  │  │ 💡 Zone L: 3200K  Zone R: 4500K   │  │  │
│  │  └────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────┘  │
│                                                │
│  ROW 1 — PRIMARY FUNCTIONS                     │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐         │
│  │  💡  │ │  🔊  │ │  🎵  │ │  ⚡  │         │
│  │LIGHTS│ │VOLUME│ │MUSIC │ │POWER │         │
│  │      │ │Master│ │      │ │ MODE │         │
│  └──────┘ └──────┘ └──────┘ └──────┘         │
│                                                │
│  ROW 2 — SYSTEM CONTROLS                       │
│  ┌────────────┐  ┌─────┐  ┌────────────┐      │
│  │  ⇄ SWAP    │  │ (●) │  │  MODE SEL  │      │
│  │  L ↔ R     │  │ NFC │  │  [ROTARY]  │      │
│  └────────────┘  └─────┘  └────────────┘      │
│                                                │
│  ROW 3 — EASTER EGGS & EXTRAS                  │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐         │
│  │  ?!  │ │  ☆   │ │  ♫   │ │  ◈   │         │
│  │RANDOM│ │PARTY │ │AMBIENT│ │SECRET│         │
│  │      │ │ MODE │ │SOUNDS│ │      │         │
│  └──────┘ └──────┘ └──────┘ └──────┘         │
│                                                │
└────────────────────────────────────────────────┘
```

### Left Armrest Button Panel

```
┌──────────────────────────────┐
│     LEFT ARMREST SURFACE     │
│                              │
│  ┌──────────────────────┐    │
│  │     ◎ JOYSTICK-L     │    │
│  │   (2-axis + push)    │    │
│  └──────────────────────┘    │
│                              │
│  ┌─────┐ ┌─────┐            │
│  │ FN1 │ │ FN2 │  Function  │
│  │     │ │     │  buttons   │
│  └─────┘ └─────┘            │
│  ┌─────┐ ┌─────┐            │
│  │ FN3 │ │ FN4 │  (user-    │
│  │     │ │     │  mappable) │
│  └─────┘ └─────┘            │
│                              │
│  [═══ INDICATOR LED BAR ═══] │
│  (RGB strip, shows mode/     │
│   feedback/notifications)    │
│                              │
└──────────────────────────────┘
```

Right armrest is a mirror image.

### Button Types & Specifications

| Button | Type | Size | Illumination | Feedback |
|--------|------|------|-------------|----------|
| **Joystick push** | Integrated switch | N/A | Shaft ring LED | Click + haptic |
| **FN1–FN4** (per arm) | Cherry MX Blue (tactile+click) | 20×20mm cap | Individual RGB LED | Audible click + haptic |
| **LIGHTS** | Silicone dome, backlit | 30×30mm | Amber LED | Haptic pulse |
| **VOLUME** | Rotary encoder w/ push | 20mm diameter knob | Ring LED | Detented rotation |
| **MUSIC** | Silicone dome, backlit | 30×30mm | Green LED | Haptic pulse |
| **POWER MODE** | Silicone dome, backlit | 30×30mm | Red LED | Haptic pulse |
| **SWAP** | Large mechanical, guarded | 40×25mm | Bicolor Red/Green LED | Heavy click + dual haptic |
| **NFC Reader** | Flush-mount circular | 30mm diameter | Blue ring LED | Tone on read |
| **MODE SELECT** | Rotary encoder w/ push | 25mm knob | OLED updates | Detented + haptic |
| **Easter egg row** | Cherry MX, novelty caps | 20×20mm | RGB programmable | Surprise! |

### Total I/O Count

| Category | Count | Type |
|----------|-------|------|
| Joystick analog axes | 4 | Analog input (2 per joystick) |
| Joystick push buttons | 2 | Digital input |
| Function buttons (per arm) | 8 total (4×2) | Digital input |
| Dashboard buttons | 8 | Digital input |
| Rotary encoders | 2 (volume + mode) | 2× quadrature + push |
| NFC reader | 1 | SPI |
| OLED display | 1 (or 3: one per arm + center) | I2C |
| RGB LED strips | 4 (2 arms + base + backrest) | WS2812B data line |
| Haptic motors | 3 (left arm, right arm, center) | PWM |
| Speakers/buzzer | 2 (stereo) or 1 (mono) | I2S or PWM |
| **Total GPIO-level signals** | **~35-40** | Mixed analog/digital |

---

## 5. Electronics Architecture

### System Block Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                      ELECTRONICS ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│                    ┌───────────────────────────┐                     │
│                    │    RASPBERRY PI 4B / 5     │                     │
│                    │    (Main Brain)            │                     │
│                    │                            │                     │
│                    │  • WiFi/BT                 │                     │
│                    │  • USB host                │                     │
│                    │  • I2C bus master          │                     │
│                    │  • SPI bus master          │                     │
│                    │  • Audio out (I2S/HDMI)    │                     │
│                    └──────┬──────┬──────┬───────┘                     │
│                           │      │      │                            │
│              ┌────────────┘      │      └────────────┐               │
│              │                   │                   │               │
│     ┌────────┴────────┐  ┌──────┴───────┐  ┌────────┴────────┐      │
│     │  I2C BUS        │  │  SPI BUS     │  │  USB            │      │
│     │                 │  │              │  │                 │      │
│     │  ┌───────────┐  │  │  ┌─────────┐ │  │  ┌───────────┐ │      │
│     │  │ ADS1115   │  │  │  │ RC522   │ │  │  │ USB Audio │ │      │
│     │  │ 16-bit ADC│  │  │  │ NFC     │ │  │  │ Interface │ │      │
│     │  │ (4 ch)    │  │  │  │ Reader  │ │  │  │ (speakers)│ │      │
│     │  │ Joystick  │  │  │  └─────────┘ │  │  └───────────┘ │      │
│     │  │ analog in │  │  │              │  │                 │      │
│     │  └───────────┘  │  │  ┌─────────┐ │  │  ┌───────────┐ │      │
│     │                 │  │  │ WS2812B │ │  │  │ USB-C PD  │ │      │
│     │  ┌───────────┐  │  │  │ LED     │ │  │  │ Power     │ │      │
│     │  │ MCP23017  │  │  │  │ Driver  │ │  │  │ Delivery  │ │      │
│     │  │ 16-ch I/O │  │  │  │ (GPIO)  │ │  │  └───────────┘ │      │
│     │  │ Expander  │  │  │  └─────────┘ │  │                 │      │
│     │  │ #1        │  │  └──────────────┘  └─────────────────┘      │
│     │  │ (buttons  │  │                                              │
│     │  │  L arm)   │  │                                              │
│     │  └───────────┘  │                                              │
│     │                 │                                              │
│     │  ┌───────────┐  │                                              │
│     │  │ MCP23017  │  │                                              │
│     │  │ #2        │  │                                              │
│     │  │ (buttons  │  │                                              │
│     │  │  R arm +  │  │                                              │
│     │  │  center)  │  │                                              │
│     │  └───────────┘  │                                              │
│     │                 │                                              │
│     │  ┌───────────┐  │    ┌──────────────────────────┐              │
│     │  │ SH1106    │  │    │   POWER DISTRIBUTION     │              │
│     │  │ OLED ×1-3 │  │    │                          │              │
│     │  │ (status)  │  │    │   5V/10A from USB-C PD   │              │
│     │  └───────────┘  │    │   or 12V→5V buck from    │              │
│     │                 │    │   center pedestal         │              │
│     │  ┌───────────┐  │    │                          │              │
│     │  │ DRV2605L  │  │    │   3.3V regulated for     │              │
│     │  │ Haptic ×3 │  │    │   logic & sensors        │              │
│     │  │ (L/R/Ctr) │  │    │                          │              │
│     │  └───────────┘  │    └──────────────────────────┘              │
│     │                 │                                              │
│     └─────────────────┘                                              │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Why Raspberry Pi 4B/5 (not Zero)

The couch requires more I/O and processing than a single chair:
- **4 analog channels** (ADS1115 via I2C) for joystick axes
- **Audio output** (I2S DAC or USB audio) for music/sound effects
- **Enough I2C addresses** for 2× MCP23017 + 3× OLED + 3× DRV2605L + ADS1115
- **WiFi + BT** for Home Assistant + Bluetooth speakers
- **Processing headroom** for the Easter egg animations and sound engine

### I2C Address Map

| Address | Device | Location |
|---------|--------|----------|
| `0x20` | MCP23017 #1 | Left armrest buttons + LEDs |
| `0x21` | MCP23017 #2 | Right armrest + center dashboard buttons |
| `0x3C` | SH1106 OLED #1 | Center dashboard display |
| `0x3D` | SH1106 OLED #2 (optional) | Left armrest mini display |
| `0x3E` | SH1106 OLED #3 (optional) | Right armrest mini display |
| `0x48` | ADS1115 ADC | Joystick analog inputs (4 channels) |
| `0x5A` | DRV2605L #1 | Left armrest haptic motor |
| `0x5B` | DRV2605L #2 (via TCA9548A) | Right armrest haptic motor |
| `0x5C` | DRV2605L #3 (via TCA9548A) | Center dashboard haptic motor |
| `0x70` | TCA9548A I2C mux | Multiplexer for duplicate-address devices |

### Wiring Topology

```
                          PEDESTAL BASE
                    ┌──────────────────────┐
                    │  • Pi 4B/5           │
                    │  • Power supply      │
                    │  • USB audio DAC     │
                    │  • Main wire harness │
                    │    junction          │
                    └──────────┬───────────┘
                               │
                     ┌─────────┼─────────┐
                     │         │         │
              ┌──────┴──┐ ┌───┴───┐ ┌───┴──────┐
              │ LEFT ARM│ │CENTER │ │RIGHT ARM │
              │         │ │CONSOLE│ │          │
              │ 8-wire  │ │12-wire│ │ 8-wire   │
              │ ribbon   │ │ribbon │ │ ribbon   │
              │ cable   │ │cable  │ │ cable    │
              │         │ │       │ │          │
              │• MCP I2C│ │• OLED │ │• MCP I2C │
              │• ADC ch │ │• NFC  │ │• ADC ch  │
              │  0,1    │ │• Enc  │ │  2,3     │
              │• Haptic │ │• Btns │ │• Haptic  │
              │• LEDs   │ │• Haptic│ │• LEDs   │
              │• GND,VCC│ │• LEDs │ │• GND,VCC │
              └─────────┘ └───────┘ └──────────┘
```

All cables routed through internal channels molded into the fiberglass shell.
Connectors: **JST-XH** for signal cables, **XT30** for power runs.

### Connector Pinouts

**Left/Right Arm Ribbon (8-pin JST-XH):**

| Pin | Signal | Notes |
|-----|--------|-------|
| 1 | VCC (5V) | Power for LEDs, haptic |
| 2 | GND | Common ground |
| 3 | SDA | I2C data (shared bus) |
| 4 | SCL | I2C clock (shared bus) |
| 5 | JOY_X | Analog to ADS1115 ch 0/2 |
| 6 | JOY_Y | Analog to ADS1115 ch 1/3 |
| 7 | LED_DATA | WS2812B data line |
| 8 | HAPTIC_EN | DRV2605L trigger (via I2C mux) |

---

## 6. Software Architecture

### Layered Design

```
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                         │
│                                                             │
│  ┌─────────────┐ ┌──────────────┐ ┌───────────────────┐    │
│  │ Lighting    │ │ Music        │ │ Easter Egg        │    │
│  │ Controller  │ │ Player       │ │ Engine            │    │
│  │ (per-zone)  │ │ (MPD/Mopidy)│ │ (see section 7)   │    │
│  └──────┬──────┘ └──────┬───────┘ └────────┬──────────┘    │
│         │               │                  │               │
│  ┌──────┴───────────────┴──────────────────┴──────────┐    │
│  │              EVENT BUS (asyncio + MQTT)             │    │
│  │                                                     │    │
│  │  Topics:                                            │    │
│  │  cybersyn/couch/{id}/joystick/{side}/axis           │    │
│  │  cybersyn/couch/{id}/joystick/{side}/button         │    │
│  │  cybersyn/couch/{id}/button/{location}/{name}       │    │
│  │  cybersyn/couch/{id}/mode                           │    │
│  │  cybersyn/couch/{id}/swap                           │    │
│  │  cybersyn/couch/{id}/easter_egg/{name}              │    │
│  │  cybersyn/couch/{id}/nfc                            │    │
│  │  cybersyn/couch/{id}/display/{location}             │    │
│  └──────┬──────────────────────────────────────────────┘    │
│         │                                                   │
│  ┌──────┴──────────────────────────────────────────────┐    │
│  │              CONTROL ROUTING ENGINE                  │    │
│  │                                                     │    │
│  │  • Reads current mode (Independent/Swapped/etc.)    │    │
│  │  • Maps joystick axes → target function             │    │
│  │  • Routes button presses → correct handler          │    │
│  │  • Manages swap handshake state machine             │    │
│  │  • Deadzone processing, axis curves, rate limiting  │    │
│  └──────┬──────────────────────────────────────────────┘    │
│         │                                                   │
│  ┌──────┴──────────────────────────────────────────────┐    │
│  │              HARDWARE ABSTRACTION LAYER              │    │
│  │                                                     │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐ │    │
│  │  │ Joystick │ │ Buttons  │ │ Display  │ │ Audio  │ │    │
│  │  │ Driver   │ │ Driver   │ │ Driver   │ │ Driver │ │    │
│  │  │(ADS1115) │ │(MCP23017)│ │(SH1106)  │ │(ALSA)  │ │    │
│  │  └──────────┘ └──────────┘ └──────────┘ └────────┘ │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐            │    │
│  │  │ LED      │ │ Haptic   │ │ NFC      │            │    │
│  │  │ Driver   │ │ Driver   │ │ Driver   │            │    │
│  │  │(WS2812B) │ │(DRV2605L)│ │(RC522)   │            │    │
│  │  └──────────┘ └──────────┘ └──────────┘            │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  OS: Raspberry Pi OS Lite (64-bit) or DietPi               │
│  Runtime: Python 3.11+ / asyncio                            │
│  Config: YAML files in /etc/cybersyn/                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Swap State Machine

```
                    ┌─────────┐
                    │  IDLE   │ ← default after boot
                    │(current │
                    │  mode)  │
                    └────┬────┘
                         │
                    SWAP pressed
                    by person A
                         │
                    ┌────▼────┐
                    │PENDING  │ ← LED blinks on both arms
                    │(3s timer│   OLED shows "Swap? Confirm!"
                    │ starts) │
                    └────┬────┘
                         │
              ┌──────────┼──────────┐
              │          │          │
         Person B    Timeout     Person A
         confirms    (3 sec)     double-press
              │          │          │
         ┌────▼────┐ ┌───▼────┐ ┌──▼──────┐
         │CONFIRMED│ │CANCEL  │ │FORCE    │
         │         │ │        │ │SWAP     │
         │ Execute │ │ Return │ │ Execute │
         │ swap    │ │ to     │ │ swap    │
         │         │ │ IDLE   │ │ (solo)  │
         └────┬────┘ └───┬────┘ └──┬──────┘
              │          │         │
              └──────────┴─────────┘
                         │
                    ┌────▼────┐
                    │  IDLE   │ ← new mode active
                    │(updated │   haptic + audio confirm
                    │  mode)  │
                    └─────────┘
```

### Configuration File (`/etc/cybersyn/couch.yaml`)

```yaml
couch:
  id: "couch_1"
  name: "Cybersyn Loveseat Alpha"

mqtt:
  broker: "homeassistant.local"
  port: 1883
  username: "${MQTT_USER}"
  password: "${MQTT_PASS}"

joysticks:
  deadzone: 0.08          # 8% center deadzone
  curve: "exponential"     # linear | exponential | s-curve
  curve_exponent: 2.0      # for exponential curve
  poll_rate_hz: 50         # 50 Hz polling
  swap_confirm_timeout: 3  # seconds

  left:
    adc_channel_x: 0
    adc_channel_y: 1
    invert_x: false
    invert_y: false
    default_mapping: "lighting"

  right:
    adc_channel_x: 2
    adc_channel_y: 3
    invert_x: false
    invert_y: true
    default_mapping: "music"

buttons:
  debounce_ms: 50
  long_press_ms: 800

  mappings:
    # Left arm function buttons
    left_fn1: { action: "lighting.zone_toggle", zone: "left" }
    left_fn2: { action: "lighting.scene_cycle", zone: "left" }
    left_fn3: { action: "music.playlist_cycle" }
    left_fn4: { action: "easter_egg.random" }

    # Right arm function buttons
    right_fn1: { action: "lighting.zone_toggle", zone: "right" }
    right_fn2: { action: "lighting.scene_cycle", zone: "right" }
    right_fn3: { action: "music.playlist_cycle" }
    right_fn4: { action: "easter_egg.random" }

    # Center dashboard
    lights: { action: "lighting.master_toggle" }
    music: { action: "music.play_pause" }
    power_mode: { action: "system.power_mode_cycle" }
    swap: { action: "system.swap_request" }
    random: { action: "easter_egg.random" }
    party: { action: "easter_egg.party_mode" }
    ambient: { action: "audio.ambient_cycle" }
    secret: { action: "easter_egg.konami_start" }

lighting:
  zones:
    left:
      led_start: 0
      led_count: 30
      default_color: [255, 147, 41]  # warm amber
    right:
      led_start: 30
      led_count: 30
      default_color: [255, 147, 41]
    base:
      led_start: 60
      led_count: 45
      default_color: [255, 100, 0]
    backrest:
      led_start: 105
      led_count: 20
      default_color: [255, 80, 0]

  scenes:
    cybersyn_classic:
      color: [255, 147, 41]
      brightness: 0.7
      effect: "steady"
    deep_space:
      color: [0, 20, 80]
      brightness: 0.4
      effect: "slow_pulse"
    party:
      effect: "rainbow_chase"
      speed: 0.5
      brightness: 1.0
    chill:
      color: [180, 100, 255]
      brightness: 0.3
      effect: "breathe"

audio:
  backend: "mpd"           # mpd | mopidy | pulseaudio
  default_volume: 40       # percent
  startup_sound: "cybersyn_boot.wav"
  button_click: "click_01.wav"
  swap_confirm: "swap_confirm.wav"

  ambient_sounds:
    - "rain_on_glass.ogg"
    - "spacecraft_hum.ogg"
    - "fireplace.ogg"
    - "ocean_waves.ogg"
    - "cybersyn_opsroom_ambience.ogg"
```

### MQTT Topic Reference

| Topic | Payload | Direction |
|-------|---------|-----------|
| `cybersyn/couch/{id}/joystick/left/axis` | `{"x": 0.42, "y": -0.15}` | Out |
| `cybersyn/couch/{id}/joystick/right/axis` | `{"x": 0.0, "y": 0.67}` | Out |
| `cybersyn/couch/{id}/joystick/{side}/button` | `{"state": "pressed"}` | Out |
| `cybersyn/couch/{id}/button/{location}/{name}` | `{"state": "pressed", "duration_ms": 120}` | Out |
| `cybersyn/couch/{id}/mode` | `{"mode": "independent", "left_app": "lighting", "right_app": "music"}` | Out |
| `cybersyn/couch/{id}/swap` | `{"state": "pending\|confirmed\|cancelled"}` | Out |
| `cybersyn/couch/{id}/nfc` | `{"uid": "04:A2:...", "user": "operator_1"}` | Out |
| `cybersyn/couch/{id}/led/{zone}/set` | `{"color": [255,100,0], "brightness": 0.8, "effect": "steady"}` | In |
| `cybersyn/couch/{id}/display/{location}/set` | `{"text": "Hello", "line": 0}` | In |
| `cybersyn/couch/{id}/audio/command` | `{"action": "play\|pause\|next\|volume", "value": 50}` | In |
| `cybersyn/couch/{id}/easter_egg/trigger` | `{"name": "party_mode"}` | In/Out |

---

## 7. Easter Egg System

### Built-in Easter Eggs

| # | Name | Trigger | Effect | Duration |
|---|------|---------|--------|----------|
| 1 | **Party Mode** | PARTY button | Rainbow chase on all LEDs, upbeat music, haptic bass sync | Until cancelled |
| 2 | **Deep Space** | Hold both joystick buttons 3s | LEDs fade to deep blue, spacecraft ambience, star-twinkle effect | Until cancelled |
| 3 | **Konami Code** | SECRET button, then ↑↑↓↓←→←→ on joystick + both FN1s | All LEDs flash, "achievement unlocked" sound, unlocks hidden features | 5 sec |
| 4 | **Cybersyn Boot** | Power on | Retro CRT boot sequence on OLEDs, ascending tone, LEDs sweep from center | 8 sec |
| 5 | **Random Wisdom** | RANDOM button | OLED displays a random Stafford Beer / cybernetics quote, spoken via TTS | 10 sec |
| 6 | **Mood Sync** | NFC tap matching cards | Two occupants tap paired NFC cards simultaneously → LEDs pulse in sync | 30 sec |
| 7 | **Secret DJ** | Rotate MODE encoder 10 full turns clockwise | Unlocks DJ mode: joystick X = crossfade, Y = filter, buttons = sample pads | Until mode change |
| 8 | **The Algedonic Signal** | Both occupants press FN4 simultaneously | Red alert! All LEDs go red, alarm sound, OLED shows "ALGEDONIC ALERT" (reference to Beer's alerting system) | 5 sec |
| 9 | **Chilean Flag** | Hold LIGHTS + MUSIC + POWER simultaneously | LEDs display Chilean flag colors (red, white, blue) in a wave | 10 sec |
| 10 | **Ghost in the Machine** | Leave couch unoccupied for 30 min | LEDs slowly breathe on their own, random ambient sounds at low volume | Until occupancy detected |

### User-Programmable Easter Eggs

The config file supports custom triggers:

```yaml
easter_eggs:
  custom:
    - name: "my_secret"
      trigger:
        type: "sequence"          # sequence | simultaneous | timing | nfc
        buttons: ["left_fn1", "left_fn2", "right_fn1", "right_fn2"]
        timeout_ms: 2000
      effects:
        leds:
          pattern: "custom_animation.json"
        audio:
          file: "my_sound.wav"
        haptic:
          pattern: "double_pulse"
        display:
          text: "You found it!"
```

### Stafford Beer Quotes Database (for Random Wisdom)

Stored in `/etc/cybersyn/quotes.json`:

```json
[
  "The purpose of a system is what it does.",
  "Acceptable to whom? is the question.",
  "If cybernetics is the science of control, management is the profession of control.",
  "Instead of trying to specify it in full detail, you specify it only somewhat. You then ride on the dynamics of the system in the direction you want to go.",
  "Our institutions are failing because they are disobeying laws of effective organization which their managers do not know about, to which indeed their managers are contemptuously indifferent.",
  "The whole enterprise of science is an exercise in cybernetics: a feedback loop between hypothesis and experiment.",
  "Variety absorbs variety."
]
```

---

## 8. Bill of Materials

### Electronics BOM

| Item | Part | Qty | Unit Cost | Total | Source |
|------|------|-----|-----------|-------|--------|
| Main computer | Raspberry Pi 4B 4GB (or Pi 5) | 1 | $55 | $55 | RPi authorized dealer |
| ADC | ADS1115 16-bit I2C | 1 | $12 | $12 | Adafruit / AliExpress |
| I/O Expander | MCP23017 I2C 16-ch | 2 | $4 | $8 | Adafruit / LCSC |
| I2C Multiplexer | TCA9548A 8-ch | 1 | $6 | $6 | Adafruit |
| Joystick | Hall-effect 2-axis industrial | 2 | $25 | $50 | RobotShop / AliExpress |
| OLED Display | 1.3" SH1106 I2C 128×64 | 1-3 | $8 | $8-24 | AliExpress |
| NFC Reader | MFRC522 RC522 SPI | 1 | $5 | $5 | AliExpress |
| Haptic Driver | DRV2605L breakout | 3 | $8 | $24 | Adafruit |
| LRA Motor | 10mm coin vibration | 3 | $2 | $6 | AliExpress |
| Mech Switches | Cherry MX Blue | 12 | $1 | $12 | KBDfans / AliExpress |
| Keycaps | Custom dye-sub PBT | 12 | $3 | $36 | Signature Plastics |
| Silicone Domes | Custom backlit 30mm | 4 | $5 | $20 | Ali / custom mold |
| Rotary Encoder | EC11 w/ push + knob | 2 | $4 | $8 | AliExpress |
| LED Strip | WS2812B 60/m IP30 | 3m | $8/m | $24 | BTF-Lighting |
| USB Audio DAC | PCM2704 or better | 1 | $15 | $15 | AliExpress |
| Speakers | 2" full range, 5W | 2 | $8 | $16 | Parts Express |
| Power Supply | USB-C PD 45W or 12V/5A | 1 | $20 | $20 | Anker / MeanWell |
| Buck Converter | 12V→5V 5A step-down | 1 | $8 | $8 | Pololu |
| PCB (custom) | Main distribution board | 1 | $15 | $15 | JLCPCB |
| Connectors | JST-XH sets, ribbon cable | Lot | $15 | $15 | AliExpress |
| Wire | 22 AWG silicone, various | 10m | $1/m | $10 | AliExpress |
| Misc | Standoffs, screws, heat shrink | Lot | $15 | $15 | Amazon |
| **Electronics Subtotal** | | | | **$398-414** | |

### Structural BOM

| Item | Description | Qty | Cost | Source |
|------|-------------|-----|------|--------|
| Fiberglass cloth | 6oz E-glass, 10 yd | 1 | $60 | US Composites |
| Epoxy resin | 2-part laminating, 2 gal | 1 | $80 | US Composites |
| Gel coat | White tooling gel coat, 1 gal | 1 | $45 | Fiberglass Supply |
| Foam core | XPS insulation board 1" (plug) | 4 sheets | $30/ea = $120 | Home Depot |
| Pedestal tube | 4" diameter steel tube, 18" | 1 | $40 | Metal Supermarkets |
| Base plate | 1/4" steel, 27" diameter | 1 | $80 | SendCutSend |
| Swivel bearing | Heavy-duty lazy susan, 12" | 1 | $35 | Amazon |
| Upholstery foam | 2" high-density, 2 yd | 1 | $60 | Foam Factory |
| Fabric | Burnt orange Ultrasuede, 3 yd | 1 | $120 | Fabric.com |
| Spray adhesive | 3M Super 77, 2 cans | 2 | $15/ea = $30 | Amazon |
| Sanding supplies | 80-400 grit, Bondo, primer | Lot | $60 | Auto parts |
| **Structural Subtotal** | | | **$730** | |

### Total Estimated Cost

| Category | Cost |
|----------|------|
| Electronics | $400-415 |
| Structural / materials | $730 |
| 3D printed parts (armrest bays, button mounts) | $40-60 |
| Contingency (15%) | $175 |
| **Grand Total** | **$1,345-1,380** |

*For a second couch, structural costs drop to ~$400 (mold is reusable), electronics stay the same.*

---

## 9. Build Phases

### Phase 0: Breadboard Proof-of-Concept (2-3 weeks)

**Goal**: Validate the full electronics stack on a breadboard before building anything physical.

- [ ] Wire 2× joysticks → ADS1115 → Pi, confirm analog reads
- [ ] Wire 8× Cherry MX switches → MCP23017 → Pi, confirm digital reads
- [ ] Wire 2× rotary encoders, confirm quadrature decode
- [ ] Connect SH1106 OLED, display joystick position live
- [ ] Connect WS2812B strip (short test strip), drive from Pi
- [ ] Connect DRV2605L + LRA motor, test haptic patterns
- [ ] Connect RC522 NFC, read a card UID
- [ ] Wire everything simultaneously, confirm no I2C conflicts
- [ ] Run the full firmware, test joystick → LED control loop
- [ ] Test MQTT publish/subscribe with Home Assistant
- [ ] Test swap state machine with two joysticks
- [ ] Record latency measurements (target: <20ms input-to-output)

**Deliverable**: Working breadboard with all sensors/actuators, running firmware.

### Phase 1: Custom PCB Design (2-3 weeks)

**Goal**: Design a single distribution PCB that replaces the breadboard.

- [ ] Schematic in KiCad: Pi header, I2C bus, SPI bus, connectors for all modules
- [ ] PCB layout: single board that fits in pedestal base cavity
- [ ] Add JST-XH connectors for each arm ribbon cable + center console
- [ ] Add screw terminals for power input
- [ ] Add test points for debugging
- [ ] Fabricate at JLCPCB (2-layer, standard)
- [ ] Assemble and validate against breadboard behavior

**Deliverable**: Assembled PCB, tested and working.

### Phase 2: 3D Printed Armrest Mockup (2-3 weeks)

**Goal**: Validate ergonomics and button placement before committing to fiberglass.

- [ ] Model armrest in FreeCAD/Fusion 360 with joystick cavity, button holes, electronics bay
- [ ] Print at 1:1 scale (may require splitting across multiple prints)
- [ ] Install joystick, buttons, OLED into printed armrest
- [ ] Test ergonomics: reach distances, wrist angle, visibility of OLED
- [ ] Test two people sitting side by side, ensure armrest doesn't interfere
- [ ] Iterate on dimensions at least once
- [ ] Model center console dashboard panel, print and test

**Deliverable**: Validated ergonomic model with embedded electronics.

### Phase 3: Fiberglass Shell (4-6 weeks)

**Goal**: Build the actual couch shell.

- [ ] Build foam/MDF plug from CAD model (CNC if available, hand-shaped if not)
- [ ] Fair and finish plug surface (Bondo, sand to 400 grit)
- [ ] Apply PVA release agent + wax
- [ ] Lay up female mold (2 halves for complex shape, or single pull)
- [ ] Demold, inspect mold quality
- [ ] Lay up production shell in mold
- [ ] Demold shell, trim edges
- [ ] Bond in cable channel inserts and electronics bay walls (secondary layup)
- [ ] Sand, prime, paint (white)
- [ ] Test fit armrest modules and center console into shell

**Deliverable**: Finished fiberglass shell with integrated cable routes.

### Phase 4: Pedestal Base (2-3 weeks)

**Goal**: Build the structural base with swivel.

- [ ] Cut and weld steel pedestal tube
- [ ] Cut base plate (laser or plasma)
- [ ] Weld tube to plate, grind smooth
- [ ] Mount swivel bearing to top of tube
- [ ] Mount Pi + PCB enclosure inside tube or under seat
- [ ] Route power cable through tube center
- [ ] Test stability: load test at 200kg (440 lbs) — two adults + safety factor
- [ ] Powder coat or paint matte black

**Deliverable**: Completed pedestal base with concealed electronics.

### Phase 5: Upholstery & Assembly (2-3 weeks)

**Goal**: Upholster and assemble the complete couch.

- [ ] Cut foam cushion sections (seat, backrest, armrest tops)
- [ ] Glue foam to shell
- [ ] Sew fabric covers (or hire upholsterer)
- [ ] Install fabric, staple/glue to shell underside
- [ ] Mount armrest electronics modules into cavities
- [ ] Install center dashboard panel
- [ ] Route and connect all ribbon cables
- [ ] Install LED strips in channels (armrests, base, backrest)
- [ ] Install speakers in shell (behind perforated grille areas)
- [ ] Mount shell to pedestal
- [ ] Final cable connections
- [ ] Power-on test

**Deliverable**: Fully assembled Cybersyn Couch.

### Phase 6: Software Integration & Tuning (2-3 weeks)

**Goal**: Full software stack running, calibrated, Easter eggs programmed.

- [ ] Flash Pi with DietPi + cybersyn-couch service
- [ ] Calibrate joystick center positions and ranges
- [ ] Tune deadzone and response curves per user preference
- [ ] Configure lighting scenes
- [ ] Set up music library / Mopidy playlists
- [ ] Record/source all sound effects
- [ ] Implement and test all 10 Easter eggs
- [ ] Configure Home Assistant integration
- [ ] Create web dashboard for remote monitoring
- [ ] Load-test: 8-hour soak test running all systems
- [ ] Write user manual

**Deliverable**: Ship-ready Cybersyn Couch.

### Phase 7: Multi-Couch Network (future)

- [ ] Design couch-to-couch MQTT coordination
- [ ] Implement voting/polling across couches
- [ ] Build central display wall integration
- [ ] Create "Opsroom" mode where 7 couches coordinate

---

## 10. Manufacturing

### Shell Manufacturing Decision Matrix

| Factor | Fiberglass Hand Lay-Up | Rotomolding | CNC Foam + Resin Infusion |
|--------|----------------------|-------------|--------------------------|
| **Qty = 1** | Best | Overkill | Good |
| **Qty = 7** | Good | Best | Expensive |
| **Surface quality** | Excellent (with gel coat) | Good (grainy) | Excellent |
| **Weight** | Light (8-12 kg shell) | Heavier (15-20 kg) | Lightest (6-10 kg) |
| **Tooling cost** | $1,500-3,000 | $5,000-10,000 | $500 (CNC time) |
| **Per-unit cost** | $300-500 | $80-150 | $400-600 |
| **Cable channels** | Bond in after | Mold in | Mold in |
| **Skill level** | Intermediate | Professional | Advanced |
| **Recommended for** | Prototype + small batch | Production run of 7+ | One-off art piece |

**Recommendation**: Fiberglass hand lay-up for the first couch, with the option to commission a rotomold if demand grows.

### 3D Printed Components

These parts are printed in PETG or ABS:

| Part | Material | Print Time | Notes |
|------|----------|------------|-------|
| Joystick mount plate | PETG | 3h | Bolts into armrest cavity |
| Button panel frame (×2) | PETG | 4h each | Holds Cherry MX switches |
| Dashboard panel frame | ABS | 5h | Center console mount |
| OLED bezel (×1-3) | PETG | 1h each | Snap-fit around display |
| Electronics bay lid (×2) | PETG | 2h each | Armrest underside access |
| Speaker grille | PETG | 2h | Perforated pattern |
| NFC reader mount | PLA | 1h | Flush-mount ring |
| Cable clip set | PLA | 0.5h | Internal cable management |

---

## 11. Safety & Power

### Electrical Safety

| Concern | Mitigation |
|---------|------------|
| **Fire risk** | All wiring 22 AWG silicone (rated 200°C), 5A fuse on main power line |
| **Shock risk** | Everything runs at 5V or 3.3V DC — no mains voltage inside the couch |
| **Short circuit** | Polyfuse (resettable) on each arm's power feed |
| **Heat** | Pi in ventilated cavity with passive heatsink, thermal shutdown at 80°C |
| **Pinch points** | All electronics sealed behind panels, no exposed PCBs |
| **EMI** | Shielded I2C/SPI runs if interference observed; ferrite clamps on power |

### Power Budget

| Subsystem | Typical Draw | Peak Draw |
|-----------|-------------|-----------|
| Raspberry Pi 4B | 3.0W | 6.0W |
| ADS1115 + MCP23017s | 0.1W | 0.2W |
| OLED displays (×3) | 0.3W | 0.5W |
| WS2812B LEDs (125 LEDs @ 30% avg) | 7.5W | 37.5W (full white) |
| Haptic motors (×3, pulsed) | 0.1W avg | 3.0W peak |
| Speakers (2× 5W) | 2.0W avg | 10.0W peak |
| NFC reader | 0.1W | 0.2W |
| **Total** | **~13W typical** | **~57W peak** |

A 45W USB-C PD supply covers typical usage with headroom. For full party-mode peak loads, use a 12V/5A (60W) supply with buck converters.

### Structural Safety

| Concern | Mitigation |
|---------|------------|
| **Tip-over** | Base weighted with steel plate, CoG analysis at full recline |
| **Load rating** | Design for 200 kg (440 lbs) — two adults + safety factor |
| **Swivel lock** | Optional friction lock on bearing for stationary use |
| **Material off-gassing** | Use low-VOC epoxy, cure fully (7 days) before upholstering |

---

## Appendices

### A. Joystick Axis-to-Function Mapping Table

| Mode (via rotary) | Joystick X | Joystick Y | Push Button |
|--------------------|------------|------------|-------------|
| 0: Lighting | Color temp | Brightness | Zone on/off |
| 1: Music | Skip track | Volume | Play/Pause |
| 2: Display Nav | Scroll H | Scroll V | Select |
| 3: Motorized (future) | Recline | Footrest | Lock |
| 4: Fun/Game | Steer | Throttle | Fire/Action |
| 5: Camera/Projector | Pan | Tilt | Shutter |
| 6: Custom | User-defined | User-defined | User-defined |

### B. LED Channel Map

| Index Range | Zone | Location | Default Color |
|-------------|------|----------|---------------|
| 0–29 | Left Arm | Under left armrest lip | Warm amber |
| 30–59 | Right Arm | Under right armrest lip | Warm amber |
| 60–104 | Base | Around pedestal base circumference | Deep orange |
| 105–124 | Backrest | Behind/under backrest top edge | Soft orange |

### C. NFC User Profiles

When a known NFC tag is tapped, the couch loads that user's preferences:

```yaml
nfc_profiles:
  "04:A2:B3:C4:D5":
    name: "Operator Alpha"
    lighting_scene: "cybersyn_classic"
    music_playlist: "synthwave"
    joystick_curve: "exponential"
    easter_eggs_unlocked: ["konami", "dj_mode"]

  "04:F6:E7:D8:C9":
    name: "Operator Beta"
    lighting_scene: "deep_space"
    music_playlist: "ambient"
    joystick_curve: "linear"
    easter_eggs_unlocked: ["konami"]
```

### D. Home Assistant Integration

```yaml
# Example Home Assistant automation
automation:
  - alias: "Cybersyn Party Mode"
    trigger:
      platform: mqtt
      topic: "cybersyn/couch/couch_1/easter_egg/trigger"
      payload: '{"name": "party_mode"}'
    action:
      - service: light.turn_on
        target:
          area_id: living_room
        data:
          effect: "rainbow"
      - service: media_player.play_media
        target:
          entity_id: media_player.living_room
        data:
          media_content_type: playlist
          media_content_id: "party_mix"

  - alias: "Cybersyn Algedonic Alert"
    trigger:
      platform: mqtt
      topic: "cybersyn/couch/couch_1/easter_egg/trigger"
      payload: '{"name": "algedonic_alert"}'
    action:
      - service: notify.all
        data:
          message: "ALGEDONIC ALERT from the Cybersyn Couch!"
```

---

*This document is a living spec. Version 0.1 — 2026-03-24.*
*Hardware: CERN-OHL-S-2.0 | Software: MIT | Docs: CC BY-SA 4.0*
