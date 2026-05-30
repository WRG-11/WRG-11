## WinstonRedGuard (WRG-11)

Open-source AI/LLM security tooling — threat detection, monorepo infrastructure, and AI agent scaffolding.

### Published Packages

| Package | What it does |
|---------|-------------|
| [wrg-mcp-server](https://pypi.org/project/wrg-mcp-server/) | MCP server exposing 60+ tools to Claude and AI agents |
| [wrg-devguard](https://pypi.org/project/wrg-devguard/) | Security scanner: secrets, crypto, credentials, policy gates |
| [instinct-mcp](https://pypi.org/project/instinct-mcp/) | Pattern learning engine with MCP integration |
| [wrg-rule-lab](https://pypi.org/project/wrg-rule-lab/) | Declarative rule engine with conflict detection |

### Live

- [wrg-mcp-server](https://registry.modelcontextprotocol.io/v0/servers?search=wrg-mcp-server) on MCP Registry
- [devguard-scan](https://wrg-11.github.io/devguard-scan/) — browser-based secret scanner (zero upload)

### Focus Areas

- **AI/LLM Security** &mdash; prompt injection defense, agent safety, red teaming
- **Monorepo Governance** &mdash; automated quality gates, coverage ratchets, registry consistency
- **OSINT & Research** &mdash; deterministic decision engine with multiple data-source adapters, zero LLM dependency
- **Developer Experience** &mdash; MCP servers, CLI tools, Electron desktop apps

### Tech Stack

`Python` `FastAPI` `LangGraph` `MCP` `Playwright` `Docker` `GitHub Actions` `Electron`

### Stats

<!-- STATS:START -->
- 36 active apps in registry, 2 candidate, 45 archived (83 total in monorepo)
- 4 PyPI packages, 1 MCP Registry entry
- 585 test files, 11,000+ tests collected
- 60% minimum coverage floor per app (per-app ratchets enforced)
- CodeQL scanning active across all public repos
<!-- STATS:END -->
