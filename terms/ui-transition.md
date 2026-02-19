---
category: ui
type: tool
tags: [interaction]
---

# UI Transition

## Definition
Smooth property change between states (color, position, opacity) with duration and easing.

## Examples
- Button color transition 200ms ease
- Modal fade-in 300ms cubic-bezier
- Menu slide 400ms ease-out
- Scale transition on hover

## Do's and Don'ts

**Do's**
- Use appropriate easing curves
- Match duration to distance
- Limit concurrent transitions
- Test 60fps performance

**Don'ts**
- Abrupt state changes
- Long transitions (>500ms)
- Competing transitions
- Generic easing everywhere

## References
- [CSS-Tricks: CSS Transitions](https://css-tricks.com/almanac/properties/t/transition/)
- [Material Design: Motion](https://m3.material.io/styles/motion/overview)
