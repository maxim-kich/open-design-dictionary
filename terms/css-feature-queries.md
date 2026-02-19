---
category: ui
type: tool
tags: [web]
---

# CSS Feature Queries

## Definition
Conditional CSS based on browser feature support.

## Examples
- @supports (grid-gap: 1rem) { .grid { display: grid; } }
- @supports (container-type: inline-size) { .cq { container-type: inline-size; } }
- @supports (aspect-ratio: 1) fallback
- Subgrid feature detection

## Do's and Don'ts

**Do's**
- Progressive enhancement
- Graceful fallbacks
- Test support thresholds
- Document feature tiers

**Don'ts**
- Assume universal support
- No fallback styles
- Browser sniffing instead
- Disable modern features

## References
- [MDN: @supports](https://developer.mozilla.org/en-US/docs/Web/CSS/@supports)
- [CSS-Tricks: CSS Feature Queries](https://css-tricks.com/css-feature-queries/)
