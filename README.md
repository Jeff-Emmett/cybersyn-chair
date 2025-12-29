# Cybersyn Chair Recreation Project

A modern recreation of the iconic Cybersyn Operations Room chairs from Chile's Project Cybersyn (1971-1973), with integrated Raspberry Pi electronics for smart home/office control.

![Cybersyn Opsroom](https://upload.wikimedia.org/wikipedia/commons/1/1e/Cybersyn_control_room.jpg)

## Project Goals

1. **Faithful Recreation**: Reproduce the aesthetic of Gui Bonsiepe's original fiberglass swivel chairs
2. **Modern Electronics**: Integrate Raspberry Pi with customizable armrest controls
3. **Modular Design**: Create swappable armrest modules for different use cases
4. **Open Source**: Publish all CAD files, electronics schematics, and software

---

## Historical Background

### The Original Cybersyn Project (1971-1973)

Project Cybersyn was Chile's pioneering experiment in real-time economic management under President Salvador Allende. The Operations Room (Opsroom) was the nerve center - a hexagonal 72m² space containing 7 fiberglass swivel chairs arranged in a circle.

**Design Team:**
- **Gui Bonsiepe** (Lead Designer, German industrial designer)
- Fernando Shultz
- Rodrigo Walker
- Pepa Foncea
- Industrial Design Area of INTEC (Chilean State Technology Institute)

### Original Chair Specifications

| Feature | Description |
|---------|-------------|
| **Material** | Fiberglass shell with orange upholstery |
| **Style** | Tulip/pedestal base (similar to Saarinen, but custom) |
| **Seating** | 7 chairs in inward-facing circle |
| **Swivel** | Full 360° rotation (considered optimal for creativity) |
| **Armrests** | Integrated control panels, ashtrays, drink holders |

### Armrest Control Layout

The original buttons were deliberately large ("big hand" design) for users without keyboard experience:

```
┌─────────────────────────────────────┐
│         ORIGINAL BUTTON LAYOUT      │
├─────────────────────────────────────┤
│                                     │
│  TOP ROW (3 square buttons):        │
│  [■] [■] [■]                        │
│   │   │   │                         │
│   └───┴───┴── Select data screens   │
│                                     │
│  MIDDLE ROW (5 buttons):            │
│  [○] [○] [○] [○] [○]                │
│   │                                 │
│   └── Navigate subdirectories       │
│       (hypertext-like navigation)   │
│                                     │
│  BOTTOM ROW (1 large rectangular):  │
│  [████████████████████]             │
│   │                                 │
│   └── Index/Home screen             │
│                                     │
└─────────────────────────────────────┘
```

The buttons connected via wires through the floor to slide carousels that displayed pre-made data visualization slides.

### Design Philosophy

- **No tables**: Intentionally omitted to prevent paper shuffling and encourage democratic discussion
- **Odd number (7)**: Ensures tie-breaking votes
- **Swivel chairs**: Maximizes creative interaction
- **No keyboards**: Large buttons for accessibility
- **No Star Trek influence**: Despite visual similarities, designers claimed no sci-fi inspiration

---

## Existing Resources & References

### Reconstructions

| Location | Year | Notes |
|----------|------|-------|
| FabLab Santiago, Chile | 2016 | Recreation supervised by original designers |
| Disseny Hub Barcelona, Spain | 2023 | First *functional* reconstruction, 72m² hexagonal room |

### Primary Sources

- **Eden Medina, *Cybernetic Revolutionaries* (MIT Press, 2011)** - Definitive historical account with design details
- **Stafford Beer Collection** - Liverpool John Moores University archives
- **INTEC Publication**: "Diseño de una sala de operaciones," INTEC, no. 4 (1973), pp. 19–28
- **Gui Bonsiepe Archive** - Original sketches

### Available 3D Models (Starting Points)

| Model | Source | Format | Notes |
|-------|--------|--------|-------|
| Tulip Chair | [GrabCAD](https://grabcad.com/library/tulip-chair-1) | Various | Saarinen-style, needs armrest mods |
| Saarinen Tulip | [Sketchfab](https://sketchfab.com/3d-models/saarinen-tulip-chair-bc48eb1d27794a7baa8b2009aff5590e) | Free | Good base geometry |
| Knoll Tulip | [FaceQuad](https://facequad.com/products/knoll-tulip-chair-and-armchair-3d-model) | OBJ, FBX | Armchair variant |
| Eames Shell | [Herman Miller](https://www.hermanmiller.com/resources/3d-models-and-planning-tools/product-models/individual/eames-molded-fiberglass-side-chair-dowel-base-nonupholstered/) | Revit, SketchUp, AutoCAD | Fiberglass shell reference |

### Reference Images

- [Google Arts & Culture - FabLab Recreation](https://artsandculture.google.com/asset/the-counterculture-room-cybersyn-chair-gui-bonsiepe-recreated-by-fablab-santiago-in-2016/vQHnhWYDvfxj6Q)
- [Artsy - Original Opsroom Photos](https://www.artsy.net/artwork/gui-bonsiepe-cybersyn-operations-room-datafeed-with-chairs)
- [99% Invisible Episode](https://99percentinvisible.org/episode/project-cybersyn/) - Includes photos and context

---

## Manufacturing Approaches

### Option 1: Fiberglass Hand Lay-Up (Recommended for Authenticity)

**Estimated Cost**: $800-2,000/chair + mold
**Tooling Cost**: $1,000-5,000 for plug and mold

**Process:**
1. Create positive plug from CNC-milled foam or MDF
2. Apply release agent and gel coat
3. Lay fiberglass mat + polyester/epoxy resin
4. Cure under controlled conditions
5. Demold and finish

**Resources:**
- [Instructables: Fiberglass Shell Chair](https://www.instructables.com/DEVELOPING-FORM-Fabricating-Organic-Fiberglass-For/)
- [Hand Lay-Up Process Guide](https://www.deloachindustries.com/blog/fiberglass-process-hand-lay-up-contact-molding-)

### Option 2: Rotational Molding (Best for Small Batches)

**Estimated Cost**: $50-150/chair at 50+ units
**Tooling Cost**: $3,000-10,000 for aluminum mold

**Advantages:**
- Tooling costs 1/5th of injection molding
- Creates seamless hollow shells (perfect for hiding electronics)
- Ideal for 50-500 unit production runs

**Resources:**
- [Rotomolding vs Injection Molding Comparison](https://rotodynamics.com/injection-molding-advantages-disadvantages-and-the-appeal-of-rotational-molding/)

### Option 3: Hybrid Approach

| Component | Method | Material |
|-----------|--------|----------|
| Shell/seat | Fiberglass hand lay-up OR rotomolding | Fiberglass or LLDPE |
| Armrests | 3D printed master → silicone mold → cast | Polyurethane resin |
| Base/pedestal | CNC machined or cast | Aluminum or steel |
| Electronics bay | 3D printed inserts | PETG/ABS |

---

## Electronics Integration

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    ARMREST MODULE                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              BUTTON PANEL (Top Surface)               │  │
│  │                                                       │  │
│  │    [DATA 1] [DATA 2] [DATA 3]   ← Screen selection   │  │
│  │                                                       │  │
│  │    [NAV 1] [NAV 2] [NAV 3] [NAV 4] [NAV 5]           │  │
│  │              ↑                                        │  │
│  │         Navigation/subdirectory buttons               │  │
│  │                                                       │  │
│  │    [═══════════ INDEX/HOME ═══════════]              │  │
│  │              ↑                                        │  │
│  │         Large "big hand" button                       │  │
│  │                                                       │  │
│  └───────────────────────────────────────────────────────┘  │
│                           │                                 │
│  ┌────────────────────────┴──────────────────────────────┐  │
│  │              ELECTRONICS CAVITY                       │  │
│  │                                                       │  │
│  │   ┌─────────────┐    ┌────────────────────────────┐  │  │
│  │   │ Raspberry   │    │  GPIO Breakout Board       │  │  │
│  │   │ Pi Zero 2 W │────│  + Button Matrix Driver    │  │  │
│  │   │             │    │  + Status LEDs             │  │  │
│  │   └──────┬──────┘    └─────────────┬──────────────┘  │  │
│  │          │                         │                 │  │
│  │   ┌──────┴─────────────────────────┴──────────────┐  │  │
│  │   │     USB-C Power + Data (through pedestal)     │  │  │
│  │   └───────────────────────────────────────────────┘  │  │
│  │                                                       │  │
│  │   MODULAR EXPANSION BAYS (snap-in):                  │  │
│  │   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   │  │
│  │   │  NFC    │ │  OLED   │ │ Haptic  │ │  USB    │   │  │
│  │   │ Reader  │ │ Display │ │ Motors  │ │  Ports  │   │  │
│  │   └─────────┘ └─────────┘ └─────────┘ └─────────┘   │  │
│  │                                                       │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Recommended Hardware

| Component | Model | Dimensions | Cost | Notes |
|-----------|-------|------------|------|-------|
| **Main Board** | Raspberry Pi Zero 2 W | 65 × 30 mm | ~$15 | WiFi/BT, sufficient GPIO |
| **Alternative** | Raspberry Pi Pico W | 51 × 21 mm | ~$6 | Even smaller, pure button I/O |
| **Buttons** | Cherry MX mechanical | 15.6 × 15.6 mm | ~$1 ea | Satisfying tactile feel |
| **Alt Buttons** | Silicone dome pads | Custom | ~$20/set | Authentic "big hand" style |
| **Display** | 1.3" SH1106 OLED | 35 × 33 mm | ~$8 | Optional status display |
| **NFC** | RC522 RFID module | 40 × 60 mm | ~$5 | User identification |
| **Haptic** | DRV2605L + LRA motor | 10 × 10 mm | ~$8 | Button feedback |

### Software Stack

```
┌─────────────────────────────────────────────────────────┐
│                   SOFTWARE LAYERS                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  APPLICATION LAYER                                      │
│  ├── Home Assistant integration (MQTT)                  │
│  ├── Custom Cybersyn dashboard (web UI)                 │
│  └── Multi-chair coordination (WebSocket)               │
│                                                         │
│  MIDDLEWARE                                             │
│  ├── Python asyncio event loop                          │
│  ├── Button debouncing & state machine                  │
│  └── Module hot-plug detection                          │
│                                                         │
│  HARDWARE ABSTRACTION                                   │
│  ├── gpiozero (button/LED control)                      │
│  ├── smbus2 (I2C modules)                               │
│  └── spidev (SPI displays)                              │
│                                                         │
│  OS: Raspberry Pi OS Lite (headless)                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Communication Protocol

**MQTT Topics:**
```
cybersyn/chair/{chair_id}/button/{button_name}  → pressed/released
cybersyn/chair/{chair_id}/module/{module_type}  → module data
cybersyn/chair/{chair_id}/status                → online/offline
cybersyn/display/{screen_id}/show               → screen control
```

---

## Project Phases

### Phase 1: Research & Design (Current)
- [x] Historical research on original design
- [x] Identify existing CAD resources
- [x] Document manufacturing options
- [ ] Obtain high-resolution reference photos
- [ ] Contact FabLab Santiago / Disseny Hub Barcelona for specs
- [ ] Create initial CAD model

### Phase 2: Prototype Electronics
- [ ] Build button matrix on breadboard
- [ ] Write Pi Zero control software
- [ ] Test MQTT integration with Home Assistant
- [ ] Design modular bay connector system
- [ ] 3D print armrest electronics enclosure

### Phase 3: Physical Prototype
- [ ] Modify existing tulip chair CAD for armrest cavity
- [ ] 3D print 1:4 scale model for review
- [ ] Create foam/MDF plug for fiberglass testing
- [ ] Make test fiberglass section
- [ ] Integrate electronics into armrest

### Phase 4: Production
- [ ] Finalize CAD for manufacturing
- [ ] Create production mold (fiberglass or rotomold)
- [ ] Produce first complete chair
- [ ] Document build process
- [ ] Publish open-source files

### Phase 5: Multi-Chair System
- [ ] Build 7-chair Opsroom configuration
- [ ] Create central display system
- [ ] Implement cross-chair coordination
- [ ] Add data visualization dashboard

---

## Directory Structure

```
cybersyn-chair/
├── README.md                 # This file
├── docs/
│   ├── history.md           # Detailed historical background
│   ├── references.md        # Links to sources and archives
│   └── manufacturing.md     # Detailed manufacturing guides
├── cad/
│   ├── chair-shell/         # Main chair body CAD files
│   ├── armrest/             # Armrest with electronics cavity
│   ├── pedestal-base/       # Swivel base design
│   └── modules/             # Snap-in module designs
├── electronics/
│   ├── schematics/          # KiCad circuit designs
│   ├── pcb/                 # Custom PCB layouts
│   └── bom/                 # Bill of materials
├── software/
│   ├── firmware/            # Pi Zero control code
│   ├── server/              # Central coordination server
│   └── dashboard/           # Web-based control panel
├── manufacturing/
│   ├── mold-designs/        # Fiberglass mold CAD
│   └── assembly-guides/     # Step-by-step build docs
└── media/
    ├── reference-photos/    # Historical images
    └── renders/             # 3D renders of design
```

---

## Cost Estimates

### Single Chair (DIY/Maker)

| Item | Estimated Cost |
|------|----------------|
| Fiberglass materials + mold (amortized over 7) | $200-400 |
| Metal pedestal base (fabricated) | $200-400 |
| Upholstery (orange fabric + foam) | $100-200 |
| Raspberry Pi Zero 2 W | $15 |
| Electronics (buttons, wiring, modules) | $50-100 |
| 3D printed components | $20-50 |
| **Total per chair** | **$585-1,165** |

### 7-Chair Opsroom Setup

| Item | Estimated Cost |
|------|----------------|
| 7 chairs (at $800 avg) | $5,600 |
| Central server (Pi 4 + display) | $150 |
| Network infrastructure | $100 |
| Display screens (7× monitors) | $1,400 |
| Room setup (hexagonal layout, wiring) | $500 |
| **Total Opsroom** | **$7,750** |

---

## Contributing

This is an open-source project. Contributions welcome:

1. **CAD Design**: Help model the chair shell, armrest, and base
2. **Electronics**: Design PCBs, write firmware
3. **Manufacturing**: Share fabrication experience
4. **Historical Research**: Locate original specifications and drawings
5. **Documentation**: Improve guides and tutorials

---

## License

- **Hardware designs**: CERN Open Hardware License v2
- **Software**: MIT License
- **Documentation**: CC BY-SA 4.0

---

## Acknowledgments

- **Gui Bonsiepe** and the original INTEC design team
- **Stafford Beer** for the Cybersyn vision
- **Eden Medina** for preserving this history in *Cybernetic Revolutionaries*
- **FabLab Santiago** for the 2016 recreation
- **Disseny Hub Barcelona** for the functional reconstruction

---

## Contact

For questions, collaboration, or access to original specifications:

- Open an issue on this repository
- Email: [your-email]
- Disseny Hub Barcelona: [Documentation Center](https://www.dissenyhub.barcelona/en/centredoc/services/information-and-requests)
