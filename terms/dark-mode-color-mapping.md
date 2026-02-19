---
category: ui
type: methodology
tags: [color,  design-systems]
---

# Dark Mode Color Mapping

## Definition
A methodology for systematically adapting a light mode color palette to dark mode. Mapping defines how each color transforms: backgrounds invert from light to dark, text flips from dark to light, and accent colors adjust saturation and lightness to maintain visibility and reduce eye strain.

## Examples
- Mapping white backgrounds to gray-900 and gray-100 surfaces to gray-800
- Reducing saturation of bright accent colors to prevent eye strain on dark backgrounds
- Inverting the color scale so text-primary (gray-900) maps to gray-100 in dark mode
- Adjusting elevation: using lighter surfaces instead of shadows to show depth

## Do's and Don'ts

**Do's**
- Use semantic color tokens to enable automatic theme switching
- Reduce saturation of vibrant colors for dark mode (less visual strain)
- Maintain consistent contrast ratios across both modes
- Use surface elevation (lighter grays) instead of shadows for depth
- Test both modes side by side for visual consistency

**Don'ts**
- Simply invert all colors (produces poor results)
- Use pure black (#000000) as the darkest background (too harsh)
- Keep the same saturation levels for accent colors (often too vibrant)
- Forget to adjust illustrations and images for dark mode
- Assume light mode contrast ratios automatically work in dark mode

## References
- [Material Design: Dark Theme](https://m3.material.io/styles/color/dark-theme)
- [Apple Human Interface Guidelines: Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)
