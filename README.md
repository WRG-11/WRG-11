<div align="center">

<img src="assets/banner.svg" width="100%" alt="WinstonRedGuard · WRG-11 — AI/LLM security, OSINT tooling, detection engineering" />

<p><strong>Pseudonymous solo research lab — AI/LLM security &amp; OSINT tooling</strong></p>
<p><em>Working artifacts, not promises. Everything open source under MIT.</em></p>

<p>
  <img src="https://img.shields.io/badge/license-MIT-2ea043?labelColor=30363d" alt="license" />
  <img src="https://img.shields.io/badge/sigma_rules-68-1f6feb?labelColor=30363d" alt="sigma rules" />
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

Offensive &amp; defensive AI/LLM security tools, labs, and CTF write-ups — zero-dependency Python.

### 🔍 Scanners

[**devguard-scan**](https://github.com/WRG-11/devguard-scan) &nbsp; ![last commit](https://img.shields.io/github/last-commit/WRG-11/devguard-scan?style=flat&labelColor=30363d&color=6e7681&display_timestamp=committer&label=updated) &nbsp; · &nbsp; [**▶ live demo**](https://wrg-11.github.io/devguard-scan/)

100% client-side secret scanner — paste code or drop files, nothing leaves your browser (zero upload).

<img src="assets/devguard-scan-demo.png" width="100%" alt="devguard-scan in-browser — 5 secrets flagged, values [REDACTED], 0-byte upload" />

### 📡 Detection / Sigma

[**wrg-sigma-rules**](https://github.com/WRG-11/wrg-sigma-rules) &nbsp; ![last commit](https://img.shields.io/github/last-commit/WRG-11/wrg-sigma-rules?style=flat&labelColor=30363d&color=6e7681&display_timestamp=committer&label=updated)

<!--SIGMA_RULES_START-->68<!--SIGMA_RULES_END--> sigma detection rules across 11 MITRE ATT&CK tactic categories — 0 benign false-positives; ships 3 MCP tools + 3 Claude Code skills.

### 🧭 OSINT & research

[**osint-trust-envelope**](https://github.com/WRG-11/osint-trust-envelope) &nbsp; ![last commit](https://img.shields.io/github/last-commit/WRG-11/osint-trust-envelope?style=flat&labelColor=30363d&color=6e7681&display_timestamp=committer&label=updated)

Per-source epistemic ceilings for OSINT results — honest verified / inferred / heuristic / unverified envelopes; zero-dependency Python.

---

### 🔗 Upstream contributions

Detection content merged into community projects:

- [**nuclei-templates #16333**](https://github.com/projectdiscovery/nuclei-templates/pull/16333) — Milvus CVE-2026-26190 detection template
- [**nuclei-templates #16346**](https://github.com/projectdiscovery/nuclei-templates/pull/16346) — changedetection.io CVE-2026-25527 detection template

---

<div align="center">

<sub><code>0 / <!--SIGMA_RULES_START-->68<!--SIGMA_RULES_END--> benign sigma false-positives</code> · <code>0 CodeQL alerts</code> · <code>MIT across the ecosystem</code> · <code>zero-dependency Python where it makes sense</code></sub>

</div>
