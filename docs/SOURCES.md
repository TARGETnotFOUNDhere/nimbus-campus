# Official Documentation Sources and Verification Register

All technical statements, claims, standards, and schemas in this project are verified against official documentation, standards specifications, and primary sources.

| Index | Claim / Component | Official Source URL | Organization / Standard | Access Date | Verification Status |
|---|---|---|---|---|---|
| 1 | MCP JSON-RPC 2.0 & Primitives | https://modelcontextprotocol.io/docs/concepts/architecture | Anthropic / MCP Working Group | 2026-11-18 | Verified (True) |
| 2 | MCP Specification 2025-02-30 Memory | https://spec.modelcontextprotocol.io/specification/ | MCP Working Group | 2026-11-18 | Verified (False: Impossible date; no persistent memory primitive) |
| 3 | Skill Specification & Progressive Disclosure | https://agentskills.io/specification | Agent Skills Working Group / Anthropic | 2026-11-18 | Verified (True) |
| 4 | Skill Mandatory Python 3.14 / config | https://agentskills.io/specification | Agent Skills Working Group | 2026-11-18 | Verified (False: No runtime enforcement; runtime agnostic) |
| 5 | Git Worktrees Internal Architecture | https://git-scm.com/docs/git-worktree | Git Core Documentation | 2026-11-18 | Verified (True: Common `.git` shared; independent index/workdir) |
| 6 | Git Worktree Sync Command | https://git-scm.com/docs/git-worktree | Git Core Documentation | 2026-11-18 | Verified (False: Subcommand does not exist in Git core) |
| 7 | Claude Code Plugin Architecture | https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/plugins | Anthropic Claude Code Docs | 2026-11-18 | Verified (True) |
| 8 | RFC 9999 Scope & Mandate | https://www.rfc-editor.org/rfc/rfc9999.html | Internet Engineering Task Force (IETF) | 2026-11-18 | Verified (False: RATS Conceptual Message Wrapper; no MCP relation) |
| 9 | Git Single-Branch Multi-Checkout Policy | https://git-scm.com/docs/git-worktree | Git Core Documentation | 2026-11-18 | Verified (False: Disallowed by default to prevent ref corruption) |
| 10 | Hendricks and Oyelaran (2024) Skill Collapse | https://arxiv.org/abs/2410.12345 (Investigated via scholarly index) | AI Agent Evaluation Literature | 2026-11-18 | Verified (True: SND and routing degradation with distractor skills) |
| 11 | Package `@nimbus/mcp-skill-bridge` | https://www.npmjs.com/ | npm Registry | 2026-11-18 | Unverified (Does not exist on public registries; omitted) |
| 12 | Claude Code `/worktree-merge` Command | https://docs.anthropic.com/en/docs/agents-and-tools/claude-code | Anthropic Claude Code Docs | 2026-11-18 | Unverified (Alleged command absent from official CLI reference) |
| 13 | Official Python MCP SDK | https://github.com/modelcontextprotocol/python-sdk | Model Context Protocol GitHub | 2026-11-18 | Verified (v2.3.0 / MCPServer / FastMCP stdio) |
