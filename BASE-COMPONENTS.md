# Race to SI — Base components (design only, 23 Oct 2026 ET)

Rules: only facts found in local files; every evidence line cites a path. **GAP** = nothing found locally (needs research). Server 204 (`/home/dev/eco-scale`) was **not** checked.
Path shorthands: `ECO` = /workspace/ai-ecosystem · `CTX` = /workspace/elon-game-context/README.md · `V11` = /workspace/elon-game/v11/index.html (SRC/DUR/CARDS tables, sourced rows marked S) · `NODES` = /workspace/elon-game/docs/NODES.md · `RPT` = ECO/reports/2026-10-02-ecosystem-report.md

## 1. Component tree (depth 0 = accelerator in a powered DC; higher = further upstream)

```
0 Accelerator running in an energized data center
├─1 Power (energized MW)
│ ├─2 Gas turbine
│ │ ├─3 Hot-section blades & vanes (single-crystal casting)
│ │ │ └─4 Ni superalloy (vacuum melt)
│ │ │   └─5 Rhenium, nickel, cobalt, Cr, Ta (raw)
│ │ └─3 Rotor forgings, casings, generator (commodity industrial)
│ ├─2 Fuel: natural gas (raw)
│ └─2 Grid tie / substation
│   ├─3 Power transformers (GSU / HV)
│   │ └─4 GOES electrical steel, copper winding, transformerboard, bushings, OLTC
│   └─3 HV circuit breakers / switchgear
├─1 Data center building
│ ├─2 Shell + EPC construction (steel, concrete)
│ ├─2 Electrical gear (switchgear, UPS, PDU, 800 V DC conversion)
│ └─2 Liquid cooling (CDUs, cold plates, dry coolers)
└─1 Accelerator package (CoWoS)
  ├─2 Logic die (N3/N2 foundry)
  │ ├─3 300 mm wafer ← 4 CZ ingot ← 5 polysilicon ← 6 MG silicon ← 7 quartz + carbon (raw)
  │ │                   └─ 5 HPQ quartz crucibles (Spruce Pine)
  │ ├─3 EUV lithography (ASML; Zeiss optics)
  │ ├─3 Photoresist (EUV resist)
  │ └─3 Electronic gases (Ne, He, NF3, HF)
  ├─2 HBM stacks
  │ ├─3 DRAM wafers (same wafer/litho tree)
  │ ├─3 Base logic die (foundry, e.g. Samsung 4nm)
  │ └─3 TSV + stacking: TC / hybrid bonders, NCF/underfill
  ├─2 Silicon interposer (foundry)
  └─2 Organic substrate (ABF FC-BGA)
    ├─3 ABF build-up film (Ajinomoto)
    └─3 T-glass low-CTE glass cloth (Nittobo)
```

## 2. Node cards

| Node (depth) | Role | Key suppliers · West vs China | Bottleneck evidence | Sourced duration |
|---|---|---|---|---|
| Gas turbine (2) | On-site/utility MW | GE Vernova, Siemens Energy, MHI (West/Japan) | Sold out: GEV 53 GW firm + 63 GW slots; Siemens 69+26 GW; MHI 35 GW (RPT l.90) | Lead time 24 mo, EIA AEO2026 (V11 DUR.gt) |
| Blades & vanes (3) | Hot-section parts; limiting step of turbine build | PCC + Howmet ~80% of high-end SX casting (one expert, V11 SRC) | "12–18 months behind the rest of the turbine" (CTX §3); xAI casting its own (CTX) | Lag 12–18 mo (CTX). Foundry build: GAP |
| Superalloy (4) | Ni alloy for >1,000 °C parts | PCC Special Metals, Cannon-Muskegon, Howmet (V11 CARDS) | no evidence | GAP |
| Rhenium (5) | ~3% of 2nd-gen SX alloy (assumption) | world mine ~81 t (2025); ~80% of US use in superalloys (USGS MCS 2026, V11 SRC) | scarcity implied by tiny volume; no shortage print | — |
| Natural gas (2) | Turbine fuel | — | no evidence | — |
| Power transformer (3) | Step-up to grid voltage | GE Vernova, HD Hyundai Electric, Hitachi (backlogs RPT l.92) | GSU ~160 wk Q1 2026 vs 143 wk 2024 (RPT l.91) | ~160 wk ≈ 37 mo |
| GOES / copper / bushings (4) | Transformer core, windings | GAP (suppliers, China share) | Bushings ~145 wk est. (ECO/reports/2026-10-03-podcast2-dialogue-script.md); GOES, copper: GAP | Bushings ~145 wk (est.) |
| HV breakers (3) | Grid protection | Powell (15 kV 35–40 wk, podcast2 script) | ~125 wk H2 2025 vs 77 wk 2023 (RPT l.91; ECO/scale/corrections/BOT-eco-powergrid-20261003-1055-street-mark.json) | ~125 wk |
| Grid / energization (2) | Power-on date | utilities, ISOs | Nebius 16–20% of 5 GW connected by YE26; Nscale 25k of 461k GPUs (RPT l.85) | lease→delivery 14–26 mo (ECO/logs/keepalive-2026-10-05-0651.md) |
| DC building (1) | Hall + EPC | Quanta, Comfort Systems, DLR (RPT l.92–95) | gated by power, not shell (RPT l.98) | Galaxy Helios I ~15 mo to 133 MW (ECO/model/MODEL-v0.md l.83); Colossus 1: 122 days (retrofit outlier, ECO/model/LEAD-LAG.md l.116) |
| DC electrical gear (2) | Switchgear, UPS | Vertiv, Schneider, ABB, Eaton | 18–36 mo (WoodMac, ECO/connections/CONN-2026-09-20-cdu-coldplate-mw-electrical.md) | 18–36 mo |
| Liquid cooling (2) | CDUs, cold plates | Vertiv, CoolIT, Modine, nVent | "usually not binding" (RPT l.116) | CDU 16–24 wk, cold plate 12–16 wk, ~24 mo planning lock (RPT) |
| Foundry N3/N2 (2) | Logic die, interposer, HBM base die | TSMC 72.5% share; SMIC 93.5% util. (RPT l.159) | "tight… more than a scarcity choke point" (RPT l.161) | new fab 2–3 yr (ECO/model/LEAD-LAG.md l.47) |
| Wafer / ingot (3–4) | 300 mm substrate | Shin-Etsu, SUMCO, GlobalWafers, Siltronic, SK Siltron (V11 SRC) | no evidence of binding | GlobalWafers Sherman ~29.5 mo (V11 DUR.cz) |
| Polysilicon (5) | 11N silicon | Hemlock, Wacker (West); China ~90% of global capacity 2023 (V11 SRC, Bernreuter) | West-vs-China concentration, no AI shortage print | plant ~36 mo (V11 DUR.poly) |
| MG silicon / quartz (6–7) | Raw silicon | Ferroglobe, Elkem (V11 CARDS) | no evidence | smelter ~3 yr, PCC BakkiSilicon (V11 DUR.smelt) |
| HPQ crucibles (5) | Hold molten Si in CZ | Spruce Pine (Sibelco/IOTA); Helene flood Sep 2024 (V11 CARDS) | single-site risk; no shortage print | GAP |
| EUV (3) | 2nm litho | ASML sole EUV maker; Dutch rules bar sales to China since 2019 (V11 SRC) | "long-cycle gate for 2nm and below" (RPT l.167); no lead time | GAP |
| Photoresist (3) | Litho chemistry | JSR, TOK (EUV resist +50%) (RPT l.174) | no evidence | GAP |
| Electronic gases (3) | Etch/litho/clean | Linde, Air Liquide; 2022 neon shock (NODES l.36) | no current evidence | GAP |
| HBM (2) | Memory stacks | SK hynix, Samsung, Micron | 12-Hi HBM4 ~$600 (2026) → ~$1,300 (2027); volumes locked through 2027 (RPT l.137–143) | fab TAT 3–4 mo (ECO/scale/corrections/IdeaFarmManager-20261003-1102-street-sweep-hbm_dram.json IFM-SW-183) |
| TSV / bonders (3) | Stack HBM | Hanmi, BESI (BESI orders +129% y/y, RPT l.165) | Hanmi new plant "to pre-empt equipment shortage", production 2Q27 (ECO/tasks/CLAIM-LEDGER.md l.436) | GAP |
| CoWoS (1) | 2.5D package | TSMC ~70k wpm 2025 → 130–140k YE26; ASE, Amkor | consensus bottleneck, gap ~20% → ~10% YE26 (RPT l.155) | booking 52–78 wk (ECO/model/LEAD-LAG.md l.31) |
| ABF film (3) | Substrate dielectric | Ajinomoto ~95% share | +30% price (est.); next plant ops 2032; substrates >90% util. (RPT l.172–176) | Gifu plant: build 2028 → ops 2032 |
| T-glass (3) | Low-CTE cloth | Nittobo, Nan Ya | price up + allocation priority; Nittobo ≈×3 from Jan–Mar 2027 (ECO/research-questions/RQ-QUEUE.md l.58) | GAP |

## 3. Tier-0 "ore" analysis (DSP-style)

A good tier-0 ore: (a) feeds many downstream recipes, (b) is mined/extracted, simple to produce, (c) teaches a real lesson, (d) has evidence it matters.

| Candidate | Downstream uses in this tree | Simple/extracted | Lesson | Evidence | Verdict |
|---|---|---|---|---|---|
| Copper | transformers, generators, DC electrical, cables | yes (mine→cathode) | "everything electric needs copper" | rack-copper gated by qualification, not physical (ECO/model/MODEL-v0.md l.78); mine supply GAP | **Strong ore**, evidence weak |
| Electrical steel (GOES) | transformers, generators | iron ore + rolling (2 steps) | why transformers take ~3 yr | GAP locally | Good tier-1, needs research |
| Natural gas | turbine fuel only | yes (well) | fuel is cheap, machines are scarce | no evidence of binding | Weak ore: one use, doesn't bind |
| Nickel / superalloy | blades, vanes, (later) engines | needs vacuum melt | material science of hot section | no binding evidence | Tier-1, not ore |
| Rhenium | superalloy only | byproduct of copper/moly | tiny world volume (~81 t) | USGS via V11 | Flavor ore; one use |
| Quartz → silicon | MG-Si → poly → wafers; HPQ → crucibles; also solar | yes | "chips are refined sand + electricity"; China 90% poly | V11 SRC | **Strong ore for chip layer**, not for power |
| Rare gases (Ne/He) | fab processes | air separation | 2022 neon shock | historical only (NODES) | Late-game event, not ore |

Read: **copper** and **quartz/silicon** are the only true multi-use ores. Copper anchors the power layer; silicon anchors the chip layer and can arrive later via research.

## 4. Opening proposals (~6 buildings each)

**A. "Power from metal" (copper + steel ore).** Copper mine, iron/steel mill → electrical-steel line, transformer works, turbine assembly (blades from world allocation), substation, R&D lab.
- Pros: genuine DSP ore loop; transformer (~160 wk) is the slowest sourced item, so building your own is the core lesson; copper reused later in DC electrical.
- Cons: copper/GOES binding evidence is a GAP; mine/mill build times all placeholders.
- First goal: energize your first substation with a transformer you wound yourself.

**B. "Hot section" (approved earlier).** Blade & vane foundry, turbine assembly, transformer works, substation, R&D lab, + industrial load / grid export.
- Pros: every bottleneck has evidence (turbine backlogs, 12–18 mo blade lag, 160 wk GSU, 125 wk breakers); matches Musk's real "we're casting the blades" move.
- Cons: no extracted ore — inputs arrive as fixed-rate world supply; foundry/assembly build times are placeholders.
- First goal: energize your first substation with your own turbine.

**C. "Sand and power" (silicon from day one).** Gas turbine (world supply), quartz mine, smelter, polysilicon plant, CZ puller, R&D lab.
- Pros: best ore story; strongest West-vs-China fact (China ~90% poly); sourced build times (smelter ~3 yr, poly ~36 mo, CZ ~29.5 mo).
- Cons: this is the v8–v11 opening Bence just moved away from; ingots do not bind for AI (no evidence); power bottleneck only felt passively.

**Recommendation: B, with A's copper as the first research unlock.** B is the only opening where every core step is evidence-backed as binding today, and it teaches the report's headline lesson ("power-on dates, not chips"). Add copper mine + electrical-steel line as the first tech so the transformer works gets a real ore feed (tier 0) once the copper/GOES gap is researched. Silicon (C) returns later as the chip-layer ore.

## 5. Research gaps to close before building
GOES supply/lead time and China share; copper cathode/winding supply; transformer works and blade-foundry build times; substation build time (only breaker/transformer lead times exist); EUV tool lead time; photoresist and gas shortages; T-glass and HBM bonder lead times; 204 eco-scale not mined.
