# WinstonRedGuard (WRG-11)

Solo security researcher. I report authorization bugs in open-source software and build AI/LLM security tooling and detection rules.

## Published advisories

Credited reporter on four published GitHub Security Advisories:

| Advisory | Finding | Weakness | Severity | Published |
| --- | --- | --- | --- | --- |
| [GHSA-wc96-jm46-37hh](https://github.com/OneUptime/oneuptime/security/advisories/GHSA-wc96-jm46-37hh) | OneUptime: Verification-code resend lacks an ownership check | CWE-862 | Low | Aug 2026 |
| [GHSA-9xwv-p7r5-5h5p](https://github.com/Jexactyl/Jexactyl/security/advisories/GHSA-9xwv-p7r5-5h5p)<br>CVE-2026-107854 | Jexactyl: Free-billing flow lacks an ownership check | CWE-639 | Medium | Jul 2026 |
| [GHSA-43h8-3896-wqv5](https://github.com/pelican-dev/panel/security/advisories/GHSA-43h8-3896-wqv5) | Pelican: Application API mounts bypass the ACL scope | CWE-862 | Medium | Jul 2026 |
| [GHSA-4wxv-r46p-w2f9](https://github.com/pelican-dev/panel/security/advisories/GHSA-4wxv-r46p-w2f9) | Pelican: Bulk suspend and unsuspend actions lack authorization | CWE-862 | Medium | Jul 2026 |

The OneUptime finding is in incoming call numbers, the sibling channel that the CVE-2026-30959 fix sweep left uncovered.

Vendor security acknowledgement: zn (local security layer for coding agents), SEC-2026-01, a high-severity control-plane authorization gap where missing function-level checks let non-admin tenant keys modify policy or consensus state. Credited on the [usezn.com Security Hall of Fame](https://usezn.com/security/).

## Merged upstream

Detection templates merged into projectdiscovery/nuclei-templates:

| Pull request | CVE | Target | Merged |
| --- | --- | --- | --- |
| [#16345](https://github.com/projectdiscovery/nuclei-templates/pull/16345) | CVE-2026-31831 | Tautulli ≤ 2.16.1, unauthenticated path traversal | Jul 2026 |
| [#16335](https://github.com/projectdiscovery/nuclei-templates/pull/16335) | CVE-2026-33476 | SiYuan ≤ v3.6.1 | Jun 2026 |
| [#16333](https://github.com/projectdiscovery/nuclei-templates/pull/16333) | CVE-2026-26190 | Milvus, unauthenticated metrics port | Jun 2026 |
| [#16346](https://github.com/projectdiscovery/nuclei-templates/pull/16346) | CVE-2026-25527 | changedetection.io ≤ 0.52.9 | Jun 2026 |

## Open source

The pinned repositories below include [wrg-sigma-rules](https://github.com/WRG-11/wrg-sigma-rules) (<!--SIGMA_RULES_START-->294<!--SIGMA_RULES_END--> Sigma rules across <!--SIGMA_TACTICS_START-->16<!--SIGMA_TACTICS_END--> ATT&CK tactic categories, none marked `stable`) and [mcp-objauthz-lab](https://github.com/WRG-11/mcp-objauthz-lab), a vulnerable-by-design MCP server for learning object-level and cross-tenant authorization bugs (BOLA/IDOR). desktop-automation-mcp is Apache-2.0; the others are MIT.
