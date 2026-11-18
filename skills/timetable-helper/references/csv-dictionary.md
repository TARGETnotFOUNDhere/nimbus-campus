# Timetable CSV Data Dictionary

This document details the schema, allowed values, and data types for `skills/timetable-helper/data/timetable.csv`.

## Schema Overview

| Column Name | Data Type | Mandatory | Description | Allowed Values / Pattern | Example |
|---|---|---|---|---|---|
| `batch` | String | Yes | Student academic batch / cohort identifier | `CSE-A`, `CSE-B`, `AIML-A`, `AIML-B`, `ECE-A` | `CSE-A` |
| `day` | String | Yes | Day of the academic week | `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` | `Monday` |
| `slot` | String | Yes | Timetable slot identifier | `Slot-1`, `Slot-2`, `Slot-3`, `Slot-4`, `Slot-5` | `Slot-1` |
| `start_time` | String | Yes | Class scheduled start time (24-hour format) | `HH:MM` (08:00 to 18:00) | `09:00` |
| `end_time` | String | Yes | Class scheduled end time (24-hour format) | `HH:MM` (09:00 to 19:00) | `10:00` |
| `course_code` | String | Yes | Official catalog course code | Alphanumeric (e.g., `CS[0-9]{3}[P]?`) | `CS301` |
| `course_name` | String | Yes | Full course title | Descriptive string | `Data Structures & Algorithms` |
| `instructor` | String | Yes | Faculty assigned to teach | Formal name with honorific | `Dr. Robert Fox` |
| `room` | String | Yes | Physical classroom / laboratory location | `LH-[0-9]{3}`, `CS-Lab-[0-9]`, `AI-Lab-[0-9]` | `LH-101` |
| `class_type` | String | Yes | Session modality | `Lecture`, `Tutorial`, `Practical`, `Seminar` | `Lecture` |

## Integrity Rules

1. **No Overlapping Slots**: A single batch cannot have two classes scheduled in overlapping time windows on the same day.
2. **Room Exclusivity**: A physical room cannot host multiple batches during overlapping time intervals.
3. **Exact Matching**: Query parameters for `batch` and `day` must match case-insensitively with canonical normalization (`CSE-A` matches `cse-a`, `Monday` matches `monday`).
4. **No Hallucination**: If a batch, day, or time slot has no corresponding entry, the assistant MUST report that no record exists.
