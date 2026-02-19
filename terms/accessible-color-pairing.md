---
category: ui
type: methodology
tags: [color, accessibility]
---

# Accessible Color Pairing

## Definition
A method for systematically identifying and documenting color combinations that meet accessibility contrast requirements. Pairing involves testing foreground colors against multiple backgrounds to create a matrix of compliant combinations for text, icons, and interactive elements.

## Examples
- Creating a contrast matrix showing which text colors pass AA/AAA on each background color
- Documenting that blue-600 works on white and gray-100, but not on gray-200
- Building a reference table of approved color pairs for the design system
- Identifying which accent colors can be used for text vs. decorative elements only

## Do's and Don'ts

**Do's**
- Create a systematic matrix of all foreground/background combinations
- Document both AA (4.5:1) and AAA (7:1) compliance for each pair
- Include pairs for all UI contexts: text, icons, borders, focus states
- Update pairing documentation when palette changes
- Provide clear guidance on which pairs to use where

**Don'ts**
- Assume a color that works on white works on all light backgrounds
- Create pairs without testing actual contrast ratios
- Document only text pairs (icons and UI elements need pairs too)
- Forget to test pairs in both light and dark modes
- Approve pairs that only barely pass (aim for comfortable margins)

## References
- [Lyft: Designing Accessible Color Systems](https://design.lyft.com/re-approaching-color-9e604ba22c88)
- [WebAIM: Contrast Checker](https://webaim.org/resources/contrastchecker/)
