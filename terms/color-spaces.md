---
category: ui
type: tool
tags: [color]
---

# Color Spaces

## Definition
A color space is a mathematical model that defines how colors are represented as numerical values. Different color spaces serve different purposes: RGB for screens, CMYK for print, HSL/HSB for intuitive adjustments, and LAB/LCH for perceptually uniform color work.

## Examples
- Using RGB or Hex values when defining colors for web interfaces
- Switching to HSL to quickly adjust lightness or saturation while keeping the same hue
- Working in CMYK when preparing assets for print production
- Using LAB color space to create visually uniform color gradients

## Do's and Don'ts

**Do's**
- Use HSL/HSB for manual color adjustments and exploration
- Use RGB/Hex for final implementation in digital products
- Consider LAB/LCH when creating color scales that need perceptual uniformity
- Document which color space your design system uses as source of truth
- Convert colors properly when moving between color spaces

**Don'ts**
- Mix color spaces without understanding conversion implications
- Use RGB for intuitive color adjustments (hard to predict results)
- Ignore color space when collaborating across design and development
- Assume colors look identical across different color spaces
- Forget that some colors exist in one space but not another (gamut limits)

## References
- [MDN: Color Spaces](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)
- [CSS Color Level 4: Color Spaces](https://www.w3.org/TR/css-color-4/)
