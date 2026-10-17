# R-031 — Phase 1 ALTERNATE metal building: design loads for the Summertown RFQ (risk category, wind, snow, seismic, tornado) (Phase 1, D-095)

Researched by KEYSTONE 2026-10-17 (~6:05–6:30 AM CT, daily research worker for ticket P1-T-MB2). All sources retrieved **2026-10-17**. Feeds the Summertown Metals RFQ (the companion proposal asks the supplier for "the design loads, code edition, and engineered or stamped drawings") and, later, the `code.*` / structural notes of `params/phase1_metal_bldg_rev_b.yaml` (no `loads.*` block exists today). Builds on R-006 (code edition / AHJ), R-029 (A-3 / E, Type IIB, sprinklers) and R-030 (ICC 500 250 mph zone, translucent panels).
Status: research note, **not legal advice**, not a structural design or a code analysis by a licensed design professional. **PRELIMINARY — CONCEPTUAL DESIGN — NOT FOR CONSTRUCTION.** The PEMB manufacturer's engineer and the project's engineer of record (EOR) set and seal the design loads; the building official / DCM assigns occupancy.
Format follows prompt §10. Six sub-questions; gaps and conflicts at the end. No sheets, params, generators or decisions were changed.

**Building facts used (ASSUMED, from params — not re-decided here):** 60 x 125 ft = **7,500 SF**, one story, PEMB (Summertown Metals, D-095), 5 bays of 25 ft, eave 16 ft, 14 ft clear, 1:12 gable, ridge along the 125 ft length (ridge ≈ 16 + 30 / 12 = 18.5 ft, KEYSTONE arithmetic). Assumed Group A-3 (could be E, R-029.1), Type IIB, non-sprinklered, drawn occupant load **98**. Site: Hazel Green High School, 14380 Hwy 231-431 N, Hazel Green, Madison County, AL 35750; exact campus spot TBD.
**Point used for every hazard lookup:** **34.9351 N, 86.5697 W** (OSM campus centroid of HGHS, S7; the Census geocode of the street address is 34.935092, -86.571739, about 0.1 mile west, S7). The ASCE Hazard Tool reported ground elevation **783 ft NAVD 88** at this point (S4). Hazard values change slowly over a campus, but re-run at the final building spot.

## Sources (all retrieved 2026-10-17)
- **S1** — Alabama Building Code 2021 (IBC 2021) Chapter 16, §§1603.1.3–1603.1.5, 1604.3 / Table 1604.3, 1604.5 / Table 1604.5, 1604.5.1, Table 1607.1 (roofs), 1607.14.2.1, 1608.1–1608.2, 1609.3, 1609.3.1 / Table 1609.3.1, 1609.4.2–1609.4.3, Figures 1609.3(1)–(4), 1613.1, 1613.2.2, 1613.2.5 / Tables 1613.2.5(1)–(2), 1613.2.5.1 — https://up.codes/viewer/alabama/ibc-2021/chapter/16/structural-design — PRIMARY (code text as published on UpCodes). Box copies `research_src/r031/ibc21_ch16.html` / `.txt`, figures `ibc21_fig1609_3-*.jpg`, crops `crop_rcII_AL.png`, `crop_ibc21_fig1609_3-2.png`.
- **S2** — 2018 IBC Chapter 16 as adopted in Texas (same sections; 2018 numbering differs, e.g. roof live load reduction §1607.12.2, Eq. 16-26) — https://up.codes/viewer/texas/ibc-2018/chapter/16/structural-design — SECONDARY for Madison County (2018 model text, not the county's amended copy). Box copy `r031/ibc18_tx_ch16.html` / `.txt`.
- **S3** — Referenced standards, Chapter 35: Alabama IBC 2021 lists "ASCE/SEI 7—16 with Supplement 1" and "ICC 500—2020"; 2018 IBC (Texas copy) lists "ASCE/SEI 7—16" and "ICC 500—14" — https://up.codes/viewer/alabama/ibc-2021/chapter/35/referenced-standards and https://up.codes/viewer/texas/ibc-2018/chapter/35/referenced-standards — PRIMARY / SECONDARY. Box copies `r031/ibc21_ch35.txt`, `r031/ibc18_tx_ch35.txt`.
- **S4** — **ASCE Hazard Tool** ("the quick, reliable, and free way to look up key design parameters specified in ASCE standards") — https://ascehazardtool.org/ — queried 2026-10-17 ~6:17–6:30 AM CT through the public web page (headless Chrome on the box), lat 34.9351 / long -86.5697, **ASCE/SEI 7-16**, Risk Categories I, II, III, IV, Soil Class "D - Default (see Section 11.4.3)", load types Wind / Snow / Seismic; plus **ASCE/SEI 7-22** RC II and RC III (Wind / Snow / Tornado) for reference only. PRIMARY (ASCE's own map data). Box copies `r031/asce_rc{1,2,3,4}_results.txt` / `.png`, `asce_rc2_responses.json` (raw map-service replies, incl. RC II 700-yr pixel value 105.297 mph), `asce_rc2_722_*`, `asce_rc3_722*`, `asce_rc3_722t_details1.txt` (tornado table).
- **S5** — **USGS Seismic Design Web Services, ASCE 7-16** — https://earthquake.usgs.gov/ws/building-codes/asce7-16/calculate?latitude=34.9351&longitude=-86.5697&riskCategory=II&siteClass=D&title=HGHS (also riskCategory III / IV and siteClass A / B / C / E; and siteClass=D-default as called by S4) — PRIMARY (USGS is the source of the ASCE 7 seismic maps). Box copies `r031/usgs_asce716_rc*_*.json`, `usgs_asce716_rcII_Ddefault_via_ascetool` (inside `asce_rc2_responses.json`).
- **S6** — Applied Technology Council, "ATC Design Loads" notice: "Effective December 31, 2024 … the ATC Hazards by Location site will no longer be accessible. Users are encouraged to utilize the ASCE Hazard Tool" — https://www.atcouncil.org/windspeed-sp-540504796 — PRIMARY. hazards.atcouncil.org itself returns a "Website Suspended" page (box copy `r031/atc_home.html`); the old API host did not answer. **So the ATC tool named in R-030 and in IBC Figure 1609.3 note 6 ("www.atcouncil.org/windspeed") is gone; S4 is its replacement.**
- **S7** — U.S. Census Geocoder (address match "14380 US HWY 231, HAZEL GREEN, AL, 35750" → 34.935092, -86.571739) — https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=14380+Highway+231-431+N%2C+Hazel+Green%2C+AL+35750&benchmark=Public_AR_Current&format=json — and OpenStreetMap Nominatim ("Hazel Green High School, 14380, College Street …" → 34.9350542, -86.5696677) — https://nominatim.openstreetmap.org/search?q=Hazel+Green+High+School,+Alabama&format=json — PRIMARY for location only. Box copies `r031/census_geocode.json`, `r031/osm_hghs.json`.
- **S8** — MBMA, *Common Industry Practices*, 2024 Edition, §3.1 Design Responsibility and §3.2.1 (information the End Customer must supply to the Builder / Manufacturer) — https://mbma.com/sites/default/files/documents/MBMA%20Common%20Industry%20Practices%202024%20Edition_0.pdf — PRIMARY (industry practice document). Box copy `r031/mbma_cip_2024.pdf` / `.txt`.
- **S9** — FEMA, *Design Guide for New Tornado Load Requirements in ASCE 7-22* (January 2023) — https://www.fema.gov/sites/default/files/documents/fema_asce-7-22-tornado-loads-design-guide_012023.pdf — PRIMARY (federal guidance). Box copy `r031/fema_asce722_tornado_guide.pdf` / `fema_tornado.txt`.
- **S10** — QuiPermit, "Huntsville Alabama Building Permits and Code Guide" ("generally about 115 mph … Risk Category II … Huntsville area"; snow "commonly treated around 10 psf") — https://quipermit.com/cities/huntsville — SECONDARY (aggregator; **conflicts with S4 on wind, not relied on**, see flags). Northcraft Steel Buildings, "Steel Buildings in Alabama" (Huntsville / Madison County SDC C, RC II, Site Class D, from USGS) — https://www.northcraftsteel.com/steel-buildings-alabama — SECONDARY (corroboration only).
- Repo context (not re-researched): R-006 (Madison County enforces 2018 IBC; DCM / State Building Code = 2021 IBC), R-029, R-030.
- Not available / not used: ASCE 7-16 text itself (paywalled; tables 1.5-2 importance factors, 12.2-1 R values, Ch. 7 / 26–30 formulas not read); MBMA *Metal Building Systems Manual* (paywalled); Madison County's 2020-09-02 amending resolution (same gap as R-006 / R-029 / R-030); a geotechnical report for HGHS (none found).

---

## R-031.1 — Risk Category (IBC Table 1604.5)

QUESTION: What risk category applies to this building as Group A-3 with an occupant load of 98, and as Group E? Does the E "> 250" rule matter, and does being an accessory building on a school campus change it?

ANSWER (one paragraph): **Risk Category II either way.** A-3 at 98 is far under the public-assembly > 300 line, and E at 98 is under the E > 250 line. The table counts the occupants **of the building or structure**, so a detached building on the HGHS campus is judged on its own 98, not the whole school. It only moves up if it is joined to a higher-category building (shared structure, required egress or life-safety systems), or if the district **designates** it as an emergency shelter (that is Risk Category IV).
- **Table 1604.5, IBC 2021 (S1):** RC II = "Buildings and other structures except those listed in Risk Categories I, III and IV." RC III includes "Buildings and other structures whose primary occupancy is public assembly with an occupant load greater than 300"; "… containing one or more public assembly spaces, each having an occupant load greater than 300 and a cumulative occupant load of these public assembly spaces of greater than 2,500"; "Buildings and other structures containing Group E or Group I-4 occupancies or combination thereof, with an occupant load greater than 250"; "Any other occupancy with an occupant load greater than 5,000." RC IV includes "Designated earthquake, hurricane or other emergency shelters."
- **2018 IBC (S2):** same RC III public-assembly (> 300) and E lines ("Buildings and other structures containing Group E occupancies with an occupant load greater than 250"); no I-4 wording and no 2,500-cumulative line. **Same answer (RC II).**
- **§1604.5.1 (S1, S2):** "Where buildings or structures have two or more portions that are structurally separated, each portion shall be separately classified. Where a separated portion … provides required access to, required egress from or shares life safety components with another portion having a higher risk category, both portions shall be assigned to the higher risk category." A detached building with its own exits does neither (KEYSTONE reading).
- **Storm shelter tie-in (S1 §1604.5.1 exception):** "Where a storm shelter designed and constructed in accordance with ICC 500 is provided in a building … the risk category for the normal occupancy of the building shall apply unless the storm shelter is a designated emergency shelter in accordance with Table 1604.5." So an ICC 500 room (R-030 alternate) does **not** by itself push the building to RC IV.
- Table note (S1): occupancies that use gross area in Table 1004.5 may use net area for this occupant-load count. The drawn 98 already uses gross, so it can only go down.

SOURCE: S1, S2 — retrieved 2026-10-17. R-029 / R-030 for the A-3 vs E question.
EDITION / SECTION: IBC 2021 (Alabama) §1604.5, Table 1604.5 (and notes), §1604.5.1 (and exception); 2018 IBC Table 1604.5, §1604.5.1 via S2 (secondary).
CONFIDENCE: HIGH for RC II as drawn (explicit thresholds, 98 is far below both) / MEDIUM for "detached = judged alone" (KEYSTONE reading of "building or structure"; official confirms) / HIGH that a designated emergency shelter would be RC IV
NEEDS ARCHITECT CONFIRMATION: YES. Confirm the building stays **detached** (no structural tie or shared egress with the existing school) and is **not designated** as a community emergency shelter.

---

## R-031.2 — Basic design wind speed V and exposure

QUESTION: What is the basic design wind speed V for the HGHS site under ASCE 7-16 (the standard both the 2018 and 2021 IBC reference), for each candidate risk category, and what exposure category applies?

ANSWER (one paragraph): **V = 105 mph for Risk Category II** (site-specific, ASCE Hazard Tool, ASCE 7-16; Exposure C basis). For reference RC I = 97, RC III = 111, RC IV = 116 mph. Allowable-stress speed V_asd ≈ 81 mph for 105 mph (Table 1609.3.1 interpolation). Not a hurricane-prone or wind-borne debris region, no special wind region. **Exposure is TBD until the campus spot is picked:** Exposure B if suburban / wooded roughness runs at least 1,500 ft upwind in a sector (mean roof height ≤ 30 ft), otherwise Exposure C. The campus is open lawn, fields and parking, so **plan on Exposure C unless the engineer documents B for every direction.**
- **ASCE Hazard Tool, ASCE 7-16, lat 34.9351 / long -86.5697 (S4):** RC II "Wind … 105 Vmph" (raw map value 105.297, layer wind2016_700 = 700-yr MRI); RC I "97 Vmph"; RC III "111 Vmph"; RC IV "116 Vmph". Lower-MRI values returned for serviceability: **10-yr 72 mph**, 25-yr 78, 50-yr 84.5, 100-yr 90.0. Hurricane wind-borne-debris and special-wind-region layers: no feature at the point.
- **Map cross-check (S1 Figures 1609.3(1) and 1609.3(2)):** on the RC II figure north Alabama sits inland of the 110 mph contour with nearby point values 104–105 mph; on the RC III figure it sits inland of the 115 mph contour with nearby point values 111 mph. Consistent with S4. Figure note 1: "Values are nominal design 3-second gust wind speeds in miles per hour … at 33 feet (10 m) above ground for Exposure C Category." Note 5 (RC II): "approximately a 7% probability of exceedance in 50 years (… MRI = 700 Years)"; RC III: "MRI = 1700 Years".
- **§1609.3 (S1):** "The basic design wind speed, V, for use in the design of Risk Category II buildings and structures shall be obtained from Figures 1609.3(1), 1609.3(5) and 1609.3(6)." 2018 (S2): RC II from "Figures 1609.3(1) and 1609.3(5)". Both editions use the **ASCE 7-16** maps (S3: 2021 references "ASCE/SEI 7—16 with Supplement 1"; 2018 references "ASCE/SEI 7—16"). **No 2018 / 2021 difference in V.**
- **V_asd (S1, S2 Table 1609.3.1, "Linear interpolation is permitted"):** V 100 → 78, 110 → 85, 120 → 93. KEYSTONE interpolation: 105 → **81.5**; 111 → 85.8; 116 → 89.8 mph.
- **Exposure (S1 §1609.4.3, same in S2):** "Exposure B. For buildings with a mean roof height of less than or equal to 30 feet (9144 mm), Exposure B shall apply where the ground surface roughness, as defined by Surface Roughness B, prevails in the upwind direction for a distance of not less than 1,500 feet (457 m)." "Exposure C shall apply for all cases where Exposure B or D does not apply." Surface Roughness C = "Open terrain with scattered obstructions having heights generally less than 30 feet … flat open country, and grasslands." Mean roof height ≈ (16 + 18.5) / 2 ≈ 17 ft (KEYSTONE arithmetic) → the 1,500 ft rule applies.
- **Do not reuse "115 mph" (S10):** an aggregator page quotes ~115 mph RC II for Huntsville. That matches the older ASCE 7-10 inland value, not ASCE 7-16 (S4 gives 105). A quote at 115 is conservative (stronger, likely costs more); it is not the code minimum here.

SOURCE: S1, S2, S3, S4 — retrieved 2026-10-17. S10 noted as a conflict only.
EDITION / SECTION: ASCE 7-16 (via IBC 2021 §1609.3 / Figures 1609.3(1)–(4) and 2018 IBC §1609.3 / Figures 1609.3(1)–(8)); IBC 2021 / 2018 Table 1609.3.1, §1609.4.2–1609.4.3; ASCE 7-16 Ch. 26 (not read; paywalled).
CONFIDENCE: HIGH for V (site-specific ASCE data, matches the code maps) / HIGH for "not hurricane-prone / no WBD" / LOW for exposure (TBD-site; C recommended as the safe default)
NEEDS ARCHITECT CONFIRMATION: YES. The EOR / PEMB engineer re-runs S4 at the final building spot and states the exposure per direction (IBC 1603.1.4).

---

## R-031.3 — Ground snow load pg

QUESTION: What is the ground snow load pg for the site per ASCE 7-16 Figure 7.2-1 (IBC 1608.2)?

ANSWER (one paragraph): **pg = 10 psf** (ASCE Hazard Tool, ASCE 7-16, same value for RC I–IV because the 7-16 map is not risk-based). That is not over the 10 psf trigger, so IBC 1603.1.3 needs only pg on the drawings (no pf / Ce / Ct / Is / drift list). The **20 psf roof live load** (IBC Table 1607.1, ordinary pitched roof, reducible to no less than 12 psf) is a separate, higher minimum; the PEMB engineer checks both plus drift at any roof step (none drawn).
- **S4 (ASCE 7-16, RC I, II, III, IV):** "Snow … 10 lb/ft2" for all four runs; map attribute Load1 = 10, DisplaySI 0.48 kN/m².
- **§1608.1 / 1608.2 (S1, same in S2):** "Design snow loads shall be determined in accordance with Chapter 7 of ASCE 7, but the design roof load shall be not less than that determined by Section 1607." "The ground snow loads … shall be determined in accordance with ASCE 7 or Figures 1608.2(1) and 1608.2(2)." (The UpCodes copy of Figure 1608.2(1) image was not saved; S4 is the site value.)
- **§1603.1.3 (S1, S2):** "The ground snow load, pg, shall be indicated. In areas where the ground snow load, pg, exceeds 10 pounds per square foot (psf) … the following additional information shall also be provided…" — 10 does not exceed 10.
- **Roof live load (S1 Table 1607.1 and §1607.14.2.1; 2018 §1607.12.2.1 in S2):** "Ordinary flat, pitched, and curved roofs (that are not occupiable) 20" psf; reduced Lr "12 ≤ Lr ≤ 20". The reduction depends on each member's tributary area (PEMB engineer's calc).
- **ASCE 7-22 preview (S4, reference only — not adopted in Alabama):** 7-22 snow is risk-targeted: **24 psf for RC II, 28 psf for RC III** at this point. This would only matter if DCM or the county moves to the 2024 IBC before permit.

SOURCE: S1, S2, S4 — retrieved 2026-10-17.
EDITION / SECTION: ASCE 7-16 Fig. 7.2-1 (via S4); IBC 2021 §§1603.1.3, 1607.14.2.1, 1608.1, 1608.2, Table 1607.1; 2018 IBC same text, §1607.12.2.1 via S2 (secondary).
CONFIDENCE: HIGH for pg = 10 psf under ASCE 7-16 / HIGH for the 20 psf roof live load minimum / MEDIUM for "live load governs over snow" (pf formula in ASCE 7 Ch. 7 not read)
NEEDS ARCHITECT CONFIRMATION: YES (PEMB engineer states pg, Lr and any collateral load on the quote).

---

## R-031.4 — Seismic: Ss, S1, site class, Seismic Design Category

QUESTION: What are Ss and S1 at the site, and what is the likely Seismic Design Category (site class TBD)?

ANSWER (one paragraph): **Ss = 0.265 g, S1 = 0.118 g** (USGS, ASCE 7-16). With no soil report the code default is **Site Class D**, which gives **SDS = 0.281 g, SD1 = 0.186 g and SDC C** for Risk Category II (SDC B from the short-period table, **C from the 1-second table**, and the higher one governs). SDC C is the working value for the RFQ. **A geotechnical report could lower it:** Site Class C gives SDC B, Site Class B or A gives SDC A, Site Class E gives SDC D. IBC 1613.2.5.1 also lets the engineer use the short-period table alone (SDC B at Site Class D) if four conditions are met. One of them, for flexible diaphragms, is that vertical bracing elements be no more than 40 ft apart, which a 60 ft clear-span PEMB may not meet. That is the engineer's call.
- **USGS ASCE 7-16 web service (S5), lat 34.9351 / long -86.5697, Risk Category II:**

| Site Class | Fa | Fv | SMS | SM1 | SDS | SD1 | SDC (short / 1-s / governing) |
|---|---|---|---|---|---|---|---|
| A | 0.8 | 0.8 | — | — | 0.142 | 0.063 | A / A / **A** |
| B | 0.9 | 0.8 | 0.239 | 0.095 | 0.159 | 0.063 | A / A / **A** |
| C | 1.3 | 1.5 | 0.345 | 0.178 | 0.230 | 0.118 | B / B / **B** |
| **D (default)** | **1.588** | **2.363** | **0.421** | **0.280** | **0.281** | **0.186** | **B / C / C** |
| E | 2.357 | 4.2 | — | — | 0.417 | 0.331 | C / D / **D** |

  Same Ss / S1 / SDS / SD1 for every site class: Ss 0.265, S1 0.118. Also returned (Site Class D): PGA_M 0.208 g, TL 12 s, Ts **0.664 s**, T0 0.133 s. Risk Category III at Site Class D → SDC C (same as II); **Risk Category IV at Site Class D → SDC D** (S5).
- **D-default (S4 → S5):** the ASCE Hazard Tool's "D - Default (see Section 11.4.3)" call returns the same SDS 0.281 / SD1 0.186 / SDC C. Fa 1.588 is already above the 1.2 floor.
- **§1613.2.2 (S1, same in S2):** "Where the soil properties are not known in sufficient detail to determine the site class, Site Class D, subjected to the requirements of Section 1613.2.3, shall be used unless the building official or geotechnical data determines that Site Class E or F soils are present at the site." 2018 (S2): "Where Site Class D is selected as the default site class … the value of Fa shall be not less than 1.2."
- **Tables 1613.2.5(1) / (2) (S1, S2), RC I or II column:** SDS "0.167g ≤ SDS < 0.33g → B"; SD1 "0.133g ≤ SD1 < 0.20g → C". (2021 uses ≤; the UpCodes 2018 copy prints "<" at both ends, a rendering difference; same bands.)
- **§1613.2.5.1 (S1, same in S2):** "Where S1 is less than 0.75, the seismic design category is permitted to be determined from Table 1613.2.5(1) alone where all of the following apply: [Ta < 0.8 Ts in both directions; period used for drift < Ts; Eq. 12.8-2 used for Cs;] The diaphragms are rigid … or, for diaphragms permitted to be idealized as flexible …, the distances between vertical elements of the seismic force-resisting system do not exceed 40 feet." 0.8 x Ts = 0.53 s (KEYSTONE arithmetic). The PEMB engineer decides whether it applies.
- **Corroboration (S10, Northcraft):** "Huntsville (Madison County) | C" for RC II, Site Class D, from USGS. Matches.
- **What the drawings must show (S1 §1603.1.5):** risk category, Ie, Ss and S1, site class, SDS and SD1, SDC, the seismic force-resisting system(s), design base shear(s), Cs, R, and the analysis procedure.

SOURCE: S1, S2, S4, S5 — retrieved 2026-10-17. S10 corroboration only.
EDITION / SECTION: ASCE 7-16 (USGS web service; ASCE 7 Ch. 11–12 not read); IBC 2021 §§1603.1.5, 1613.1, 1613.2.2, 1613.2.5, Tables 1613.2.5(1)–(2), 1613.2.5.1; 2018 IBC same sections via S2 (secondary).
CONFIDENCE: HIGH for Ss / S1 and the per-site-class table (USGS service) / HIGH for SDC C at default Site Class D / LOW for the final SDC (site class TBD, and the 1613.2.5.1 option depends on the frame / bracing layout)
NEEDS ARCHITECT CONFIRMATION: YES. A soil boring / geotech report (needed for the foundation anyway) sets the site class; the PEMB engineer states the SDC and SFRS.

---

## R-031.5 — Tornado loads (ASCE 7-22 Chapter 32) and the R-030 shelter link

QUESTION: Do ASCE 7-22 Chapter 32 tornado loads apply under the 2018 / 2021 IBC, and how does this connect to the ICC 500 shelter question in R-030?

ANSWER (one paragraph): **No, not under the codes in force here.** Both the 2018 and 2021 IBC reference **ASCE 7-16**, which has no tornado chapter; Chapter 32 arrives with ASCE 7-22 / the **2024 IBC**, which Alabama has not adopted (R-006). Even under 7-22, tornado loads only reach **Risk Category III and IV** buildings, and the ASCE tool shows "Not Applicable to Risk Category 2" here. This building is RC II (R-031.1). The only tornado design that could apply today is **ICC 500 (250 mph)**: required only if the building is classed E and DCM says a shelter is needed (R-030.1), or if the district chooses a shelter room. It is a separate design, carried as an **optional RFQ alternate**.
- **S3:** 2021 IBC references "ASCE/SEI 7—16 with Supplement 1"; 2018 IBC references "ASCE/SEI 7—16".
- **S9 (FEMA, Jan 2023):** "With the publication of ASCE 7-22 … tornado load requirements are now considered as a minimum design load in conventional building design when buildings are located in tornado-prone areas. The new ASCE 7 tornado load provisions do not apply to storm shelters or safe rooms. The ASCE 7 tornado load requirements will be included in the 2024 International Building Code (IBC)…" and "Buildings and other structures that are classified as Risk Category III or IV and are located in the tornado-prone region … may be required to be designed … with consideration for tornado loads determined in accordance with Chapter 32 of ASCE 7."
- **S4 (ASCE 7-22, reference only):** RC II: "Tornado — Not Applicable to Risk Category 2". RC III (MRI 1,700 yr) tornado speed V_T by effective plan area: Ae 2,000 ft² → 74 mph; 10,000 → 80; 40,000 → 80; 100,000 → 91 mph (basic wind V = 113 mph for 7-22 RC III). At the 10,000,000-yr MRI the tool shows V_T 252–262 mph, the same range as the ICC 500 250 mph zone in R-030.
- **R-030.1 link:** IBC 2021 §423.5 needs an ICC 500 shelter only for Group E (≥ 50 occupants) in the 250 mph zone, with exceptions; A-3 needs none. §1604.5.1 exception (R-031.1): a shelter inside the building does not change the RC II unless it is a designated emergency shelter.

SOURCE: S1, S3, S4, S9 — retrieved 2026-10-17. R-006, R-030 (repo).
EDITION / SECTION: IBC 2021 / 2018 Ch. 35 (ASCE 7-16); ASCE 7-22 Ch. 32 via S9 (not read directly); ICC 500-2020 §304.2 via R-030; IBC 2021 §§423.5, 1604.5.1.
CONFIDENCE: HIGH that Ch. 32 is not required under IBC 2018 / 2021 / MEDIUM that it would not apply even under 7-22 (RC II per S4 and S9) / ICC 500 applicability stays as in R-030 (A-3: none; E: ask DCM)
NEEDS ARCHITECT CONFIRMATION: YES (only if the code edition changes before permit, or if a shelter is chosen).

---

## R-031.6 — RFQ checklist: design-load items Summertown's PEMB engineer must state

QUESTION: Which design-load items must Summertown's PEMB engineer state on the quote and design (letter of certification / design criteria sheet)?

ANSWER (one paragraph): **MBMA practice says the manufacturer designs only to the loads written into the order and "assumes that no such loads or conditions exist" otherwise. The RFQ must spell out every item below.** MBMA also says the manufacturer's engineer is **not** the project's engineer of record, so an EOR (architect or engineer) is still needed for the foundation, anchor bolts, the slab and anything Summertown does not supply.
- **S8 §3.2.1:** must be supplied: "2. The applicable code or standard, including the specific edition …"; "3. The applicable design loads including Live, Snow, Wind, Tornado, Seismic, Collateral and Auxiliary loads … Unless design loads or conditions are specifically set out in the Order Documents, the Manufacturer assumes that no such loads or conditions exist."; "4. All coefficients or factors (e.g., Exposure, Importance, Risk Category, etc.)"; "5. … conditions causing snow drifting, including location of adjacent structures"; "8. All serviceability criteria limiting vertical or horizontal deflection of components or gross building drift…". **S8 §3.1:** "The Manufacturer or the Manufacturer's Engineer is not the Registered Design Professional, Engineer of Record for the Construction Project…" and "it is highly recommended that the End Customer hire a Registered Design Professional or Engineer of Record (EOR)…".

**Checklist (values are cited above; anything not cited is TBD):**

| # | Item | Value to put in the RFQ | Source |
|---|---|---|---|
| 1 | Code edition | **2021 IBC (Alabama Building Code, DCM) — ASCE 7-16 w/ Supp. 1**; confirm vs Madison County 2018 IBC (ASCE 7-16). Loads below are the same under both. | R-006, S3 |
| 2 | Risk Category | **II** (A-3 or E at 98; detached; not a designated shelter) | R-031.1, S1 |
| 3 | Basic wind speed V | **105 mph** (RC II, ASCE 7-16); V_asd ≈ 81 mph | R-031.2, S4 |
| 4 | Wind exposure | **TBD-site; price Exposure C** unless B is documented for all directions | S1 §1609.4.3 |
| 5 | Enclosure / internal pressure GCpi | **TBD** (enclosed assumed; large overhead / equipment doors could change it — engineer to state) | S1 §1603.1.4 item 4 |
| 6 | Components and cladding pressures | Summertown to state zone pressures for roof / wall panels, doors and the translucent band | S1 §1603.1.4 item 5 |
| 7 | Ground snow pg | **10 psf** (state Is, Ce, Ct, pf, any drift) | R-031.3, S4 |
| 8 | Roof live load | **20 psf** (Table 1607.1), reducible per §1607.14.2.1 (12 psf min) | S1 |
| 9 | Collateral load | **TBD** — sum of lights, sprinkler-ready piping (none required, R-029), ducts, ceiling (none drawn), PV-ready (R-028, optional). Ask Summertown to state the collateral value they used. | S8 |
| 10 | Seismic | **Ss 0.265, S1 0.118, Site Class D (default, TBD by geotech), SDS 0.281, SD1 0.186, SDC C**; state Ie, SFRS, R, Cs, base shear, procedure | R-031.4, S5, S1 §1603.1.5 |
| 11 | Deflection limits | IBC Table 1604.3 at minimum: roof members not supporting a ceiling L/180 (L or S or W), L/120 (D+L); exterior walls with flexible finishes L/120 (wind); note a: metal roofing / siding total L/60, purlins supporting metal roofing L/150 (live), girts supporting metal siding L/90 (wind); wind for deflection may be 0.42 x C&C or the **10-yr wind (72 mph, S4)**. Stricter limits **TBD** where the translucent band, wall pads or doors need them (girts at the band / door jambs). Frame drift: **TBD** (owner / EOR to set; S8 item 8). | S1 Table 1604.3 + table notes, S2 (same), S4 |
| 12 | Tornado | ASCE 7-22 Ch. 32: **not applicable** (IBC 2018 / 2021; RC II) | R-031.5 |
| 13 | Translucent wall panels | Plastic (polycarbonate / FRP) or glass? If plastic: **CC1 or CC2** with test data per IBC 2606.4; panel sizes / gaps to suit Table 2607.4 at the actual FSD (≥ 10 ft required; continuous band needs FSD > 30 ft + CC1) | R-030.3 / R-030.4 |
| 14 | Storm shelter (OPTIONAL alternate) | Price separately: ICC 500-2020 tornado shelter room / wall system, **250 mph**, debris per ICC 500 Table 305.1.1, capacity TBD (≈ 60 if DCM requires it as E) | R-030.1 |
| 15 | Foundations / anchor bolts | Summertown to give column reactions; foundation design by the EOR from a geotech report (also fixes the site class in item 10) | S8 §3.1 / §3.2.2 |
| 16 | Certification | Letter of design certification sealed by a registered engineer (Alabama registration ASSUMED required — confirm), listing items 1–14 (IBC 1603.1 data must appear on the construction documents) | S1 §1603.1.3–1603.1.5, S8 §3.1 |

SOURCE: S1, S2, S3, S4, S5, S8 — retrieved 2026-10-17; R-029, R-030 (repo).
EDITION / SECTION: IBC 2021 §§1603.1.3–1603.1.5, 1604.3 / Table 1604.3 (and table notes), 1607 Table 1607.1, 1607.14.2.1; MBMA CIP 2024 §§3.1, 3.2.1, 3.2.2.
CONFIDENCE: HIGH for the list of items (code and MBMA text) / HIGH for the cited values / TBD for exposure, GCpi, collateral, drift, stricter deflection limits and site class
NEEDS ARCHITECT CONFIRMATION: YES. The EOR checks the RFQ before it goes out. **No RFQ or email was sent by KEYSTONE.**

---

## Could not verify (UNVERIFIED)
- **ASCE 7-16 text itself** (paywalled): importance factors (Table 1.5-2), the snow pf formula (Ch. 7), wind procedure (Ch. 26–30), R / Ω / Cd for PEMB frames (Table 12.2-1), and the 11.4.3 / 11.6 wording behind the tool's "D - Default". The values above come from the ASCE tool and USGS, not from reading the standard.
- **Final building spot:** every hazard value used the campus centroid. Re-run at the final spot (values should match within rounding).
- **Exposure category, enclosure classification, collateral load, frame drift:** TBD until the site, doors and MEP are set.
- **Site class / geotech:** no soil data found; SDC C rests on the default Site Class D.
- **Madison County 2018 amendments** (resolution 2020-09-02): not read. The 2018 text came from the Texas UpCodes copy.
- **IBC Figure 1608.2(1)** image was not saved; pg relies on S4 (ASCE's map service).
- **Whether DCM or the county will move to the 2024 IBC / ASCE 7-22 before permit** (it would raise pg to 24 psf at RC II): unknown.

## Conflicts / flags
- **Wind 105 vs 115 mph:** an aggregator page (S10) quotes ~115 mph RC II for Huntsville, which is the old ASCE 7-10 inland value. ASCE 7-16 (the code standard here) gives **105 mph** at the site. Quotes at 115 are conservative, not wrong. Compare quotes at the same V.
- **SDC C, not A / B:** with no soil report, default Site Class D gives SDC C. That means a real seismic check, SFRS and detailing statements, and possible nonstructural bracing. A geotech report showing Site Class C would give SDC B. **This is the one item that could change cost** (small): it argues for getting the soil boring before the final Summertown price.
- **Risk Category IV trap:** if the district wants to *designate* the building as a community emergency shelter, Table 1604.5 makes it RC IV (wind 116 mph, SDC D at Site Class D per S5). Do not use that word in the RFQ unless intended.
- **ATC tool gone:** IBC 2021 Figure 1609.3 note 6 and R-030 still point to www.atcouncil.org/windspeed, which was discontinued 2024-12-31 (S6). Use the ASCE Hazard Tool (S4) from now on. For ICC 500 Figure 304.2(1) the ASCE tool does not reproduce the ICC map. R-030's 250 mph answer still rests on DCM's county map plus the ICC figure.
- **Code edition (open, R-006 / D-008):** DCM 2021 vs Madison County 2018. **For every load in this file the two editions give the same values** (both reference ASCE 7-16). The only differences found were wording (Table 1604.5 adds I-4 and the 2,500-cumulative line in 2021) and section numbers (roof live load reduction 1607.12.2 in 2018 vs 1607.14.2 in 2021; wind figures (1)–(8) vs (1)–(12)).

## What changes for KEYSTONE
- **Nothing needs regenerating.** No sheet or param states a design load today. These values go into the Summertown RFQ, and later into a `loads:` block in a future params rev (not made today).
- **Decision / cost / code impact:** RC II, 105 mph, 10 psf and "no tornado chapter" **confirm the defaults** (ordinary PEMB design). **SDC C** (default soil) is the one finding with a code-requirement and small cost effect. It is reduced only by a geotech report. No change to D-095.
- **Add to the AHJ / DCM pre-application list:**
  1. Confirm Risk Category II for a detached 98-occupant A-3 (or E) building on the HGHS campus, and that it is not a designated emergency shelter.
  2. Confirm the code edition / ASCE 7 edition for structural loads (2021 IBC / ASCE 7-16 w/ Supp. 1 vs county 2018 IBC / ASCE 7-16).
  3. Will a geotechnical report be required (sets site class and foundation design)?
- **Questions to add to the Summertown Metals RFQ:** the 16-line checklist in R-031.6, plus (a) the collateral load value they assumed, (b) their standard frame-drift and girt-deflection criteria, and (c) whether the 105 mph / Exposure C / SDC C design changes their price vs their standard 115 mph package (if they have one).
