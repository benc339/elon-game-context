# Race to SI: sub-component chokepoint tree (stages 1–2)
Written 2026-10-23. Design doc only. Nothing is invented. Every claim cites a file. If no file had it, the node says **GAP**.

**Tags**
- **BINDING**: evidence it is short now.
- **POTENTIAL**: a sourced reason it could bind (concentration, long lead time, a small market, export controls, by-product supply, past shortage).
- **NO EVIDENCE**: searched and nothing found.
- **GAP**: not researched, or the data names the question without answering it.

Recursion continues under BINDING and POTENTIAL nodes and stops at NO EVIDENCE, GAP or raw material.

**Path shorthand**
- `AE` = /workspace/ai-ecosystem
- `RQ039` = AE/sources/2026-10-03-rq039-tx-swgr-lt-batch1.md
- `RQ065` = AE/sources/2026-10-06-rq065-optics-supply-batch1.md
- `RQ069` = AE/sources/2026-10-08-rq069-inp-substrate-batch1.md and AE/sources/2026-10-16-rq069-inp-substrate-batch5.md, batch6.md
- `RPT` = AE/reports/2026-10-02-ecosystem-report.md
- `SOFAR` = AE/reports/2026-10-23-research-so-far-main.txt
- `204:` = 204:/home/dev/eco-scale/data/…

**Search coverage:** /workspace/ai-ecosystem was searched with ripgrep, excluding backups and tmp. On 204, data/, sources/ and units/ were searched by file name only, plus grep of graph/edges.json, graph/eco-map.json and findings/.
- These terms had **zero hits in both places**: rhenium, magnet/winding wire, insulating oil, pressboard (only "transformerboard"), and casting furnaces.

## Tree
```
[0] Powered AI hall
├─[1] Gas turbine (stage 1). BINDING: GEV 116 GW backlog + reservations, Siemens 69+26 GW, MHI 35 GW (RPT §2.2). About 24 months.
│  ├─[2] Hot-section blades & vanes. BINDING: run "twelve to eighteen months behind the rest of the turbine"; SpaceX casts its own (SOFAR)
│  │  ├─[3] Investment casters (Howmet, Doncasters/DPC, PCC). POTENTIAL (concentration): Howmet ">50% globally for turbine blades in the IGT market" (secondary; 204:data/graph/eco-map.json, Howmet node). Doncasters 2025 rev $837M (424B4, same file)
│  │  │  ├─[4] Ceramic cores. POTENTIAL (small, specialised; capacity being added): Howmet Whitehall MI new ceramic-core building, up to $107.5M through 2028 (204: Howmet Whitehall facility node). Supplier shares: GAP
│  │  │  ├─[4] Ni superalloy remelt/ingot. GAP: 204 lists it as an open question ("Which nickel superalloy remelt/ingot and ceramic-core suppliers feed Doncasters, Howmet…")
│  │  │  │  └─[5] Rhenium (by-product of molybdenum/copper). GAP: zero hits in our data. The by-product logic is a hypothesis to verify, not sourced here
│  │  │  └─[4] Vacuum casting furnaces. GAP (zero hits)
│  ├─[2] Large forgings (rotors/discs). NO EVIDENCE (only unrelated "forging" hits)
│  └─[2] Behind-the-meter alternatives: recip engines (Caterpillar restarting about 1.5 GW, RPT), Bloom fuel cells. NO EVIDENCE of sub-chokepoints
│
├─[1] Large power transformer / GSU. BINDING: about 160 weeks (RPT); LPT 30–36 months, EHV up to 60 months; US imports about 80%+/82%, domestic about 30% (2023) (RQ039)
│  ├─[2] HV bushings. BINDING: "longest LPT-component LT, up to 130 weeks", 345 kV >130 weeks, "no domestic 765-kV bushing suppliers" (RQ039; AE/tea-leaves/2026-09-20-idea-bushings-oltc-lpt-gate.md). RPT: "Not really" priced in
│  │  └─[3] Bushing inputs (porcelain/resin-impregnated paper, condenser cores). GAP
│  ├─[2] On-load tap changers (OLTC). BINDING + POTENTIAL (concentration): 80–90 weeks; "only 1–2 U.S. manufacturers"; "Reinhausen only U.S. OLTC producer" (RQ039)
│  │  └─[3] OLTC inputs (contacts, vacuum switching). GAP
│  ├─[2] GOES (grain-oriented electrical steel). POTENTIAL: RPT names "GOES steel under large transformers" as a sub-component play ("Partially" priced in). 204 has a node "US grain-oriented electrical steel for transformers" (204:data/graph/edges.json). Supplier count, China share and lead time: GAP
│  │  └─[3] Iron ore / silicon steel slab. NO EVIDENCE (raw)
│  ├─[2] Transformerboard / pressboard. POTENTIAL (named, thin): RPT/course "Not really" priced in; no lead time or share. GAP on numbers
│  ├─[2] Copper winding / magnet wire. GAP (zero hits)
│  └─[2] Insulating oil. GAP (zero hits)
│
├─[1] HV circuit breakers. BINDING: about 125 weeks (RPT)
│  ├─[2] SF6 gas / SF6-free. POTENTIAL (regulatory): SF6 leak limits ≤0.5%/yr in permits (AE/scale/graph/nodes.json, Kilby plant); Eaton buying COL Group (MV SF6-free) for €810M (204:data/graph/edges.json). Supply concentration: GAP
│  └─[2] Interrupters. GAP
│
├─[1] MV switchgear / MV transformers. BINDING: 18–36 months (WoodMac, RPT); distribution transformers 3–6 months → 1–2+ years (DOE, RQ039); MV switchgear OEM weeks MISS
│  ├─[2] Vacuum interrupters. GAP: 204 only asks the question ("Which manufacturers supply vacuum interrupters… to US MV switchgear OEMs?", 204:data/findings/grid_electrical/T90971958954748.json)
│  └─[2] Copper busbar / insulation. GAP (same open question)
│
├─[1] Liquid cooling. POTENTIAL (order lock): CDUs 16–24 weeks, cold plates 12–16 weeks, manifolds 8–12 weeks, dry coolers 20–30 weeks; lock about 24 months ahead (AE/connections/CONN-2026-09-20-cdu-coldplate-mw-electrical.md). "Qualified liquid-cooling parts" a pinch point (RPT)
│  ├─[2] CDUs / rear-door heat exchangers (Vertiv, Motivair–Schneider, CoolIT–Ecolab). NO EVIDENCE beyond the above
│  ├─[2] Cold plates (vacuum-brazed microchannel). POTENTIAL (few qualified fabricators; WORKING thesis only): /workspace/idea-farm/theses/working/thesis-microchannel-coldplates-hyperscale-2026-09-09.md
│  ├─[2] UQD liquid couplings. POTENTIAL (named): RPT "Not really" priced in. GAP on numbers
│  ├─[2] Stainless manifolds (ASME). GAP: AE/tea-leaves/2026-09-20-idea-asme-stainless-cdu-manifolds.md (idea only)
│  └─[2] Pumps. GAP (only pump-laser hits)
│
├─[1] Rack power (800 VDC shelves, BBU, busbars). POTENTIAL: "800 V power conversion" a pinch point; HVDC volume 2027 (RPT; AE/model/MODEL-v0.md rack-power row)
│  ├─[2] Power shelves/PSUs (Delta, Lite-On, AcBel, Flex; China: Megmeet). POTENTIAL (new 100–110 kW SKUs certify 1Q27, volume 2H27 for AcBel; MODEL-v0)
│  │  └─[3] SiC/GaN power devices (Infineon). GAP
│  ├─[2] Rack busbars / power whips (BizLink). NO EVIDENCE (share not reported; AE/scale/audits/work/sig.json)
│  └─[2] Copper NVLink cables/connectors (Amphenol, Credo, TE). NO EVIDENCE
│
└─[1] Optics (transceivers). BINDING upstream (RQ065: assembly is not the constraint, lasers are)
   ├─[2] InP lasers (EML/CW): Coherent, Lumentum, Sumitomo, Mitsubishi. BINDING: COHR "indium phosphide capacity continues to be our primary constraint"; LITE "shipping behind customer demand on EML… significantly behind demand" at YE; CPO lasers "way behind" (RQ065). Steps: COHR InP 2× by Sep-26, >2× again by end-2027 (Zurich 6-inch 1H27); LITE EML >+50% by Dec-26 quarter
   │  ├─[3] InP substrates/wafers (AXT, Sumitomo, JX). BINDING + POTENTIAL: LITE "secured additional InP substrate supply from AXTI… probably going to need more help on substrate" (RQ065). AXT InP rev $30.7M Q2'26, a record; backlog "well over $100 million" into 2027; capacity 2× in 2026, again in 2027 (RQ069). Small market
   │  │  └─[4] Indium metal. POTENTIAL (China concentration): "China controls 70% of global InP supply; Yunnan Germanium Industry is the core target" (AE/scale/findings/optics/T90992321489287.json → techflowpost, secondary). Export-control status: GAP
   │  └─[3] Pump lasers. BINDING: "Pump lasers sold out; ~3-year take-or-pay"; "significantly undershipping demand" (AE/scale/graph/nodes.json; AE/scale/findings/optics/*)
   ├─[2] PAM4 DSPs (Marvell, Broadcom; 3nm). POTENTIAL (2-supplier market, leading-edge wafers): Marvell "first 3nm PAM4 optical DSP" (AE/scale/graph/eco-map.json). Shortage: NO EVIDENCE
   ├─[2] MT/TMT ferrules. POTENTIAL (named): RPT "Not really" priced in. GAP on numbers
   └─[2] Module assembly (Innolight, Eoptolink in China; Fabrinet). NO EVIDENCE: Eoptolink about 38% and Innolight about 85% of printed capacity used (RQ065)
```

## Chains, deepest real chokepoint → DC
1. **Indium (China ~70%, POTENTIAL)** → InP substrate (BINDING) → InP EML/CW lasers (BINDING) → optical transceivers → GPU fabric → hall
2. **Pump lasers (BINDING, sold out, 3-year take-or-pay)** → optical links → hall
3. **HV bushings (BINDING, up to 130 weeks, no US 765 kV maker)** → LPT/GSU (BINDING, 30–36 months) → substation → grid power → hall
4. **OLTC (BINDING + 1 US maker, 80–90 weeks)** → LPT → substation → hall
5. **Ceramic cores / Ni superalloy (POTENTIAL / GAP)** → investment casting (POTENTIAL: Howmet >50% of IGT blades) → hot-section blades (BINDING, 12–18 months behind the turbine) → gas turbine (BINDING) → power → hall
6. **GOES (POTENTIAL)** → transformer core → LPT → hall
7. **SF6 regulation (POTENTIAL)** → HV breakers (BINDING, 125 weeks) → substation → hall
8. **800 VDC power shelves (POTENTIAL, 2027 volume)** → racks → hall
9. **Qualified cold plates / UQDs (POTENTIAL)** → CDU loop (24-month order lock) → hall energization

## Good deeper game layers
- **InP laser fab ← InP substrate ← indium.** This is the best China-dependence story, with the strongest evidence.
- **Bushing + OLTC shops** feeding the transformer works. They are binding, and the US barely makes them.
- **Investment casting ← ceramic cores ← superalloy** feeding the blade foundry. This is the real hot-section chain, but rhenium and superalloy are GAPs.
- **GOES mill** as the ore-to-transformer link. It fits the DSP-style ore loop, but its numbers are GAPs.

## Top GAPs to research
- Rhenium supply and China share
- GOES producers, lead time and China share
- Vacuum interrupter makers
- Superalloy melters
- Magnet wire, insulating oil and pressboard
- Casting furnaces
- Indium export controls
- Pumps
- SiC/GaN supply for 800 VDC
