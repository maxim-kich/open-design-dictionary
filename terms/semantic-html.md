---
category: ui
type: principle
tags: [accessibility,  web]
---

# Semantic HTML

## Definition
Meaningful markup (headings, lists, landmarks) aiding assistive technology.

## Examples
- <h1> to <h6> hierarchy
- <nav>, <main>, <aside> landmarks
- <ul>, <ol>, <dl> proper lists
- <button> vs <div> semantics

## Do's and Don'ts

**Do's**
- Proper heading hierarchy
- ARIA landmark roles
- Native HTML controls
- Screen reader announces correctly

**Don'ts**
- <div role='button'>
- h3>h2 heading order
- <b> instead of <strong>
- Visual-only styling

## References
- [WebAIM: Semantic Structure](https://webaim.org/techniques/semanticstructure/)
- [HTML5 Doctor: Semantics](http://html5doctor.com/)
