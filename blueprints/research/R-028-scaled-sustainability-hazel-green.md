# R-028 — Scaled sustainability for a ~87,000 GSF arena in Hazel Green (solar, rainwater, daylight, LED + HVAC)

Researched by KEYSTONE 2026-10-14 (daily automation, ~6:10 AM CT). Feeds D-018 (rooftop solar + stormwater storage = Phase 2 design intent, **unsized**) and the PARKING_LOT sustainability item.
Status: research note. **PRELIMINARY — CONCEPTUAL DESIGN — NOT FOR CONSTRUCTION. Not an engineering design, not a tax opinion, not a bid.**
**Order-of-magnitude ranges only.** Nothing here sets a size in `params/phase2.yaml`; `sustainability.*.size` stays **TBD** until Shane sizes it and the architect / MEP engineer confirms.
Labels: **CITED** = from a source below · **ASSUMED** = KEYSTONE planning factor or arithmetic on cites · **DECIDED** = Shane (D-###).

**Mercedes-Benz Stadium rule (PARKING_LOT, prompt §4):** its 4,000 panels, 680,000-gal cistern, 1.1M-gal vault / 2.1M-gal system and "47 %" water figure are **that stadium's numbers, not this project's** — cited once in R-028.6 as inspiration only. Never in params, never on a sheet.

## Building basis (from the repo, not new)

| Item | Value | Label |
|---|---:|---|
| TOTAL GSF | 86,964 | P2-C-101 Rev H (in review) |
| L1 footprint | 57,896 SF | P2-C-101 Rev H |
| L2 area | 29,068 SF | P2-C-101 Rev H |
| Change vs last revision | 0 SF (R-028 changes no area) | — |
| Roof plan area used below | ≈ 57,896 SF (= L1 footprint; canopies / overhangs not counted) | ASSUMED |
| Site / parcel | TBD | D-006 OPEN |
| Owner type (tax-exempt or not) | TBD | D-007 OPEN |

## Sources (all retrieved 2026-10-14)

- **S1** — NREL / NLR *PVWatts* v8 API (NSRDB PSM V3 TMY-2020 cell at 34.93 N, -86.58 W, Hazel Green). Runs: 1 kW-DC, fixed open rack, azimuth 180, losses 14 %, DC/AC 1.2, tilt 5 / 10 / 20 deg → **1,299 / 1,341 / 1,399 kWh-AC per kW-DC per year**. https://developer.nlr.gov/api/pvwatts/v8.json (calculator: https://pvwatts.nlr.gov/). Box copies `/workspace/research_src/r028/pvw_t5.json`, `pvw_t10.json`, `pvw_t20.json`. PRIMARY (model).
- **S2** — NREL (for DOE FEMP), *Foundational Course: Renewable Energy Technologies — Solar* (commercial): flat roof **8 W-DC/ft²**; sloped flush roof 11 W-DC/ft²; roof must accept added load "typically 2-4 lbs/ft²". https://www.energy.gov/sites/prod/files/2015/09/f26/Solar%20-Commercial-NREL.pdf — box copy `doe_nrel_solar.pdf`. PRIMARY (dated 2015 — module density has risen since; conservative).
- **S3** — Gagnon et al., *Estimating rooftop solar technical potential across the US...*, Environ. Res. Lett. 13 (2018) 024027: flat roofs modelled at a **0.70** module-area-to-roof-area ratio. https://iopscience.iop.org/article/10.1088/1748-9326/aaa554 — read through the search index. PRIMARY (peer-reviewed). Also NREL/TP-6A20-64793 (2016), usable roof **reduced 50 % or 65 %** for shading / obstructions: https://docs.nlr.gov/docs/fy16osti/64793.pdf (search index).
- **S4** — HUD Exchange, *Appendix F — Rooftop Calculation Tool*: 4–6 ft fire-code perimeter setback; "roughly 100 square feet of usable rooftop space to install 1 kW". https://files.hudexchange.info/resources/documents/Appendix-F-Rooftop-Calculation-Tool.pdf — box copy `hud.pdf`. SECONDARY (federal guidance).
- **S5** — Berkeley Lab, *Tracking the Sun* (2025 data update): non-residential median installed price **$2.40/W (>100 kW)**, **$3.10/W (≤100 kW)**, as reported by Mercom 2026-10: https://www.mercomindia.com/us-residential-solar-storage-adoption-jumps-to-37-in-2025 ; program page https://emp.lbl.gov/tracking-the-sun/ ; 2024 slide deck (20th / median / 80th pct, large non-res **$1.9 / $2.4 / $3.3 per W-DC**): https://escholarship.org/content/qt0zp741f0/qt0zp741f0.pdf (search index). PRIMARY data, national (not Alabama-localized).
- **S6** — Huntsville Utilities, *Solar Connect* page: **max 50 kW**; 2026 purchase rate **$0.064270/kWh**; "Huntsville Utilities does not do net metering or net billing." https://www.hsvutil.org/community_resources/programs/solar_connect_.php — fetched. PRIMARY (utility).
- **S7** — TVA EnergyRight, *Dispersed Power Production*: renewable facilities **up to 80 MW**; sell all or excess at TVA monthly avoided cost, "currently **$0.034/kWh**"; 5-year commitment. https://www.tva.com/energy/valley-renewable-energy/dispersed-power-production-program — fetched. PRIMARY (utility).
- **S8** — Hazel Green ZIP 35750 retail provider "City of Huntsville" and avg commercial rate ~**11.09 ¢/kWh**: https://eredux.com/locations/al/zip/35750/ (search index). SECONDARY aggregator — **provider for the actual parcel UNVERIFIED (D-006)**.
- **S9** — ENERGY STAR Portfolio Manager, *U.S. Energy Use Intensity by Property Type* (Aug 2024): **Indoor Arena** median **site EUI 56.2 kBtu/ft²**, source 112.0 (CBECS Public Assembly peer group); Recreation 50.8 site. https://portfoliomanager.energystar.gov/pdf/reference/US%20National%20Median%20Table.pdf — box copy `estar_median.pdf`. PRIMARY.
- **S10** — Nixon Peabody, *Renewable energy after the Big Beautiful Bill* (2025-07-24): solar 48E / 45Y need construction start **by 2026-07-04** or placed in service **by 2027-12-31**; elective (direct) pay for tax-exempt entities untouched. https://www.nixonpeabody.com/insights/alerts/2025/07/24/renewable-energy-after-the-big-beautiful-bill — fetched. SECONDARY (law firm).
- **S11** — Eide Bailly, *What the OBBB Act Means for Section 48 & 48E* (updated 2025-08-26): geothermal heat-pump property stays under §48, construction must commence before **2035-01-01** (same page also says "through 2032" — internal inconsistency, see R-028.5). https://www.eidebailly.com/insights/alerts/2025/obbb-energy-credits — fetched. SECONDARY (CPA firm).
- **S12** — NOAA NCEI 1991–2020 Normals, Huntsville Intl Airport USW00003856: **annual precipitation 54.29 in**. https://www.ncei.noaa.gov/access/services/data/v1?dataset=normals-annualseasonal-1991-2020&stations=USW00003856&format=csv&dataTypes=ANN-PRCP-NORMAL — box copy `noaa_hsv_ann.csv`. PRIMARY.
- **S13** — Texas Water Development Board, *The Texas Manual on Rainwater Harvesting*, 3rd ed.: **0.62 gal per ft² of roof per inch of rain**; collection efficiency **75–90 %** (examples use 85 %). https://www.twdb.texas.gov/publications/brochures/conservation/doc/RainwaterHarvestingManual_3rdedition.pdf — box copy `twdb.pdf`. PRIMARY (state agency manual; method is climate-independent).
- **S14** — Alabama Cooperative Extension (ACES), *Athletic Turf Management* (2020): athletic turf needs "approximately **1 to 1 1/2 inches of water per week** during the growing season" (rain + irrigation). https://www.aces.edu/blog/topics/lawn-garden/athletic-turf-management/ — fetched. PRIMARY (state extension).
- **S15** — USGS Circular 1268, conversion factors: "1 inch of rain = … **27,200 gallons per acre**". https://pubs.usgs.gov/circ/2004/circ1268/htdocs/text-conversion.html — fetched (curl). PRIMARY.
- **S16** — *Alabama Plumbing Code 2021* (IPC 2021) Chapter 13 Nonpotable Water Systems, §1301.4 permits + engineering calcs, §1303 rainwater (roof collection, debris excluder, first-flush diverter, storage tanks; outdoor irrigation piping downstream of a backflow preventer exempt from some piping rules). https://up.codes/viewer/alabama/ipc-2021/chapter/13/nonpotable-water-systems — fetched. SECONDARY host of code text.
- **S17** — U.S. DOE Building Energy Codes Program, *Alabama*: commercial code **ASHRAE 90.1-2013** (state amendments), effective 2016-01-01, mandatory statewide. https://www.energycodes.gov/status/states/alabama — fetched. PRIMARY.
- **S18** — *Alabama Energy Code 2015* (IECC 2015) on UpCodes: Table C301.1 **Madison County = 3A**; **C402.4.2** minimum skylight area; **C402.4.2.1** daylight-responsive controls under skylights. https://up.codes/viewer/alabama/iecc-2015/chapter/CE_4/ce-commercial-energy-efficiency and .../CE_3/ce-general-requirements — box copy `al_iecc15_ce4.html`. SECONDARY host. ASHRAE 90.1-2013's parallel skylight clause (§5.5.4.2.3) is **paywalled — UNVERIFIED** here.
- **S19** — U.S. DOE, *Consumer Guide to Energy-Efficient Lighting* (2021): "LEDs use **up to 90 % less energy** and last up to 25 times longer than incandescent bulbs." https://www.energy.gov/sites/default/files/2021-08/ES-EE%20Lighting_080921.pdf — box copy `doe_light.pdf`. PRIMARY.
- **S20** — U.S. DOE, *Consumer Guide to Geothermal Heat Pumps* (2021): savings "**25 % to 50 %** compared to air-source heat pump systems". https://www.energy.gov/sites/default/files/2021-08/ES-Geothermal%20heat%20pumps_080221.pdf — box copy `doe_ghp.pdf`. PRIMARY (consumer-level; not an arena study).
- **S21** — Mercedes-Benz Stadium, *Sustainability & LEED Platinum*: 4,000 PV panels ≈ 1.6M kWh/yr; 680,000-gal cistern; 1.1M-gal vault; 2.1M-gal system; 47 % water reduction. https://www.mercedesbenzstadium.com/sustainability — fetched. **INSPIRATION ONLY.**
- Not used: vendor LED gym case studies (netzero-usa, Litetronics) claiming 50–70 % vs metal halide — vendor marketing, noted only as LOW in R-028.5. Solar "kWh per kW" calculators (SunWatts 1,418, GridKalk 1,492) — superseded by S1.

---

## R-028.1 — Rooftop solar: how big, how much energy

QUESTION: What does a *scaled* rooftop PV array look like on this building's roof?

ANSWER (one paragraph): On ~57,896 SF of roof (ASSUMED = L1 footprint), with **35–65 % usable** after fire-code perimeter paths, the drum / curved roof, skylights and rooftop equipment (ASSUMED band, bracketed by S3's 50–65 % reductions and 0.70 flat-roof ratio and S4's 4–6 ft setbacks) and **8–10 W-DC per usable ft²** (S2 flat-roof 8 W; S4 ~100 ft² per kW), the roof holds roughly **LOW ~160 kW · MID ~260 kW · HIGH ~380 kW DC** (KEYSTONE arithmetic: 57,896 × 0.35 × 8; × 0.50 × 9; × 0.65 × 10). At **1,300–1,400 kWh per kW per year** in Hazel Green (S1, tilt 5–20 deg), that is roughly **0.2M · 0.35M · 0.5M kWh/yr**. For scale only: an indoor arena at the ENERGY STAR median **56.2 kBtu/ft² site** (S9) × 86,964 GSF ≈ 4.9M kBtu ≈ **1.4M kWh-equivalent/yr if all-electric** (ASSUMED all-electric) — so a full roof covers about **15–37 %** of a *median* arena's annual energy, not net-zero. Installed cost at the national large non-residential band **$1.9–$3.3/W (median $2.40)** (S5) is roughly **$0.3M–$1.2M** before incentives (KEYSTONE arithmetic; not Alabama-localized; not a bid). Structural: PV adds "typically 2–4 lbs/ft²" (S2) — the structural engineer must carry it on the long-span roof. For comparison only, Mercedes' 4,000 panels make ~1.6M kWh/yr (S21) — roughly 3–8× this roof's range.

SOURCE: PVWatts v8 — https://developer.nlr.gov/api/pvwatts/v8.json — retrieved 2026-10-14; NREL Solar foundational course — https://www.energy.gov/sites/prod/files/2015/09/f26/Solar%20-Commercial-NREL.pdf — retrieved 2026-10-14; ENERGY STAR US EUI table — https://portfoliomanager.energystar.gov/pdf/reference/US%20National%20Median%20Table.pdf — retrieved 2026-10-14; LBNL Tracking the Sun via Mercom — https://www.mercomindia.com/us-residential-solar-storage-adoption-jumps-to-37-in-2025 — retrieved 2026-10-14 (+ S3, S4).
EDITION / SECTION: PVWatts v8.5.0, NSRDB PSM V3 TMY-2020; ENERGY STAR table Aug 2024 (Indoor Arena row); LBNL 2025 data update (2024 percentile deck).
CONFIDENCE: MEDIUM (yield and EUI are primary; usable-roof fraction and density are ASSUMED bands; cost is national, not local).
NEEDS ARCHITECT CONFIRMATION: YES — roof plan area, curved / drum geometry, rooftop MEP layout, skylight area (R-028.4) and structural reserve set the real usable area.

## R-028.2 — Solar value here: utility rules and federal credit

QUESTION: What do the local utility rules and the 2025 federal tax law do to the value of a Hazel Green rooftop array?

ANSWER (one paragraph): Two things push toward a **smaller, self-consumption-sized** array rather than "fill the roof". (1) **No net metering.** Huntsville Utilities (reported retail provider for ZIP 35750, S8 — **parcel provider UNVERIFIED, D-006**) states it "does not do net metering or net billing"; its Solar Connect buyback is capped at **50 kW** and pays **$0.064270/kWh** in 2026 (S6). Larger systems can sell to TVA under Dispersed Power Production (up to 80 MW) at TVA's avoided cost, **currently $0.034/kWh** (S7) — versus roughly **11 ¢/kWh** average commercial retail in 35750 (S8, aggregator). An event-driven arena exports much of its midday output on non-event days, so exported kWh are worth roughly 30–60 % of self-used kWh (3.4 or 6.43 ¢ vs ~11.09 ¢, KEYSTONE arithmetic). (2) **Federal credit timing.** Under the 2025 OBBBA, solar under §48E/§45Y must have **begun construction by 2026-07-04** (already passed) or be **placed in service by 2027-12-31** (S10, S11). A project still at schematic design with an open site (D-006) and budget (D-012) is unlikely to meet 2027 — **plan the solar with no federal credit** unless a tax adviser says otherwise. Elective (direct) pay for tax-exempt owners was not changed (S10), but it only pays if an underlying credit exists. Practical scaled reading (ASSUMED): design the roof **"solar-ready"** (structure, conduit, roof paths) and size a first array to daytime base load — Shane / MEP to set kW.

SOURCE: Huntsville Utilities, Solar Connect — https://www.hsvutil.org/community_resources/programs/solar_connect_.php — retrieved 2026-10-14; TVA EnergyRight, Dispersed Power Production — https://www.tva.com/energy/valley-renewable-energy/dispersed-power-production-program — retrieved 2026-10-14; Nixon Peabody, Renewable energy after the Big Beautiful Bill — https://www.nixonpeabody.com/insights/alerts/2025/07/24/renewable-energy-after-the-big-beautiful-bill — retrieved 2026-10-14 (+ S8, S11).
EDITION / SECTION: HU 2026 purchase rate; TVA DPP price as posted Oct 2026 (updated monthly, "subject to change"); OBBBA (H.R. 1, signed 2025-07-04) §48E/§45Y wind-solar termination.
CONFIDENCE: MEDIUM (utility pages primary and current; parcel utility unverified; tax reading is secondary — **not tax advice**).
NEEDS ARCHITECT CONFIRMATION: YES — plus utility (confirm provider for the parcel, interconnection path > 50 kW) and a tax adviser (owner type D-007; any credit).

## R-028.3 — Rainwater harvest for field irrigation

QUESTION: How much rain can this roof yield, and what does field irrigation need, at a *scaled* (not 680,000-gal) level?

ANSWER (one paragraph): Yield = rain (in) × roof ft² × 0.62 × collection efficiency 75–90 % (S13). With Huntsville's **54.29 in/yr** normal (S12) on ~57,896 SF of roof (ASSUMED), the roof sheds roughly **1.46M–1.75M gal/yr** of collectable rain (KEYSTONE arithmetic: 57,896 × 54.29 × 0.62 × 0.75 / 0.90) — about **36,000 gal per inch of rain before efficiency losses** (57,896 × 0.62). Demand side: ACES says athletic turf needs **1–1.5 in of water per week** in the growing season, rain included (S14); 1 in on 1 acre ≈ **27,200 gal** (S15), so **each acre of turf needs roughly 27,000–41,000 gal per fully dry week**. The binding number is **storage, not roof yield**. Example only (ASSUMED): carrying **1 acre through 2 dry weeks** takes ~**55,000–82,000 gal** of storage — about one-tenth of Mercedes' 680,000-gal cistern (S21, inspiration only). Concept-sheet field pads in `params/phase2.yaml` `campus` are ~**15 ac** (football 2.5, soccer 2 × 2, baseball / softball ~8 total — irrigated turf is less, infields are dirt; TBD). At ~27,000–41,000 gal per acre per dry week, **all 15 ac would draw ~0.41M–0.61M gal per dry week** (KEYSTONE arithmetic, upper bound) — far more than a 1-in rain on the roof yields (~36,000 gal, enough for about **1 acre-week**). Reading (ASSUMED): roof rainwater is a **supplement for the show fields** (e.g. football + one soccer), not whole-campus irrigation; the rest needs well / utility water. No tank size is set (parcel D-006 OPEN). Alabama adopts IPC 2021 Chapter 13: rainwater systems need a **permit with engineering calcs** (§1301.4), roof-only collection (or approved paved surfaces), debris excluder, automatic first-flush diverter, storage-tank rules, backflow protection on any potable makeup, and signage; outdoor irrigation piping downstream of a backflow preventer is exempt from some piping rules (S16). Detention / stormwater-quality rules for the county are **TBD** (not researched here; civil engineer, D-006).

SOURCE: NOAA NCEI 1991–2020 Normals (USW00003856) — https://www.ncei.noaa.gov/access/services/data/v1?dataset=normals-annualseasonal-1991-2020&stations=USW00003856&format=csv&dataTypes=ANN-PRCP-NORMAL — retrieved 2026-10-14; Texas Manual on Rainwater Harvesting 3rd ed. — https://www.twdb.texas.gov/publications/brochures/conservation/doc/RainwaterHarvestingManual_3rdedition.pdf — retrieved 2026-10-14; ACES Athletic Turf Management — https://www.aces.edu/blog/topics/lawn-garden/athletic-turf-management/ — retrieved 2026-10-14; USGS Circ. 1268 — https://pubs.usgs.gov/circ/2004/circ1268/htdocs/text-conversion.html — retrieved 2026-10-14; Alabama Plumbing Code 2021 Ch. 13 — https://up.codes/viewer/alabama/ipc-2021/chapter/13/nonpotable-water-systems — retrieved 2026-10-14.
EDITION / SECTION: NOAA 1991–2020 normals; TWDB manual 3rd ed. (yield equation); IPC 2021 §§1301.4, 1301.5, 1303.2–1303.4, 1303.10, 1303.14 exception.
CONFIDENCE: HIGH for rainfall and the yield / acre-inch arithmetic; MEDIUM for irrigation demand (seasonal, soil-dependent); LOW for any tank size (example only — irrigated turf acreage not set).
NEEDS ARCHITECT CONFIRMATION: YES — civil / plumbing engineer sizes storage from field acreage and monthly rain (summer deficit), and confirms the county's stormwater rules.

## R-028.4 — Daylighting

QUESTION: Does code push this building toward skylights / daylighting, and what does a scaled version look like?

ANSWER (one paragraph): Probably yes, for big high spaces. Alabama's commercial code is **ASHRAE 90.1-2013** with state amendments (S17); the state's 2015 IECC text (S18) — Madison County is **Climate Zone 3A** — requires, in an enclosed space **> 2,500 ft²** directly under a roof with **≥ 75 % of the ceiling > 15 ft**, used as (among others) a **lobby, concourse, corridor, storage space or gymnasium/exercise center**, a daylight zone under skylights of **≥ half the floor area** with **skylight area ≥ 3 % of that zone** (VT ≥ 0.40) or effective aperture ≥ 1 % (IECC 2015 C402.4.2), plus **daylight-responsive controls** for lights in those zones (C402.4.2.1). Scale (KEYSTONE arithmetic): every **10,000 ft²** of qualifying space needs ≥ 5,000 ft² of toplit zone → **≥ 150 ft² of skylight**. Exceptions include spaces where the **daylight zone under rooftop monitors > 50 %** of the floor (fits a clerestory / monitor roof in the SRM-HQ look, D-074) and spaces whose sidelit zones leave < 2,500 ft² (S18). Whether the **competition bowl** counts as "gymnasium/exercise center" (the list has no "sports arena"), and whether the project uses the 90.1-2013 path (its parallel skylight clause is **paywalled — UNVERIFIED**), is the architect's call. Design caution (ASSUMED): wrestling / broadcast need glare control — diffuse glazing or monitors facing north, not clear skylights over the mats.

SOURCE: DOE Building Energy Codes Program, Alabama — https://www.energycodes.gov/status/states/alabama — retrieved 2026-10-14; Alabama Energy Code 2015 (IECC) Ch. 4 C402.4.2 / C402.4.2.1 and Table C301.1 — https://up.codes/viewer/alabama/iecc-2015/chapter/CE_4/ce-commercial-energy-efficiency — retrieved 2026-10-14.
EDITION / SECTION: IECC 2015 C402.4.2, C402.4.2.1, Table C301.1 (as hosted for Alabama); ASHRAE 90.1-2013 §5.5.4.2.3 UNVERIFIED (paywalled).
CONFIDENCE: MEDIUM (code text primary-hosted; space-type applicability to an arena bowl and compliance path not confirmed).
NEEDS ARCHITECT CONFIRMATION: YES — compliance path (90.1-2013 vs IECC 2015), which spaces qualify (lobby / concourse / storage annex / bowl), and glare criteria.

## R-028.5 — LED lighting + efficient HVAC

QUESTION: What do "LED + efficient HVAC" mean at this scale, in numbers that are actually sourced?

ANSWER (one paragraph): **LED:** DOE says LEDs use **up to 90 % less energy** than incandescent (S19); for a new arena, LED is effectively the baseline, so the scaled lever is **controls** (daylight-responsive controls in toplit zones are already code under C402.4.2.1, S18; event / practice / cleaning scenes and occupancy control — ASSUMED design intent, no % claimed). Vendor gym retrofit studies claim **50–70 %** savings vs metal halide — **LOW confidence, vendor**, not used for sizing. **HVAC:** DOE says geothermal (ground-source) heat pumps save **25–50 %** vs air-source heat pumps (S20) — the same family of system SRM's Smyrna HQ uses (D-074 reference). Unlike solar, **geothermal heat-pump property keeps a federal §48 credit path** if construction begins before **2035-01-01** (S11; that page also says "through 2032" — read as the full-rate window; **tax adviser to confirm** the rate step-down), with elective pay available to tax-exempt owners (S10). Bore-field size, wells vs open land, and cost are **TBD** (needs load calc + site geotech, D-006). Arena benchmark for any later savings claim: ENERGY STAR Indoor Arena median **56.2 kBtu/ft² site** (S9).

SOURCE: DOE Consumer Guide to Energy-Efficient Lighting — https://www.energy.gov/sites/default/files/2021-08/ES-EE%20Lighting_080921.pdf — retrieved 2026-10-14; DOE Consumer Guide to Geothermal Heat Pumps — https://www.energy.gov/sites/default/files/2021-08/ES-Geothermal%20heat%20pumps_080221.pdf — retrieved 2026-10-14; Eide Bailly OBBB §48 / §48E — https://www.eidebailly.com/insights/alerts/2025/obbb-energy-credits — retrieved 2026-10-14 (+ S9, S10, S18).
EDITION / SECTION: DOE consumer guides (Aug 2021); Eide Bailly update 2025-08-26; IECC 2015 C402.4.2.1.
CONFIDENCE: MEDIUM for the DOE ranges (consumer-level, not arena-specific); LOW for any arena-specific % (none claimed); MEDIUM-LOW for credit timing (secondary, internally inconsistent source).
NEEDS ARCHITECT CONFIRMATION: YES — MEP engineer (system selection, load calc, geotech for bore field) and tax adviser (credit, owner D-007).

## R-028.6 — Mercedes-Benz Stadium: inspiration only

QUESTION: How do the Mercedes figures relate to this project?

ANSWER (one paragraph): They are **reference only** (PARKING_LOT). Mercedes-Benz Stadium reports 4,000 PV panels producing ~1.6M kWh/yr across the stadium / GWCC campus (canopies, parking, entrances — not just roof), a 680,000-gal cistern for irrigation and cooling-tower makeup, a 1.1M-gal underground vault, a 2.1M-gal total stormwater system with bioswales, and a design 47 % water-use reduction (S21). The scaled readings in R-028.1–.5 are roughly **3–8× smaller in solar output** and about **an order of magnitude smaller in storage** for a 1-acre irrigation example. Ideas worth borrowing without its numbers: PV on **canopies / parking shade** (not only roof — relevant if the roof is curved / crowded), a single cistern serving **irrigation + any cooling makeup**, bioswales in the parking field (R-027, D-006).

SOURCE: Mercedes-Benz Stadium, Sustainability & LEED Platinum — https://www.mercedesbenzstadium.com/sustainability — retrieved 2026-10-14
EDITION / SECTION: Energy; Stormwater Management; Water Conservation sections.
CONFIDENCE: HIGH (owner's own page) — as a description of **that** stadium only.
NEEDS ARCHITECT CONFIRMATION: YES — none of these numbers go in params or on sheets.

---

## Summary — scaled order-of-magnitude table (NOT params)

| Item | Scaled range for THA | Label | Key cites |
|---|---|---|---|
| Rooftop PV size | ~160 / 260 / 380 kW-DC (LOW / MID / HIGH) | ASSUMED on cites | S1–S4 |
| PV output | ~0.2M / 0.35M / 0.5M kWh/yr | ASSUMED on S1 | S1 |
| Share of median arena energy (if all-electric) | ~15–37 % | ASSUMED | S9 |
| PV installed cost, pre-incentive | ~$0.3M–$1.2M (national band) | ASSUMED on S5 | S5 |
| Export value | HU ≤ 50 kW $0.0643/kWh; TVA DPP ~$0.034/kWh; no net metering | CITED | S6, S7 |
| Federal solar credit | Unlikely (needs service by 2027-12-31) | CITED reading, not tax advice | S10, S11 |
| Roof rain yield | ~36,000 gal per inch (before losses); ~1.46M–1.75M gal/yr | ASSUMED on cites | S12, S13 |
| Turf irrigation need | ~27,000–41,000 gal per acre per dry week | ASSUMED on cites | S14, S15 |
| Storage | TBD (example: 1 ac × 2 dry wk ≈ 55k–82k gal); roof covers ~1 acre-week per inch of rain vs ~15 ac of field pads | TBD / ASSUMED | S12–S15, phase2.yaml campus |
| Skylights (if space qualifies) | ≥ 3 % of toplit zone ≥ half floor (≈ 150 ft² per 10,000 ft²) | CITED code + arithmetic | S18 |
| LED | Baseline; controls are the lever | CITED / ASSUMED | S18, S19 |
| Geothermal HP | 25–50 % vs air-source; §48 path to 2035 start | CITED | S11, S20 |

**Area table (required):** L1 57,896 · L2 29,068 · TOTAL 86,964 GSF · Δ vs last revision **0 SF** (research only).

## What R-028 does NOT change

No sheet, generator, params file or decision changed. `params/phase2.yaml` `sustainability.rooftop_solar.size` and `stormwater_storage.size` stay **TBD**. D-018 stays DECIDED as design intent; D-006 / D-007 / D-012 stay OPEN.

## NEEDS ARCHITECT CONFIRMATION

**YES.** Before any of this is sized or drawn: (1) Shane says which items to size and to what target (e.g. kW or % of load; acres of field to irrigate); (2) architect / structural confirm usable roof and PV dead load; (3) MEP confirms load, HVAC system and controls; (4) civil confirms storage and county stormwater rules on the real parcel (D-006); (5) the parcel's utility confirms interconnection > 50 kW; (6) tax adviser confirms any credit (D-007).
