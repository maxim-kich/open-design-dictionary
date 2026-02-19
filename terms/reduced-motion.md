---
category: ui
type: principle
tags: [accessibility,  interaction]
---

# Reduced Motion

## Definition
Respect user's 'prefers-reduced-motion' OS setting.

## Examples
- @media (prefers-reduced-motion)
- Simple transitions only
- Static focus indicators
- No decorative motion

## Do's and Don'ts

**Do's**
- Honor reduced-motion media query
- Test with OS setting enabled
- Provide static alternatives
- Never disable critical motion

**Don'ts**
- Ignore prefers-reduced-motion
- Parallax effects everywhere
- Auto-playing animations
- Motion-only feedback

## References
- [WCAG 2.3: Focus Appearance](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html)
- [CSS: prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)
