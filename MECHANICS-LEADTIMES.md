# Race to SI — lead-time & chokepoint mechanics (driven by TREE.json)
Written 2026-10-23. Data: /workspace/ai-ecosystem/chokepoint-tree/TREE.json (198 nodes; fields id, name, tag, depth, parents, children, evidence, source, lead_time). Every number below is copied from TREE.json/branch files; none invented. GAP ⇒ placeholder, shown in-game with a "placeholder" badge.

## The one time-scale factor
**K = 1 real-world month of lead/build time → 1 game minute** (so 30–36 months ≈ 30–36 min; 130 weeks ≈ 30 min; 52–78 weeks ≈ 12–18 min). Every queue, build and event date uses K and nothing else; the game calendar starts 2026-10-23 and advances at the same K (1 game minute = 1 calendar month), so dated events fire at the right relative moment. Tuning = change K only.

## (a) Order vs build, for every part
Each node has two paths: **Order** = join a world queue with the sourced lead time (`lead_time`); **Build** = your own factory, taking its sourced build time. Missing figures ⇒ placeholder.
| Part (TREE.json id) | Order lead time (sourced) | Own-factory build time |
|---|---|---|
| Large power transformer / GSU (`power:large-power-transformers-…`) | 30–36 months; EHV up to 60 months (NLR); GSU ~160 wk (Street view, WoodMac/Reuters) | 1–3 years (DOE 2024, via ChatGPT Pro consult) |
| HV bushings | up to 130 weeks (NLR) | placeholder (GAP) |
| On-load tap changers | 80–90 weeks (NLR) | placeholder |
| HV breakers / GIS | ~125 weeks (Street view) | placeholder (`Interrupter/drive/casting supply` GAP) |
| MV switchgear (`dcelec:mv-switchgear-…`) | 52–80 wk; 78–104 wk at 38 kV | placeholder |
| Turbine hot-section blades | Howmet new capacity earliest Aug 2028 | placeholder (blade foundry build time = GAP) |
| CoWoS (`cowos`) | 52–78 weeks (secondary) | placeholder |
| HBM (`hbm-stacks`) | sold out (GAP on weeks) → placeholder | placeholder |
| Liquid cooling CDUs/cold plates | order ~24 months ahead | placeholder |
| AI hall shell (`dcbuild:building-shell-…`) | — | median ~19.9 months (n=9); 122 days Colossus outlier |
| Substation (`power:transmission-build-substation`) | — | ~3 months transformer→full energization (Abilene, one site); generic = placeholder |

## (b) Visible order queues on the globe
Each supplier node with a location (e.g. TSMC Taiwan for `cowos`/`logic-die`; Ajinomoto Japan for `abf-film`; Nittobo Japan for `t-glass`; Howmet blades; Hitachi/Siemens/Hyosung transformer plants incl. Siemens Charlotte 2027, Hitachi South Boston 2028) shows a queue ring with a real countdown (lead time × K). You compete for slots with other buyers: CoWoS allocation uses `CoWoS demand by customer` (NVIDIA ~60% of 2026 global demand, Street view MS); grid slots use `grid-queue` (ERCOT ~410 GW, ~87% DC). West vs China queues are separate where the tree says so (China stack: SMIC 7nm-class DUV, CXMT/Huawei HBM).

## (c) BINDING chokepoints ⇒ stalls + assistant explanation
When a building waits on a BINDING node, it stalls and the assistant explains with the node's evidence line and source link. Uses all 43 BINDING nodes; main ones: grid-queue, LPT, bushings, OLTC, HV breakers, MV switchgear, blades/casting furnaces/rotor forgings, CoWoS, HBM (DRAM wafers, TSV stacking, TC bonders, base die), ABF substrate/film, T-glass, logic die/EUV, helium, InP lasers/substrates, 800G/1.6T transceivers (~30% 1.6T shortfall, secondary), UQD couplings, land/zoning (~75 projects, ~$130B, Q1 2026), electricians (349k workers needed 2026).

## (d) POTENTIAL chokepoints ⇒ dated world/China events
| Event (date) | Node | Effect |
|---|---|---|
| Texas ≥75 MW energization pause until report due **2026-12-10** | `grid-queue`, ERCOT PGRR 145 node | new halls can't energize on grid until then; own generation bypasses |
| China's suspension of gallium/germanium export ban to US **ends 2026-11-27** | `gallium` (China 99% primary), `germanium` | GaN power stages, GaAs lasers, fiber dopant: random chance of re-ban → queues lengthen |
| China indium export controls (since Feb 2025) | `indium` (~70% China refinery), `dcbuild:inp-export-permit-regime` | InP substrate permits can be delayed |
| Helium / Qatar halt (2026; spot prices doubled, Reuters 2026-03-12) | `helium` | fab throughput hit; Barclays "manageable tail risk" ⇒ moderate severity |
| Refrigerant steps (AIM Act 2027/2029) | `dcelec:refrigerants-…` | chiller cost/time step |
| Fluorspar (China 58%; 3M PFAS exit) | `fluorspar` | seals, fluorinated gases, SF6 |
Event dates are mapped through K.

## (e) Research unlocks in-house chokepoint parts
Research nodes = BINDING/POTENTIAL parts you can make yourself: transformer works (+GOES line, copper winding), bushing & tap-changer shop, switchgear works (+vacuum interrupters), blade foundry (+ceramic cores, superalloy melt, rhenium sourcing), cooling plant (cold plates, UQDs, CDUs), rack integrator, later fab/HBM/CoWoS/substrate (ABF film, T-glass). Unlocking moves a part from path (a)-Order to (a)-Build; build time from TREE.json or placeholder.

## (f) Score = compute online over time vs China
Score starts when the first hall energizes (stage 2 goal: 100 MW hall, ~300 Vera Rubin racks). Curve = compute online vs a China curve built from the China nodes (SMIC 7nm DUV Ascend, CXMT HBM; their volumes are GAPs ⇒ placeholder curve, labelled). Reference: SpaceX/xAI 1.7 GW at 30 Sep 2026, ~2.2 GW end-Oct, 2.5–3.0 GW end-Q4 2026 (README.md).
