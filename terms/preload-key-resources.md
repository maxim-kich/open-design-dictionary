---
category: ui
type: tool
tags: [web, analytics]
---

# Preload Key Resources

## Definition
Fetch critical assets early in page load process.

## Examples
- <link rel=preload as=font href=hero.woff2>
- Preload LCP hero image
- Preload critical CSS/JS
- DNS prefetch third-parties

## Do's and Don'ts

**Do's**
- Prioritize LCP resources
- Monitor preload impact
- Remove unused preloads
- Cross-origin CORS correct

**Don'ts**
- Preload everything
- Wrong as= type attributes
- No crossorigin
- Unused preloads

## References
- [Web.dev: Preload Critical Resources](https://web.dev/preload-critical-resources/)
- [MDN](https://developer.mozilla.org/en-US/)
