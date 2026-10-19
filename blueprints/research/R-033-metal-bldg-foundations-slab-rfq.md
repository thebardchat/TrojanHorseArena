# R-033 — Phase 1 ALTERNATE metal building: foundations + slab-on-ground for the Summertown RFQ / bid (geotech, frost depth, slab, vapor retarder, flatness, anchor rods, ready-mix order) (Phase 1, D-095)

Researched by KEYSTONE 2026-10-19 (~6:06–6:20 AM CT, daily research worker for ticket P1-T-MB2). All sources retrieved **2026-10-19**. Fills R-031.6 item 15 ("Foundations / anchor bolts … by the EOR from a geotech report"), which no earlier R-file expanded. Feeds the Summertown Metals RFQ (what the kit supplier must hand the foundation designer), the concrete / sitework bid scope, and the ready-mix order. Builds on R-006 (code edition / AHJ), R-005 (mats), R-031 (SDC C at default Site Class D; MBMA CIP §3.1) and R-032 (E10: unheated slab edge needs no insulation in CZ 3).
Status: research note, **not legal advice**, not a geotechnical or structural design by a licensed design professional. **PRELIMINARY — CONCEPTUAL DESIGN — NOT FOR CONSTRUCTION.** The engineer of record (EOR) sizes footings, slab, reinforcement and anchor embedment from a geotech report and Summertown's reactions; DCM / the building official approves.
Format follows prompt §10. Seven sub-questions; gaps and conflicts at the end. No sheets, params, generators or decisions were changed.

**Building facts used (ASSUMED, from params — not re-decided here):** 60 x 125 ft = **7,500 SF** slab, PEMB clear span (no interior columns), frame lines x 0 / 25 / 50 / 75 / 100 / 125, endwall columns y 0 / 20 / 40 / 60 → **12 main-frame column bases + 4 intermediate endwall column bases = 16** (KEYSTONE count from `building.*`). Mat room 50 x 60 = **3,000 SF**, one 42 x 42 mat (R-005). Five exits D1–D5. Site: HGHS, 14380 Hwy 231-431 N, Madison County Schools property, campus spot TBD. R-031: SDC **C** at default Site Class D (B at Site Class C). No geotech report exists for the site (R-031).

## Sources (all retrieved 2026-10-19)
- **S1** — Alabama Building Code 2021 (IBC 2021) Ch. 18: §§1803.1, 1803.2 (+ exception), 1803.3, 1803.5.8, 1803.5.11, 1803.6, 1804.6, 1806.2 / Table 1806.2, 1809.4, 1809.5, 1809.5.1 — https://up.codes/viewer/alabama/ibc-2021/chapter/18/soils-and-foundations — PRIMARY. Box copy `research_src/r033/ibc21_ch18.html` / `.txt`.
- **S2** — same code Ch. 19: §1904.2 (nonstructural concrete), §1907.1 (slab minimum + vapor retarder) — https://up.codes/viewer/alabama/ibc-2021/chapter/19/concrete — PRIMARY. Box copy `r033/ibc21_ch19.*`.
- **S3** — same code Ch. 17: §1705.3 (+ exceptions) / Table 1705.3, §1705.6 — https://up.codes/viewer/alabama/ibc-2021/chapter/17/special-inspections-and-tests — PRIMARY. Box copy `r033/ibc21_ch17.*`.
- **S4** — City of Huntsville Code of Ordinances Ch. 7 Art. IV (Ord. 21-1006, eff. 2022-01-01): §7-192(17) IRC Table R301.2(1) "Frost Line Depth … 12 inches", weathering "Moderate", air freezing index "Under 200", mean annual temp "59.4"; §7-194(30) IBC 1907.1 restated — https://library.municode.com/al/huntsville/codes/code_of_ordinances?nodeId=COOR_CH7BUBURE_ARTIVTECO_DIV11ALENCO_SS7-209--7-310RE — PRIMARY for Huntsville, **SECONDARY for HGHS** (neighboring jurisdiction; HGHS is county / DCM).
- **S5** — Madison County Building Inspection, *Building Codes* (2018 IBC / IRC / IPC / IMC, "Effective January 2021", local amendments in two resolutions) — https://www.madisoncountyal.gov/departments/inspection/building-codes — PRIMARY for the code list; the resolutions were not reachable (curl 403; same gap as R-006 / R-029 – R-032). FrostLineDepth.com, *Alabama* ("Madison County — No official local value"; "Huntsville — 12 in") — https://www.frostlinedepth.com/alabama/ — SECONDARY (aggregator).
- **S6** — ACI 302.1R-15 *Guide to Concrete Floor and Slab Construction*, Ch. 5 excerpt (§§5.2.1, 5.2.2, 5.2.3, 5.2.3.1, 5.2.3.2, 5.2.4, 5.2.9.1, 5.2.9.3, 5.2.12) — https://www.concrete.org/portals/0/files/pdf/302.1r-15_chapter5.pdf — PRIMARY (ACI guide; free ACI University excerpt). TOC from https://www.concrete.org/Portals/0/Files/PDF/Previews/302_1R-15_PREVIEW.pdf. Box copies `r033/aci302_1r15_ch5.*`, `aci302_1r15_preview.*`.
- **S7** — NRMCA *CIP 29 — Vapor Retarders Under Slabs on Grade* (2004, 2017) — https://www.nrmca.org/wp-content/uploads/2021/01/29pr.pdf — SECONDARY (ready-mix industry). Box copy `r033/nrmca_cip29.*`.
- **S8** — NRMCA *CIP 31 — Ordering Ready Mixed Concrete* (2000, 2016, 2023) — https://www.nrmca.org/wp-content/uploads/2021/01/31pr.pdf — and NRMCA / ASCC *Checklist for Ordering and Scheduling Ready Mixed Concrete* — https://www.nrmca.org/wp-content/uploads/2021/06/2Ordering-Scheduling.pdf — SECONDARY (industry; both rest on ASTM C94/C94M, not read). Box copies `r033/nrmca_cip31.*`, `nrmca_ordering_checklist.*`.
- **S9** — Obla & Lobo, "Selecting Exposure Classes and Requirements for Durability," *Concrete International*, May 2023 (NRMCA copy, restating ACI CODE-318-19(22) Tables 19.3.2.1 / 19.3.3.1, Commentary R19.3.1, and ACI SPEC-301-20 §§4.2.2.3 / 4.2.2.4(b)) — https://www.nrmca.org/wp-content/uploads/NRMCA_GuideToSelectingExposureClasses.pdf — SECONDARY (ACI 318 itself not read; paywalled). Box copy `r033/nrmca_exposure_guide.*`.
- **S10** — Conspectus, *Tech Tips: Floor Slab Flatness & Levelness* (2012, restating ACI 117-10 / ASTM E1155) — https://www.conspectusinc.com/hubfs/Conspectus%20Tech%20Tips%20A4010%20Floor%20Slab%20Flatness%20%26%20Levelness%20rev10.12.29.pdf — SECONDARY (spec consultant; ACI 117 itself paywalled). Box copy `r033/conspectus_ffl.*`.
- **S11** — The Euclid Chemical Co., *Concrete Floor Systems Design Guide* (2006, "reflects … ACI 302.1R-04"; hosted by PDH Express) — https://www.pdhexpress.com/wp-content/themes/pdhexpress/pdf-courses/concrete-floor-systems-design-guide.pdf — SECONDARY, **RULE-OF-THUMB ONLY** (admixture manufacturer; superseded ACI edition). Box copy `r033/pdh_floor_design_guide.*`.
- **S12** — MBMA, *Common Industry Practices*, 2024 Ed., §2.1.3, §3.2.2, §6.4, §6.8 — https://mbma.com/sites/default/files/documents/MBMA%20Common%20Industry%20Practices%202024%20Edition_0.pdf — PRIMARY. Box copy `research_src/r031/mbma_cip_2024.txt` (R-031's copy reused).
- **S13** — ANSI/AISC 303-22 *Code of Standard Practice for Steel Buildings and Bridges* (May 9, 2022), §7.5.1–7.5.4 — https://welovesteelconstruction.ssi-steel.com/wp-content/uploads/2024/08/Specification-AISC-303-22_Code-of-Standard-Practice-for-Steel-Buildings-and-Bridges.pdf — PRIMARY text (third-party mirror of AISC's free standard; fractions read from the PDF's mm values). Box copy `r033/aisc303_22.*`.
- **S14** — Gravolite, *Wrestling Mats Installation and Care Guide* ("The subfloor must be clean, dry, and level") — https://www.gravolite.com/brochures/1777016637_wrestling-mats-installation-and-care-guide.pdf — SECONDARY (mat maker; gives no number). Box copy `r033/gravolite_mat_guide.*`.
- **S15** — GSA 2015 Annual Meeting abstract 263-7 (marked "ABSTRACT WITHDRAWN"): Madison County "underlain by … Bangor, Monteagle, and Tuscumbia Limestones … 460 moderate to large sinkholes and 547 caves" — https://gsa.confex.com/gsa/2015AM/webprogram/Paper266503.html — SECONDARY / LOW (context flag only). The Geological Survey of Alabama sinkhole map layer (map.ogb.state.al.us … Natural_Hazards/MapServer/123) was queried: it holds 370 points, **all in Mobile / Baldwin counties**, so it says nothing about Hazel Green (box copy `r033/gsa_sinkhole_layer.json`).
- Repo context (not re-researched): R-005, R-006, R-031 (SDC C, item 15), R-032 (E10).
- Not available / not used: ACI 360R-10 (slab-on-ground design; paywalled), ACI 117-10 / ACI 318-19 / ACI 301-20 full text, ASTM C94, E1745, E1643, E1155 (paywalled; values used only as restated by S6, S7, S9, S10); Madison County's commercial amending resolution; any HGHS soil boring.

---

## R-033.1 — Is a geotechnical report required, and what must it give the EOR?

QUESTION: Does the IBC require a geotechnical investigation for this building, and what must the report deliver for a PEMB foundation and slab?

ANSWER (one paragraph): **Plan on one. It is effectively required.** IBC 1803.2 requires a geotechnical investigation, and the building official may waive it only where "satisfactory data from adjacent areas" shows it is not needed (S1). A separate trigger applies here: R-031 found **SDC C** on the default Site Class D, and §1803.5.11 requires that structures in SDC C get an investigation that evaluates slope instability, liquefaction, total and differential settlement, and surface displacement (S1). The waiver also covers 1803.5.11, so it takes existing campus soil data to avoid one. The report also sets the **site class**, and Site Class C would drop the seismic design to SDC B (R-031). Without a report the EOR must use the **presumptive bearing values** of Table 1806.2, as low as **1,500 psf** for clays and silts, which means larger footings. Madison County sits on karst limestone (S15, LOW), so the boring scope should also look for voids. **The district or DCM orders and pays for the report, and it goes in with the permit application (§1803.6).** Summertown does not provide it.
- **§1803.2 (S1):** "Geotechnical investigations shall be conducted in accordance with Sections 1803.3 through 1803.5. Exception: The building official shall be permitted to waive the requirement … where satisfactory data from adjacent areas is available that demonstrates an investigation is not necessary for any of the conditions in Sections 1803.5.1 through 1803.5.6 and Sections 1803.5.10 and 1803.5.11." §1803.3.1: scope (number / type of borings, lab program) "shall be determined by a registered design professional."
- **§1803.5.11 (S1):** "For structures assigned to Seismic Design Category C, D, E or F, a geotechnical investigation shall be conducted, and shall include an evaluation of … Slope instability. Liquefaction. Total and differential settlement. Surface displacement due to faulting or seismically induced lateral spreading or lateral flow."
- **§1803.5.8 / §1804.6 (S1):** fill more than **12 in** deep under shallow foundations needs a report with fill specs, lift thickness, density tests. Fill ≤ 12 in needs no report if compacted to **≥ 90 %** of ASTM D1557 maximum dry density, verified by special inspection (§1705.6, S3).
- **Table 1806.2 (S1), vertical foundation pressure (psf):** crystalline bedrock 12,000; sedimentary rock 4,000; sandy gravel / gravel (GW, GP) 3,000; sand / silty / clayey sand and gravel (SW, SP, SM, SC, GM, GC) 2,000; **clay, sandy clay, silty clay, clayey silt, silt, sandy silt (CL, ML, MH, CH) 1,500**. "Mud, organic silt, organic clays, peat or unprepared fill shall not be assumed to have a presumptive load-bearing capacity."
- **§1803.6 report contents (S1):** boring location plot, boring / penetration logs, soil profile, water table, "Recommendations for foundation type and design criteria, including … bearing capacity …; provisions to mitigate the effects of expansive soils; mitigation of the effects of liquefaction, differential settlement …", expected total and differential settlement.
- **What to ask the geotech for (KEYSTONE list, from S1 + S6 §5.2.2):** site class (R-031), allowable bearing pressure, footing depth, expansive-soil check (§1803.5.3), undercut / fill specs, subgrade prep and proof-rolling for the slab, a modulus of subgrade reaction for slab design (ACI 360R input; UNVERIFIED, not read), groundwater, capillary-break need (S7), and karst / void screening.

SOURCE: S1, S3, S15 — retrieved 2026-10-19; R-031 (repo).
EDITION / SECTION: IBC 2021 (Alabama) §§1803.2, 1803.3.1, 1803.5.3, 1803.5.8, 1803.5.11, 1803.6, 1804.6, 1806.2 / Table 1806.2, 1705.6. 2018 IBC (county) not re-read for these sections (UNVERIFIED wording).
CONFIDENCE: HIGH for the code text / HIGH that SDC C triggers 1803.5.11 (R-031 value) / MEDIUM that a waiver is unlikely (no campus soil data found) / LOW for the karst risk at this exact spot (withdrawn abstract; county-wide count)
NEEDS ARCHITECT CONFIRMATION: YES. Ask DCM / MCSS: is there prior HGHS boring data (waiver basis), and will they commission the geotech?

---

## R-033.2 — Frost depth and minimum footing depth (Madison County)

QUESTION: What frost depth applies to footings at HGHS, and what does the IBC require?

ANSWER (one paragraph): **IBC 1809.4 sets 12 in minimum below undisturbed ground, and 1809.5 requires footings to go below "the frost line of the locality"** (or follow ASCE 32, or bear on rock) (S1). **Madison County publishes no frost-line number** that KEYSTONE could find (S5; the county resolutions were not reachable). The nearest official value is the **City of Huntsville: 12 inches** (its IRC climatic table, which also lists weathering "Moderate", air freezing index "Under 200" and mean annual temperature 59.4 °F) (S4). **Working value for the bid: 12 in minimum to bottom of footing**, with the final depth set by the geotech / EOR (bearing stratum) and confirmed with DCM. Exterior landings at **required exits with outward-swinging doors** (D1–D5 in params) also need frost protection (§1809.5.1). Huntsville's residential rule of 2 ft below grade for perimeter footings applies only to houses in the city. It does not apply here (S4 §7-192(34)).
- **§1809.4 (S1):** "The minimum depth of footings below the undisturbed ground surface shall be 12 inches (305 mm). Where applicable, the requirements of Section 1809.5 shall be satisfied. The minimum width of footings shall be 12 inches."
- **§1809.5 (S1):** "… foundations … shall be protected from frost by one or more of the following methods: Extending below the frost line of the locality. Constructing in accordance with ASCE 32. Erecting on solid rock." The exception (RC I, ≤ 400–600 SF, eave ≤ 10 ft) does not fit a 7,500 SF RC II building. "Shallow foundations shall not bear on frozen soil …"
- **§1809.5.1 (S1):** "Frost protection shall be provided at exterior landings for all required exits with outward-swinging doors."
- **S4 (Huntsville Table R301.2(1)):** "Frost Line Depth … 12 inches"; "Weathering … Moderate"; "Air Freezing Index … Under 200"; "Mean Annual Temp … 59.4".

SOURCE: S1, S4, S5 — retrieved 2026-10-19.
EDITION / SECTION: IBC 2021 §§1809.4, 1809.5, 1809.5.1; Huntsville Ord. 21-1006 §7-192(17) (2018 IRC Table R301.2(1)).
CONFIDENCE: HIGH for the IBC rule / MEDIUM for 12 in as the local frost line (neighboring city's adopted value; county / DCM value not found)
NEEDS ARCHITECT CONFIRMATION: YES. Ask DCM: "What frost line do you use for Madison County (12 in?)".

---

## R-033.3 — Slab-on-ground: thickness, strength, reinforcement, joints

QUESTION: What do the IBC / ACI set for the slab, and what are typical ranges for a school-type floor like this (marked as rule of thumb)?

ANSWER (one paragraph): **Code minimums are low: 3½ in thick (IBC 1907.1) and 2,500 psi for an interior, F0 nonstructural slab (IBC 1904.2).** The real thickness, strength and reinforcement belong to the EOR under ACI 360R, which was not read. ACI 302.1R-15 lists what the slab documents must state (S6 §5.2.1). **Rule of thumb only:** a manufacturer guide based on the older ACI 302.1R-04 suggests **3,000 psi and 4 in minimum for Class 1–2 (foot traffic, "Offices etc.") floors**, and 3,500 psi / 5 in for Class 4 (foot plus light vehicles) (S11). NRMCA's worked example for an interior floor slab on a 10 mil vapor retarder uses **3,500 psi** (S9). NRMCA calls 3,500–5,000 psi "typical for most concrete applications" (S8). For an unreinforced slab, the same rule-of-thumb guide puts contraction joints at **2–3 times the slab thickness in feet, max 18 ft** (4 in → 8–12 ft; 5 in → 10–15 ft) (S11). ACI says to keep panels at no more than **1.5 : 1** and joints on the column lines (S6). **For the bid: carry the slab as "4 in min, 3,500 psi" (or the EOR's value) and add a 5 in alternate for any area that gets carts or lifts.** That is a KEYSTONE assumption. Thickness and reinforcement stay **TBD (EOR)**.
- **§1907.1 (S2):** "The thickness of concrete floor slabs supported directly on the ground shall be not less than 3 1/2 inches (89 mm)." **§1904.2 (S2):** nonstructural concrete "minimum specified compressive strength … 2,500 psi … for Class F0; 3,000 psi … F1; and 3,500 psi … F2 and F3."
- **S6 §5.2.1 (design items the documents must state):** "a) Slab-on-ground design criteria b) Base and subbase materials, preparation requirements, and vapor retarder/barrier … c) Concrete thickness d) Concrete compressive strength, flexural strength, or both e) … mixture proportion requirements, ultimate drying shrinkage strain … f) Joint locations and details g) Reinforcement (type, size, and location) when required … i) Surface finish j) Tolerances (base, subbase, slab thickness, and floor flatness and levelness) k) Concrete curing l) Joint filling … n) Testing requirements o) Preconstruction meeting …" "If any of this information is not provided, the contractor should request it from the slab-on-ground slab designer."
- **Joints (S6):** §5.2.9.3 "Contraction joints are usually located on column lines with intermediate joints located at equal spaces between column lines"; "aspect ratio of slab panels … should be a maximum of 1.5 to 1; however, a ratio of 1 to 1 is preferred. L- and T-shaped panels should be avoided." §5.2.9.1: isolation joints at "columns, equipment foundations, footings … drains". §5.2.12: "Deformed reinforcing bars should not be continued across contraction joints …" "It is reasonable to expect random visible cracks to occur in 0 to 3 percent of the surface area" (§5.2.9.3).
- **Reinforcement handling (S6 §5.2.4):** "Welded wire reinforcement should not be placed on the ground and pulled up after placement of the concrete." Synthetic fibers control plastic and drying shrinkage (§5.2.6). The choice of type is the EOR's.
- **Special inspection (S3 §1705.3 exceptions):** none required for "Isolated spread concrete footings of buildings three stories or less … fully supported on earth or rock" or "Nonstructural concrete slabs supported directly on the ground". The continuous-footing exception needs light-frame walls plus Table 1809.7 plus ≤ 2,500 psi, which a PEMB grade beam does not meet. **KEYSTONE reading: plan on periodic inspection of rebar and cast-in anchor rods and on cylinder / slump / air / temperature tests (Table 1705.3 items 1, 3, 5, 6) at the grade beams. Column piers / pads may be exempt.** The EOR and DCM confirm.

SOURCE: S2, S3, S6, S8, S9, S11 — retrieved 2026-10-19.
EDITION / SECTION: IBC 2021 §§1904.2, 1907.1, 1705.3 / Table 1705.3; ACI 302.1R-15 §§5.2.1, 5.2.4, 5.2.6, 5.2.9.1, 5.2.9.3, 5.2.12; ACI 302.1R-04 Table (via S11, superseded); ACI 360R (not read).
CONFIDENCE: HIGH for code minimums / LOW–MEDIUM for the typical 3,000–3,500 psi, 4–5 in ranges (secondary, rule of thumb) / MEDIUM on the special-inspection reading
NEEDS ARCHITECT CONFIRMATION: YES — the EOR sets thickness, f'c, reinforcement and joint plan (ACI 360R).

---

## R-033.4 — Vapor retarder and base under the mat-room slab (ACI 302.1R)

QUESTION: Does the slab need a vapor retarder, where does it go, and what spec, given vinyl-covered wrestling mats (and possibly a finished floor) laid on it?

ANSWER (one paragraph): **Yes. Put an ASTM E1745 vapor retarder, at least 10 mil, directly under and in contact with the slab, with laps and penetrations sealed per ASTM E1643.** The code minimum is lower: IBC 1907.1 accepts **6-mil polyethylene lapped 6 in** (S2). ACI 302.1R-15, however, says conventional 6, 8 and 10 mil polyethylene "does not fully conform to the requirements of ASTM E1745 and should not be considered for use as below-slab moisture protection" (S6). NRMCA's rule is a **minimum 10 mil, < 0.1 perm** sheet under every interior slab (S7). ACI lists **vinyl, rubber and impermeable coatings** as moisture-sensitive coverings (S6 §5.2.3). Vinyl-covered mats lying on the slab trap moisture the same way (KEYSTONE reading; the mat maker requires a "clean, dry" floor, S14). That points to ACI's direct-contact location (§5.2.3.2; the Fig. 5.2.3.2 flow chart itself was not readable). Placing concrete directly on the sheet means more curl and crusting risk and delays finishing (S6 §5.2.3.2), so the mix and the curing must account for it (R-033.7). The IBC exception ("migration of moisture … will not be detrimental") **does not fit** the mat room or the showers (KEYSTONE reading).
- **§1907.1 (S2):** "A 6-mil (0.006 inch; 0.15 mm) polyethylene vapor retarder with joints lapped not less than 6 inches (152 mm) shall be placed between the base course or subgrade and the concrete floor slab, or other approved equivalent …" Exceptions include "For buildings of other occupancies where migration of moisture through the slab from below will not be detrimental to the intended occupancy …" and "Where approved based on local site conditions."
- **S6 §5.2.3.1:** "According to ASTM E1745 a vapor retarder/barrier material is to have a permeance … not exceeding 0.1 perms … most flooring installations will benefit by using a material with a permeance level well below 0.1 perms." "The laps or seams … should be overlapped 6 in. (150 mm) (ASTM E1643) … Joints and penetrations should be sealed …"
- **S6 §5.2.3.2:** "the greatest level of protection for floor coverings, coatings, or building environments is provided when the vapor retarder/barrier is placed in direct contact with the slab." A fill layer on top of the sheet traps water from rain, saw-cutting and curing. Concrete in direct contact "shows more settlement and exhibits significantly larger length change … increased potential for a greater measure of slab curl."
- **S7 (NRMCA rules):** "1. Provide a vapor retarder directly under and in contact with all interior floor slabs. 2. Use a sheet product with a minimum thickness of 10 mils that has a permeance less than 0.1 perms … 4. Order a concrete mixture designed for low shrinkage … 5. … If the concrete slab will receive a moisture-sensitive floor covering, cure the concrete under plastic sheeting for 3 days and do not moist cure the slab for more than 7 days." Base: "compacted to provide uniform support … clean fine-graded, preferably crushed, material with about 10 to 30 percent passing the No. 100 sieve … Concrete sand should not be used." If the geotech calls for a capillary break: "6 to 8 inch … coarse gravel or crushed stone", choked with "2-in. … fine-grained compactable fill", and the retarder **still** goes on top.

SOURCE: S2, S6, S7, S14 — retrieved 2026-10-19.
EDITION / SECTION: IBC 2021 §1907.1 (+ exceptions); ACI 302.1R-15 §§5.2.3, 5.2.3.1, 5.2.3.2 (Fig. 5.2.3.2 flow chart image not readable in the text copy); ASTM E1745 / E1643 (via S6 / S7; not read).
CONFIDENCE: HIGH that a retarder is code-required here / HIGH for the ACI / NRMCA ≥ 10 mil, E1745, direct-contact recommendation / MEDIUM that loose-laid vinyl mats count as "moisture-sensitive" (KEYSTONE reading)
NEEDS ARCHITECT CONFIRMATION: YES (EOR / architect pick retarder class and location; geotech says if a capillary break is needed).

---

## R-033.5 — Floor flatness / levelness for the mat room

QUESTION: What flatness should the bid specify so the mats lie flat?

ANSWER (one paragraph): **Mat makers give no number. They require only "clean, dry, and level" and say to fix bumps with leveling compound (S14). So the slab spec has to state the tolerance in ACI 117 F-numbers.** ACI 117 classes, as restated by a spec consultant (S10): **Conventional FF 20 / FL 15** ("not suitable for applied finishes … usually left exposed"), **Moderately Flat FF 25 / FL 20** ("suitable for carpeted finishes in commercial buildings"), **Flat FF 35 / FL 25** ("thin set ceramic tile, vinyl tile"). Minimum local values default to **60 %** of the specified overall values. Measure by ASTM E1155 **within 72 hours** of placement. **KEYSTONE recommendation (rule of thumb, not a mat-maker requirement): specify Moderately Flat SOFF 25 / SOFL 20 (MLFF 15 / MLFL 12) for the mat room, the same class used under carpet. Specify Flat 35 / 25 only if a glued resilient or rubber floor goes under the mats (TBD).** Contraction joints should be filled flush so the mat seams do not telegraph them (S6 §5.2.9.3 notes that joint curl can conflict with floor coverings).
- **S10:** "Floor Surface Classification SOFF SOFL — Conventional 20 15; Moderately Flat 25 20; Flat 35 25; Very Flat 45 35; Super Flat 60 40." "ACI 117 sets the Minimum Local values at 60% of the Specified Overall values, unless specified otherwise." "F-Numbers must be measured within 72 hours of placing the slab." Straightedge alternative (10 ft, gap for 90 % / 100 % of samples): Conventional 1/2 / 3/4 in; Moderately Flat 3/8 / 5/8 in; Flat 1/4 / 3/8 in.
- **S6 §5.2.9.3:** "Floor surface curling at joints is a normal consequence of volume change … This distortion can lead to conflicts with respect to installation of some floor coverings … The designer should correlate the slab design with the requirements imposed by the floor covering specification."
- **Arithmetic (KEYSTONE):** one 42 x 42 mat on a 50 x 60 room. ACI 302.1R panels at ≤ 1.5 : 1 on 25 ft frame lines (x 0 / 25 / 50) mean joint lines run under the mat whatever the layout. Flush joint filling matters more than where the joints fall.

SOURCE: S6, S10, S14 — retrieved 2026-10-19.
EDITION / SECTION: ACI 117-10 / ASTM E1155 (via S10, secondary); ACI 302.1R-15 §5.2.9.3.
CONFIDENCE: MEDIUM–HIGH for the F-number classes (ACI 117 as restated by S10; standard not read) / LOW–MEDIUM for "Moderately Flat is enough for mats" (KEYSTONE rule of thumb; no mat-maker number found)
NEEDS ARCHITECT CONFIRMATION: YES (architect sets FF / FL; confirm the mat / finish system first).

---

## R-033.6 — Anchor rods and column reactions: what Summertown gives vs what the EOR does (MBMA / AISC)

QUESTION: How must the RFQ coordinate anchor rods, reactions and the slab with the PEMB supplier?

ANSWER (one paragraph): **Summertown designs the steel and hands over two things: the column reactions and an anchor-rod plan showing location, diameter and projection only. Everything in the concrete is by others.** That includes the foundation design, rod embedment, any **tie rods / hairpins** taking frame thrust, the rods themselves and their templates (S12 §3.2.2, §2.1.3). If the slab or rods are set wrong, **the owner (End Customer) pays for the fix**, unless the builder also poured the concrete (S12 §6.4). The bid should therefore (a) make Summertown's anchor-rod plan and reaction table a **pre-pour submittal**, (b) state the AISC 303-22 setting tolerances, and (c) require an as-built survey of the rods before the steel ships (S13 §7.5.4). With 16 column bases (KEYSTONE count), the reactions decide pad and pier sizes and whether a 60 ft clear-span frame's horizontal thrust goes into footings or into rods tied across the slab. That changes the slab design (TBD, Summertown + EOR).
- **S12 §3.2.2:** "The Manufacturer is not responsible for the design, materials or workmanship of the foundation. Anchor rod plans prepared by the Manufacturer are intended to show only location, diameter, and projection of anchor rods … The Manufacturer is responsible for providing to the Builder the loads imposed by the Metal Building System on the foundation. It is the responsibility of the End Customer to ensure that adequate provisions are made for specifying anchor rod embedment, bearing angles, tie rods, and/or other associated items embedded in the concrete foundation, as well as foundation design … This is the responsibility of the Registered Design Professional or Engineer of Record."
- **S12 §2.1.3:** "not commonly available from the Manufacturer: 1. Materials for foundations … reinforcing steel, concrete …, anchor rods, embedments, anchor rod templates, leveling plates, tie rod …" **§6.4:** "The End Customer is responsible for all additional costs resulting from errors in the concrete slab and foundation or in the setting of anchor rods, except where the concrete slab and foundation are constructed by the Builder. The Erector is responsible for ensuring that concrete dimensions and anchor rod locations are correct before setting any steel." §6.8: erection tolerances per the AISC Code of Standard Practice.
- **S13 §7.5.1:** rods set "in accordance with embedment drawings that have been approved …"; "(a) The vertical variation in location from the specified top of anchor rod location shall be equal to or less than plus or minus **1/2 in. (13 mm)**." "(b) The horizontal variation … : 3/4 and 7/8 in. rods → **1/4 in. (6 mm)**; 1, 1-1/4, 1-1/2 in. → **3/8 in. (10 mm)**; 1-3/4, 2, 2-1/2 in. → **1/2 in. (13 mm)**." §7.5.2: rods "perpendicular to the theoretical bearing surface." §7.5.4: the owner's designated representative for construction "shall conduct a survey of the as-built locations of anchor rods … and shall verify that all items … meet the corresponding tolerances."

SOURCE: S12, S13 — retrieved 2026-10-19; R-031 (MBMA §3.1 / §3.2.1).
EDITION / SECTION: MBMA CIP 2024 §§2.1.3, 3.2.2, 6.4, 6.8; ANSI/AISC 303-22 §§7.5.1–7.5.4.
CONFIDENCE: HIGH for the split of responsibility and the tolerances (primary text) / TBD for reactions, rod sizes, hairpin vs footing thrust (Summertown)
NEEDS ARCHITECT CONFIRMATION: YES (EOR designs embedment / foundations; Summertown supplies reactions).

---

## R-033.7 — RFQ / bid checklist and ready-mix order line items

QUESTION: What must the Summertown RFQ and the concrete / sitework bid state, and what goes on the ready-mix order?

ANSWER (one paragraph): **Summertown must deliver reactions and an anchor-rod plan (FD1–FD3). The concrete bid needs the geotech report, frost depth, slab design items, vapor retarder, flatness, tolerances and testing (FD4–FD12). The ready-mix order needs one mix per element (footings / grade beams, interior slab, exterior stoops), each with strength, exposure class, air, aggregate size, slump, admixtures and quantity (table below).** Order quantity: the 7,500 SF slab is **92.6 CY at 4 in or 115.7 CY at 5 in**. NRMCA's 4–10 % overage gives **96–102 CY (4 in) or 120–127 CY (5 in)**, about **9–13 truckloads (4 in) or 11–16 (5 in)** at 8–12 CY a truck (KEYSTONE arithmetic on S8 figures). Footing volume is **TBD** until reactions and bearing pressure are known.

| # | RFQ / bid item | Value / ask | Source |
|---|---|---|---|
| FD1 | Column reactions (Summertown) | Table per column base and load case: vertical, uplift, horizontal (thrust / shear), and whether the frames assume tie rods / hairpins in the slab. ~16 bases (KEYSTONE count). | S12 §3.2.2 |
| FD2 | Anchor-rod plan (Summertown) | Location, diameter, projection; base plate size; who supplies rods / templates (MBMA: usually not the manufacturer). Pre-pour submittal. | S12 §§2.1.3, 3.2.2 |
| FD3 | Base / slab-edge detail (Summertown) | Finished-floor reference and base trim / closure at the slab edge (also the R-032 air-barrier line E7). **TBD**. | S12 §3.2.2; R-032 |
| FD4 | Geotechnical report (owner) | Required (SDC C → §1803.5.11) unless waived on adjacent data. Deliverables per R-033.1 incl. site class, bearing, fill / subgrade, capillary break, karst screening. | S1 |
| FD5 | Footing depth | ≥ 12 in below undisturbed grade and below the local frost line (working value **12 in**, confirm with DCM); frost-protected landings at exits with outward-swinging doors. | S1 §§1809.4–1809.5.1; S4 |
| FD6 | Bearing pressure | From the geotech; if none, presumptive Table 1806.2 (as low as **1,500 psf** for CL / ML / MH / CH). | S1 |
| FD7 | Slab design items | All ACI 302.1R §5.2.1 items a–o on the drawings (criteria, base, thickness, f'c, mix limits, joints, reinforcement, finish, tolerances, curing, joint filler, embedments, tests, pre-con meeting). Working values: 4 in min / 3,500 psi (RULE OF THUMB), EOR to set. | S6; S9; S11 |
| FD8 | Vapor retarder | ASTM E1745, **≥ 10 mil**, < 0.1 perm, **directly under the slab**, laps 6 in sealed, penetrations sealed (ASTM E1643). Code floor: 6-mil poly (IBC 1907.1). | S2; S6; S7 |
| FD9 | Base course | Compacted, uniform, fine-graded crushed material (10–30 % passing No. 100; no concrete sand); proof-roll; capillary break 6–8 in only if geotech requires. | S6 §5.2.2; S7 |
| FD10 | Flatness | Mat room **SOFF 25 / SOFL 20** (MLFF 15 / MLFL 12), ASTM E1155 within 72 h; others per finish (RULE OF THUMB). | S10 |
| FD11 | Joints | Joint plan by EOR; contraction joints on column lines, panels ≤ 1.5 : 1, isolation at columns / footings / drains, joints filled flush in the mat room. Rule of thumb 2–3 x thickness (ft), ≤ 18 ft. | S6; S11 |
| FD12 | Inspection / testing | Periodic rebar + cast-in anchor inspection, cylinders / slump / air / temperature at grade beams (Table 1705.3 items 1, 3, 5, 6) unless the EOR / DCM rules them exempt; fill density ≥ 90 % D1557 (§1705.6); as-built anchor-rod survey. | S3; S13 §7.5.4 |

**Ready-mix order line items (one mix designation per element; values cited or TBD — EOR confirms):**

| Line | Footings / grade beams / piers | Interior slab (mat room + rest) | Exterior stoops / aprons at exits | Source |
|---|---|---|---|---|
| Specified f'c (28-day) | **TBD (EOR)**; code floor 2,500 psi at F0 | **TBD (EOR)**; code floor 2,500 (F0, nonstructural); working 3,500 psi (rule of thumb) | F1 → **3,500** / F2 → **4,500** psi (EOR picks class) | S2 §1904.2; S9; S11 |
| Exposure class | **F0** if wholly below frost line ("buried in the soil below the frost line"); exposed stem walls may be F1 / F2 | **F0, S0, W0, C0** (inside, on a vapor retarder) | **F1 or F2** (freezing with water; "if there is doubt … F2") | S9 (ACI 318 R19.3.1) |
| Max w/cm | none at F0 (structural design may set one) | none by code at F0; **TBD**: a lower w/cm dries faster for coverings (UNVERIFIED number) | 0.55 (F1) / 0.45 (F2) | S9 |
| Air content | not required at F0 | **non-air-entrained; ≤ 3 % if hard-troweled** | Target by NMSA: 3/4 in → **5.0 %** (F1) / **6.0 %** (F2); 1 in → 4.5 / 6.0 %; tolerance ±1.5 % | S9 (ACI 301 §4.2.2.4(b); ACI 318 Table 19.3.3.1); S8 |
| Nominal max aggregate | ≤ 1/5 narrowest form width and ≤ 3/4 clear bar spacing | ≤ 1/3 slab depth (4 in slab → ≤ 1-1/3 in); **3/4 or 1 in** typical | 3/4 or 1 in | S9 (ACI 301 §4.2.2.3); S8 |
| Slump | 3–5 in typical (pump / congested steel may need more) | 3–5 in typical (rule-of-thumb guide: 5 in max for Class 2) | 3–5 in | S8; S11 |
| Shrinkage / moisture | — | Ask for a **low-shrinkage** mix (direct contact with the retarder raises curl risk); reduced-moisture-emission mix if a glued floor is used | — | S7; S6 §5.2.3.2 |
| Admixtures / fibers | per producer | water reducer per producer; synthetic fibers optional (EOR) | per producer | S6 §5.2.6; S8 checklist |
| Quantity | **TBD** (reactions + bearing) | 92.6 CY @ 4 in / 115.7 CY @ 5 in, **+4–10 %** | TBD (landing sizes) | S8 (arithmetic KEYSTONE) |
| Placement / logistics | chute or pump; rate, truck spacing, start time | pump vs chute; rate / spacing; washout area | — | S8 checklist |
| Site access | A loaded truck is "about 80,000 lbs" and "may not be able to maneuver on loose dirt or over … curbs and pathways". Plan the campus haul route. | same | same | S8 CIP 31 |
| Curing | per EOR | if coverings: cure under plastic 3 days, no moist cure > 7 days | per EOR | S7 |
| Tests at discharge | cylinders, slump, air, temperature (ASTM C31 / C172) where Table 1705.3 applies | same, or per EOR if exempt | same | S3; S8 |

SOURCE: S1–S14 — retrieved 2026-10-19; R-031 item 15, R-032 E7 / E10 (repo).
EDITION / SECTION: as in R-033.1 – R-033.6; ACI 318-19(22) Tables 19.3.2.1 / 19.3.3.1 and ACI 301-20 §§4.2.2.3 / 4.2.2.4(b) via S9 (secondary).
CONFIDENCE: HIGH for the list of items / MEDIUM for exposure-class picks (EOR call; S9 examples) / LOW for the working strength / thickness (rule of thumb) / HIGH for the quantity arithmetic as stated
NEEDS ARCHITECT CONFIRMATION: YES — **EOR confirms every value before any order or bid goes out. No RFQ, bid or email was sent by KEYSTONE.**

---

## Could not verify (UNVERIFIED)
- **ACI 360R-10, ACI 117-10, ACI 318-19, ACI 301-20, ASTM C94 / E1745 / E1643 / E1155 full text** (paywalled). Values come from the ACI 302.1R-15 Ch. 5 excerpt (S6) and secondary restatements (S7–S11).
- **ACI 302.1R-15 floor class table and recommended mixture** (§4.1, §8.4): not in the free excerpt. S11's 3,000 psi / 4 in Class 2 figures come from the **superseded 2004 edition**, via a manufacturer.
- **Madison County / DCM frost depth:** no published county value found; the commercial resolution was unreachable. 12 in is Huntsville's adopted value.
- **Site soils:** no boring data; karst risk at HGHS unknown (S15 county-wide; GSA sinkhole layer covers Mobile / Baldwin only).
- **Max w/cm for moisture control** under coverings: a number exists in flooring-industry guidance (ACI 302.2R), but it was not read. Left TBD.
- **Summertown's reactions, rod sizes and whether its frames use hairpins / tie rods:** unknown until the quote.
- **2018 IBC (county) text** for §§1803 / 1809 / 1907 / 1705.3 was not re-read (Huntsville's 2018 amendment of 1907.1 matches the 2021 wording, S4).

## Conflicts / flags
- **Code vs industry on the vapor retarder:** IBC 1907.1 accepts 6-mil polyethylene. ACI 302.1R-15 says 6–10 mil polyethylene "should not be considered", and NRMCA wants ≥ 10 mil E1745. **Specify the industry level.** It costs a little more and is not a code issue.
- **Air in the interior slab:** NRMCA warns that requiring air in a troweled interior slab "can cause delamination problems". Interior slab = F0, non-air-entrained, ≤ 3 % if hard-troweled. Only the exterior stoops get air-entrained concrete. **Keep the two mixes separate on the order and on the ticket**, with distinct mix designations (S8).
- **Geotech is on the critical path twice:** it is required by SDC C (§1803.5.11), and it is the only way to drop SDC C to B (R-031) or to use bearing above the presumptive 1,500–2,000 psf. Getting it before Summertown's final price helps both.
- **Huntsville's 2 ft residential footing rule** (S4 §7-192(34)) is a city one- and two-family dwelling amendment. It does not apply to this county / DCM school building. Do not carry it into the bid.
- **Who pays for anchor-rod errors:** MBMA puts it on the End Customer unless the builder poured the concrete (S12 §6.4). Either buy the foundations from the same builder, or require the AISC 303 tolerances plus an as-built survey before steel ships.

## What changes for KEYSTONE
- **Nothing needs regenerating.** No sheet or param states a foundation or slab value today (`cost` lists "foundation" as TBD). These items go into the Summertown RFQ (FD1–FD3), the concrete / sitework bid (FD4–FD12) and the ready-mix order table. A future params rev can add a `foundation:` / `slab:` block (not made today).
- **Decision / cost / code impact:** (1) **A geotech report is a code requirement** (SDC C) unless DCM waives it, and it is an owner cost (amount TBD, no number invented). (2) **Vapor retarder ≥ 10 mil E1745 in direct contact** is an upgrade over the code's 6-mil poly; small cost. (3) **Slab ≈ 93–116 CY** before overage, which gives Shane a real ready-mix order size. Thickness, f'c and footings stay TBD (EOR). No change to D-095.
- **Add to the AHJ / DCM pre-application list:**
  1. Is there HGHS soil data that would support a §1803.2 waiver, or must MCSS commission a geotech (SDC C → §1803.5.11)?
  2. What frost line does DCM use for Madison County (12 in?)?
  3. Special-inspection program for PEMB grade beams / anchor rods (Table 1705.3) on a DCM school project.
- **Questions to add to the Summertown Metals RFQ:** FD1–FD3, plus (a) whether their frame design assumes hairpins or tie rods across the slab, (b) anchor-rod diameters (they set the AISC tolerance), and (c) whether they or the erector supply rods and templates.
