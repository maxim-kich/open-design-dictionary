#!/usr/bin/env python3
"""
Build script for Open Design Dictionary.
Compiles all terms/*.md files into:
  - open-design-dictionary.json       (full, all fields)
  - open-design-dictionary-lite.json  (name, category, type, definition)
  - open-design-dictionary.md         (single Markdown file, all terms)
"""

import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent.parent
TERMS_DIR = ROOT / "terms"
OUT_JSON_FULL = ROOT / "open-design-dictionary.json"
OUT_JSON_LITE = ROOT / "open-design-dictionary-lite.json"
OUT_MD = ROOT / "open-design-dictionary.md"


def parse_frontmatter(text):
    """Split YAML frontmatter from body. Returns (frontmatter_str, body_str)."""
    if not text.startswith("---"):
        return "", text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return "", text
    return parts[1].strip(), parts[2].strip()


def parse_yaml_simple(yaml_str):
    """Minimal YAML parser for the frontmatter we actually use."""
    data = {}
    for line in yaml_str.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        # Handle inline lists: [a, b, c]
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1]
            data[key] = [v.strip().strip('"').strip("'") for v in inner.split(",") if v.strip()]
        else:
            data[key] = value.strip('"').strip("'")
    return data


def extract_section(body, heading):
    """Extract text under a ## heading up to the next ## heading."""
    pattern = rf"##\s+{re.escape(heading)}\s*\n(.*?)(?=\n##\s|\Z)"
    match = re.search(pattern, body, re.DOTALL)
    if not match:
        return ""
    return match.group(1).strip()


def parse_dos_donts(section_text):
    """Parse Do's and Don'ts section into two lists."""
    dos, donts = [], []
    current = None
    for line in section_text.splitlines():
        stripped = line.strip()
        if re.match(r"\*\*Do.s\*\*", stripped, re.IGNORECASE):
            current = "dos"
        elif re.match(r"\*\*Don.ts?\*\*", stripped, re.IGNORECASE):
            current = "donts"
        elif stripped.startswith("- ") and current == "dos":
            dos.append(stripped[2:].strip())
        elif stripped.startswith("- ") and current == "donts":
            donts.append(stripped[2:].strip())
    return dos, donts


def parse_references(section_text):
    """Extract reference list items."""
    refs = []
    for line in section_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            refs.append(stripped[2:].strip())
    return refs


def slugify(name):
    slug = name.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug


def parse_term_file(path):
    text = path.read_text(encoding="utf-8")
    fm_str, body = parse_frontmatter(text)
    fm = parse_yaml_simple(fm_str)

    # Term name from # heading
    name_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    name = name_match.group(1).strip() if name_match else path.stem

    definition = extract_section(body, "Definition")
    examples_raw = extract_section(body, "Examples")
    dos_donts_raw = extract_section(body, "Do's and Don'ts")
    references_raw = extract_section(body, "References")

    dos, donts = parse_dos_donts(dos_donts_raw)
    references = parse_references(references_raw)

    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]

    return {
        "name": name,
        "slug": slugify(name),
        "category": fm.get("category", ""),
        "type": fm.get("type", ""),
        "tags": tags,
        "definition": definition,
        "examples": examples_raw,
        "dos": dos,
        "donts": donts,
        "references": references,
    }


def build_md(terms):
    parts = [
        "# Open Design Dictionary\n",
        f"*{len(terms)} terms — generated from `terms/*.md`*\n",
    ]
    for term in terms:
        parts.append("\n---\n")
        parts.append(f"## {term['name']}\n")
        parts.append(f"**Category:** {term['category']} | **Type:** {term['type']}")
        if term["tags"]:
            parts.append(f" | **Tags:** {', '.join(term['tags'])}")
        parts.append("\n\n")
        parts.append(f"{term['definition']}\n")

        if term["examples"]:
            parts.append(f"\n**Examples**\n{term['examples']}\n")

        if term["dos"] or term["donts"]:
            parts.append("\n**Do's and Don'ts**\n")
            if term["dos"]:
                parts.append("\n*Do's*\n")
                for item in term["dos"]:
                    parts.append(f"- {item}\n")
            if term["donts"]:
                parts.append("\n*Don'ts*\n")
                for item in term["donts"]:
                    parts.append(f"- {item}\n")

        if term["references"]:
            parts.append("\n**References**\n")
            for ref in term["references"]:
                parts.append(f"- {ref}\n")

    return "".join(parts)


def main():
    if not TERMS_DIR.exists():
        print(f"Error: terms directory not found at {TERMS_DIR}", file=sys.stderr)
        sys.exit(1)

    md_files = sorted(TERMS_DIR.glob("*.md"))
    print(f"Found {len(md_files)} term files.")

    terms = []
    errors = []
    for f in md_files:
        try:
            terms.append(parse_term_file(f))
        except Exception as e:
            errors.append((f.name, str(e)))

    if errors:
        print(f"\nParse errors ({len(errors)}):")
        for name, err in errors:
            print(f"  {name}: {err}")

    # Sort alphabetically by name
    terms.sort(key=lambda t: t["name"].lower())

    # Full JSON
    OUT_JSON_FULL.write_text(json.dumps(terms, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Written: {OUT_JSON_FULL.name}")

    # Lite JSON
    lite = [
        {"name": t["name"], "category": t["category"], "type": t["type"], "definition": t["definition"]}
        for t in terms
    ]
    OUT_JSON_LITE.write_text(json.dumps(lite, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Written: {OUT_JSON_LITE.name}")

    # Single MD
    OUT_MD.write_text(build_md(terms), encoding="utf-8")
    print(f"Written: {OUT_MD.name}")

    # Summary
    print(f"\nTotal terms: {len(terms)}")
    categories = Counter(t["category"] for t in terms)
    print("By category:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
