---
category: ui
type: tool
tags: [color, accessibility]
---

# Color Blindness Simulation

## Definition
A testing method that simulates how designs appear to users with different types of color vision deficiency. Common simulations include protanopia (red-blind), deuteranopia (green-blind), tritanopia (blue-blind), and achromatopsia (complete color blindness), helping identify problematic color dependencies.

## Examples
- Testing a status indicator system (red/yellow/green) to ensure states are distinguishable without color
- Simulating deuteranopia on a data visualization to check if chart segments remain identifiable
- Verifying that error states are not communicated solely through red color
- Checking that link colors are distinguishable from body text under all simulations

## Do's and Don'ts

**Do's**
- Test all three major types: protanopia, deuteranopia, tritanopia
- Ensure critical information has non-color indicators (icons, patterns, labels)
- Use simulation early in the design process, not just at the end
- Test interactive states (hover, focus, selected) under simulation
- Consider that ~8% of men have some form of color vision deficiency

**Don'ts**
- Rely on red/green distinction for critical UI elements
- Use color as the only differentiator between states
- Assume passing one simulation means passing all
- Skip testing data visualizations and charts
- Forget to test both light and dark mode under simulation

## References
- [Coblis: Color Blindness Simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/)
- [Stark: Accessibility Tools for Figma](https://www.getstark.co/)
