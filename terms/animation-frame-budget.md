---
category: ui
type: methodology
tags: [mobile, analytics]
---

# Animation Frame Budget

## Definition
Frame rendering performance target for smooth motion.

## Examples
- 16.67ms per frame target
- Main thread budget 120ms
- Skipped frame monitoring
- Device-specific budgets

## Do's and Don'ts

**Do's**
- Profile on target devices
- Optimize expensive ops
- Reduce layer complexity
- Test across hardware

**Don'ts**
- 30fps tolerance
- Desktop performance only
- No frame timing tools
- Ignore dropped frames

## References
- [Apple: CADisplayLink](https://developer.apple.com/documentation/quartzcore/cadisplaylink)
- [Android Developer](https://developer.android.com/)
