## Overview

This guide explains how to add new terms to the Open Design Dictionary. Follow the structure and guidelines below to ensure consistency and quality.

## Before You Start

1. Check if the term already exists (search alphabetically in `terms/`)
2. Review the Categories, Types, and Tags sections below
3. Review [TEMPLATE.md](TEMPLATE.md) for the term structure
4. Make sure you understand the term well enough to explain it clearly

## File Structure

**File naming:**
- Name: lowercase, hyphenated
- Extension: `.md`
- Example: `type-scale.md`, `information-architecture.md`

**File location:**
- Place in `terms/` directory
- Files are organized alphabetically

## Frontmatter

```yaml
---
category: ui
type: principle
tags: [visual-hierarchy, typography]
---
```

**Rules:**
- `category`: Required. Single value from Categories list below.
- `type`: Required. Single value from Types list below.
- `tags`: Required. Array of tags from Tags list below. Minimum 1, maximum 5 recommended.

---

## Categories

Categories provide the primary organizational structure. Each term belongs to exactly one category.

| Category | Description |
|----------|-------------|
| `ui` | User interface design, visual design, components, patterns, visual systems |
| `ux` | User experience, interaction design, research, testing, user-centered approaches |
| `strategy` | Design strategy, principles, decision-making, problem-solving, alignment |
| `management` | Processes, team dynamics, communication, collaboration, workflows |

---

## Types

Types classify the nature of each term. Each term has exactly one type.

| Type | Description |
|------|-------------|
| `principle` | Foundational design principle or concept |
| `methodology` | Process, approach, or method |
| `tool` | Software, technique, or practical resource |
| `pattern` | Reusable solution or design pattern |
| `framework` | Structured approach or system |
| `concept` | Theoretical idea or mental model |

---

## Tags

Tags enable cross-category discovery and flexible filtering. A term can have multiple tags.

| Tag | Description |
|-----|-------------|
| `color` | Color theory, palettes, color systems |
| `typography` | Typefaces, font sizing, line height, readability |
| `visual-hierarchy` | Visual emphasis, contrast, focal points |
| `iconography` | Icon design, symbol systems, visual language |
| `interaction` | User interactions, feedback, state changes |
| `navigation` | Navigation systems, wayfinding, information flow |
| `accessibility` | Accessible design, inclusive practices |
| `design-systems` | Component libraries, design tokens, pattern systems |
| `documentation` | Design documentation, guidelines, specifications |
| `information-architecture` | Content structure, organization, hierarchy |
| `data-visualization` | Charts, graphs, data representation, dashboards |
| `principles` | Design principles, foundational concepts, best practices |
| `web` | Web-specific considerations, browser concerns |
| `mobile` | Mobile-specific considerations, touch, responsive |
| `research` | User research, discovery, insights |
| `testing` | Usability testing, validation, user feedback |
| `ideation` | Idea generation, creative thinking, problem reframing |
| `analytics` | Quantitative measurement, metrics, data tracking |
| `strategy` | Design strategy, business alignment, goals |
| `processes` | Workflows, methodologies, team processes |

---

## Content Guidelines

Refer to [TEMPLATE.md](TEMPLATE.md) for the exact structure.

### Definition
- Clear and concise (1-2 sentences maximum)
- Avoid jargon or explain jargon used
- Focus on what, not why

### Examples
- Practical and recognizable
- Use generic or hypothetical scenarios
- Should illustrate the definition
- 2-4 examples is ideal

### Do's and Don'ts
- Actionable advice
- Based on best practices
- Help designers apply the term correctly
- Each item should be 1 short sentence or phrase

### References
- Link to authoritative sources (W3C, WCAG, design resources, articles)
- Minimum 1 reference

---

## Validation Checklist

Before submitting a pull request, verify:

- [ ] File name is lowercase and hyphenated
- [ ] Frontmatter is valid YAML
- [ ] Category is valid (ui, ux, strategy, management)
- [ ] Type is valid (principle, methodology, tool, pattern, framework, concept)
- [ ] All tags are from the Tags list above
- [ ] Definition is clear and concise
- [ ] Examples are practical and relevant
- [ ] Do's and Don'ts are actionable
- [ ] All references have valid URLs

---

## Proposing New Categories, Types, or Tags

If you need a new category, type, or tag that doesn't exist, update this file in your pull request and explain why it's needed. New additions require discussion before merging.

## Pull Request Process

1. Create a branch
2. Add your term file(s)
3. If proposing new categories, types, or tags, update this file in the same PR
4. Submit a pull request with a clear description
5. Address feedback if requested
