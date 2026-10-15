# R-029 — Phase 1 ALTERNATE metal building: occupancy (A-3 / A-4 / E), Type IIB, sprinkler triggers, height / area (Phase 1, D-095)

Researched by KEYSTONE 2026-10-15 (~6:15 AM CT, research worker for ticket P1-T-MB2). All sources retrieved **2026-10-15**. Feeds the code block of `params/phase1_metal_bldg_rev_b.yaml` (`code.*`) and the code notes on MetalBldg Set Rev B (P1-G-101 / A-201 / A-301 / A-901 Rev B). Builds on R-002 (DCM + MCSS approval path), R-006 (code edition / AHJ), R-007 (occupancy + occupant load factors, arena).
Status: research note, **not legal advice**, not a code analysis by a licensed design professional. **PRELIMINARY — CONCEPTUAL DESIGN — NOT FOR CONSTRUCTION.** The building official / fire code official assigns occupancy, construction type and occupant load; the architect and the PEMB engineer of record confirm.
Format follows prompt §10. Five sub-questions; gaps and conflicts at the end. No sheets, params, generators or decisions were changed.

**Building facts used (ASSUMED, from params — not re-decided here):** 60 x 125 ft = **7,500 SF**, **one story**, clear-span pre-engineered metal building (PEMB, Summertown Metals, D-095); eave 16 ft, 1:12 gable (ASSUMED); all exits D1–D5 at grade (ASSUMED). Drawn occupant load **98** (`phase1_metal_bldg_rev_b.yaml`, IBC 2021 Table 1004.5 factors: mat room 3,000 SF ÷ 50 gross = 60; girls' + boys' locker rooms 832 SF ÷ 50 = 17 each; office 286 ÷ 150 = 2; storage 143 ÷ 300 = 1; jan. / mech 143 ÷ 300 = 1; corridors, toilets and showers carried at 0 as accessory — KEYSTONE arithmetic re-run from params 2026-10-15). Sheets ASSUME IBC / IPC 2021, Group A-3, Type IIB, non-sprinklered; AHJ to confirm. Site: Hazel Green High School, Madison County Schools (public K-12); exact campus location TBD.

## Sources (all retrieved 2026-10-15)
- **S1** — Alabama Building Code 2021 (IBC 2021) Chapter 3, §§303.1–303.6, 304.1, 305.1 — https://up.codes/viewer/alabama/ibc-2021/chapter/3/occupancy-classification-and-use — PRIMARY (code text as published on UpCodes). Box copy `research_src/r029/ch3.txt`.
- **S2** — Alabama Building Code 2021 (IBC 2021) Chapter 6, Table 601, §§602.1, 602.1.1, 602.2, 603.1 — https://up.codes/viewer/alabama/ibc-2021/chapter/6/types-of-construction — PRIMARY. Box copy `research_src/r029/ch6.txt`.
- **S3** — Alabama Building Code 2021 (IBC 2021) Chapter 9, §§901.7, 903.2, 903.2.1, 903.2.1.3, 903.2.1.4, 903.2.1.7, 903.2.3, 907.2.1, 907.2.3 — https://up.codes/viewer/alabama/ibc-2021/chapter/9/fire-protection-and-life-safety-systems — PRIMARY. Box copy `research_src/r029/ch9.txt` (matches the 2026-10-09 copy used for R-007 / R-015).
- **S4** — Alabama Fire Code 2021 (IFC 2021) Chapter 9, §§903.2.1.3, 903.2.3 — https://up.codes/viewer/alabama/ifc-2021/chapter/9/fire-protection-and-life-safety-systems — PRIMARY. Box copy `research_src/r029/ifc9.txt`.
- **S5** — Alabama Building Code 2021 (IBC 2021) Chapter 5, Tables 504.3, 504.4, 506.2; §§503.1, 504.1, 506.1, 506.2, 506.2.1, 508.2.3, 508.3.1, 508.3.2 — https://up.codes/viewer/alabama/ibc-2021/chapter/5/general-building-heights-and-areas — PRIMARY. Box copy `research_src/r029/ch5.txt` (tables parsed from `ch5.html`).
- **S6** — Alabama Building Code 2021 (IBC 2021) Chapter 2 definitions ("Fire area", "Exit discharge, level of", "Height, building") — https://up.codes/viewer/alabama/ibc-2021/chapter/2/definitions — PRIMARY.
- **S7** — Alabama Building Code 2021 (IBC 2021) Chapter 26, §§2603.4, 2603.4.1.4, 2603.5–2603.5.7, 2603.9 (foam plastic in exterior walls) — https://up.codes/viewer/alabama/ibc-2021/chapter/26/plastic — PRIMARY.
- **S8** — Alabama Building Code 2021 (IBC 2021) Chapter 4, §§423.5, 423.5.1, 423.5.2 (storm shelters, Group E) — https://up.codes/viewer/alabama/ibc-2021/chapter/4/special-detailed-requirements-based-on-occupancy-and-use — PRIMARY.
- **S9** — Alabama DCM, "State Building Code" (2021 IBC adopted July 1, 2022, amended March 17, 2025 with listed 2024 sections; 2021 IFC; 2020 ICC 500; 2019 NFPA 72; jurisdiction "on all public and private kindergarten through twelfth grade (K-12) schools") — https://dcm.alabama.gov/bldg_code.aspx — PRIMARY (state).
- **S10** — Ala. Admin. Code r. 482-2-101-.02, State Fire Marshal, adoption of the 2021 IFC (Appendices B, C, D, E, M; effective Jan 1, 2025 revision) — https://admincode.legislature.state.al.us/api/filing/670000f339953c06d5abb830/filing — PRIMARY (same rule as R-006 S6).
- **S11** — 2018 IBC Chapter 9 as adopted in Texas (UpCodes, `texas/ibc-2018`), §§903.2.1.3, 903.2.3, 907.2.1, 907.2.3 — https://up.codes/viewer/texas/ibc-2018/chapter/9/fire-protection-systems — SECONDARY for Madison County (2018 model text, not Madison County's amended copy).
- **S12** — 2018 IBC Chapter 5 as adopted in Texas (UpCodes), Tables 504.3, 504.4, 506.2 — https://up.codes/viewer/texas/ibc-2018/chapter/5/general-building-heights-and-areas — SECONDARY for Madison County.
- **S13** — ICC, "2018 IBC and IFC Use of Fire Sprinklers and Alarms" (slides; §903.2.1.3 summary) — https://www.iccsafe.org/wp-content/uploads/Use-of-Fire-Sprinklers-and-Alarms.pdf — SECONDARY (ICC training material).
- **S14** — NFSA, "Fire Sprinkler Guide: 2018 IBC" (June 2020; §§903.2.1.3, 903.2.3 summaries) — https://nfsa.org/wp-content/uploads/2020/06/2020.06-NFSA-Fire-Sprinkler-Guide-2018-IBC.pdf — SECONDARY.
- Repo context (not re-researched): R-002 (DCM + MCSS), R-006 (Madison County 2018 codes; State Fire Marshal 2021 IFC), R-007 (arena = A-4; Table 1004.5 factors).
- Not available: ICC Digital Codes 2018 pages (codes.iccsafe.org) render by script and returned no text to the fetch; Madison County's 2020-09-02 amending resolution was not read (same gap as R-006).

---

## R-029.1 — Occupancy: A-3, A-4, E or mixed?

QUESTION: Is a school wrestling training room + locker building, with **no spectator seating**, Group A-3, A-4, E, or mixed?

ANSWER (one paragraph): **As drawn (practice only, no seats), the text supports A-3 or E; it does not support A-4. Which of A-3 / E is a building-official call.**
- **A-3 (S1, 303.4):** "assembly uses intended for worship, recreation or amusement and other assembly uses not classified elsewhere in Group A including … **Gymnasiums (without spectator seating)**." A wrestling practice room with no seats is the closest listed use. This is what the sheets ASSUME.
- **A-4 (S1, 303.5):** "assembly uses intended for viewing of indoor sporting events and activities **with spectator seating** including … Arenas." This is the Phase 2 arena (R-007.1). It does **not** apply to Rev B as drawn (no seats). It **would** apply if the mat room hosts meets / duals with bleachers or spectator chairs.
- **E (S1, 305.1 + 303.1.3):** Group E is use "by six or more persons at any one time for educational purposes through the 12th grade" (305.1), and **303.1.3**: "A room or space used for assembly purposes that is **associated with a Group E occupancy is not considered a separate occupancy**." Because this is a public high school's athletic building, a building official may classify it as part of the campus's Group E rather than A-3. The text does not say whether a **detached** building on the campus counts as "associated"; KEYSTONE did not find a source that settles it.
- **B — unlikely:** 304.1 puts "training and skill development **not in a school or academic program** (… martial arts studios, gymnastics …)" in B. A school team program is the opposite case. B via 303.1.1 needs an occupant load under 50; this building is 98.
- **Mixed (S5, 508):** the office (B, 286 SF), storage and jan. / mech (143 SF each) total 572 SF = **7.6 %** of the 7,500 SF story (KEYSTONE arithmetic). That is under the 10 % cap for **accessory occupancies** (508.2.3), so no separation is required (508.2.4). Locker rooms, toilets and showers are normally treated as part of the main occupancy. If the official treats them as **nonseparated** instead, "the most restrictive provisions of Chapter 9 … apply to the total nonseparated occupancy area" (508.3.1), and area / stories use the most restrictive group (508.3.2). Neither path changes the R-029.3 result below.

What each answer would change (detail in R-029.3 / .4): A-3 and E have the same sprinkler thresholds (12,000 SF / 300 occupants / level of exit discharge). E has a larger allowable area. E also brings a manual fire alarm at more than 50 occupants (907.2.3) and the storm-shelter rule (423.5). See Conflicts / flags.

SOURCE: S1, S5 — retrieved 2026-10-15. Compare R-007.1 (arena = A-4 with seats, 303.5).
EDITION / SECTION: IBC 2021 (Alabama) §§303.1.1, 303.1.3, 303.4, 303.5, 304.1, 305.1, 508.2.3, 508.2.4, 508.3.1, 508.3.2. 2018 IBC: 303.4 / 303.5 not re-read here (R-006 / R-007 gap).
CONFIDENCE: HIGH that A-4 needs spectator seating (explicit text) / MEDIUM for A-3 vs E (303.1.3 reading for a detached campus building is untested)
NEEDS ARCHITECT CONFIRMATION: YES — and **ask the AHJ / DCM in writing: A-3 or E?** Also confirm with Shane / the coaches whether the mat room will host meets with spectators. If it will, that makes it A-4, and the load factor changes (R-029.3 sensitivity).

---

## R-029.2 — Construction type: can an insulated-metal-panel PEMB be Type IIB?

QUESTION: Can a typical pre-engineered metal building with insulated metal panel (IMP) walls be classified Type IIB?

ANSWER (one paragraph): **Yes. A steel PEMB is the normal Type IIB case, if the building elements are noncombustible. With no sprinklers, a foam-core IMP wall must carry specific fire tests.**
- **Definition (S2, 602.2):** "Types I and II construction are those types of construction in which the building elements specified in Table 601 are of **noncombustible materials**, except as permitted in Section 603 and elsewhere in this code."
- **Table 601, Type IIB column (S2), in hours:**
  - Primary structural frame **0** (note c)
  - Bearing walls, exterior **0**; interior **0**
  - Nonbearing walls and partitions, interior **0**
  - Floor construction **0**
  - Roof construction **0** (note c)
  - Nonbearing exterior walls: "See Table 705.5", which sets a rating by **fire separation distance**
- **So Type IIB means noncombustible, with no fire-resistance rating on the structural frame.** A steel rigid frame with steel purlins, girts and panels fits.
- **Exterior walls still depend on the site.** The rating comes from Table 705.5 and the fire separation distance to lot lines or to other buildings on the campus. Table 705.5 was not read, and the location on campus is TBD.
- **Combustibles allowed in Types I / II (S2, 603.1) include:**
  - Fire-retardant-treated wood in nonbearing partitions, and in roof construction
  - "Thermal and acoustical insulation, other than foam plastics, having a flame spread index of not more than 25" (typical PEMB faced fiberglass blanket; product data needed)
  - "Foam plastics in accordance with Chapter 26"
  - Blocking, millwork, and interior finishes under Chapter 8
  - Interior partitions should therefore be steel stud / CMU, or FRT wood.
- **IMP foam-core flag (S7).** The one-story relief in **2603.4.1.4** (foam ≤ 4 in, behind metal facings, no thermal barrier) applies only where "the building is equipped throughout with an automatic sprinkler system in accordance with Section 903.3.1.1." **Rev B is non-sprinklered**, so that relief is not available. Type II exterior walls with foam plastic then must meet **2603.5.1–2603.5.7** (2603.5):
  - **NFPA 285** wall-assembly test (2603.5.5). Its one-story exception again points to 2603.4.1.4.
  - A **thermal barrier** (2603.4 / 2603.5.2), **or** "special approval" from large-scale tests such as NFPA 286, FM 4880, UL 1040 or UL 1715 (2603.9)
  - Potential heat (NFPA 259, 2603.5.3)
  - Flame spread ≤ 25 / smoke-developed ≤ 450 (2603.5.4)
  - Labels (2603.5.6)
  - NFPA 268 ignition (2603.5.7)
  - Many commercial IMPs publish these listings, but KEYSTONE did not check any Summertown Metals product.
  - Simpler alternative: single-skin steel panels with fiberglass insulation (603.1 FSI ≤ 25), which avoids the foam-plastic path.

SOURCE: S2, S7 — retrieved 2026-10-15.
EDITION / SECTION: IBC 2021 (Alabama) §§602.1, 602.1.1, 602.2, 603.1, Table 601; §§2603.4, 2603.4.1.4, 2603.5–2603.5.7, 2603.9. Table 705.5 NOT read.
CONFIDENCE: HIGH for the definition and Table 601 values (text read) / LOW for this building's actual type (no supplier drawings, panel spec or insulation data)
NEEDS ARCHITECT CONFIRMATION: YES. **The supplier (Summertown Metals) and the PEMB engineer of record must confirm the actual construction type**, the wall and roof panel system, and the insulation fire-test data (NFPA 285 / 2603.9 listings if foam-core IMP). The architect sets the Table 705.5 exterior-wall ratings once the campus location is fixed.

---

## R-029.3 — Sprinklers: do 7,500 SF / ~98 occupants / one story trip IBC 903.2.1.3?

QUESTION: For Group A-3, what are the 903.2.1.3 triggers, and does this building trip any of them?

ANSWER (one paragraph): **As drawn and as published, no trigger is tripped, so 903.2.1.3 does not require sprinklers.**
- **IBC 2021 903.2.1.3 (S3):** "An automatic sprinkler system shall be provided throughout stories containing Group A-3 occupancies … where one of the following conditions exists:
  1. The fire area exceeds 12,000 square feet (1115 m2).
  2. The fire area has an occupant load of 300 or more.
  3. The fire area is located on a floor other than a level of exit discharge serving such occupancies."
- The **Alabama Fire Code 2021 (IFC) 903.2.1.3 text is identical** (S4). The State Fire Marshal adopted the 2021 IFC (S10), and DCM lists it too (S9).
- "Fire area" is "the aggregate floor area enclosed and bounded by fire walls, fire barriers, exterior walls or horizontal assemblies of a building" (S6). No fire barriers are drawn, so the **whole building is one fire area of 7,500 SF**.

KEYSTONE arithmetic (params values only):

| Trigger (903.2.1.3) | Limit | Rev B (ASSUMED) | Result |
|---|---|---|---|
| 1. Fire area | > 12,000 SF trips | 7,500 SF (one fire area) | **not tripped** (4,500 SF under; 62.5 % of the limit) |
| 2. Occupant load of the fire area | ≥ 300 trips | 98 (drawn); 150 even if all 7,500 SF were counted at 50 gross | **not tripped** (202 under) |
| 3. Floor other than a level of exit discharge | any | one story at grade; exits D1–D5 discharge at grade ("the story at the point at which an exit terminates", S6) | **not tripped** |
| 903.2.1.7 Multiple fire areas sharing egress, combined load | ≥ 300 trips | one fire area, 98 | **not tripped** |

**If the official calls it E (R-029.1),** 903.2.3 uses the same three thresholds (S3 and S4: > 12,000 SF, on a floor other than the level of exit discharge, load ≥ 300). Result: also **not tripped**.

**Sensitivity — the result holds only for practice use.** If the 3,000 SF mat room is used for meets with spectators or folding chairs:
- It becomes A-4 (303.5). 903.2.1.4 has the same three thresholds.
- Its occupant load could rise to 3,000 ÷ 7 net (chairs only) ≈ **429**, or ÷ 5 net (standing) = **600** (Table 1004.5 factors per R-007.2).
- Either is **≥ 300, which trips trigger 2.**
- At 15 net (unconcentrated, tables and chairs) the room is 200 and the building about 238, so it does not trip.
- The posted occupant load (1004.9, R-007.5) would have to hold the room below 300 for every configuration.

**Related, not a sprinkler trigger:** a Group A manual fire alarm is required at an assembly occupant load of **300 or more** (907.2.1, S3), so **not required at 98 if A-3**. If the building is **E**, 907.2.3 requires a manual fire alarm system unless the load is **50 or less**, so it **is required at 98**. Emergency voice / alarm is not required at **100 or less**: 98 is **2 under** that threshold.

**2018 IBC (Madison County's edition per R-006):** the 2018 model text of 903.2.1.3 reads the same (12,000 SF / 300 / level of exit discharge; S11, S13, S14), and so do 903.2.3 and 907.2.1 / 907.2.3 (S11). Madison County's local amendments were not read.

**Owner / AHJ may still require sprinklers.** Nothing found here says Madison County Schools or DCM require sprinklers above the code. That was not researched; the yaml already notes "AHJ / Madison County Schools may require."

SOURCE: S3, S4, S6, S10, S11, S13, S14 — retrieved 2026-10-15.
EDITION / SECTION: IBC 2021 / IFC 2021 (Alabama) §§901.7, 903.2.1.3, 903.2.1.4, 903.2.1.7, 903.2.3, 907.2.1, 907.2.3; IBC 2021 Ch. 2 "fire area", "exit discharge, level of". 2018 IBC same sections via secondary sources (S11, S13, S14).
CONFIDENCE: HIGH for the 2021 text and the arithmetic / MEDIUM for 2018 (model text via another state's UpCodes copy plus ICC / NFSA guides, county amendments not read) / LOW for the inputs (the 7,500 SF, 98 occupants and use are ASSUMED)
NEEDS ARCHITECT CONFIRMATION: YES. **The fire code official (State Fire Marshal / DCM for K-12) and the building AHJ must confirm** the non-sprinklered basis, the single fire area, and the intended use (practice only vs. meets).

---

## R-029.4 — Height and area: does Type IIB A-3 non-sprinklered allow 7,500 SF, one story?

QUESTION: Rough check — does the Type IIB, A-3, non-sprinklered allowable height / stories / area hold a 7,500 SF one-story building?

ANSWER (one paragraph): **Yes, with margin. The values below were read from the Alabama IBC 2021 tables on UpCodes (S5).**

| Table (IBC 2021) | A-3, Type IIB, NS | E, Type IIB, NS (if E) | Rev B (ASSUMED) | Result |
|---|---|---|---|---|
| 504.3 height (row "A, B, E, F, M, S, U", NS) | **55 ft** | 55 ft | eave 16 ft; ridge ≈ 16 + 30 × 1/12 = 18.5 ft; building height is measured to "the average height of the highest roof surface" (S6), between those two | PASS |
| 504.4 stories above grade plane | **2** | 2 | 1 | PASS |
| 506.2 allowable area factor A_t (NS) | **9,500 SF** | 14,500 SF | 7,500 SF | PASS: 2,000 SF under (79 % of A-3); 7,000 SF under for E (52 %) |

- **Equation 5-1 (506.2.1).** For a single-occupancy one-story building, the allowable area per story is the tabular factor plus any frontage increase (506.3). The check above takes **no frontage increase**, so 9,500 SF is the floor value. Frontage increase would only add area.
- **Mixed use.** With accessory B / S spaces (R-029.1), area is based on the main occupancy (508.2.3). Nonseparated, it is based on the most restrictive group (508.3.2): A-3 IIB NS 9,500 is the lowest of A-3 / B / S-1 here.
- **Correction (text only, not a number).** The yaml string `code.allowable.text` says "9,500 SF / **1 storey** allowed". **Table 504.4 allows 2 stories** for A-3 IIB NS. The building is 1 story, so the check still passes. The parent may want to reword the note in a future revision (KEYSTONE did not change params).
- **2018 IBC cross-check (S12, Texas-adopted 2018 IBC on UpCodes):** A-3 IIB NS = 55 ft / 2 stories / 9,500 SF; E IIB NS = 2 stories / 14,500 SF. These match 2021.
- **Not applicable:** unlimited-area buildings (507.x) need sprinklers or A-4 / B / F / M / S conditions.

SOURCE: S5, S6, S12 — retrieved 2026-10-15.
EDITION / SECTION: IBC 2021 (Alabama) Tables 504.3, 504.4, 506.2; §§503.1, 504.1, 506.1, 506.2, 506.2.1, 508.2.3, 508.3.2. 2018 IBC Tables 504.3 / 504.4 / 506.2 via S12 (secondary for Madison County).
CONFIDENCE: HIGH for the tabular values (2021 tables parsed from the page's own table cells; the 2018 copy agrees) / MEDIUM for the application (height measurement and frontage not checked against a survey)
NEEDS ARCHITECT CONFIRMATION: YES. Also confirm whether the new building is **detached**. If it touches or connects to an existing HGHS building without a fire wall (503.1, 706), the area and fire-area checks must include that building, and R-029.3 / R-029.4 could flip.

---

## R-029.5 — School overlay (pointer only)

QUESTION: Which review path applies to **new construction** on a public K-12 campus?

ANSWER (one paragraph): **R-002 already covers this; not re-researched.**
- **R-002.1:** DCM reviews and inspects work on public K-12 schools at any cost and from any funding source. Its listed jurisdiction includes "any new construction". Plans must come from a design professional.
- **R-002.2:** MCSS guidelines route campus building / land improvements through the principal, MCSS Operations & Facilities, Board of Education approval, then DCM.
- **One new item from S9 (DCM "State Building Code" page):** DCM enforces the **2021 IBC** (amended 2025-03-17; the listed 2024 replacements are flammable-gas / hazardous-material / refrigerant items, none in §§303, 504, 506, 602 or 903), the **2021 IFC**, the **2020 ICC 500** storm-shelter standard and **2019 NFPA 72**. Its jurisdiction text covers work "on all public and private kindergarten through twelfth grade (K-12) schools."
- Madison County's Inspection Department enforces the **2018** IBC (R-006.2).
- **KEYSTONE does not decide which office or edition governs this school-property building**; both are listed on the sheets as open.

SOURCE: R-002 (sources retrieved 2026-10-03); R-006 (retrieved 2026-10-04); S9 — retrieved 2026-10-15.
EDITION / SECTION: DCM State Building Code page as of 2026-10-15; DCM Manual of Procedures Ch. 1 (as cited in R-002).
CONFIDENCE: MEDIUM (inherits R-002's confidence; district process not confirmed)
NEEDS ARCHITECT CONFIRMATION: YES. **NEEDS DISTRICT CONFIRMATION: YES.** MCSS Operations & Facilities (or its architect) should make the DCM project-verification call. They should also confirm whether Madison County Inspection is involved at all for a K-12 building, and therefore whether the 2018 or the 2021 edition governs.

---

## Could not verify (UNVERIFIED)
- **A-3 vs E for a detached school athletic building** (303.1.3 "associated with a Group E occupancy"). No commentary or AHJ interpretation was read. ICC Commentary is paywalled.
- **Madison County's local amendments** (resolution 2020-09-02) to the 2018 IBC / IFC Chapter 9 or 5 were not read. The 2018 values here come from the model text via S11 / S12 / S13 / S14, not the county's adopted copy.
- **ICC Digital Codes 2018 pages:** they returned no text to the fetch (script-rendered).
- **Table 705.5** (exterior wall rating by fire separation distance) was not read, and the campus location is TBD.
- **The actual PEMB type and panel / insulation fire-test listings** for Summertown Metals. No product data seen.
- **ICC 500 Figure 304.2(1):** whether Hazel Green lies in the 250 mph tornado shelter zone was **not read**. It only matters if the building is classified E (423.5).
- **Light-transmitting plastic wall panels** (the yaml's "translucent wall-panel daylight band"): IBC §2607 area / separation limits for non-sprinklered buildings were not read.
- Any **MCSS or DCM owner policy requiring sprinklers** beyond the code: not researched.

## Conflicts / flags
- **Code edition / AHJ (open, R-006 / D-008):** DCM (2021 IBC / IFC, K-12 jurisdiction, S9) vs Madison County Inspection (2018 IBC / IFC, R-006). For the questions in this file, the 2018 and 2021 numbers read the same (S11 / S12), so the edition question does not change R-029.3 or R-029.4.
- **E classification would add items the sheets do not show:**
  - A **manual fire alarm** (907.2.3: required above 50 occupants; 98 is over).
  - The **ICC 500 storm-shelter** check (423.5: Group E with an occupant load of 50 or more in the 250 mph zone; capacity counts the site per 423.5.1; new building on an existing E site per its exception; DCM adopts ICC 500 2020, S9).
  - The **IPC fixture row** may change from A-3 to E (not re-checked here).
- **Meets / spectators would flip the answer:** A-4 plus a possible load ≥ 300 trips 903.2.1.4 trigger 2 (R-029.3 sensitivity). Ask Shane / the coaches about intended use before the AHJ meeting.
- **Foam-core IMP without sprinklers:** the 2603.4.1.4 one-story relief needs sprinklers, so the wall product needs NFPA 285 plus 2603.9 (or a thermal barrier) listings. Put this in the Summertown Metals quote request.
- **Detached vs attached:** an attached or connected building without a fire wall pulls the existing school into the fire-area and allowable-area math.
- **yaml text:** `code.allowable.text` says "1 storey allowed". Table 504.4 says 2 stories for A-3 IIB NS. This is a text error only, so the conclusion stands. Params were not changed per ticket rules.

## What changes for KEYSTONE
- The Rev B code block (A-3 ASSUMED, Type IIB ASSUMED, non-sprinklered, 9,500 SF allowable, 903.2.1.3 not tripped) is **consistent with the published IBC / IFC 2021 text**, and with the 2018 model text, for **practice use with no spectators**. Nothing needs regenerating.
- Future revisions of the sheet notes could cite R-029 on each code line. Optional text fix: "2 stories allowed (Table 504.4), 1 provided."
- Questions to add to the AHJ / DCM pre-application list:
  1. A-3 or E?
  2. Single fire area / non-sprinklered accepted?
  3. Fire alarm and ICC 500 shelter if E?
  4. Which edition governs (2018 county / 2021 DCM)?
- Question to add to the Summertown Metals RFQ: Type IIB confirmation from the engineer of record; wall / roof panel and insulation fire-test data (NFPA 285, 2603.9) for a non-sprinklered building.
