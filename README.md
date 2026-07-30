<div align="center">

<h1>🛡️ WinstonRedGuard · WRG-11</h1>

<p><strong>Pseudonymous solo research lab for AI/LLM security &amp; OSINT tooling</strong></p>
<p><em>Working artifacts, not promises. Everything open source under MIT.</em></p>

<p>
  <img src="https://img.shields.io/badge/license-MIT-2ea043?labelColor=30363d" alt="license" />
  <img src="https://img.shields.io/badge/sigma_rules-80-1f6feb?labelColor=30363d" alt="sigma rules" />
  <img src="https://img.shields.io/badge/benign_false--positives-0-2ea043?labelColor=30363d" alt="benign false positives" />
  <img src="https://img.shields.io/badge/CodeQL_alerts-0-2ea043?labelColor=30363d" alt="CodeQL alerts" />
</p>

<p>
  <code>Python 3.12</code> · <code>Sigma</code> · <code>MCP</code> · <code>OSINT</code> · <code>MITRE ATT&amp;CK</code> · <code>Claude Code</code>
</p>

</div>

---

Solo researcher working on AI/LLM security, detection engineering, and OSINT tooling. I publish small, zero-dependency artifacts I actually use: vulnerable-by-design labs, a client-side secret scanner, Sigma detection content, and OSINT trust envelopes. Bug reports and detection rules occasionally land upstream.

### 🧪 Security labs & research

[**mcp-objauthz-lab**](https://github.com/WRG-11/mcp-objauthz-lab) &nbsp; ![last commit](https://img.shields.io/github/last-commit/WRG-11/mcp-objauthz-lab?style=flat&labelColor=30363d&color=6e7681&display_timestamp=committer&label=updated)

Vulnerable-by-design MCP server for learning object-level / cross-tenant authorization (BOLA/IDOR) bugs + a hunt checklist.

[**ai-security-toolkit**](https://github.com/WRG-11/ai-security-toolkit) &nbsp; ![last commit](https://img.shields.io/github/last-commit/WRG-11/ai-security-toolkit?style=flat&labelColor=30363d&color=6e7681&display_timestamp=committer&label=updated)

Offensive &amp; defensive AI/LLM security tools, labs, and CTF write-ups. Zero-dependency Python.

### 🔍 Scanners

[**devguard-scan**](https://github.com/WRG-11/devguard-scan) &nbsp; ![last commit](https://img.shields.io/github/last-commit/WRG-11/devguard-scan?style=flat&labelColor=30363d&color=6e7681&display_timestamp=committer&label=updated) &nbsp; · &nbsp; [**▶ live demo**](https://wrg-11.github.io/devguard-scan/)

100% client-side secret scanner. Paste code or drop files; nothing leaves your browser (zero upload).

### 📡 Detection / Sigma

[**wrg-sigma-rules**](https://github.com/WRG-11/wrg-sigma-rules) &nbsp; ![last commit](https://img.shields.io/github/last-commit/WRG-11/wrg-sigma-rules?style=flat&labelColor=30363d&color=6e7681&display_timestamp=committer&label=updated)

<!--SIGMA_RULES_START-->80<!--SIGMA_RULES_END--> sigma detection rules across 12 detection categories, 0 benign false-positives. Ships 3 MCP tools + 3 Claude Code skills.

### 🧭 OSINT & research

[**osint-trust-envelope**](https://github.com/WRG-11/osint-trust-envelope) &nbsp; ![last commit](https://img.shields.io/github/last-commit/WRG-11/osint-trust-envelope?style=flat&labelColor=30363d&color=6e7681&display_timestamp=committer&label=updated)

Per-source epistemic ceilings for OSINT results: honest verified / inferred / heuristic / unverified envelopes. Zero-dependency Python.

---

### 🛡 Security advisories

Credited reporter on published GitHub Security Advisories:

- **Pelican:** application API mounts ACL-scope bypass, CWE-862/863 ([GHSA-43h8-3896-wqv5](https://github.com/pelican-dev/panel/security/advisories/GHSA-43h8-3896-wqv5))
- **Pelican:** Filament suspend-all / unsuspend-all missing authorization ([GHSA-4wxv-r46p-w2f9](https://github.com/pelican-dev/panel/security/advisories/GHSA-4wxv-r46p-w2f9))

### 🔗 Upstream detections

Detection templates merged into projectdiscovery/nuclei-templates:

- **CVE-2026-26190** Milvus, unauthenticated metrics port ([#16333](https://github.com/projectdiscovery/nuclei-templates/pull/16333))
- **CVE-2026-25527** changedetection.io ≤ 0.52.9 ([#16346](https://github.com/projectdiscovery/nuclei-templates/pull/16346))
- **CVE-2026-33476** SiYuan ≤ v3.6.1 ([#16335](https://github.com/projectdiscovery/nuclei-templates/pull/16335))
<div align="center">

<sub><code>0 / <!--SIGMA_RULES_START-->80<!--SIGMA_RULES_END--> benign sigma false-positives</code> · <code>0 CodeQL alerts</code> · <code>MIT across the ecosystem</code> · <code>zero-dependency Python where it makes sense</code></sub>

</div>
