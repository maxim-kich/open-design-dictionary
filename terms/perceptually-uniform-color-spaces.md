---
category: ui
type: tool
tags: [color]
---

# Perceptually Uniform Color Spaces

## Definition
Color spaces (LAB, LCH, OKLAB, OKLCH) designed so that equal numerical changes produce equal perceived visual changes. Unlike RGB or HSL, these spaces ensure that a 10-unit lightness change looks the same whether moving from light to mid or mid to dark tones.

## Examples
- Generating a color scale in LCH by adjusting lightness in equal steps for visually even gradients
- Using OKLCH in CSS to create smooth transitions that don't muddy through gray
- Building accessible color ramps where each step has predictable perceived difference
- Adjusting chroma in LCH to desaturate colors without shifting hue unexpectedly

## Do's and Don'ts

**Do's**
- Use LCH/OKLCH for generating color scales and gradients
- Adjust lightness (L) for creating tonal variations
- Use chroma (C) for saturation adjustments without hue shifts
- Consider OKLCH for CSS (modern browser support)
- Verify results visually (models are approximations)

**Don'ts**
- Use RGB/HSL for creating perceptually even scales
- Assume HSL lightness is perceptually uniform (it's not)
- Forget that out-of-gamut colors may clip when converted to RGB
- Ignore that different hues have different maximum chroma ranges
- Over-rely on numbers without visual validation

## References
- [OKLCH in CSS: Why We Moved From RGB and HSL](https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl)
- [Lea Verou: LCH Colors in CSS](https://lea.verou.me/2020/04/lch-colors-in-css-what-why-and-how/)
