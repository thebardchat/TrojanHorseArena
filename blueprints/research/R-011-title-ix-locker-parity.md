# R-011 — Title IX locker room parity expectations (Phase 2 event / team locker rooms)

Researched by KEYSTONE 2026-10-12 (daily automation, ~6:10 AM CT). Feeds P2-A-401 (enlarged locker plans) and program / owner notes. Builds on R-024 (ADA locker rooms, showers, benches) and R-009 (fixture counts). R-010 (ADA assembly seating) is not affected.
Status: research note, **not legal advice and not a code review (D-008)**. **PRELIMINARY — CONCEPTUAL DESIGN — NOT FOR CONSTRUCTION.**
Nothing below sets a fixture count, SF, or room size. Title IX gives **comparability / equivalence tests**, not dimensions.

## Sources (all retrieved 2026-10-12)

- **S1** — 34 CFR 106.41 *Athletics* (eCFR, issue date 2026-10-08). https://www.ecfr.gov/current/title-34/subtitle-B/chapter-I/part-106/subpart-D/section-106.41 — text pulled through the eCFR versioner API (`/api/versioner/v1/full/2026-10-08/title-34.xml?part=106&section=106.41`); box copy `/workspace/research_src/r011/ecfr_106.41.txt`. PRIMARY.
- **S2** — 34 CFR 106.33 *Comparable facilities* (same method). https://www.ecfr.gov/current/title-34/subtitle-B/chapter-I/part-106/subpart-D/section-106.33 — box copy `ecfr_106.33.txt`. PRIMARY.
- **S3** — 34 CFR 106.31 *Education programs or activities* and 106.11 *Application* (same method; 106.11 / 106.31 last amended 91 FR 61316-61318, 2026-09-29). Box copies `ecfr_106.31.txt`, `ecfr_106.11.txt`. PRIMARY.
- **S4** — U.S. Dept. of Education, *Recodification of Title IX Rules*, final rule, 91 FR 61308 (FR Doc. 2026-19929), effective 2026-09-29. https://www.federalregister.gov/documents/2026/09/29/2026-19929/recodification-of-title-ix-rules — full text at https://www.federalregister.gov/documents/full_text/text/2026/09/29/2026-19929.txt (box copy `fr_2026-19929.txt`). PRIMARY.
- **S5** — HEW/OCR, *Title IX and Intercollegiate Athletics; a Policy Interpretation*, 44 FR 71413 (1979-12-11), as posted by ED: https://www.ed.gov/laws-and-policy/civil-rights-laws/federal-register-notices-and-regulations/policy-interpretation-title-ix-and-intercollegiate-athletics — **direct fetch blocked (HTTP 403 / timeout from box and fetcher); quoted text read through the WebSearch index of the same ED page.** PRIMARY (agency guidance), access-limited.
- **S6** — ED, *Q and A: Intercollegiate Athletics Policy Three-Part Test, Part Three* (says the 1979 PI principles "often will apply to interscholastic, club, and intramural athletic programs"). http://www.ed.gov/laws-and-policy/civil-rights-laws/title-ix-and-sex-discrimination/title-ix-key-issues/title-ix-and-athletics/q-and-intercollegiate-athletics-policy-three-part-test-part-three — read through WebSearch index (same block). PRIMARY, access-limited.
- **S7** — OCR resolution letter, Lockport Township High School District 205 (OCR 05-14-1298). https://www.ed.gov/sites/ed/files/about/offices/list/ocr/docs/investigations/more/05141298-a.pdf — read through WebSearch index (direct 403). PRIMARY example (K-12 application of S1 / S5 to locker rooms, incl. off-campus facilities and a visiting-team locker room). Access-limited.
- **S8** — 20 U.S.C. 1681 (Title IX) and 1687 ("program or activity"), Cornell LII. https://www.law.cornell.edu/uscode/text/20/1681 · https://www.law.cornell.edu/uscode/text/20/1687 — SECONDARY host of the statute text.
- **S9** — Alabama Act 2022-290 (HB 322, enrolled), codified Ala. Code § 16-1-54. https://alison.legislature.state.al.us/files/pdf/SearchableInstruments/2022RS/PrintFiles/HB322-Enr.pdf (box copy `al_hb322_enr.pdf`); act record https://arc-sos.state.al.us/cgi/actdetail.mbr/detail?page=act&year=2022&act=290 (signed 2022-04-08). PRIMARY (state).
- **S10** — Executive Order 14201, *Keeping Men Out of Women's Sports*, 90 FR 9279 (2025-02-11). https://www.federalregister.gov/documents/2025/02/11/2025-02513/keeping-men-out-of-womens-sports — read through WebSearch index. PRIMARY (federal enforcement policy; not a facility standard).
- Not used as a rule source: ED's Feb 2023 *Title IX and Athletic Opportunities in K-12 Schools* resource — the ED file name marks it **rescinded**. NFHS / Women's Sports Foundation summaries — context only.

---

## R-011.1 — What Title IX says about locker rooms

QUESTION: What does the current Title IX regulation require for locker rooms in athletics?

ANSWER: Two rules. (1) **34 CFR 106.33:** "A recipient may provide separate toilet, locker room, and shower facilities on the basis of sex, but such facilities provided for students of one sex shall be comparable to such facilities provided for students of the other sex." (2) **34 CFR 106.41(c):** a recipient that "operates or sponsors interscholastic, intercollegiate, club or intramural athletics shall provide equal athletic opportunity for members of both sexes," judged on factors including "(7) Provision of locker rooms, practice and competitive facilities." 106.41(c) also says unequal spending alone "will not constitute noncompliance." The standard is **comparable / equivalent**, not identical, and the regulation gives **no SF, fixture or locker count**.

SOURCE: 34 CFR 106.33 and 106.41 (eCFR) — URLs in S1 / S2 — retrieved 2026-10-12
EDITION / SECTION: 34 CFR part 106 as recodified by 91 FR 61308 (effective 2026-09-29). 106.33 last amended 85 FR 30579 (2020); 106.41 text unchanged except 106.41(d) (obsolete adjustment period) not reinstated (S4).
CONFIDENCE: HIGH
NEEDS ARCHITECT CONFIRMATION: NO (text) / YES (whether it applies, see R-011.4)

## R-011.2 — How OCR judges locker room parity

QUESTION: What does OCR actually compare when it checks locker rooms and facilities?

ANSWER: The 1979 Policy Interpretation (S5, § on 86.41(c)(7), now 106.41(c)(7)) says compliance is assessed by the equivalence for men and women of: **(1) quality and availability of facilities for practice and competitive events; (2) exclusivity of use; (3) availability of locker rooms; (4) quality of locker rooms; (5) maintenance of facilities; (6) preparation of facilities for practice and competitive events.** The governing principle is "equivalent treatment, benefits, and opportunities," judged across the program as a whole. ED states (S6) these principles "often will apply to interscholastic, club, and intramural" programs, i.e., high-school teams too. An OCR K-12 resolution (S7) applied the same six factors, looked at off-campus practice / competition sites, and noted where the district put opposing (visiting) teams. **Design reading (KEYSTONE, ASSUMED):** for P2 this means a girls' team room should not be smaller, older-finish, less available, or farther / worse-served than the boys' room, and event locker assignment should not systematically favor one sex.

SOURCE: 44 FR 71413 (S5); ED Q&A (S6); OCR 05-14-1298 (S7) — URLs above — retrieved 2026-10-12 (via search index; direct fetch blocked)
EDITION / SECTION: 1979 Policy Interpretation, item "f. Provision of Locker Rooms, Practice and Competitive Facilities (§ 86.41(c)(7))"; still listed by ED as current policy.
CONFIDENCE: MEDIUM (text read through the search index, not a clean direct copy)
NEEDS ARCHITECT CONFIRMATION: YES (and owner's counsel, if a school will be a user)

## R-011.3 — Current federal status (October 2026)

QUESTION: Which Title IX rule text is in force today?

ANSWER: ED's final rule 91 FR 61308 (S4), effective **2026-09-29**, repealed the vacated 2024 rule and restored part 106 "as it appeared on April 28, 2024," with listed exceptions (one 106.45 sentence, Appendix A, 106.3(c)-(d), 106.41(d)). The locker-room sections above (106.33, 106.41(c)) are the restored text. Separately, EO 14201 (S10, 2025-02-05) directs ED to "affirmatively protect all-female athletic opportunities and all-female locker rooms" and to prioritize enforcement against institutions that require female students "to appear unclothed before males." This is enforcement policy, not a facility size; for design it points to **sex-separated team rooms with private changing**, which the current plan already assumes (separate boys / girls lockers).

SOURCE: 91 FR 61308 (S4); EO 14201, 90 FR 9279 (S10) — URLs above — retrieved 2026-10-12
EDITION / SECTION: FR Doc. 2026-19929, Part IV; EO 14201 § 3(b)(ii)-(iii)
CONFIDENCE: HIGH (S4) / MEDIUM (S10, read through search index)
NEEDS ARCHITECT CONFIRMATION: NO (status) / YES (re-check before permit; federal policy can change)

## R-011.4 — Does Title IX apply to Shane's Phase 2 building? (D-028 / D-007)

QUESTION: Phase 2 is Shane's build, not a school project (D-028). When, if ever, does Title IX parity reach these locker rooms?

ANSWER: Title IX covers "any education program or activity receiving Federal financial assistance" (20 U.S.C. 1681(a), S8), and part 106 "applies to every recipient and to the education program or activity operated by such recipient" (34 CFR 106.11, S3). A privately owned arena that takes no federal financial assistance is **not itself a Title IX recipient by that text.** Three ways it could still matter, all **TBD**:
- **(a) School users (most likely).** If Madison County Schools / Hazel Green High School (a recipient) rents or uses the building for its teams, **the school** carries the duty: 106.41(c)(7) parity in the locker rooms it provides, and 106.31(b)(6) / (d) bar a recipient from giving "significant assistance" to, or running activities through, an operator that discriminates on the basis of sex. In practice the school would need boys' and girls' rooms of **comparable** quality and availability in this building. S7 shows OCR does review off-campus sites a district uses.
- **(b) Federal money to the owner.** 20 U.S.C. 1687(3)(A) treats a whole private organization as covered when assistance goes to it as a whole or it is "principally engaged in the business of providing education, ... or parks and recreation." If the owner of record (D-007, OPEN) takes federal grants, ask counsel. 
- **(c) Youth club (HG Trojan Youth Wrestling).** A non-school club is not a recipient by the statute text unless it gets federal financial assistance. NOT RESEARCHED further; owner's counsel.
**Alabama:** Ala. Code § 16-1-54 (S9) requires "every multiple occupancy restroom or changing area designated for student use" to be used by biological sex, but it is defined as an area "in a public K-12 school building." By its text it does not reach a private building; **ASSUMED** that a school renting the arena will still expect its students' team rooms assigned by sex (school policy). District / AHJ to confirm.

SOURCE: 20 U.S.C. 1681, 1687 (S8); 34 CFR 106.11, 106.31 (S3); Ala. Code § 16-1-54 / Act 2022-290 (S9); OCR 05-14-1298 (S7) — retrieved 2026-10-12
EDITION / SECTION: as cited
CONFIDENCE: MEDIUM (applicability depends on owner of record D-007 and any school use agreement — both TBD)
NEEDS ARCHITECT CONFIRMATION: YES — plus owner's attorney and, if school events are planned, Madison County Schools.

## R-011.5 — What this means for the current plan (no numbers changed)

QUESTION: Does the current Phase 2 locker program raise a parity flag?

ANSWER: Current params: boys locker **3,500 SF**, girls locker tagged **3,503 SF**, drawn equal per D-013 (OPEN); event locker rooms 1-4 at 900 SF each (D-060), fixture counts ASSUMED in R-024 / P2-A-401. Title IX does not require identical SF, but **drawing them equal (D-013 rule) already meets the "comparable" test on size**; the 3 SF tag difference is not a parity issue either way. Items the regulation's factors would look at that the drawings do not yet show (all **TBD**, not designed here): finish quality, showers / toilets per room (keep the same per room), team-room / film-room access, lockers per room, distance to the court and the athletic trainer room, and scheduling of event rooms 1-4. **Recommendation (ASSUMED, no decision logged):** keep boys / girls rooms equal in SF, fixtures and finish; if event rooms 1-4 are assigned by sex on event days, keep a 2 + 2 split or an equal-quality rotation; give officials separate changing for each sex (NOT RESEARCHED: officials are not students, so Title IX 106.33 does not cover them; employment / building-code rules may).

SOURCE: params/phase2.yaml (boys_locker / girls_locker); DECISIONS D-013, D-060; R-024 — plus S1 / S2 / S5 — retrieved 2026-10-12
EDITION / SECTION: phase2.yaml current; 34 CFR 106.33 / 106.41(c)(7)
CONFIDENCE: HIGH (equal = comparable on size) / LOW (everything else is TBD until layouts exist)
NEEDS ARCHITECT CONFIRMATION: YES

## Could not verify / not researched

1. ED / OCR pages (S5-S7) blocked direct fetch (HTTP 403 / timeout) on 2026-10-12; quotes come from the search index of those same pages. Re-pull a clean copy when access allows.
2. OCR 1990 *Title IX Athletics Investigator's Manual* (ERIC ED400763) — not read in full.
3. AHSAA rules (if any) on visiting-team locker rooms — not researched.
4. Madison County Schools facility-use / rental policy (what it would require of a private host) — not researched; ties to R-002.
5. Whether any federal grant is planned for Phase 2 (R-011.4 b) — Shane / owner (D-007).

## What changes for KEYSTONE

- **New research file:** this file. No sheet regenerated; no params changed; no decision logged.
- P2-A-401 notes (next revision only): cite R-011 next to R-024; "boys / girls team rooms comparable per 34 CFR 106.33 (equal SF per D-013)."
- D-013 stays OPEN; R-011 gives a reason to keep the draw-equal rule.
- **NEEDS ARCHITECT CONFIRMATION: YES** on R-011.2, R-011.4, R-011.5.
