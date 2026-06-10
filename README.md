# WinstonRedGuard (WRG-11)

WRG-11 is a pseudonymous solo research lab working on AI/LLM security and OSINT tooling — Sigma detection rules, MCP security research, scanners, and agent tooling, published as working artifacts rather than promises. Everything is open source under MIT.

## Security labs & research

| Project | What it does |
|---------|--------------|
| [mcp-objauthz-lab](https://github.com/WRG-11/mcp-objauthz-lab) ⭐ | Vulnerable-by-design MCP server for learning object-level / cross-tenant authorization (BOLA/IDOR) bugs + a hunt checklist |
| [ai-security-toolkit](https://github.com/WRG-11/ai-security-toolkit) | Offensive & defensive AI/LLM security tools, labs, CTF writeups, and research — zero-dependency Python |

## Scanners

| Project | What it does |
|---------|--------------|
| [wrg-devguard](https://pypi.org/project/wrg-devguard/) | Pluggable code-security scanner: secrets, credentials, crypto policy — CLI + GitHub Action |
| [devguard-scan](https://github.com/WRG-11/devguard-scan) | 100% client-side secret scanner (zero upload) — browser port of the wrg-devguard engine |

## Detection / Sigma

| Project | What it does |
|---------|--------------|
| [wrg-sigma-rules](https://github.com/WRG-11/wrg-sigma-rules) | 68 sigma detection rules across 11 MITRE ATT&CK tactic categories — 0 benign false-positives; ships 3 MCP tools + 3 Claude Code skills |

## MCP & agent tooling

| Project | What it does |
|---------|--------------|
| [wrg-mcp-server](https://pypi.org/project/wrg-mcp-server/) | MCP server exposing WRG tools (detection, research, OSINT, threat-intel) to Claude and AI agents |
| [instinct](https://pypi.org/project/instinct-mcp/) | Self-learning memory for AI coding agents — MCP server |
| [wrg-skills](https://github.com/WRG-11/wrg-skills) | Claude Code skills — headline `mcp-audit` with five documented real-world MCP audits |
| [wrg-rule-lab](https://pypi.org/project/wrg-rule-lab/) | Deterministic rule evaluation engine — local-first, JSON DSL, batch + diff + simulate |

## OSINT & research

| Project | What it does |
|---------|--------------|
| [osint-trust-envelope](https://github.com/WRG-11/osint-trust-envelope) | Per-source epistemic ceilings for OSINT results — honest verified / inferred / heuristic / unverified envelopes; zero-dependency Python |
| [arastirma-ussu](https://github.com/WRG-11/arastirma-ussu) | Local-first AI research assistant — 5-layer stack with memory, web search, document analysis (Ollama + Qdrant) |

## Live

- [devguard-scan](https://wrg-11.github.io/devguard-scan/) — 100% client-side secret scanner (zero upload)
- [wrg-mcp-server](https://registry.modelcontextprotocol.io/v0/servers?search=wrg-mcp-server) on the MCP Registry

## Quality

`0 / 68 sigma false-positives` · `0 CodeQL alerts` · `MIT across the ecosystem` · zero-dependency Python where it makes sense

[Portfolio →](https://wrg-11.github.io/wrg-portfolio/)
