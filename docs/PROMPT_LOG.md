# AI Interaction and Verification Prompt Log

This document records the exact interactions, prompt invocations, verification checkpoints, and human audit corrections executed during the development of the Nimbus Campus Helpdesk agent toolchain.

---

### Entry 1: Verification of MCP Specifications and Claim Audit

- **Date:** 2026-11-18
- **AI Tool Used:** Gemini 3.8 Flash (Low) / Antigravity Assistant
- **Exact Prompt:**
  > *"Analyze the following claim for technical accuracy: 'MCP specification revision 2025-02-30 mandates a Persistent Memory Primitive.' Verify against official MCP specifications."*
- **Summary of AI Output:**
  The model flagged that the date `2025-02-30` is mathematically and calendar-wise impossible (February never has 30 days). Furthermore, review of the official Model Context Protocol architecture (https://modelcontextprotocol.io/) shows that MCP defines three core primitives: **Tools**, **Resources**, and **Prompts**. There is no official "Persistent Memory Primitive" in the specification; memory mechanisms in agentic frameworks are typically application-level abstractions (such as local JSON/SQLite or custom vector databases) rather than core protocol primitives.
- **Official Documentation Used for Verification:**
  - MCP Architecture Documentation: https://modelcontextprotocol.io/docs/concepts/architecture
  - MCP Specification Revisions: https://spec.modelcontextprotocol.io/specification/
- **Incorrect or Unverifiable Information Detected:**
  The statement contained an invalid date (Feb 30) and an invented protocol primitive ("Persistent Memory Primitive").
- **What I Corrected or Rejected and Why:**
  Marked Claim 2 as **False**. Formally explained the factual primitives of MCP (Tools, Resources, Prompts) and noted the calendar impossibility of the revision timestamp.

---

### Entry 2: Evaluation of RFC 9999 and Cryptographic Signatures

- **Date:** 2026-11-18
- **AI Tool Used:** Gemini 3.8 Flash (Low) / Antigravity Assistant
- **Exact Prompt:**
  > *"Check IETF standards index for RFC 9999. Does it mandate Ed25519 signatures for stdio MCP servers?"*
- **Summary of AI Output:**
  The model conducted a search against official IETF indices and located RFC 9999, published in July 2026, titled *"Remote ATtestation procedureS (RATS) Conceptual Message Wrapper (CMW)"* by H. Birkholz et al. The document focuses entirely on attestation payloads, evidence appraisal, and endorsement wrapping within the RATS architecture. It has no affiliation with the Model Context Protocol, Anthropic, or stdio process transports.
- **Official Documentation Used for Verification:**
  - IETF RFC Editor / Datatracker: https://www.rfc-editor.org/rfc/rfc9999.html
  - IETF RATS Working Group: https://datatracker.ietf.org/wg/rats/documents/
- **Incorrect or Unverifiable Information Detected:**
  Claiming that RFC 9999 pertains to MCP stdio signatures is completely fabricated.
- **What I Corrected or Rejected and Why:**
  Marked Claim 8 as **False**. Documented the genuine scope of RFC 9999 (RATS CMW) to demonstrate strict factual verification.

---

### Entry 3: Investigation of Alleged Dependency `@nimbus/mcp-skill-bridge`

- **Date:** 2026-11-18
- **AI Tool Used:** Gemini 3.8 Flash (Low) / Antigravity Assistant
- **Exact Prompt:**
  > *"Investigate whether package '@nimbus/mcp-skill-bridge' version 2.3 exists on npm or PyPI. Provide installation instructions if verified."*
- **Summary of AI Output:**
  A comprehensive registry search of npmjs.com and pypi.org returned no matching package named `@nimbus/mcp-skill-bridge`. The search revealed related tools (such as `@nimbus-dev/mcp` and `@mcp-s/skills`), but no package under the exact `@nimbus/mcp-skill-bridge` scope exists.
- **Official Documentation Used for Verification:**
  - npm Registry: https://www.npmjs.com/search?q=%40nimbus%2Fmcp-skill-bridge
  - Python Package Index: https://pypi.org/
- **Incorrect or Unverifiable Information Detected:**
  The package name `@nimbus/mcp-skill-bridge` v2.3 appears to be a hallucinated or unreleased internal dependency.
- **What I Corrected or Rejected and Why:**
  Explicitly classified the package as **Unverified** in accordance with assignment instructions. Did not install or depend on this phantom package; instead, built the server purely with the official, verified `mcp` SDK (`mcp>=1.3.0`).

---

### Entry 4: Audit of Git Worktree Commands and `/worktree-merge`

- **Date:** 2026-11-18
- **AI Tool Used:** Gemini 3.8 Flash (Low) / Antigravity Assistant
- **Exact Prompt:**
  > *"Verify whether 'git worktree sync --all' is a valid Git core command, and whether Claude Code provides a built-in slash command '/worktree-merge'."*
- **Summary of AI Output:**
  Evaluation of `git help worktree` (Git core manual) reveals valid subcommands: `add`, `list`, `lock`, `move`, `prune`, `remove`, `repair`, `unlock`. There is no `sync` subcommand in core Git. Furthermore, checking official Claude Code documentation (https://docs.anthropic.com/en/docs/agents-and-tools/claude-code) showed no built-in `/worktree-merge` slash command; worktree merging is handled through standard Git commands (`git merge`, `git checkout`) or custom user-defined scripts.
- **Official Documentation Used for Verification:**
  - Official Git SCM Reference: https://git-scm.com/docs/git-worktree
  - Claude Code CLI Reference: https://docs.anthropic.com/en/docs/agents-and-tools/claude-code
- **Incorrect or Unverifiable Information Detected:**
  `git worktree sync --all` and `/worktree-merge` are non-existent built-in commands.
- **What I Corrected or Rejected and Why:**
  Marked Claim 6 as **False**. Labelled Claude Code `/worktree-merge` as **Unverified/Non-existent** in the core CLI. Demonstrated manual Git conflict resolution and history graphing instead of relying on fictitious commands.

---

### Entry 5: Python MCP SDK 2.x Architecture Migration and Compatibility

- **Date:** 2026-11-18
- **AI Tool Used:** Gemini 3.8 Flash (Low) / Antigravity Assistant
- **Exact Prompt:**
  > *"When executing pytest on server.py, the test failed with: 'ModuleNotFoundError: No module named mcp.server.fastmcp. This is mcp 2.x, where FastMCP was renamed to MCPServer'. How should server.py be updated to support modern MCP SDK without breaking compatibility?"*
- **Summary of AI Output:**
  The model observed that the environment has `mcp==2.3.0` installed. In MCP Python SDK v2.x, `FastMCP` was migrated to `MCPServer` (`from mcp.server.mcpserver import MCPServer`). The proposed fix was to employ a defensive dual-import try-except block that instantiates `MCPServer` if available, and gracefully falls back to `FastMCP` if deployed in an older v1.x environment.
- **Official Documentation Used for Verification:**
  - MCP Python SDK Migration Guide: https://py.sdk.modelcontextprotocol.io/v2/migration/#fastmcp-renamed-to-mcpserver
- **Incorrect or Unverifiable Information Detected:**
  Legacy sample code still using `from mcp.server.fastmcp import FastMCP` directly fails on MCP SDK 2.0+.
- **What I Corrected or Rejected and Why:**
  Updated `mcp-server/server.py` with defensive compatibility logic. Re-ran `pytest`, achieving 100% test pass rate (12/12 tests passing).
