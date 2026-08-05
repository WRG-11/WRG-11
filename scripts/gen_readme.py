#!/usr/bin/env python3
"""Stamp live custom-metrics into the profile README.

Single source of truth: the wrg-sigma-rules repo README declares the canonical
corpus numbers in ``METRIC:`` markers stamped from disk by its own
readme_stamp.py. We mirror them into this profile so the badge + prose never
drift. shields.io / github-readme-stats badges are live on render and need no
stamping; only the mirrored corpus numbers do.

Two are mirrored: the rule count and the ATT&CK tactic-category count. The
second was added after the profile read "13 ATT&CK tactic categories" while
the corpus had 14 — the rule count was mirrored and stayed right, the tactic
count was typed by hand here and went stale with nothing to object.

Zero external deps (stdlib urllib). Safe: if the count can't be parsed, the
README is left unchanged and we exit 0 (never commit a broken number).
"""
from __future__ import annotations

import re
import sys
import urllib.request

SIGMA_README = "https://raw.githubusercontent.com/WRG-11/wrg-sigma-rules/main/README.md"
README_PATH = "README.md"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "wrg-profile-readme-stamp"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def find_rule_count(sigma_readme: str) -> str | None:
    # wrg-sigma-rules stamps its canonical count into a METRIC marker via its
    # own readme_stamp.py (counts resources/examples/<tactic>/*.yml) — read that
    # single source of truth first, with looser phrasings as fallback.
    for pattern in (
        r"<!--\s*METRIC:sigma_rule_count\s*-->(\d+)<!--\s*/METRIC:sigma_rule_count\s*-->",
        r"(\d+)\s+production\s+rules",
        r"(\d+)\s+sigma\s+(?:detection\s+)?rules",
    ):
        m = re.search(pattern, sigma_readme, re.IGNORECASE)
        if m:
            return m.group(1)
    return None


def find_tactic_count(sigma_readme: str) -> str | None:
    """Read the tactic-category count the sigma README stamps from disk.

    No looser fallback than the marker on purpose: a phrase-matching regex
    here would happily pick up whatever number happened to sit next to the
    words "tactic categories", which is the failure this function exists to
    end. No marker, no stamp.
    """
    m = re.search(
        r"<!--\s*METRIC:tactic_category_count\s*-->(\d+)"
        r"<!--\s*/METRIC:tactic_category_count\s*-->",
        sigma_readme,
    )
    return m.group(1) if m else None


def main() -> int:
    try:
        sigma_readme = fetch(SIGMA_README)
    except Exception as exc:  # noqa: BLE001 -- network flake must not break CI
        print(f"WARN: could not fetch sigma README ({exc}); leaving README unchanged", file=sys.stderr)
        return 0

    count = find_rule_count(sigma_readme)
    tactics = find_tactic_count(sigma_readme)

    if not count:
        print("WARN: rule count not found in sigma README; leaving README unchanged", file=sys.stderr)
        return 0

    with open(README_PATH, encoding="utf-8") as f:
        original = f.read()

    updated = re.sub(
        r"(<!--SIGMA_RULES_START-->).*?(<!--SIGMA_RULES_END-->)",
        rf"\g<1>{count}\g<2>",
        original,
        flags=re.DOTALL,
    )
    updated = re.sub(r"(sigma_rules-)\d+(-)", rf"\g<1>{count}\g<2>", updated)

    # A missing tactic count leaves that marker alone rather than blanking
    # it: an upstream README that briefly lacks the marker should not be
    # able to erase a correct number here.
    if tactics:
        updated = re.sub(
            r"(<!--SIGMA_TACTICS_START-->).*?(<!--SIGMA_TACTICS_END-->)",
            rf"\g<1>{tactics}\g<2>",
            updated,
            flags=re.DOTALL,
        )
    else:
        print("WARN: tactic count marker not found upstream; left as-is", file=sys.stderr)

    stamped = f"sigma rule count = {count}, tactic categories = {tactics or 'unchanged'}"
    if updated != original:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"README updated: {stamped}")
    else:
        print(f"No change ({stamped})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
