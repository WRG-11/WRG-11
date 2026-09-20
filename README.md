<div align="center">

<h1>🛡️ WinstonRedGuard · WRG-11</h1>

<p><strong>Pseudonymous solo research lab for AI/LLM security, detection engineering &amp; OSINT tooling</strong></p>
<p><em>Working artifacts, not promises. The five featured project repositories are MIT-licensed.</em></p>

<p>
  <img src="https://img.shields.io/badge/featured_projects-MIT-2ea043?labelColor=30363d" alt="featured projects are MIT-licensed" />
  <img src="https://img.shields.io/badge/sigma_rules-296-1f6feb?labelColor=30363d" alt="sigma rules" />
</p>

<p>
  <code>Python 3.12</code> · <code>Sigma</code> · <code>MCP</code> · <code>OSINT</code> · <code>MITRE ATT&amp;CK</code> · <code>Claude Code</code>
</p>

</div>

---

Solo researcher working on AI/LLM security, detection engineering, and OSINT tooling. I publish small, security-focused open-source artifacts I actually use: vulnerable-by-design labs, a client-side secret scanner, Sigma detection content, OSINT trust envelopes, and a deny-by-default desktop-automation MCP server. Several core tools are standard-library-only. Bug reports and detection rules occasionally land upstream.

### 🧪 Security labs & research

[**mcp-objauthz-lab**](https://github.com/WRG-11/mcp-objauthz-lab) &nbsp; ![updated](https://img.shields.io/github/last-commit/WRG-11/mcp-objauthz-lab?style=flat&labelColor=30363d&color=6e7681&display_timestamp=committer&label=updated)

Vulnerable-by-design MCP server for learning object-level / cross-tenant authorization (BOLA/IDOR) bugs, paired with a hunt checklist and CI that keeps the vulnerable-fixture set honest.

[**ai-security-toolkit**](https://github.com/WRG-11/ai-security-toolkit) &nbsp; ![updated](https://img.shields.io/github/last-commit/WRG-11/ai-security-toolkit?style=flat&labelColor=30363d&color=6e7681&display_timestamp=committer&label=updated)

Offensive &amp; defensive AI/LLM security tools, labs, and CTF write-ups. Zero-dependency Python.

### 🔍 Scanners

[**devguard-scan**](https://github.com/WRG-11/devguard-scan) &nbsp; ![updated](https://img.shields.io/github/last-commit/WRG-11/devguard-scan?style=flat&labelColor=30363d&color=6e7681&display_timestamp=committer&label=updated) &nbsp; · &nbsp; [**▶ live demo**](https://wrg-11.github.io/devguard-scan/)

100% client-side secret scanner. Paste code or drop files; nothing leaves your browser (zero upload).

### 📡 Detection / Sigma

[**wrg-sigma-rules**](https://github.com/WRG-11/wrg-sigma-rules) &nbsp; ![updated](https://img.shields.io/github/last-commit/WRG-11/wrg-sigma-rules?style=flat&labelColor=30363d&color=6e7681&display_timestamp=committer&label=updated)

<!--SIGMA_RULES_START-->296<!--SIGMA_RULES_END--> Sigma detection rules across <!--SIGMA_TACTICS_START-->14<!--SIGMA_TACTICS_END--> ATT&CK tactic categories, none marked `stable` — sigma's `status:` field used literally rather than aspirationally. Ships 3 MCP tools + 3 Claude Code skills.

### 🧭 OSINT & research

[**osint-trust-envelope**](https://github.com/WRG-11/osint-trust-envelope) &nbsp; ![updated](https://img.shields.io/github/last-commit/WRG-11/osint-trust-envelope?style=flat&labelColor=30363d&color=6e7681&display_timestamp=committer&label=updated)

Per-source epistemic ceilings for OSINT results: honest verified / inferred / heuristic / unverified envelopes. Zero-dependency Python.

### 🖥️ Desktop automation (MCP)

[**desktop-automation-mcp**](https://github.com/WRG-11/desktop-automation-mcp) &nbsp; `Apache-2.0` &nbsp; ![updated](https://img.shields.io/github/last-commit/WRG-11/desktop-automation-mcp?style=flat&labelColor=30363d&color=6e7681&display_timestamp=committer&label=updated)

Deny-by-default, per-action-gated Windows window MCP server. Every capability (observe, click, type, close, drag) is a separately granted permission, and every effect is re-verified against the live target (identity, focus, occlusion) right before it runs. It hands the client pixels and window-relative coordinates, never on-screen text, so screen content cannot be mistaken for instructions. UIA-less canvas apps are supported through versioned, hash-verified coordinate profiles.

---

### 🛡 Security advisories

Credited reporter on published GitHub Security Advisories:

- **Pelican:** application API mounts ACL-scope bypass, CWE-862/863 ([GHSA-43h8-3896-wqv5](https://github.com/pelican-dev/panel/security/advisories/GHSA-43h8-3896-wqv5))
- **Pelican:** Filament suspend-all / unsuspend-all missing authorization ([GHSA-4wxv-r46p-w2f9](https://github.com/pelican-dev/panel/security/advisories/GHSA-4wxv-r46p-w2f9))
- **Jexactyl:** free-billing flow missing ownership check, CWE-862 ([GHSA-9xwv-p7r5-5h5p](https://github.com/Jexactyl/Jexactyl/security/advisories/GHSA-9xwv-p7r5-5h5p))
- **OneUptime:** incoming-call-number resend-verification-code missing ownership check — the sibling channel the CVE-2026-30959 fix sweep left uncovered, CWE-862 ([GHSA-wc96-jm46-37hh](https://github.com/OneUptime/oneuptime/security/advisories/GHSA-wc96-jm46-37hh))

Vendor security acknowledgement:

- **zn:** high-severity control-plane authorization gap on policy and consensus handlers, where non-admin tenant keys could modify policy or consensus state through missing function-level checks (SEC-2026-01, credited on the [usezn.com Security Hall of Fame](https://usezn.com/security/))

### 🔗 Upstream detections

Detection templates merged into projectdiscovery/nuclei-templates:

- **CVE-2026-26190** Milvus, unauthenticated metrics port ([#16333](https://github.com/projectdiscovery/nuclei-templates/pull/16333))
- **CVE-2026-25527** changedetection.io ≤ 0.52.9 ([#16346](https://github.com/projectdiscovery/nuclei-templates/pull/16346))
- **CVE-2026-33476** SiYuan ≤ v3.6.1 ([#16335](https://github.com/projectdiscovery/nuclei-templates/pull/16335))
- **CVE-2026-31831** Tautulli ≤ 2.16.1, unauthenticated path traversal ([#16345](https://github.com/projectdiscovery/nuclei-templates/pull/16345))

<div align="center">

<sub><code>0 of <!--SIGMA_RULES_START-->296<!--SIGMA_RULES_END--> sigma rules marked stable</code> · <code>no open CodeQL alerts across 5 featured repos (checked 2026-09-20)</code> · <code>MIT-licensed featured projects</code> · <code>standard-library-first where it makes sense</code></sub>

</div>
