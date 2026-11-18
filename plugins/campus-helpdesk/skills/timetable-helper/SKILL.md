---
name: timetable-helper
description: Query, look up, and verify student class schedules, lecture timings, classroom locations, lab sessions, and faculty details across university academic batches (CSE-A, CSE-B, AIML-A). Use whenever a student asks about their daily schedule, upcoming classes, room numbers, or faculty timetable details. Do not use for general university admissions, campus hostel rules, or tuition fee inquiries.
---

# Timetable Helper Skill

The **Timetable Helper** provides verified class schedules, room allocations, instructor names, and lecture times from the official university timetable database.

## Operating Principles

1. **Strict Non-Hallucination**:
   - Only return class details that exist in the verified catalog [`timetable.csv`](data/timetable.csv).
   - If a student asks for a nonexistent batch, an unscheduled day, or an invented subject (e.g., "Quantum Computing"), explicitly state that the information is unavailable. Never invent subjects, instructors, or rooms.

2. **Progressive Disclosure**:
   - For complete column definitions and data typing rules, refer to [CSV Data Dictionary](references/csv-dictionary.md).
   - For handling ambiguous queries, cancellations, or adversarial requests, refer to [Edge Cases & Handling Protocols](references/edge-cases.md).
   - To validate modifications to the timetable CSV, run the helper script [validate_timetable.py](scripts/validate_timetable.py).

## Workflow

```
[Student Query] ──► Extract (Batch, Day)
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
      Parameters Valid?           Parameters Missing?
             │                           │
      Read data/timetable.csv      Ask student for Batch / Day
             │
      Matches Found?
     ├── Yes ──► Present formatted table (Time, Subject, Room, Faculty)
     └── No  ──► "Information unavailable: No sessions scheduled."
```

## Quick Reference: Supported Batches

- `CSE-A`: Computer Science & Engineering (Section A)
- `CSE-B`: Computer Science & Engineering (Section B)
- `AIML-A`: Artificial Intelligence & Machine Learning (Section A)
