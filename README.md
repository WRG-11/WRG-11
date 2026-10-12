# WinstonRedGuard (WRG-11)

Solo security researcher. I report authorization bugs in open-source software and build AI/LLM security tooling and detection rules.

## Published advisories

Credited reporter on four published GitHub Security Advisories:

| Advisory | Project | Issue | Weakness | Severity | Published |
| --- | --- | --- | --- | --- | --- |
| [GHSA-43h8-3896-wqv5](https://github.com/pelican-dev/panel/security/advisories/GHSA-43h8-3896-wqv5) | Pelican, game server management panel | Application API mounts bypass the ACL scope | CWE-862 | Medium | 2026-07-06 |
| [GHSA-4wxv-r46p-w2f9](https://github.com/pelican-dev/panel/security/advisories/GHSA-4wxv-r46p-w2f9) | Pelican | Filament suspend-all / unsuspend-all actions lack authorization | CWE-862 | Medium | 2026-07-06 |
| [GHSA-9xwv-p7r5-5h5p](https://github.com/Jexactyl/Jexactyl/security/advisories/GHSA-9xwv-p7r5-5h5p) | Jexactyl, game management panel with billing | Free-billing flow lacks an ownership check | CWE-639, CVE-2026-107854 | Medium | 2026-07-28 |
| [GHSA-wc96-jm46-37hh](https://github.com/OneUptime/oneuptime/security/advisories/GHSA-wc96-jm46-37hh) | OneUptime, monitoring and observability platform | Resend-verification-code for incoming call numbers lacks an ownership check, the sibling channel the CVE-2026-30959 fix sweep left uncovered | CWE-862 | Low | 2026-08-05 |

Vendor security acknowledgement:

- zn (local security layer for coding agents), SEC-2026-01: high-severity control-plane authorization gap on policy and consensus handlers, where non-admin tenant keys could modify policy or consensus state through missing function-level checks. Credited on the [usezn.com Security Hall of Fame](https://usezn.com/security/).

## Merged upstream

Detection templates merged into projectdiscovery/nuclei-templates:

| Pull request | CVE | Target | Merged |
| --- | --- | --- | --- |
| [#16333](https://github.com/projectdiscovery/nuclei-templates/pull/16333) | CVE-2026-26190 | Milvus, unauthenticated metrics port | 2026-06-08 |
| [#16346](https://github.com/projectdiscovery/nuclei-templates/pull/16346) | CVE-2026-25527 | changedetection.io ≤ 0.52.9 | 2026-06-08 |
| [#16335](https://github.com/projectdiscovery/nuclei-templates/pull/16335) | CVE-2026-33476 | SiYuan ≤ v3.6.1 | 2026-06-11 |
| [#16345](https://github.com/projectdiscovery/nuclei-templates/pull/16345) | CVE-2026-31831 | Tautulli ≤ 2.16.1, unauthenticated path traversal | 2026-07-23 |

## Projects

- [mcp-objauthz-lab](https://github.com/WRG-11/mcp-objauthz-lab): vulnerable-by-design MCP server for learning object-level and cross-tenant authorization bugs (BOLA/IDOR), with a hunt checklist.
- [wrg-sigma-rules](https://github.com/WRG-11/wrg-sigma-rules): <!--SIGMA_RULES_START-->294<!--SIGMA_RULES_END--> Sigma detection rules across <!--SIGMA_TACTICS_START-->16<!--SIGMA_TACTICS_END--> ATT&CK tactic categories, none marked `stable`, plus an MCP server that drafts, validates and converts rules.
- [ai-security-toolkit](https://github.com/WRG-11/ai-security-toolkit): AI/LLM security tools, labs and CTF write-ups. The core tools use only the Python standard library.
- [devguard-scan](https://github.com/WRG-11/devguard-scan): secret scanner that runs entirely in the browser; nothing is uploaded. [Live demo](https://wrg-11.github.io/devguard-scan/).
- [osint-trust-envelope](https://github.com/WRG-11/osint-trust-envelope): wraps an OSINT lookup in a trust envelope (verified / inferred / heuristic / unverified) capped by what the source type can support.
- [desktop-automation-mcp](https://github.com/WRG-11/desktop-automation-mcp): deny-by-default MCP server for operating specific Windows application windows. Each action class is a separate permission.

desktop-automation-mcp is Apache-2.0; the other five are MIT.
