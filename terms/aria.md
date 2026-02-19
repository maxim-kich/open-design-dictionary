---
category: ui
type: tool
tags: [accessibility,  web]
---

# ARIA

## Definition
Accessible Rich Internet Applications - attributes for dynamic content.

## Examples
- aria-expanded for accordions
- aria-live for announcements
- aria-label for unlabeled icons
- role='alert' for errors

## Do's and Don'ts

**Do's**
- Use as last resort (prefer semantics)
- Validate ARIA implementation
- Test with screen readers
- Document custom ARIA

**Don'ts**
- aria-* on static content
- Invalid ARIA values
- ARIA hiding content
- Untested ARIA patterns

## References
- [W3C: ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [WebAIM: ARIA Basics](https://webaim.org/techniques/aria/)
