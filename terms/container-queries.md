---
category: ui
type: tool
tags: [web]
---

# Container Queries

## Definition
Style components based on container size not viewport.

## Examples
- @container (min-width: 400px) {}
- Card adapts to parent width
- Component responsive internally
- Side-by-side container variants

## Do's and Don'ts

**Do's**
- container-type: inline-size
- Self-contained components
- Fallback media queries
- Test container contexts

**Don'ts**
- Viewport media queries only
- Fixed component sizes
- Responsive parent only
- No container fallback

## References
- [Chrome: Container Queries](https://developer.chrome.com/docs/css-container-queries/)
- [CSS-Tricks: Container Queries](https://css-tricks.com/container-queries/)
