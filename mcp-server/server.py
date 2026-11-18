#!/usr/bin/env python3
"""
server.py
Official Python MCP Server implementation for the Nimbus Campus Helpdesk.
Implements:
  - Tool 1: get_timetable(batch, day)
  - Tool 2: get_fee_status(student_id)
  - Resource: hostel://rules
Compatible with both MCP Python SDK 2.x (MCPServer) and 1.x (FastMCP).
Uses stdio transport.
"""

import csv
import json
import re
from pathlib import Path
from typing import Any, Dict, List

# Compatible import across MCP SDK versions
try:
    from mcp.server.mcpserver import MCPServer
    mcp = MCPServer("campus-helpdesk")
except (ImportError, ModuleNotFoundError):
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("campus-helpdesk")

# Define Base Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
TIMETABLE_FILE = DATA_DIR / "timetable.csv"
FEES_FILE = DATA_DIR / "fees.json"
HOSTEL_RULES_FILE = DATA_DIR / "hostel-rules.md"

# Input validation patterns
STUDENT_ID_PATTERN = re.compile(r"^STU-\d{4}$", re.IGNORECASE)
VALID_DAYS = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday"}


@mcp.tool(
    name="get_timetable",
    description="Retrieve the verified academic schedule, class times, instructors, and rooms for a given student batch and day of the week. Inputs must be a valid batch (e.g. 'CSE-A', 'CSE-B', 'AIML-A') and a weekday ('Monday' through 'Saturday'). Returns a list of structured class objects or an explicit message if no sessions are scheduled."
)
def get_timetable(batch: str, day: str) -> str:
    """
    Search mock CSV timetable for matching batch and weekday classes.
    Strictly validates input parameters and never fabricates nonexistent sessions.
    """
    clean_batch = batch.strip().upper()
    clean_day = day.strip().capitalize()

    if not clean_batch or not clean_day:
        return json.dumps({
            "status": "error",
            "message": "Both 'batch' and 'day' parameters are required."
        })

    if clean_day.lower() not in VALID_DAYS:
        return json.dumps({
            "status": "error",
            "message": f"Invalid day '{day}'. Allowed days are Monday through Saturday."
        })

    if not TIMETABLE_FILE.exists():
        return json.dumps({
            "status": "error",
            "message": "Timetable database file is missing from server."
        })

    matches: List[Dict[str, Any]] = []
    with open(TIMETABLE_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("batch", "").strip().upper() == clean_batch and \
               row.get("day", "").strip().capitalize() == clean_day:
                matches.append({
                    "slot": row.get("slot"),
                    "start_time": row.get("start_time"),
                    "end_time": row.get("end_time"),
                    "course_code": row.get("course_code"),
                    "course_name": row.get("course_name"),
                    "instructor": row.get("instructor"),
                    "room": row.get("room"),
                    "class_type": row.get("class_type")
                })

    if not matches:
        return json.dumps({
            "status": "unavailable",
            "batch": clean_batch,
            "day": clean_day,
            "message": f"Information unavailable: No classes scheduled for batch '{clean_batch}' on '{clean_day}'."
        }, indent=2)

    return json.dumps({
        "status": "success",
        "batch": clean_batch,
        "day": clean_day,
        "total_classes": len(matches),
        "classes": matches
    }, indent=2)


@mcp.tool(
    name="get_fee_status",
    description="Query tuition fee payment and reconciliation status for an enrolled student using their institutional ID. Format must strictly match 'STU-XXXX' (e.g., 'STU-1001'). Never exposes sensitive personally identifiable information (PII) such as bank accounts, national IDs, or home addresses. Returns status as 'paid', 'pending', or 'overdue'."
)
def get_fee_status(student_id: str) -> str:
    """
    Check tuition fee ledger by student ID.
    Enforces privacy by masking non-essential PII and returning only financial status.
    """
    clean_id = student_id.strip().upper()

    if not STUDENT_ID_PATTERN.match(clean_id):
        return json.dumps({
            "status": "error",
            "message": f"Invalid student ID format '{student_id}'. Expected format 'STU-XXXX' where XXXX is a 4-digit number."
        })

    if not FEES_FILE.exists():
        return json.dumps({
            "status": "error",
            "message": "Fee ledger database file is missing from server."
        })

    with open(FEES_FILE, mode="r", encoding="utf-8") as f:
        fee_db = json.load(f)

    record = fee_db.get(clean_id)
    if not record:
        return json.dumps({
            "status": "not_found",
            "student_id": clean_id,
            "message": f"Student ID '{clean_id}' was not found in the campus fee reconciliation registry."
        }, indent=2)

    return json.dumps({
        "status": "success",
        "student_id": clean_id,
        "fee_status": record.get("status"),
        "academic_year": record.get("academic_year"),
        "semester": record.get("semester"),
        "balance_due_inr": record.get("balance_due_inr"),
        "due_date": record.get("due_date", "N/A"),
        "last_payment_date": record.get("last_payment_date", "N/A")
    }, indent=2)


@mcp.resource(
    "hostel://rules",
    name="Hostel Residential Rules & Code of Conduct",
    description="Official regulatory documentation outlining Nimbus University hostel curfew, visitor policies, electrical safety guidelines, quiet hours, and disciplinary codes.",
    mime_type="text/markdown"
)
def get_hostel_rules() -> str:
    """
    Exposes the official university hostel regulations as an MCP Resource.
    Resource URI: hostel://rules
    """
    if not HOSTEL_RULES_FILE.exists():
        return "# Error\nHostel rules document not found on server."

    with open(HOSTEL_RULES_FILE, mode="r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    mcp.run(transport="stdio")
