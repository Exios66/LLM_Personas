# Agent Tools

Tool specifications and references for agent-invokable tools. Use this directory to document which tools agents may call (APIs, scripts, MCP tools, CLI commands) and how they should be used.

## Purpose

- **Tool specs** describe name, purpose, inputs, outputs, and usage constraints.
- **References** can point to implementation locations (e.g. `litigation/run.py`, MCP server configs) so agents and operators know where behavior lives.

## Naming

- Use kebab-case: `litigation-runner.md`, `state-read.md`.
- One tool (or logical tool group) per file.

## Relation to Repo

- **Litigation runner:** `litigation/run.py` — invokes LLM with full framework prompt; not a “tool” in the narrow sense but an agent entry point.
- **MCP / Cursor tools:** Document here if agents are expected to use specific MCP tools or Cursor capabilities so that prompts can reference them by name.
