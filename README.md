# Nimbus Labs – Campus Helpdesk Agent

An enterprise-grade, verifiable AI-agent toolchain built for university academic assistance, fee status reconciliation, and residential code of conduct guidance. Developed in compliance with the **Model Context Protocol (MCP)** specification, **Agent Skills** standard, and **Claude Code plugin** architecture.

---

## Project Structure

```
nimbus-campus-helpdesk/
│
├── README.md                                  # Execution instructions and architecture guide
├── docs/
│   ├── REPORT.md                              # Comprehensive technical report and claim audit
│   ├── REFLECTION.md                          # Architectural reflection (Skills vs. MCP vs. Worktrees)
│   ├── PROMPT_LOG.md                          # 5-entry empirical interaction and verification log
│   ├── SOURCES.md                             # Source registry with official URLs & access dates
│   └── Nimbus_Campus_Helpdesk_Report.pdf      # Formatted academic submission PDF
│
├── skills/
│   └── timetable-helper/                      # Reusable Agent Skill
│       ├── SKILL.md                           # Skill entrypoint with progressive disclosure
│       ├── references/
│       │   ├── csv-dictionary.md              # Data dictionary and table schema
│       │   └── edge-cases.md                  # Edge case & non-hallucination protocols
│       ├── scripts/
│       │   └── validate_timetable.py          # Chronological & collision validator
│       └── data/
│           └── timetable.csv                  # Mock academic schedule (20 records)
│
├── plugins/
│   └── campus-helpdesk/                       # Claude Code Plugin package
│       ├── .claude-plugin/
│       │   └── plugin.json                    # Plugin manifest
│       ├── commands/
│       │   └── timetable.md                   # /timetable slash command definition
│       ├── skills/
│       │   └── timetable-helper/              # Packaged skill bundle
│       ├── hooks/
│       │   ├── hooks.json                     # PreToolExecution lifecycle hook configuration
│       │   ├── protect-data.sh                # Directory immutability enforcement script
│       │   └── CONFIG.md                      # Resolved path configuration
│       └── .mcp.json                          # MCP server configuration
│
├── marketplace/
│   └── marketplace.json                       # Plugin marketplace registration
│
├── mcp-server/                                # Official Python MCP Server
│   ├── server.py                              # MCP server implementation (stdio transport)
│   ├── requirements.txt                       # Python dependencies
│   ├── README.md                              # Standalone server documentation
│   ├── data/
│   │   ├── timetable.csv                      # Class schedule dataset
│   │   ├── fees.json                          # Tuition fee reconciliation ledger
│   │   └── hostel-rules.md                    # Hostel residential rules document
│   └── tests/
│       └── test_server.py                     # Pytest suite (12 test cases)
│
├── worktrees/
│   └── evidence/
│       └── worktree-log.txt                   # Verbatim Git worktree lifecycle & conflict log
│
└── screenshots/
    └── README.md                              # Test transcripts and execution verification
```

---

## Quickstart & Execution Instructions

### 1. Prerequisites
- Python 3.10+ (tested on Python 3.14)
- Git 2.30+
- Virtual environment tool (`venv`)

### 2. Setup Virtual Environment
```bash
# Navigate to project root
cd nimbus-campus-helpdesk

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r mcp-server/requirements.txt
```

### 3. Run Automated Tests
```bash
# Run MCP server unit tests
pytest mcp-server/tests/test_server.py -v

# Run Timetable CSV validator
python skills/timetable-helper/scripts/validate_timetable.py
```

### 4. Execute the MCP Server
```bash
# Start MCP server over stdio
python mcp-server/server.py
```

### 5. Inspecting with MCP Inspector
```bash
npx @modelcontextprotocol/inspector python mcp-server/server.py
```

### 6. Test Data Protection Hook
```bash
# Attempt to write to protected data directory (should exit with error 1)
bash plugins/campus-helpdesk/hooks/protect-data.sh "skills/timetable-helper/data/timetable.csv"
```

---

## Assignment Parts Summary

| Part | Component | Description | Key Artifacts |
|---|---|---|---|
| **Part A** | Claim Audit | 10 technical statements fact-checked against official documentation. | [`docs/REPORT.md`](docs/REPORT.md) |
| **Part B** | Skill Design | `timetable-helper` skill with progressive disclosure and zero hallucination. | [`skills/timetable-helper/`](skills/timetable-helper/) |
| **Part C** | Plugin Package | Claude Code `campus-helpdesk` plugin, slash command, hooks, and threat model. | [`plugins/campus-helpdesk/`](plugins/campus-helpdesk/) |
| **Part D** | MCP Server | Python MCP SDK server exposing 2 tools, 1 resource, and 12 unit tests. | [`mcp-server/`](mcp-server/) |
| **Part E** | Git Worktrees | 3 branches, 3 worktrees, merge conflict creation, manual resolution, and graph. | [`worktrees/evidence/worktree-log.txt`](worktrees/evidence/worktree-log.txt) |
| **Part F** | Reflection & Logs | 300-word architectural reflection and 5-entry prompt log. | [`docs/REFLECTION.md`](docs/REFLECTION.md), [`docs/PROMPT_LOG.md`](docs/PROMPT_LOG.md) |

---

## Verification & Unverified Claims Statement
- **`@nimbus/mcp-skill-bridge`**: Unverified. Checked against npm and PyPI registries; omitted from codebase.
- **Claude Code `/worktree-merge`**: Unverified. Checked against Anthropic documentation; Git merge operations executed via standard Git CLI.
- **RFC 9999**: Verified as RATS Conceptual Message Wrapper (CMW); statement regarding Ed25519 stdio signatures audited as False.
