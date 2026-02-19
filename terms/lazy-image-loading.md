---
category: ui
type: pattern
tags: [web, analytics]
---

# Lazy Image Loading

## Definition
Images load only when scrolled into viewport.

## Examples
- loading=lazy native attribute
- IntersectionObserver API
- Fade-in placeholder animation
- Priority hints for above-fold

## Do's and Don'ts

**Do's**
- Native loading=lazy first
- Critical images eager
- Smooth placeholder fade
- Network prioritization

**Don'ts**
- Lazy ALL images
- No above-fold optimization
- Jarring layout shifts
- No priority hints

## References
- [Web.dev: Lazy Loading](https://web.dev/lazy-loading/)
- [MDN](https://developer.mozilla.org/en-US/)
