# Architectural Reflection: AI-Agent Toolchain Engineering

**Student Name:** Nimbus Student  
**Degree Program:** B.Tech Computer Science & Engineering  
**Project:** Nimbus Labs – Campus Helpdesk Agent  
**Date:** November 18, 2026  

---

## 1. Problem Boundaries: Skills, Plugins, MCP, and Git Worktrees

Modern AI-assisted software engineering relies on distinct architectural abstractions that solve fundamentally different problems:

- **Skills (`SKILL.md`)** solve instructional specialization and progressive disclosure. Rather than overloading an agent's static context, skills provide on-demand domain workflows dynamically loaded when semantic intent matches.
- **Plugins (`plugin.json`)** solve packaging, distribution, and lifecycle management. A plugin bundles commands, hooks, skills, and MCP configurations into an installable, versioned unit.
- **Model Context Protocol (MCP)** solves standardized runtime connectivity. Adhering to JSON-RPC 2.0 over stdio/SSE, it exposes typed tools, resources, and prompts under protocol capability negotiation.
- **Git Worktrees** solve parallel workspace isolation. They allow concurrent tasks or subagents to mutate independent directories simultaneously without branch switching, sharing the underlying `.git` object store.

## 2. Decision Framework: Skill vs. MCP Tool Selection

The choice between a Skill and an MCP tool depends on whether the task demands **procedural reasoning** or **deterministic execution**:

- **Select a Skill** when the task involves multi-step guidance, conversational heuristics, natural language synthesis, prompt specialization, or navigating files. Skills operate within the LLM's cognitive space to steer planning.
- **Select an MCP Tool** when the task requires guaranteed deterministic logic, exact calculation, file/database I/O, or credential-bounded network requests. Tools execute externally, eliminating hallucinations from data retrieval.

For our Helpdesk, querying schedules uses an MCP tool (`get_timetable`) to ensure zero class hallucination, while the `timetable-helper` Skill directs conversational tone and missing parameter handling.

## 3. Delegation Boundaries: Work Never Delegated Without Human Review

Autonomous AI agents excel at retrieval and boilerplate, but several critical domains must **never** be delegated without human verification:

1. **Production Database Mutations & Migrations**: Schema alterations or destructive writes risk irrecoverable institutional data loss.
2. **Security & Cryptographic Configurations**: Auth policies, firewall rules, and encryption boundaries require formal threat modeling; subtle prompt misunderstandings cause critical exploits.
3. **Cross-Branch Git Merge Resolutions**: Agents resolve textual syntax conflicts locally but miss holistic systemic invariants across feature branches.
4. **Financial Reconciliation & Compliance**: Altering student fees or medical records carries legal liability; AI outputs must remain strictly advisory.
