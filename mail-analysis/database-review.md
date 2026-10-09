# Email database review — 2026-10-08

Reviewed all 94 current INBOX messages. Other folders were not reviewed.
Credential and license emails were excluded from database candidates.
Eight exam calendar attachments were independently checked. The follow-up import
updated both generators and all five generated databases. Supporting course extracts:
`../plan/source-extracts/email-course-facts-2026-10-08.json` relative to bht-schedule.
Source identity includes mailbox, UIDVALIDITY, UID, date, subject and excerpt.

## Additions supported by current course-detail fields

| Subject / scope | Candidate fact | Current field | Email UID |
| --- | --- | --- | --- |
| Web Engineering II, Zug 1 | Blatt 00 due 2026-10-15 at 23:59; Moodle activity 1508636 | deadlines, sources | 93 |
| Theoretical computer science, Zug 2 | Test: Mengen opens 2026-10-05 at 14:03 and closes 2026-10-19 at 23:59; activity 1510499 | deadlines, keyFacts, sources | 67 |
| Mediendesign SU, Zug 2 | Binding enrollment submission due 2026-10-11 at 19:00; activity 1521541 | deadlines, sources | 66 |
| Mediendesign SU, Zug 2, personal | Submission confirmation on 2026-10-05; confirms submission, not acceptance or passing | keyFacts if explicitly personal; dedicated progress field would be clearer | 76 |
| Betriebssysteme, Weis / track unknown | Exercise sheet 1: four shell tasks worth 6, 6, 16, 16 points (44 total); vimtutor and sheets 1–2 using vi; only taught standard sh commands. Neither track nor deadline stated | unassignedDetails.workloadRules/keyFacts/sources | 91 |
| Web Engineering II, Zug 1 | Blatt 0 project fixed; update existing fork and clone or recreate. Do not execute instructions during import | keyFacts, sources | 92 |
| Software Engineering II, Ziemer / Zug 2 | Teams of at most five people in the same exercise block; group preferences due 2026-10-07 at 16:00; otherwise random allocation | deadlines, workloadRules, keyFacts, sources | 74 |
| Project Moodle course; track not stated | Pitch on Thursday 2026-10-08, 09:30–11:30, Ingeborg-Meising-Saal. Date inferred from 2026-10-04 announcement. Activity 1400091 | unassignedDetails.deadlines/keyFacts until scope confirmed | 70 |
| Project Moodle course; track not stated | GitLab subgroups/repositories created; members should have Owner role; invitations may be in spam; questions via Discord; supervisor assignments to follow | unassignedDetails.keyFacts until scope confirmed | 70 |

Moodle emails do not explicitly state a timezone for these deadlines. Preserve
this uncertainty instead of labelling all times verified Europe/Berlin.

## Schedule and group changes

- Web Engineering II, Zug 1 (UID 81): additional Wednesday exercise 12:15–13:45,
  B240. Not present in current schedule. Attendance in another exercise generally
  allowed; registered group has priority; defenses and mock exam normally in the
  registered group. Redistribution planned. Teacher and track are established;
  new stable group ID and exact validity dates need confirmation before a meeting
  record is created. Store announcement and rules in keyFacts/workloadRules now.
- Software Engineering II, Ziemer / Zug 2 (UID 74): first lecture 2026-10-09 at
  16:00; actual exercise times to be determined and may differ from the timetable.
  Do not replace weekly times with an unconfirmed plan.
- Medientechnologien (UIDs 79, 87): Hönemann announces both of her exercise groups
  together on 2026-10-09 at 14:15, B325; no 08:00 exercise that day. Mixdorff says
  exercises begin 2026-10-16. These may have different instructor/group scope or
  distinguish an introduction from ordinary exercises. Keep both sources and
  flag scope for clarification; do not cancel all tracks automatically.
- Theoretical computer science, Werth / Zug 2 (UID 84): some students will be
  reassigned to the other track because of capacity. No individual assignment is
  confirmed by this announcement. Preserve this as a note, not a group update.
- Mediendesign (UIDs 77–78): overcrowding, late exercise referenced as starting
  at 19:00 (current timetable has 19:30), tentative Tuesday-morning alternatives
  and possible Monday SU with Tuesday exercise. No finalized personal assignment.
  Individual projects are said to be unavailable this semester in Zahn's course;
  do not apply this to Schiffers' course.

One-day cancellations, moves, task status and group reassignment would be more
reliable with explicit event/assignment/progress fields. Existing keyFacts can
preserve these announcements without changing the schema.

## Exams: confirmations, not new records

| Subject | Tracks | Date | Time | Room | UID |
| --- | --- | --- | --- | --- | --- |
| Medientechnologien | 1, 2 | 2027-01-15 | 12:00–14:00 | not stated | 58 |
| Betriebssysteme | 1 | 2027-01-19 | 16:00–17:30 | D138 | 85 |
| Web Engineering II | 2 | 2027-01-25 | 16:00–17:00 | not stated | 64 |
| Theoretical computer science | 2 | 2027-01-29 | 10:00:51–11:30:51 | Vorlesungsraum | 83 |
| Software Engineering II | 1 | 2027-02-03 | 12:15–13:45 | H4 | 59 |
| Web Engineering II | 1 | 2027-02-03 | 14:15–15:15 | not stated | 61 |
| Software Engineering II | 1 | 2027-03-31 | 13:30–15:00 | TBD | 60 |
| Web Engineering II | 1 | 2027-03-31 | 16:00–17:00 | not stated | 62 |

All eight match existing examSlots. ICS files confirm the same values, including
the unusual 51 seconds in theoretical computer science. No timezone is declared
in the exam DTSTART/DTEND properties. Keep stable IDs and add provenance on import;
do not create duplicate exams or invent missing rooms or a second-period label.

## Separate personal or semester-wide candidates

- Recognition correspondence (UIDs 29–41): recognition performed and subsequently
  adjusted; precise module mapping must be checked in the recognition PDFs or Polli.
  Do not mark arbitrary current modules completed. Studium Generale recognition
  is confirmed in correspondence, but individual module/credit mapping is unclear.
- International mobility (UIDs 63, 75): information event 2026-10-12; application
  day/month deadlines 15 December for winter 2027/28 and 15 July for summer 2028.
  Deadline years must be recorded as inferred until confirmed. General eligibility
  and thesis-abroad guidance belongs in a mobility/planning area, not course grading.
- AStA interview (UIDs 86, 88): booking confirmed 2026-10-13, 13:00–14:00
  Europe/Berlin; invitation gives M E03. Personal calendar candidate.
- Semester-wide opportunities: Studium Generale enrollment 2026-10-01–17 (UID 51),
  Entrepreneur:innen@BHT Tuesdays 16:00–18:00 in GLASBOX, 2.5 ECTS, pitch
  2027-02-02 (UID 57); Zukunftstage 2026-11-16–20 with SG/WP options (UID 14).
- AStA summer exam circular (UID 5) has summer-2026 dates and general regulations
  commentary. It must not replace winter-term handbook or teacher assessment rules.
- Campus events, jobs, library services, ticket information and IT announcements
  are identifiable, but the current subject database has no appropriate dedicated
  destination. Historical deadlines must remain historical. General receipt of
  these mailing-list messages does not establish personal relevance or eligibility.

## Suggested import priority

1. Add the three explicit course deadlines and supporting sources.
2. Add operating-systems tasks and SE2 Zug 2 team rules.
3. Preserve project pitch and organizational facts with track uncertainty.
4. Add the new WE2 exercise after group/validity confirmation; keep tentative and
   conflicting scheduling announcements as notes until resolved.
5. Strengthen provenance for the eight existing exams without duplicating them.

## Import completed — 2026-10-08

Both generators were updated before regeneration. The generated databases now
contain 11 course-detail additions, seven imported tasks, the confirmed additional
WE2 exercise, eight strengthened exam references and separate personal planning.
All existing modules, groups, meetings and exam values were preserved.

The new WE2 group has a null official group number, registration period and date
range rather than invented values. Unknown Betriebssysteme and project tracks
remain unassigned. Tentative one-day scheduling changes remain explicitly qualified
notes rather than automatic calendar cancellations.

The three recognition PDFs were saved outside the app. Form fields were extracted,
and pages 1–5 of the signed module mapping were visually verified. Fourteen module
rows with 75 documented credits and placement in semester 3 are stored as a dated
2026-09-07 snapshot. Later administrative adjustments and current Polli grades are
not assumed to match that snapshot. Other PDF attachments were not imported.

The interview calendar attachment explicitly establishes Europe/Berlin.
Original calendar attachments are saved in the external plan/source-exports folders.
Imported homework appears in the interface while preserving browser edits,
submission changes and deletion choices.
