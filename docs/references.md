# Cybersyn Chair - References & Resources

## Primary Historical Sources

### Books & Academic Papers

| Source | Description | Access |
|--------|-------------|--------|
| **Eden Medina, *Cybernetic Revolutionaries* (MIT Press, 2011)** | Definitive academic history with design details, armrest button layouts, and archival photos | [MIT Press](https://mitpress.mit.edu/9780262525961/cybernetic-revolutionaries/) / [PDF](https://uberty.org/wp-content/uploads/2015/10/Eden_Medina_Cybernetic_Revolutionaries.pdf) |
| **"Diseño de una sala de operaciones," INTEC, no. 4 (1973), pp. 19–28** | Original Chilean technical documentation of the Opsroom design | Archives (contact institutions below) |

### Archives

| Archive | Contents | Contact |
|---------|----------|---------|
| **Stafford Beer Collection** | Original correspondence, technical drawings, project documents | Liverpool John Moores University, Liverpool, UK |
| **Gui Bonsiepe Archive** | Sketches, design drawings, photographs | Contact via [guibonsiepe.com](http://www.guibonsiepe.com/) |
| **INTEC Archives** | Chilean State Technology Institute records | Chile National Archives |

### Key Interviews & Contacts

- **Gui Bonsiepe** - Lead designer, interviewed by Eden Medina (May 2008, La Plata, Argentina)
- **Hugo Palmarola** - Curator of DHub exhibition, Chilean design historian
- **Eden Medina** - MIT Professor, author, [edenmedina.mit.edu](https://edenmedina.mit.edu/)

---

## Reconstructions

### FabLab Santiago (2016)

- **Location**: Santiago, Chile
- **Supervised by**: Original designers including Gui Bonsiepe
- **Contact**: [FabLabs.io Profile](https://www.fablabs.io/labs/fablabscl)
- **Note**: Website fablabsantiago.org currently inactive

### Disseny Hub Barcelona (2023)

- **Location**: Barcelona, Spain
- **Exhibition**: "How to Design a Revolution: The Chilean Road to Design"
- **Details**: First *functional* reconstruction - 72m² hexagonal room with working controls
- **Curators**: Hugo Palmarola, Eden Medina, Pedro Ignacio Alonso
- **Contact**: [Documentation Center](https://www.dissenyhub.barcelona/en/centredoc/services/information-and-requests)
- **Exhibition Page**: [Cybersyn in Action](https://www.dissenyhub.barcelona/en/activity/cybersyn-action)

---

## Visual References

### High-Quality Photos

| Source | Description |
|--------|-------------|
| [Google Arts & Culture - FabLab Chair](https://artsandculture.google.com/asset/the-counterculture-room-cybersyn-chair-gui-bonsiepe-recreated-by-fablab-santiago-in-2016/vQHnhWYDvfxj6Q) | FabLab Santiago 2016 recreation, high-res |
| [Artsy - Original Opsroom](https://www.artsy.net/artwork/gui-bonsiepe-cybersyn-operations-room-datafeed-with-chairs) | Cantor Fitzgerald Gallery collection |
| [Wikipedia - Control Room](https://en.wikipedia.org/wiki/Project_Cybersyn#/media/File:Cybersyn_control_room.jpg) | Classic operations room photo |

### Video Resources

| Source | Description |
|--------|-------------|
| [99% Invisible Podcast](https://99percentinvisible.org/episode/project-cybersyn/) | Episode with photos and context |
| [MIT News - Designing a Revolution](https://news.mit.edu/2023/designing-revolution-1002) | Coverage of Barcelona exhibition |

---

## CAD Resources (Starting Points)

### Tulip/Pedestal Chair Models

| Name | Source | Formats | Notes |
|------|--------|---------|-------|
| Tulip Chair | [GrabCAD](https://grabcad.com/library/tulip-chair-1) | Various | Saarinen-style, modify for armrests |
| Saarinen Tulip | [Sketchfab](https://sketchfab.com/3d-models/saarinen-tulip-chair-bc48eb1d27794a7baa8b2009aff5590e) | Free download | Good base geometry |
| Knoll Tulip Armchair | [FaceQuad](https://facequad.com/products/knoll-tulip-chair-and-armchair-3d-model) | OBJ, FBX, 3DS | Armchair variant with armrests |
| Tulip Dining Set | [CadNav](https://www.cadnav.com/3d/tulip-chair.html) | Multiple | Several variations |
| Open3dModel Collection | [Open3dModel](https://open3dmodel.com/3d-models/tulip-chair) | Blend, Max, OBJ, etc. | 13 tulip chair models |

### Fiberglass Shell References

| Name | Source | Formats | Notes |
|------|--------|---------|-------|
| Eames Fiberglass Chair | [Herman Miller](https://www.hermanmiller.com/resources/3d-models-and-planning-tools/product-models/individual/eames-molded-fiberglass-side-chair-dowel-base-nonupholstered/) | Revit, SketchUp, AutoCAD | Official models for reference |
| Eames Collection | [GrabCAD](https://grabcad.com/library/tag/eames) | Various | Community-created models |

---

## Manufacturing Resources

### Fiberglass Fabrication

| Resource | Description |
|----------|-------------|
| [Instructables: Fiberglass Shell Chair](https://www.instructables.com/DEVELOPING-FORM-Fabricating-Organic-Fiberglass-For/) | Complete DIY guide with mold-making |
| [Hand Lay-Up Process](https://www.deloachindustries.com/blog/fiberglass-process-hand-lay-up-contact-molding-) | Industrial process overview |
| [Fiberglass Supply](https://www.fiberglasssupply.com/) | Materials supplier (US) |
| [US Composites](https://www.uscomposites.com/) | Resins, fabrics, tools |

### Rotational Molding

| Resource | Description |
|----------|-------------|
| [Roto Dynamics Comparison](https://rotodynamics.com/injection-molding-advantages-disadvantages-and-the-appeal-of-rotational-molding/) | Rotomolding vs injection molding |
| [Treatstock Guide](https://www.treatstock.com/guide/article/138-rotomolding-vs-injection-molding) | Cost comparison for small batches |

### Metal Fabrication (Pedestal Base)

| Resource | Description |
|----------|-------------|
| [SendCutSend](https://sendcutsend.com/) | Laser cutting, bending, welding |
| [Xometry](https://www.xometry.com/) | On-demand CNC and sheet metal |
| [Protolabs](https://www.protolabs.com/) | Rapid manufacturing services |

---

## Electronics & Software

### Hardware

| Component | Recommended Part | Datasheet/Guide |
|-----------|------------------|-----------------|
| Raspberry Pi Zero 2 W | Official | [RPi Docs](https://www.raspberrypi.com/documentation/) |
| Cherry MX Switches | Various colors | [Cherry MX Guide](https://www.cherrymx.de/en/cherry-mx.html) |
| OLED Display (SH1106) | 1.3" I2C | Common modules |
| RC522 NFC Reader | MFRC522 | [Datasheet](https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf) |

### Software Libraries

| Library | Purpose | Install |
|---------|---------|---------|
| gpiozero | GPIO control | `pip install gpiozero` |
| paho-mqtt | MQTT client | `pip install paho-mqtt` |
| luma.oled | OLED display | `pip install luma.oled` |
| mfrc522 | NFC reader | `pip install mfrc522` |

### Home Automation

| Platform | Integration |
|----------|-------------|
| [Home Assistant](https://www.home-assistant.io/) | MQTT integration for buttons/displays |
| [Node-RED](https://nodered.org/) | Visual workflow automation |

---

## Related Projects

| Project | Description | Link |
|---------|-------------|------|
| Cybersyn Poster | Boot Boyz Biz merchandise | [Shop](https://boot-boyz.biz/products/cybersyn) |
| Eames Institute | Shell chair history | [Collection](https://www.eamesinstitute.org/collection/form-follows-formulation/) |
| Open Desk | Open-source furniture designs | [opendesk.cc](https://www.opendesk.cc/) |
| WikiHouse | Open-source building system | [wikihouse.cc](https://www.wikihouse.cc/) |

---

## Action Items for Research

1. [ ] Contact Disseny Hub Barcelona documentation center for technical specs
2. [ ] Request access to Stafford Beer Collection at Liverpool John Moores
3. [ ] Attempt to reach FabLab Santiago via fablabs.io for 2016 reconstruction files
4. [ ] Search Internet Archive for fablabsantiago.org snapshots
5. [ ] Locate copy of INTEC no. 4 (1973) article on Opsroom design
6. [ ] Email Gui Bonsiepe for any available design documentation
