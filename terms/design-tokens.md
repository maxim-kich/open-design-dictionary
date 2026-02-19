---
category: ui
type: principle
type: tool
tags: [design-systems]
---

# Design Tokens

## Definition
Primitive values (colors, sizes, spacing) stored as variables to maintain consistency across design tools, code, and platforms.

## Examples
- color-primary: #007acc
- spacing-md: 16px
- radius-lg: 8px
- font-size-xl: 24px

## Do's and Don'ts

**Do's**
- Use semantic names (e.g., color-danger not #ff0000)
- Define tokens at lowest level (rem not px)
- Document token relationships
- Automate token sync between tools

**Don'ts**
- Mix hardcoded values with tokens
- Use arbitrary numeric values
- Ignore platform differences
- Skip token validation

## References
- [Design Tokens Community Group](https://design-tokens.github.io/)
- [Tokens Studio](https://tokens.studio/)
