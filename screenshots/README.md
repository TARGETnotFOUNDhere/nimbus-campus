# Project Evidence & Test Execution Artifacts

This directory contains execution evidence, verified test logs, and terminal transcripts validating the Nimbus Campus Helpdesk agent toolchain.

## Available Evidence Logs

1. **Worktree Lifecycle & Merge Graph**:
   - Path: [`worktrees/evidence/worktree-log.txt`](../worktrees/evidence/worktree-log.txt)
   - Contains verbatim output for `git worktree add`, `git worktree list`, intentional merge conflict generation, manual conflict resolution, `git log --graph --oneline --all`, and `git worktree remove` / `git worktree prune`.

2. **Automated Unit & Integration Test Suite**:
   - Tool: `pytest`
   - Command: `pytest mcp-server/tests/test_server.py -v`
   - Result: 12 tests passed, 0 failed.
   - Status: Verified.

3. **MCP Stdio JSON-RPC Protocol Interoperability**:
   - Verification script: Direct stdio pipe test of `initialize`, `notifications/initialized`, `tools/list`, and `tools/call`.
   - Result: Valid JSON-RPC 2.0 frames with capability negotiation and strict parameter validation.

4. **Timetable CSV Integrity**:
   - Tool: `python skills/timetable-helper/scripts/validate_timetable.py`
   - Result: 20 records validated with zero schema violations, overlaps, or room double-bookings.
