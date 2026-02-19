---
category: ui
type: methodology
tags: [color,  accessibility]
---

# Color Overlay Testing

## Definition
A method for verifying color readability and visual hierarchy when UI elements are layered with transparency or overlays. Testing ensures that text, icons, and interactive elements remain legible on semi-transparent backgrounds, modals, scrims, and overlapping surfaces.

## Examples
- Testing modal scrim opacity to ensure background content is sufficiently dimmed
- Verifying text readability on cards with semi-transparent backgrounds over images
- Checking toast notifications remain legible over varying page content
- Testing dropdown menus with transparency against different underlying colors

## Do's and Don'ts

**Do's**
- Test overlays against multiple background scenarios (light, dark, colorful, images)
- Verify contrast ratios for text on the resulting blended colors
- Consider how overlays appear in both light and dark modes
- Test with actual content, not just solid test backgrounds
- Document approved overlay opacity values for consistency

**Don'ts**
- Assume a single opacity value works on all backgrounds
- Skip testing overlays on image-heavy pages
- Forget that transparency compounds when multiple overlays stack
- Test only against white or neutral backgrounds
- Ignore how overlays affect focus states and interactive elements beneath

## References
- [Material Design: Elevation and Shadows](https://m3.material.io/styles/elevation/overview)
- [W3C: Understanding Contrast](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
