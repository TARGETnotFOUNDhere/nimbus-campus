#!/usr/bin/env python3
"""
validate_timetable.py
Validation script for campus timetable CSV data.
Enforces schema validity, temporal order, room collisions, and batch overlaps.
"""

import csv
import sys
from pathlib import Path

REQUIRED_COLUMNS = [
    "batch", "day", "slot", "start_time", "end_time",
    "course_code", "course_name", "instructor", "room", "class_type"
]

VALID_DAYS = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
VALID_CLASS_TYPES = {"Lecture", "Tutorial", "Practical", "Seminar"}

def parse_time(time_str: str) -> int:
    """Convert HH:MM to minutes from midnight for range checking."""
    parts = time_str.strip().split(":")
    if len(parts) != 2:
        raise ValueError(f"Invalid time format: {time_str}")
    h, m = int(parts[0]), int(parts[1])
    if not (0 <= h <= 23 and 0 <= m <= 59):
        raise ValueError(f"Time out of range: {time_str}")
    return h * 60 + m

def validate_timetable(csv_path: str) -> bool:
    path = Path(csv_path)
    if not path.exists():
        print(f"ERROR: File not found: {csv_path}", file=sys.stderr)
        return False

    errors = []
    rows = []

    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            print("ERROR: CSV is empty or has no header.", file=sys.stderr)
            return False

        missing_cols = [c for c in REQUIRED_COLUMNS if c not in reader.fieldnames]
        if missing_cols:
            print(f"ERROR: Missing required columns: {missing_cols}", file=sys.stderr)
            return False

        for line_no, row in enumerate(reader, start=2):
            for col in REQUIRED_COLUMNS:
                if not row.get(col, "").strip():
                    errors.append(f"Line {line_no}: Empty value for '{col}'")

            # Day validation
            day = row.get("day", "").strip()
            if day not in VALID_DAYS:
                errors.append(f"Line {line_no}: Invalid day '{day}'")

            # Class type validation
            c_type = row.get("class_type", "").strip()
            if c_type not in VALID_CLASS_TYPES:
                errors.append(f"Line {line_no}: Invalid class_type '{c_type}'")

            # Time order validation
            try:
                start_m = parse_time(row.get("start_time", ""))
                end_m = parse_time(row.get("end_time", ""))
                if start_m >= end_m:
                    errors.append(f"Line {line_no}: start_time ({row.get('start_time')}) must precede end_time ({row.get('end_time')})")
            except ValueError as ve:
                errors.append(f"Line {line_no}: {ve}")

            rows.append((line_no, row))

    # Overlap and collision checks
    for i in range(len(rows)):
        l1, r1 = rows[i]
        try:
            s1, e1 = parse_time(r1["start_time"]), parse_time(r1["end_time"])
        except ValueError:
            continue

        for j in range(i + 1, len(rows)):
            l2, r2 = rows[j]
            if r1["day"] != r2["day"]:
                continue
            try:
                s2, e2 = parse_time(r2["start_time"]), parse_time(r2["end_time"])
            except ValueError:
                continue

            # Check overlap: (StartA < EndB) and (EndA > StartB)
            if (s1 < e2) and (e1 > s2):
                if r1["batch"] == r2["batch"]:
                    errors.append(f"Collision: Batch '{r1['batch']}' double-booked on {r1['day']} between Line {l1} and Line {l2}")
                if r1["room"] == r2["room"]:
                    errors.append(f"Collision: Room '{r1['room']}' double-booked on {r1['day']} between Line {l1} and Line {l2}")

    if errors:
        print(f"Validation FAILED with {len(errors)} error(s):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return False

    print(f"Validation PASSED: {len(rows)} timetable records verified successfully.")
    return True

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).resolve().parent.parent / "data" / "timetable.csv")
    success = validate_timetable(target)
    sys.exit(0 if success else 1)
