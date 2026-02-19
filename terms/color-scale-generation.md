---
category: ui
type: methodology
tags: [color,  design-systems]
---

# Color Scale Generation

## Definition
A method for creating systematic tonal variations of a base color, typically producing a scale from light to dark (e.g., 50, 100, 200... 900). Color scales provide consistent options for different UI states, backgrounds, and text while maintaining color harmony.

## Examples
- Generating a blue scale from near-white (blue-50) to near-black (blue-900) for a design system
- Creating a gray scale with 10 steps to handle backgrounds, borders, and text colors
- Building semantic scales where success-100 is a light tint and success-700 is the darkest usable shade

## Do's and Don'ts

**Do's**
- Use perceptually uniform color spaces (LCH/LAB) for more even steps
- Ensure sufficient contrast between adjacent steps for usability
- Include enough steps to cover backgrounds, borders, text, and hover states
- Test scales in both light and dark mode contexts
- Document the intended use for each step (e.g., 500 = default, 600 = hover)

**Don'ts**
- Generate scales by simply adjusting lightness in RGB (produces uneven results)
- Create too many steps (10-12 is usually sufficient)
- Assume linear lightness changes produce linear visual changes
- Forget to verify contrast ratios between text and background steps
- Mix different generation methods within the same design system

## References
- [Stripe: Designing Accessible Color Systems](https://stripe.com/blog/accessible-color-systems)
- [Tailwind CSS: Customizing Colors](https://tailwindcss.com/docs/customizing-colors)
