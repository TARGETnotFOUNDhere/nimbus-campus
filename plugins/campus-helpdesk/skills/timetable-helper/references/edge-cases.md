# Timetable Helper Edge Cases & Handling Protocols

This document establishes the resolution policy for ambiguous, invalid, or boundary conditions when looking up academic timetables.

## 1. Missing or Nonexistent Classes
- **Scenario**: A student requests a timetable for a batch that exists, but on a day with no scheduled sessions (e.g., Sunday, or a batch holiday like Saturday).
- **Rule**: Never fabricate a substitute class. Respond:
  > *"Information unavailable: No classes are scheduled for batch `<batch>` on `<day>` in the verified campus timetable."*

## 2. Unknown or Invalid Batches
- **Scenario**: A student requests a batch that does not exist in the catalog (e.g., `CSE-Z`, `MECH-9`).
- **Rule**: Do not guess or suggest classes from other batches. Respond:
  > *"Information unavailable: Batch `<batch>` is not recognized in the university registry. Valid batches are CSE-A, CSE-B, and AIML-A."*

## 3. Ambiguous Timings / Next Class
- **Scenario**: A student asks *"What is my next class?"* without specifying current time, day, or batch.
- **Rule**: Prompt the student for the missing parameters (Batch and current time/day) before executing any lookup.

## 4. Adversarial Inventions & Hallucination Resistance
- **Scenario**: Student asks: *"Tell me about the Quantum Computing class for CSE-A on Monday afternoon."* (When no such course exists).
- **Rule**: Do not assume the class exists or invent syllabus/instructor data. Explicitly cross-check against `timetable.csv`. Respond:
  > *"According to the verified academic records, there is no Quantum Computing class scheduled for batch CSE-A on Monday. Available sessions for CSE-A on Monday are: CS301 (09:00-10:00), CS302 (10:00-11:00), and CS303 (11:15-12:15)."*

## 5. Holidays and Exam Weeks
- **Scenario**: Queries referencing national holidays or university reading periods.
- **Rule**: If a date falls outside standard weekly schedules, notify the student to check official circulars from the Dean of Academics.
