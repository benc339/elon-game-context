# Race to SI: Stage 2, "What the turbines power": the AI data center
Design doc only. Written 2026-10-23. Every number below is quoted from a file. If no file had it, the entry says **GAP**. Nothing is invented.
Shorthand for source paths: `AE` = /workspace/ai-ecosystem. `RPT` = AE/reports/2026-10-02-ecosystem-report.md. `LL` = AE/model/LEAD-LAG.md. `M0` = AE/model/MODEL-v0.md. `CDU-CONN` = AE/connections/CONN-2026-09-20-cdu-coldplate-mw-electrical.md.
Server 204 (/home/dev/eco-scale): a scoped grep for switchgear, transceiver, chiller, cooling tower, interconnection queue and UPS lead-time strings found no extra figures within the time limit. Treat 204 as unchecked, not as having no data.

## Component tree (powered AI hall)
```
Powered AI hall
├─ Site: land, permits, shell + MEP build
├─ Grid tie: interconnect queue slot → substation (LPT/GSU, HV breakers) [stage 1 makes these]
├─ On-site generation: gas turbines / recip engines / fuel cells [stage 1]
├─ Electrical in the hall: MV transformers, switchgear (MSB), UPS + batteries, busway, PDUs, 800 VDC power racks/shelves/BBU
├─ Cooling: cold plates → CDUs → manifolds → chillers / dry coolers / cooling towers; water
├─ IT: racks/servers (ODM) ← networking (switches) + optics (transceivers ← InP lasers) + copper (NVLink cables)
└─ Accelerators ← logic die (TSMC N3/N2) + HBM + CoWoS packaging + ABF substrate  [own chain, stage 3]
```

## Components (role · suppliers West/China · bottleneck evidence · durations)
| # | Component | Role | Key suppliers (West / China) | Bottleneck evidence | Sourced durations |
|---|---|---|---|---|---|
| 1 | **Grid interconnect queue slot** | Permission to draw grid MW | Utilities/ISOs: ERCOT, PJM, Dominion, Southern, AEP / China: GAP | **Strong.** ERCOT large-load queue about 410 GW (Mar 2026), about 87% of it data centers. Batch Zero studied only 66.4 GW base. New data-center energization ≥75 MW paused until Dec 2026. Dominion has about 53.8 GW contracted. (M0 row "Energizable GW") | Queue wait in months: **GAP** |
| 2 | **Large power transformers / GSU** | Step-up and step-down at the substation | Siemens Energy, Hitachi, HD Hyundai Electric, GE Vernova / China: GAP (US imports about 80%+, origin not split) | **Strong.** GSU about 160 weeks in Q1 2026 (RPT §2.2, Reuters) | LPT PO→receipt 30–36 months, EHV up to 60 months (NLR via M0, LL). Bushings up to 130 weeks, OLTC 80–90 weeks (M0) |
| 3 | **HV circuit breakers** | Substation protection | GE Vernova, ABB, Siemens / China: GAP | **Strong.** About 125 weeks (RPT §2.2) | 125 weeks |
| 4 | **MV transformers + switchgear (in-hall)** | Feed the halls at medium voltage | ETN, Schneider, ABB, Siemens, Powell, HPS; PWRWELL (Johor) / China: GAP | **Strong.** WoodMac puts US data-center critical electrical equipment at 18–36 months. Manufacturers are adding about 20% to year-old POs (CDU-CONN) | 18–36 months. Distribution transformers went from 3–6 months to 1–2+ years (DOE, M0). MV switchgear OEM weeks: **GAP** |
| 5 | **Gas turbines / on-site generation** | Behind-the-meter power | GE Vernova, Siemens Energy, MHI, Caterpillar; Bloom fuel cells / China: GAP | **Strong.** GEV has 116 GW of backlog plus reservations. Siemens has 69 GW of backlog plus 26 GW reserved. MHI has 35 GW (RPT §2.2) | About 24 months (stage 1 doc) |
| 6 | **Shell + MEP (land, permits, building)** | The building itself | Comfort Systems, Quanta, Sterling, EME (EPCs); DLR, EQIX, Crusoe / China: GAP | **Medium.** Builds are getting slower: filed schedules have risen from about 9–12 months (2024 starts) to a median of about 19.9 months (Sep–Oct 2026 registrations), and deliveries arrive a median of about 4 months late, none early (LL "Shell build stage"). Skilled labour scarcity is a risk factor (EME, LL) | Abilene ~12 months to first energized building and ~15 months to live. Helios ~15 months. MSFT Fairwater ~33 months to equipment online. xAI Colossus retrofit: 122 days (LL). Permits as a separate step: **GAP** |
| 7 | **UPS + batteries** | Ride-through when power drops | Vertiv, ETN, Schneider; Delta/Lite-On BBU (Taiwan) / China: Megmeet (rack power) | **No evidence** that it binds. Bill-of-materials counts only (Vertiv RD027/028, M0) | **GAP** |
| 8 | **Busway / PDUs / 800 VDC power racks** | Get power to the racks | Vertiv, ETN, Schneider; Delta, Lite-On, AcBel, Flex / China: Megmeet | **Medium (emerging).** RPT §2.3 names 800 V power conversion as a pinch point. HVDC volume is 2027 (Delta, M0) | 800 VDC mass production Nov-26 to Q1-27 for ASICs, GPUs about Q2-27 (Lite-On, M0) |
| 9 | **Cold plates / CDUs / manifolds** | Direct-to-chip liquid loop | Vertiv, CoolIT (Ecolab), Boyd (ETN), nVent, Delta / China: GAP | **Medium.** Lead times are short, but buyers are told to lock orders about 24 months ahead. RPT also lists "qualified liquid-cooling parts" as a pinch point | CDUs 16–24 weeks, cold plates 12–16 weeks, manifolds 8–12 weeks (CDU-CONN, LL) |
| 10 | **Chillers / dry coolers / cooling towers** | Reject the heat | Modine, Vertiv, Trane-class / China: GAP | **Weak.** Modine has a $4B capacity agreement for 2027–29 (estimated, RPT §2.3) | Dry coolers 20–30 weeks. Chillers and cooling towers: **GAP** |
| 11 | **Water** | Make-up water for cooling | Utilities / China: GAP | **No evidence** in our data. Claude flagged it as a gap (consults/claude-base-components.md) | **GAP** |
| 12 | **Racks / servers (ODM)** | Integrate the NVL72-class rack | Foxconn, Quanta, Wistron, Supermicro, Dell, Pegatron / China: Lenovo, Inspur-class GAP | **Weak.** Supermicro has capacity for 6,000 racks a month (RPT §2.3) | Customer rail pulls lead ODM shipments by 2–3 months (LL). Board→rack weeks: **GAP** |
| 13 | **Networking switches** | Scale-out fabric | NVIDIA, Arista, Broadcom, Accton / China: GAP | **No evidence** that it binds (revenue only, RPT) | **GAP** |
| 14 | **Optics (transceivers ← InP lasers)** | GPU↔switch links | Coherent, Lumentum, Fabrinet, AAOI / **China: Innolight #1, Eoptolink #2** | **Medium.** RPT §2.3 names InP lasers as a real pinch point. TPUs alone imply more than 6M 800G+ modules (estimated) | AAOI is taking capacity from 200k to 650k units a month by YE26. Lead time: **GAP** |
| 15 | **Copper / NVLink cables, connectors** | Scale-up inside the rack | Amphenol, Credo, TE / China: GAP | **No evidence** (record orders only) | **GAP** |
| 16 | **Accelerators** (own chain) | The compute | NVIDIA, Broadcom (TPU/MTIA), AMD; TSMC, SK hynix, Samsung, Micron / **China: Huawei Ascend, Cambricon** (M0 row 41) | **Strong, but upstream.** Gated by CoWoS slots and HBM, not by design capacity (RPT §2.4) | CoWoS booking 52–78 weeks (AE/connections/INDEX.md, secondary). Rack bring-up: **GAP** |

**Bridge rules (for game balance, sourced):** a Vera Rubin NVL72 rack is 330 kW cabinet TDP with 72 GPUs (CONN rubin-nvl72). 1 GW holds roughly 350–430k GPUs, about 2.3–2.8 kW per GPU all-in (RPT, derived).
**Key insight for the game:** chips can ship while the hall waits 0.5–3 years for MV gear and the liquid loop (CDU-CONN). Power-on dates, not chip counts, decide when compute arrives.

## Ranked bottlenecks (stage 2)
1. Grid interconnect queue slot
2. LPT/GSU transformers (30–36 months, about 160 weeks)
3. HV breakers (125 weeks)
4. MV gear and switchgear (18–36 months)
5. Shell build (median 16.5–20 months and rising, about 4 months late)
6. InP optics lasers
7. 800 VDC power conversion
8. Liquid cooling (short lead times, but needs a 24-month order lock)
9. Chillers
10. ODM racks, UPS, switches, copper, water: no evidence they bind

## Proposed stage-2 buildings (5)
1. **Switchgear works:** makes MV transformers and switchgear, 18–36 months (WoodMac).
2. **Hall builder (shell + MEP):** placing a hall takes about 15 months (Abilene/Helios actuals). A retrofit option is 122 days (Colossus).
3. **Cooling plant:** makes CDUs and cold plates (16–24 and 12–16 weeks) plus dry coolers (20–30 weeks).
4. **Rack integrator (ODM):** turns accelerators, optics and power shelves into an NVL72 rack (330 kW). Rail→ship 2–3 months.
5. **Grid queue office:** not a factory. It spends research or time to get an interconnect slot (wait time is a **GAP**). The way around it is your own stage-1 turbines behind the meter.
Accelerators come in as a trickle import at first (the "chips arrive before the hall" lesson), until stage 3 unlocks the fab, HBM and CoWoS.

**Second goal:** "Energize your first 100 MW AI hall: about 300 Rubin-class racks (330 kW each, ~0.1 GW) running on your own turbines + switchgear + cooling." Win text: *compute online*. Score starts counting accelerator-hours.

## GAPs to fill (next research asks)
Interconnect queue wait in months; MV switchgear weeks; UPS/BBU, chiller, cooling tower and optics lead times; water use per MW; China supplier share for transformers, switchgear and cooling; permitting duration; board→rack weeks; build times for factories (switchgear works, cooling plant, ODM line); the eco-scale data on 204 was not fully searched.
