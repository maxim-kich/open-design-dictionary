---
category: ui
type: methodology
tags: [design-systems, analytics, testing]
---

# Visual Regression Failures

## Definition
Number of visual differences detected between design mockups and implemented components during automated testing.

## Examples
- 3 failures in button variants
- 12 card layout shifts
- 1 color token mismatch
- Monthly failures: 16

## Do's and Don'ts

**Do's**
- Integrate into CI/CD pipeline
- Prioritize high-impact failures
- Distinguish bugs from variances
- Track resolution time

**Don'ts**
- Disable tests for convenience
- Ignore small pixel differences
- Test only on one browser
- Blame other teams

## References
- [Chromatic](https://www.chromatic.com/)
