# R-030 — Phase 1 ALTERNATE metal building: ICC 500 storm shelter (if Group E), plumbing fixtures, translucent wall panels, exterior wall ratings (Phase 1, D-095)

Researched by KEYSTONE 2026-10-16 (~6:15 AM CT, daily research worker for ticket P1-T-MB2). All sources retrieved **2026-10-16**. Closes four items R-029 left UNVERIFIED (ICC 500 Figure 304.2(1); IPC fixture row if E; IBC §2607 translucent panels; Table 705.5). Feeds `params/phase1_metal_bldg_rev_b.yaml` (`code.*`, `fixtures.*`, `lighting`) and the code notes on MetalBldg Set Rev B (P1-G-101 / A-201 / A-301 / A-901 Rev B). Builds on R-002 (DCM + MCSS approval path), R-006 (code edition / AHJ), R-009 (fixture method, arena), R-028 (daylight trigger), R-029 (A-3 / E, Type IIB, sprinklers).
Status: research note, **not legal advice**, not a code analysis by a licensed design professional. **PRELIMINARY — CONCEPTUAL DESIGN — NOT FOR CONSTRUCTION.** The building official / DCM assigns occupancy and occupant load; the architect and the PEMB engineer of record confirm.
Format follows prompt §10. Four sub-questions; gaps and conflicts at the end. No sheets, params, generators or decisions were changed.

**Building facts used (ASSUMED, from params — not re-decided here):** 60 x 125 ft = **7,500 SF**, one story, PEMB (Summertown Metals, D-095), eave 16 ft, 14 ft clear, 1:12 gable, ridge along the 125 ft length. Assumed A-3 (R-029.1: A-3 or E is the official's call), Type IIB, non-sprinklered. Drawn occupant load **98** (KEYSTONE arithmetic re-run from params 2026-10-16, IBC 2021 Table 1004.5 factors as in the yaml): mat room 3,000 SF ÷ 50 = 60; girls' + boys' locker rooms 832 SF ÷ 50 = 16.64 → 17 each; office 286 ÷ 150 = 1.91 → 2; storage 143 ÷ 300 → 1; jan. / mech 143 ÷ 300 → 1; corridors / toilets / showers 0 (accessory). Fixtures drawn (yaml `fixtures.provided`): women's RR 2 WC + 2 lav; men's RR 1 WC + 1 urinal + 1 lav; girls' team 1 WC + 1 lav + 4 showers; boys' team 1 WC + 1 lav + 4 showers; 2 drinking fountains; 1 service sink. `lighting`: "translucent wall-panel daylight band above 12 ft (ASSUMED)"; no roof skylights in params. Site: Hazel Green High School, 14380 Hwy 231-431 N (Madison County Schools); exact campus location TBD.

## Sources (all retrieved 2026-10-16)
- **S1** — Alabama Building Code 2021 (IBC 2021) Chapter 4, §§423.1–423.5.2 (storm shelters) — https://up.codes/viewer/alabama/ibc-2021/chapter/4/special-detailed-requirements-based-on-occupancy-and-use — PRIMARY (code text as published on UpCodes). Box copy `research_src/r030/ibc21_ch4.txt`.
- **S2** — Alabama Storm Shelter Code 2020 (ICC 500-2020) Chapter 3, §304.2, **Figure 304.2(1)** "Design wind speeds, V_T, for tornadoes", Table 305.1.1 — https://up.codes/viewer/alabama/icc-500-2020/chapter/3/structural-design-and-testing-criteria — PRIMARY (figure image is low resolution, 666 x 432 px). Box copies `r030/icc500_2020_ch3.html`, `r030/icc500_fig304-2-1.jpg`, crop `r030/fig_crop_AL.png`.
- **S3** — Alabama DCM **Bulletin #23-01** (Nov 21, 2022), "Updated guidance on mandatory tornado storm shelters … in public and private K-12 schools required by the International Building Code", with **Attachment A** "State map with counties showing approximate tornado wind speed zones (refer to ICC 500, Figure 304.2(1) for official map)" — https://dcm.alabama.gov/PDF/bulletins/11-21-22_Bulletin23-01_all_K-12_Storm_Shelters_per_IBC.pdf — PRIMARY (state guidance). Box copies `r030/dcm_bul23-01.pdf` / `.txt`, map page `r030/dcm_bul23-01_attA_tornado_map.png`.
- **S4** — Alabama DCM **Bulletin #23-02** (Nov 22, 2022), tornado storm shelters for public K-12 schools subject to Act 2010-746 — https://dcm.alabama.gov/PDF/bulletins/11-22-22_Bulletin23-02_Public_K-12_Storm_Shelters_per_Act_2010-746.pdf — PRIMARY. Box copy `r030/dcm_bul23-02.pdf` / `.txt`.
- **S5** — Alabama DCM Bulletins index (23-01 and 23-02 listed as current; older storm-shelter bulletins superseded) — https://dcm.alabama.gov/bulletins.aspx — PRIMARY.
- **S6** — Alabama DCM "State Building Code" page (2021 IPC adopted July 1, 2022; 2020 ICC/NSSA 500; 2010 ADA Standards supersede IBC / A117.1 accessibility; jurisdiction "all public and private … K-12 schools") — https://dcm.alabama.gov/bldg_code.aspx — PRIMARY. Box copy `r030/dcm_bldg_code.txt`.
- **S7** — Alabama Plumbing Code 2021 (IPC 2021) Chapter 4, Table 403.1, §§403.1, 403.1.1, 403.2, 403.5, 403.6, 410.2, 410.3.1, 410.4, 424.2 — https://up.codes/viewer/alabama/ipc-2021/chapter/4/fixtures-faucets-and-fixture-fittings — PRIMARY. Box copy `r030/ipc21_ch4.txt`.
- **S8** — Alabama Building Code 2021 (IBC 2021) Chapter 29, Table 2902.1, §2902.1.1 — https://up.codes/viewer/alabama/ibc-2021/chapter/29/plumbing-systems — PRIMARY. Box copy `r030/ibc21_ch29.txt`.
- **S9** — Alabama Building Code 2021 (IBC 2021) Chapter 26, §§2606.4, 2607.1–2607.6, Table 2607.4, 2610.4–2610.7 — https://up.codes/viewer/alabama/ibc-2021/chapter/26/plastic — PRIMARY. Box copy `r030/ibc21_ch26.txt`.
- **S10** — Alabama Building Code 2021 (IBC 2021) Chapter 7, §705.5, Table 705.5, §705.8, Table 705.8, §705.8.1 — https://up.codes/viewer/alabama/ibc-2021/chapter/7/fire-and-smoke-protection-features — PRIMARY. Box copy `r030/ibc21_ch7.txt`.
- **S11** — 2018 IBC Chapter 4 as adopted in Texas, §§423.3–423.4.2 — https://up.codes/viewer/texas/ibc-2018/chapter/4/special-detailed-requirements-based-on-occupancy-and-use — SECONDARY for Madison County (2018 model text, not the county's amended copy). Cross-checked against the Georgia-adopted copy (https://up.codes/viewer/georgia/ibc-2018/chapter/4/special-detailed-requirements-based-on-occupancy-and-use): same §423.4 text.
- **S12** — 2018 IBC Chapter 29 as adopted in Texas, Table 2902.1 — https://up.codes/viewer/texas/ibc-2018/chapter/29/plumbing-systems — SECONDARY.
- **S13** — 2018 IPC as adopted in Georgia, Table 403.1, §§403.1.1, 410.2, 424.2 — https://up.codes/viewer/georgia/ipc-2018/chapter/4/fixtures-faucets-and-fixture-fittings — SECONDARY (carries Georgia amendments, e.g. 410.2 "25 or fewer").
- **S14** — 2018 IBC as adopted in Texas, Chapter 26 Table 2607.4 and Chapter 6 **Table 602** (2018 location of the exterior-wall rating table) — https://up.codes/viewer/texas/ibc-2018/chapter/26/plastic and https://up.codes/viewer/texas/ibc-2018/chapter/6/types-of-construction — SECONDARY.
- **S15** — Dale McKinley Construction, "Storm Safe Rooms" (north Alabama contractor page: "North Alabama is in the 250 mph zone") — https://www.dalemckinleyconstruction.com/safe-rooms — SECONDARY (marketing; corroboration only, not relied on).
- Repo context (not re-researched): R-002, R-006 (Madison County enforces 2018 IBC / IPC), R-009 (fixture method), R-028.3 (IECC 2015 C402.4.2 skylight trigger), R-029.
- Not available / not used: ATC Hazards by Location (the site-specific tool named in Figure 304.2(1) note 3) was not queried; ICC Digital Codes (script-rendered); Alabama Act 2010-746 itself was not read (only DCM's bulletin about it); Madison County's 2020-09-02 amending resolution (same gap as R-006 / R-029).

---

## R-030.1 — Storm shelter: 250 mph zone? Required if Group E?

QUESTION: Is Hazel Green / Madison County in the ICC 500 Figure 304.2(1) 250 mph tornado zone, and if the building were Group E (load 98), would IBC 423.5 require a storm shelter for a new detached building on the existing HGHS campus?

ANSWER (one paragraph): **Yes, Madison County is in the 250 mph zone. As A-3 (the sheets' assumption) §423.5 does not apply. If the official calls it E, the IBC text points to a shelter for at least the new building's required capacity, unless existing campus shelters cover it (needs the building official's approval) or the building itself meets ICC 500. DCM's own threshold method may give a different answer (no classrooms).**
- **Zone (S2, S3):** ICC 500 §304.2: "For tornado shelters, the design wind speed, V_T, shall be in accordance with Figure 304.2(1)." The figure's legend has 130 / 160 / 200 / 250 mph zones. On the UpCodes image (S2) the darkest (250 mph) zone covers north Alabama; the 200 / 250 boundary runs near Montgomery. DCM's county map (S3, Attachment A) draws the 250 / 200 line from about Choctaw / Clarke counties to Randolph County; **Madison County is well north of it, in the 250 mph zone.** DCM: "The map is provided as a guide and the design professional must use their professional judgement." S15 (contractor, secondary) says the same.
- **IBC 2021 §423.5 (S1):** "In areas where the shelter design wind speed for tornados is 250 mph in accordance with Figure 304.2(1) of ICC 500, all Group E occupancies with an occupant load of 50 or more shall have a storm shelter constructed in accordance with ICC 500." Exceptions: Group E day care; Group E accessory to places of religious worship; "Buildings meeting the requirements for shelter design in ICC 500."
- **§423.5.1 Required occupant capacity (S1):** "shall include all of the buildings on the site and shall be the greater of": (1) "The total occupant load of the classrooms, vocational rooms and offices in the Group E occupancy"; (2) "The occupant load of the largest indoor assembly space that is associated with the Group E occupancy." Exceptions: (1) a new building on an existing Group E site that "is not of sufficient size to accommodate the required occupant capacity … for all of the buildings on the site" — the shelter "shall at a minimum accommodate the required occupant capacity for the new building"; (2) "Where approved by the building official, the required occupant capacity of the shelter shall be permitted to be reduced by the occupant capacity of any existing storm shelters on the site."
- **§423.5.2 Location (S1):** within the buildings served, or "the maximum distance of travel from not fewer than one exterior door of each building to a door of the shelter serving that building does not exceed 1,000 feet."
- **A-3 case:** §423 requires shelters only for Group E (423.5) and critical emergency operations (423.4). **No shelter is required for A-3** (other shelters are optional, 423.2).

KEYSTONE arithmetic (params values only; IF the building is Group E):

| Item | Value | Basis |
|---|---|---|
| 423.5 threshold | 98 ≥ 50 → **tripped** (48 over) | drawn load 98 |
| 423.5.1 (1) classrooms / vocational / offices in the new building | office 2 (286 ÷ 150); 0 classroom / vocational SF in params | yaml rooms |
| 423.5.1 (2) largest indoor assembly space | mat room **60** (3,000 ÷ 50) | yaml |
| New-building minimum (exception 1) | greater of 2 and 60 = **60 occupants** | KEYSTONE reading; official decides |
| Reduction by existing HGHS shelters (exception 2) | **TBD** — existing campus shelter capacity unknown | needs MCSS / DCM records |
| Distance to shelter (423.5.2) | **TBD** — campus location TBD | ≤ 1,000 ft travel |

**DCM reading (S3, Bulletin 23-01):** DCM says the threshold occupant load "shall be determined as 30 square feet per occupant plus 10%" of "gross classroom area", and "For a new Group E occupancy, the minimum occupant load shall be based on the classroom area included in the new addition." It adds: "Auxiliary support areas such as cafeterias, band practice rooms, etc. are not required to be included as general classroom instruction area." Rev B has **0 SF of classroom area** in params, so under this method the threshold count would be 0 (below 50). The same bulletin also says "the new addition or stand-alone building shall be required to accommodate the occupant load of any space added to the existing E occupancy site" and points back to 423.5.1. **These two readings conflict for a building with no classrooms. KEYSTONE does not resolve it; DCM must.**
- DCM also notes it "views the adoption of the International Building Code as being applicable to building construction that occurs subsequent to its adoption and is not intended to address or correct pre-existing building conditions" (S3).
- Bulletin 23-02 (S4, Act 2010-746) covers "each new public school"; item 12 recommends shelters be "accessible from areas that are likely to be used outside of school hours, such as band practice rooms, field houses, gymnasiums and similar areas." This is guidance, not a requirement for this building. Whether the Act reaches a new detached building on an existing campus was not verified (Act not read).

**2018 IBC (Madison County edition per R-006), §423.4 (S11):** same trigger text (250 mph, Group E, load ≥ 50, same three exceptions). Differences found: 423.4.1 item 2 reads "the occupant load of **any** indoor assembly space" (2021: "the **largest**"), and exception 2 says "**code official**" (2021: "building official"). Same new-building exception, same 1,000 ft location rule (423.4.2). For Rev B (one assembly space, the mat room) the result is the same.

SOURCE: S1, S2, S3, S4, S5, S11 — retrieved 2026-10-16. S15 corroboration only.
EDITION / SECTION: IBC 2021 (Alabama) §§423.1, 423.2, 423.4, 423.5, 423.5.1, 423.5.2; ICC 500-2020 (Alabama) §304.2, Figure 304.2(1); DCM Bulletins 23-01 and 23-02 (Nov 2022); 2018 IBC §§423.3, 423.4, 423.4.1, 423.4.2 via S11 (secondary).
CONFIDENCE: HIGH that Madison County is in the 250 mph zone (DCM county map + ICC figure agree; design professional confirms) / HIGH that A-3 triggers no shelter (explicit text) / MEDIUM for the Group E reading (60-occupant minimum is KEYSTONE's reading of 423.5.1 exception 1) / LOW on whether DCM would require a shelter at all for a no-classroom athletic building (its bulletin's method conflicts with the IBC text) / TBD existing campus shelter capacity
NEEDS ARCHITECT CONFIRMATION: YES — and **ask DCM in writing** (see AHJ list): if classified E, is an ICC 500 shelter required for this building, at what capacity, and can existing HGHS shelters be counted?

---

## R-030.2 — Plumbing fixtures: required (A-3 vs E) vs drawn

QUESTION: For the 98-occupant load, what minimum fixtures does the Alabama plumbing code require under the A-3 (gymnasium) row and under the E row, and do the drawn fixtures meet them?

ANSWER (one paragraph): **The drawn fixtures meet or exceed every candidate row (A-3 gymnasium, E, and the arena row the yaml uses). Showers are not required by the table for A-3 or E; the 8 drawn showers are program, not code.**
- **Which table:** the IPC Table **403.1** and IBC Table **2902.1** (S7, S8) have identical assembly / educational rows as published. DCM adopts the 2021 IPC (S6). The IBC table number is 2902.1; the IPC number is 403.1. (The yaml cites "IPC 2021 Table 2902.1" and "IPC 2902.1.1"; the IPC numbers are 403.1 / 403.1.1. Citation text only.)
- **Which row:** UpCodes' table shows a "Classification" (Assembly / Educational …) and "Description" column; the A-1 … A-5 sub-column did not render, so rows are matched by description. **"Auditoriums without permanent seating, … arcades and gymnasiums"**: WC 1 per 125 M / 1 per 65 F; lav 1 per 200; showers "—"; DF 1 per 500; other "1 service sink". The word "gymnasiums" matches IBC 303.4 "Gymnasiums (without spectator seating)" (R-029.1). **"Educational facilities"**: WC 1 per 50 (M and F); lav 1 per 50; showers "—"; DF 1 per 100; 1 service sink. The yaml `fixtures.ratios` (75 / 40 / 200 / 150 / DF 1,000) are the **"Coliseums, arenas, skating rinks, pools and tennis courts for indoor sporting events and activities"** row (the R-009 arena row, IBC 303.5 A-4 wording), not the gymnasium row.
- **Sex split (S7 §403.1.1; S8 §2902.1.1):** "To determine the occupant load of each sex, the total occupant load shall be divided in half." Fractions round up. Exceptions: approved statistical data; all-gender multiple-user facilities (count 100 % of the load); single-user rooms (403.1.2). **So 98 → 49 M / 49 F is code, not an assumption.**
- **Drinking fountains (S7):** 410.3.1 "Not fewer than two drinking fountains shall be provided" — one wheelchair, one standing — or one dual-spout unit (exception). 410.2: none required at a load of 15 or fewer. 410.4: water dispensers may replace up to 50 % only "where three or more drinking fountains are required."
- **Urinals (S7, 424.2):** in each toilet room, urinals may replace up to 67 % of the required WCs in assembly and educational occupancies.
- **Service sink (S7, 403.6):** "Service sinks shall be located on an accessible route."

KEYSTONE arithmetic (49 M / 49 F; ceil = round up):

| Fixture | A-3 gymnasium row | E row | Arena row (yaml ratios) | Drawn (yaml) | Result |
|---|---|---|---|---|---|
| WC male | 49/125 = 0.39 → **1** | 49/50 = 0.98 → **1** | 49/75 = 0.65 → **1** | men's 1 + boys' team 1 = **2** (+1 urinal) | PASS all |
| WC female | 49/65 = 0.75 → **1** | 49/50 = 0.98 → **1** | 49/40 = 1.23 → **2** | women's 2 + girls' team 1 = **3** | PASS all |
| Lav male | 49/200 → **1** | 49/50 → **1** | 49/200 → **1** | 1 + 1 = **2** | PASS all |
| Lav female | 49/200 → **1** | 49/50 → **1** | 49/150 → **1** | 2 + 1 = **3** | PASS all |
| Showers | — (none) | — (none) | — (none) | **8** (4 + 4) | not code-required |
| Drinking fountains | 98/500 → 1 (per sex: 1 + 1); **2 by 410.3.1** (or 1 dual-spout) | 98/100 = 0.98 → 1 (per sex: 1 + 1); **2 by 410.3.1** | 98/1,000 → 1; **2 by 410.3.1** | **2** | PASS all |
| Service sink | **1** | **1** | **1** | **1** (jan. / mech) | PASS |

- **E sensitivity:** the E drinking-fountain ratio is 1 per 100; at load 98 the total-load count is 1 (2 under the next step). 410.3.1 already sets 2, which are drawn.
- **Mixed-occupancy check:** counting the office (2 occupants) under the Business row and summing fractions (403.1.1) does not change any count (e.g. WC female 48/65 + 1/40 = 0.76 → 1).
- **Team toilets:** the girls' and boys' team WC / lav rooms open to both the locker room and the corridor (D-095), so counting them toward the building total is reasonable; the building passes on the women's / men's restrooms alone under the A-3 and E rows (F 2 / M 1 WC vs 1 / 1 required). Under the arena row, female WC 2 required = 2 in the women's room alone.

**2018 (Madison County, R-006):** the 2018 IBC Table 2902.1 (S12, Texas copy) and 2018 IPC Table 403.1 (S13, Georgia copy) show the same gymnasium, educational and arena rows, the same 50 / 50 rule and the same 67 % urinal rule. The 2018 403.1.1 has only the statistical-data exception (no all-gender exception). Results unchanged.

SOURCE: S6, S7, S8, S12, S13 — retrieved 2026-10-16. R-009 for the arena-row method.
EDITION / SECTION: IPC 2021 (Alabama) Table 403.1, §§403.1, 403.1.1, 403.1.2, 403.2, 403.6, 410.2, 410.3.1, 410.4, 424.2; IBC 2021 Table 2902.1, §2902.1.1; 2018 IBC Table 2902.1 and 2018 IPC Table 403.1 via S12 / S13 (secondary).
CONFIDENCE: HIGH for the table ratios, the 50 / 50 rule and the arithmetic / MEDIUM for row selection (the A-sub-column did not render; matched by description; official picks A-3 vs E) / LOW for the inputs (load 98 and use ASSUMED)
NEEDS ARCHITECT CONFIRMATION: YES. The plumbing official confirms the row. Accessibility of the fixtures follows the 2010 ADA Standards per DCM (S6); not re-checked here.

---

## R-030.3 — Translucent wall-panel daylight band (IBC §2607); skylights (§2610)

QUESTION: For a non-sprinklered Type IIB building (A-3 or E), what does IBC §2607 allow for light-transmitting plastic wall panels, and does the yaml's "translucent wall-panel daylight band above 12 ft" fit?

ANSWER (one paragraph): **Allowed for A-3 and E, but only in exterior walls that need no fire-resistance rating. For Type IIB that means a fire separation distance of 10 ft or more (Table 705.5, R-030.4). Panel size, % and spacing then depend on the distance and the plastic class (CC1 / CC2). The band fits or not depending on the campus location, which is TBD.**
- **2607.1 (S9):** "Light-transmitting plastics shall not be used as wall panels in exterior walls in occupancies in Groups A-1, A-2, H, I-2 and I-3. In other groups, light-transmitting plastics shall be permitted … provided that the walls are not required to have a fire-resistance rating." A-3 and E are "other groups." Panels must comply with 2606.
- **2607.2:** panels "shall not alter the type of construction classification." **2607.3:** not more than 75 ft above grade plane (band is at 12–16 ft).
- **2607.4:** single-panel area and separations per Table 2607.4; the maximum % of wall area in any story is the Table 2607.4 value "or the percentage of unprotected openings permitted by Section 705.8, whichever is smaller."
- **2607.5:** the 100 % increase applies only with an NFPA 13 sprinkler system (903.3.1.1). **Not available to Rev B (non-sprinklered).**
- **2607.6:** combinations of plastic glazing and plastic wall panels follow the wall-panel limits.
- **2606.4 (material):** self-ignition ≥ 650 °F (ASTM D1929); smoke-developed index ≤ 450 (ASTM E84 / UL 723) or smoke density ≤ 75 (ASTM D2843); and Class **CC1** (burning extent ≤ 1 in, ASTM D635) or **CC2** (burning rate ≤ 2½ in/min). 2606.2 / 2606.3: technical data and identification marks for the building official.

**Table 2607.4 (S9), as published:**

| Fire separation distance (ft) | Class | Max % of exterior wall | Max single panel area (SF) | Min vertical sep. (ft) | Min horizontal sep. (ft) |
|---|---|---|---|---|---|
| Less than 6 | — | Not permitted | Not permitted | — | — |
| 6 to < 11 | CC1 | 10 | 50 | 8 | 4 |
| 6 to < 11 | CC2 | Not permitted | Not permitted | — | — |
| 11 to ≤ 30 | CC1 | 25 | 90 | 6 | 4 |
| 11 to ≤ 30 | CC2 | 15 | 70 | 8 | 4 |
| Over 30 | CC1 | 50 | Not limited | 3 (note b) | 0 |
| Over 30 | CC2 | 50 | 100 | 6 (note b) | 3 |

Notes: (a) combinations — see 2607.6; (b) vertical separation reductions — see 2607.4 (30 in flame-barrier exception).

**Combined with Table 705.5 (R-030.4):** a Type IIB A / E exterior wall needs 1 hour below 10 ft FSD, so 2607.1 bars plastic panels there. Usable cases are therefore FSD **10 to < 11 ft** (CC1 only), **11–30 ft**, and **over 30 ft**.

KEYSTONE arithmetic (from params: sidewall 125 ft long x 16 ft eave; band "above 12 ft" = at most 4 ft tall to the eave; endwall 60 ft x 16 ft + gable 0.5 x 60 x 2.5 ft):
- Sidewall area per story ≈ 125 x 16 = **2,000 SF**. A continuous full-length 4 ft band = 125 x 4 = **500 SF = 25.0 %**.
- Endwall area ≈ 960 + 75 = **1,035 SF**. A full-width 4 ft band = 240 SF = **23.2 %**.
- **FSD over 30 ft, CC1:** 25 % ≤ 50 %, no single-area limit, 0 ft horizontal separation → **a continuous band fits.** CC2: panels ≤ 100 SF (≤ 25 ft long at 4 ft tall) with ≥ 3 ft gaps.
- **FSD 11–30 ft, CC1:** 25 % cap is exactly the full band, but each panel ≤ 90 SF (≤ 22.5 ft long at 4 ft tall) with ≥ 4 ft gaps, so **a continuous band does not fit; a segmented band does.** CC2: ≤ 15 % (300 SF on a sidewall), panels ≤ 70 SF (≤ 17.5 ft long), 4 ft gaps.
- **FSD 10 to < 11 ft:** CC1 only, ≤ 10 % (200 SF on a sidewall), panels ≤ 50 SF (≤ 12.5 ft long), 4 ft gaps.
- **FSD < 10 ft:** not permitted (rated wall).
- **705.8 cap ("whichever is smaller"):** Table 705.8 unprotected, non-sprinklered openings are 15 % at 10 to < 15 ft, 25 % at 15 to < 20, 45 % at 20 to < 25, 70 % at 25 to < 30, no limit at 30+ (S10). But 705.8.1 exception 2 says buildings whose exterior walls and frame "are not required to be fire-resistance rated shall be permitted to have unlimited unprotected openings", and that is the Type IIB case at FSD ≥ 10 ft. **Whether the 705.8 cap still limits plastic panels there is an architect / official reading (flag).**
- Vertical separation only matters between stacked panels; a single band row on a one-story building has none (ASSUMED single row).

**Skylights (§2610):** none in params, so §2610 is not triggered. For reference if added (S9): each skylight ≤ 100 SF within the curb unless sprinklered or smoke / heat vents per 910 (2610.4); aggregate ≤ 33⅓ % of the room floor area (CC1) or 25 % (CC2) (2610.5); ≥ 4 ft apart (2610.6); not within 6 ft of an exterior wall whose openings must be protected (2610.7). See the R-028 flag below on whether the energy code would require skylights in the mat room.

**2018 IBC (S14):** Table 2607.4 reads the same (same rows, values and notes); 2607.1 has the same A-1 / A-2 / H / I-2 / I-3 prohibition text.

SOURCE: S9, S10, S14 — retrieved 2026-10-16.
EDITION / SECTION: IBC 2021 (Alabama) §§2606.2–2606.4, 2607.1–2607.6, Table 2607.4, 2610.4–2610.7, 705.8, Table 705.8, 705.8.1; 2018 IBC Table 2607.4 via S14 (secondary).
CONFIDENCE: HIGH for the table values and the A-3 / E permission (text read) / MEDIUM for the 705.8 cap interaction (exception reading) / LOW for fit (band length, panel class and FSD all TBD; band height derived from "above 12 ft" + 16 ft eave)
NEEDS ARCHITECT CONFIRMATION: YES. Also confirm the panel is a **plastic** (polycarbonate / FRP) product. If it is glass, §2607 does not apply (glazing under Chapter 24 and opening limits under 705.8 instead).

---

## R-030.4 — Exterior wall fire-resistance by fire separation distance (Table 705.5)

QUESTION: What does IBC Table 705.5 require for Type IIB exterior walls, Group A-3 / E, by fire separation distance?

ANSWER (one paragraph): **Type IIB, Group A or E: 1 hour if the fire separation distance is under 10 ft; 0 hours at 10 ft or more.** The actual rating stays **TBD** until the campus location is fixed (distance to lot lines / to an imaginary line between buildings on the same lot).

| Fire separation distance X (ft) | Construction type row | Group A, B, E, F-2, I, R, S-2, U | Applies to Rev B (IIB) |
|---|---|---|---|
| X < 5 | All | **1** | 1 h |
| 5 ≤ X < 10 | IA, IVA: 1 / Others: **1** | 1 | 1 h ("Others" includes IIB) |
| 10 ≤ X < 30 | IIB, VB | **0** | 0 h |
| X ≥ 30 | All | **0** | 0 h |

- 705.5 (S10): exterior walls rated "in accordance with Table 601 … and Table 705.5"; walls with FSD > 10 ft rated from the inside only, ≤ 10 ft from both sides.
- Table notes (S10): load-bearing exterior walls also meet Table 601 (Type IIB = 0, R-029.2); "Where Table 705.8 permits nonbearing exterior walls with unlimited area of unprotected openings, the required fire-resistance rating for the exterior walls is 0 hours."
- The same table also sets the **2607.1 limit** in R-030.3: rated walls (FSD < 10 ft) cannot have plastic wall panels.
- **2018 IBC (S14):** the same table is numbered **Table 602**; for IIB and A / E it reads the same (1 / 1 / 0 / 0).

SOURCE: S10, S14 — retrieved 2026-10-16.
EDITION / SECTION: IBC 2021 (Alabama) §705.5, Table 705.5 (and notes), §705.8.1; 2018 IBC Table 602 via S14 (secondary).
CONFIDENCE: HIGH for the table values / TBD for the actual rating (no site plan, FSD unknown)
NEEDS ARCHITECT CONFIRMATION: YES. The architect sets the FSD and ratings from the site plan. If the building sits within 10 ft of another HGHS building or a lot line, its walls need 1 hour, which also rules out the translucent band on that face.

---

## Could not verify (UNVERIFIED)
- **Site-specific tornado wind speed** (ATC Hazards by Location, Figure 304.2(1) note 3) was not queried. The zone answer rests on DCM's county map (a guide) and a low-resolution copy of the ICC figure.
- **Existing HGHS storm shelter capacity and location** (for 423.5.1 exception 2 and the 1,000 ft rule): unknown → TBD.
- **How DCM treats a no-classroom athletic building classified E** (its 30 SF classroom method vs IBC 423.5.1 item 2): no ruling found.
- **Alabama Act 2010-746** was not read, so whether it reaches a new detached building on an existing campus is unverified (DCM 23-02 frames it as "each new public school").
- **The A-1 … A-5 sub-column of Table 403.1 / 2902.1** did not render on UpCodes; rows were matched by description.
- **The translucent panel product:** plastic vs glass, CC1 vs CC2, 2606.4 test data — no Summertown or panel-maker data seen.
- **705.8 cap vs 705.8.1 exception 2** for plastic panel %: interpretation not settled.
- **2010 ADA drinking fountain / toilet details** (DCM says ADA supersedes IBC accessibility): not re-read today.
- **Madison County 2018 amendments** (resolution 2020-09-02): not read. 2018 values come from Texas / Georgia UpCodes copies (Georgia copy has state amendments).

## Conflicts / flags
- **E classification would add a storm shelter question** on top of R-029's manual fire alarm: IBC 423.5 says yes at 98 ≥ 50 (minimum about 60 occupants for the new building, KEYSTONE reading), but DCM's classroom-area threshold could say no. **Biggest open cost risk in this file. Ask DCM before pricing.**
- **yaml `fixtures.ratios` text:** labelled "A-3 indoor sport row", but the values are the "coliseums, arenas … indoor sporting events" row (IBC 303.5 A-4 wording). The A-3 "gymnasiums" row is 1 per 125 M / 1 per 65 F / lav 1 per 200 / DF 1 per 500. The drawn fixtures pass either row, so this is a text / citation fix only. The yaml also cites "IPC 2902.1" (IPC = 403.1; IBC = 2902.1). Params not changed per ticket rules.
- **Daylight band vs fire separation:** the band is only allowed on faces at FSD ≥ 10 ft; a continuous band needs FSD > 30 ft with CC1 plastic. Campus location decides.
- **R-028.3 cross-reference (not re-verified today):** IECC 2015 C402.4.2 requires skylights in spaces > 2,500 SF under a roof with ≥ 75 % of the ceiling > 15 ft, used as (among others) a gymnasium / exercise center. The mat room is 3,000 SF with a 16 ft eave / 14 ft clear (params). Whether it triggers is UNVERIFIED. If it does, skylights (§2610 limits above) or a sidelight / monitor exception would be needed.
- **Code edition (open, R-006 / D-008):** DCM 2021 vs Madison County 2018. For every item in this file, the 2018 text found reads the same in substance (423.4 wording differences noted in R-030.1).

## What changes for KEYSTONE
- **Nothing needs regenerating.** The Rev B fixture counts pass the A-3, E and arena rows. No shelter is required as A-3. The translucent band and exterior wall ratings stay TBD until the campus location is fixed.
- Optional text fixes for a future Rev C (not made): `fixtures.ratios` source → "IBC 2021 Table 2902.1 / IPC 2021 Table 403.1, coliseum / arena row (conservative); A-3 gymnasium row = 125 / 65 / 200 / 500"; `fixtures.basis` → "IPC 403.1.1 / IBC 2902.1.1"; add notes "translucent band only on faces with FSD ≥ 10 ft (IBC 2607.1, Table 705.5); continuous band needs FSD > 30 ft + CC1 (Table 2607.4)" and "if Group E: ICC 500 shelter per IBC 423.5 / DCM 23-01, capacity TBD".
- **Questions to add to the AHJ / DCM pre-application list:**
  1. If DCM classifies the building as Group E, is an ICC 500 tornado shelter required for a new detached athletic building with no classrooms (IBC 423.5.1 item 2 vs Bulletin 23-01's classroom method)? At what capacity?
  2. Does HGHS already have ICC 500 shelter capacity on campus that can be counted (423.5.1 exception 2), and is one within 1,000 ft of the proposed site (423.5.2)?
  3. Confirm the design wind speed (250 mph per DCM Attachment A) and whether the building may instead be designed to ICC 500 (423.5 exception 3).
  4. Which fixture row applies (A-3 gymnasium or E), and do team toilets count toward the building total?
  5. Does the 705.8 unprotected-opening % cap apply to plastic wall panels on unrated Type IIB walls (705.8.1 exception 2)?
- **Questions to add to the Summertown Metals RFQ:**
  1. Is the daylight panel plastic (polycarbonate / FRP) or glass? If plastic: CC1 or CC2 (ASTM D635), self-ignition ≥ 650 °F (ASTM D1929), smoke index ≤ 450 (ASTM E84) per IBC 2606.4, with labels.
  2. Standard panel widths / lengths and minimum gaps, so segments can stay ≤ 90 SF (CC1) or ≤ 70 SF (CC2) at 11–30 ft FSD.
  3. Price as an alternate: an ICC 500 tornado-shelter room or wall system (250 mph, missile per ICC 500 Table 305.1.1), in case DCM requires one.
