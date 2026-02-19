---
category: ui
type: tool
tags: [web, mobile]
---

# Viewport Meta Tag

## Definition
HTML tag controlling mobile zoom scaling behavior.

## Examples
- <meta name=viewport content=width=device-width initial-scale=1>
- maximum-scale=1.0 user-scalable=no
- viewport-fit=cover iPhone X
- width=device-width shrink-to-fit=no

## Do's and Don'ts

**Do's**
- Always include viewport tag
- Test zoom behavior
- Support pinch-zoom
- Document mobile behavior

**Don'ts**
- Omit viewport tag
- Disable all zooming
- Fixed scale=1.0 only
- Ignore Safari iOS quirks

## References
- [MDN: Viewport Meta Tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag)
- [CSS-Tricks: Viewport Meta Tag](https://css-tricks.com/snippets/html/viewport-metatag/)
