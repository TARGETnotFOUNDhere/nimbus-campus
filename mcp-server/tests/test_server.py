"""
Unit and integration tests for the Campus Helpdesk MCP server.
Tests:
  - Input validation (batch, day, student_id)
  - Timetable lookup (success, unavailable, error)
  - Non-hallucination guarantee
  - Fee status checking (paid, pending, overdue, not found, invalid format)
  - Resource fetching (hostel://rules)
"""

import json
import pytest
import sys
from pathlib import Path

# Add mcp-server directory to python path
SERVER_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SERVER_DIR))

from server import get_timetable, get_fee_status, get_hostel_rules

class TestTimetableTool:
    def test_valid_timetable_cse_a_monday(self):
        res_str = get_timetable("CSE-A", "Monday")
        res = json.loads(res_str)
        assert res["status"] == "success"
        assert res["batch"] == "CSE-A"
        assert res["day"] == "Monday"
        assert res["total_classes"] == 3
        # Ensure CS301 is present
        courses = [c["course_code"] for c in res["classes"]]
        assert "CS301" in courses
        assert "CS302" in courses
        assert "CS303" in courses

    def test_case_insensitivity(self):
        res_str = get_timetable("cse-b", "tuesday")
        res = json.loads(res_str)
        assert res["status"] == "success"
        assert res["batch"] == "CSE-B"
        assert res["day"] == "Tuesday"
        assert len(res["classes"]) == 1
        assert res["classes"][0]["course_code"] == "CS301"

    def test_unavailable_class_non_hallucination(self):
        # Sunday has no classes
        res_str = get_timetable("CSE-A", "Sunday")
        res = json.loads(res_str)
        # Sunday is rejected as invalid day
        assert res["status"] == "error"
        assert "Allowed days are Monday through Saturday" in res["message"]

    def test_valid_day_no_classes_scheduled(self):
        # Friday for CSE-B only has Slot-3 CS305; check Saturday (no classes)
        res_str = get_timetable("CSE-A", "Saturday")
        res = json.loads(res_str)
        assert res["status"] == "unavailable"
        assert "Information unavailable" in res["message"]

    def test_nonexistent_batch(self):
        res_str = get_timetable("CSE-Z", "Monday")
        res = json.loads(res_str)
        assert res["status"] == "unavailable"
        assert "Information unavailable" in res["message"]


class TestFeeStatusTool:
    def test_valid_fee_paid_student(self):
        res_str = get_fee_status("STU-1001")
        res = json.loads(res_str)
        assert res["status"] == "success"
        assert res["student_id"] == "STU-1001"
        assert res["fee_status"] == "paid"
        assert res["balance_due_inr"] == 0

    def test_valid_fee_pending_student(self):
        res_str = get_fee_status("STU-1002")
        res = json.loads(res_str)
        assert res["status"] == "success"
        assert res["fee_status"] == "pending"
        assert res["balance_due_inr"] == 15000

    def test_valid_fee_overdue_student(self):
        res_str = get_fee_status("STU-1003")
        res = json.loads(res_str)
        assert res["status"] == "success"
        assert res["fee_status"] == "overdue"
        assert res["balance_due_inr"] == 45000

    def test_invalid_student_id_format(self):
        res_str = get_fee_status("INVALID-ID-999")
        res = json.loads(res_str)
        assert res["status"] == "error"
        assert "Expected format 'STU-XXXX'" in res["message"]

    def test_student_not_found(self):
        res_str = get_fee_status("STU-9999")
        res = json.loads(res_str)
        assert res["status"] == "not_found"
        assert "was not found" in res["message"]

    def test_no_sensitive_pii_leaked(self):
        res_str = get_fee_status("STU-1001")
        res = json.loads(res_str)
        # Ensure sensitive PII fields are absent
        forbidden_keys = ["bank_account", "ssn", "national_id", "password", "credit_card", "phone"]
        for fk in forbidden_keys:
            assert fk not in res


class TestHostelRulesResource:
    def test_get_hostel_rules_content(self):
        content = get_hostel_rules()
        assert "Hostel Rules and Residential Code of Conduct" in content
        assert "Curfew and Biometric Timings" in content
        assert "22:00" in content
        assert "Substance Policy" in content
