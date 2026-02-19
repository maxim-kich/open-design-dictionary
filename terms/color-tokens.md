---
category: ui
type: methodology
tags: [color,  design-systems]
---

# Color Tokens

## Definition
A systematic approach to organizing colors in design systems using hierarchical abstraction levels: primitive tokens (raw color values), semantic tokens (purpose-based names like "text-primary"), and component tokens (context-specific like "button-background"). This structure enables consistent theming and maintainability.

## Examples
- Primitive: `blue-500: #3B82F6` → Semantic: `color-action: blue-500` → Component: `button-primary-bg: color-action`
- Changing `color-action` from blue to green updates all components referencing it
- Using `text-primary` instead of `gray-900` so dark mode can remap it to `gray-100`

## Do's and Don'ts

**Do's**
- Start with primitive tokens as the foundation
- Create semantic tokens that describe purpose, not appearance
- Use component tokens sparingly for specific overrides
- Name tokens consistently across the system
- Document the relationship between token levels
- Design semantic tokens with theming in mind

**Don'ts**
- Reference primitive tokens directly in components
- Create semantic tokens for every possible use case
- Use color names in semantic tokens (e.g., "blue-text")
- Skip the semantic layer and go straight to component tokens
- Forget to consider dark mode when designing the token structure
- Create circular references between token levels

## References
- [Tokens Studio: Design Tokens](https://tokens.studio/)
- [Design Tokens W3C Community Group](https://www.w3.org/community/design-tokens/)
