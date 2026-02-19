---
category: ui
type: methodology
tags: [web, analytics]
---

# Critical CSS Extraction

## Definition
Extract above-fold styles for immediate rendering.

## Examples
- 14KB render-blocking CSS
- Critical path inline styles
- Async non-critical CSS
- Automated critical extraction

## Do's and Don'ts

**Do's**
- Automate extraction process
- Monitor bundle size
- Test render performance
- Mobile-first critical

**Don'ts**
- Inline ALL CSS
- Manual extraction
- Forget non-critical async
- Desktop-optimized critical

## References
- [web.dev: Extract Critical CSS](https://web.dev/articles/extract-critical-css)
