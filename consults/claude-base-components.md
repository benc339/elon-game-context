# Race to SI — independent read on base components and the opening

All numbers below carry a source on the same line: either a URL or a bundle path. Where I had no source I wrote **GAP** rather than guess. I introduced **no numbers from outside the bundle**, so there are no NEW-flagged facts — that is itself a finding: the questions your opening hinges on (ore-side lead times, foundry build times) are not answerable from what you have.

## 1. The component tree, down to raw inputs

Your tree in `elon-game-context/BASE-COMPONENTS.md` §1 is structurally right. I'd restate it with two changes: *power* splits into **energy** and **electrical plant** (they bind differently), and the chip side needs a **tool** branch, because in this ecosystem equipment, not material, is what actually gates (`ai-ecosystem/model/LEAD-LAG.md`, RQ-067 rows).

**Power side**
- Energized MW ← grid tie **or** behind-the-meter generation. BTM is real: xAI's Southaven permit is 41 turbines ≈ 1.2 GW (`elon-game-context/README.md` §4a, MDEQ PSD 10 Mar 2026 via Compute Atlas).
- Gas turbine ← hot-section blades & vanes ← single-crystal casting ← Ni superalloy (vacuum melt) ← Ni, Co, Cr, Ta, Re. Blades/vanes run "12 to 18 months behind the rest of the turbine" (https://www.fool.com/earnings/call-transcripts/2026/10/20/spacex-spcx-q3-2026-earnings-call-transcript/). Turbine lead time 24 months (EIA AEO2026 Electricity Market Module Table 3, via `elon-game/v11/index.html` DUR.gt). Casting-machine commitment → earliest output ~24 months (Howmet Q2 2026 call, `elon-game-context/README.md` §5).
- Also turbine ← rotor forgings, casings, generator — "castings and forgings arriving in '27" (GE Vernova Q2 call 22 Jul 2026, `elon-game-context/README.md` §5).
- Grid tie ← large power transformer ← GOES core steel + copper windings + bushings + OLTC. LPT typical 30–36 months PO→receipt, EHV up to 60 months (NLR via `ai-ecosystem/model/LEAD-LAG.md`); US GSU ~160 weeks in Q1 2026 vs 143 weeks 2024 (https://www.reuters.com/business/energy/us-power-companies-scramble-secure-equipment-surging-data-center-demand-strains-2026-07-09/); bushings ≤130 weeks, OLTC 80–90 weeks (NLR, `ai-ecosystem/model/LEAD-LAG.md`); HV breakers ~125 weeks (same Reuters line, `ai-ecosystem/reports/2026-10-02-ecosystem-report.md` §2.2). GOES and copper-cathode tonnage: **GAP**.
- Fuel ← natural gas (well). Binding evidence: **GAP**.
- Hall side: shell/EPC, MV gear, UPS/PDU/800 VDC, liquid cooling. Critical electrical 18–36 months (https://www.woodmac.com/press-releases/data-center-demand-drives-us-electrical-equipment-market-to-$65b-reshaping-industry-dynamics/); CDU 16–24 wk, cold plate 12–16 wk, dry cooler 20–30 wk, manifolds 8–12 wk (https://thecoolingreport.com/intel/data-center-cooling-supply-chain-guide-2026.html).

**Chip side**
- Accelerator package ← CoWoS ← logic die + HBM stacks + interposer + ABF substrate. Booking ~52–78 weeks (secondary, `ai-ecosystem/model/LEAD-LAG.md`); TSMC CoWoS ~70k wpm 2025 → 130–140k YE26 → 185–190k YE27 (TrendForce/KGI estimates, `ai-ecosystem/reports/2026-10-02-ecosystem-report.md` §2.6).
- Logic die ← 300 mm wafer ← CZ ingot ← polysilicon ← MG silicon ← quartz + carbon. Smelter ~3 yr, poly plant 36 months ("Building a polysilicon plant can easily take three years", ChemSusChem 2023, via `elon-game/v11/index.html` DUR.poly), CZ/wafer plant ~29.5 months (GlobalWafers Sherman groundbreak 1 Dec 2022 → open 15 May 2025, `elon-game/v11/index.html` DUR.cz). China ~90% of global polysilicon capacity 2023 (Bernreuter via v11 SRC).
- Crucible branch: HPQ quartz (Spruce Pine) → fused-quartz crucible. Build times: **GAP** (v11 marks hpq 30 mo / cru 12 mo as assumptions, `elon-game/v11/index.html` DUR).
- Tool branch: EUV (ASML sole supplier; barred from China since 2019, v11 SRC), TC/hybrid bonders (BESI Q3-26 orders timed to customer 1H27 plans ⇒ ~2–3 quarters, `ai-ecosystem/model/LEAD-LAG.md`; Hanmi PO→term-end ~3 months, Hanmi KIND 2026-06-08), test (NVIDIA total test capacity 2× CY2026→CY2027, GTC Berlin 2026-10-21, `ai-ecosystem/model/LEAD-LAG.md`).
- Materials branch: ABF film (Ajinomoto >95% high-end share; Gifu construction 2028, ops **2032**, `ai-ecosystem/connections/CONN-2026-09-20-abf-fcbga-ajinomoto.md`); T-glass (Nittobo Fukushima ≈×3, production Q4 FY2026 = Jan–Mar 2027, `ai-ecosystem/tasks/CLAIM-LEDGER.md` CL-2026-10-06-NTB-FUKU3X); electronic gases (2022 neon shock, `elon-game/docs/NODES.md` l.36).

## 2. What makes a good tier-0 ore here

DSP's ores work because they are **continuously extracted, cheap, multi-use, and never the thing you wait for** — the waiting is in the machines. Criteria for this game, ordered by weight:

1. **Fan-out ≥ 3 downstream recipes.** A one-use ore is a recipe input, not an ore.
2. **Flow-rate controllable by the player.** The lesson must be "I built more mine", not "I waited for an allocation."
3. **It must *not* be the binding constraint.** This is the one your doc half-misses. Ores should be abundant so the player learns that the scarcity is in *tooling and lead time* — which is exactly what the ecosystem data says (GSU ~160 weeks vs fuel: no evidence of binding, `elon-game-context/BASE-COMPONENTS.md` §3).
4. **Sourced extraction duration**, because of your build-time rule.
5. **A teachable West-vs-China or single-site fact** attached to it.
6. **Recipe reuse across both branches** (power and chip), so the same ore stays relevant after the chip layer unlocks.

Note the tension between (3) and "bottom-up from REAL bottlenecks": the bottlenecks are *not* at tier 0. So tier 0 should be the **floor you stand on**, and the first goal should be the first thing above it that actually makes you wait.

## 3. Candidate ores

| Candidate | Fan-out | Player-controlled | Binds today? | Verdict |
|---|---|---|---|---|
| **Copper** | transformers, generators, cables, busbar, cold plates, NVLink copper (>5,000 cables per GB200 NVL72, `ai-ecosystem/reports/2026-10-02-ecosystem-report.md` §2.3) | mine→cathode, simple | no sourced mine-supply bind — **GAP** | **Best power-side ore.** Highest fan-out of anything in the tree, and uniquely spans power *and* rack. |
| **Quartz → MG-Si → poly** | wafers (logic, DRAM, interposer), crucibles, solar | yes | no AI-shortage print (`elon-game-context/BASE-COMPONENTS.md` §3) | **Best chip-side ore**, and the only chain with *sourced* build times end to end (36 mo poly, 29.5 mo CZ, v11 DUR). Keep for layer 2. |
| **Iron → GOES electrical steel** | transformer cores, generator laminations | yes (ore + rolling) | GOES specifically: **GAP** | Good *tier-1*, bad tier-0: fan-out 2, and you must already have iron. Its value is explanatory — it's why the ~160-week GSU exists. |
| **Natural gas** | turbine fuel; nothing else | yes (well) | no evidence of binding | **Reject as ore.** Fan-out 1. It's a good *flavour* building (free-ish fuel beside a scarce machine), not a tier-0. |
| **Nickel + Co/Cr/Ta → superalloy** | blades, vanes, (later) rockets/engines | needs vacuum melt — not "simple" | the *casting*, not the alloy, is the chokepoint (Wood Mackenzie names single-crystal hot-section blades the critical bottleneck, `elon-game-context/README.md` §5) | Tier-1. Making it an ore would teach the wrong lesson. |
| **Rhenium** | superalloy only | byproduct, not mined to order | world mine ~81 t (2025); ~80% of US use in superalloys (USGS MCS 2026 via v11 SRC) | **Flavour**, as your doc says. Excellent as a hard cap on blade output later. |
| **Neon / helium** | fab etch & litho | air separation | historical only (2022 shock, NODES l.36) | **Event**, not ore. Perfect as a mid-game shock that halts a running fab. |
| Others worth naming | **Water** (cooling; 1 MW = 284.3 refrigeration tons, `elon-game-context/README.md` §4a) and **land/interconnect queue position** (ERCOT ~410 GW LLI, ~87% DC, `ai-ecosystem/model/MODEL-v0.md`) | — | the queue genuinely binds | Neither is an ore, but **interconnect queue slot** is the most under-modelled scarce *resource* in your design. Consider it a non-belt currency. |

So: **two ores, copper and quartz/silicon** — same conclusion as your doc, reached for a sharper reason (fan-out + cross-branch reuse, not just "multi-use").

## 4. Critique of BASE-COMPONENTS.md and opening B

**Right, and worth keeping.** The depth-0 framing ("accelerator running in an energized data center") is the correct root — it forces power and chips to converge on one object. The ore-criteria list is sound. The per-node evidence discipline (GAP, sourced-duration column) is the document's real asset and should survive into the game's Sources panel unchanged. And the headline lesson you've extracted — the binding constraint is **power-on dates, not chips** (Nebius 16–20% of 5 GW connected by YE26; Nscale 25k of 461k GPUs, `ai-ecosystem/reports/2026-10-02-ecosystem-report.md` §2.1) — is the right thing for a player to feel in hour one.

**Wrong or risky.**
1. **Opening B has no ore, and you've recorded that as a "con" when it's a rule violation.** Your own brief says bottom-up from raw inputs and DSP-style; B's inputs "arrive as fixed-rate world supply" (`elon-game-context/BASE-COMPONENTS.md` §4B). A DSP opening where nothing is extracted isn't a bare DSP opening — it's an allocation-management game. Fixed-rate world supply (1 turbine / 8 months, 1 blade set / 2 months, v11 SRC) is a *waiting* mechanic. Waiting is the lesson of hour three, not minute one.
2. **B's build times are almost all assumptions**: blade foundry 36 mo, alloy melt 24 mo, turbine assembly 18 mo, install 3 mo — all `s:0` in `elon-game/v11/index.html` DUR. Opening B therefore violates "build times proportional to real sourced durations" *more* than opening C does, where smelter/poly/CZ are sourced. Your doc notes this as a con; I'd rank it as disqualifying for the *opening* specifically, since the opening is where a learn-while-playing game earns trust.
3. **Recommending "B + copper as first research unlock" hides the ore behind a tech gate**, which means the first 20 minutes have no extraction loop at all. That's the same shape as v8–v11, just with a different first building.
4. **Missing nodes.** No **interconnect/queue** node despite it being the best-evidenced bind. No **water/heat-rejection** node (284.3 refrigeration tons per MW is sourced). No **equipment/tool** tier on the chip side, even though your own LEAD-LAG file says cleanroom and tool availability, not materials, gate 2026–27 shipments (AMAT: "it will be the availability of clean room ... that will determine what we can all ship next year", `ai-ecosystem/model/LEAD-LAG.md`). No **labour** node, though EME's risk factor names skilled-labour scarcity (same file).
5. **One factual soft spot**: the doc credits "PCC + Howmet ~80% of high-end SX casting (one expert)". The bundle's firmer figure is Howmet's own claim of **more than 50% of the global IGT blade market** (Q2 2026 call, secondary transcript, `elon-game-context/README.md` §5). Use the sourced one.

## 5. Three openings, ~6 buildings each

**Opening A — "Copper and the core" (power ore).** Copper mine · iron mine/DRI · GOES rolling line · transformer works · substation/grid tie · R&D lab.
First goal: *energize 10 MW through a transformer you wound yourself.*
Teaches: the ~160-week GSU (Reuters 2026-07-09) as a thing you can beat by building, and copper's fan-out. Risks: GOES and copper lead times are **GAP**; mine/mill build times **GAP**.

**Opening B — "Hot section" (yours).** Blade & vane foundry · alloy melt · turbine assembly · transformer works · substation · R&D lab.
First goal: *energize your first substation with your own turbine.*
Teaches: the real Musk move and the single hardest-evidenced bottleneck. Risks: no extraction; 4 of 6 build times are assumptions.

**Opening C — "Fuel, metal, power" (hybrid; my recommendation).** Gas well · copper mine · transformer works · substation/grid tie · gas turbine pad (first turbine from world allocation) · R&D lab.
First goal: *put 100 MW of AI load on line.* Then the research tree's first two branches are **blade & vane foundry** (because the allocated turbine arrives slower than you can use it — 12–18 months behind, SpaceX Q3 2026 call) and **GOES line** (because the transformer is the longest sourced item you own).

**I recommend C.** It satisfies every rule simultaneously, which neither A nor B does: two extracted ores from minute one (gas is trivially simple, copper has the fan-out), a sourced-duration spine (turbine 24 mo EIA; transformer 30–36 mo NLR / ~160 wk Reuters; electrical 18–36 mo WoodMac), and a first goal that is a *number of megawatts*, not a building — so it generalises straight into the real metric the whole ecosystem is measured in (GW). It also keeps AI and data centers hidden exactly as long as you want: the player is chasing MW and only later learns what the MW are for. And critically, it makes B's lesson the *first research reward* rather than the opening premise: you feel the blade lag as a wait you chose to escape, which is a far better teaching moment than starting with a foundry you don't yet know you need.

Gas earns its place here not as an ore by my own criteria (fan-out 1) but as the **tutorial ore** — the frictionless one that teaches belts and the shared power pool before copper teaches scarcity. If you'd rather hold the line on fan-out, swap the gas well for a quartz mine and accept that silicon arrives 10 minutes earlier than planned.

## Before you build, close these

GOES supply/lead time and China share · copper cathode and winding-wire lead times · blade-foundry, alloy-melt and turbine-assembly build durations (all four currently assumptions in `elon-game/v11/index.html` DUR) · substation build duration as distinct from component lead times · copper mine and GOES mill build durations · whether the ProEnergy 6000PE shares LM6000 lineage (open per `elon-game-context/README.md` §4c), which decides whether your 154-blade/94-vane figure applies to the Southaven mix. The eco-scale DB on 204 (15 GB, 461 nodes / 3,129 sourced facts per `ai-ecosystem/reports/2026-10-02-ecosystem-report.md` header) was never mined for any of these — that's the cheapest place to start.
