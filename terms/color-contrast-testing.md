---
category: ui
type: tool
tags:
  - color
  - accessibility
---

# Color Contrast Testing

## Definition
A method for verifying that color combinations meet accessibility standards for readability. Testing measures the luminance ratio between foreground and background colors against WCAG thresholds: 4.5:1 for normal text (AA), 3:1 for large text (AA), and 7:1 for enhanced contrast (AAA).

## Examples
- Testing body text color against page background to ensure 4.5:1 minimum ratio
- Verifying that button text meets contrast requirements on both default and hover states
- Checking placeholder text contrast (often fails due to low-contrast gray)
- Validating icon contrast against various background colors in the system

## Do's and Don'ts

**Do's**
- Test all text/background combinations in your design system
- Include hover, focus, and disabled states in testing
- Test against both light and dark mode backgrounds
- Document passing color pairs for easy reference
- Re-test when any color values change

**Don'ts**
- Assume similar colors have similar contrast ratios
- Skip testing for large text (still requires 3:1)
- Ignore non-text elements (icons, focus rings, borders)
- Test only in isolation without real UI context
- Rely solely on automated tools without visual verification

## References
- [WCAG 2.1: Contrast (Minimum)](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- [WebAIM: Contrast Checker](https://webaim.org/resources/contrastchecker/)
