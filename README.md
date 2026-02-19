# Open Design Dictionary

Open Design Dictionary is a community-maintained, open-source dictionary of design terms and concepts. Organized alphabetically and tagged by category, type, and domain for easy discovery and cross-reference.

## Overview

This dictionary provides clear, practical definitions of design terminology across UI, UX, strategy, and management. Each term includes examples, do's and don'ts, and references to authoritative sources.

Designed to be simple, universal, and easy to contribute to.

## Structure

- **Terms** are stored as individual Markdown files in the `terms/` directory
- **Categories** organize terms into four primary areas: UI, UX, Strategy, Management
- **Types** classify terms by nature: principle, methodology, tool, pattern, framework, concept
- **Tags** enable cross-category discovery and flexible filtering
- **Frontmatter** (YAML) makes the dictionary machine-readable

## Files

| File | Description |
|------|-------------|
| `open-design-dictionary.json` | Full dictionary as JSON (all fields) |
| `open-design-dictionary.md` | Full dictionary as single Markdown file |
| `open-design-dictionary-lite.json` | Lightweight JSON (name, category, type, definition only) |
| `terms/` | Individual term files (source of truth) |
| `CONTRIBUTING.md` | Guidelines for adding new terms |
| `TEMPLATE.md` | Template for new term entries |

## Philosophy

- **Minimal and focused** - Tags and categories are kept intentionally small to avoid fragmentation
- **Universal** - Terms are generic and context-independent
- **Practical** - Definitions emphasize application over theory
- **Accessible** - Examples are generic scenarios, not specific products
- **Community-driven** - Anyone can contribute

## Usage

### For Individuals

Use this dictionary to clarify design terminology, understand cross-category connections, and explore best practices.

### For Teams

Reference specific terms in design discussions, documentation, and guidelines. Link to terms for shared vocabulary.

### For Tools & Integrations

The dictionary is available in machine-readable formats for easy integration:

**JSON (full):**
```
https://raw.githubusercontent.com/maxim-kich/open-design-dictionary/main/open-design-dictionary.json
```

**JSON (lightweight):**
```
https://raw.githubusercontent.com/maxim-kich/open-design-dictionary/main/open-design-dictionary-lite.json
```

**Markdown (single file):**
```
https://raw.githubusercontent.com/maxim-kich/open-design-dictionary/main/open-design-dictionary.md
```

Use these to feed LLMs, build design tools, or integrate with platforms like Lovable, Cursor, or Claude.

## License

This dictionary is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to use, adapt, and distribute this content, provided you give appropriate credit to the original authors.

## Contributing

I welcome contributions from the design community. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Questions or suggestions? Open an issue to discuss.
