---
category: ui
type: methodology
tags: [color,  data-visualization]
---

# Data Visualization Color Scales

## Definition
A methodology for selecting appropriate color scales based on data type. Sequential scales (light to dark) show ordered data, diverging scales (two hues from a neutral center) show deviation from a midpoint, and categorical scales (distinct hues) differentiate unrelated categories.

## Examples
- Using a sequential blue scale (light to dark) to show temperature from low to high
- Applying a diverging red-white-green scale to show profit/loss deviation from zero
- Choosing 5-7 distinct categorical colors for different product lines in a pie chart
- Using a single-hue sequential scale for population density maps

## Do's and Don'ts

**Do's**
- Match scale type to data type (sequential for ordered, categorical for nominal)
- Limit categorical palettes to 5-7 distinguishable colors
- Use perceptually uniform scales for accurate data representation
- Test scales under color blindness simulation
- Ensure sufficient contrast between adjacent values in sequential scales

**Don'ts**
- Use rainbow scales for sequential data (not perceptually uniform)
- Apply categorical colors to ordered data
- Use too many categories (hard to distinguish beyond 7 colors)
- Forget that red/green distinctions fail for colorblind users
- Assume diverging scales need symmetric data ranges

## References
- [ColorBrewer: Color Advice for Maps](https://colorbrewer2.org/)
- [D3 Color Scales](https://d3js.org/d3-scale-chromatic)
