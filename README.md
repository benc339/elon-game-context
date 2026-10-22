# Elon compute-empire game: idea + AI-ecosystem context pack

Compiled 22 Oct 2026 (ET). This is a starting brief for building the game from scratch: the idea in Bence's words, plus sourced real-world knowledge. How to build it is entirely up to the builder.

**Number rules.** Every figure has a period and a source. **Sourced** means a named public source printed it. **Derived** means our own arithmetic on sourced inputs, and it is never a source figure.

---

## 1. The idea (Bence's words, close paraphrase)

- The game should be like **Dyson Sphere Program**, in **3D**, but on **all of Earth**.
- You **play as Elon**, starting in **October 2026** with the real state of the world. That includes his real assets:
  - the Tesla factories
  - SpaceX's capabilities
  - the **13 GW data-center plan** for next year (end-2027)
  - making his own **turbine blades and vanes**
- You **compete with the other companies** for supply from the chip ecosystem.
- You **order from the real suppliers**: TSMC, the memory makers, the turbine makers, and so on.
- There's a **creative tech tree**, because we don't know what Elon will invent. One example is the **modular inference boxes with power built in** that he mentioned (quote below).

## 2. Musk's modular inference-box quote (Sourced)

> "We think there's also a lot of opportunity for inference compute if you manufacture modular inference compute at the factory level and then such that it's -- the power and cooling are built in at the factory and then you distribute modular inference compute clusters all over the country, if not all over the world. That's about as much as I should say about scaling power and cooling."

Source: Elon Musk, SpaceX (SPCX) Q3 2026 earnings call, 20 Oct 2026, from the Motley Fool transcript: https://www.fool.com/earnings/call-transcripts/2026/10/20/spacex-spcx-q3-2026-earnings-call-transcript/

This was an idea mentioned on the call. No product, size or date was announced.

## 3. SpaceX/xAI headline facts (SPCX Q3 2026 call, 20 Oct 2026, and Q3 release)

- **Nameplate compute:**
  - 1.7 GW at 30 Sep 2026; 1.4 GW at Q2 2026; 0.6 GW at Q3 2025 (SpaceX Q3 2026 results release).
  - "nearly 2.2 GW" at end-Oct 2026, and 2.5–3.0 GW by end-Q4 2026 (CFO on the call).
- **Plan layers.** These are different layers, not contradictions:
  - Musk would be "surprised" by less than **13 GW of compute by end-2027**.
  - He is "highly confident" of **10 GW added in 2027**.
  - There is a "small possibility" of about 23 GW total.
  - There is a **+20 GW power and cooling** plan for 2027, sized "far in excess of what is needed ... to turn the GPUs on".
- **GPU pace.** Musk: "roughly 200,000 GB300s online per month for every month for the remainder of this year and continuing that pace next year. With next year being primarily Rubin, Vera Rubin compute."
  - A later "20,000 GB300s a month" in the same call is treated as a speaker slip.
  - [Derived] Check: +~0.5 GW in about a month at ~2.44 kW per GPU at facility level ≈ 205k GPUs. 20k a month would add only ~0.05 GW.
- **Training cluster:** 440,000 Vera Rubin by end-Q2 2027.
- **Blades and vanes:** turbine OEMs say blades and vanes run "12 to 18 months behind the rest of the turbine", and "we're casting the blades and vanes for the turbines" (Musk).
- **Capex:** Q3 2026 total $19.6bn; Q4 2026 guide $35–40bn (CFO). Space Infrastructure capex was $16,444M in Q3 (release).
- **Economics:** new compute has a "payback of less than a year". Pricing is slightly above the high end of $30–50 per watt.
- **Other:** Starship Flight 14 reached orbit. Starlink has 13.6M consumer subscribers and 90% of global mass to orbit. Terafab targets a test chip in mid-2027 and volume by Q3 2028 (Fool key-points summary).

## 4. 13 GW breakdown: from gigawatts down to blades and vanes

The basis is open: the company doesn't define "nameplate". The October ramp fits a **facility basis** (IT × PUE ~1.3) better than an IT-only basis, so both are shown. The roll-up uses only "13 GW total / 10 GW added in 2027".

### 4a. Per-GW coefficients
| Part | Sourced input (period, source) | Per GW [Derived] |
|---|---|---|
| GPUs, GB300 | NVL72 = 72 GPUs, 132–140 kW operating (Supermicro datasheet, 2026); 142 kW max (NVIDIA reference architecture, 2026) | IT basis 514k–545k GPUs; facility basis at 2.44 kW/GPU (Nodus Partners, 2026) ~410k |
| GPUs, Vera Rubin | VR200 NVL72: Max-Q ~1.8 kW/GPU, ~190 kW/rack; Max-P ~2.3 kW, ~230 kW (Ming-Chi Kuo via CTEE, 7 Jan 2026) | IT 313k–379k packages; facility (PUE 1.3) 241k–292k |
| Rubin Ultra | 3.6 kW/package; Kyber rack 144 packages, ~600 kW (Tom's Hardware; Nodus, citing GTC 2025) | IT ~240k packages |
| HBM | GB300 288 GB HBM3e (Supermicro); Rubin 288 GB HBM4, 8 stacks (Tom's Hardware); Rubin Ultra 1 TB HBM4E (Tom's Hardware / GTC 2025) | GB300 IT 148k–157k TB; Rubin IT 90k–109k TB (0.72–0.87bn Gb) |
| Other DRAM | 960 GB LPDDR5X per 4-GPU GB300 tray (Supermicro) | GB300 IT ~123k–131k TB |
| CoWoS | Rubin = CoWoS-L, 2 compute + 2 I/O dies + 8 HBM (Tom's Hardware). Packages per wafer are **not sourced** | OPEN |
| NICs | GB300: 4× ConnectX-8 800G per 4 GPUs (Supermicro); Rubin uses CX-9 1.6T (Tom's Hardware), count not sourced | GB300 IT 514k–545k 800G NICs |
| Turbines | Southaven permit: 17 Solar Titan 130 + 16 Titan 350 + 8 ProEnergy 6000PE = 41 units, ~1.2 GW (MDEQ PSD permit 10 Mar 2026 via Compute Atlas); SMT-130 ~16 MW (Tom's Hardware, 2025) | ~34 turbines/GW for this mix (~29 MW/unit) |
| Blades/vanes | GE LM6000 HPT stage 1: 80 blades + 23 two-vane nozzle segments (46 vanes); stage 2: 74 blades + 24 segments (48 vanes) (GE LM6000 PC/PD/PG/PH technical details deck). GE 7HA.03 is a 4-stage turbine, counts not printed (GE Vernova whitepaper) | 154 HPT blades + 94 vanes per LM6000-class turbine. Titan 130/350 counts OPEN |
| Transformers | Illustrative 1.42 MVA firm per MW IT; N+1 3×75 MVA per 100 MW (J. R. Sterling, 2026); HV units typically 50–100 MVA, >12-month lead (SemiAnalysis, 2024) | 1.42 GVA firm / 2.25 GVA installed per GW ≈ 19–30 HV units at 75 MVA |
| Cooling | GB300 ~90% liquid / 10% air (Lenovo via Nodus); in-row CDU up to 1.8 MW per 8 racks (Supermicro); 1 MW = 284.3 refrigeration tons | ~284k tons of heat; ~556 in-row CDUs per GW IT |
| $/GW | SpaceX capex above; SemiAnalysis ~$50bn/GW (7 Aug 2026); NVIDIA content ~$40bn/GW Vera Rubin, ~$25bn/GW Grace Blackwell (Jensen Huang, NVDA Q2 FY27 call, Aug 2026) | $27–50bn per GW added (whole-company capex, an upper bound) |

### 4b. What 10 GW added in 2027 implies (all Derived)
These bounds treat the whole 10 GW as VR200 NVL72 ("primarily Vera Rubin").
- **Rubin packages:** 3.1–3.8M on an IT basis, or 2.4–2.9M on a facility basis. Cross-check: 200k/month × 12 = 2.4M.
- **HBM4:** 0.69–1.09 EB ≈ 5.5–8.8bn Gb in 2027, about 7–18% of our 48.6–75.2bn Gb modelled 2027 HBM demand.
- **NVIDIA content:** ~$400bn.
- **All-in capex:** ~$270–500bn.
- **Gas turbines:** ~340 units if all power were on-site gas at the Southaven mix, which Musk says it won't be ("not just gas turbines"). That means ~52k HPT blades and ~32k vanes. This is an upper-bound illustration, not a forecast.
- **HV transformers:** 14.2 GVA firm / 22.5 GVA installed ≈ 190–300 units at 75 MVA.
- **Cooling:** ~2.8M refrigeration tons; ~5.6k in-row CDUs (GB300-class sizing).

### 4c. Tensions
- **KGI (15 Sep 2026)** expects 5.89M Rubin + 2.85M Rubin Ultra in CY2027. xAI's 10 GW alone would be 2.4–3.8M Rubin packages, **41–65% of KGI's Rubin**, before any other customer.
  - This is a tension, not a contradiction: it isn't confirmed whether KGI counts dies or packages.
- **$/GW:** $40bn/GW of NVIDIA content would leave only ~$0–10bn/GW for everything else. That is implausible against power and shell costs, and probably reflects IT-basis GW vs nameplate GW.
- **Still unsourced:**
  - CoWoS-L packages per wafer
  - Titan 130/350 blade counts
  - whether the ProEnergy 6000PE shares the LM6000 lineage
  - Rubin NICs and transceivers per GPU
  - Rubin CDU sizing
  - SpaceX's GB300/Rubin mix
  - the non-gas share of power
  - OEM slot allocations
  - xAI's actual transformer sizing

## 5. Turbine and casting supply (the blades-and-vanes bottleneck)

**Howmet (HWM):**
- Gas Turbines end-market revenue was **$944M in FY2025** (10-K, 12 Feb 2026).
- It was **$284M in Q1 2026, +39% y/y** (Q1 deck, 7 May 2026), and **$321M in Q2 2026, +38% y/y** vs $233M (10-Q, 6 Aug 2026).
- The company targets going from ~$1B (2025) to $2B+ in 3–5 years (Tech & Markets Day, 10 Mar 2026).
- On the Q2 2026 call (6 Aug 2026, secondary transcript), it claimed **more than 50% of the global industrial gas turbine (IGT) blade market** and said **~24 months** pass from committing a new casting machine to its earliest output.

**GE Vernova:**
- Gas turbine run rate is **20 GW/yr in Q3 2026**, rising to **24 GW/yr in 2028**, with "castings and forgings arriving in '27" (2Q26 call, 22 Jul 2026). It is "mostly sold out through '30".

**Siemens Energy:**
- Company-compiled consensus for **Gas Services FY2027 revenue is €16,723m** (17 estimates, as of 17 Jul 2026, published 29 Jul 2026). Orders are €32,315m and the margin before special items is 18.3%.
- FY2025 Gas Services revenue was 66% service and 34% new units (Annual Report 2025).
- New units have **"~€400m per GW"** of revenue potential (CMD, 20 Nov 2025), and capacity is ~22 GW/yr across all frames (FY2025–27 average, same CMD).
- **Blades and vanes are its biggest limit.**
- [Derived] €16,723m × 34% ÷ €400m/GW ≈ 14 GW of new units (≈21 GW at a 50% share). This fits inside the 22 GW/yr capacity.

**Other casting supply:**
- SpaceX's in-house **blades-and-vanes foundry in Bastrop, TX** was reported at **$280M** (1 Sep 2026, secondary).
- Doncasters IGT revenue was $351M in FY2025, and an industry forecast puts IGT airfoil casting orders at +9%/yr over 2024–2035 (S-1, 15 Jun 2026).
- MHI targets +30% gas turbine shipments by FY2028 and has started precision-casting capex (27 May 2026).
- GE Aerospace agreed to acquire CPP for $11.75bn (8 Sep 2026).
- Wood Mackenzie names single-crystal hot-section blades the industry's critical bottleneck. It puts global gas turbine capacity at ~60–70 GW/yr and the large power transformer lead time at 18–36 months.


## 6. Rival gigawatt plans (Sourced, Oct 2026 unless noted)
| Rival | Figures (source, period) |
|---|---|
| OpenAI Stargate | 7 US sites >9 GW planned: Abilene 1.2, Shackelford 2.0, Milam 1.2, New Mexico 2.2, Wisconsin 1.3, Michigan 1.4, Ohio <0.3 GW. Abilene ~0.3 GW was operational in Apr 2026 (Epoch AI, 2026). Original commitment 10 GW / $500B (OpenAI). Non-US sites not sourced |
| Oracle | >10 GW of power/DC capacity secured, coming online over 3 years; >400 MW delivered in Q3 FY26 (DCD / Oracle CEO blog, Mar 2026). Bloom fuel cells up to 2.8 GW, 1.2 GW contracted (Bloomberg, 13 Apr 2026). Overlaps Stargate |
| Meta | Prometheus (New Albany, OH): ~471 MW operating, 1 GW by Q3 2028 (Engineering at Meta, 19 Oct 2026; BlockWest). Hyperion (LA): 1.632 GW by Q1 2028, 2 GW by 2030, ~5 GW by ~2032 (BlockWest; Epoch); $50B Louisiana investment (CNBC, 13 Jul 2026) |
| Microsoft | Fairwater Wisconsin: 369 MW operating, 2.263 GW by Q2 2028 (BlockWest, Oct 2026). Fleet GW not sourced. Maia 300 "potentially more than a million" units next year (Reuters, 12 Oct 2026) |
| AWS | ~3.8–3.9 GW of power added in the trailing 12 months; plans to double capacity by end-2027; 2026 capex ~$200B (The Register, 6 Feb 2026; DCD; CRN) |
| Anthropic | ≥14.8 GW of disclosed commitments (SEDaily, 7 Sep 2026): Amazon up to 5 GW; Google/Broadcom TPU ~3.5 GW arriving 2027 + ~1 GW in 2026; AMD up to 2 GW (first GW H1 2027); Azure $30B with no GW given. Overlaps AWS/Google |
| Google | 2026 capex guide $195–205B (Alphabet Q2 call, 22 Jul 2026). No fleet GW disclosed |
| CoreWeave | 1.5 GW active at end-Q2 2026; ~3.7 → ~4.2 GW contracted (Q2 2026 results, 11 Aug 2026) |

Tesla (Tesla Q3 2026 update, 21 Oct 2026):
- Installed vehicle capacity: Shanghai >950k, Fremont >550k, Berlin >375k Model Y, Texas >375k Model Y + >125k Cybertruck + >125k Cybercab, Nevada Semi 25k.
- Megapack: 40 GWh (CA) + 50 GWh (TX) + 20 GWh (Shanghai).
- Optimus: early ramp in Fremont, under construction in Texas.

## 7. Further sourced and derived reference figures
| Type | Value | Source / date |
|---|---|---|
| Sourced | Inference boxes, Musk verbatim: "We think there's also a lot of opportunity for inference compute if you manufacture modular inference compute at the factory level and then such that it's -- the power and cooling are built in at the factory and then you distribute modular inference compute clusters all over the country, if not all over the world. That's about as much as I should say about scaling power and cooling." | Motley Fool transcript, SpaceX (SPCX) Q3 2026 call, 20 Oct 2026 (an idea on the call; no product, size or date announced) |
| Sourced | Nameplate compute "nearly 2.2 gigawatts … at the end of this month alone in October"; 2.5–3 GW by end-Q4 2026 (CFO) | Motley Fool transcript, SpaceX (SPCX) Q3 2026 call, 20 Oct 2026 |
| Sourced | "surprised" if less than 13 GW of compute by end-2027; "highly confident of 10 gigawatts" added in 2027; +20 GW power/cooling plan for 2027 | Motley Fool transcript, SpaceX (SPCX) Q3 2026 call, 20 Oct 2026 |
| Sourced | "roughly 200,000 GB300s online per month … next year being primarily Rubin, Vera Rubin" (a later "20,000" on the same call is treated as a slip) | Motley Fool transcript, SpaceX (SPCX) Q3 2026 call, 20 Oct 2026 |
| Sourced | 440,000 Vera Rubin training cluster by end-Q2 2027 | Motley Fool transcript, SpaceX (SPCX) Q3 2026 call, 20 Oct 2026 |
| Sourced | Blades/vanes "12 to 18 months behind the rest of the turbine"; "we're casting the blades and vanes for the turbines" | Motley Fool transcript, SpaceX (SPCX) Q3 2026 call, 20 Oct 2026 |
| Sourced | Q4 2026 capex guide $35–40bn; Q3 capex $19.6bn | Motley Fool transcript, SpaceX (SPCX) Q3 2026 call, 20 Oct 2026 |
| Sourced | New compute "payback of less than a year"; pricing slightly above the high end of $30–50 per watt | Motley Fool transcript, SpaceX (SPCX) Q3 2026 call, 20 Oct 2026 |
| Sourced | Starship Flight 14 reached orbit and deployed Starlink V3; Flight 15 "next month" will try to catch both stages; weekly flights "at some point in the first half next year" | Motley Fool transcript, SpaceX (SPCX) Q3 2026 call, 20 Oct 2026 |
| Sourced | Starlink 13.6M consumer subscribers; 90% share of global mass to orbit | Motley Fool transcript, SpaceX (SPCX) Q3 2026 call, 20 Oct 2026 |
| Sourced | Terafab roadmap: test chip mid-2027, volume production by Q3 2028 | Motley Fool transcript, SpaceX (SPCX) Q3 2026 call, 20 Oct 2026 (Fool key-points summary) |
| Sourced | Southaven permit: 41 turbines (17 Titan 130 + 16 Titan 350 + 8 ProEnergy 6000PE) ≈ 1.2 GW, MDEQ PSD 10 Mar 2026 | Compute Atlas; MDEQ PSD permit |
| Sourced | GE LM6000 HPT: 154 blades + 94 vanes per turbine | GE LM6000 tech-details deck |
| Sourced | GE Vernova: 20 GW/yr gas turbines (3Q26) → 24 GW (2028); "mostly sold out through '30" | GE Vernova Q2 call, 22 Jul 2026 |
| Sourced | Siemens Energy ~50 large gas turbines/yr from FY27 | Siemens Energy Q3 FY26 deck / pre-close call, 2026 |
| Sourced | Global gas turbine capacity ~60–70 GW/yr | Wood Mackenzie  |
| Sourced | Large power transformer lead time 18–36 months | Wood Mackenzie (as compiled 3 Oct 2026) |
| Sourced | NVIDIA content ~$40bn/GW Vera Rubin, ~$25bn/GW Grace Blackwell | Jensen Huang, NVDA Q2 FY27 call |
| Sourced | KGI CY2027: 5.89M Rubin + 2.85M Rubin Ultra | KGI, 15 Sep 2026 |
| Sourced | TSMC CoWoS ~140k wafers/month end-2026 → ~220k end-2027 | Institutional estimate, SECONDARY |
| Sourced | 2027 HBM demand 48.6–75.2bn Gb; Rubin 288 GB HBM4 | Our 2027 HBM demand model range (derived); Tom's Hardware |
| Sourced | Tesla installed capacity: Shanghai >950k, Fremont >550k, Berlin >375k Model Y, Texas >375k Model Y + >125k Cybertruck + >125k Cybercab, Nevada Semi 25k; Megapack 40 GWh (CA) + 50 GWh (TX) + 20 GWh (Shanghai); Optimus: early ramp (Fremont), construction (Texas) | Tesla Q3 2026 Update deck, 21 Oct 2026 |
| Sourced | Rival plans: OpenAI Stargate >9 GW across 7 US sites (~0.3 GW Abilene live); Oracle >10 GW over 3 yrs; Meta Prometheus 1 GW by Q3 2028 + Hyperion 1.632 GW by Q1 2028; Microsoft Fairwater WI 2.263 GW by Q2 2028 (fleet not sourced); AWS +3.8–3.9 GW TTM, doubling by end-2027; Anthropic ≥14.8 GW commitments (overlaps AWS/Google); Google 2026 capex $195–205bn (no GW given); CoreWeave 4.2 GW contracted / 1.5 GW active | (Epoch, DCD, BlockWest, SEDaily, Alphabet, CoreWeave, Oct 2026) |
| Derived | ~34 turbines/GW → ~29 MW per unit (Southaven mix) | 1.2 GW ÷ 41 |
| Derived | GPUs per GW: GB300 ~410k, Vera Rubin ~270k (facility basis, PUE 1.3) | 13 GW breakdown (this doc, §4) (Supermicro, Nodus, Kuo) |
| Derived | HV transformers ~19–30 per GW; in-row CDUs ~556 per GW | 13 GW breakdown (this doc, §4) |
| Derived | NVIDIA 2027 output ≈ 34 GW/yr ≈ 8.5 GW per quarter | KGI units ÷ packages/GW (unit basis not confirmed) |
| Derived | Revenue ≈ $10bn per GW online per quarter | <1-year payback on ~$40bn/GW |


## 9. Main public sources
- SpaceX Q3 2026 call transcript (Motley Fool, 20 Oct 2026): https://www.fool.com/earnings/call-transcripts/2026/10/20/spacex-spcx-q3-2026-earnings-call-transcript/
- SpaceX Q3 2026 results: https://s21.q4cdn.com/184289198/files/content_files/SpaceX-Reports-Third-Quarter-2026-Results.pdf
- Supermicro GB300 NVL72 datasheet: https://www.supermicro.com/datasheet/datasheet_SuperCluster_GB300_NVL72.pdf
- NVIDIA NVL72 reference architecture: https://docs.nvidia.com/enterprise-reference-architectures/nvl72-ai-factory/latest/components.html
- Nodus Partners, AI rack power: https://nodus.partners/insights/ai-rack-power
- CTEE / Kuo, VR200: https://www.ctee.com.tw/news/20260107701081-430704
- Tom's Hardware, Vera Rubin in depth: https://www.tomshardware.com/pc-components/gpus/nvidias-vera-rubin-platform-in-depth-inside-nvidias-most-complex-ai-and-hpc-platform-to-date
- Compute Atlas, Colossus 2 power station: https://www.compute-atlas.com/facilities/xai-colossus-2-power-station-southaven-ms
- Tom's Hardware, xAI turbines: https://www.tomshardware.com/tech-industry/xai-pushes-power-strategy-towards-1gw-ai-factory
- J. R. Sterling, substation MVA: https://julianrsterling.com/articles/data-centre-substation-size-mva/
- SemiAnalysis, Datacenter Anatomy part 1: https://newsletter.semianalysis.com/p/datacenter-anatomy-part-1-electrical
- Epoch AI, Stargate sites: https://epoch.ai/publications/openai-stargate-where-the-us-sites-stand
- Engineering at Meta, Prometheus: https://engineering.fb.com/2026/10/19/data-center-engineering/inside-prometheus-meta-gigawatt-scale-supercluster/
- Plus the filings and calls named inline: Howmet 10-K/10-Q/calls, GE Vernova 2Q26, Siemens Energy CMD/consensus/AR, Tesla Q3 2026 update, KGI, CoreWeave, Oracle, AWS and Alphabet.
