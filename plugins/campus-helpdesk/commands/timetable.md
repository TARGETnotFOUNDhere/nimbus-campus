---
description: Retrieve and display the official class schedule for an academic batch.
usage: /timetable <batch> [day]
---

# Timetable Slash Command

Execute a structured timetable lookup for campus batches.

## Instructions

1. If `<batch>` is omitted, ask the user to provide their academic batch (`CSE-A`, `CSE-B`, or `AIML-A`).
2. If `[day]` is omitted, default to the current weekday.
3. Invoke the `get_timetable(batch, day)` MCP tool or consult `skills/timetable-helper/data/timetable.csv`.
4. Render the returned slots in a clean markdown table showing:
   - Slot & Time
   - Course Code & Name
   - Room Number
   - Faculty Instructor
5. If no records exist, inform the student that information is unavailable. Never fabricate classes.
