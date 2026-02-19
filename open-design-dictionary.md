# Open Design Dictionary
*427 terms — generated from `terms/*.md`*

---
## A/B Testing
**Category:** ux | **Type:** methodology | **Tags:** testing

A quantitative method that compares two versions of a design by randomly showing each version to users and measuring which performs better on specific metrics. A/B testing provides statistical evidence for design decisions by measuring actual behavior.

**Examples**
- Testing two different button colors to see which has higher click-through rate
- Comparing two checkout flows to determine which has better completion rate

**Do's and Don'ts**

*Do's*
- Test one variable at a time
- Define success metrics before testing
- Ensure statistical significance before concluding
- Run tests long enough for reliable data
- Test with sufficient traffic volume
- Document learnings for future reference

*Don'ts*
- Test too many variables simultaneously
- Stop tests prematurely based on early results
- Make conclusions with insufficient sample size
- Ignore statistical significance
- Test without clear hypotheses
- Use A/B testing for exploratory research

**References**
- [Nielsen Norman Group: A/B Testing](https://www.nngroup.com/articles/ab-testing-usability-engineering/)
- [Optimizely: A/B Testing Guide](https://www.optimizely.com/optimization-glossary/ab-testing/)

---
## Accessibility
**Category:** ui | **Type:** concept | **Tags:** accessibility

Inclusive design enabling users with disabilities to use digital interfaces equally.

**Examples**
- Screen reader support for blind users
- Keyboard navigation for motor impaired
- High contrast for low vision users
- Captions for deaf users

**Do's and Don'ts**

*Do's*
- Follow WCAG 2.1 AA guidelines
- Test with real assistive technology
- Design for all abilities from start
- Document accessibility decisions

*Don'ts*
- Treat as afterthought
- Skip real device testing
- Assume 'it works for me'
- Ignore standards compliance

**References**
- [W3C WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [NN/g: Accessibility Principles](https://www.nngroup.com/articles/accessibility-principles/)

---
## Accessibility Audit
**Category:** ux | **Type:** methodology | **Tags:** testing, accessibility

A systematic evaluation of a product's compliance with accessibility standards (WCAG) and usability for people with disabilities. Accessibility audits use automated tools, manual testing, and assistive technology to identify barriers and ensure inclusive design.

**Examples**
- Testing a website with screen readers to identify issues for blind users
- Evaluating color contrast, keyboard navigation, and ARIA labels against WCAG 2.1 Level AA

**Do's and Don'ts**

*Do's*
- Use both automated tools and manual testing
- Test with actual assistive technologies
- Involve users with disabilities when possible
- Document issues with severity levels
- Test across different assistive technologies
- Create remediation plan with priorities

*Don'ts*
- Rely only on automated accessibility checkers
- Skip manual keyboard navigation testing
- Ignore WCAG guidelines and levels
- Test only with one assistive technology
- Treat accessibility as one-time audit
- Forget to retest after fixes

**References**
- [W3C: WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM: Web Accessibility Evaluation](https://webaim.org/articles/evaluationguide/)

---
## Accessibility Documentation
**Category:** ui | **Type:** tool | **Tags:** documentation, accessibility

Guidelines ensuring WCAG compliance in design deliverables.

**Examples**
- Color contrast test results
- Keyboard navigation map
- Screen reader text hierarchy
- Focus order documentation

**Do's and Don'ts**

*Do's*
- Include test results
- Document all states
- Specify ARIA requirements
- Test with actual tools

*Don'ts*
- Generic accessibility text
- Missing contrast ratios
- No keyboard testing
- Screenshot compliance

**References**
- [W3C WAI](https://www.w3.org/WAI/)
- [WebAIM](https://webaim.org/)

---
## Accessibility Personas
**Category:** ux | **Type:** tool | **Tags:** accessibility, research

User archetypes with specific disabilities.

**Examples**
- Screen reader user Sarah
- Motor impaired Mike
- Low vision Lisa
- Cognitive disability Chris

**Do's and Don'ts**

*Do's*
- Real disability research
- Specific assistive tech
- Realistic scenarios
- Cross-disability coverage

*Don'ts*
- Generic personas + 'disabled'
- Hypothetical scenarios
- Single disability focus
- No tech specification

**References**
- [TPGi: Personas](https://www.tpgi.com/personas/)
- [Knownwell](https://knownwell.substack.com/)

---
## Accessibility Testing
**Category:** ui | **Type:** methodology | **Tags:** testing, accessibility

Screen reader keyboard WCAG compliance validation.

**Examples**
- NVDA VoiceOver testing
- Keyboard trap detection
- 4.5:1 contrast validation
- ARIA landmark testing

**Do's and Don'ts**

*Do's*
- Manual screen reader test
- Keyboard-only navigation
- Color contrast checker
- WCAG 2.1 AA minimum

*Don'ts*
- Automated scans only
- Sample page testing
- No keyboard testing
- WCAG A compliance

**References**
- [WAVE WebAIM](https://wave.webaim.org/)
- [Accessible.org](https://www.accessible.org/)

---
## Accessibility Tree
**Category:** ui | **Type:** concept | **Tags:** accessibility

Browser DOM representation for assistive technology.

**Examples**
- Semantic heading structure
- ARIA landmark roles
- Focus order matches DOM
- Screen reader announces correctly

**Do's and Don'ts**

*Do's*
- Validate with screen readers
- Semantic HTML first
- ARIA only when needed
- Test dynamic content

*Don'ts*
- Ignore tree structure
- ARIA everywhere
- No screen reader test
- DOM order mismatch

**References**
- [MDN: Accessibility HTML](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML)
- [WebAIM](https://webaim.org/)

---
## Accessible Color Pairing
**Category:** ui | **Type:** methodology | **Tags:** color, accessibility

A method for systematically identifying and documenting color combinations that meet accessibility contrast requirements. Pairing involves testing foreground colors against multiple backgrounds to create a matrix of compliant combinations for text, icons, and interactive elements.

**Examples**
- Creating a contrast matrix showing which text colors pass AA/AAA on each background color
- Documenting that blue-600 works on white and gray-100, but not on gray-200
- Building a reference table of approved color pairs for the design system
- Identifying which accent colors can be used for text vs. decorative elements only

**Do's and Don'ts**

*Do's*
- Create a systematic matrix of all foreground/background combinations
- Document both AA (4.5:1) and AAA (7:1) compliance for each pair
- Include pairs for all UI contexts: text, icons, borders, focus states
- Update pairing documentation when palette changes
- Provide clear guidance on which pairs to use where

*Don'ts*
- Assume a color that works on white works on all light backgrounds
- Create pairs without testing actual contrast ratios
- Document only text pairs (icons and UI elements need pairs too)
- Forget to test pairs in both light and dark modes
- Approve pairs that only barely pass (aim for comfortable margins)

**References**
- [Lyft: Designing Accessible Color Systems](https://design.lyft.com/re-approaching-color-9e604ba22c88)
- [WebAIM: Contrast Checker](https://webaim.org/resources/contrastchecker/)

---
## Acquisition Cost (CAC)
**Category:** strategy | **Type:** tool | **Tags:** analytics

Cost acquiring single paying customer.

**Examples**
- $78 CAC paid search
- $42 CAC organic
- CAC:LTV ratio 1:3.1
- Channel-specific CAC

**Do's and Don'ts**

*Do's*
- Track by acquisition channel
- Include all marketing costs
- Monitor CAC:LTV ratio
- Optimize high-CAC channels

*Don'ts*
- Average all channels
- Exclude salaries overhead
- Ignore LTV comparison
- Monthly snapshots only

**References**
- [For Entrepreneurs: CAC](https://www.forentrepreneurs.com/cac/)
- [ProfitWell](https://profitwell.com/)

---
## Active State
**Category:** ui | **Type:** pattern | **Tags:** interaction

Visual indication during interaction (button pressed, link activating).

**Examples**
- Button depressed/shadow inward
- Link underline animation
- Slider handle being dragged
- Dropdown expanding

**Do's and Don'ts**

*Do's*
- Show clear active feedback
- Match active to interaction type
- Use appropriate duration (<200ms)
- Test active state clarity

*Don'ts*
- Subtle active states
- Active states longer than 200ms
- Confusing active feedback
- Skip active state testing

**References**
- [Smashing Magazine: Active States](https://www.smashingmagazine.com/2021/05/accessible-interactions/)
- [UX Planet: Interaction States](https://uxplanet.org/interaction-states-in-ui-design/)

---
## Affinity Diagramming
**Category:** ux | **Type:** methodology | **Tags:** research

A collaborative method for organizing large amounts of qualitative data by grouping related observations, ideas, or insights into clusters. Affinity diagramming synthesizes research findings into patterns and reveals relationships between data points.

**Examples**
- Organizing sticky notes with user quotes and observations from interviews into thematic groups
- Clustering usability test findings to identify common issues and prioritize fixes

**Do's and Don'ts**

*Do's*
- Write one observation per sticky note
- Work collaboratively with the team
- Group silently before discussing
- Let patterns emerge naturally from the data
- Create hierarchy with sub-groups if needed
- Label groups with clear, descriptive names

*Don'ts*
- Start with predetermined categories
- Work alone when team synthesis is valuable
- Write multiple ideas on one note
- Rush the grouping process
- Force data into artificial categories
- Skip naming the final groups

**References**
- [Nielsen Norman Group: Affinity Diagramming](https://www.nngroup.com/articles/affinity-diagram/)
- [Interaction Design Foundation: Affinity Diagrams](https://www.interaction-design.org/literature/article/affinity-diagrams-learn-how-to-cluster-and-bundle-ideas-and-facts)

---
## Affordance
**Category:** ui | **Type:** principle | **Tags:** interaction

Visual cues suggesting possible interactions (raised button, pointer cursor, icon meaning).

**Examples**
- Button with shadow suggesting clickability
- Slider handle suggesting draggable
- Link underline suggesting clickable
- Toggle switch suggesting on/off

**Do's and Don'ts**

*Do's*
- Use familiar affordances
- Test affordance clarity
- Combine visual + contextual cues
- Ensure accessibility affordances

*Don'ts*
- Rely on icons alone
- Use unfamiliar metaphors
- Ignore cultural differences
- Skip affordance testing

**References**
- [Don Norman: The Design of Everyday Things](https://www.nngroup.com/books/design-everyday-things-revised/)
- [Interaction Design Foundation: Affordances](https://www.interaction-design.org/literature/topics/affordances)

---
## AI Design Assist
**Category:** ui | **Type:** tool

Machine learning accelerates design workflow.

**Examples**
- Figma Auto Layout AI
- Variant generation ML
- Color palette suggestion
- Layout completion AI

**Do's and Don'ts**

*Do's*
- Human oversight required
- Transparent AI decisions
- Training data disclosure
- Undo AI suggestions

*Don'ts*
- Blind AI acceptance
- Opaque black box tools
- No human validation
- Production AI output

**References**
- [Figma AI](https://www.figma.com/ai/)
- [Magician Design](https://magician.design/)

---
## Alignment Principle
**Category:** ui | **Type:** principle

Consistent positioning creates visual order.

**Examples**
- Left-aligned body text
- Right-aligned prices
- Center hero elements
- Baseline grid typography

**Do's and Don'ts**

*Do's*
- Grid-based alignment
- Consistent edge alignment
- Visual flow direction
- Responsive alignment shifts

*Don'ts*
- Centered body text
- Inconsistent left/right
- Floating unaligned elements
- Arbitrary positioning

**References**
- [Practical Typography: Alignment](https://practicaltypography.com/alignment/)
- [Smashing Magazine](https://www.smashingmagazine.com/)

---
## Analogy Brainstorming
**Category:** ux | **Type:** methodology | **Tags:** ideation

Apply solutions from unrelated domains to current problem.

**Examples**
- Checkout like fast food drive-through
- Onboarding like hotel check-in
- Dashboard like car instrument panel
- Support like concierge service

**Do's and Don'ts**

*Do's*
- Distant analogies
- Extract principles
- Multiple domains
- Test transfers

*Don'ts*
- Obvious comparisons
- Copy literally
- Single analogy
- Force fit solutions

**References**
- [IDEO: Analogous Inspiration](https://www.ideo.com/)
- [Synectics](https://www.synecticsworld.com/)

---
## Animation Frame Budget
**Category:** ui | **Type:** methodology | **Tags:** mobile, analytics

Frame rendering performance target for smooth motion.

**Examples**
- 16.67ms per frame target
- Main thread budget 120ms
- Skipped frame monitoring
- Device-specific budgets

**Do's and Don'ts**

*Do's*
- Profile on target devices
- Optimize expensive ops
- Reduce layer complexity
- Test across hardware

*Don'ts*
- 30fps tolerance
- Desktop performance only
- No frame timing tools
- Ignore dropped frames

**References**
- [Apple: CADisplayLink](https://developer.apple.com/documentation/quartzcore/cadisplaylink)
- [Android Developer](https://developer.android.com/)

---
## App Clip
**Category:** ui | **Type:** pattern | **Tags:** mobile

Lightweight iOS app experience no download.

**Examples**
- Starbucks App Clip order
- Parking payment Clip
- Event ticket Clip
- 50MB size limit

**Do's and Don'ts**

*Do's*
- Single focused function
- Core ML integration
- Passkeys Sign in Apple
- AR Quick Look support

*Don'ts*
- Full app experience
- Multiple features
- Large download size
- No Apple integration

**References**
- [Apple: App Clips](https://developer.apple.com/app-clips/)
- [App Clips Dev](https://www.appclips.dev/)

---
## App Gesture Back
**Category:** ui | **Type:** pattern | **Tags:** mobile, interaction

Edge swipe returns to previous screen.

**Examples**
- iOS left-edge swipe back
- Android full-screen swipe
- 50px edge gesture zone
- Visual drag preview

**Do's and Don'ts**

*Do's*
- Consistent platform gesture
- Visual edge indicator
- Minimum 44px trigger zone
- Escape hatch menu button

*Don'ts*
- Swipe anywhere randomly
- No visual feedback
- Conflicts with horizontal scroll
- Desktop-only back

**References**
- [Apple HIG: Back Navigation](https://developer.apple.com/design/human-interface-guidelines/back-navigation)
- [Material Design](https://material.io/)

---
## App Icon Grid
**Category:** ui | **Type:** pattern | **Tags:** mobile

Home screen icon arrangement and spacing.

**Examples**
- iOS 5x4 icon grid
- Android adaptive icons
- App icon corner radius
- Launch screen consistency

**Do's and Don'ts**

*Do's*
- Match platform grid
- Consistent icon style
- Proper safe area spacing
- Multiple format exports

*Don'ts*
- Desktop icon design
- Inconsistent grid spacing
- Missing adaptive icons
- Wrong corner radius

**References**
- [Apple: App Store Product Page](https://developer.apple.com/app-store/product-page/)
- [Material Design](https://m3.material.io/)

---
## App State Restoration
**Category:** strategy | **Type:** methodology | **Tags:** mobile, strategy

Previous session state reload on app relaunch.

**Examples**
- Scroll position restoration
- Form data preservation
- Tab state memory
- Draft persistence

**Do's and Don'ts**

*Do's*
- Automatic state capture
- Cross-device sync
- Privacy-respecting storage
- Crash recovery support

*Don'ts*
- No state preservation
- Login required every launch
- Lost form progress
- Manual state saving

**References**
- [Apple: State Restoration](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle/preparing_your_ui_for_app_state_restoration)
- [Android Developer](https://developer.android.com/)

---
## App Store Screenshot
**Category:** ui | **Type:** tool | **Tags:** mobile, documentation

Marketing visuals for app store product pages.

**Examples**
- iPhone 6.7 display mockup
- Feature highlight carousel
- App preview video loop
- Localized screenshots

**Do's and Don'ts**

*Do's*
- Platform-specific mockups
- Feature-first hierarchy
- Clear value proposition
- A/B test screenshots

*Don'ts*
- Desktop screenshots
- Feature list overload
- Low-quality mockups
- Generic stock photos

**References**
- [Apple: App Store Product Page](https://developer.apple.com/app-store/product-page/)
- [Google Play](https://play.google.com/)

---
## ARIA
**Category:** ui | **Type:** tool | **Tags:** accessibility, web

Accessible Rich Internet Applications - attributes for dynamic content.

**Examples**
- aria-expanded for accordions
- aria-live for announcements
- aria-label for unlabeled icons
- role='alert' for errors

**Do's and Don'ts**

*Do's*
- Use as last resort (prefer semantics)
- Validate ARIA implementation
- Test with screen readers
- Document custom ARIA

*Don'ts*
- aria-* on static content
- Invalid ARIA values
- ARIA hiding content
- Untested ARIA patterns

**References**
- [W3C: ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [WebAIM: ARIA Basics](https://webaim.org/techniques/aria/)

---
## ARIA Live Regions
**Category:** ui | **Type:** pattern | **Tags:** accessibility, interaction

Announce dynamic content changes screen readers.

**Examples**
- aria-live=polite toast
- aria-live=assertive urgent
- aria-atomic complete message
- Role alert status

**Do's and Don'ts**

*Do's*
- Polite vs assertive correct
- Screen reader test
- Concise announcement text
- Timeout management

*Don'ts*
- ARIA everywhere
- No screen reader test
- Verbose announcements
- Wrong politeness level

**References**
- [MDN: ARIA Live Regions](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Live_Regions)
- [W3C](https://www.w3.org/)

---
## Artistic Fonts
**Category:** ui | **Type:** concept | **Tags:** typography

Highly stylized, decorative typefaces designed for visual impact and expression. Artistic fonts are used sparingly for headlines, branding, or special occasions to create distinctive visual statements.

**Examples**
- Using a script font for wedding invitation headers
- Applying display fonts for event posters and banners
- Choosing hand-drawn fonts for creative agency branding
- Using retro fonts for nostalgic design themes

**Do's and Don'ts**

*Do's*
- Use artistic fonts for headlines and branding only
- Ensure artistic fonts maintain readability
- Test artistic fonts at intended sizes
- Limit to one artistic font per interface

*Don'ts*
- Use artistic fonts for body text
- Apply artistic fonts to lengthy content
- Choose artistic fonts without considering context
- Overuse decorative typefaces

**References**
- [Canva: A Beautifully Illustrated Glossary of Typographic Terms](https://www.canva.com/learn/typography-terms/)
- [UX Design Institute: Typography Best Practices](https://www.uxdesigninstitute.com/blog/typography-best-practices/)

---
## Asset Sheet
**Category:** ui | **Type:** tool | **Tags:** documentation, design-systems

Organized collection of production-ready design files and specifications.

**Examples**
- SVG icons with 32px/24px variants
- Color variables exported as CSS
- Typography styles with web-safe fallbacks
- Component PNGs at 3x resolution

**Do's and Don'ts**

*Do's*
- Export at correct resolutions
- Include file naming convention
- Provide format options
- Specify file sizes

*Don'ts*
- Zip everything together
- Forget format variations
- No naming system
- Mix source and export files

**References**
- [Sketch: Exporting](https://www.sketch.com/docs/exporting/)
- [Zeplin](https://zeplin.io/)

---
## Assumption Mapping
**Category:** strategy | **Type:** tool | **Tags:** strategy

Risk-prioritize untested product hypotheses.

**Examples**
- 23 assumptions mapped
- 6 high-risk must validate
- Desirability 4.2 Viability 3.1
- Weekly validation plan

**Do's and Don'ts**

*Do's*
- All 3 risk types (D/V/F)
- Team scoring consensus
- Timeboxed validation
- Progress tracking

*Don'ts*
- Risk-blind prioritization
- Solo assumption mapping
- Never validated
- All assumptions equal

**References**
- [Strategyzer: Assumption Mapping](https://www.strategyzer.com/library/assumption-mapping)
- [Lean Stack](https://leanstack.com/)

---
## Async Design Review
**Category:** management | **Type:** methodology | **Tags:** processes

Asynchronous documented feedback system.

**Examples**
- Figma comment threads
- Loom video walkthroughs
- Slack #design-review channel
- 48hr feedback SLA

**Do's and Don'ts**

*Do's*
- Clear review questions
- Visual annotations
- Actionable feedback only
- Single source of truth

*Don'ts*
- Email feedback chains
- Verbal hallway chats
- No documentation
- Mixed feedback channels

**References**
- [Figma: Async Design Review](https://www.figma.com/blog/async-design-review/)
- [Linear](https://www.linear.app/)

---
## Atomic Design
**Category:** ui | **Type:** methodology | **Tags:** design-systems, framework

Methodology organizing UI components into five hierarchical levels: atoms, molecules, organisms, templates, and pages for scalable systems.

**Examples**
- Atoms: button, input field
- Molecules: search form, product card
- Organisms: header, footer
- Templates: homepage layout
- Pages: actual content pages

**Do's and Don'ts**

*Do's*
- Start with atomic elements first
- Build bottom-up progressively
- Document component anatomy
- Test at each abstraction level

*Don'ts*
- Jump directly to page-level design
- Mix abstraction levels randomly
- Ignore atomic consistency
- Skip documentation at each level

**References**
- [Atomic Design by Brad Frost](https://atomicdesign.bradfrost.com/)
- [Pattern Lab](https://patternlab.io/)

---
## Atomic Design Workflow
**Category:** ui | **Type:** methodology | **Tags:** processes, design-systems

Atoms Molecules Organisms Templates Pages build order.

**Examples**
- Atoms: buttons inputs
- Molecules: search forms
- Organisms: cards headers
- Templates: page layouts
- Pages: content pages

**Do's and Don'ts**

*Do's*
- Bottom-up construction
- Documentation each level
- Testing each abstraction
- Cross-team component library

*Don'ts*
- Page-first design
- Skip documentation
- No testing protocol
- Designer silos

**References**
- [Atomic Design](https://atomicdesign.bradfrost.com/)
- [Pattern Lab](https://patternlab.io/)

---
## Backlog Refinement
**Category:** management | **Type:** methodology | **Tags:** processes

Prioritization grooming 1-2 weeks ahead.

**Examples**
- Story splitting
- Acceptance criteria writing
- Estimation refinement
- 1-2hr weekly session

**Do's and Don'ts**

*Do's*
- INVEST story criteria
- 3 Amigos review
- Capacity-based prioritization
- Documentation updated

*Don'ts*
- No refinement time
- Large unwieldy stories
- No acceptance criteria
- Monthly refinement

**References**
- [Agile Alliance: Backlog Refinement](https://www.agilealliance.org/glossary/backlog-refinement/)
- [Scrum Guides](https://scrumguides.org/)

---
## Beta Testing
**Category:** ux | **Type:** methodology | **Tags:** testing

Releasing a product or feature to a limited group of real users in production environment before full launch. Beta testing identifies issues, gathers feedback, and validates performance with actual usage patterns and data.

**Examples**
- Releasing a new feature to 5% of users to catch bugs and gather initial feedback
- Inviting power users to test beta version and provide early feedback

**Do's and Don'ts**

*Do's*
- Select beta users who match target audience
- Set clear expectations about beta status
- Provide feedback channels for beta users
- Monitor metrics and gather qualitative feedback
- Plan for rollback if major issues arise
- Thank and reward beta participants

*Don'ts*
- Beta test with all users at once
- Release beta without monitoring plan
- Ignore feedback from beta users
- Skip internal testing before beta
- Leave features in beta indefinitely
- Forget to communicate with beta testers

**References**
- [ProductPlan: Beta Testing Guide](https://www.productplan.com/glossary/beta-test/)
- [Maze: Beta Testing Best Practices](https://maze.co/guides/beta-testing/)

---
## Bottom Navigation
**Category:** ui | **Type:** pattern | **Tags:** navigation, mobile

Fixed bottom bar with 4-5 primary destinations (common in mobile apps).

**Examples**
- Home, Search, Add, Notifications, Profile
- iOS tab bar pattern
- Material Design bottom nav
- E-commerce cart + categories

**Do's and Don'ts**

*Do's*
- Limit to 5 tabs maximum
- Use icon + label
- Thumb-friendly positioning
- Highlight current location

*Don'ts*
- More than 5 tabs
- Text-only labels
- Bury primary actions
- Inconsistent tab behavior

**References**
- [Material Design: Bottom Navigation](https://m3.material.io/components/bottom-navigation/overview)
- [iOS HIG: Tab Bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)

---
## Bounce Rate
**Category:** ux | **Type:** tool | **Tags:** analytics

Percentage single-page sessions without interaction.

**Examples**
- 42% landing page bounce
- 28% product page bounce
- Mobile bounce 51%
- Bounce by traffic source

**Do's and Don'ts**

*Do's*
- Segment by traffic source
- Mobile vs desktop split
- Content performance proxy
- A/B test improvements

*Don'ts*
- All pages equal
- Desktop-only analysis
- No segmentation
- Ignore traffic quality

**References**
- [Hotjar: Bounce Rate](https://www.hotjar.com/blog/bounce-rate/)
- [CXL](https://cxl.com/)

---
## Brainstorming
**Category:** strategy | **Type:** methodology | **Tags:** ideation

A group creativity technique for generating a large number of ideas in a short time by encouraging free thinking and deferring judgment. Brainstorming leverages diverse perspectives to explore solution spaces broadly before evaluating ideas.

**Examples**
- Running a 30-minute session where team members generate ideas for improving onboarding flow
- Using brainstorming to explore different approaches to solving a navigation problem

**Do's and Don'ts**

*Do's*
- Defer judgment and criticism during ideation
- Encourage wild and ambitious ideas
- Build on others' ideas
- Aim for quantity over quality initially
- Use a facilitator to keep energy and focus
- Document all ideas visually

*Don'ts*
- Critique or evaluate ideas during generation
- Let dominant voices monopolize the session
- Stop too early before exhausting possibilities
- Brainstorm without a clear problem statement
- Skip the synthesis and prioritization step afterward
- Brainstorm individually when group diversity adds value

**References**
- [Interaction Design Foundation: Brainstorming](https://www.interaction-design.org/literature/article/learn-how-to-use-the-best-ideation-methods-brainstorming)
- [Nielsen Norman Group: Brainstorming Guidelines](https://www.nngroup.com/articles/better-brainstorming/)

---
## Brainwriting 6-3-5
**Category:** ux | **Type:** tool | **Tags:** ideation

Six people write 3 ideas in 5 minutes then rotate papers.

**Examples**
- 108 ideas in 30 minutes
- Silent generation phase
- Build on others' ideas
- Structured rotation

**Do's and Don'ts**

*Do's*
- Strict time limits
- Silent writing
- Read before adding
- Full 6 rounds

*Don'ts*
- Verbal discussion
- Skip rotations
- Ignore previous ideas
- Fewer than 6 people

**References**
- [MindTools: Brainwriting](https://www.mindtools.com/)
- [Creative Problem Solving](https://www.creativeeducationfoundation.org/)

---
## Brand Guidelines
**Category:** strategy | **Type:** tool | **Tags:** documentation

Rules maintaining visual identity across touchpoints.

**Examples**
- Logo safe area requirements
- Color usage hierarchy
- Typography pairing rules
- Photography style guide

**Do's and Don'ts**

*Do's*
- Include motion guidelines
- Specify digital vs print
- Cover social media formats
- Test across mediums

*Don'ts*
- Static logo sheet only
- Missing motion rules
- Generic color rules
- No format specifications

**References**
- [Brandfolder](https://brandfolder.com/)
- [Frontify](https://frontify.com/)

---
## Breadcrumb Navigation
**Category:** ui | **Type:** pattern | **Tags:** navigation

Shows current location and path from home (Home > Category > Product).

**Examples**
- Home > Electronics > Phones > iPhone 15
- Category > Subcategory > Item
- Account > Billing > Invoices
- Documentation > API > Endpoints

**Do's and Don'ts**

*Do's*
- Show complete path hierarchy
- Use clear separators (> >>)
- Link all but current location
- Mobile-responsive truncation

*Don'ts*
- Link current page in breadcrumb
- Use vague category names
- Hide breadcrumbs on mobile
- Inconsistent breadcrumb style

**References**
- [NN/g: Breadcrumb Navigation](https://www.nngroup.com/articles/breadcrumbs/)
- [UX Planet: Navigation Elements](https://uxplanet.org/ux-glossary-navigation/)

---
## Breadcrumb Trail
**Category:** ui | **Type:** pattern | **Tags:** navigation

Hierarchical path showing current location (Home > Category > Subcategory).

**Examples**
- Home > Products > Electronics > Phones
- Documentation > API > Authentication
- Account > Orders > #12345
- Blog > Design > UI Patterns

**Do's and Don'ts**

*Do's*
- Complete clickable path
- Clear hierarchy separators
- Current location unlinked
- Mobile-responsive truncation

*Don'ts*
- Link current location
- Vague category names
- Hide on mobile
- Inconsistent styling

**References**
- [NN/g: Breadcrumbs](https://www.nngroup.com/articles/breadcrumbs/)
- [Material Design: Breadcrumb](https://m3.material.io/foundations/layout/understanding-layout/overview)

---
## Browser Support Matrix
**Category:** ui | **Type:** tool | **Tags:** web

Specific browsers and versions officially supported by website.

**Examples**
- Chrome 90+, Firefox 88+, Safari 15+, Edge 91+
- Mobile: iOS Safari 15+, Android Chrome 90+
- IE11 polyfill support only
- Annual support matrix update

**Do's and Don'ts**

*Do's*
- Publish public matrix
- Automate compatibility tests
- Document polyfill strategy
- Quarterly browser testing

*Don'ts*
- Support everything
- Hide matrix from devs
- Annual testing only
- Ignore mobile browsers

**References**
- [Browserslist](https://browserslist.dev/)
- [Can I Use](https://caniuse.com/)

---
## Build-Measure-Learn
**Category:** strategy | **Type:** methodology | **Tags:** strategy

MVP feedback loop continuous product learning.

**Examples**
- Landing page MVP
- 100 signups 7-day waitlist
- Pivot to paid feature
- 3-day BML cycles

**Do's and Don'ts**

*Do's*
- Smallest viable test
- Quantitative + qualitative
- Pre-defined success
- Rapid iteration

*Don'ts*
- Big bang launch
- Qualitative feedback only
- No success criteria
- Monthly learning cycles

**References**
- [Lean Startup: Principles](https://www.leanstartup.com/principles)
- [Eric Ries](https://ericries.com/)

---
## Business Dashboard
**Category:** ui | **Type:** tool | **Tags:** data-visualization

Multi-chart display of key business metrics on single performance overview.

**Examples**
- Sales dashboard with 6 KPIs
- Marketing campaign tracker
- Customer support metrics
- Inventory levels overview

**Do's and Don'ts**

*Do's*
- Prioritize top 4-6 metrics
- Consistent time periods
- Mobile responsive layout
- Clear action thresholds

*Don'ts*
- 20+ metrics displayed
- Inconsistent date ranges
- No visual hierarchy
- Raw numbers only

**References**
- [Tableau Dashboard](https://www.tableau.com/dashboard)
- [Looker Studio](https://lookerstudio.google.com/)

---
## Card Sorting
**Category:** ux | **Type:** methodology | **Tags:** research, information-architecture

A research method where participants organize topics or content into categories that make sense to them. Card sorting reveals how users mentally model information and helps inform information architecture and navigation structure.

**Examples**
- Having users group feature names into categories to inform app navigation structure
- Asking participants to organize content topics to design a website's information hierarchy

**Do's and Don'ts**

*Do's*
- Use realistic content labels that users will encounter
- Choose between open sorting (users create categories) or closed sorting (predefined categories)
- Test with 15-30 participants for reliable patterns
- Look for agreement in groupings across participants
- Follow up with tree testing to validate structure
- Use digital tools for remote card sorting

*Don'ts*
- Use too many cards (30-60 is typical maximum)
- Use internal jargon or unclear labels
- Rely on card sorting alone for IA decisions
- Skip analysis of disagreements and outliers
- Force participants into categories that don't make sense

**References**
- [Nielsen Norman Group: Card Sorting](https://www.nngroup.com/articles/card-sorting-definition/)
- [Optimal Workshop: Card Sorting Guide](https://www.optimalworkshop.com/learn/101s/card-sorting/)

---
## Cascade Layers
**Category:** ui | **Type:** tool | **Tags:** web

Explicit CSS cascade control priority.

**Examples**
- @layer base components utilities;
- Third-party CSS isolation
- Reset override control
- Specificity wars solved

**Do's and Don'ts**

*Do's*
- Logical layer ordering
- Third-party isolation
- Documentation layer order
- Automated linting

*Don'ts*
- Specificity hacks
- !important everywhere
- Undocumented layers
- Manual order management

**References**
- [MDN: Cascade Layers](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade_layers)
- [CSS-Tricks](https://css-tricks.com/)

---
## Chart Hover Tooltip
**Category:** ui | **Type:** pattern | **Tags:** data-visualization, interaction

Pop-up panel shows precise values and context on data point interaction.

**Examples**
- Exact sales value + % change
- Timestamp + raw data
- Category breakdown tooltip
- Confidence interval display

**Do's and Don'ts**

*Do's*
- Show all relevant context
- Consistent positioning
- Keyboard accessible
- Truncate intelligently

*Don'ts*
- Offset positioning only
- Missing units/formatting
- Slow loading content
- Desktop hover only

**References**
- [Chart.js: Tooltip Configuration](https://www.chartjs.org/docs/latest/configuration/tooltip.html)
- [D3.js](https://d3js.org/)

---
## Churn Rate
**Category:** strategy | **Type:** tool | **Tags:** analytics

Percentage users abandoning product over time period.

**Examples**
- Monthly churn 4.2%
- Revenue churn 3.1%
- 90-day churn analysis
- Segment churn by cohort

**Do's and Don'ts**

*Do's*
- Track revenue churn
- Cohort churn curves
- Exit survey correlation
- Win-back experiments

*Don'ts*
- Gross churn only
- No revenue analysis
- Monthly aggregate only
- Ignore reactivation

**References**
- [ProductPlan: Churn Rate](https://www.productplan.com/glossary/churn-rate/)
- [Baremetrics](https://baremetrics.com/)

---
## Cognitive Load
**Category:** ux | **Type:** principle

Mental effort required to understand/use interface.

**Examples**
- Single decision per screen
- Familiar design patterns
- Clear visual hierarchy
- Consistent navigation

**Do's and Don'ts**

*Do's*
- Minimize working memory use
- Familiar metaphors first
- Chunk information logically
- Progressive disclosure

*Don'ts*
- Complex multi-step screens
- Novel interaction models
- Information overload
- Inconsistent patterns

**References**
- [NN/g: Reduce Cognitive Load](https://www.nngroup.com/articles/reduce-cognitive-load/)
- [CXL](https://cxl.com/)

---
## Cognitive Walkthrough
**Category:** ux | **Type:** methodology | **Tags:** testing

An expert evaluation method that assesses how easy an interface is to learn by walking through tasks from a new user's perspective. Cognitive walkthrough focuses on learnability and whether users can understand what to do without training.

**Examples**
- Evaluating a new feature by asking "Will users know what to do?" at each step
- Walking through first-time user flow to identify where new users might get confused

**Do's and Don'ts**

*Do's*
- Define realistic tasks and user personas
- Ask four key questions at each step
- Focus on first-time use and learnability
- Document assumptions and findings
- Involve multiple evaluators
- Use early in design process

*Don'ts*
- Evaluate expert user flows
- Skip defining user characteristics
- Rush through the walkthrough
- Focus on efficiency over learnability
- Work alone without discussion
- Use cognitive walkthrough for all usability issues

**References**
- [Nielsen Norman Group: Cognitive Walkthrough](https://www.nngroup.com/articles/cognitive-walkthrough-workshop/)
- [Usability.gov: Cognitive Walkthrough](https://www.usability.gov/how-to-and-tools/methods/cognitive-walkthroughs.html)

---
## Cohort Retention Curve
**Category:** ux | **Type:** tool | **Tags:** analytics

Retention patterns by user acquisition group.

**Examples**
- Jan cohort D30 18% retention
- Paid vs organic curves
- Feature cohort retention
- Seasonal cohort patterns

**Do's and Don'ts**

*Do's*
- Track 8+ cohorts
- Multiple dimensions
- D1 D7 D30 standard
- Benchmarking vs industry

*Don'ts*
- Single cohort analysis
- No dimension splitting
- Short-term only
- No industry context

**References**
- [Amplitude: Cohort Analysis](https://amplitude.com/blog/cohort-analysis/)

---
## Color Blindness Simulation
**Category:** ui | **Type:** tool | **Tags:** color, accessibility

A testing method that simulates how designs appear to users with different types of color vision deficiency. Common simulations include protanopia (red-blind), deuteranopia (green-blind), tritanopia (blue-blind), and achromatopsia (complete color blindness), helping identify problematic color dependencies.

**Examples**
- Testing a status indicator system (red/yellow/green) to ensure states are distinguishable without color
- Simulating deuteranopia on a data visualization to check if chart segments remain identifiable
- Verifying that error states are not communicated solely through red color
- Checking that link colors are distinguishable from body text under all simulations

**Do's and Don'ts**

*Do's*
- Test all three major types: protanopia, deuteranopia, tritanopia
- Ensure critical information has non-color indicators (icons, patterns, labels)
- Use simulation early in the design process, not just at the end
- Test interactive states (hover, focus, selected) under simulation
- Consider that ~8% of men have some form of color vision deficiency

*Don'ts*
- Rely on red/green distinction for critical UI elements
- Use color as the only differentiator between states
- Assume passing one simulation means passing all
- Skip testing data visualizations and charts
- Forget to test both light and dark mode under simulation

**References**
- [Coblis: Color Blindness Simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/)
- [Stark: Accessibility Tools for Figma](https://www.getstark.co/)

---
## Color Contrast Testing
**Category:** ui | **Type:** tool | **Tags:** 

A method for verifying that color combinations meet accessibility standards for readability. Testing measures the luminance ratio between foreground and background colors against WCAG thresholds: 4.5:1 for normal text (AA), 3:1 for large text (AA), and 7:1 for enhanced contrast (AAA).

**Examples**
- Testing body text color against page background to ensure 4.5:1 minimum ratio
- Verifying that button text meets contrast requirements on both default and hover states
- Checking placeholder text contrast (often fails due to low-contrast gray)
- Validating icon contrast against various background colors in the system

**Do's and Don'ts**

*Do's*
- Test all text/background combinations in your design system
- Include hover, focus, and disabled states in testing
- Test against both light and dark mode backgrounds
- Document passing color pairs for easy reference
- Re-test when any color values change

*Don'ts*
- Assume similar colors have similar contrast ratios
- Skip testing for large text (still requires 3:1)
- Ignore non-text elements (icons, focus rings, borders)
- Test only in isolation without real UI context
- Rely solely on automated tools without visual verification

**References**
- [WCAG 2.1: Contrast (Minimum)](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- [WebAIM: Contrast Checker](https://webaim.org/resources/contrastchecker/)

---
## Color Extraction
**Category:** ui | **Type:** tool | **Tags:** 

A method for deriving color palettes from existing visual sources such as photographs, brand materials, or artwork. Extraction identifies dominant, secondary, and accent colors from an image to create cohesive palettes grounded in real-world references.

**Examples**
- Extracting brand colors from a company logo to build a UI palette
- Pulling dominant colors from a hero image to create a themed landing page
- Deriving a color scheme from a mood board for a new product direction
- Using a photograph as the basis for an illustration color palette

**Do's and Don'ts**

*Do's*
- Use multiple source images to find common color themes
- Adjust extracted colors for accessibility (contrast, saturation)
- Extract both dominant and subtle accent colors
- Consider the emotional tone of source images
- Validate extracted palettes against UI requirements

*Don'ts*
- Use extracted colors directly without accessibility testing
- Rely on a single image for an entire palette
- Ignore that extracted colors may lack sufficient contrast
- Forget to create tonal variations from extracted base colors
- Assume extracted palettes work for all UI states (hover, disabled, etc.)

**References**
- [Adobe Color: Extract Theme](https://color.adobe.com/create/image)
- [Coolors: Image Color Palette Generator](https://coolors.co/image-picker)

---
## Color Overlay Testing
**Category:** ui | **Type:** methodology | **Tags:** color, accessibility

A method for verifying color readability and visual hierarchy when UI elements are layered with transparency or overlays. Testing ensures that text, icons, and interactive elements remain legible on semi-transparent backgrounds, modals, scrims, and overlapping surfaces.

**Examples**
- Testing modal scrim opacity to ensure background content is sufficiently dimmed
- Verifying text readability on cards with semi-transparent backgrounds over images
- Checking toast notifications remain legible over varying page content
- Testing dropdown menus with transparency against different underlying colors

**Do's and Don'ts**

*Do's*
- Test overlays against multiple background scenarios (light, dark, colorful, images)
- Verify contrast ratios for text on the resulting blended colors
- Consider how overlays appear in both light and dark modes
- Test with actual content, not just solid test backgrounds
- Document approved overlay opacity values for consistency

*Don'ts*
- Assume a single opacity value works on all backgrounds
- Skip testing overlays on image-heavy pages
- Forget that transparency compounds when multiple overlays stack
- Test only against white or neutral backgrounds
- Ignore how overlays affect focus states and interactive elements beneath

**References**
- [Material Design: Elevation and Shadows](https://m3.material.io/styles/elevation/overview)
- [W3C: Understanding Contrast](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)

---
## Color Proportion Rule
**Category:** ui | **Type:** methodology | **Tags:** color

A color distribution guideline that suggests using a dominant color for 60% of the design, a secondary color for 30%, and an accent color for 10%. This ratio creates visual balance and hierarchy while preventing color overload.

**Examples**
- Using a neutral background (60%), brand color for headers and cards (30%), and a contrasting CTA color (10%)
- Applying white/light gray as dominant, dark gray for text and containers, and blue for interactive elements
- In a dashboard: light background (60%), data containers (30%), status indicators and buttons (10%)

**Do's and Don'ts**

*Do's*
- Use the dominant 60% for backgrounds and large surfaces
- Apply the 30% to secondary elements like navigation, cards, or sections
- Reserve the 10% for calls to action and key interactive elements
- Treat the rule as a guideline, not an exact formula
- Adjust ratios slightly based on content density and purpose

*Don'ts*
- Use the accent color for large areas
- Make the secondary color compete with the accent
- Apply the rule rigidly without considering content needs
- Forget that the rule applies to visual weight, not pixel count
- Use multiple accent colors at 10% each (dilutes impact)

**References**
- [UX Design Institute: 60-30-10 Color Rule](https://www.uxdesigninstitute.com/blog/60-30-10-color-rule/)
- [Canva: The 60-30-10 Rule](https://www.canva.com/learn/60-30-10-rule/)

---
## Color Scale Generation
**Category:** ui | **Type:** methodology | **Tags:** color, design-systems

A method for creating systematic tonal variations of a base color, typically producing a scale from light to dark (e.g., 50, 100, 200... 900). Color scales provide consistent options for different UI states, backgrounds, and text while maintaining color harmony.

**Examples**
- Generating a blue scale from near-white (blue-50) to near-black (blue-900) for a design system
- Creating a gray scale with 10 steps to handle backgrounds, borders, and text colors
- Building semantic scales where success-100 is a light tint and success-700 is the darkest usable shade

**Do's and Don'ts**

*Do's*
- Use perceptually uniform color spaces (LCH/LAB) for more even steps
- Ensure sufficient contrast between adjacent steps for usability
- Include enough steps to cover backgrounds, borders, text, and hover states
- Test scales in both light and dark mode contexts
- Document the intended use for each step (e.g., 500 = default, 600 = hover)

*Don'ts*
- Generate scales by simply adjusting lightness in RGB (produces uneven results)
- Create too many steps (10-12 is usually sufficient)
- Assume linear lightness changes produce linear visual changes
- Forget to verify contrast ratios between text and background steps
- Mix different generation methods within the same design system

**References**
- [Stripe: Designing Accessible Color Systems](https://stripe.com/blog/accessible-color-systems)
- [Tailwind CSS: Customizing Colors](https://tailwindcss.com/docs/customizing-colors)

---
## Color Schemes
**Category:** ui | **Type:** methodology | **Tags:** color

A structured method for selecting harmonious color combinations based on their relationships on the color wheel. Common schemes include complementary (opposite colors), analogous (adjacent colors), triadic (three equidistant colors), and split-complementary (one color plus two adjacent to its complement).

**Examples**
- Using a complementary scheme (blue and orange) to create strong visual contrast for CTAs
- Applying an analogous scheme (blue, blue-green, green) for a calm, cohesive interface
- Choosing a triadic scheme (red, yellow, blue) for a vibrant, balanced design
- Using split-complementary to get contrast without the intensity of pure complementary

**Do's and Don'ts**

*Do's*
- Start with a primary color and derive others using scheme rules
- Use complementary schemes for elements that need to stand out
- Use analogous schemes for harmonious, low-contrast designs
- Adjust saturation and lightness within the scheme for variety
- Test schemes with real content and UI components

*Don'ts*
- Use all colors from a scheme at equal intensity
- Apply triadic schemes without careful balance (can be overwhelming)
- Ignore the 60-30-10 rule when applying color schemes
- Rely solely on the color wheel without testing in context
- Forget that color schemes are starting points, not rigid rules

**References**
- [Adobe Color: Color Wheel](https://color.adobe.com/create/color-wheel)
- [Interaction Design Foundation: Color Theory](https://www.interaction-design.org/literature/topics/color-theory)

---
## Color Spaces
**Category:** ui | **Type:** tool | **Tags:** color

A color space is a mathematical model that defines how colors are represented as numerical values. Different color spaces serve different purposes: RGB for screens, CMYK for print, HSL/HSB for intuitive adjustments, and LAB/LCH for perceptually uniform color work.

**Examples**
- Using RGB or Hex values when defining colors for web interfaces
- Switching to HSL to quickly adjust lightness or saturation while keeping the same hue
- Working in CMYK when preparing assets for print production
- Using LAB color space to create visually uniform color gradients

**Do's and Don'ts**

*Do's*
- Use HSL/HSB for manual color adjustments and exploration
- Use RGB/Hex for final implementation in digital products
- Consider LAB/LCH when creating color scales that need perceptual uniformity
- Document which color space your design system uses as source of truth
- Convert colors properly when moving between color spaces

*Don'ts*
- Mix color spaces without understanding conversion implications
- Use RGB for intuitive color adjustments (hard to predict results)
- Ignore color space when collaborating across design and development
- Assume colors look identical across different color spaces
- Forget that some colors exist in one space but not another (gamut limits)

**References**
- [MDN: Color Spaces](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)
- [CSS Color Level 4: Color Spaces](https://www.w3.org/TR/css-color-4/)

---
## Color Tokens
**Category:** ui | **Type:** methodology | **Tags:** color, design-systems

A systematic approach to organizing colors in design systems using hierarchical abstraction levels: primitive tokens (raw color values), semantic tokens (purpose-based names like "text-primary"), and component tokens (context-specific like "button-background"). This structure enables consistent theming and maintainability.

**Examples**
- Primitive: `blue-500: #3B82F6` → Semantic: `color-action: blue-500` → Component: `button-primary-bg: color-action`
- Changing `color-action` from blue to green updates all components referencing it
- Using `text-primary` instead of `gray-900` so dark mode can remap it to `gray-100`

**Do's and Don'ts**

*Do's*
- Start with primitive tokens as the foundation
- Create semantic tokens that describe purpose, not appearance
- Use component tokens sparingly for specific overrides
- Name tokens consistently across the system
- Document the relationship between token levels
- Design semantic tokens with theming in mind

*Don'ts*
- Reference primitive tokens directly in components
- Create semantic tokens for every possible use case
- Use color names in semantic tokens (e.g., "blue-text")
- Skip the semantic layer and go straight to component tokens
- Forget to consider dark mode when designing the token structure
- Create circular references between token levels

**References**
- [Tokens Studio: Design Tokens](https://tokens.studio/)
- [Design Tokens W3C Community Group](https://www.w3.org/community/design-tokens/)

---
## Column Chart
**Category:** ui | **Type:** tool | **Tags:** data-visualization

Vertical bars compare category values side-by-side for easy magnitude comparison.

**Examples**
- Monthly sales by product line
- Website traffic by source
- Survey results by demographic
- Budget allocation by department

**Do's and Don'ts**

*Do's*
- Order categories logically
- Start y-axis at zero
- Limit to 7-12 categories
- Label bars directly

*Don'ts*
- 3D effects or shadows
- Horizontal orientation
- Truncated y-axis
- Too many categories (>15)

**References**
- [Data to Viz: Bar Chart](https://www.data-to-viz.com/graph/bar.html)
- [Extreme Presentation](https://extremepresentation.com/)

---
## Comparison Testing
**Category:** ux | **Type:** methodology | **Tags:** testing

A research method where participants evaluate multiple design alternatives side-by-side to determine preferences and relative strengths. Comparison testing helps teams make decisions between competing approaches by understanding user reasoning.

**Examples**
- Showing users three different homepage layouts and asking which best helps them find information
- Comparing two onboarding flows to see which users find clearer and more engaging

**Do's and Don'ts**

*Do's*
- Test 2-4 alternatives maximum
- Rotate presentation order to avoid bias
- Ask participants to explain their preferences
- Look for patterns across participants
- Test alternatives at similar fidelity levels
- Use findings to inform hybrid solutions

*Don'ts*
- Show too many alternatives at once
- Present alternatives in the same order to everyone
- Accept preference without understanding reasoning
- Assume the most popular option is always best
- Compare alternatives at different fidelity levels
- Let comparison testing replace usability testing

**References**
- [Nielsen Norman Group: Preference Testing](https://www.nngroup.com/articles/preference-testing/)
- [Maze: A/B Testing vs Preference Testing](https://maze.co/guides/usability-testing/ab-testing-vs-preference-testing/)

---
## Competitive Analysis
**Category:** strategy | **Type:** methodology | **Tags:** research

Systematic evaluation of competing products, services, or companies to understand their strengths, weaknesses, features, and strategies. Competitive analysis identifies market opportunities, industry standards, and differentiation opportunities.

**Examples**
- Reviewing 5-10 similar apps to understand common features and design patterns before building
- Analyzing competitor pricing models and value propositions to inform product strategy

**Do's and Don'ts**

*Do's*
- Focus on direct and indirect competitors
- Look at features, design patterns, and user experience
- Document both strengths and weaknesses
- Consider business model and positioning
- Update analysis regularly as market evolves
- Use findings to inform, not dictate, design decisions

*Don'ts*
- Copy competitors without understanding user needs
- Only analyze obvious direct competitors
- Ignore competitors' weaknesses and failures
- Treat competitive analysis as one-time activity
- Let competitor features drive your roadmap
- Forget to analyze why competitors made certain choices

**References**
- [Nielsen Norman Group: Competitive UX Analysis](https://www.nngroup.com/articles/competitive-usability-evaluations/)
- [Product School: Competitive Analysis Guide](https://productschool.com/blog/product-management-2/competitive-analysis-templates-examples)

---
## Component Adoption Rate
**Category:** ui | **Type:** methodology | **Tags:** design-systems, analytics

Percentage of new designs using approved system components versus custom/ad-hoc implementations, measuring system effectiveness.

**Examples**
- 85% of new buttons use system Button
- 92% cards use system Card component
- 78% forms use system Input variants
- 65% modals use system Modal

**Do's and Don'ts**

*Do's*
- Track across design files monthly
- Set adoption targets by component
- Celebrate adoption wins
- Identify resistance patterns

*Don'ts*
- Ignore adoption tracking
- Penalize low adoption
- Track only completed projects
- Compare teams unfairly

**References**
- [Design Systems Metrics](https://www.designsystems.com/metrics/)
- [DS Metrics](https://dsmetrics.com/)

---
## Component Deprecation
**Category:** ui | **Type:** methodology | **Tags:** design-systems, processes

Structured process for retiring outdated components while maintaining backward compatibility and smooth team transition.

**Examples**
- Mark legacy-button as deprecated
- 3-month sunset period
- Provide migration guide
- Auto-redirect in documentation

**Do's and Don'ts**

*Do's*
- Give generous sunset periods
- Provide migration tooling
- Update all internal usage first
- Communicate widely

*Don'ts*
- Remove components abruptly
- Break existing implementations
- Ignore usage analytics
- Skip migration support

**References**
- [Design Systems News: Deprecation](https://designsystems.news/deprecation/)

---
## Component Documentation
**Category:** ui | **Type:** tool | **Tags:** documentation, design-systems

Specs detailing component anatomy, states, variants, and usage guidelines.

**Examples**
- Button component with 8 variants documented
- Modal anatomy with overlay rules
- Form field states (error, success, disabled)
- Tooltip positioning guidelines

**Do's and Don'ts**

*Do's*
- Document all states
- Include code snippets
- Show don't tell with examples
- Specify responsive behavior

*Don'ts*
- Document only happy path
- Skip edge cases
- Use vague descriptions
- Forget accessibility notes

**References**
- [Storybook Docs](https://storybook.js.org/docs)

---
## Component Library
**Category:** ui | **Type:** tool | **Tags:** design-systems

Curated collection of reusable UI building blocks (buttons, cards, modals) with defined states, variants, and usage guidelines.

**Examples**
- Button component with primary/secondary variants
- Card component for product listings
- Modal for confirmation dialogs
- Navigation bar with multiple breakpoint variants

**Do's and Don'ts**

*Do's*
- Define all necessary states (hover, focus, disabled)
- Provide code snippets for each variant
- Include accessibility attributes
- Test across breakpoints and themes

*Don'ts*
- Build without design handoff process
- Create infinite variants
- Ignore browser inconsistencies
- Skip performance optimization

**References**
- [Storybook: Component Libraries](https://storybook.js.org/docs)

---
## Component Promotion Workflow
**Category:** ui | **Type:** methodology | **Tags:** processes, design-systems

Design system approval publishing process.

**Examples**
- RFC → Review → Promote → Publish
- Design system RFC template
- Cross-team approval
- Automated publishing

**Do's and Don'ts**

*Do's*
- Peer review required
- Documentation mandatory
- Backward compatibility
- Changelog entry

*Don'ts*
- Direct publishing
- No documentation
- Breaking changes unannounced
- Solo promotion

**References**
- [Storybook: Workflows](https://storybook.js.org/docs/workflows/)

---
## Component Reuse Ratio
**Category:** ui | **Type:** methodology | **Tags:** design-systems, analytics

Ratio of total components created to unique component types, where higher ratios indicate better reuse and system efficiency.

**Examples**
- 150 total cards / 3 card variants = 50:1
- 89 buttons / 4 button types = 22:1
- 42 modals / 2 modal variants = 21:1
- Overall reuse ratio: 28:1

**Do's and Don'ts**

*Do's*
- Benchmark against industry standards
- Track per component type
- Improve lowest ratios first
- Celebrate reuse champions

*Don'ts*
- Count total instances only
- Ignore variant quality
- Compare unrelated components
- Skip context consideration

**References**
- [Smashing Magazine: Component Reuse](https://www.smashingmagazine.com/component-reuse/)
- [DS Health](https://dshealth.com/)

---
## Component Specs
**Category:** ui | **Type:** tool | **Tags:** documentation, design-systems

Technical details for implementing specific UI components.

**Examples**
- Button spacing between elements
- Focus indicator specifications
- Loading skeleton dimensions
- Tooltip positioning rules

**Do's and Don'ts**

*Do's*
- Include spacing system
- Specify all states
- Provide codepen examples
- Cover platform differences

*Don'ts*
- Visual only specs
- Missing spacing details
- Generic state descriptions
- Desktop only

**References**
- [Primer Components](https://primer.style/components)
- [Adobe Spectrum](https://spectrum.adobe.com/)

---
## Component Variants
**Category:** ui | **Type:** pattern | **Tags:** design-systems

Different states or versions of a component (primary/secondary button, large/small size) that maintain consistent behavior and visual language.

**Examples**
- Button: primary, secondary, ghost, destructive
- Input: default, error, disabled, success
- Card: elevated, outlined, filled
- Badge: default, pill, dot

**Do's and Don'ts**

*Do's*
- Limit to 3-5 variants per component
- Define clear use cases per variant
- Maintain visual kinship
- Document visual order hierarchy

*Don'ts*
- Create unlimited variants
- Use variants inconsistently
- Ignore accessibility per variant
- Skip performance optimization

**References**
- [Design Systems Patterns](https://www.designsystems.com/patterns/)

---
## Concept Testing
**Category:** ux | **Type:** methodology | **Tags:** testing

Evaluating an idea, feature, or product concept with users before significant development investment. Concept testing validates assumptions, gauges user interest, and identifies potential issues early when changes are still inexpensive.

**Examples**
- Showing mockups of a new feature to users and asking about usefulness and clarity
- Presenting different product concepts to target customers to assess appeal and fit

**Do's and Don'ts**

*Do's*
- Test early before significant investment
- Use realistic but low-fidelity representations
- Ask about comprehension, appeal, and differentiation
- Test multiple concepts to compare
- Recruit representative users
- Focus on understanding "why" behind reactions

*Don'ts*
- Wait until development is complete to test
- Over-polish concepts, which can bias feedback
- Lead participants toward positive responses
- Test only one concept without alternatives
- Confuse concept testing with usability testing
- Make decisions based on small sample sizes

**References**
- [Maze: Concept Testing Guide](https://maze.co/guides/concept-testing/)
- [Nielsen Norman Group: Concept Evaluation](https://www.nngroup.com/articles/concept-evaluation/)

---
## Consistency Principle
**Category:** ui | **Type:** principle | **Tags:** design-systems

Same actions produce same results everywhere.

**Examples**
- Swipe left always deletes
- Primary button always right
- ESC always closes modals
- Same icons same meaning

**Do's and Don'ts**

*Do's*
- Document patterns centrally
- Component library usage
- Cross-platform consistency
- Regular design audits

*Don'ts*
- Different gestures by screen
- Moving primary button
- Icon reuse different meaning
- Platform-specific patterns

**References**
- [NN/g: Consistency](https://www.nngroup.com/articles/consistency/)
- [Interaction Design Foundation](https://www.interaction-design.org/)

---
## Container Queries
**Category:** ui | **Type:** tool | **Tags:** web

Style components based on container size not viewport.

**Examples**
- @container (min-width: 400px) {}
- Card adapts to parent width
- Component responsive internally
- Side-by-side container variants

**Do's and Don'ts**

*Do's*
- container-type: inline-size
- Self-contained components
- Fallback media queries
- Test container contexts

*Don'ts*
- Viewport media queries only
- Fixed component sizes
- Responsive parent only
- No container fallback

**References**
- [Chrome: Container Queries](https://developer.chrome.com/docs/css-container-queries/)
- [CSS-Tricks: Container Queries](https://css-tricks.com/container-queries/)

---
## Content Analysis
**Category:** ux | **Type:** methodology | **Tags:** research

A systematic method for analyzing textual, visual, or audio content by categorizing and coding data into themes. Content analysis transforms qualitative information into quantifiable insights through structured examination.

**Examples**
- Coding customer support tickets to identify the most common complaint categories
- Analyzing social media posts to understand sentiment and recurring topics

**Do's and Don'ts**

*Do's*
- Define clear coding categories before starting
- Ensure categories are mutually exclusive
- Code consistently across all content
- Calculate inter-rater reliability with multiple coders
- Document your coding scheme
- Use software tools for large datasets

*Don'ts*
- Use overlapping or ambiguous categories
- Let a single coder handle all analysis
- Change coding scheme midway without re-coding
- Ignore context when coding content
- Skip validation of coding reliability
- Overcomplicate the coding scheme

**References**
- [Scribbr: Content Analysis Guide](https://www.scribbr.com/methodology/content-analysis/)
- [University of Minnesota: Content Analysis](https://www.extension.umn.edu/evaluation/tools-for-evaluation/content-analysis/)

---
## Content Facet
**Category:** ux | **Type:** pattern | **Tags:** information-architecture

Attribute used to filter content collections.

**Examples**
- Product: Color, Size, Material
- Article: Author, Date, Tag
- Jobs: Location, Role, Experience
- Events: Type, Date, Location

**Do's and Don'ts**

*Do's*
- 3-7 facets maximum
- Clear business value
- Multiple selection
- Descriptive labels

*Don'ts*
- Irrelevant attributes
- More than 10 facets
- Single select only
- Internal metadata

**References**
- [Filter Design Patterns](https://www.filterdesignpatterns.com/)
- [Baymard Institute](https://baymard.com/)

---
## Content Inventory
**Category:** ux | **Type:** tool | **Tags:** information-architecture, research

Comprehensive list of existing content items and attributes.

**Examples**
- 247 product pages with status
- 89 blog posts with authors
- 42 documentation files
- 156 landing pages inventoried

**Do's and Don'ts**

*Do's*
- Include ownership info
- Track update frequency
- Note content quality
- Export to spreadsheet

*Don'ts*
- List pages only
- Skip file types
- No metadata collection
- Manual counting only

**References**
- [Content Inventory](https://www.contentinventory.io/)
- [Doing Content Audit](https://doingcontentaudit.com/)

---
## Content Model
**Category:** strategy | **Type:** concept | **Tags:** information-architecture

Structured definition of content types and their properties.

**Examples**
- Article: title, author, date, tags, body
- Product: name, price, images, specs, reviews
- Event: title, date, location, capacity
- Job: title, company, location, description

**Do's and Don'ts**

*Do's*
- Define required fields
- Plan relationships
- Content model diagrams
- Validate with real data

*Don'ts*
- Page-based thinking
- Missing key properties
- No relationships planned
- Developer spec only

**References**
- [Content Modeling](https://contentmodeling.org/)
- [Mortensoft](https://mortensoft.com/)

---
## Content Style Guide
**Category:** strategy | **Type:** tool | **Tags:** documentation, typography

Standards for tone, voice, and writing conventions.

**Examples**
- Voice attributes (friendly, direct)
- Grammar preferences
- Date/number formatting
- Error messaging patterns

**Do's and Don'ts**

*Do's*
- Include localization rules
- Cover all content types
- Test readability scores
- Update with user feedback

*Don'ts*
- Copy-paste from legal
- Desktop reading only
- Missing voice examples
- No localization rules

**References**
- [Write the Docs](https://www.writethedocs.org/)
- [Content Style Guide](https://contentstyleguide.com/)

---
## Contextual Inquiry
**Category:** ux | **Type:** methodology | **Tags:** research

A qualitative research method combining observation and interview in the user's actual work environment. Researchers observe users performing tasks in their natural context while asking questions to understand their motivations, challenges, and workflows.

**Examples**
- Observing nurses in a hospital while they use medical record software during their shift
- Watching office workers manage email and calendar tasks in their actual workspace

**Do's and Don'ts**

*Do's*
- Conduct sessions in the user's actual environment, not a lab
- Let the user lead and perform their normal tasks
- Ask questions in the moment to understand context
- Take detailed notes about environment and workflow
- Focus on understanding the "why" behind actions

*Don'ts*
- Interrupt users during critical tasks
- Take users out of their natural environment
- Rely solely on what users say without observing behavior
- Make assumptions about their workflow
- Rush through the session

**References**
- [Nielsen Norman Group: Contextual Inquiry](https://www.nngroup.com/articles/contextual-inquiry/)
- [Interaction Design Foundation: Contextual Inquiry](https://www.interaction-design.org/literature/topics/contextual-inquiry)

---
## Continuous Design Process
**Category:** strategy | **Type:** methodology | **Tags:** processes

Iterative shipping feedback cycles.

**Examples**
- Weekly MVP experiments
- Build-measure-learn loops
- Continuous deployment
- Real user feedback

**Do's and Don'ts**

*Do's*
- Small frequent releases
- Automated deployment
- User feedback integration
- Experimentation culture

*Don'ts*
- Big bang releases
- Manual deployment
- Survey feedback only
- Monthly cycles

**References**
- [Continuous Design](https://continuousdesign.com/)
- [Lean Startup](https://leanstartup.com/)

---
## Continuous Discovery
**Category:** ux | **Type:** methodology | **Tags:** research

An ongoing research practice where product teams regularly interact with customers to inform decisions and validate assumptions throughout development. Continuous discovery embeds research into weekly routines rather than treating it as separate project phases.

**Examples**
- Conducting weekly user interviews with existing customers to understand evolving needs
- Regularly observing customer support sessions to identify recurring problems

**Do's and Don'ts**

*Do's*
- Make research a weekly habit, not a phase
- Involve the entire product team in research
- Focus on learning over comprehensive studies
- Keep research lightweight and actionable
- Create systems for sharing insights
- Connect research directly to decisions

*Don'ts*
- Wait for big research projects
- Let only researchers talk to customers
- Collect insights without acting on them
- Make continuous discovery too formal or heavy
- Stop research once product ships
- Ignore what you're learning from support and analytics

**References**
- [Teresa Torres: Continuous Discovery Habits](https://www.producttalk.org/2021/05/continuous-discovery-habits/)
- [The Fountain Institute: Continuous Discovery](https://www.thefountaininstitute.com/blog/ux-research-methods-product-discovery)

---
## Contrast Principle
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy, accessibility

Color size differences create emphasis separation.

**Examples**
- 4.5:1 text contrast minimum
- Primary vs secondary buttons
- Hero text vs background
- Focus states high contrast

**Do's and Don'ts**

*Do's*
- WCAG contrast compliance
- Size + color emphasis
- Background/foreground balance
- Test in all lighting

*Don'ts*
- Low contrast text
- Similar button colors
- Pastel on pastel
- Insufficient focus contrast

**References**
- [WebAIM: Contrast](https://www.webaim.org/articles/contrast/)
- [Contrast Checker](https://contrastchecker.com/)

---
## Contribution Docs
**Category:** strategy | **Type:** tool | **Tags:** documentation, processes

Guidelines for teams extending or customizing the system.

**Examples**
- Component contribution workflow
- Token naming conventions
- Documentation requirements
- PR review checklist

**Do's and Don'ts**

*Do's*
- Templates and examples
- Automated validation
- Clear acceptance criteria
- Credit contributors

*Don'ts*
- Vague contribution policy
- No templates provided
- Gatekeep contributions
- Ignore small improvements

**References**
- [Design Systems: Contribute](https://www.designsystems.com/contribute/)
- [All Contributors](https://allcontrib.org/)

---
## Contribution Review Process
**Category:** management | **Type:** methodology | **Tags:** processes

Peer review merge standards.

**Examples**
- Design system PR template
- Automated linting tests
- 2 approver minimum
- Changelog automation

**Do's and Don'ts**

*Do's*
- Clear acceptance criteria
- Automated checks first
- Cross-team review
- Comprehensive testing

*Don'ts*
- Direct main merge
- Single reviewer
- No automated checks
- Verbal approval

**References**
- [Storybook: Publish Workflows](https://storybook.js.org/docs/workflows/publish/)
- [GitHub](https://www.github.com/)

---
## Conversion Rate
**Category:** strategy | **Type:** tool | **Tags:** analytics

Percentage users completing desired action (purchase signup).

**Examples**
- 3.2% checkout completion
- 12.4% newsletter signup
- 8.7% free trial start
- 1.8% upgrade conversion

**Do's and Don'ts**

*Do's*
- Segment by traffic source
- A/B test improvements
- Track funnel drop-offs
- Set realistic benchmarks

*Don'ts*
- Vanity metrics focus
- No segmentation
- Single aggregate number
- Ignore funnel analysis

**References**
- [Mixpanel: Conversion Rate](https://mixpanel.com/blog/conversion-rate/)

---
## Core Web Vitals
**Category:** ui | **Type:** methodology | **Tags:** web, analytics

Google metrics measuring loading interactivity visual stability.

**Examples**
- LCP < 2.5s, FID < 100ms, CLS < 0.1
- INP < 200ms (FID replacement)
- 75% URL compliance target
- Monthly vitals monitoring

**Do's and Don'ts**

*Do's*
- Prioritize LCP optimization
- Real user monitoring
- Field data tracking
- Actionable thresholds

*Don'ts*
- Focus vanity metrics
- Lab data only
- Ignore CLS completely
- No improvement roadmap

**References**
- [Web.dev: Vitals](https://web.dev/vitals/)
- [DebugBear](https://www.debugbear.com/)

---
## Cost of Delay
**Category:** strategy | **Type:** framework | **Tags:** strategy

A prioritization approach that quantifies the economic impact of time by calculating the value lost when a decision or initiative is delayed. Cost of Delay helps teams make urgent vs important trade-offs based on financial impact.

**Examples**
- Calculating that delaying a checkout fix costs $10,000 per week in lost revenue, making it higher priority
- Comparing cost of delay across features to decide release order

**Do's and Don'ts**

*Do's*
- Estimate economic value in real terms (revenue, cost savings)
- Consider both direct and indirect costs
- Use relative rather than precise calculations
- Combine with effort estimates for CD3 (Cost of Delay Divided by Duration)
- Update estimates as market conditions change
- Use to challenge assumptions about urgency

*Don'ts*
- Get stuck on perfect precision in estimates
- Ignore intangible or long-term value
- Use Cost of Delay as the only prioritization factor
- Forget opportunity costs of not doing other work
- Assume all delays have linear cost curves
- Skip the validation of cost assumptions

**References**
- [Black Swan Farming: Cost of Delay](https://blackswanfarming.com/cost-of-delay/)
- [ProductPlan: Cost of Delay](https://www.productplan.com/glossary/cost-of-delay/)

---
## Crazy 8s Timed Sketch
**Category:** ux | **Type:** tool | **Tags:** ideation

Fold paper into 8 sections sketch one idea per minute.

**Examples**
- 8 homepage variations
- 8 checkout flows
- 8 onboarding screens
- 8-minute total exercise

**Do's and Don'ts**

*Do's*
- Strict one minute
- Rough sketches ok
- Different each panel
- Share and discuss

*Don'ts*
- Detailed drawings
- Repeat same idea
- Skip panels
- No time pressure

**References**
- [Google Design Sprint](https://designsprintkit.withgoogle.com/)
- [AJ&Smart](https://ajsmart.com/)

---
## Critical CSS Extraction
**Category:** ui | **Type:** methodology | **Tags:** web, analytics

Extract above-fold styles for immediate rendering.

**Examples**
- 14KB render-blocking CSS
- Critical path inline styles
- Async non-critical CSS
- Automated critical extraction

**Do's and Don'ts**

*Do's*
- Automate extraction process
- Monitor bundle size
- Test render performance
- Mobile-first critical

*Don'ts*
- Inline ALL CSS
- Manual extraction
- Forget non-critical async
- Desktop-optimized critical

**References**
- [web.dev: Extract Critical CSS](https://web.dev/articles/extract-critical-css)

---
## Cross-Browser Testing
**Category:** ui | **Type:** tool | **Tags:** testing, web

Functionality consistency across Chrome Firefox Safari Edge.

**Examples**
- Chrome 120 Firefox 121
- Safari 17 Edge 120
- CSS Grid rendering parity
- JavaScript feature support

**Do's and Don'ts**

*Do's*
- Automate with BrowserStack
- Test top 90% browsers
- Document browser bugs
- Visual regression testing

*Don'ts*
- Manual testing only
- Support <1% browsers
- Ignore rendering diffs
- No automation

**References**
- [BrowserStack](https://www.browserstack.com/)
- [Sauce Labs](https://saucelabs.com/)

---
## Cross-chart Filter
**Category:** ui | **Type:** pattern | **Tags:** data-visualization, interaction

Clicking one chart filters all connected charts simultaneously.

**Examples**
- Click region filters all metrics
- Date selection across charts
- Category click coordination
- KPI threshold filtering

**Do's and Don'ts**

*Do's*
- Visual filter state indicator
- Undo/Reset capability
- Loading states during filter
- Bookmarkable URLs

*Don'ts*
- Filter applies instantly
- No visual feedback
- Complex filter logic
- No exclusion option

**References**
- [Tableau Dashboards](https://www.tableau.com/products/dashboards)
- [Power BI](https://powerbi.microsoft.com/)

---
## Cross-Device Testing
**Category:** ui | **Type:** tool | **Tags:** testing, mobile

iPhone Android tablet desktop behavior consistency.

**Examples**
- iPhone 15 iPad Pro Samsung S24
- Portrait landscape testing
- Touch vs mouse behavior
- Device-specific gestures

**Do's and Don'ts**

*Do's*
- Real devices preferred
- All screen orientations
- Touch target validation
- Platform gesture support

*Don'ts*
- Emulators only
- Desktop testing only
- Single device class
- Ignore orientation

**References**
- [LambdaTest](https://www.lambdatest.com/)
- [BrowserStack Devices](https://www.browserstack.com/devices)

---
## Cross-Functional Workshop
**Category:** management | **Type:** methodology | **Tags:** processes

Mixed-discipline collaborative sessions.

**Examples**
- Product Design Eng workshop
- Jobs-to-be-done mapping
- Opportunity solution tree
- 4hr facilitated session

**Do's and Don'ts**

*Do's*
- Diverse representation
- Clear agenda outcomes
- Pre-work required
- Documented outputs

*Don'ts*
- Homogeneous group
- Open-ended discussion
- No pre-work
- Verbal outcomes only

**References**
- [Miro: Workshop](https://www.miro.com/workshop/)
- [Mural](https://mural.co/)

---
## CSS Clamp Function
**Category:** ui | **Type:** tool | **Tags:** web, typography

Dynamic value between min max based on viewport.

**Examples**
- font-size: clamp(1rem, 4vw, 2rem)
- Responsive spacing clamp
- Fluid typography scale
- Container-aware sizing

**Do's and Don'ts**

*Do's*
- Mobile-first min values
- Readable max limits
- Test extreme viewports
- Combine with container queries

*Don'ts*
- Fixed clamp values
- Over-narrow viewport test
- Clamp everything
- No fallbacks

**References**
- [MDN: clamp()](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp())
- [CSS-Tricks](https://css-tricks.com/)

---
## CSS Custom Properties
**Category:** ui | **Type:** tool | **Tags:** web, design-systems

Dynamic CSS variables for theming consistency.

**Examples**
- --color-primary: #007acc
- --spacing-md: 1.5rem
- --radius-lg: 12px
- CSS custom property sets

**Do's and Don'ts**

*Do's*
- Semantic naming convention
- Fallback values
- Theme switching
- Design token mapping

*Don'ts*
- Hardcoded values
- Magic numbers
- !important overrides
- No fallback values

**References**
- [MDN: CSS Custom Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_custom_properties)
- [CSS-Tricks: Variables](https://css-tricks.com/variables/)

---
## CSS Feature Queries
**Category:** ui | **Type:** tool | **Tags:** web

Conditional CSS based on browser feature support.

**Examples**
- @supports (grid-gap: 1rem) { .grid { display: grid; } }
- @supports (container-type: inline-size) { .cq { container-type: inline-size; } }
- @supports (aspect-ratio: 1) fallback
- Subgrid feature detection

**Do's and Don'ts**

*Do's*
- Progressive enhancement
- Graceful fallbacks
- Test support thresholds
- Document feature tiers

*Don'ts*
- Assume universal support
- No fallback styles
- Browser sniffing instead
- Disable modern features

**References**
- [MDN: @supports](https://developer.mozilla.org/en-US/docs/Web/CSS/@supports)
- [CSS-Tricks: CSS Feature Queries](https://css-tricks.com/css-feature-queries/)

---
## CSS Scroll Snap
**Category:** ui | **Type:** tool | **Tags:** web, interaction

Snaps scroll container to specific points.

**Examples**
- Fullscreen sections snap
- Horizontal card carousel
- Mobile snap points
- Touch-friendly snapping

**Do's and Don'ts**

*Do's*
- scroll-snap-align
- Smooth snap behavior
- Keyboard accessibility
- Fallback smooth scroll

*Don'ts*
- Jerky snapping
- No momentum scrolling
- Desktop-only snap
- Tiny snap targets

**References**
- [MDN: CSS Scroll Snap](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap)
- [CSS-Tricks](https://css-tricks.com/)

---
## CSS Subgrid
**Category:** ui | **Type:** tool | **Tags:** web

Child grid inherits parent grid tracks.

**Examples**
- Nested grid perfect alignment
- Component grid system
- Form field perfect alignment
- Complex layout harmony

**Do's and Don'ts**

*Do's*
- Explicit subgrid declaration
- Fallback standard grid
- Browser support testing
- Documentation required

*Don'ts*
- Manual track mirroring
- Ignore browser support
- Complex nested grids
- No fallback planning

**References**
- [MDN: Subgrid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Subgrid)
- [CSS-Tricks](https://css-tricks.com/)

---
## Customer Lifetime Value (LTV)
**Category:** strategy | **Type:** tool | **Tags:** analytics

Predicted net profit from entire customer relationship.

**Examples**
- $247 avg LTV
- LTV:CAC ratio 3.2:1
- Cohort LTV curves
- Segment by acquisition

**Do's and Don'ts**

*Do's*
- Include all revenue streams
- Discount future revenue
- Track LTV:CAC ratio
- Update predictions

*Don'ts*
- Static LTV calculation
- First month revenue only
- No discounting
- Average all customers

**References**
- [For Entrepreneurs: LTV](https://www.forentrepreneurs.com/ltv/)
- [Baremetrics](https://baremetrics.com/)

---
## DACI Decision Roles
**Category:** strategy | **Type:** framework | **Tags:** strategy, processes

Driver Approver Contributor Informed responsibilities.

**Examples**
- Product manager = Driver
- VP Product = Approver
- Design Eng = Contributors
- Marketing = Informed

**Do's and Don'ts**

*Do's*
- Clear single Driver
- Approver has authority
- Contributors have voice
- Document decisions

*Don'ts*
- Multiple Drivers
- No clear Approver
- Silent Contributors
- All Informed

**References**
- [Atlassian: DACI](https://www.atlassian.com/team-playbook/plays/daci/)

---
## Daily Active Users (DAU)
**Category:** ux | **Type:** tool | **Tags:** analytics

Unique users using product per calendar day.

**Examples**
- DAU 24.7k MAU 187k
- DAU/MAU stickiness 13.2%
- DAU growth 8% MoM
- Segment DAU by feature

**Do's and Don'ts**

*Do's*
- Track DAU/MAU ratio
- Segment by user type
- Monitor day-of-week
- Set growth targets

*Don'ts*
- Report raw DAU only
- No stickiness ratio
- Daily fluctuations ignored
- All-time unique

**References**
- [Amplitude: DAU](https://amplitude.com/blog/dau/)

---
## Daily Design Standup
**Category:** management | **Type:** methodology | **Tags:** processes

15min team synchronization ritual.

**Examples**
- Yesterday: Card progress
- Today: 3 priority tasks
- Blockers: Immediate help needed
- 2min per person max

**Do's and Don'ts**

*Do's*
- Physical digital board
- Single conversation
- Timekeeper designated
- Blockers escalated

*Don'ts*
- Status reporting only
- Problem solving meeting
- >20min duration
- No time limit

**References**
- [Atlassian: Standups](https://www.atlassian.com/agile/standups)
- [Basecamp](https://basecamp.com/)

---
## Dark Mode Color Mapping
**Category:** ui | **Type:** methodology | **Tags:** color, design-systems

A methodology for systematically adapting a light mode color palette to dark mode. Mapping defines how each color transforms: backgrounds invert from light to dark, text flips from dark to light, and accent colors adjust saturation and lightness to maintain visibility and reduce eye strain.

**Examples**
- Mapping white backgrounds to gray-900 and gray-100 surfaces to gray-800
- Reducing saturation of bright accent colors to prevent eye strain on dark backgrounds
- Inverting the color scale so text-primary (gray-900) maps to gray-100 in dark mode
- Adjusting elevation: using lighter surfaces instead of shadows to show depth

**Do's and Don'ts**

*Do's*
- Use semantic color tokens to enable automatic theme switching
- Reduce saturation of vibrant colors for dark mode (less visual strain)
- Maintain consistent contrast ratios across both modes
- Use surface elevation (lighter grays) instead of shadows for depth
- Test both modes side by side for visual consistency

*Don'ts*
- Simply invert all colors (produces poor results)
- Use pure black (#000000) as the darkest background (too harsh)
- Keep the same saturation levels for accent colors (often too vibrant)
- Forget to adjust illustrations and images for dark mode
- Assume light mode contrast ratios automatically work in dark mode

**References**
- [Material Design: Dark Theme](https://m3.material.io/styles/color/dark-theme)
- [Apple Human Interface Guidelines: Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)

---
## Dark Mode Guide
**Category:** ui | **Type:** tool | **Tags:** documentation, color

Specifications for implementing theme variations.

**Examples**
- Elevation shadow adjustments
- Color mapping rules
- Reduced motion settings
- High contrast variants

**Do's and Don'ts**

*Do's*
- Test all components
- Adjust elevations
- Provide luminance delta
- Include user preference

*Don'ts*
- Literal color inversion
- Same shadows as light
- Missing contrast testing
- No user preference

**References**
- [Material Design 3: Dark Theme](https://m3.material.io/styles/color/dark-theme/overview)
- [Dark Mode Design](https://darkmode.design/)

---
## Data Heat Grid
**Category:** ui | **Type:** tool | **Tags:** data-visualization

Color intensity matrix shows value density across two categorical axes.

**Examples**
- Website heat grid by hour/day
- Sales performance matrix
- Correlation heatmap
- Occupancy grid by room/time

**Do's and Don'ts**

*Do's*
- Sequential color scale
- Clear axis labels
- Size-proportional cells
- Zero baseline reference

*Don'ts*
- Rainbow color schemes
- Missing scale legend
- Square cells only
- Too many categories

**References**
- [Heatmapper](https://www.heatmapper.ca/)
- [D3 Graph Gallery: Heatmap](https://d3-graph-gallery.com/heatmap.html)

---
## Data Point Drilldown
**Category:** ui | **Type:** pattern | **Tags:** data-visualization, interaction, navigation

Clicking aggregate data reveals component-level detail.

**Examples**
- Country → City → Store drill
- Month → Week → Day breakdown
- Category → Subcategory detail
- KPI → Component analysis

**Do's and Don'ts**

*Do's*
- Clear back/up navigation
- Consistent detail patterns
- Loading state feedback
- Bookmarkable drill paths

*Don'ts*
- Infinite drill levels
- No summary context
- Different detail formats
- Slow loading details

**References**
- [Looker: Drill-downs](https://www.looker.com/product/drill-downs)
- [Metabase](https://metabase.com/)

---
## Data Visualization Color Scales
**Category:** ui | **Type:** methodology | **Tags:** color, data-visualization

A methodology for selecting appropriate color scales based on data type. Sequential scales (light to dark) show ordered data, diverging scales (two hues from a neutral center) show deviation from a midpoint, and categorical scales (distinct hues) differentiate unrelated categories.

**Examples**
- Using a sequential blue scale (light to dark) to show temperature from low to high
- Applying a diverging red-white-green scale to show profit/loss deviation from zero
- Choosing 5-7 distinct categorical colors for different product lines in a pie chart
- Using a single-hue sequential scale for population density maps

**Do's and Don'ts**

*Do's*
- Match scale type to data type (sequential for ordered, categorical for nominal)
- Limit categorical palettes to 5-7 distinguishable colors
- Use perceptually uniform scales for accurate data representation
- Test scales under color blindness simulation
- Ensure sufficient contrast between adjacent values in sequential scales

*Don'ts*
- Use rainbow scales for sequential data (not perceptually uniform)
- Apply categorical colors to ordered data
- Use too many categories (hard to distinguish beyond 7 colors)
- Forget that red/green distinctions fail for colorblind users
- Assume diverging scales need symmetric data ranges

**References**
- [ColorBrewer: Color Advice for Maps](https://colorbrewer2.org/)
- [D3 Color Scales](https://d3js.org/d3-scale-chromatic)

---
## Dead Click Analysis
**Category:** ux | **Type:** tool | **Tags:** analytics

Clicks non-functional decorative elements.

**Examples**
- 14% clicks on images
- 8% logo dead clicks
- Mobile dead zone clicks
- Visual design cleanup

**Do's and Don'ts**

*Do's*
- Prioritize high-traffic dead
- A/B test removal impact
- Mobile vs desktop split
- Revenue correlation

*Don'ts*
- All clicks equal
- Low-traffic cleanup
- No A/B testing
- Ignore revenue impact

**References**
- [UXCam: Dead Clicks](https://uxcam.com/blog/dead-clicks/)

---
## Decorative Chart Elements
**Category:** ui | **Type:** principle | **Tags:** data-visualization

Non-data ink elements distract from data message and reduce clarity.

**Examples**
- Background gradients
- Animated sparkles
- Picture icons instead of bars
- Heavy drop shadows

**Do's and Don'ts**

*Do's*
- Replace with data ink
- Test chart without element
- Consider cognitive load
- Maintain data integrity

*Don'ts*
- Patriotic color schemes
- Branded backgrounds
- Celebratory confetti
- Motion without purpose

**References**
- [Storytelling with Data: Chart Junk](https://www.storytellingwithdata.com/blog/2019/2/12/chart-junk)
- [Junk Charts](https://junkcharts.typepad.com/)

---
## Deep Linking Scheme
**Category:** ui | **Type:** tool | **Tags:** mobile, navigation

URL schemes opening specific app screens.

**Examples**
- myapp://profile/123
- universal links iOS
- App Links Android
- Deferred deep linking

**Do's and Don'ts**

*Do's*
- Clear URL structure
- Fallback web experience
- Test all link types
- Analytics tracking

*Don'ts*
- Obfuscated URL schemes
- No web fallback
- Broken universal links
- Desktop-only linking

**References**
- [Apple: Universal Links](https://developer.apple.com/documentation/xcode/supporting-universal-links)
- [Android Developer](https://developer.android.com/)

---
## Default State
**Category:** ui | **Type:** pattern | **Tags:** interaction

Normal resting appearance of interactive element before any user interaction.

**Examples**
- Standard button appearance
- Unhovered menu item
- Unfocused input field
- Normal toggle position

**Do's and Don'ts**

*Do's*
- Establish clear default states
- Use as hierarchy baseline
- Maintain consistency across components
- Test default state recognition

*Don'ts*
- Use distracting defaults
- Make defaults look inactive
- Inconsistent default styling
- Skip default state documentation

**References**
- [Material Design: States & Interactions](https://m3.material.io/foundations/interaction/states)
- [Figma: Component States](https://www.figma.com/best-practices/component-architecture/)

---
## Definition of Done
**Category:** management | **Type:** concept | **Tags:** processes

Shared quality criteria story completion.

**Examples**
- Code reviewed merged
- Tests passing 80% coverage
- Cross-browser tested
- Docs updated

**Do's and Don'ts**

*Do's*
- Team-agreed criteria
- Visible to all
- Regularly revisited
- Measurable verifiable

*Don'ts*
- Vague completion
- Moving target
- Team-specific DoD
- Never documented

**References**
- [Scrum.org: Definition of Done](https://www.scrum.org/resources/blog/definition-done)
- [Agile Alliance](https://www.agilealliance.org/)

---
## Design Brief Template
**Category:** strategy | **Type:** tool | **Tags:** strategy, processes

Project scope objectives constraints success criteria.

**Examples**
- Objective: Improve checkout 20%
- Success: CR lift + time -30%
- Constraints: No new pages
- Timeline: 6 weeks

**Do's and Don'ts**

*Do's*
- Specific measurable success
- Clear constraints scope
- Stakeholder signoff
- Kickoff reference doc

*Don'ts*
- Vague inspirational brief
- Unlimited scope
- No success criteria
- Never referenced

**References**
- [Figma: Design Brief Template](https://www.figma.com/blog/design-brief-template/)
- [Smashing Magazine](https://www.smashingmagazine.com/)

---
## Design Career Ladder
**Category:** management | **Type:** framework | **Tags:** processes

Progression framework skill levels responsibilities.

**Examples**
- Junior → Mid → Senior → Lead
- Level-specific expectations
- Promotion rubric
- Quarterly career conversations

**Do's and Don'ts**

*Do's*
- Clear skill progression
- Multiple career paths
- Regular reviews
- Mentorship mapping

*Don'ts*
- Vague promotion criteria
- Single linear path
- Annual reviews only
- No skill framework

**References**
- [Intercom: Design Career Ladders](https://www.intercom.com/blog/design-career-ladders/)
- [Career Frameworks](https://careerframeworks.org/)

---
## Design Consistency Score
**Category:** ui | **Type:** tool | **Tags:** analytics, design-systems

Uniformity measurement across product surfaces.

**Examples**
- Button consistency 94%
- Color usage variance 3%
- Typography drift 2.1%
- Cross-platform score

**Do's and Don'ts**

*Do's*
- Multiple consistency axes
- Weighted component impact
- Historical benchmarking
- Automated detection

*Don'ts*
- Single visual metric
- All components equal
- No weighting
- Manual sampling

**References**
- [Zeroheight: Design System Metrics](https://zeroheight.com/blog/design-system-metrics/)

---
## Design Critique Session
**Category:** management | **Type:** methodology | **Tags:** processes

Structured peer feedback on in-progress design work.

**Examples**
- 30min focused critique
- 2min designer context
- 20min peer feedback
- 8min synthesis action items

**Do's and Don'ts**

*Do's*
- Specific ask from designer
- 'I like start stop continue'
- Timeboxed feedback
- Documented action items

*Don'ts*
- General feedback
- Solution giving
- Unlimited discussion
- No follow-through

**References**
- [Figma: Design Critique](https://www.figma.com/blog/design-critique/)
- [Medium](https://medium.com/)

---
## Design Debt Score
**Category:** ui | **Type:** methodology | **Tags:** design-systems, analytics

Quantitative measure of divergence from design system standards, calculated from component usage, token adherence, and consistency violations.

**Examples**
- 15% custom components detected
- 22 token override violations
- 8% accessibility deviations
- Overall debt score: 18/100

**Do's and Don'ts**

*Do's*
- Define clear scoring criteria
- Track trends over time
- Prioritize high-impact debt
- Share scores transparently

*Don'ts*
- Hide debt from stakeholders
- Ignore incremental accumulation
- Focus only on visual debt
- Skip developer input

**References**
- [Frontend Mentor: Design Debt](https://www.frontendment.dev/design-debt/)
- [Design Systems News](https://designsystems.news/)

---
## Design Decision Log
**Category:** strategy | **Type:** tool | **Tags:** documentation, processes

Records explaining rationale behind key design choices.

**Examples**
- Why we chose this grid system
- Navigation pattern evolution
- Color palette selection process
- Component naming conventions

**Do's and Don'ts**

*Do's*
- Link to research data
- Include alternatives considered
- Tag by component/area
- Make searchable

*Don'ts*
- Blame assignments
- Technical details only
- Missing tradeoffs
- Buried in chat threads

**References**
- [Architecture Decision Records](https://adr.github.io/)
- [Design Systems News](https://www.designsystems.news/)

---
## Design Documentation
**Category:** ui | **Type:** tool | **Tags:** documentation, design-systems

Artifacts recording design processes, decisions, and deliverables for team alignment and consistency.

**Examples**
- Figma file with component variants and states
- PDF spec sheet with responsive breakpoints
- Notion page linking research to final designs
- Video walkthrough of prototype flows

**Do's and Don'ts**

*Do's*
- Keep living and versioned
- Link decisions to research
- Include rationale for choices
- Make accessible to all stakeholders

*Don'ts*
- Create one-off documents
- Skip usage examples
- Let docs become outdated
- Hide from developers

**References**
- [Figma: Design Documentation](https://www.figma.com/best-practices/design-documentation/)
- [UX Design](https://uxdesign.cc/)

---
## Design Governance
**Category:** management | **Type:** framework | **Tags:** processes

The framework of processes, policies, and decision-making structures that guide design work and ensure consistency across an organization. Design governance defines who makes decisions, how standards are maintained, and how design quality is upheld.

**Examples**
- Establishing an approval process for new design system components
- Creating guidelines for when designers can deviate from established patterns

**Do's and Don'ts**

*Do's*
- Define clear decision-making authority
- Document processes and standards
- Balance consistency with flexibility
- Create escalation paths for conflicts
- Review and update governance regularly
- Make governance proportional to organization size

*Don'ts*
- Create governance that blocks all progress
- Make processes too complex or bureaucratic
- Have governance without clear ownership
- Ignore governance when convenient
- Copy governance from other companies without adapting
- Implement governance without team buy-in

**References**
- [InVision: Design Governance Guide](https://www.invisionapp.com/inside-design/design-governance/)
- [Nielsen Norman Group: Design Systems Governance](https://www.nngroup.com/articles/design-systems-governance/)

---
## Design Guild Meetings
**Category:** management | **Type:** methodology | **Tags:** processes

Cross-team community of practice sharing.

**Examples**
- Component library updates
- Design system metrics
- Cross-team critique
- Tooling workflow sharing

**Do's and Don'ts**

*Do's*
- Rotate facilitators
- Actionable takeaways
- Guest speakers
- Published notes

*Don'ts*
- Design-only attendees
- Status updates only
- No cross-pollination
- Secret discussions

**References**
- [InVision: Design Guild](https://www.invisionapp.com/inside-design/design-guild/)
- [Design Systems](https://designsystems.com/)

---
## Design Handoff
**Category:** ui | **Type:** tool | **Tags:** documentation, design-systems, processes

Package transferring designs to developers with specs, assets, and code snippets.

**Examples**
- Zeplin project with measurements
- Figma Dev Mode specs
- Abstract API with states
- CodeSandbox examples

**Do's and Don'ts**

*Do's*
- Include all states
- Provide code examples
- Specify responsive behavior
- Test developer questions

*Don'ts*
- Hand off incomplete designs
- No code examples
- Missing assets
- Ignore developer tools

**References**
- [Zeplin Dev Mode](https://zeplin.io/features/dev-mode)
- [Figma Dev Mode](https://www.figma.com/dev-mode/)

---
## Design Office Hours
**Category:** management | **Type:** methodology | **Tags:** processes

Scheduled help troubleshooting availability.

**Examples**
- Tue 2-3pm Figma help
- Thu 10-11am critique
- Drop-in troubleshooting
- Rotating experts

**Do's and Don'ts**

*Do's*
- Clear expertise advertised
- Timeboxed sessions
- Ticket system optional
- Published recordings

*Don'ts*
- Unscheduled drop-ins
- Unlimited time
- Single expert always
- No preparation

**References**
- [Figma: Office Hours](https://www.figma.com/blog/office-hours/)
- [Notion](https://www.notion.so/)

---
## Design Operations
**Category:** management | **Type:** concept | **Tags:** processes

The orchestration of people, processes, and tools to enable design teams to create value more effectively. Also called DesignOps, it focuses on operational efficiency, workflow optimization, and removing blockers for designers.

**Examples**
- Establishing design file organization standards and naming conventions across teams
- Managing design tool licenses, training, and onboarding processes

**Do's and Don'ts**

*Do's*
- Focus on enabling designers, not controlling them
- Measure and improve workflow efficiency
- Standardize where it creates value
- Build scalable processes as team grows
- Collaborate across product, engineering, and research ops
- Listen to designer pain points

*Don'ts*
- Add process without clear value
- Solve problems designers don't have
- Optimize for ops convenience over designer needs
- Implement rigid, inflexible systems
- Work in isolation from design team
- Forget that DesignOps serves design outcomes

**References**
- [Nielsen Norman Group: DesignOps 101](https://www.nngroup.com/articles/design-operations-101/)
- [InVision: DesignOps Handbook](https://www.invisionapp.com/inside-design/designops-handbook/)

---
## Design Principles Definition
**Category:** strategy | **Type:** methodology | **Tags:** principles

Establishing clear, actionable guidelines that express the values and priorities guiding design decisions for a product or team. Design principles help teams make consistent choices and resolve conflicts during the design process.

**Examples**
- Creating principles like "Clarity over cleverness" to guide interface design decisions
- Defining "Empower experts, welcome beginners" to balance feature complexity

**Do's and Don'ts**

*Do's*
- Base principles on research insights and strategy
- Make principles specific and actionable
- Create 3-7 principles maximum
- Include examples of principles in action
- Use principles to resolve design debates
- Review and evolve principles periodically

*Don'ts*
- Use generic principles that could apply to any product
- Create too many principles
- Make principles vague or abstract
- Define principles in isolation from user needs
- Set and forget principles without using them
- Let principles become rigid rules

**References**
- [Nielsen Norman Group: Design Principles](https://www.nngroup.com/articles/design-principles/)
- [Jeremy Keith: Design Principles](https://principles.adactio.com/)

---
## Design Specification
**Category:** ui | **Type:** tool | **Tags:** documentation, design-systems

Detailed blueprint covering layouts, interactions, and responsive behaviors.

**Examples**
- Homepage layout with 3 breakpoints
- Checkout flow with state transitions
- Search results page specifications
- Mobile navigation drawer behavior

**Do's and Don'ts**

*Do's*
- Include measurements
- Specify all interactions
- Cover all breakpoints
- Link to assets

*Don'ts*
- Screenshots only
- Missing mobile specs
- Vague interaction notes
- No measurements

**References**
- [InVision: Design Specs](https://www.invisionapp.com/inside-design/spec-ct/)

---
## Design Sprint Process
**Category:** strategy | **Type:** methodology | **Tags:** processes

5-day collaborative problem solving prototype testing.

**Examples**
- Mon: Understand map decide
- Tue: Sketch individual solutions
- Wed: Decide prototype
- Thu: Prototype 8hr fake it
- Fri: Test 5 users

**Do's and Don'ts**

*Do's*
- Cross-functional team
- Real user interviews
- High-fidelity prototype
- Single concrete problem

*Don'ts*
- Designers only team
- Low-fidelity sketches
- Fake user interviews
- Multiple problems

**References**
- [GV: Sprint](https://www.gv.com/sprintzero/)
- [Designlab](https://www.designlab.com/)

---
## Design System
**Category:** ui | **Type:** framework | **Tags:** design-systems, documentation

A centralized repository of reusable components, patterns, and guidelines that ensures visual and functional consistency across products and teams.

**Examples**
- Material Design by Google
- Carbon Design System by IBM
- Atlassian's Design System
- Shopify Polaris

**Do's and Don'ts**

*Do's*
- Establish clear governance and ownership
- Document usage guidelines comprehensively
- Include real-world examples in documentation
- Plan for regular audits and updates

*Don'ts*
- Create without developer involvement
- Ignore accessibility requirements
- Allow unchecked contributions
- Forget to version components

**References**
- [Material Design](https://www.material.io/design)
- [Carbon Design System](https://carbondesignsystem.com/)

---
## Design System Audit
**Category:** management | **Type:** methodology | **Tags:** design-systems

A systematic review of a design system and its implementation across products to identify inconsistencies, unused components, and improvement opportunities. Design system audits assess health and alignment between system and products.

**Examples**
- Reviewing all products to identify UI patterns not yet documented in the design system
- Analyzing component usage data to identify unused or underutilized components

**Do's and Don'ts**

*Do's*
- Conduct audits regularly (quarterly or biannually)
- Review both the system and product implementations
- Identify inconsistencies and technical debt
- Document findings with evidence
- Prioritize improvements based on impact
- Involve designers and engineers in audit

*Don'ts*
- Audit only the design system files
- Skip checking actual product implementations
- Conduct audits without follow-up actions
- Make audits too infrequent
- Ignore feedback from design system users
- Create massive backlogs without prioritization

**References**
- [Sparkbox: Design System Audit](https://sparkbox.com/foundry/design_system_audit)
- [Brad Frost: Conducting Interface Inventory](https://bradfrost.com/blog/post/conducting-an-interface-inventory/)

---
## Design System Contribution Rate
**Category:** ui | **Type:** methodology | **Tags:** design-systems, analytics

Percentage of design system updates contributed by product designers versus dedicated system team, indicating healthy adoption.

**Examples**
- 28% new components from product teams
- 42% variant contributions
- 15% documentation updates
- Overall contribution rate: 32%

**Do's and Don'ts**

*Do's*
- Credit contributors publicly
- Lower barriers to contribution
- Provide contribution templates
- Review contributions promptly

*Don'ts*
- Gatekeep contributions
- Ignore small improvements
- Require perfect submissions
- Demotivate contributors

**References**
- [Design Systems News: Contribution](https://designsystems.news/contribution/)
- [Design Systems](https://www.designsystems.com/)

---
## Design System Maintenance
**Category:** management | **Type:** methodology | **Tags:** design-systems, processes

The ongoing process of updating, improving, and supporting a design system to keep it relevant, usable, and aligned with product needs. Maintenance includes component updates, documentation improvements, version management, user support, and governance activities.

**Examples**
- Conducting quarterly design system audits to identify outdated components and inconsistencies
- Creating a contribution process for teams to propose new components or patterns
- Updating design tokens when brand guidelines change across all components
- Providing support channels for designers and developers using the system
- Versioning the system and communicating breaking changes to stakeholders
- Tracking component usage to identify unused or underutilized patterns

**Do's and Don'ts**

*Do's*
- Treat the design system as a product with dedicated resources
- Establish clear governance processes and decision-making protocols
- Create channels for user feedback and support requests
- Schedule regular audits of the system and products using it
- Document changes and maintain a public roadmap
- Communicate updates proactively to all users

*Don'ts*
- Assume the design system is "done" after initial launch
- Let the system diverge from actual product implementations
- Make breaking changes without migration guidance
- Ignore feedback from designers and engineers using the system
- Maintain components that no one uses
- Manage the design system as a side project without dedicated time

**References**
- [Brad Frost: Maintaining Design Systems](https://atomicdesign.bradfrost.com/chapter-5/)
- [UXPin: Design System Maintenance Guide](https://www.uxpin.com/studio/blog/design-system-maintenance/)
- [Smashing Magazine: Tips for Managing Design Systems](https://www.smashingmagazine.com/2019/05/tips-managing-design-systems/)

---
## Design Systems First
**Category:** strategy | **Type:** principle | **Tags:** design-systems

Build reusable components before custom work.

**Examples**
- Component library before pages
- Design tokens before colors
- Patterns before prototypes
- Documentation before handoff

**Do's and Don'ts**

*Do's*
- 70% reuse target minimum
- Atomic design methodology
- Cross-team component ownership
- Regular adoption audits

*Don'ts*
- Custom work always
- One-off prototypes
- Designer silos
- No component governance

**References**
- [Atomic Design by Brad Frost](https://atomicdesign.bradfrost.com/)
- [Design Systems](https://www.designsystems.com/)

---
## Design Token Migration
**Category:** ui | **Type:** methodology | **Tags:** design-systems, processes

Systematic process of updating token references across design files, codebases, and documentation during system evolution.

**Examples**
- Migrate from spacing-1 to spacing-xs
- Update color-primary-500 to primary
- Replace legacy typography tokens
- Full system token refresh

**Do's and Don'ts**

*Do's*
- Plan migration in phases
- Provide find/replace scripts
- Communicate timelines clearly
- Verify post-migration

*Don'ts*
- Migrate everything at once
- Skip backward compatibility
- Ignore documentation updates
- Rush without testing

**References**
- [Token Migration Guide](https://theydesign.io/token-migration/)
- [Design Systems CoE](https://coe.designsystems.com/)

---
## Design Token Semantics
**Category:** ui | **Type:** concept | **Tags:** design-systems

Meaningful names describing design intent not values.

**Examples**
- color-danger not #dc2626
- spacing-large not 32px
- radius-rounded not 8px
- Semantic hierarchy

**Do's and Don'ts**

*Do's*
- Describe function purpose
- Platform-agnostic names
- Versioned semantic changes
- Documentation mappings

*Don'ts*
- Technical color names
- Magic number spacing
- Visual radius names
- Hardcoded references

**References**
- [Design Tokens: Semantic](https://design-tokens.github.io/docs/semantic/)
- [Conveyor Design](https://tokens.conveyordesign.com/)

---
## Design Token Synchronization Pipeline
**Category:** ui | **Type:** tool | **Tags:** processes, design-systems

Design-code token consistency automation.

**Examples**
- Figma → Style Dictionary → Code
- Design token pull request
- Automated token validation
- Cross-platform sync

**Do's and Don'ts**

*Do's*
- Semantic token naming
- Automated validation
- Versioned token releases
- Rollback capability

*Don'ts*
- Manual token copying
- Hardcoded values
- Platform drift
- No validation

**References**
- [Design Tokens Community](https://design-tokens.github.io/)
- [Conveyor Design](https://tokens.conveyordesign.com/)

---
## Design Token Usage Coverage
**Category:** ui | **Type:** methodology | **Tags:** design-systems, analytics

Percentage of UI elements referencing design tokens versus hardcoded values, indicating system maturity and maintainability.

**Examples**
- 95% colors use token references
- 88% spacing uses scale values
- 92% typography uses style tokens
- 76% radius uses token values

**Do's and Don'ts**

*Do's*
- Audit regularly across platforms
- Set progressive coverage targets
- Prioritize high-impact tokens
- Automate token usage reports

*Don'ts*
- Assume 100% coverage exists
- Ignore legacy code
- Track only design files
- Skip platform differences

**References**
- [Design Token Metrics](https://theydesign.io/blog/design-token-metrics/)
- [Design Systems CoE](https://coe.designsystems.com/)

---
## Design Tokens
**Category:** ui | **Type:** tool | **Tags:** design-systems

Primitive values (colors, sizes, spacing) stored as variables to maintain consistency across design tools, code, and platforms.

**Examples**
- color-primary: #007acc
- spacing-md: 16px
- radius-lg: 8px
- font-size-xl: 24px

**Do's and Don'ts**

*Do's*
- Use semantic names (e.g., color-danger not #ff0000)
- Define tokens at lowest level (rem not px)
- Document token relationships
- Automate token sync between tools

*Don'ts*
- Mix hardcoded values with tokens
- Use arbitrary numeric values
- Ignore platform differences
- Skip token validation

**References**
- [Design Tokens Community Group](https://design-tokens.github.io/)
- [Tokens Studio](https://tokens.studio/)

---
## Developer Satisfaction (DSAT)
**Category:** ui | **Type:** methodology | **Tags:** design-systems, analytics

Survey-based metric measuring developer experience with design system quality, documentation, and implementation efficiency.

**Examples**
- Documentation clarity: 4.2/5
- Component reliability: 4.5/5
- Handoff quality: 3.8/5
- Overall DSAT: 82%

**Do's and Don'ts**

*Do's*
- Survey quarterly with specific questions
- Act on qualitative feedback
- Track improvements over time
- Share results with design team

*Don'ts*
- Survey anonymously
- Ask leading questions
- Ignore negative outliers
- Skip follow-up actions

**References**
- [Design Systems: Developer Experience](https://www.designsystems.com/developer-experience/)
- [NN/g](https://nngroup.com/)

---
## Diary Studies
**Category:** ux | **Type:** methodology | **Tags:** research

A longitudinal research method where participants self-report their experiences, behaviors, and activities over an extended period. Diary studies capture context and patterns that emerge over time in users' natural environments.

**Examples**
- Having users log their fitness app usage daily for two weeks to understand engagement patterns
- Asking parents to document their morning routines with children over a month to identify pain points

**Do's and Don'ts**

*Do's*
- Provide clear instructions and templates for entries
- Keep entry requirements simple and quick
- Set realistic timeframes and frequency
- Send reminders to maintain participation
- Compensate participants appropriately
- Combine with follow-up interviews for depth

*Don'ts*
- Make diary entries too time-consuming or complex
- Run studies for too long without breaks
- Ignore dropout rates and incomplete entries
- Rely solely on self-reported data
- Forget to pilot test your diary format

**References**
- [Nielsen Norman Group: Diary Studies](https://www.nngroup.com/articles/diary-studies/)
- [UX Collective: Diary Study Guide](https://uxdesign.cc/the-definitive-guide-to-diary-studies-bd90221d6f6c)

---
## Disabled State
**Category:** ui | **Type:** pattern | **Tags:** interaction

Visual indication of unavailable interaction (grayed out, reduced opacity).

**Examples**
- Grayed submit button before validation
- Dimmed menu option when unavailable
- Ghosted icon for disabled feature
- Faded tooltip on disabled item

**Do's and Don'ts**

*Do's*
- Use consistent disabled styling
- Provide disabled state explanation
- Maintain spatial layout
- Test disabled state clarity

*Don'ts*
- Use active colors for disabled
- Remove disabled items entirely
- Inconsistent disabled styling
- No disabled state context

**References**
- [Material Design: Disabled States](https://m3.material.io/foundations/interaction/states)
- [NN/g: Disabled State Patterns](https://www.nngroup.com/articles/disabled-controls/)

---
## Discovery Sprint
**Category:** strategy | **Type:** methodology | **Tags:** strategy, research

Week-long intensive problem validation research.

**Examples**
- Mon: Understand map problems
- Tue: Sketch solutions
- Wed: Decide prototype
- Fri: Test with users

**Do's and Don'ts**

*Do's*
- Real user interviews
- Cross-functional team
- Concrete prototypes
- 5 user interviews min

*Don'ts*
- Fake user interviews
- Designers only team
- PowerPoint prototypes
- Skip user testing

**References**
- [GV: Sprint Zero](https://www.gv.com/sprintzero/)
- [Designlab](https://www.designlab.com/)

---
## Documentation Audit
**Category:** ui | **Type:** tool | **Tags:** documentation, analytics

Review assessing completeness and quality of design documentation.

**Examples**
- Component doc coverage: 87%
- Accessibility spec gaps found
- Variant documentation missing
- Mobile spec completeness

**Do's and Don'ts**

*Do's*
- Score by component type
- Prioritize high-impact gaps
- Track improvement over time
- Share with whole team

*Don'ts*
- Pointless box ticking
- Audit without action plan
- Blame individuals
- Annual only

**References**
- [Design Systems Metrics](https://www.designsystems.com/metrics/)

---
## Documentation Engagement
**Category:** ui | **Type:** tool | **Tags:** analytics, design-systems

Time spent views on system documentation.

**Examples**
- 4m32s avg doc session
- Most-viewed components
- Search term analysis
- Update engagement drop

**Do's and Don'ts**

*Do's*
- Track search behavior
- Most-used vs documented
- Update adoption correlation
- Content performance

*Don'ts*
- Page views only
- No search analysis
- All docs equal
- No update tracking

**References**
- [Zeroheight Analytics](https://zeroheight.com/analytics/)

---
## Dogfood Testing
**Category:** ux | **Type:** methodology | **Tags:** testing, research

Internal team uses own product before external launch.

**Examples**
- Designers use own Figma file
- PMs use own project tool
- Support team uses own CRM
- Daily dogfooding ritual

**Do's and Don'ts**

*Do's*
- Real work not demos
- All team levels participate
- Bug reporting streamlined
- Weekly dogfood debrief

*Don'ts*
- Weekend dogfooding
- Demo data only
- Voluntary participation
- No feedback process

**References**
- [NN/g: Dogfooding](https://www.nngroup.com/articles/dogfooding/)
- [UX Collective](https://uxcollective.com/)

---
## Dot Voting Prioritization
**Category:** ux | **Type:** tool | **Tags:** ideation

Team members allocate limited votes to prioritize ideas.

**Examples**
- 3 dots per person
- Sticker voting on sticky notes
- Digital voting in Miro
- Time-boxed 5-minute voting

**Do's and Don'ts**

*Do's*
- Equal votes per person
- Anonymous voting option
- Clear voting criteria
- Discuss top results

*Don'ts*
- Unlimited votes
- Public pressure voting
- Skip discussion phase
- Ignore outlier votes

**References**
- [NN/g: Dot Voting](https://www.nngroup.com/articles/dot-voting/)
- [Interaction Design Foundation](https://www.interaction-design.org/)

---
## Double Diamond Process
**Category:** strategy | **Type:** methodology | **Tags:** processes

Discover Define Develop Deliver divergent convergent design phases.

**Examples**
- Discover: 2 weeks user research
- Define: Problem statement synthesis
- Develop: Ideation prototyping
- Deliver: User testing iteration

**Do's and Don'ts**

*Do's*
- Equal time divergent/convergent
- Cross-functional team
- Real user validation
- Document key decisions

*Don'ts*
- Skip discovery phase
- Design-only team
- No user testing
- Rush convergence

**References**
- [Design Council: Double Diamond](https://www.designcouncil.org.uk/our-resources/the-double-diamond/)
- [Stanford d.school](https://dschool.stanford.edu/)

---
## Dropdown Menu
**Category:** ui | **Type:** pattern | **Tags:** navigation

Menu expanding downward from trigger showing related options.

**Examples**
- User profile dropdown (Profile, Settings, Logout)
- Language selector dropdown
- Sort options dropdown
- Filter menu dropdown

**Do's and Don'ts**

*Do's*
- Clear trigger affordance
- Logical option grouping
- Keyboard navigation support
- Responsive positioning

*Don'ts*
- Deep nesting in dropdowns
- Too many (>10) options
- Poor mobile handling
- No keyboard escape

**References**
- [NN/g: Dropdown Guidelines](https://www.nngroup.com/articles/drop-down-menus/)
- [UX Collective: Menu Patterns](https://uxdesign.cc/dropdown-menu-design/)

---
## Dynamic Date Range
**Category:** ui | **Type:** pattern | **Tags:** data-visualization, interaction

Slider controls instantly update all charts by selected time period.

**Examples**
- Last 7/30/90/365 days
- Custom date range picker
- Compare periods toggle
- Relative date selection

**Do's and Don'ts**

*Do's*
- Preset popular ranges
- Visual date range indicator
- Bookmarkable selections
- Keyboard arrow controls

*Don'ts*
- Calendar popup only
- No relative dates
- Slow chart updates
- Mobile swipe issues

**References**
- [Looker Studio](https://www.lookerstudio.google.com/)
- [Redash](https://www.redash.io/)

---
## Dynamic Type Scaling
**Category:** ui | **Type:** tool | **Tags:** mobile, accessibility

Text resizes with system accessibility settings.

**Examples**
- SF Pro Dynamic Type
- Roboto scalable text sizes
- Preferred font scaling
- Minimum 11pt readable

**Do's and Don'ts**

*Do's*
- Honor Dynamic Type
- Test all scaling levels
- Responsive layouts
- Legible at max scale

*Don'ts*
- Fixed font sizes
- Layout breaks at 200%
- Minimum 16px clamp
- Desktop font sizing

**References**
- [Apple HIG: Typography](https://developer.apple.com/design/human-interface-guidelines/typography)
- [Material Design](https://m3.material.io/)

---
## Elevator Pitch Framework
**Category:** strategy | **Type:** framework | **Tags:** strategy

30-second compelling value proposition.

**Examples**
- Uber: Tap button car comes
- Slack: Email for teams
- 3 problems 1 solution
- For target user who

**Do's and Don'ts**

*Do's*
- Problem → Solution → Benefit
- Customer-focused language
- 30-second max length
- Practice delivery

*Don'ts*
- Feature dump
- Internal jargon
- 5-minute pitch
- Team-focused not customer

**References**
- [Product Talk: Elevator Pitch Template](https://www.producttalk.org/2020/09/elevator-pitch-template/)
- [Design Better](https://www.designbetter.co/)

---
## Empathy Mapping
**Category:** ux | **Type:** methodology | **Tags:** research

A collaborative visualization tool that captures what users say, think, feel, and do to build shared understanding of user needs and behaviors. Empathy maps synthesize research observations into a simple, digestible format organized into four quadrants.

**Examples**
- Creating an empathy map after user interviews to align the team on user motivations and pain points
- Using empathy maps in workshops to build empathy for different user segments

**Do's and Don'ts**

*Do's*
- Base maps on real research data, not assumptions
- Use the four quadrants: Says, Thinks, Does, Feels
- Create maps collaboratively with cross-functional teams
- Focus on one persona or user segment per map
- Update maps as you learn more about users
- Use maps to generate insights and "How Might We" questions

*Don'ts*
- Create empathy maps without user research
- Confuse empathy maps with personas
- Include too much detail or make them complex
- Use the same map for multiple different user types
- Treat empathy maps as final deliverables
- Skip the synthesis step after creating maps

**References**
- [Nielsen Norman Group: Empathy Mapping](https://www.nngroup.com/articles/empathy-mapping/)
- [UX Collective: Empathy Map Guide](https://uxdesign.cc/empathy-map-a-guide-to-getting-inside-users-head-3c4ad8e29e7f)

---
## Empty State Design
**Category:** ui | **Type:** pattern | **Tags:** information-architecture

Meaningful content guidance when no data exists.

**Examples**
- 'No search results try...'
- 'No orders yet start shopping'
- 'No team members invite first'
- Onboarding empty states

**Do's and Don'ts**

*Do's*
- Actionable next steps
- Visual illustration
- Copy matches context
- Mobile-optimized layout

*Don'ts*
- Blank page error 404
- 'No data available'
- Generic illustration
- Desktop messaging

**References**
- [Empty States](https://emptystat.es/)
- [NN/g](https://www.nngroup.com/articles/)

---
## EN 301 549
**Category:** ui | **Type:** framework | **Tags:** accessibility

EU harmonized ICT accessibility standard incorporating WCAG 2.1 AA + mobile/hardware.

**Examples**
- EN 301 549 V3.2.1 (2021)
- Mandatory for public sector EU
- Hardware + non-web documents
- EAA 2025 compliance baseline

**Do's and Don'ts**

*Do's*
- Follow EN 301 549 Chapter 5 (WCAG)
- Test non-web deliverables too
- Prepare for EAA 2025 enforcement
- Document EU compliance

*Don'ts*
- Ignore non-WCAG chapters
- Skip hardware requirements
- Assume WCAG = full compliance
- No EU market preparation

**References**
- [ETSI EN 301 549 V3.2.1](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf)
- [European Accessibility Act](https://ec.europa.eu/social/main.jsp?catId=1202)

---
## Error Prevention
**Category:** ux | **Type:** principle | **Tags:** interaction

Design eliminates common user mistakes.

**Examples**
- Auto-save form progress
- Confirmation before delete
- Input validation real-time
- Undo capability everywhere

**Do's and Don'ts**

*Do's*
- Confirm destructive actions
- Clear input constraints
- Auto-save/correct formats
- Easy recovery paths

*Don'ts*
- Free text everywhere
- No confirmation dialogs
- Silent form failures
- Irreversible actions

**References**
- [NN/g: Error Messages](https://www.nngroup.com/articles/error-messages/)
- [UX Design CC](https://uxdesign.cc/)

---
## Error Rate Testing
**Category:** ux | **Type:** methodology | **Tags:** testing

Frequency severity of user mistakes during tasks.

**Examples**
- 2.3 errors per task avg
- 41% critical errors
- Learnability error reduction
- Error recovery measurement

**Do's and Don'ts**

*Do's*
- Classify error severity
- Note exact error quotes
- Track error patterns
- Test error recovery

*Don'ts*
- Count all clicks errors
- Ignore error context
- Single test round
- No severity classification

**References**
- [IxDF: Error Rates](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/error-rates)
- [MeasuringU](https://measuringu.com/)

---
## Error Recovery Path
**Category:** ux | **Type:** pattern | **Tags:** interaction

Easy undo back clear fix mechanisms.

**Examples**
- Undo toast notification
- Back button restores state
- Clear form resets
- Draft autosave recovery

**Do's and Don'ts**

*Do's*
- Multiple recovery options
- Clear undo affordance
- State preservation
- Confirmation dialogs

*Don'ts*
- Irreversible actions
- No undo indication
- Lost form progress
- Complex recovery

**References**
- [NN/g: Error Messages](https://www.nngroup.com/articles/error-messages/)
- [UX Movement](https://uxmovement.com/)

---
## Ethnographic Research
**Category:** ux | **Type:** methodology | **Tags:** research

Immersive study natural environment context.

**Examples**
- Shadow doctor 3 days
- Home visit user interviews
- Field study retail workers
- Cultural context immersion

**Do's and Don'ts**

*Do's*
- Naturalistic observation
- Multiple days immersion
- Contextual artifacts
- Team field visits

*Don'ts*
- Lab-based ethnography
- Single visit only
- Questionnaire substitute
- Researcher bias unchecked

**References**
- [NN/g: Ethnographic Research](https://www.nngroup.com/articles/ethnographic-research/)
- [UX Planet](https://uxplanet.org/)

---
## European Accessibility Act (EAA)
**Category:** ui | **Type:** framework | **Tags:** accessibility

EU law mandating accessibility for digital products/services (effective June 2025).

**Examples**
- Applies to e-commerce, banking apps
- €100K+ fines for non-compliance
- WCAG 2.1 AA + EN 301 549 baseline
- 5-year remediation period

**Do's and Don'ts**

*Do's*
- Plan EAA compliance now
- Audit against EN 301 549
- Budget for accessibility retrofits
- Train teams on EU requirements

*Don'ts*
- Wait until 2025 enforcement
- Assume WCAG covers everything
- Skip non-web requirements
- Ignore supply chain compliance

**References**
- [European Commission: EAA](https://ec.europa.eu/social/main.jsp?catId=1202)
- [Level Access: EAA Guide](https://www.levelaccess.com/blog/european-accessibility-act/)

---
## Executive Briefing Deck
**Category:** strategy | **Type:** tool | **Tags:** strategy

Concise 5-8 slide leadership communication.

**Examples**
- Problem 1 slide
- Solution 2 slides
- Proof 1 slide
- Ask 1 slide

**Do's and Don'ts**

*Do's*
- 5-8 slides maximum
- Data visualization
- Clear single ask
- Rehearsed 10min delivery

*Don'ts*
- 25+ slide decks
- Text walls
- Multiple competing asks
- Unprepared delivery

**References**
- [Amazon: Briefings](https://www.amazon.press/briefings)
- [First Round Review](https://firstround.com/)

---
## Executive Summary Chart
**Category:** strategy | **Type:** tool | **Tags:** data-visualization, strategy

Single chart conveys business situation instantly to leadership.

**Examples**
- Single KPI vs target
- Traffic light status summary
- 3-number business health
- Revenue vs forecast

**Do's and Don'ts**

*Do's*
- Answer business question
- Single visual metaphor
- Large clear typography
- Mobile-first design

*Don'ts*
- Multiple complex charts
- Raw data tables
- Industry jargon
- Missing action context

**References**
- [Dual Brain: Executive Dashboard Design](https://www.dualbrain.com/2014/09/executive-dashboard-design.html)
- [Toptal](https://www.toptal.com/)

---
## Exit Page Analysis
**Category:** ux | **Type:** tool | **Tags:** analytics

Where users abandon before completing goals.

**Examples**
- 41% exit checkout step 2
- 28% pricing page exit
- Mobile exit page patterns
- Recovery A/B experiments

**Do's and Don'ts**

*Do's*
- Segment by traffic source
- Time-on-exit-page
- Recovery experiments
- Qualitative exit research

*Don'ts*
- Single exit page focus
- No segmentation
- No recovery testing
- Desktop-only analysis

**References**
- [Hotjar: Exit Pages](https://www.hotjar.com/blog/exit-pages/)
- [CXL](https://cxl.com/)

---
## F-Pattern
**Category:** ui | **Type:** pattern | **Tags:** visual-hierarchy

Content-heavy scan (top horizontal → left vertical → horizontals) for maximum visibility.

**Examples**
- Blog article layout with sidebar
- News feed structure
- Search results page
- Long-form content with navigation

**Do's and Don'ts**

*Do's*
- Headlines/CTAs in F-hotspots
- Structure content by F-path
- Blogs/articles layouts
- Test with heatmaps

*Don'ts*
- Important content off F-path
- Force grid on F-content
- Ignore content patterns
- Assume uniform scanning

**References**
- [NN/g: F-Pattern](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)
- [Eleken: UX Tips](https://www.eleken.co/blog-posts/f-pattern-in-ux-design)

---
## Faceted Navigation
**Category:** ux | **Type:** pattern | **Tags:** information-architecture, navigation

Multi-attribute filtering of content results.

**Examples**
- Color + Size + Brand filters
- Price range + Rating + Category
- Location + Date + Type
- Tags + Status + Priority

**Do's and Don'ts**

*Do's*
- Independent facets first
- Show count per facet
- Sticky filter panel
- Clear all option

*Don'ts*
- Dependent filters only
- No count indicators
- Collapsed by default
- No URL parameters

**References**
- [Baymard: Facets](https://www.baymard.com/lists/facets)
- [NN/g](https://nngroup.com/)

---
## Fake Door Test
**Category:** ux | **Type:** methodology | **Tags:** testing

A validation technique that measures interest in a feature by adding an entry point for it in the interface before building it. Also called Smoke Test, fake door tests use click-through rates to assess demand and prevent wasted effort on unwanted features.

**Examples**
- Adding a "Premium Analytics" menu item that leads to a coming soon page to measure interest
- Including a button for an unbuilt feature to see how many users attempt to access it

**Do's and Don'ts**

*Do's*
- Make the entry point realistic and discoverable
- Communicate clearly when users click through
- Track both clicks and user characteristics
- Follow up with interested users for feedback
- Use to validate demand before building
- Be transparent about feature status

*Don'ts*
- Frustrate users with too many fake doors
- Mislead users about feature availability
- Test features you don't intend to build
- Ignore users who show interest
- Use fake doors in production indefinitely
- Create fake doors for critical features users expect

**References**
- [ProductPlan: Fake Door Testing](https://www.productplan.com/glossary/fake-door-test/)
- [Lean Startup: Smoke Tests](https://theleanstartup.com/principles)

---
## Feature Adoption Rate
**Category:** ux | **Type:** tool | **Tags:** analytics

Percentage users using specific new feature.

**Examples**
- 23% used AI search week 1
- 68% power users adoption
- Feature cohort retention
- Cross-feature correlation

**Do's and Don'ts**

*Do's*
- Track week 1 4 12 adoption
- Power vs average users
- Retention by adoption
- Feature interaction matrix

*Don'ts*
- Single timepoint measure
- All users equal
- No power user analysis
- Ignore feature interplay

**References**
- [Amplitude: Feature Adoption](https://amplitude.com/blog/feature-adoption/)

---
## Feedback Loops
**Category:** management | **Type:** concept | **Tags:** processes

Systematic mechanisms for collecting, analyzing, and acting on information to drive continuous improvement. Feedback loops create cycles where outputs inform future inputs, enabling teams to learn and adapt iteratively.

**Examples**
- Weekly review of customer support tickets to identify recurring issues
- Monthly synthesis of usability test findings to inform design priorities

**Do's and Don'ts**

*Do's*
- Create short feedback loops for faster learning
- Close the loop by acting on feedback
- Make feedback loops systematic and regular
- Share learnings across the organization
- Measure the impact of changes
- Combine multiple feedback sources

*Don'ts*
- Collect feedback without acting on it
- Make feedback loops too long
- Rely on a single feedback source
- Skip communicating what you learned
- Let feedback loops become performative
- Ignore negative or uncomfortable feedback

**References**
- [Harvard Business Review: The Feedback Loop](https://hbr.org/2011/07/the-power-of-small-wins)
- [ProductPlan: Product Feedback Loop](https://www.productplan.com/glossary/product-feedback-loop/)

---
## Feedback Principle
**Category:** ui | **Type:** principle | **Tags:** interaction

System confirms actions with immediate visible response.

**Examples**
- Button press animation
- Loading spinner on submit
- Success message toast
- Drag preview visualization

**Do's and Don'ts**

*Do's*
- Immediate visual feedback
- Loading states clear
- Success/error confirmation
- Progress indication

*Don'ts*
- Silent form submission
- No button press states
- Indeterminate loading
- Invisible interactions

**References**
- [NN/g: Feedback](https://www.nngroup.com/articles/feedback/)
- [Adrian Roselli](https://adrianroselli.com/)

---
## Field Studies
**Category:** ux | **Type:** methodology | **Tags:** research

Research conducted in the user's natural environment by observing behavior and interactions in real-world contexts. Also called ethnographic research, field studies reveal how users actually behave rather than how they say they behave.

**Examples**
- Observing shoppers in a retail store to understand browsing and purchasing behavior
- Spending time with delivery drivers to understand their daily workflow and challenges

**Do's and Don'ts**

*Do's*
- Immerse yourself in the user's environment
- Observe actual behavior over extended periods
- Document environmental factors that influence behavior
- Build rapport and trust with participants
- Look for patterns across multiple observations
- Capture photos and videos when appropriate

*Don'ts*
- Make quick judgments based on limited observation
- Ignore the context surrounding user behavior
- Rely only on what users say without observing
- Conduct field studies in artificial settings
- Forget to get proper permissions and consent

**References**
- [Nielsen Norman Group: Field Studies](https://www.nngroup.com/articles/field-studies/)
- [Interaction Design Foundation: Ethnographic Research](https://www.interaction-design.org/literature/topics/ethnographic-research)

---
## Figma Library
**Category:** ui | **Type:** tool | **Tags:** design-systems, documentation

Shared Figma file containing master components, styles, and assets synchronized across design team files for consistency.

**Examples**
- Published components library
- Color styles collection
- Text styles with variables
- Effects and grid styles

**Do's and Don'ts**

*Do's*
- Use components over symbols
- Publish frequently with changelogs
- Organize by abstraction level
- Include usage documentation

*Don'ts*
- Publish untested components
- Use local overrides heavily
- Ignore variant organization
- Forget to detach instances

**References**
- [Figma: Libraries Best Practices](https://www.figma.com/best-practices/libraries/)

---
## Filter Panel
**Category:** ux | **Type:** pattern | **Tags:** information-architecture, web

Collapsible panel containing facet controls.

**Examples**
- Left sidebar on desktop
- Modal overlay on mobile
- Top filter chips
- Drawer from top/bottom

**Do's and Don'ts**

*Do's*
- Sticky on scroll
- Visual count badges
- Collapsible sections
- Keyboard accessible

*Don'ts*
- Always expanded
- Tiny touch targets
- No clear/reset
- Poor mobile layout

**References**
- [UIE](https://www.uie.com/)
- [Pttrns](https://pttrns.com/)

---
## First-Click Testing
**Category:** ux | **Type:** methodology | **Tags:** testing, information-architecture

Where users click first reveals IA effectiveness.

**Examples**
- 32 users find 'cancel sub'
- 78% correct first click
- Tree testing validation
- 100ms response capture

**Do's and Don'ts**

*Do's*
- Text-only tree structure
- Single clear find task
- Benchmark success rates
- Large sample 30+

*Don'ts*
- Visual design distractions
- Multiple find tasks
- Small sample size
- No success benchmarking

**References**
- [Treejack](https://www.treejack.com/)
- [Optimal Workshop: First Click](https://optimalworkshop.com/first-click)

---
## Fitts's Law
**Category:** ux | **Type:** principle | **Tags:** interaction

Time to reach target inversely proportional to size, directly proportional to distance.

**Examples**
- Large buttons easier to tap
- Menu items at screen edges
- Primary CTA full viewport width
- Thumb-friendly mobile targets

**Do's and Don'ts**

*Do's*
- Make important targets large
- Place targets near cursor path
- Minimize pointer travel distance
- Use keyboard shortcuts

*Don'ts*
- Tiny touch targets (<44px)
- Deeply nested menus
- Targets in screen corners
- Inconsistent sizing

**References**
- [NN/g: Fitts's Law](https://www.nngroup.com/articles/fitts-law/)
- [Laws of UX: Fitts's Law](https://lawsofux.com/fittss-law/)

---
## Five-Second Testing
**Category:** ux | **Type:** methodology | **Tags:** testing, research

Brief exposure tests instant comprehension memory.

**Examples**
- 5sec hero section exposure
- 'What is main message?'
- 65% correct comprehension
- Brand recall testing

**Do's and Don'ts**

*Do's*
- Single clear question
- Exact 5-second timer
- Large sample 50+
- Multiple design variants

*Don'ts*
- Vague recall questions
- Longer than 5 seconds
- Small sample size
- No benchmarking

**References**
- [Five Second Test](https://fivesecondtest.com/)
- [NN/g](https://www.nngroup.com/)

---
## Flexbox Container
**Category:** ui | **Type:** tool | **Tags:** web

One-dimensional layout for aligning distributing items.

**Examples**
- Navigation flex row wrap
- Card grid with gap
- Centered hero content
- Vertical button stack

**Do's and Don'ts**

*Do's*
- flex properties logical
- Gap instead margins
- Order for visual only
- Single dimension focus

*Don'ts*
- Float clearing hacks
- Inline-block whitespace
- Table-cell layouts
- CSS Grid for 1D

**References**
- [CSS-Tricks: Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [MDN](https://developer.mozilla.org/en-US/)

---
## Floating Action Button
**Category:** ui | **Type:** pattern | **Tags:** mobile

Prominent circular button for primary app action.

**Examples**
- + button for new message
- Camera icon for photo capture
- Compose tweet FAB
- New event calendar button

**Do's and Don'ts**

*Do's*
- Single prominent action
- Speed dial expansion
- Elevation shadow
- Resting state visible

*Don'ts*
- Multiple FABs competing
- Secondary action placement
- Hidden behind content
- Desktop positioning

**References**
- [Material Design: FAB](https://m3.material.io/components/floating-action-button)
- [Apple Developer](https://developer.apple.com/)

---
## Focal Point
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy

Single dominant element capturing initial attention using multiple techniques.

**Examples**
- Hero section with prominent CTA button
- Hero image with centered text overlay
- Dashboard with highlighted key metric
- Landing page with dominant headline

**Do's and Don'ts**

*Do's*
- One focal point per screen
- Combine size/color/contrast
- Position by reading patterns
- Test with heatmaps

*Don'ts*
- Multiple competing focal points
- Subtle focal techniques
- Random focal positioning
- Ignore page hierarchy

**References**
- [99designs: Visual Hierarchy](https://99designs.com/blog/tips/visual-hierarchy-design-principles/)
- [CareerFoundry: Hierarchy Guide](https://careerfoundry.com/en/blog/ui-design/visual-hierarchy/)

---
## Focus Groups
**Category:** ux | **Type:** methodology | **Tags:** research

A moderated group discussion with 6-10 participants to explore attitudes, perceptions, and opinions about a product, service, or concept. Focus groups gather diverse perspectives through facilitated conversation and group dynamics.

**Examples**
- Discussing reactions to new product concepts with target customers before development
- Exploring pain points in current user experience with existing customers

**Do's and Don'ts**

*Do's*
- Recruit participants who represent your target audience
- Prepare a discussion guide with open-ended questions
- Encourage all participants to share their views
- Watch for group dynamics and dominant voices
- Record sessions for later analysis
- Use focus groups for exploratory research

*Don'ts*
- Rely on focus groups as your only research method
- Let one person dominate the conversation
- Ask leading questions that bias responses
- Use focus groups to validate usability or design decisions
- Take group consensus as fact
- Mix stakeholders with end users in the same session

**References**
- [Nielsen Norman Group: Focus Groups](https://www.nngroup.com/articles/focus-groups/)
- [Maze: Focus Group Guide](https://maze.co/guides/ux-research/focus-groups/)

---
## Focus Indicator
**Category:** ui | **Type:** principle | **Tags:** accessibility, interaction

Visible outline showing current keyboard focus location.

**Examples**
- 2px blue outline on buttons
- Focus ring around interactive elements
- :focus-visible CSS selector
- High contrast focus styling

**Do's and Don'ts**

*Do's*
- Minimum 2px thick indicators
- 3:1 contrast minimum
- Visible on ALL focusable elements
- Consistent styling

*Don'ts*
- Remove focus styles (:focus {outline:0})
- Low contrast focus rings
- Inconsistent indicators
- Mouse-only focus styling

**References**
- [WCAG 2.1: Focus Visible (2.4.7)](https://www.w3.org/WAI/WCAG21/Understanding/focus-visible.html)
- [WebAIM: Focus Indicators](https://webaim.org/techniques/keyboard/)

---
## Focus Management
**Category:** ui | **Type:** pattern | **Tags:** accessibility

Logical predictable keyboard focus order.

**Examples**
- Tab order matches reading
- Skip links available
- Focus visible consistent
- Dynamic content management

**Do's and Don'ts**

*Do's*
- Logical DOM order
- Skip repetitive content
- Focus indicators 3:1 contrast
- Screen reader announcement

*Don'ts*
- Tabindex manipulation
- Invisible focus
- Trapped focus areas
- Arbitrary order

**References**
- [WebAIM: Focusable](https://webaim.org/techniques/focusable/)
- [BOIA](https://www.boia.org/)

---
## Focus Order
**Category:** ui | **Type:** principle | **Tags:** accessibility, navigation

Logical tab sequence matching visual reading order.

**Examples**
- Top navigation → hero → form → footer
- Left-to-right, top-to-bottom flow
- Modals trap focus logically
- Logical order despite CSS reordering

**Do's and Don'ts**

*Do's*
- Matches visual reading order
- Skip repetitive navigation
- Modal focus trapping
- Test complete tab paths

*Don'ts*
- Tab jumps around screen
- Reverse tab order
- Navigation at page end
- Visual vs logical mismatch

**References**
- [WCAG 2.4.3: Focus Order](https://www.w3.org/WAI/WCAG21/Understanding/focus-order.html)
- [WebAIM: Keyboard Shortcuts](https://webaim.org/techniques/keyboard/)

---
## Focus State
**Category:** ui | **Type:** pattern | **Tags:** interaction, accessibility

Keyboard navigation highlight for accessibility and screen readers.

**Examples**
- Input field blue outline on tab
- Button focus ring on keyboard nav
- Menu item highlight on arrow keys
- Link focus indicator

**Do's and Don'ts**

*Do's*
- Use high-contrast focus indicators
- Consistent focus styling
- Support keyboard navigation
- Test with screen readers

*Don'ts*
- Remove focus styles
- Inconsistent focus indicators
- Low-contrast focus rings
- Ignore keyboard users

**References**
- [WebAIM: Focus Indicators](https://webaim.org/techniques/keyboard/)
- [WCAG 2.1: Focus Visible](https://www.w3.org/WAI/WCAG21/Understanding/focus-visible.html)

---
## Font Ascender
**Category:** ui | **Type:** concept | **Tags:** typography

Part of lowercase letters that extends above the x-height line (e.g., 'h', 'k', 'l', 'b', 'd'). Ascenders contribute to letter differentiation and rhythm in text blocks.

**Examples**
- Ensuring adequate line spacing to prevent ascender collision
- Checking ascender clarity in fonts used for small text
- Evaluating ascender proportions when selecting typefaces
- Testing how ascenders affect vertical rhythm in layouts

**Do's and Don'ts**

*Do's*
- Ensure ascenders have adequate space from lines above
- Use fonts where ascenders are clearly defined
- Account for ascender height in line spacing calculations
- Test ascender clarity at small sizes

*Don'ts*
- Crop or hide ascenders in UI layouts
- Use excessive line height that breaks ascender-descender balance
- Choose fonts with weak or ambiguous ascenders
- Ignore ascender impact on visual rhythm

**References**
- [Monotype: A Glossary of Typographic Terms](https://www.monotype.com/resources/expertise/typography-terms)
- [Tom Chalky: Your Ultimate Typography Glossary](https://tomchalky.com/typography-glossary)

---
## Font Descender
**Category:** ui | **Type:** concept | **Tags:** typography

Part of lowercase letters that extends below the baseline (e.g., 'g', 'j', 'p', 'q', 'y'). Descenders require adequate vertical space and affect line height calculations in UI design.

**Examples**
- Reserving space below text in buttons to prevent descender clipping
- Adjusting form field heights to accommodate descenders
- Testing descender rendering in different fonts
- Ensuring descenders don't overlap with content below

**Do's and Don'ts**

*Do's*
- Reserve sufficient space below baseline for descenders
- Account for descenders in button and form field sizing
- Ensure descenders don't overlap with elements below
- Use consistent descender depth across typefaces

*Don'ts*
- Crop descenders in UI elements
- Ignore descender space in line height calculations
- Use fonts with inconsistent descender lengths
- Place descenders too close to content below

**References**
- [Monotype: A Glossary of Typographic Terms](https://www.monotype.com/resources/expertise/typography-terms)
- [UX Planet: Principles of Typography in UI Design](https://uxplanet.org/principles-of-typography-in-ui-design)

---
## Font Display Swap
**Category:** ui | **Type:** tool | **Tags:** web, typography

Show fallback font immediately while custom loads.

**Examples**
- font-display: swap declaration
- font-display: block FOIT fix
- Preload critical font files
- Fallback font stack

**Do's and Don'ts**

*Do's*
- font-display: swap default
- Preload hero fonts
- System font fallback
- Multiple fallback weights

*Don'ts*
- No font-display
- FOIT/FOUT issues
- Single web font only
- No preload strategy

**References**
- [WebKit: Font Display](https://webkit.org/blog/10748/font-display/)
- [Google Chrome: Font Display Samples](https://googlechrome.github.io/samples/font-display/)

---
## Font Hierarchy
**Category:** ui | **Type:** principle | **Tags:** typography, visual-hierarchy

Use of size, weight, color, and style to denote content importance and guide user focus. Font hierarchy creates visual structure that helps users scan and understand content priority.

**Examples**
- Using H1 for page titles, H2 for sections, body for content
- Combining larger size with bold weight for primary headings
- Using color to differentiate links from body text
- Creating caption styles for secondary information

**Do's and Don'ts**

*Do's*
- Use 3-4 hierarchy levels maximum (H1, H2, body, caption)
- Combine size and weight for clear distinction
- Maintain consistent hierarchy across pages
- Use hierarchy to highlight key information

*Don'ts*
- Create too many hierarchy levels (confusing)
- Use weight alone without size variation
- Break hierarchy for decorative purposes
- Apply hierarchy inconsistently across interface

**References**
- [Kaarwan: Typography Best Practices for UI Design](https://www.kaarwan.com/blog/typography-best-practices)
- [UX Collective: 10 Principles for Typography in UI Design](https://uxdesign.cc/10-principles-for-typography-in-ui-design)

---
## Font Kerning
**Category:** ui | **Type:** tool | **Tags:** typography

Adjustment of space between individual letter pairs to improve visual balance and readability. Kerning compensates for the irregular shapes of letters, making text appear more cohesive.

**Examples**
- Adjusting space between 'A' and 'V' to prevent excessive gaps
- Tightening kerning in headlines for visual impact
- Fine-tuning letter pairs in logo design for brand consistency
- Compensating for problematic pairs like 'T' and 'o'

**Do's and Don'ts**

*Do's*
- Kern letter pairs with irregular spacing (e.g., 'A' and 'V')
- Use kerning to improve headlines and large display text
- Adjust kerning proportionally based on font size and context
- Test kerning across different screen sizes and zoom levels

*Don'ts*
- Apply uniform kerning to all letter combinations
- Over-kern, creating excessive gaps between letters
- Ignore font designer's built-in kerning pairs
- Kern small body text at 12px or below (harder to perceive)

**References**
- [Interaction Design Foundation: The UX Designer's Guide to Typography](https://www.interaction-design.org/literature/article/the-ux-designer-s-guide-to-typography)
- [Monotype: A Glossary of Typographic Terms](https://www.monotype.com/resources/expertise/typography-terms)

---
## Font Leading
**Category:** ui | **Type:** tool | **Tags:** typography

Vertical space between lines of text (line height). Named after the lead strips used in traditional typography, leading directly impacts readability and visual rhythm in text blocks.

**Examples**
- Setting 1.5x line height for body text to improve readability
- Using tighter leading in headlines for compact visual impact
- Increasing leading for long paragraphs to aid scanning
- Adjusting leading proportionally when scaling font sizes

**Do's and Don'ts**

*Do's*
- Use 1.4-1.6x line height for body text (optimal for web)
- Increase leading for long paragraphs to aid scanning
- Apply tighter leading to headlines and display text
- Scale leading proportionally with font size

*Don'ts*
- Use leading less than 1.2x for body text (cramped)
- Apply excessive leading that breaks paragraph cohesion
- Ignore leading in mobile contexts (responsive adjustment needed)
- Use fixed pixel-based leading instead of relative units

**References**
- [NN/g: Typography Terms Glossary](https://www.nngroup.com/articles/typography-terms-ux/)
- [FlowMapp: 20 Basic Typographic Terms for UI Designers](https://www.flowmapp.com/blog/typographic-terms)

---
## Font Tracking
**Category:** ui | **Type:** tool | **Tags:** typography

Uniform adjustment of space between all letters in a word or line. Unlike kerning, tracking applies the same spacing value across an entire text block for consistent letter density.

**Examples**
- Increasing tracking in all-caps headings for improved legibility
- Applying loose tracking to create an elegant, airy feel in display text
- Using negative tracking for dense content to save space
- Adjusting tracking for different font weights

**Do's and Don'ts**

*Do's*
- Use tracking for headlines to create emphasis
- Increase tracking for all-caps text to improve legibility
- Apply negative tracking to dense content to save space
- Adjust tracking based on font size and weight

*Don'ts*
- Apply excessive tracking that breaks word cohesion
- Use positive tracking for small body text (reduces readability)
- Forget that tracking affects perceived font weight
- Apply tracking inconsistently across similar elements

**References**
- [Interaction Design Foundation: The UX Designer's Guide to Typography](https://www.interaction-design.org/literature/article/the-ux-designer-s-guide-to-typography)
- [Kaarwan: Typography Best Practices for UI Design](https://www.kaarwan.com/blog/typography-best-practices)

---
## Font Weight
**Category:** ui | **Type:** tool | **Tags:** typography, visual-hierarchy

Thickness of characters in a font (e.g., Light, Regular, Bold, Black). Font weight creates visual emphasis, hierarchy, and contrast while maintaining a consistent typeface family.

**Examples**
- Using Regular (400) for body text and Bold (700) for headings
- Applying Light weight for large display text
- Using Semi-Bold (600) for subheadings
- Combining weight variations within a single font family

**Do's and Don'ts**

*Do's*
- Use weight variation for hierarchy (Light → Regular → Bold → Black)
- Limit to 2-3 weights per interface for clarity
- Combine weight with size for emphasis
- Test weight rendering across browsers and devices

*Don'ts*
- Use excessive weights that confuse hierarchy
- Mix weights from different font families
- Rely on weight alone for emphasis
- Use extreme weights for body text

**References**
- [UX Design Institute: 10 Principles for Typography in UI Design](https://www.uxdesigninstitute.com/blog/typography-principles/)
- [Material Design 3: Typography](https://m3.material.io/styles/typography)

---
## Font X-Height
**Category:** ui | **Type:** concept | **Tags:** typography

Height of lowercase letters (excluding ascenders and descenders) in a font. X-height significantly influences perceived font size and legibility at small sizes, even when point size remains constant.

**Examples**
- Choosing fonts with generous x-height for mobile interfaces
- Comparing x-heights when pairing typefaces for visual harmony
- Selecting high x-height fonts for small UI labels and captions
- Testing perceived size differences between fonts at the same point size

**Do's and Don'ts**

*Do's*
- Choose fonts with generous x-height for small body text (10-14px)
- Consider x-height when pairing typefaces
- Test x-height perception across different sizes
- Account for x-height in accessibility considerations

*Don'ts*
- Ignore x-height when selecting fonts for readability
- Mix fonts with vastly different x-heights in hierarchy
- Assume point size alone determines legibility
- Use fonts with tiny x-height for UI text

**References**
- [Monotype: A Glossary of Typographic Terms](https://www.monotype.com/resources/expertise/typography-terms)
- [Designlab: 20 Typography Terms You Need to Know](https://designlab.com/blog/typography-terms)

---
## Footer Navigation
**Category:** ui | **Type:** pattern | **Tags:** navigation

Bottom-of-page links for secondary navigation, legal, and utility content.

**Examples**
- Company info, legal links, social media
- Secondary categories
- Newsletter signup
- Contact/sitemap links

**Do's and Don'ts**

*Do's*
- Secondary/supporting content only
- Consistent across site
- Mobile-responsive columns
- Clear visual separation

*Don'ts*
- Primary navigation in footer
- Overload with too many links
- Poor mobile stacking
- Duplicate top nav

**References**
- [NN/g: Footer Patterns](https://www.nngroup.com/articles/footers/)
- [UX Planet: Navigation Glossary](https://uxplanet.org/ux-glossary-navigation/)

---
## Frequency Histogram
**Category:** ui | **Type:** tool | **Tags:** data-visualization

Adjacent bars show distribution frequency of continuous numeric data.

**Examples**
- Age distribution of customers
- Response times histogram
- File sizes distribution
- Test scores frequency

**Do's and Don'ts**

*Do's*
- Equal bin widths
- Clear bin labeling
- Start at zero
- Smooth curve overlay

*Don'ts*
- Unequal bin sizes
- Too few/many bins
- Gaps between bars
- Category data

**References**
- [Histogram](https://www.histogram.com/)
- [Seeing Data Viz](https://seeing-dataviz.com/)

---
## Funnel Drop-off Analysis
**Category:** ux | **Type:** methodology | **Tags:** research, analytics

Drop-off rates at each conversion step.

**Examples**
- Checkout funnel 68% cart drop
- Signup funnel step analysis
- Feature adoption funnel
- A/B test funnel comparison

**Do's and Don'ts**

*Do's*
- Segment by traffic source
- Mobile vs desktop split
- Historical trend comparison
- Qualitative exit research

*Don'ts*
- Single device analysis
- No segmentation
- Vanity metrics focus
- No qualitative follow-up

**References**
- [Amplitude: Funnel Analysis](https://amplitude.com/blog/funnel-analysis)

---
## Gamestorming
**Category:** strategy | **Type:** methodology | **Tags:** ideation

A set of facilitation techniques that use game mechanics and playful activities to enhance ideation, problem-solving, and collaboration. Gamestorming structures creative sessions with clear rules, goals, and time constraints to increase engagement and output.

**Examples**
- Using "6-3-5" where 6 people sketch 3 ideas in 5 minutes, then pass papers to iterate
- Playing "Crazy Eights" to rapidly generate 8 different solution sketches in 8 minutes

**Do's and Don'ts**

*Do's*
- Choose games that match your objective
- Explain rules clearly before starting
- Set time limits to maintain energy
- Use visual and physical materials
- Debrief and reflect after games
- Combine multiple games in a session

*Don'ts*
- Use games without clear purpose
- Let games run too long without timeboxing
- Skip the warm-up activities
- Force participation without explaining benefits
- Use complex games with unclear rules
- Forget to capture insights and outputs

**References**
- [Gamestorming: Official Website](https://gamestorming.com/)
- [Interaction Design Foundation: Gamestorming](https://www.interaction-design.org/literature/article/gamestorming-a-playbook-for-innovators-rulebreakers-and-changemakers)

---
## Gestalt Closure
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy

Incomplete shapes recognized as whole when context suggests completion.

**Examples**
- Circular progress indicator with gap suggesting completion
- Loading spinner with missing segment implying motion
- Logo with negative space creating implied shapes
- Icon outline with strategic gaps still read as complete

**Do's and Don'ts**

*Do's*
- Use incomplete circles for progress
- Create implied shapes with spacing
- Apply closure for icons/logos
- Test closure recognition

*Don'ts*
- Make shapes too incomplete
- Use closure for critical info
- Ignore closure on small screens
- Over-rely on closure effect

**References**
- [GestaltPrinciples.com](https://www.gestaltprinciples.com/)
- [Eleken: Gestalt Principles](https://www.eleken.co/blog-posts/gestalt-principles-in-ui-design)

---
## Gestalt Common Fate
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy, interaction

Elements moving same direction perceived as belonging together.

**Examples**
- Menu items sliding open together
- Grouped animations for related actions
- Cards transitioning simultaneously
- Elements scrolling as single unit

**Do's and Don'ts**

*Do's*
- Animate grouped elements together
- Use motion for related actions
- Apply common fate to transitions
- Test motion grouping

*Don'ts*
- Animate unrelated items together
- Use conflicting motion directions
- Over-animate for common fate
- Ignore motion accessibility

**References**
- [Userbit: Gestalt in UX](https://userbit.com/blog/gestalt-principles-ux)
- [Artversion: Gestalt Hierarchies](https://artversion.com/blog/gestalt-principles/)

---
## Gestalt Common Region
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy

Elements within same bounded area automatically grouped together.

**Examples**
- Card component grouping related info
- Sidebar section with background color
- Modal dialog containing form elements
- Section with distinct background/border

**Do's and Don'ts**

*Do's*
- Use cards for content chunks
- Background containers for sections
- Consistent region styling
- Test region grouping

*Don'ts*
- Inconsistent region boundaries
- Overlapping region boundaries
- Too many nested regions
- Ignore region hierarchy

**References**
- [UX Tigers: Gestalt Principles](https://www.uxtigers.com/post/gestalt-ui)
- [Eleken: Gestalt Design](https://www.eleken.co/blog-posts/gestalt-principles-in-ui-design)

---
## Gestalt Connectedness
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy

Connected elements (lines/shapes) perceived as single continuous unit.

**Examples**
- Process flow with connecting lines between steps
- Menu items linked with lines
- Breadcrumb trail with separator lines
- Connected nodes in flowchart diagram

**Do's and Don'ts**

*Do's*
- Connect related menu items
- Use lines for process flows
- Link grouped actions visually
- Test connectedness perception

*Don'ts*
- Connect unrelated elements
- Use ambiguous connections
- Overuse connectedness
- Break connections responsively

**References**
- [Interaction Design Foundation: Gestalt Principles](https://www.interaction-design.org/literature/topics/gestalt-principles)
- [Toptal: Gestalt Design](https://www.toptal.com/designers/ui/gestalt-principles-of-design)

---
## Gestalt Continuity
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy

Eye follows lines/shapes in smooth, continuous paths rather than abrupt changes.

**Examples**
- Diagonal line flow from top-left to bottom-right
- Breadcrumb trail guiding eye through navigation
- Multi-step process with connecting lines
- Form layout flowing vertically without jarring breaks

**Do's and Don'ts**

*Do's*
- Align elements along visual paths
- Create flow lines with spacing
- Use continuity for navigation
- Guide eye through content flow

*Don'ts*
- Break continuity randomly
- Force unnatural eye paths
- Ignore continuity in grids
- Use conflicting flow directions

**References**
- [Superside: 11 Gestalt Principles](https://www.superside.com/blog/gestalt-principles)
- [UX Tigers: Gestalt Principles](https://www.uxtigers.com/post/gestalt-ui)

---
## Gestalt Enclosure
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy

Containers/borders/backgrounds defining content chunks and hierarchy levels.

**Examples**
- Card with shadow containing related info
- Modal dialog with distinct border
- Nested containers for subsections
- Form fieldset with visual grouping

**Do's and Don'ts**

*Do's*
- Cards for content separation
- Nested enclosure hierarchy
- Consistent container styling
- Support content flow

*Don'ts*
- Overuse enclosure (clutter)
- Inconsistent enclosure styles
- Break enclosure hierarchy
- Ignore spacing relationships

**References**
- [Maze: Visual Hierarchy](https://maze.co/guides/visual-hierarchy/)
- [Interaction Design Foundation: Visual Hierarchy](https://www.interaction-design.org/literature/topics/visual-hierarchy)

---
## Gestalt Figure-Ground
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy, color

Distinguishing main subject (figure) from background (ground) through contrast.

**Examples**
- White button text on dark background
- Primary content highlighted against neutral background
- Modal overlay with focal content centered
- Foreground element with blurred background

**Do's and Don'ts**

*Do's*
- High contrast for primary content
- Clear figure-ground separation
- Test figure-ground on all devices
- Use negative space effectively

*Don'ts*
- Low contrast figure-ground
- Ambiguous subject-background
- Busy backgrounds competing
- Poor contrast accessibility

**References**
- [Interaction Design Foundation: Gestalt Principles](https://www.interaction-design.org/literature/topics/gestalt-principles)
- [Figma: Gestalt Principles](https://www.figma.com/resource-library/gestalt-principles/)

---
## Gestalt Proximity
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy

Close elements perceived as grouped; spacing defines relationships and creates visual chunks.

**Examples**
- Form fields grouped by topic with spacing between sections
- Navigation items clustered together, separate from content
- Related buttons grouped close together vs isolated actions
- Card components with consistent padding creating groups

**Do's and Don'ts**

*Do's*
- Group related form fields together
- Use consistent spacing scales
- Test grouping perception with users
- Apply proximity consistently

*Don'ts*
- Scatter related elements randomly
- Use inconsistent spacing
- Overcrowd proximity groups
- Ignore responsive spacing

**References**
- [Interaction Design Foundation: Gestalt Principles](https://www.interaction-design.org/literature/topics/gestalt-principles)
- [UX Tigers: Gestalt for UI Design](https://www.uxtigers.com/post/gestalt-ui)

---
## Gestalt Prägnanz
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy

Brain simplifies complex forms to simplest, most stable interpretation.

**Examples**
- Minimalist icon design recognized instantly
- Simple geometric shapes in UI components
- Clean logo recognized quickly
- Simplified data visualization charts

**Do's and Don'ts**

*Do's*
- Use simple, clean shapes
- Avoid unnecessary visual complexity
- Let Prägnanz guide icon design
- Test simple vs complex recognition

*Don'ts*
- Overcomplicate simple concepts
- Use redundant visual details
- Force complex Prägnanz effects
- Ignore cultural Prägnanz differences

**References**
- [GestaltPrinciples.com](https://www.gestaltprinciples.com/)
- [Aela: Gestalt in UX/UI](https://aelaschool.com/en/interactiondesign/gestalt-principles-ux-ui/)

---
## Gestalt Similarity
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy

Similar-looking elements grouped visually regardless of position through shared style/properties.

**Examples**
- All primary buttons styled identically across interface
- Card components with same border/shadow treatment
- Navigation items with matching font weight and color
- List items sharing consistent icon and text formatting

**Do's and Don'ts**

*Do's*
- Style similar buttons identically
- Use consistent card styling
- Apply similarity for navigation items
- Test similarity grouping

*Don'ts*
- Mix styles within same content type
- Use random visual treatments
- Apply similarity to unrelated items
- Ignore similarity in lists

**References**
- [Toptal: Gestalt Principles of Design](https://www.toptal.com/designers/ui/gestalt-principles-of-design)
- [CareerFoundry: Gestalt Explained](https://careerfoundry.com/en/blog/ux-design/gestalt-principles/)

---
## Gestalt Symmetry
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy

Symmetrical elements create balance, order, and visual stability.

**Examples**
- Login form centered with symmetric fields
- Hero section with balanced text/image layout
- Navigation split symmetrically left/right
- Icon pairs mirrored around center line

**Do's and Don'ts**

*Do's*
- Center primary CTAs symmetrically
- Balance layout around center axis
- Use symmetry for login forms
- Apply symmetry consistently

*Don'ts*
- Mix symmetry/asymmetry randomly
- Force symmetry on complex layouts
- Use symmetry for dynamic content
- Ignore symmetry in mobile

**References**
- [FullClarity: Gestalt in UI](https://fullclarity.co.uk/gestalt-principles/)
- [LinkedIn: Gestalt Hierarchy](https://www.linkedin.com/pulse/gestalt-principles-visual-hierarchy/)

---
## Gesture
**Category:** ui | **Type:** pattern | **Tags:** interaction, mobile

Multi-touch input patterns (pinch, swipe, long-press, double-tap).

**Examples**
- Pinch to zoom image
- Swipe to delete list item
- Long-press context menu
- Double-tap like/unlike

**Do's and Don'ts**

*Do's*
- Use familiar gesture patterns
- Provide visual gesture affordance
- Support gesture cancellation
- Test gesture discoverability

*Don'ts*
- Unfamiliar custom gestures
- No visual gesture hints
- Gestures blocking other actions
- Poor gesture precision

**References**
- [NN/g: Touch Gestures](https://www.nngroup.com/articles/touch-gesture-controls/)
- [Human Interface Guidelines: Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures)

---
## Glyph
**Category:** ui | **Type:** concept | **Tags:** typography

Individual character or symbol in a font, including letters, numbers, punctuation, and special symbols. Each glyph is a unique visual unit designed to work within a typeface system.

**Examples**
- Checking if a font includes currency glyphs needed for international use
- Verifying special character availability for multilingual content
- Testing glyph rendering for mathematical symbols
- Ensuring icon fonts have all required glyphs

**Do's and Don'ts**

*Do's*
- Ensure all required glyphs are included in your font selection
- Test glyph rendering for special characters
- Account for missing glyphs in fallback strategies
- Verify glyph consistency across font weights

*Don'ts*
- Assume all glyphs render identically across fonts
- Use custom glyphs without fallbacks
- Ignore glyph availability for multilingual content
- Mix glyphs from different fonts without testing

**References**
- [Tom Chalky: Your Ultimate Typography Glossary](https://tomchalky.com/typography-glossary)
- [Monotype: A Glossary of Typographic Terms](https://www.monotype.com/resources/expertise/typography-terms)

---
## Golden Ratio
**Category:** ui | **Type:** principle

1:1.618 proportion creates natural visual harmony.

**Examples**
- Sidebar:content = 1:1.618
- Typography scale perfect fourths
- Card height:width ratio
- Image crop golden rectangle

**Do's and Don'ts**

*Do's*
- Fibonacci spacing sequence
- Type scale ratios
- Layout proportion harmony
- Test aesthetic balance

*Don'ts*
- Arbitrary pixel dimensions
- Equal section heights
- Ignore proportion math
- Symmetrical everything

**References**
- [Canva: Golden Ratio](https://www.canva.com/learn/golden-ratio/)
- [Smashing Magazine](https://www.smashingmagazine.com/)

---
## Grid Alignment
**Category:** ui | **Type:** tool | **Tags:** visual-hierarchy

Grid positioning creating visual flow, rhythm, and consistent relationships.

**Examples**
- 8pt grid system for component spacing
- Baseline grid aligning text vertically
- Column layout with consistent gutters
- Responsive grid scaling from 12 to 4 columns

**Do's and Don'ts**

*Do's*
- 8pt/12pt grid systems
- Baseline text alignment
- Consistent column gutters
- Responsive grid scaling

*Don'ts*
- Mix alignment methods
- Eyeball alignment
- Inconsistent grid systems
- Break grid for decoration

**References**
- [Figma: Visual Hierarchy Tips](https://www.figma.com/resource-library/visual-hierarchy/)
- [NN/g: Visual Design](https://www.nngroup.com/articles/visual-design/)

---
## Guerrilla Testing
**Category:** ux | **Type:** methodology | **Tags:** testing, research

Quick informal tests recruiting anyone available nearby.

**Examples**
- Coffee shop 8 testers
- 15min checkout tasks
- Smartphone prototype testing
- Immediate feedback loop

**Do's and Don'ts**

*Do's*
- Specific target users
- Clear success metrics
- Record quick notes
- Thank + incentivize

*Don'ts*
- Wrong target audience
- Vague testing goals
- No note-taking system
- Test non-representative

**References**
- [NN/g: Guerrilla Testing](https://www.nngroup.com/articles/guerrilla-testing/)
- [UX Myth](https://uxmyth.com/)

---
## Hamburger Menu
**Category:** ui | **Type:** pattern | **Tags:** navigation, mobile

Three-line icon expanding to reveal navigation drawer/menu (≡).

**Examples**
- Mobile top-right hamburger revealing sidebar
- Desktop collapsed navigation
- App drawer access
- Multi-level menu expansion

**Do's and Don'ts**

*Do's*
- Use recognizable icon (≡)
- Smooth drawer animation
- Clear close gesture
- Prioritize frequent destinations

*Don'ts*
- Hide primary navigation only
- Poor discoverability
- No visual hierarchy in menu
- Confusing close gestures

**References**
- [UXPin: Navigation Patterns](https://www.uxpin.com/studio/blog/hamburger-menu-alternatives/)
- [NN/g: Hamburger Menus](https://www.nngroup.com/articles/hamburger-menus/)

---
## Haptic Feedback Types
**Category:** ui | **Type:** pattern | **Tags:** mobile, interaction

Distinct vibration patterns for different interactions.

**Examples**
- Light tap success
- Medium warning vibration
- Heavy error feedback
- Success tick pattern

**Do's and Don'ts**

*Do's*
- Match haptic to meaning
- Platform-standard patterns
- Accessibility toggle
- Battery optimization

*Don'ts*
- Random vibration strength
- Always maximum intensity
- No haptic variety
- Desktop-only feedback

**References**
- [Apple: UIFeedbackGenerator](https://developer.apple.com/documentation/uifeedbackgenerator)
- [Android Developer](https://developer.android.com/)

---
## Heatmap Analysis
**Category:** ux | **Type:** tool | **Tags:** research, analytics

Visual representation of user click scroll attention patterns.

**Examples**
- Click heatmap dashboard
- Scroll depth revenue page
- Attention heatmap hero
- Mobile gesture heatmap

**Do's and Don'ts**

*Do's*
- Multiple heatmap types
- Segment by user type
- Compare time periods
- Overlay session recordings

*Don'ts*
- Single heatmap type
- All pages equal priority
- No behavioral context
- Desktop-only analysis

**References**
- [NN/g: Heatmaps](https://www.nngroup.com/articles/heatmap-visualizations-signifiers/)

---
## Heuristic Evaluation
**Category:** ux | **Type:** methodology | **Tags:** testing, principles

An expert review method where evaluators examine an interface against established usability principles (heuristics) to identify usability problems. Heuristic evaluation is quick, inexpensive, and effective for finding issues without involving users.

**Examples**
- Reviewing a website against Nielsen's 10 usability heuristics to identify violations
- Having 3-5 UX experts independently evaluate an app and consolidate their findings

**Do's and Don'ts**

*Do's*
- Use established heuristic sets (Nielsen's 10, etc.)
- Have 3-5 evaluators work independently
- Document severity ratings for each issue
- Consolidate findings from multiple evaluators
- Follow up with usability testing
- Focus on issues that violate clear principles

*Don'ts*
- Rely only on heuristic evaluation
- Have evaluators work together initially
- Skip severity ratings
- Use only one evaluator
- Ignore domain-specific heuristics
- Let personal preferences override heuristics

**References**
- [Nielsen Norman Group: 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [Nielsen Norman Group: How to Conduct Heuristic Evaluation](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/)

---
## Hick's Law
**Category:** ux | **Type:** principle

Decision time increases logarithmically with number of choices.

**Examples**
- 3 primary navigation options
- 2 button sizes (primary/secondary)
- Single checkout CTA per step
- 4 filter categories maximum

**Do's and Don'ts**

*Do's*
- Limit choices to 3-5 max
- Progressive disclosure options
- Context-specific choice sets
- Prioritize most likely options

*Don'ts*
- 12+ menu items
- All options visible always
- Equal visual weight choices
- No defaults/preselection

**References**
- [NN/g: Hick's Law](https://www.nngroup.com/articles/hicks-law/)
- [Laws of UX: Hick's Law](https://lawsofux.com/hicks-law/)

---
## Hiring Rubric
**Category:** management | **Type:** tool | **Tags:** processes

Structured evaluation criteria scoring system.

**Examples**
- Senior Designer: 4 skills 1-5
- Team fit behavioral
- Portfolio review rubric
- Interview scoring sheet

**Do's and Don'ts**

*Do's*
- Objective criteria first
- Multiple interviewers
- Calibration discussion
- Documentation required

*Don'ts*
- Gut feel hiring
- Single interviewer
- Subjective scoring
- No documentation

**References**
- [Hiring Things](https://www.hiringthings.com/)
- [Lever](https://lever.co/)

---
## Hover State
**Category:** ui | **Type:** pattern | **Tags:** interaction

Visual change on mouse-over indicating interactivity and suggesting further action.

**Examples**
- Button subtle lift/glow on hover
- Link underline/color change
- Menu item background highlight
- Tooltip preview on hover

**Do's and Don'ts**

*Do's*
- Use subtle hover effects
- Indicate actionable next step
- Maintain spatial relationships
- Test hover across devices

*Don'ts*
- Distracting hover animations
- Hover effects on non-interactive
- Slow hover transitions
- Mobile-only hover states

**References**
- [CSS-Tricks: Hover Effects](https://css-tricks.com/css-link-hover-effects/)
- [NN/g: Hover State Guidelines](https://www.nngroup.com/articles/timing-exposing-content/)

---
## How Might We
**Category:** strategy | **Type:** methodology | **Tags:** ideation

A question format that reframes problems as opportunities for ideation by using "How might we..." to open possibilities. HMW questions turn insights and challenges into actionable springboards for generating solutions.

**Examples**
- Reframing "Users abandon cart" into "How might we give users confidence during checkout?"
- Converting "Feature is hard to find" into "How might we make key features more discoverable?"

**Do's and Don'ts**

*Do's*
- Start with user insights or problem statements
- Make questions broad enough to allow solutions
- Keep questions specific enough to be actionable
- Generate multiple HMW questions per problem
- Use HMW questions to launch brainstorming
- Frame questions positively as opportunities

*Don'ts*
- Create questions that are too broad or vague
- Suggest solutions within the question
- Frame questions negatively
- Stop at one HMW question per problem
- Use HMW without prior research or insights
- Let HMW questions replace problem definition

**References**
- [Stanford d.school: How Might We Questions](https://dschool.stanford.edu/resources/how-might-we-questions)
- [Interaction Design Foundation: HMW Questions](https://www.interaction-design.org/literature/article/define-and-frame-your-design-challenge-by-creating-your-point-of-view-and-ask-how-might-we)

---
## Hub-and-Spoke Structure
**Category:** ux | **Type:** pattern | **Tags:** information-architecture

Central hub page linking to related content spokes.

**Examples**
- Category page > individual products
- Author profile > their articles
- Topic landing > related posts
- Country page > cities list

**Do's and Don'ts**

*Do's*
- Limit spokes to 12 max
- Hub has unique content
- Consistent spoke templates
- Breadcrumb navigation

*Don'ts*
- Hub with no content
- More than 20 spokes
- Inconsistent spoke depth
- No hub-spoke labeling

**References**
- [Patternry](https://patternry.com/)
- [Luke Wroblewski](https://lukew.com/)

---
## Hundred Ideas Exercise
**Category:** ux | **Type:** tool | **Tags:** ideation

Generate 100 ideas rapidly to push past obvious solutions.

**Examples**
- 100 app feature ideas
- 100 homepage layouts
- 100 button labels
- 30-minute time limit

**Do's and Don'ts**

*Do's*
- Quantity over quality
- No self-editing
- Time pressure
- Build on previous ideas

*Don'ts*
- Stop at 20 ideas
- Judge during generation
- Overthink each idea
- Skip wild concepts

**References**
- [IDEO: Brainstorming](https://www.ideo.com/)
- [Stanford d.school](https://dschool.stanford.edu/)

---
## Icon Baseline Alignment
**Category:** ui | **Type:** principle | **Tags:** iconography

Icons aligned to text baseline for visual rhythm and consistency, ensuring proper vertical alignment with accompanying text.

**Examples**
- Icon aligned to text baseline in navigation items
- Form input icon vertically centered with text
- Menu items with consistent icon-text spacing
- Button icons aligned to button text baseline

**Do's and Don'ts**

*Do's*
- Align icons to text baseline
- Maintain consistent icon-text spacing
- Test alignment across sizes
- Document alignment rules

*Don'ts*
- Vertically center icons with text
- Use inconsistent alignment
- Ignore baseline in different contexts
- Skip alignment in responsive design

**References**
- [NN/g: Icon-Text Alignment](https://www.nngroup.com/articles/icon-usability/)
- [Figma: Icon Baseline Guidelines](https://www.figma.com/best-practices/icon-design/)

---
## Icon Family
**Category:** ui | **Type:** tool | **Tags:** iconography, design-systems

Icons sharing visual DNA across multiple weights, sizes, and styles (e.g., light, regular, bold) maintaining recognition and consistency.

**Examples**
- SF Symbols family with 9 weights
- Material Icons family (light, regular, bold)
- Heroicons family (solid, outline variants)
- Custom icon family with 3 weight variations

**Do's and Don'ts**

*Do's*
- Create families with multiple weights
- Maintain character consistency across variants
- Document family structure
- Scale families systematically

*Don'ts*
- Create inconsistent variants
- Skip weight variations
- Mix unrelated icons in family
- Ignore scaling relationships

**References**
- [SF Symbols: Apple Icon Family](https://developer.apple.com/sf-symbols/)
- [Material Design: Icon Families](https://m3.material.io/styles/icons/overview)

---
## Icon Grid
**Category:** ui | **Type:** tool | **Tags:** iconography

Invisible structure (typically 24x24 or 32x32px) ensuring proportional consistency and alignment across all icons in a set.

**Examples**
- 24x24px grid with 2px padding for all icons
- 32x32px grid with 4px internal margin
- Optical adjustments within consistent grid
- Grid guides ensuring left/right alignment

**Do's and Don'ts**

*Do's*
- Establish consistent grid dimensions
- Include padding/margin within grid
- Document grid specifications
- Apply optical adjustments within grid

*Don'ts*
- Ignore grid consistency
- Use different grids per icon
- Force content outside grid
- Forget optical adjustments

**References**
- [Figma: Icon Grid System](https://www.figma.com/best-practices/icon-design/)
- [Design Systems Guide: Icon Grids](https://designsystems.com/iconography/)

---
## Icon Library
**Category:** ui | **Type:** tool | **Tags:** iconography, design-systems

Curated collection of icons following consistent design system rules, style, weight, and grid specifications for organizational reuse.

**Examples**
- Figma icon component library with variants
- Icon font file (SVG/EOT/TTF) with 500+ icons
- Versioned icon package (v1.0, v2.0)
- Organized by category (navigation, social, actions, status)

**Do's and Don'ts**

*Do's*
- Organize icons by category
- Version library updates
- Document icon naming conventions
- Test library across applications

*Don'ts*
- Mix uncurated icons
- Skip documentation
- Break naming consistency
- Ignore library maintenance

**References**
- [Design Systems Collective: Icon Libraries](https://designsystems.com/iconography/)
- [Ant Design: Icon System](https://ant.design/components/icon/)

---
## Icon Scale
**Category:** ui | **Type:** tool | **Tags:** iconography, design-systems

Relative sizing system for icons across UI contexts (16px, 24px, 32px, etc.). Icon scale ensures proportional sizing and maintains visual consistency.

**Examples**
- 16px icons for inline text/comments
- 24px icons for navigation and toolbars
- 32px icons for cards and component headers
- 48px icons for hero sections and CTAs

**Do's and Don'ts**

*Do's*
- Use 8px-based scale (8, 16, 24, 32, 48)
- Document scale in design system
- Scale responsively for mobile/desktop
- Test readability at each scale

*Don'ts*
- Use arbitrary icon sizes
- Skip intermediate sizes
- Ignore scale context
- Use same size across all contexts

**References**
- [Material Design 3: Icon System](https://m3.material.io/styles/icons/overview)
- [Design Tokens Guide: Icon Sizing](https://designtokens.org/)

---
## Icon Set
**Category:** ui | **Type:** principle | **Tags:** iconography

Complete group of icons sharing identical style, weight, grid, and visual characteristics for cohesive interface communication.

**Examples**
- 50-icon set for e-commerce interface
- Navigation icon set with 8 consistent icons
- Status icon set (success, error, warning, info)
- Action icon set (edit, delete, share, download)

**Do's and Don'ts**

*Do's*
- Create complete sets for features
- Maintain visual consistency
- Document set coverage
- Test set completeness

*Don'ts*
- Mix sets from different libraries
- Incomplete icon coverage
- Ignore visual coherence
- Skip documentation

**References**
- [Material Design Icons: Complete Set](https://fonts.google.com/icons)
- [Feather Icons: Minimal Icon Set](https://feathericons.com/)

---
## Icon Style
**Category:** ui | **Type:** principle | **Tags:** iconography

Consistent visual language applied to all icons (flat, skeuomorphic, outline, duotone, glyph). Icon style establishes design system coherence and aids user recognition across interface.

**Examples**
- Outline style with uniform 2px stroke weight
- Filled icons with solid color backgrounds
- Duotone icons using two complementary colors
- Glyph style icons from icon font families (Font Awesome, Material Icons)

**Do's and Don'ts**

*Do's*
- Establish one primary icon style per system
- Document style guidelines in design system
- Apply style consistently across all icon sizes
- Test style recognition across devices

*Don'ts*
- Mix multiple incompatible styles
- Change style for decorative purposes
- Use inconsistent style in similar contexts
- Ignore style in responsive design

**References**
- [Interaction Design Foundation: Icon Design Principles](https://www.interaction-design.org/literature/article/icon-design-principles)
- [Smashing Magazine: Icon Systems Guide](https://www.smashingmagazine.com/2021/04/designing-better-icons/)

---
## Icon Weight
**Category:** ui | **Type:** principle | **Tags:** iconography

Thickness of strokes or boldness of filled shapes in icons. Icon weight creates visual hierarchy and differentiates icon importance within interface.

**Examples**
- Light weight (1px) for subtle background icons
- Regular weight (2px) for primary actions
- Bold weight (3px) for emphasis and focal points
- Ultra-bold for icon badges or warnings

**Do's and Don'ts**

*Do's*
- Use weight progression for hierarchy
- Maintain consistent weight ratio across set
- Scale weight proportionally with icon size
- Test weight visibility at small sizes

*Don'ts*
- Mix weights randomly
- Use extreme weights for standard icons
- Ignore weight-size relationship
- Change weight inconsistently

**References**
- [Design Systems Collective: Icon Weights](https://designsystems.com/iconography/)
- [Figma: Icon Design Best Practices](https://www.figma.com/best-practices/icon-design/)

---
## Ideation Workshop
**Category:** strategy | **Type:** methodology | **Tags:** strategy, ideation

Structured creative problem solving session.

**Examples**
- Crazy 8s + dot voting
- 2hr cross-functional
- 50+ ideas generated
- Top 3 prioritized

**Do's and Don'ts**

*Do's*
- Diverse participants
- Structured methods
- Quantity over quality
- Clear prioritization

*Don'ts*
- Homogeneous group
- Open-ended discussion
- Criticism during generation
- No decision method

**References**
- [SessionLab: Ideation Workshop](https://www.sessionlab.com/methods/ideation-workshop)
- [Mural](https://mural.co/)

---
## Infinite Scroll Pagination
**Category:** ui | **Type:** pattern | **Tags:** web

Content loads continuously without page refresh.

**Examples**
- Social media feed
- Ecommerce product grid
- Image gallery pagination
- Loading indicator at bottom

**Do's and Don'ts**

*Do's*
- Clear loading states
- Manual load more option
- URL state preservation
- Performance throttling

*Don'ts*
- No end state
- Poor mobile performance
- Deep linking broken
- No skeleton screens

**References**
- [Infinite Scroll](https://infinite-scroll.com/)
- [Brad Frost](https://bradfrost.com/)

---
## Information Architecture
**Category:** ux | **Type:** methodology | **Tags:** information-architecture, strategy

Organization and labeling of content so users can find and understand what they need.

**Examples**
- E-commerce category structure
- Dashboard content grouping
- Documentation table of contents
- App settings organization

**Do's and Don'ts**

*Do's*
- Test with real users
- Plan for future growth
- Balance depth and breadth
- Use consistent labeling

*Don'ts*
- Copy competitor structure
- Optimize for search engines only
- Create more than 3 clicks deep
- Ignore mental models

**References**
- [NN/g: Information Architecture](https://www.nngroup.com/articles/information-architecture/)
- [Information Architecture Institute](https://informationarchitecture.org/)

---
## Information Hierarchy
**Category:** ux | **Type:** principle | **Tags:** information-architecture, visual-hierarchy

Levels of content importance and relationships.

**Examples**
- H1 primary task > H2 sections > body
- Hero banner > featured > supporting
- Priority 1 alerts > nav > content
- Product: image > title > price > desc

**Do's and Don'ts**

*Do's*
- Follow F-pattern reading
- Limit 3 levels max
- Use size + position
- Test scan patterns

*Don'ts*
- Equal visual weight
- More than 4 levels
- Bottom-up hierarchy
- Text-only signaling

**References**
- [NN/g Articles](https://nngroup.com/articles/)
- [UX Movement](https://uxmovement.com/)

---
## Interaction
**Category:** ui | **Type:** concept | **Tags:** interaction

User input triggering system response (click, tap, hover, drag, swipe).

**Examples**
- Button click submitting form
- Slider drag adjusting value
- Menu hover revealing submenu
- Swipe gesture navigating cards

**Do's and Don'ts**

*Do's*
- Design clear interaction targets
- Test interactions across devices
- Provide immediate feedback
- Support multiple input methods

*Don'ts*
- Make targets too small
- Lack visual feedback
- Ignore touch vs mouse differences
- Skip keyboard support

**References**
- [NN/g: Interaction Design Principles](https://www.nngroup.com/articles/interaction-design-principles/)
- [Material Design: Motion & Interaction](https://m3.material.io/styles/motion/overview)

---
## Interaction Cost
**Category:** ux | **Type:** concept | **Tags:** interaction, testing

Cognitive physical effort required per action.

**Examples**
- 3-click vs 1-click checkout
- Gesture vs button complexity
- Form field cognitive load
- Gesture learnability curve

**Do's and Don'ts**

*Do's*
- Minimize steps actions
- Familiar gestures first
- Progressive disclosure
- User testing validation

*Don'ts*
- Complex novel gestures
- High cognitive load forms
- Unclear interaction goals
- No learnability testing

**References**
- [NN/g: Interaction Cost](https://www.nngroup.com/articles/interaction-cost/)
- [Laws of UX](https://lawsofux.com/)

---
## Interaction Feedback
**Category:** ui | **Type:** principle | **Tags:** interaction

System response confirming user action was received (animation, color change, sound).

**Examples**
- Button color change on click
- Loading spinner on form submit
- Success animation after save
- Error shake on invalid input

**Do's and Don'ts**

*Do's*
- Provide immediate feedback
- Use appropriate feedback type
- Match feedback to action severity
- Test feedback timing

*Don'ts*
- Delay feedback >100ms
- Use identical feedback for all actions
- Over-animate feedback
- Ignore accessibility feedback

**References**
- [NN/g: Feedback Loops](https://www.nngroup.com/articles/feedback-loops/)
- [UX Movement: Interaction Feedback](https://uxmovement.com/)

---
## iOS Human Interface
**Category:** ui | **Type:** pattern | **Tags:** mobile

Apple design guidelines conventions.

**Examples**
- SF Symbols iconography
- Navigation bar + toolbar
- Modal presentation sheets
- Tab bar + sidebar

**Do's and Don'ts**

*Do's*
- Follow HIG conventions
- SF Pro typography
- Standard navigation patterns
- iOS gesture support

*Don'ts*
- Android Material patterns
- Custom navigation flows
- Third-party iconography
- Desktop window patterns

**References**
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Apple Developer](https://developer.apple.com/)

---
## ISO 9241-171
**Category:** ui | **Type:** framework | **Tags:** accessibility

Ergonomics guidance on software accessibility and human-system interaction.

**Examples**
- ISO 9241-171:2025 (latest)
- Software accessibility principles
- Beyond web - all digital products
- International standardization

**Do's and Don'ts**

*Do's*
- Use ISO 9241 principles universally
- Apply to native apps + software
- Combine with WCAG for web
- Enterprise compliance standard

*Don'ts*
- Apply only to websites
- Ignore ISO ergonomics principles
- Skip non-web applications
- Assume WCAG substitutes

**References**
- [ISO: 9241-171:2025](https://www.iso.org/standard/85169.html)
- [Chet Tailor: ISO 9241 Guide](https://www.iso.org/standard/85169.html)

---
## Jobs-to-be-Done
**Category:** strategy | **Type:** framework | **Tags:** strategy, research

User hires products for progress in life.

**Examples**
- 'Milkshake job': Keep me entertained
- Switch interview questions
- Progress-focused not demographics
- Job stories mapping

**Do's and Don'ts**

*Do's*
- Focus on progress sought
- Switch context questions
- Job map 8 stages
- Cross-job comparison

*Don'ts*
- Demographics segmentation
- Feature-focused interviews
- Current solution bias
- Static job statements

**References**
- [JTBD.info](https://jtbd.info/)
- [Jobs to Stories](https://jobs-to-stories.com/)

---
## Journey Mapping
**Category:** ux | **Type:** methodology | **Tags:** research

A visualization of the process a user goes through to accomplish a goal, showing their actions, thoughts, emotions, and pain points across touchpoints over time. Journey maps synthesize research data to create a shared understanding of user experience and identify improvement opportunities.

**Examples**
- Mapping a patient's journey through a healthcare system from symptom discovery to post-treatment follow-up
- Documenting a customer's experience buying a product, from initial awareness through purchase and support
- Visualizing an employee's onboarding journey to identify friction points in the first 90 days
- Creating a map of a traveler's airport experience to uncover service design opportunities

**Do's and Don'ts**

*Do's*
- Base maps on actual research data, not assumptions
- Include emotional journey alongside actions and touchpoints
- Identify pain points and opportunities clearly
- Create maps collaboratively with cross-functional teams
- Focus on a specific persona and specific goal
- Use maps to drive actionable improvements, not just documentation

*Don'ts*
- Create journey maps without user research
- Make maps too complex or detailed to be useful
- Map every possible path (focus on primary scenarios)
- Forget to include backstage processes that affect user experience
- Create a journey map and then never reference it again
- Confuse journey maps with service blueprints or user flows

**References**
- [Nielsen Norman Group: Journey Mapping 101](https://www.nngroup.com/articles/journey-mapping-101/)
- [Nielsen Norman Group: When and How to Create Customer Journey Maps](https://www.nngroup.com/articles/customer-journey-mapping/)
- [Adaptive Path: Guide to Experience Mapping](https://adaptivepath.org/ideas/the-anatomy-of-an-experience-map/)

---
## Kano Model
**Category:** strategy | **Type:** framework | **Tags:** strategy

A prioritization framework that categorizes features based on their relationship to customer satisfaction. The Kano Model classifies features as Basic Needs, Performance Needs, or Delighters to help teams understand which features create the most value.

**Examples**
- Identifying that fast loading is a Basic Need (expected) while personalized recommendations are Delighters (exceed expectations)
- Using Kano surveys to determine which proposed features will most increase satisfaction

**Do's and Don'ts**

*Do's*
- Survey customers to classify features
- Understand that feature categories change over time
- Focus on Delighters for differentiation
- Ensure all Basic Needs are met first
- Use Kano with other prioritization methods
- Re-evaluate feature categories periodically

*Don'ts*
- Ignore Basic Needs in favor of Delighters
- Assume feature categories are permanent
- Over-invest in Performance features alone
- Skip customer research in classification
- Use Kano for internal features or technical work
- Forget that competitors' Delighters become your Basic Needs

**References**
- [Folding Burritos: Kano Model](https://foldingburritos.com/product-prioritization-techniques/)
- [ProductPlan: Kano Model Guide](https://www.productplan.com/glossary/kano-model/)

---
## Keyboard Navigation
**Category:** ui | **Type:** pattern | **Tags:** interaction, accessibility

Tab order and key actions enabling non-mouse interface control.

**Examples**
- Tab through form fields
- Arrow keys in menus
- Enter to activate buttons
- Escape to close modals

**Do's and Don'ts**

*Do's*
- Logical tab order
- Clear focus indicators
- Keyboard shortcuts
- Skip repetitive navigation

*Don'ts*
- No keyboard support
- Confusing tab order
- Hidden focus states
- Trap keyboard focus

**References**
- [WebAIM: Keyboard Accessibility](https://webaim.org/techniques/keyboard/)
- [WCAG 2.1: Keyboard Accessible](https://www.w3.org/WAI/WCAG21/Understanding/keyboard.html)

---
## Keyboard Trap Detection
**Category:** ux | **Type:** methodology | **Tags:** accessibility, testing

Focus becomes stuck unable to tab forward/back.

**Examples**
- Modal dialog trap
- Carousel keyboard trap
- Custom dropdown trap
- Focus management bug

**Do's and Don'ts**

*Do's*
- Tab through entire flow
- Shift+Tab backward
- Escape key handling
- Visual focus indicator

*Don'ts*
- Mouse-only testing
- Skip custom components
- No visual focus
- Complex keyboard paths

**References**
- [WebAIM: Keyboard](https://webaim.org/techniques/keyboard/)
- [TPGi](https://www.tpgi.com/)

---
## KPI Performance Tracker
**Category:** strategy | **Type:** methodology | **Tags:** data-visualization, analytics

Charts designed specifically for business goal metrics and thresholds.

**Examples**
- Conversion rate vs target
- Customer acquisition cost
- Monthly recurring revenue
- Churn rate benchmark

**Do's and Don'ts**

*Do's*
- Business goal alignment
- Target/baseline reference
- Trend + current + goal
- Alert threshold bands

*Don'ts*
- Operational metrics only
- No business context
- Vanity metrics focus
- Missing targets

**References**
- [Klipfolio: KPI Examples](https://www.klipfolio.com/resources/kpi-examples)
- [Databox](https://databox.com/)

---
## Lab Usability Testing
**Category:** ux | **Type:** methodology | **Tags:** testing, research

Controlled environment with eye-tracking specialized equipment.

**Examples**
- Tobii eye tracker + 7 users
- One-way mirror observation
- Biometric response capture
- Controlled lighting conditions

**Do's and Don'ts**

*Do's*
- Calibrated equipment first
- Single participant at time
- Quiet controlled environment
- Professional moderation

*Don'ts*
- Skip equipment calibration
- Group testing sessions
- Distracting environment
- Inexperienced moderation

**References**
- [iMotions](https://imotions.com/)
- [Tobii](https://www.tobii.com/)

---
## Labeling System
**Category:** ux | **Type:** pattern | **Tags:** information-architecture

Rules for naming navigation items, categories, and content.

**Examples**
- User preference > Settings > Privacy
- Shop > Categories > Electronics > Phones
- Help > Articles > Payments
- Dashboard > Reports > Analytics

**Do's and Don'ts**

*Do's*
- Use familiar user language
- Keep labels under 12 chars
- Test with 5 users minimum
- Document conventions

*Don'ts*
- Internal jargon
- Long descriptive phrases
- Inconsistent capitalization
- Acronyms without expansion

**References**
- [Semantic Studios](https://semanticstudios.com/)
- [UX Design CC](https://uxdesign.cc/)

---
## Landing Page Test
**Category:** ux | **Type:** methodology | **Tags:** testing

A lean validation method that uses a simple web page to gauge market interest in a product or feature before building it. Landing page tests measure conversion rates to assess demand and collect leads from interested users.

**Examples**
- Creating a landing page describing a planned feature with a "Sign up for early access" button to measure interest
- Building a page for a product concept and running ads to test market demand

**Do's and Don'ts**

*Do's*
- Clearly describe the value proposition
- Include a clear call-to-action to measure intent
- Drive qualified traffic to the page
- Measure both interest and behavioral signals
- Be transparent about product status
- Follow up with interested users

*Don'ts*
- Mislead users about product availability
- Test without driving meaningful traffic
- Only measure clicks without understanding why
- Create overly complex landing pages
- Ignore qualitative feedback from visitors
- Promise features you can't deliver

**References**
- [Lean Startup: Validation Techniques](https://theleanstartup.com/)
- [GV: Validate Your Idea with a Landing Page](https://library.gv.com/how-to-validate-your-idea-with-a-landing-page-59cf47d1e341)

---
## Lazy Image Loading
**Category:** ui | **Type:** pattern | **Tags:** web, analytics

Images load only when scrolled into viewport.

**Examples**
- loading=lazy native attribute
- IntersectionObserver API
- Fade-in placeholder animation
- Priority hints for above-fold

**Do's and Don'ts**

*Do's*
- Native loading=lazy first
- Critical images eager
- Smooth placeholder fade
- Network prioritization

*Don'ts*
- Lazy ALL images
- No above-fold optimization
- Jarring layout shifts
- No priority hints

**References**
- [Web.dev: Lazy Loading](https://web.dev/lazy-loading/)
- [MDN](https://developer.mozilla.org/en-US/)

---
## Lean Canvas
**Category:** strategy | **Type:** tool | **Tags:** strategy

One-page business model visualization.

**Examples**
- Problem Top 3 customer pains
- Solution Top 3 features
- Key Metrics 3-5 success measures
- 20min team workshop

**Do's and Don'ts**

*Do's*
- Cross-functional team
- Customer validation focus
- Weekly canvas refresh
- Actionable next steps

*Don'ts*
- Solo canvas creation
- Feature-first focus
- Never updated
- Marketing plan only

**References**
- [Lean Stack: Lean Canvas](https://leanstack.com/leancanvas)
- [Strategyzer](https://www.strategyzer.com/)

---
## Lean UX Hypothesis
**Category:** strategy | **Type:** tool | **Tags:** strategy

We believe this will result in outcome we'll know success.

**Examples**
- We believe shorter checkout → +15% conversion
- Per target user behavior
- 2-week experiment
- Success: 12% lift

**Do's and Don'ts**

*Do's*
- Specific measurable outcome
- Target user segment
- Timebox experiment
- Clear success criteria

*Don'ts*
- Vague qualitative hypothesis
- No target users
- Unlimited experiment time
- Multiple success metrics

**References**
- [Lean UX: Hypothesis Template](https://leanux.org/lean-ux-hypothesis-template/)
- [Design Better](https://www.designbetter.co/)

---
## Learnability
**Category:** ux | **Type:** principle

How quickly new users understand interface.

**Examples**
- 30-second task completion
- Intuitive icon meanings
- Consistent pattern language
- Onboarding walkthroughs

**Do's and Don'ts**

*Do's*
- First-time user testing
- Familiar mental models
- Progressive disclosure
- Contextual help inline

*Don'ts*
- Zero onboarding docs
- Novel interaction paradigms
- Complex first screens
- No pattern consistency

**References**
- [NN/g: Usability 101](https://www.nngroup.com/articles/usability-101/)
- [Interaction Design Foundation](https://www.interaction-design.org/)

---
## Legend Color Picker
**Category:** ui | **Type:** pattern | **Tags:** data-visualization, interaction

Interactive legend toggles series visibility and shows values.

**Examples**
- Toggle product lines on/off
- Show/hide data series
- Color picker for custom
- Values displayed in legend

**Do's and Don'ts**

*Do's*
- Dual purpose (toggle+info)
- Click visual feedback
- Keyboard focus support
- Drag to reorder series

*Don'ts*
- Static legend only
- Click without feedback
- Hidden on mobile
- Too many items

**References**
- [Highcharts: Legend](https://www.highcharts.com/docs/chart-concepts/legend)
- [Plotly](https://plotly.com/)

---
## Ligature
**Category:** ui | **Type:** tool | **Tags:** typography

Special glyph that combines two or more characters into a single unified form for improved visual flow and appearance (e.g., 'fi', 'fl', 'ffi'). Ligatures enhance readability and aesthetics in typography.

**Examples**
- Enabling 'fi' and 'fl' ligatures in headline text
- Using discretionary ligatures for decorative branding elements
- Disabling ligatures in code editors for character clarity
- Testing ligature rendering across different browsers

**Do's and Don'ts**

*Do's*
- Enable ligatures in display and heading text
- Use standard ligatures (fi, fl, ff, ffi, ffl)
- Disable ligatures in code or technical contexts
- Test ligature rendering across browsers

*Don'ts*
- Force ligatures in body text at small sizes
- Use discretionary ligatures in UI body copy
- Enable ligatures where they break legibility
- Ignore ligature support in fallback fonts

**References**
- [Canva: A Beautifully Illustrated Glossary of Typographic Terms](https://www.canva.com/learn/typography-terms/)
- [Tom Chalky: Your Ultimate Typography Glossary](https://tomchalky.com/typography-glossary)

---
## Line Graph
**Category:** ui | **Type:** tool | **Tags:** data-visualization

Connected points show trends and changes over continuous time periods.

**Examples**
- Stock price over 12 months
- Website visits week-over-week
- Temperature throughout the day
- Revenue growth quarterly

**Do's and Don'ts**

*Do's*
- Smooth curves for trends
- Multiple lines max 4-5
- Clear time intervals
- Consistent y-axis scaling

*Don'ts*
- Area fills unless cumulative
- Disconnected points
- Irregular time intervals
- Too many data series

**References**
- [Chart.js: Line Charts](https://www.chartjs.org/docs/latest/charts/line.html)
- [D3 Graph Gallery](https://d3-graph-gallery.com/)

---
## Line Length
**Category:** ui | **Type:** principle | **Tags:** typography

Number of characters per line of text. Optimal line length is 45-75 characters (or 8-12 words), balancing readability with scanning ease. Line length significantly impacts reading speed and comprehension.

**Examples**
- Setting max-width on text containers to achieve 60 characters per line
- Using narrower columns on mobile for comfortable reading
- Adjusting line length responsively between breakpoints
- Testing line length with actual content rather than lorem ipsum

**Do's and Don'ts**

*Do's*
- Target 50-60 characters per line for optimal readability
- Adjust line length responsively for mobile (shorter) and desktop (longer)
- Use adequate line height to support longer line lengths
- Test line length with actual content

*Don'ts*
- Use excessively long lines (>100 characters)
- Use extremely short lines (<30 characters)
- Ignore line length in responsive design
- Use fixed line length across all screen sizes

**References**
- [Smashing Magazine: The Art of Web Typography](https://www.smashingmagazine.com/typography-guidelines-and-references/)
- [GeeksforGeeks: What is Typography in UI Design?](https://www.geeksforgeeks.org/what-is-typography-in-ui-design/)

---
## Linear Flow
**Category:** ux | **Type:** pattern | **Tags:** information-architecture, interaction

Step-by-step sequence where each step has a single next action.

**Examples**
- Wizard checkout process
- Multi-step form completion
- Tutorial screens sequence
- Signup qualification flow

**Do's and Don'ts**

*Do's*
- Clear progress indicator
- Save/resume capability
- Consistent step design
- Preview before final

*Don'ts*
- More than 7 steps total
- No back button
- Irreversible actions
- Tiny next buttons

**References**
- [Smashing Magazine](https://www.smashingmagazine.com/)
- [Baymard Institute](https://baymard.com/)

---
## Loading State
**Category:** ui | **Type:** pattern | **Tags:** interaction

Temporary state during processing or data fetching.

**Examples**
- Spinner replacing button text
- Skeleton screens for content
- Progress bar for file upload
- Dots bouncing for async action

**Do's and Don'ts**

*Do's*
- Match loading duration to action
- Use skeleton screens for content
- Provide estimated completion
- Cancel/escape loading states

*Don'ts*
- Indefinite loading without feedback
- Full page blockers
- Generic loading for all actions
- No loading state context

**References**
- [Skeleton Screens Guide](https://uxdesign.cc/what-you-should-know-about-skeleton-screens-a820c45a571a)
- [NN/g: Loading Patterns](https://www.nngroup.com/articles/progress-indicators/)

---
## Logical Properties
**Category:** ui | **Type:** tool | **Tags:** web

Direction-agnostic CSS (inline-start vs left).

**Examples**
- margin-inline-start: 1rem
- padding-block: 1rem 2rem
- border-inline-end: 1px solid
- RTL/LTR automatic

**Do's and Don'ts**

*Do's*
- Use logical not physical
- Test RTL languages
- Future-proof layouts
- Consistent spacing logic

*Don'ts*
- left/right/top/bottom only
- Hardcoded LTR values
- No RTL testing
- Physical fallbacks

**References**
- [MDN: Logical Properties](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Logical_properties)
- [RTL Styling](https://rtlstyling.com/)

---
## Long Press Context Menu
**Category:** ui | **Type:** pattern | **Tags:** mobile, interaction

Prolonged tap reveals additional options.

**Examples**
- Text selection handles
- Photo preview + share
- Map pin directions
- File preview + actions

**Do's and Don'ts**

*Do's*
- Clear press duration
- Visual press feedback
- Contextual relevance
- Escape to cancel

*Don'ts*
- Instant context menus
- Unrelated menu options
- No visual feedback
- Desktop right-click only

**References**
- [Apple HIG: Context Menus](https://developer.apple.com/design/human-interface-guidelines/context-menus)
- [Material Design](https://m3.material.io/)

---
## Lotus Blossom Diagram
**Category:** ux | **Type:** tool | **Tags:** ideation

Central idea expands into 8 themes each with 8 sub-ideas.

**Examples**
- Core problem center
- 8 solution categories
- 64 specific ideas total
- Visual expansion grid

**Do's and Don'ts**

*Do's*
- Start with clear core
- Force all 64 cells
- Related themes radiate
- Review connections

*Don'ts*
- Vague central idea
- Leave cells empty
- Unrelated themes
- Skip synthesis

**References**
- [Mycoted: Lotus Blossom](https://www.mycoted.com/)
- [Creativity Techniques](https://www.creativityatwork.com/)

---
## Magic Number
**Category:** strategy | **Type:** tool | **Tags:** analytics

Product growth efficiency coefficient expansion.

**Examples**
- Magic number 1.3 growth
- Quarterly growth tracking
- Sales marketing alignment
- Rule of 40 complement

**Do's and Don'ts**

*Do's*
- Track quarterly minimum
- Cross-functional alignment
- >1.0 sustainable growth
- Actionable levers

*Don'ts*
- Monthly calculation
- Siloed team metrics
- Short-term focus
- No cross-functional view

**References**
- [For Entrepreneurs: Magic Number](https://www.forentrepreneurs.com/magic-number/)
- [Ben Horowitz](https://benhorowitz.com/)

---
## Material Design Motion
**Category:** ui | **Type:** pattern | **Tags:** mobile

Google Android animation system.

**Examples**
- Shared element transitions
- FAB speed dial motion
- Card swipe animations
- Ripple touch feedback

**Do's and Don'ts**

*Do's*
- 60fps motion design
- Meaningful transitions
- Standard duration curves
- Accessibility reduces motion

*Don'ts*
- iOS-style animations
- Excessive motion design
- Inconsistent timing
- No reduce motion support

**References**
- [Material Design: Motion](https://m3.material.io/foundations/motion/overview)
- [Material Design 2](https://m2.material.io/)

---
## Mega Menu
**Category:** ui | **Type:** pattern | **Tags:** navigation, web

Large dropdown with categorized sub-navigation and thumbnails.

**Examples**
- E-commerce mega menu (Categories + images)
- Enterprise site mega menu
- News site mega menu with featured content
- Complex site architecture menu

**Do's and Don'ts**

*Do's*
- Visual categorization
- Featured content thumbnails
- Limit to desktop/large screens
- Clear hover/focus states

*Don'ts*
- Mobile mega menus
- Overwhelm with too much content
- Poor categorization
- Slow loading images

**References**
- [Smashing Magazine: Mega Menus](https://www.smashingmagazine.com/2021/01/mega-menu-design-patterns/)
- [UX Movement: Mega Menu Patterns](https://uxmovement.com/navigation/why-mega-menus-work-well/)

---
## Mental Model Mapping
**Category:** ux | **Type:** methodology | **Tags:** research

Document how users conceptualize system structure.

**Examples**
- User task flow diagrams
- Mental model vs system model
- Card sorting validation
- Journey map integration

**Do's and Don'ts**

*Do's*
- Base on user research
- Compare to current IA
- Iterative refinement
- Cross-user segment validation

*Don'ts*
- Designer assumptions only
- Static single version
- No user validation
- Feature-focused mapping

**References**
- [NN/g: Mental Models](https://www.nngroup.com/articles/mental-models/)
- [Adaptive Path](https://adaptivepath.org/)

---
## Micro Trendline
**Category:** ui | **Type:** tool | **Tags:** data-visualization

Tiny inline line chart showing trend next to summary metric.

**Examples**
- 12-week sales trend by number
- Monthly growth sparkline
- 7-day visitor trend
- Quarterly profit microchart

**Do's and Don'ts**

*Do's*
- Consistent y-axis scaling
- Same color as metric
- Hover for exact values
- Right-aligned in tables

*Don'ts*
- Individual y-axis scales
- Too much white space
- Missing context trend
- Decorative styling

**References**
- [Sparkline Charts](https://www.sparklinecharts.com/)
- [Edward Tufte](https://www.edwardtufte.com/)

---
## Micro-interaction
**Category:** ui | **Type:** tool | **Tags:** interaction

Small, purposeful animations enhancing feedback and delight.

**Examples**
- Button micro-press animation
- Like button heart bounce
- Toast notification slide-in
- Cart item count increment

**Do's and Don'ts**

*Do's*
- Keep micro-interactions <300ms
- Purposeful feedback only
- Consistent motion language
- Test across performance levels

*Don'ts*
- Distracting micro-interactions
- Overuse on every element
- Slow micro-interactions
- Inconsistent motion

**References**
- [Dan Saffer's Microinteractions](https://microinteractions.com/)
- [UX Collective: Micro-interactions](https://uxdesign.cc/micro-interactions-why-when-and-how-to-use-them-to-boost-the-ux-17094b3baaa0)

---
## Miller's Law
**Category:** ux | **Type:** principle

Average person holds 7±2 items in working memory.

**Examples**
- Navigation: 5 primary items
- Form fields per screen: 7 max
- Chunked phone numbers (123-456-7890)
- 6 tab options maximum

**Do's and Don'ts**

*Do's*
- Chunk information in 3s/7s
- Progressive disclosure lists
- Visual grouping of items
- Familiar patterns (phone format)

*Don'ts*
- Long ungrouped lists
- 15+ navigation items
- Single line addresses
- Complex multi-step forms

**References**
- [NN/g: Magic Number 7](https://www.nngroup.com/articles/magic-number-7/)
- [UX Movement](https://uxmovement.com/)

---
## Mind Mapping
**Category:** strategy | **Type:** methodology | **Tags:** ideation

A visual thinking technique that organizes information hierarchically around a central concept, with related ideas branching outward. Mind mapping helps explore connections between ideas and structure thinking during ideation and problem-solving.

**Examples**
- Creating a mind map of user needs with branches for different need categories and sub-branches for specific requirements
- Mapping out feature ideas organized by user goals

**Do's and Don'ts**

*Do's*
- Start with a clear central concept or question
- Use keywords and short phrases, not sentences
- Add visual elements like colors and icons
- Let ideas branch naturally and non-linearly
- Create connections between different branches
- Use digital or physical tools based on context

*Don'ts*
- Make the map too complex or detailed
- Organize linearly like an outline
- Overthink the structure during creation
- Use only text without visual hierarchy
- Create mind maps alone when collaboration would help
- Forget to synthesize insights after mapping

**References**
- [MindMeister: Mind Mapping Guide](https://www.mindmeister.com/mind-map)
- [Interaction Design Foundation: Mind Mapping](https://www.interaction-design.org/literature/article/introduction-to-the-essential-ideation-techniques-which-are-the-heart-of-design-thinking)

---
## Minimal Data Noise
**Category:** ui | **Type:** principle | **Tags:** data-visualization

Removing all non-essential visual elements maximizes data clarity.

**Examples**
- Thin borders only
- Minimal grid lines
- Direct data labels
- Single font weight

**Do's and Don'ts**

*Do's*
- Eliminate 3D effects
- Remove decorative images
- Simplify color palette
- Consistent stroke weights

*Don'ts*
- Background patterns
- Drop shadows
- Heavy grid lines
- Multiple textures

**References**
- [Edward Tufte: The Visual Display of Quantitative Information](https://www.edwardtufte.com/tufte/books_vdqi)
- [Information is Beautiful](https://informationisbeautiful.net/)

---
## Monadic Testing
**Category:** ux | **Type:** methodology | **Tags:** testing

A research approach where each participant evaluates only one design or concept in isolation, without comparison to alternatives. Monadic testing provides unbiased feedback on each option's absolute merits without comparative context influencing responses.

**Examples**
- Testing a new feature design where half of participants see version A only and half see version B only
- Evaluating product concepts by showing each participant just one concept to get clean reactions

**Do's and Don'ts**

*Do's*
- Use when you need unbiased absolute evaluations
- Recruit larger sample sizes (need more participants per variant)
- Ask about clarity, appeal, and usefulness
- Compare results statistically across groups
- Ensure groups are demographically similar
- Use for concepts where comparison creates bias

*Don'ts*
- Use monadic testing when direct comparison would be valuable
- Show multiple variants to the same participant
- Underestimate required sample size
- Skip validation that groups are comparable
- Use when you have very limited participants
- Forget that monadic tests are more expensive

**References**
- [Qualtrics: Monadic Testing](https://www.qualtrics.com/experience-management/research/monadic-testing/)
- [UserTesting: Monadic vs Sequential Testing](https://www.usertesting.com/resources/topics/monadic-testing)

---
## MoSCoW Method
**Category:** strategy | **Type:** framework | **Tags:** strategy

A prioritization framework that categorizes requirements or features into four groups: Must have, Should have, Could have, and Won't have. MoSCoW helps teams agree on priorities and manage scope by making trade-offs explicit.

**Examples**
- Labeling user authentication as "Must have" and dark mode as "Could have" for MVP launch
- Using MoSCoW to decide what features to cut when facing timeline constraints

**Do's and Don'ts**

*Do's*
- Define clear criteria for each category
- Limit "Must haves" to truly essential items
- Revisit categorization as priorities change
- Use MoSCoW for scope management and release planning
- Get stakeholder alignment on categories
- Document reasoning for classifications

*Don'ts*
- Make everything a "Must have"
- Use MoSCoW without time constraints context
- Let politics override user needs in classification
- Ignore "Won't haves" indefinitely
- Skip the difficult prioritization conversations
- Apply MoSCoW without understanding dependencies

**References**
- [ProductPlan: MoSCoW Prioritization](https://www.productplan.com/glossary/moscow-prioritization/)
- [Agile Business Consortium: MoSCoW Guide](https://www.agilebusiness.org/dsdm-project-framework/moscow-prioririsation.html)

---
## Multiple Chart Grid
**Category:** ui | **Type:** pattern | **Tags:** data-visualization

Grid of identical charts enables small multiple comparisons.

**Examples**
- Sales by region (12 charts)
- Temperature by city grid
- Product performance matrix
- Campaign results comparison

**Do's and Don'ts**

*Do's*
- Identical scales/axes
- Consistent color encoding
- Remove redundant legends
- Logical reading order

*Don'ts*
- Different y-axis scales
- Individual chart titles
- Repeated legends
- Irregular grid spacing

**References**
- [Small Multiples](https://www.smallmultiples.org/)
- [Information is Beautiful](https://informationisbeautiful.net/)

---
## Multivariate Testing
**Category:** ux | **Type:** methodology | **Tags:** testing

A quantitative testing method that evaluates multiple variables simultaneously to determine which combination of changes produces the best outcome. Multivariate testing tests all possible combinations of variables to find optimal designs.

**Examples**
- Testing combinations of headline, image, and button text to find the best-performing version
- Evaluating different layouts, colors, and copy simultaneously on a landing page

**Do's and Don'ts**

*Do's*
- Have sufficient traffic for testing multiple combinations
- Test variables that are likely to interact
- Define clear success metrics upfront
- Ensure statistical significance
- Use when you need to test combinations
- Plan for exponential growth in variants

*Don'ts*
- Use multivariate testing with low traffic
- Test variables that don't interact
- Add too many variables (traffic requirement grows exponentially)
- Ignore the complexity of analysis
- Use when simple A/B testing would suffice
- Forget that each combination needs sufficient data

**References**
- [Nielsen Norman Group: Multivariate vs A/B Testing](https://www.nngroup.com/articles/multivariate-testing/)
- [Optimizely: Multivariate Testing](https://www.optimizely.com/optimization-glossary/multivariate-test-vs-ab-test/)

---
## Native Swipe Gestures
**Category:** ui | **Type:** pattern | **Tags:** mobile, interaction

Left/right swipes trigger list item actions.

**Examples**
- Swipe delete messages
- Swipe archive emails
- Swipe like/unlike posts
- Swipe to favorite songs

**Do's and Don'ts**

*Do's*
- Platform-standard direction
- Visual swipe preview
- Undo confirmation
- Haptic feedback

*Don'ts*
- Vertical swipe conflicts
- No visual feedback
- Inconsistent directions
- Desktop-only swipes

**References**
- [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/)
- [Material Design](https://m2.material.io/)

---
## Navigation Drawer
**Category:** ui | **Type:** pattern | **Tags:** navigation, mobile

Side panel sliding in from edge revealing additional navigation options.

**Examples**
- Left-edge swipe revealing app menu
- Gmail label navigation drawer
- Multi-level drawer menu
- Temporary drawer overlay

**Do's and Don'ts**

*Do's*
- Gesture + button access
- Persistent vs temporary drawer
- Logical menu organization
- Smooth slide animation

*Don'ts*
- Only button access (no gesture)
- Overload with too many options
- Poor touch targets
- Confusing close behavior

**References**
- [Material Design: Navigation Drawer](https://m3.material.io/components/navigation-drawer/overview)
- [UXPin: Drawer Patterns](https://www.uxpin.com/studio/blog/navigation-drawer-design/)

---
## Navigation Model
**Category:** ux | **Type:** concept | **Tags:** information-architecture, navigation

Structure defining how users move between sections and screens.

**Examples**
- Global nav + local section nav
- Tab bar + hamburger menu
- Breadcrumb + sidebar
- Footer links + mega menu

**Do's and Don'ts**

*Do's*
- Map all user journeys
- Support multiple paths
- Test task completion
- Consider mobile first

*Don'ts*
- Desktop patterns only
- Single path to everything
- More than 7 top items
- No wayfinding support

**References**
- [NN/g: Navigation Design](https://www.nngroup.com/articles/navigation-design/)
- [Baymard Institute](https://baymard.com/)

---
## Net Promoter Score (NPS)
**Category:** ux | **Type:** tool | **Tags:** research, analytics

Single question measuring customer loyalty recommendation.

**Examples**
- 'Recommend to colleague?' 0-10
- NPS 42 calculation
- Quarterly NPS tracking
- Segment by customer type

**Do's and Don'ts**

*Do's*
- Follow-up 'why' question
- Segment by demographics
- Track over time
- Actionable follow-up

*Don'ts*
- Single score reporting
- No segmentation
- Annual measurement only
- No improvement plan

**References**
- [Qualtrics: Net Promoter Score](https://www.qualtrics.com/experience-management/customer/net-promoter-score/)
- [Delighted](https://delighted.com/)

---
## North Star Metric
**Category:** strategy | **Type:** concept | **Tags:** strategy

Single metric measuring core product value delivery.

**Examples**
- Airbnb: Bookings completed
- Slack: Daily active pairs
- Dropbox: Space shared
- Spotify: Time listening

**Do's and Don'ts**

*Do's*
- Directly ties to value
- Single unambiguous metric
- Everyone understands
- Track week-over-week

*Don'ts*
- Multiple competing metrics
- Vanity engagement metric
- Team-specific KPIs
- Lagging indicator

**References**
- [Lenny Rachitsky: North Star Metric](https://www.lennyrachitsky.com/north-star-metric)
- [Tempered Growth](https://tempered-growth.com/)

---
## Offline-First Architecture
**Category:** strategy | **Type:** methodology | **Tags:** mobile, strategy

App works without internet designed first.

**Examples**
- Local-first data sync
- Offline content caching
- Queue actions for sync
- Conflict resolution rules

**Do's and Don'ts**

*Do's*
- Clear offline indicators
- Smart sync strategy
- Graceful online recovery
- Data backup strategy

*Don'ts*
- Online-only app
- Poor offline messaging
- Data loss on disconnect
- Manual sync required

**References**
- [Realm: Offline First Strategy](https://realm.io/blog/offline-first-strategy)
- [PWA Stats](https://pwa-stats.com/)

---
## OKR Alignment Meeting
**Category:** management | **Type:** methodology | **Tags:** strategy, processes

Cross-team objective synchronization discussion.

**Examples**
- Q3 company OKRs shared
- Team OKRs contribution
- Conflicts priorities resolved
- Quarterly 90min session

**Do's and Don'ts**

*Do's*
- Company → team → individual
- Conflicts surfaced resolved
- Success metrics aligned
- Documentation shared

*Don'ts*
- Siloed OKR planning
- Bottom-up only
- No conflict resolution
- Annual alignment

**References**
- [What Matters: OKR Alignment Playbook](https://www.whatmatters.com/resources/okr-alignment-playbook)
- [re:Work](https://rework.withgoogle.com/)

---
## OKR Framework
**Category:** strategy | **Type:** framework | **Tags:** strategy

Objectives (inspirational) Key Results (measurable).

**Examples**
- Q2 Objective: Double MAU
- KR1: D30 retention 28%
- 3-5 KRs per objective
- Quarterly cadence

**Do's and Don'ts**

*Do's*
- Ambitious stretch goals
- 3-5 measurable KRs
- Cross-team visibility
- Weekly OKR checkins

*Don'ts*
- Too many OKRs
- Vague qualitative KRs
- Annual planning cycle
- Secret team OKRs

**References**
- [What Matters](https://www.whatmatters.com/)
- [OKR International](https://okrinternational.com/)

---
## Onboarding Process
**Category:** management | **Type:** methodology | **Tags:** processes

New hire first 90 days structured experience.

**Examples**
- Day 1: Welcome orientation
- Week 1: Team intros training
- Month 1: First project
- 90-day check-in

**Do's and Don'ts**

*Do's*
- Buddy mentorship program
- Clear milestones
- Feedback checkpoints
- Equipment Day 0

*Don'ts*
- Sink or swim
- No clear milestones
- Single orientation day
- No feedback loop

**References**
- [Growth Ramp: Onboarding](https://www.growthramp.io/onboarding/)
- [New Hire](https://www.new-hire.com/)

---
## One-on-One Meeting
**Category:** management | **Type:** methodology | **Tags:** processes

Regular manager-direct report sync cadence.

**Examples**
- 30min weekly
- Employee agenda first
- Career growth focus
- Action items documented

**Do's and Don'ts**

*Do's*
- Employee owns agenda
- 80% listening
- Follow-through tracking
- Rotate meeting formats

*Don'ts*
- Status reporting
- Manager monologue
- No agenda preparation
- Irregular cadence

**References**
- [Manager Tools](https://manager-tools.com/)
- [GROWS Method](https://growsmethod.com/)

---
## Opportunity Interviews
**Category:** strategy | **Type:** methodology | **Tags:** strategy, research

Customer conversations uncover unmet needs.

**Examples**
- 15 customer interviews
- 'Struggling with X because...'
- Progress mapping
- Pain gain prioritization

**Do's and Don'ts**

*Do's*
- Target struggling customers
- Progress-focused questions
- Document verbatim quotes
- Cross-interview patterns

*Don'ts*
- Happy customers only
- Feature request fishing
- Leading questions
- Single interview

**References**
- [Strategyzer: Opportunity Interviews](https://strategyzer.com/library/opportunity-interviews)
- [JTBD.info](https://jtbd.info/)

---
## Opportunity Scoring
**Category:** strategy | **Type:** framework | **Tags:** strategy

A prioritization method that identifies opportunities by measuring the gap between how important a need is and how satisfied users currently are. The largest gaps represent the biggest opportunities for improvement.

**Examples**
- Surveying users on importance and satisfaction with features to find the biggest gaps
- Identifying that "fast search" is important but users are unsatisfied, creating a high-priority opportunity

**Do's and Don'ts**

*Do's*
- Ask users to rate both importance and satisfaction
- Calculate opportunity scores (Importance - Satisfaction)
- Focus on high importance, low satisfaction items
- Use standardized scales for consistent measurement
- Survey enough users for reliable data
- Combine with other prioritization inputs

*Don'ts*
- Focus only on satisfaction without importance
- Ignore items that are important and satisfactory (maintain these)
- Use opportunity scoring for exploratory innovation
- Skip validation of why satisfaction is low
- Treat opportunity scores as the only decision factor
- Survey infrequently and treat scores as permanent

**References**
- [Strategyn: Opportunity Scoring](https://strategyn.com/outcome-driven-innovation-process/opportunity-scoring/)
- [JTBD: Opportunity Algorithm](https://jtbd.info/jobs-to-be-done-a-framework-for-customer-needs-c883cbf61c90)

---
## Opportunity Solution Tree
**Category:** ux | **Type:** tool | **Tags:** ideation

Visual map connecting outcomes to opportunities to solutions.

**Examples**
- Outcome: increase retention
- Opportunities: onboarding friction
- Solutions: welcome wizard
- Experiments to validate

**Do's and Don'ts**

*Do's*
- Start with outcome
- Multiple opportunities
- Many solutions per opportunity
- Test assumptions

*Don'ts*
- Skip to solutions
- Single opportunity
- No experimentation
- Static tree

**References**
- [Teresa Torres: Opportunity Solution Trees](https://www.producttalk.org/)
- [Continuous Discovery Habits](https://www.producttalk.org/book/)

---
## Override Detection Rate
**Category:** ui | **Type:** tool | **Tags:** analytics, design-systems

Percentage components with local style overrides.

**Examples**
- 12% button overrides
- 8% spacing deviations
- Mobile higher override rate
- Override pattern analysis

**Do's and Don'ts**

*Do's*
- Categorize override types
- Impact severity scoring
- Cross-team comparison
- Reduction target setting

*Don'ts*
- Count all overrides equal
- No categorization
- Design-only analysis
- No reduction targets

**References**
- [Supernova: Design System Metrics](https://www.supernova.io/blog/design-system-metrics)
- [Design Systems News](https://designsystems.news/)

---
## Page Load Time
**Category:** ux | **Type:** tool | **Tags:** analytics, web

Time request to interactive ready.

**Examples**
- LCP 2.4s TTI 3.8s
- Mobile 4.2s desktop 1.9s
- Core Web Vitals correlation
- Revenue impact analysis

**Do's and Don'ts**

*Do's*
- Real user monitoring
- Business impact correlation
- Platform optimization
- Continuous tracking

*Don'ts*
- Lab synthetic only
- No revenue correlation
- Desktop focus
- Monthly snapshots

**References**
- [web.dev: Performance](https://web.dev/learn/performance)

---
## Pagination
**Category:** ui | **Type:** pattern | **Tags:** navigation

Controls for navigating through multiple pages of content.

**Examples**
- Numbered pagination (1 2 3 ... 10)
- Previous/Next arrows
- Load more button
- Infinite scroll

**Do's and Don'ts**

*Do's*
- Show current page clearly
- Limit visible page numbers
- Previous/Next always available
- Jump to first/last options

*Don'ts*
- Too many page numbers
- No current page indicator
- Disable prev/next inappropriately
- Poor mobile handling

**References**
- [NN/g: Pagination Patterns](https://www.nngroup.com/articles/pagination-vs-infinite-scroll/)
- [UX Movement: Pagination](https://uxmovement.com/navigation/why-users-get-lost-using-infinite-scroll/)

---
## Pair Design Sessions
**Category:** management | **Type:** methodology | **Tags:** processes

Two designers collaborative problem solving.

**Examples**
- Morning: Problem framing
- Midday: Divergent sketching
- Afternoon: Convergent critique
- Daily 2hr sessions

**Do's and Don'ts**

*Do's*
- Senior junior pairing
- Structured agenda
- Document outcomes
- Rotate partners

*Don'ts*
- Same partner always
- Unstructured time
- No documentation
- Design-only pairing

**References**
- [Figma: Pair Design](https://www.figma.com/blog/pair-design/)
- [UX Design](https://uxdesign.cc/)

---
## Pareto Principle
**Category:** strategy | **Type:** principle | **Tags:** strategy

80% results come from 20% causes (80/20 rule).

**Examples**
- Focus 80% effort on 20% features
- Prioritize high-impact components
- Identify power users first
- Optimize top traffic pages

**Do's and Don'ts**

*Do's*
- Rank by actual impact
- Regular Pareto analysis
- Focus ruthlessly
- Measure before/after

*Don'ts*
- Apply to everything equally
- Comfortable mediocrity
- Equal resource distribution
- Ignore data patterns

**References**
- [Investopedia: Pareto Principle](https://www.investopedia.com/terms/p/pareto-principle.asp)
- [FourWeekMBA](https://fourweekmba.com/)

---
## Participatory Design
**Category:** ux | **Type:** methodology | **Tags:** research

Users co-create solutions collaborative workshops.

**Examples**
- Users sketch wireframes
- Co-design workshop 8 users
- Prototype co-creation
- Iterative user involvement

**Do's and Don'ts**

*Do's*
- Real end users
- Structured facilitation
- Concrete outputs
- Multiple iterations

*Don'ts*
- Stakeholders as users
- Unstructured sessions
- No concrete deliverables
- Single workshop

**References**
- [IxDF: Participatory Design](https://www.interaction-design.org/literature/topics/participatory-design)
- [UX Collective](https://uxcollective.com/)

---
## Pattern Library
**Category:** ui | **Type:** tool | **Tags:** documentation, design-systems

Catalog of reusable interaction and layout patterns with implementation examples.

**Examples**
- Card patterns (product, user, stats)
- Navigation patterns (tab bar, sidebar)
- Form patterns (wizard, inline edit)
- Data display patterns (table, list)

**Do's and Don'ts**

*Do's*
- Organize by abstraction level
- Include anti-patterns
- Link related patterns
- Show platform variations

*Don'ts*
- Mix components and patterns
- Lack search functionality
- Forget mobile patterns
- Static screenshots only

**References**
- [Pattern Lab](https://patternlab.io)

---
## Peak-End Rule
**Category:** ux | **Type:** principle

Users judge experiences by peak moments and endings.

**Examples**
- Fast checkout completion
- Smooth onboarding finish
- Positive farewell screen
- Quick error recovery

**Do's and Don'ts**

*Do's*
- Strong positive peak moments
- Frictionless endings
- Recovery from bad peaks
- Consistent positive closure

*Don'ts*
- Slow boring experiences
- Frustrating checkout end
- Bad last impression
- Peak problems unresolved

**References**
- [NN/g: Peak-End Rule](https://www.nngroup.com/articles/peak-end-rule/)
- [UX Collective](https://uxcollective.com/)

---
## Perceptually Uniform Color Spaces
**Category:** ui | **Type:** tool | **Tags:** color

Color spaces (LAB, LCH, OKLAB, OKLCH) designed so that equal numerical changes produce equal perceived visual changes. Unlike RGB or HSL, these spaces ensure that a 10-unit lightness change looks the same whether moving from light to mid or mid to dark tones.

**Examples**
- Generating a color scale in LCH by adjusting lightness in equal steps for visually even gradients
- Using OKLCH in CSS to create smooth transitions that don't muddy through gray
- Building accessible color ramps where each step has predictable perceived difference
- Adjusting chroma in LCH to desaturate colors without shifting hue unexpectedly

**Do's and Don'ts**

*Do's*
- Use LCH/OKLCH for generating color scales and gradients
- Adjust lightness (L) for creating tonal variations
- Use chroma (C) for saturation adjustments without hue shifts
- Consider OKLCH for CSS (modern browser support)
- Verify results visually (models are approximations)

*Don'ts*
- Use RGB/HSL for creating perceptually even scales
- Assume HSL lightness is perceptually uniform (it's not)
- Forget that out-of-gamut colors may clip when converted to RGB
- Ignore that different hues have different maximum chroma ranges
- Over-rely on numbers without visual validation

**References**
- [OKLCH in CSS: Why We Moved From RGB and HSL](https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl)
- [Lea Verou: LCH Colors in CSS](https://lea.verou.me/2020/04/lch-colors-in-css-what-why-and-how/)

---
## Performance Budget
**Category:** strategy | **Type:** methodology | **Tags:** web, analytics, strategy

Maximum acceptable thresholds for load time resources.

**Examples**
- LCP budget 2.5s, TTI 3.8s
- Bundle < 170kb gzipped
- 100 Lighthouse score target
- Mobile 3G simulation

**Do's and Don'ts**

*Do's*
- Enforce in CI/CD
- Track regression
- Stakeholder alignment
- Quarterly reviews

*Don'ts*
- No budget enforcement
- Desktop testing only
- Ignore bundle growth
- Lab data only

**References**
- [WebPageTest: Performance Budget](https://www.webpagetest.org/performance-budget/)
- [Tim Cadrigan](https://timcadrigan.com/)

---
## Performance Load Testing
**Category:** ui | **Type:** tool | **Tags:** testing, analytics

Speed interactions under network server stress.

**Examples**
- PageSpeed 95 mobile
- TTI 2.8s Core Web Vitals
- 5k concurrent users
- 3G slow network testing

**Do's and Don'ts**

*Do's*
- Real user monitoring
- Synthetic lab testing
- Load testing infrastructure
- Continuous monitoring

*Don'ts*
- Lab data only
- No concurrent testing
- Ignore real networks
- Monthly testing only

**References**
- [web.dev: Core Web Vitals](https://web.dev/articles/vitals)

---
## Performance Review Cycle
**Category:** management | **Type:** methodology | **Tags:** processes

Structured evaluation feedback process.

**Examples**
- Quarterly 360 feedback
- Self assessment + manager
- OKR attainment 70%
- Development plan creation

**Do's and Don'ts**

*Do's*
- Multi-source feedback
- Behavioral examples
- Future-focused development
- Calibration across team

*Don'ts*
- Annual review only
- Subjective ratings
- Past performance focus
- No development plan

**References**
- [15Five: Performance Review](https://www.15five.com/blog/performance-review/)
- [Culture Amp](https://cultureamp.com/)

---
## Persona Development
**Category:** ux | **Type:** methodology | **Tags:** research

Creating fictional yet realistic representations of key user segments based on research data. Personas include demographics, behaviors, goals, motivations, and pain points to help teams empathize with and design for specific user types.

**Examples**
- Developing 3-4 primary personas representing different user types for an e-commerce platform
- Creating personas for healthcare providers with different specializations and technology comfort levels

**Do's and Don'ts**

*Do's*
- Base personas on actual user research data
- Include goals, behaviors, and pain points
- Keep to 3-5 primary personas maximum
- Make personas specific and believable
- Use personas to guide design decisions
- Update personas as you learn more

*Don'ts*
- Create personas from assumptions or stereotypes
- Include too many personas
- Add irrelevant personal details
- Use personas as the only research artifact
- Make personas too generic or vague
- Create personas and never reference them

**References**
- [Nielsen Norman Group: Personas](https://www.nngroup.com/articles/persona/)
- [Interaction Design Foundation: Personas Guide](https://www.interaction-design.org/literature/article/personas-why-and-how-you-should-use-them)

---
## Pie Slice Chart
**Category:** ui | **Type:** tool | **Tags:** data-visualization

Circular sectors show part-to-whole relationships and proportions.

**Examples**
- Market share by competitor
- Budget breakdown by category
- Traffic sources percentages
- Device usage distribution

**Do's and Don'ts**

*Do's*
- Limit to 5-7 slices max
- Largest slice starts at 12
- Consistent slice ordering
- Include total percentage

*Don'ts*
- 3D pie charts
- Very thin slices (<5%)
- Donut charts with many slices
- Missing labels

**References**
- [FusionCharts: When to Use Pie Charts](https://www.fusioncharts.com/blog/when-to-use-pie-charts/)
- [Storytelling with Data](https://storytellingwithdata.com/)

---
## Pinch to Zoom
**Category:** ui | **Type:** pattern | **Tags:** mobile, interaction

Two-finger spread/shrink controls magnification.

**Examples**
- Photo gallery zoom
- Map pinch navigation
- PDF document zoom
- Canvas drawing zoom

**Do's and Don'ts**

*Do's*
- Smooth zoom animation
- Double-tap zoom preset
- Minimum/maximum bounds
- Zoom with pan

*Don'ts*
- Zoom buttons only
- Pixelated zoom quality
- No pan after zoom
- Desktop-only zoom

**References**
- [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/)
- [Material Design](https://m2.material.io/)

---
## Polyfill Implementation
**Category:** ui | **Type:** tool | **Tags:** web

JavaScript shims providing modern APIs to older browsers.

**Examples**
- IntersectionObserver polyfill
- fetch() API polyfill
- Custom Elements v1 polyfill
- ResizeObserver shim

**Do's and Don'ts**

*Do's*
- Core functionality only
- Performance budget limit
- Bundle size monitoring
- Automated testing

*Don'ts*
- Polyfill everything
- Large bundle impact
- No performance budget
- Manual polyfill updates

**References**
- [Polyfill.io](https://polyfill.io/)
- [Can I Use: Polyfill](https://caniuse.com/polyfill)

---
## Power User Percentage
**Category:** ux | **Type:** tool | **Tags:** analytics

Percentage users disproportionate value creation.

**Examples**
- 13% users 87% revenue
- Pareto 80/20 segmentation
- Power user retention 68%
- Acquisition source analysis

**Do's and Don'ts**

*Do's*
- Define power user criteria
- Revenue vs usage segments
- Retention correlation
- Acquisition optimization

*Don'ts*
- Equal user treatment
- No criteria definition
- Revenue-only focus
- Average all users

**References**
- [For Entrepreneurs: Power Users](https://www.forentrepreneurs.com/power-users/)

---
## Pre-mortem Analysis
**Category:** strategy | **Type:** tool | **Tags:** strategy

Imagine project failed predict prevent risks.

**Examples**
- 'We failed because...'
- 25 risks identified
- Mitigation plans created
- Cross-team workshop

**Do's and Don'ts**

*Do's*
- Future perfect tense
- Diverse perspectives
- Actionable mitigations
- RACI assignment

*Don'ts*
- Blame assignment
- Optimism bias only
- No mitigation plans
- Post-failure analysis

**References**
- [Psychology Today: Pre-mortems](https://www.psychologytoday.com/us/blog/the-leaders-pocket/202401/the-power-of-pre-mortems)
- [HBR](https://hbr.org/)

---
## Preference Testing
**Category:** ux | **Type:** methodology | **Tags:** testing, research

Users choose preferred design from multiple options.

**Examples**
- A/B headline preference
- Layout A vs B 68% preference
- Color scheme tournament
- 5-design preference matrix

**Do's and Don'ts**

*Do's*
- Single variable comparison
- Even presentation order
- Large sample size
- Clear preference criteria

*Don'ts*
- Multiple variable changes
- Leading presentation
- Small sample size
- Vague preference ask

**References**
- [UserTesting: Preference Testing](https://www.usertesting.com/guides/preference-testing)

---
## Preload Key Resources
**Category:** ui | **Type:** tool | **Tags:** web, analytics

Fetch critical assets early in page load process.

**Examples**
- <link rel=preload as=font href=hero.woff2>
- Preload LCP hero image
- Preload critical CSS/JS
- DNS prefetch third-parties

**Do's and Don'ts**

*Do's*
- Prioritize LCP resources
- Monitor preload impact
- Remove unused preloads
- Cross-origin CORS correct

*Don'ts*
- Preload everything
- Wrong as= type attributes
- No crossorigin
- Unused preloads

**References**
- [Web.dev: Preload Critical Resources](https://web.dev/preload-critical-resources/)
- [MDN](https://developer.mozilla.org/en-US/)

---
## Presentation Canvas
**Category:** strategy | **Type:** tool | **Tags:** strategy

Single page story structure key messages visuals.

**Examples**
- Hero slide problem statement
- 3 proof points
- Call to action bottom
- Visual hierarchy clear

**Do's and Don'ts**

*Do's*
- Single canvas per deck
- Story structure first
- Visuals not decoration
- Rehearsed timing

*Don'ts*
- Slide-by-slide planning
- Text-heavy canvas
- Decorative visuals
- Unrehearsed delivery

**References**
- [Duck Design: Presentation Canvas](https://www.duckdesign.com/blog/presentation-canvas)

---
## Primary Navigation
**Category:** ui | **Type:** pattern | **Tags:** navigation

Main navigation presenting highest-level site sections and most important destinations.

**Examples**
- Top horizontal bar with Home, Products, About
- Logo + hamburger menu for mobile
- Tab bar in mobile apps
- Global nav spanning entire site

**Do's and Don'ts**

*Do's*
- Limit to 5-7 main items
- Use prominent, persistent location
- Prioritize most-used destinations
- Ensure mobile responsiveness

*Don'ts*
- Bury primary nav in menus
- Use more than 7 main items
- Change primary nav location
- Include secondary content

**References**
- [UX Planet: Navigation Glossary](https://uxplanet.org/ux-glossary-navigation/)
- [Justinmind: Navigation Design](https://www.justinmind.com/blog/navigation-design-patterns/)

---
## Problem Framing
**Category:** strategy | **Type:** methodology

The process of clearly defining and articulating a problem before seeking solutions. Problem framing shapes how teams understand challenges and influences the range of solutions they consider.

**Examples**
- Reframing "users don't complete checkout" to "users feel uncertain about shipping costs during checkout"
- Transforming "add more features" into "users can't find the features they need"

**Do's and Don'ts**

*Do's*
- Base problem statements on research insights
- Frame problems from the user's perspective
- Make problem statements specific and actionable
- Challenge assumptions about the problem
- Explore multiple framings of the same problem
- Align stakeholders on the problem before solutioning

*Don'ts*
- Jump to solutions before framing the problem
- Frame problems around internal constraints only
- Use vague or overly broad problem statements
- Let stakeholder opinions replace user research
- Stick with the first problem framing
- Frame problems that assume a specific solution

**References**
- [Nielsen Norman Group: Problem Framing](https://www.nngroup.com/articles/problem-framing/)
- [Stanford d.school: Define Mode](https://dschool.stanford.edu/resources/define-mode)

---
## Problem Restatement
**Category:** ux | **Type:** methodology | **Tags:** ideation

Reframe problem multiple ways to unlock new solution angles.

**Examples**
- "How might we..." variations
- Opposite framing
- User perspective shift
- Constraint removal

**Do's and Don'ts**

*Do's*
- Multiple reframes
- Challenge assumptions
- Include stakeholder views
- Test framings

*Don'ts*
- Single restatement
- Keep original bias
- Skip validation
- Abstract only

**References**
- [IDEO: Reframing](https://www.ideo.com/)
- [Stanford d.school](https://dschool.stanford.edu/)

---
## Product Analytics
**Category:** ux | **Type:** tool | **Tags:** analytics

The practice of collecting and analyzing quantitative data about how users interact with a product. Product analytics tools track behavior, usage patterns, funnels, and metrics to inform design and product decisions.

**Examples**
- Tracking feature adoption rates to understand which new features users find valuable
- Analyzing drop-off points in checkout funnel to identify design improvements

**Do's and Don'ts**

*Do's*
- Define metrics that align with business and user goals
- Combine quantitative data with qualitative research
- Track behavior, not just outcomes
- Set up event tracking deliberately
- Review analytics regularly with team
- Use insights to generate hypotheses for research

*Don'ts*
- Rely only on analytics without user research
- Track everything without purpose
- Make decisions based on vanity metrics
- Ignore the "why" behind the numbers
- Forget to validate tracking implementation
- Let analytics replace talking to users

**References**
- [Amplitude: Product Analytics Guide](https://amplitude.com/blog/product-analytics)
- [Nielsen Norman Group: Analytics and User Experience](https://www.nngroup.com/articles/analytics-user-experience/)

---
## Product Roadmap
**Category:** strategy | **Type:** tool | **Tags:** strategy, processes

Timeline prioritized feature delivery plan.

**Examples**
- 3-month rolling roadmap
- Now Next Later framework
- RICE prioritized
- Quarterly stakeholder review

**Do's and Don'ts**

*Do's*
- Customer outcome focus
- Timeboxed commitment
- Cross-team alignment
- Monthly refresh

*Don'ts*
- Feature dump timeline
- Forever roadmap
- Secret team document
- Annual planning only

**References**
- [Productboard: Product Roadmaps](https://productboard.com/product-roadmaps/)
- [Roadmunk](https://roadmunk.com/)

---
## Progressive Disclosure
**Category:** ux | **Type:** pattern | **Tags:** interaction

Gradually revealing information based on user interaction and need.

**Examples**
- Collapsible sections
- Stepper wizards
- Expandable cards
- Lazy-loaded content

**Do's and Don'ts**

*Do's*
- Reveal info by relevance
- Provide clear expand/collapse cues
- Maintain context during disclosure
- Support skip to advanced

*Don'ts*
- Reveal everything at once
- Hide critical information
- Confusing disclosure controls
- No collapse option

**References**
- [NN/g: Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/)
- [UX Planet: Information Architecture](https://uxplanet.org/progressive-disclosure-in-ux-design/)

---
## Progressive Enhancement
**Category:** ui | **Type:** principle | **Tags:** accessibility, web

Core functionality first, enhancements layered.

**Examples**
- Semantic HTML foundation
- CSS visual polish
- JavaScript interactivity
- ARIA accessibility layer

**Do's and Don'ts**

*Do's*
- Content readable without JS
- Core task completion possible
- Graceful enhancement
- Feature detection first

*Don'ts*
- JS required for layout
- Content hidden without CSS
- No fallback navigation
- Flash of unstyled content

**References**
- [Smashing Magazine: Progressive Enhancement](https://www.smashingmagazine.com/2019/04/progressive-enhancement/)
- [Progressive Enhancement](https://progressiveenhancement.org/)

---
## Progressive Web App
**Category:** ui | **Type:** pattern | **Tags:** web, mobile

Website with native app features (install offline).

**Examples**
- App manifest + service worker
- Offline page support
- Add to home screen
- Push notifications

**Do's and Don'ts**

*Do's*
- HTTPS required
- App-like experience
- Fast offline fallback
- Clear install prompts

*Don'ts*
- No service worker
- Poor offline experience
- Desktop-only PWA
- Missing manifest

**References**
- [Web.dev: Progressive Web Apps](https://web.dev/progressive-web-apps/)
- [MDN](https://developer.mozilla.org/en-US/)

---
## Prototype Guide
**Category:** ui | **Type:** tool | **Tags:** documentation, interaction

Documentation of interactive prototype states, transitions, and behaviors.

**Examples**
- Modal stack order documentation
- Swipe gesture behaviors
- Loading sequence timing
- Error recovery flows

**Do's and Don'ts**

*Do's*
- Document timing
- Record edge cases
- Specify device behaviors
- Include audio guidelines

*Don'ts*
- Focus only on happy path
- Missing device specifics
- No timing information
- Static screenshots

**References**
- [InVision Prototype](https://www.invisionapp.com/prototype/)
- [Proto.io](https://proto.io/)

---
## Prototype Testing
**Category:** ux | **Type:** methodology | **Tags:** testing

Evaluating an interactive representation of a design with users to validate functionality, flow, and usability before full development. Prototype testing uses clickable mockups or working prototypes to simulate the final experience.

**Examples**
- Testing an interactive Figma prototype of a new checkout flow with target users
- Validating a coded prototype of mobile gestures with real users on devices

**Do's and Don'ts**

*Do's*
- Choose prototype fidelity appropriate to questions being tested
- Give users realistic tasks to complete
- Observe behavior more than collecting opinions
- Test critical paths and edge cases
- Iterate based on findings before building
- Document issues and prioritize fixes

*Don'ts*
- Build high-fidelity prototypes for everything
- Explain how the prototype should work
- Test only happy paths
- Defend design choices during testing
- Prototype features you can't build
- Skip prototype testing to save time

**References**
- [Nielsen Norman Group: Prototyping](https://www.nngroup.com/articles/ux-prototype-hi-lo-fidelity/)
- [Interaction Design Foundation: Prototyping](https://www.interaction-design.org/literature/topics/prototyping)

---
## Pull-to-Refresh
**Category:** ui | **Type:** pattern | **Tags:** mobile, interaction

Downward swipe gesture reloads content list.

**Examples**
- Email inbox refresh
- Social feed timeline
- Chat message list
- News feed update

**Do's and Don'ts**

*Do's*
- Haptic feedback on release
- Visual loading indicator
- Overscroll resistance
- Release threshold clear

*Don'ts*
- Pull anywhere on screen
- No visual feedback
- Jarring content jump
- Desktop mouse support

**References**
- [Apple HIG: Pull to Refresh](https://developer.apple.com/design/human-interface-guidelines/pull-to-refresh)
- [Material Design](https://m2.material.io/)

---
## RACI Matrix
**Category:** strategy | **Type:** framework | **Tags:** strategy, processes

Responsible Accountable Consulted Informed assignments.

**Examples**
- PM Responsible roadmap
- CPO Accountable priorities
- Design Consulted UX
- Sales Informed timeline

**Do's and Don'ts**

*Do's*
- Single Accountable person
- Multiple Responsible ok
- Consult before deciding
- Inform after decision

*Don'ts*
- No Accountable person
- Everyone Responsible
- Consult after decision
- Never Informed

**References**
- [ProductPlan: RACI Matrix](https://www.productplan.com/glossary/raci-matrix/)
- [Asana](https://asana.com/)

---
## Radius Tokens
**Category:** ui | **Type:** principle | **Tags:** design-systems

Variables defining consistent border radius values for components to create unified visual style across the interface.

**Examples**
- radius-xs: 2px
- radius-sm: 4px
- radius-md: 8px
- radius-full: 9999px

**Do's and Don'ts**

*Do's*
- Define 4-6 scale steps
- Use semantic names (container not 12px)
- Test visual harmony across components
- Plan for brand personality (sharp vs soft)

*Don'ts*
- Apply random radius values
- Ignore component hierarchy
- Use radius inconsistently
- Skip accessibility contrast checks

**References**
- [Material Design 3: Shape](https://m3.material.io/styles/shape/overview)
- [Bento Design](https://bento.design/)

---
## Rage Click Detection
**Category:** ux | **Type:** tool | **Tags:** analytics

Frustrated repeated clicking non-functional areas.

**Examples**
- 2.7% rage click rate
- Checkout button frustration
- Mobile menu rage clicks
- UX issue prioritization

**Do's and Don'ts**

*Do's*
- Correlate with drop-off
- Segment by user type
- Hotspot visualization
- Immediate UX fixes

*Don'ts*
- Ignore low percentages
- No drop-off correlation
- Desktop-only tracking
- No visualization

**References**
- [UXCam: Rage Clicks](https://uxcam.com/blog/rage-clicks/)

---
## Random Word Association
**Category:** ux | **Type:** tool | **Tags:** ideation

Use unrelated words to spark unexpected creative connections.

**Examples**
- "Elephant" + checkout flow
- Random noun generator
- Dictionary flip technique
- Image-based prompts

**Do's and Don'ts**

*Do's*
- Truly random words
- Force connections
- Multiple word rounds
- Document all associations

*Don'ts*
- Choose related words
- Dismiss odd connections
- Single word only
- Rush associations

**References**
- [Edward de Bono: Lateral Thinking](https://www.debono.com/)
- [Creative Confidence](https://www.creativeconfidence.com/)

---
## Real-time Metrics Board
**Category:** ui | **Type:** tool | **Tags:** data-visualization, analytics

Live-updating charts display streaming operational data continuously.

**Examples**
- Live website visitor count
- Real-time sales ticker
- Server load monitoring
- Support ticket velocity

**Do's and Don'ts**

*Do's*
- Clear update frequency
- Anomaly detection alerts
- Historical context line
- Pause/resume controls

*Don'ts*
- Over-updating (60fps)
- No historical baseline
- Alert fatigue design
- Mobile notifications

**References**
- [Grafana](https://grafana.com/)
- [InfluxData](https://www.influxdata.com/)

---
## Reduced Motion
**Category:** ui | **Type:** principle | **Tags:** accessibility, interaction

Respect user's 'prefers-reduced-motion' OS setting.

**Examples**
- @media (prefers-reduced-motion)
- Simple transitions only
- Static focus indicators
- No decorative motion

**Do's and Don'ts**

*Do's*
- Honor reduced-motion media query
- Test with OS setting enabled
- Provide static alternatives
- Never disable critical motion

*Don'ts*
- Ignore prefers-reduced-motion
- Parallax effects everywhere
- Auto-playing animations
- Motion-only feedback

**References**
- [WCAG 2.3: Focus Appearance](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html)
- [CSS: prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)

---
## Reference Grid Overlay
**Category:** ui | **Type:** pattern | **Tags:** data-visualization

Light background lines aid precise value reading and alignment.

**Examples**
- Major grid every 10%
- Minor grid every 5%
- Horizontal + vertical grids
- Zero baseline emphasis

**Do's and Don'ts**

*Do's*
- Match data precision
- Light/opaque alternation
- Extend to chart edges
- Responsive scaling

*Don'ts*
- Heavy dark grids
- Grid behind every element
- Irregular spacing
- Grid on small screens

**References**
- [Visual Cinnamon: Grids](https://www.visualcinnamon.com/2016/07/grids/)
- [D3.js](https://d3js.org/)

---
## Remote Usability Testing
**Category:** ux | **Type:** methodology | **Tags:** testing, research

Online testing across geographic locations time zones.

**Examples**
- Zoom + Miro collaborative testing
- 12 participants 3 countries
- Async video submissions
- Screen sharing + webcam

**Do's and Don'ts**

*Do's*
- Test across time zones
- Record screen + face
- Stable internet connection
- Clear session schedule

*Don'ts*
- Poor internet participants
- No face cam recording
- Single time zone only
- No tech setup test

**References**
- [NN/g: Remote Usability Testing](https://www.nngroup.com/articles/remote-usability-tests/)
- [UX Collective: Remote Testing Guide](https://uxdesign.cc/remote-usability-testing/)

---
## Research Screener
**Category:** ux | **Type:** tool | **Tags:** research

Pre-study survey qualifying research participants.

**Examples**
- 'Use product daily?'
- 'Primary role marketing?'
- 'iOS or Android user?'
- 8 screening questions

**Do's and Don'ts**

*Do's*
- Specific behavioral criteria
- Negative screening first
- Clear disqualifiers
- Test screener yourself

*Don'ts*
- Vague qualification
- Too many questions
- Leading qualification
- No quota management

**References**
- [User Interviews: Recruiting Screener](https://www.userinterviews.com/recruiting-screener)
- [UX Research Recruiting](https://uxresearch.recruiting/)

---
## Responsive Guidelines
**Category:** ui | **Type:** tool | **Tags:** documentation, mobile, web

Breakpoint-specific layout and behavior documentation.

**Examples**
- Mobile-first breakpoints
- Container query guidelines
- Fluid typography rules
- Touch target specifications

**Do's and Don'ts**

*Do's*
- Define clear breakpoints
- Specify fluid scaling
- Include touch targets
- Test on real devices

*Don'ts*
- Fixed pixel breakpoints
- Desktop-first approach
- Missing touch specs
- Arbitrary breakpoints

**References**
- [Responsive Page](https://responsive.page/)
- [Every Layout](https://every-layout.dev/)

---
## Responsive Typography
**Category:** ui | **Type:** tool | **Tags:** typography, mobile, web

Scaling text proportionally using relative units (em, rem, %) across different screen sizes and devices. Responsive typography ensures readability and maintains visual hierarchy from mobile to desktop.

**Examples**
- Using rem units for font sizes that scale with root font size
- Implementing CSS clamp() for fluid typography between breakpoints
- Scaling heading sizes down on mobile while maintaining hierarchy ratios
- Adjusting line height and letter spacing responsively

**Do's and Don'ts**

*Do's*
- Use relative units (rem, em) instead of fixed pixels
- Scale font sizes based on viewport width
- Test typography across breakpoints
- Maintain hierarchy ratios responsively

*Don'ts*
- Use fixed pixel sizes for responsive design
- Ignore mobile typography needs
- Scale too aggressively between breakpoints
- Forget to test actual device rendering

**References**
- [Kaarwan: Typography Best Practices for UI Design](https://www.kaarwan.com/blog/typography-best-practices)
- [Material Design 3: Typography](https://m3.material.io/styles/typography)

---
## Retention Rate
**Category:** strategy | **Type:** tool | **Tags:** analytics

Percentage users returning after first use (D1 D7 D30).

**Examples**
- D1 42% D7 28% D30 15%
- Cohort week 1-4 retention
- Feature-specific retention
- Power user retention 68%

**Do's and Don'ts**

*Do's*
- Track D1 D7 D30
- Cohort analysis
- Segment by acquisition
- Set retention targets

*Don'ts*
- Single day retention
- No cohort comparison
- Average all users
- Ignore power users

**References**
- [Amplitude: Retention](https://amplitude.com/blog/retention/)

---
## Retrospectives
**Category:** management | **Type:** methodology | **Tags:** processes

A structured team reflection practice where members review what went well, what didn't, and what to improve for future work. Retrospectives create space for honest discussion and continuous team improvement.

**Examples**
- Monthly design team retrospective reviewing recent projects and identifying process improvements
- Post-project retrospective to capture learnings before starting next initiative

**Do's and Don'ts**

*Do's*
- Hold retrospectives regularly (sprint, monthly, post-project)
- Create psychological safety for honest feedback
- Focus on systems and processes, not individuals
- Turn insights into actionable improvements
- Rotate facilitators to get different perspectives
- Track action items and follow through

*Don'ts*
- Skip retrospectives when busy
- Let retrospectives become blame sessions
- Discuss only what went wrong
- Generate action items without ownership
- Have the same format every time
- Ignore patterns that emerge across retrospectives

**References**
- [Atlassian: Retrospectives Guide](https://www.atlassian.com/team-playbook/plays/retrospective)
- [Nielsen Norman Group: UX Team Retrospectives](https://www.nngroup.com/articles/ux-retrospectives/)

---
## Reverse Brainstorming
**Category:** ux | **Type:** tool | **Tags:** ideation

Solve opposite problem then invert for actual solutions.

**Examples**
- How to lose users fastest
- Make checkout impossible
- Worst customer service
- Invert each anti-solution

**Do's and Don'ts**

*Do's*
- Commit to opposite
- Systematic inversion
- Document both sides
- Find hidden assumptions

*Don'ts*
- Half-hearted reversal
- Skip inversion step
- Ignore insights
- Use for simple problems

**References**
- [MindTools: Reverse Brainstorming](https://www.mindtools.com/)
- [IDEO U](https://www.ideou.com/)

---
## RICE Framework
**Category:** strategy | **Type:** framework | **Tags:** strategy

A prioritization framework that scores ideas based on four factors: Reach (number of users affected), Impact (effect on individual users), Confidence (certainty of estimates), and Effort (time required). RICE was developed by Intercom's product team to make objective, data-driven prioritization decisions.

**Examples**
- Comparing feature requests by calculating RICE scores to determine roadmap priorities
- Evaluating marketing campaigns by estimating reach, impact, confidence, and effort before launch
- Prioritizing bug fixes by assessing how many users are affected and implementation complexity
- Scoring design improvements to identify highest-value, lowest-effort changes

**Do's and Don'ts**

*Do's*
- Use consistent metrics for reach across all items being compared
- Scale impact consistently (typically 0.25 to 3: minimal, low, medium, high, massive)
- Be honest about confidence levels (use percentages: 50%, 80%, 100%)
- Estimate effort in person-weeks or story points
- Recalculate scores as new information emerges
- Combine RICE with qualitative judgment for final decisions

*Don'ts*
- Manipulate scores to justify predetermined decisions
- Compare RICE scores across completely different types of work
- Use RICE as the only factor in prioritization
- Skip the effort estimation step
- Ignore low-scoring items that address critical user needs
- Apply RICE to every minor decision (overhead not worth it)

**References**
- [Intercom: RICE - Simple Prioritization for Product Managers](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/)
- [Productboard: RICE Scoring Model](https://www.productboard.com/glossary/rice-scoring-model/)
- [Aha!: RICE Scoring Framework](https://www.aha.io/roadmapping/guide/release-management/what-is-the-rice-prioritization-model)

---
## Roadmap Alignment Workshop
**Category:** management | **Type:** methodology | **Tags:** strategy, processes

Stakeholder prioritization consensus building.

**Examples**
- RICE scores workshop
- MoSCoW voting session
- 3-month rolling roadmap
- Cross-team buy-in

**Do's and Don'ts**

*Do's*
- Data-informed discussion
- Voting not arguing
- Clear decision criteria
- Documented outcomes

*Don'ts*
- Feature dumping
- Subjective prioritization
- No decision framework
- Secret roadmap

**References**
- [Productboard: Roadmap Workshops](https://productboard.com/roadmap-workshops/)

---
## Rose Thorn Bud Canvas
**Category:** ux | **Type:** tool | **Tags:** ideation

Categorize feedback as positives, negatives, and opportunities.

**Examples**
- Rose: smooth checkout
- Thorn: slow loading
- Bud: mobile app potential
- Color-coded sticky notes

**Do's and Don'ts**

*Do's*
- Balance all categories
- Specific observations
- Prioritize buds
- Action thorns

*Don'ts*
- All roses no thorns
- Vague categorization
- Ignore buds
- Skip synthesis

**References**
- [Stanford d.school](https://dschool.stanford.edu/)
- [LUMA Institute](https://www.luma-institute.com/)

---
## Round Robin Ideation
**Category:** ux | **Type:** tool | **Tags:** ideation

Sequential idea building where each person adds to previous.

**Examples**
- Pass sketch clockwise
- Build on neighbor's idea
- 2-minute rotations
- 6 rounds total

**Do's and Don'ts**

*Do's*
- Clear time limits
- Build don't replace
- Equal participation
- Document evolution

*Don'ts*
- Skip contributions
- Criticize additions
- Dominate discussion
- Lose original idea

**References**
- [Gamestorming](https://gamestorming.com/)
- [Design Sprint](https://www.gv.com/sprint/)

---
## Rule of 40
**Category:** strategy | **Type:** tool | **Tags:** analytics

Growth + profit margin minimum 40% combined.

**Examples**
- 35% growth + 12% margin = 47
- SaaS benchmark 40%
- Quarterly Rule of 40
- Segment by product line

**Do's and Don'ts**

*Do's*
- Growth + profitability balance
- Industry benchmarking
- Quarterly minimum
- Strategic planning input

*Don'ts*
- Growth-only focus
- Annual calculation
- No industry context
- Single metric obsession

**References**
- [SaaS Metrics: Rule of 40](https://www.saasmetrics.co/rule-of-40/)
- [Key Value Software](https://keyvaluesoftware.com/)

---
## Rule of Thirds
**Category:** ui | **Type:** principle

Canvas thirds create balanced focal points.

**Examples**
- CTA button at intersection
- Hero image subject on line
- Card image focal point aligned
- Logo top-left intersection

**Do's and Don'ts**

*Do's*
- Major elements on lines
- Balance across divisions
- Negative space consideration
- Mobile third adjustments

*Don'ts*
- Center everything
- Symmetrical grid only
- Ignore composition rules
- Static pixel positioning

**References**
- [Canva: Rule of Thirds](https://www.canva.com/learn/rule-of-thirds/)
- [Photography Tuts+](https://photography.tutsplus.com/)

---
## Safe Area Insets
**Category:** ui | **Type:** tool | **Tags:** mobile

Screen areas avoiding notches status gesture bars.

**Examples**
- iPhone X notch padding
- Android gesture bar inset
- Dynamic island spacing
- Corner radius safe zones

**Do's and Don'ts**

*Do's*
- Respect safe-area-inset
- Test all device models
- Content priority layout
- Visual debug boundaries

*Don'ts*
- Content under notch
- Fixed position ignoring insets
- No testing on new devices
- Desktop viewport sizing

**References**
- [WebKit: Designing for iPhone X](https://webkit.org/blog/7929/designing-websites-for-iphone-x/)
- [Android Developer](https://developer.android.com/)

---
## Sans-Serif Fonts
**Category:** ui | **Type:** concept | **Tags:** typography

Clean typefaces without decorative strokes (serifs) at letter ends (e.g., Helvetica, Inter, Roboto). Sans-serifs are the modern standard for UI design, offering clarity and legibility on screens.

**Examples**
- Using Inter or Roboto as primary UI font
- Applying SF Pro for iOS applications
- Choosing Open Sans for web interfaces
- Using geometric sans-serifs for modern, minimal designs

**Do's and Don'ts**

*Do's*
- Use sans-serifs as default for UI text
- Choose humanist or geometric sans-serifs for personality
- Test sans-serif rendering at all sizes
- Use sans-serifs for accessibility

*Don'ts*
- Mix too many sans-serif families
- Use poorly-hinted sans-serifs at small sizes
- Apply decorative sans-serifs to body text
- Ignore sans-serif optical sizing needs

**References**
- [NN/g: Typography Terms Glossary](https://www.nngroup.com/articles/typography-terms-ux/)
- [GeeksforGeeks: What is Typography in UI Design?](https://www.geeksforgeeks.org/what-is-typography-in-ui-design/)

---
## Satisfaction Metrics
**Category:** ux | **Type:** tool | **Tags:** research

Post-task ratings CSAT SUS SEQ.

**Examples**
- CSAT 4.2/5 after task
- SUS 82/100 benchmark
- SEQ 6.8/7 single ease
- Single Ease Question

**Do's and Don'ts**

*Do's*
- Context-specific timing
- Benchmark industry standards
- Multiple metric types
- Actionable follow-ups

*Don'ts*
- Generic satisfaction
- No benchmarking
- Single metric type
- No follow-up

**References**
- [MeasuringU: Satisfaction Metrics](https://measuringu.com/satisfaction-metrics/)
- [NN/g](https://nngroup.com/)

---
## SCAMPER
**Category:** strategy | **Type:** framework | **Tags:** ideation

A structured creativity framework using seven prompts to generate new ideas by modifying existing products or concepts: Substitute, Combine, Adapt, Modify, Put to another use, Eliminate, and Reverse. SCAMPER provides systematic questions to spark creative thinking.

**Examples**
- Using SCAMPER to reimagine an existing feature by asking "What if we combined checkout with product recommendations?"
- Applying SCAMPER questions to generate mobile app improvements

**Do's and Don'ts**

*Do's*
- Work through each letter systematically
- Apply multiple SCAMPER prompts to same problem
- Use concrete examples when answering prompts
- Combine SCAMPER with other ideation methods
- Document ideas generated from each prompt
- Adapt questions to your specific context

*Don'ts*
- Rush through the prompts superficially
- Skip prompts that seem less relevant
- Use SCAMPER on blank slate problems (works best with existing concepts)
- Apply only one or two prompts
- Expect all prompts to generate equally valuable ideas
- Use SCAMPER as the only ideation approach

**References**
- [Interaction Design Foundation: SCAMPER](https://www.interaction-design.org/literature/article/learn-how-to-use-the-best-ideation-methods-scamper)
- [MindTools: SCAMPER Technique](https://www.mindtools.com/ar5hrzy/scamper)

---
## Screen Reader
**Category:** ui | **Type:** tool | **Tags:** accessibility

Software reading content aloud for visually impaired users (VoiceOver, NVDA, JAWS).

**Examples**
- VoiceOver (iOS/macOS)
- NVDA (Windows, free)
- JAWS (Windows, commercial)
- TalkBack (Android)

**Do's and Don'ts**

*Do's*
- Test with real screen readers
- Use semantic HTML structure
- Support all common screen readers
- Train team on screen reader testing

*Don'ts*
- Test by looking at screen
- Skip landmark navigation
- Assume 'it reads fine'
- Test only one screen reader

**References**
- [WebAIM: Screen Reader Testing](https://webaim.org/techniques/screenreader/)
- [NVDA: Official Documentation](https://www.nvaccess.org/documentation/)

---
## Screen Reader Testing
**Category:** ux | **Type:** methodology | **Tags:** accessibility, testing

Manual testing with NVDA VoiceOver TalkBack.

**Examples**
- NVDA Chrome testing
- VoiceOver Safari iOS
- TalkBack Android
- 2hr focused session

**Do's and Don'ts**

*Do's*
- Real screen reader users
- Task-based testing
- All platform combinations
- Detailed bug reports

*Don'ts*
- Demo with screen reader
- Quick scan only
- Single platform
- No task context

**References**
- [WebAIM Articles](https://webaim.org/articles/)
- [Deque](https://www.deque.com/)

---
## Scroll Depth Tracking
**Category:** ux | **Type:** tool | **Tags:** analytics

Percentage users reaching content sections.

**Examples**
- 68% read past fold
- 23% full article scroll
- Mobile scroll 41%
- Engagement correlation

**Do's and Don'ts**

*Do's*
- Content performance proxy
- Device segmentation
- Time-on-page correlation
- Design optimization

*Don'ts*
- Above-fold only
- Desktop focus
- No device split
- No engagement link

**References**
- [Hotjar: Scrollmaps](https://www.hotjar.com/scrollmaps/)

---
## Search Schema
**Category:** ux | **Type:** methodology | **Tags:** information-architecture

Rules defining searchable content, indexing, and ranking.

**Examples**
- Products + pages + blog indexed
- Brand before category in results
- Popular before newest
- Spelling correction rules

**Do's and Don'ts**

*Do's*
- Define indexable content
- Weight by business goals
- Test ranking quality
- Document edge cases

*Don'ts*
- Index everything
- Alphabetical only
- No synonym handling
- Developer priorities

**References**
- [Search Engine Journal](https://www.searchenginejournal.com/)
- [Algolia](https://algolia.com/)

---
## Secondary Navigation
**Category:** ui | **Type:** pattern | **Tags:** navigation

Supporting navigation for sub-sections, categories, or context-specific links.

**Examples**
- Submenu under Products (Clothing, Electronics)
- Category filters on product page
- Sidebar with related articles
- Contextual links within content

**Do's and Don'ts**

*Do's*
- Keep contextually relevant
- Use clear visual hierarchy
- Support primary nav structure
- Responsive collapse/expand

*Don'ts*
- Duplicate primary nav content
- Overwhelm with too many options
- Inconsistent secondary patterns
- Hide without clear access

**References**
- [Material Design: Navigation Patterns](https://m3.material.io/foundations/layout/understanding-layout/overview)
- [Alooba: Navigation Patterns](https://www.alooba.com/skills/concepts/ux-design/navigation-patterns/)

---
## Semantic HTML
**Category:** ui | **Type:** principle | **Tags:** accessibility, web

Meaningful markup (headings, lists, landmarks) aiding assistive technology.

**Examples**
- <h1> to <h6> hierarchy
- <nav>, <main>, <aside> landmarks
- <ul>, <ol>, <dl> proper lists
- <button> vs <div> semantics

**Do's and Don'ts**

*Do's*
- Proper heading hierarchy
- ARIA landmark roles
- Native HTML controls
- Screen reader announces correctly

*Don'ts*
- <div role='button'>
- h3>h2 heading order
- <b> instead of <strong>
- Visual-only styling

**References**
- [WebAIM: Semantic Structure](https://webaim.org/techniques/semanticstructure/)
- [HTML5 Doctor: Semantics](http://html5doctor.com/)

---
## Semantic Landmarks
**Category:** ui | **Type:** pattern | **Tags:** accessibility

ARIA roles identify page regions.

**Examples**
- role=navigation sidebar
- role=main content
- role=search form
- role=banner header

**Do's and Don'ts**

*Do's*
- Semantic HTML preferred
- Single main landmark
- Screen reader validation
- Consistent landmark use

*Don'ts*
- Multiple mains
- Generic role=region
- No landmarks
- Visual-only landmarks

**References**
- [W3C: Landmarks Tutorial](https://www.w3.org/WAI/tutorials/landmarks/)
- [WebAIM](https://webaim.org/)

---
## SEO-First Content Markup
**Category:** strategy | **Type:** methodology | **Tags:** web, strategy

Semantic HTML optimized for search engine crawling.

**Examples**
- Semantic headings H1-H6
- Schema.org structured data
- alt text descriptive
- Canonical URL tags

**Do's and Don'ts**

*Do's*
- Semantic HTML5 elements
- Descriptive link text
- Proper heading hierarchy
- Schema.org vocabulary

*Don'ts*
- div soup markup
- Click here links
- H1 everywhere
- Missing structured data

**References**
- [Google Search Docs](https://developers.google.com/search/docs)
- [Schema.org](https://schema.org/)

---
## Serial Position Effect
**Category:** ux | **Type:** principle

Better recall of first and last items in sequence.

**Examples**
- Important CTA first + last
- Navigation: key items bookend
- List pricing high-low-high
- Stepper first/last emphasized

**Do's and Don'ts**

*Do's*
- Primacy items top position
- Recency items bottom position
- Middle items supporting role
- Visual emphasis endpoints

*Don'ts*
- Important items in middle
- Random list ordering
- Equal visual treatment
- No pattern recognition

**References**
- [NN/g: Serial Position Effect](https://www.nngroup.com/articles/serial-position-effect/)
- [UX Design CC](https://uxdesign.cc/)

---
## Serif Fonts
**Category:** ui | **Type:** concept | **Tags:** typography

Typefaces with small decorative strokes (serifs) extending from the ends of letters. Serifs add formality and tradition to typography and are often used for editorial content or formal applications.

**Examples**
- Using Georgia or Times New Roman for long-form article content
- Applying serif fonts for luxury brand websites
- Choosing Garamond for print-inspired digital publications
- Pairing serif headings with sans-serif body text

**Do's and Don'ts**

*Do's*
- Use serifs for long-form reading content
- Choose serifs for formal or traditional contexts
- Test serif legibility at small sizes
- Pair serifs thoughtfully with sans-serif fonts

*Don'ts*
- Overuse serifs in modern UI interfaces
- Use ornate serifs that reduce legibility
- Apply serifs to small technical text
- Mix too many serif and sans-serif fonts

**References**
- [NN/g: Typography Terms Glossary](https://www.nngroup.com/articles/typography-terms-ux/)
- [Designlab: What Is Typography And How Is It Important To UX & UI?](https://designlab.com/blog/what-is-typography)

---
## Session Duration
**Category:** ux | **Type:** tool | **Tags:** analytics

Average time spent per user session.

**Examples**
- Avg 4m32s session
- Engagement sessions >2min
- Power users 12m+ avg
- Feature session analysis

**Do's and Don'ts**

*Do's*
- Define session meaningful
- Segment by device type
- Track engagement sessions
- Correlate with outcomes

*Don'ts*
- Technical sessions only
- All sessions equal
- Ignore device differences
- Raw time reporting

**References**
- [Mixpanel: Session Duration](https://mixpanel.com/blog/session-duration/)

---
## Shake to Undo
**Category:** ui | **Type:** pattern | **Tags:** mobile, interaction

Device shake cancels recent destructive action.

**Examples**
- Shake after delete confirmation
- Undo send message
- Shake after form submission
- Multi-step undo stack

**Do's and Don'ts**

*Do's*
- Clear confirmation dialog
- Single shake detection
- Visual undo toast
- Timeout auto-dismiss

*Don'ts*
- Always enabled shaking
- No visual confirmation
- Undo unrelated actions
- Desktop keyboard only

**References**
- [Apple HIG: Undo](https://developer.apple.com/design/human-interface-guidelines/undo)
- [UX Design CC](https://uxdesign.cc/)

---
## Sitemap
**Category:** ux | **Type:** tool | **Tags:** information-architecture, documentation

Diagram showing all pages/screens and their relationships.

**Examples**
- Hierarchical tree of 150+ pages
- Mobile app screen relationships
- Ecommerce category drill-down
- Documentation section hierarchy

**Do's and Don'ts**

*Do's*
- Keep under 3 levels deep
- Include page descriptions
- Mark priority pages
- Version control changes

*Don'ts*
- Include every single page
- Make it developer-only
- Forget mobile structure
- Static PDF only

**References**
- [Screaming Frog SEO Spider](https://www.screamingfrog.co.uk/seo-spider/)
- [UX Planet](https://uxplanet.org/)

---
## Six Thinking Hats
**Category:** ux | **Type:** tool | **Tags:** ideation

De Bono's method using six perspectives for structured thinking.

**Examples**
- White hat: facts data
- Red hat: emotions intuition
- Black hat: risks caution
- Yellow hat: benefits optimism
- Green hat: creativity ideas
- Blue hat: process control

**Do's and Don'ts**

*Do's*
- All hats sequentially
- Full team same hat
- Time each perspective
- Document per hat

*Don'ts*
- Skip hats
- Mixed perspectives
- Dominant personalities
- Rush through colors

**References**
- [Edward de Bono](https://www.debono.com/)
- [Six Thinking Hats Book](https://www.penguinrandomhouse.com/)

---
## Skeleton Loading State
**Category:** ui | **Type:** pattern | **Tags:** interaction

Low-fidelity preview content structure while loading.

**Examples**
- Article skeleton layout
- Card grid placeholders
- Form field placeholders
- List item shimmer animation

**Do's and Don'ts**

*Do's*
- Match final content shape
- Consistent animation timing
- Accessibility labels
- Error state fallback

*Don'ts*
- Generic spinners everywhere
- Mismatched content ratios
- No accessibility
- Infinite loading

**References**
- [Invicta Design: Skeleton Screens](https://www.invicta-design.com/blog/skeleton-screens/)
- [UX Planet](https://uxplanet.org/)

---
## Smoke Testing
**Category:** ux | **Type:** methodology | **Tags:** testing, processes

Basic functionality verification immediately post-deploy.

**Examples**
- Homepage loads login works
- Core user flows functional
- Database connectivity ok
- 95% test suite passing

**Do's and Don'ts**

*Do's*
- Automated smoke suite
- CI/CD gate
- Production monitoring
- Rollback capability

*Don'ts*
- Manual smoke tests
- No automation
- Deploy without testing
- Ignore monitoring

**References**
- [Martin Fowler: Smoke Test](https://www.martinfowler.com/bliki/SmokeTest.html)
- [CircleCI](https://circleci.com/)

---
## Sort Order
**Category:** ux | **Type:** pattern | **Tags:** information-architecture

Default and alternate ordering rules for content lists.

**Examples**
- Featured > Popular > Newest > Price
- Alphabetical A-Z, Z-A
- Date Recent-Old, Old-Recent
- Rating High-Low

**Do's and Don'ts**

*Do's*
- Match user expectations
- Show current sort state
- Multiple options max 5
- URL parameter support

*Don'ts*
- Default alphabetical
- More than 6 options
- No visual feedback
- Confusing labels

**References**
- [NN/g Articles](https://www.nngroup.com/articles/)
- [Baymard Institute](https://baymard.com/)

---
## Spacing Scale
**Category:** ui | **Type:** principle | **Tags:** design-systems

Standardized set of spacing values (4px, 8px, 16px multiples) used consistently for margins, padding, and gaps throughout the interface.

**Examples**
- spacing-xs: 4px
- spacing-sm: 8px
- spacing-md: 16px
- spacing-xl: 32px

**Do's and Don'ts**

*Do's*
- Use multiples of base unit (4px or 8px)
- Define 6-8 scale steps
- Apply functionally (stack vs inline)
- Document rhythm relationships

*Don'ts*
- Use arbitrary pixel values
- Ignore responsive breakpoints
- Mix scales inconsistently
- Skip vertical rhythm planning

**References**
- [Material Design: Layout](https://m2.material.io/design/layout/understanding-layout.html)
- [Every Layout](https://every-layout.dev/)

---
## Speedboat Canvas
**Category:** ux | **Type:** tool | **Tags:** ideation

Visual metaphor identifying what slows team or product progress.

**Examples**
- Anchors as blockers
- Wind as accelerators
- Rocks as risks
- Destination as goal

**Do's and Don'ts**

*Do's*
- All team participates
- Prioritize anchors
- Action items from blockers
- Regular revisits

*Don'ts*
- Blame individuals
- Ignore small anchors
- Skip action planning
- One-time exercise only

**References**
- [Innovation Games](https://www.innovationgames.com/)
- [Gamestorming](https://gamestorming.com/)

---
## Sprint Planning Meeting
**Category:** management | **Type:** methodology | **Tags:** processes

2hr commitment planning session.

**Examples**
- Story point estimation
- 2-week sprint commitment
- Definition of Done review
- Daily standup schedule

**Do's and Don'ts**

*Do's*
- Product owner present
- Team velocity based
- Stories INVEST criteria
- Risks surfaced

*Don'ts*
- >4hr planning
- No product owner
- Story points ignored
- Commitments unrealistic

**References**
- [Atlassian: Sprint Planning](https://www.atlassian.com/agile/scrum/sprint-planning)
- [Scrum Guides](https://scrumguides.org/)

---
## Sprint Review Demo
**Category:** management | **Type:** methodology | **Tags:** processes

Stakeholder showcase working software.

**Examples**
- 8 stories completed demo'd
- Stakeholder feedback
- Updated backlog
- 1hr max duration

**Do's and Don'ts**

*Do's*
- Demo working software
- Invite all stakeholders
- Real user scenarios
- Document feedback

*Don'ts*
- Slide presentation
- Team-only review
- No stakeholder input
- >2hr duration

**References**
- [Scrum.org: Sprint Review](https://www.scrum.org/resources/blog/sprint-review)
- [Atlassian](https://atlassian.com/)

---
## Stacked Area Graph
**Category:** ui | **Type:** tool | **Tags:** data-visualization

Filled areas show contribution of parts to cumulative total over time.

**Examples**
- Revenue streams by product
- Website traffic by source
- Stacked sales by region
- Cumulative budget spending

**Do's and Don'ts**

*Do's*
- Consistent stacking order
- 100% scale when comparing
- Clear legend positioning
- Highlight total line

*Don'ts*
- Compare magnitudes across
- Too many stacked series
- Missing baseline
- Bright colors on dark

**References**
- [Visual Cinnamon](https://www.visualcinnamon.com/)
- [Information is Beautiful](https://informationisbeautiful.net/)

---
## Stakeholder Interviews
**Category:** ux | **Type:** methodology | **Tags:** research

Structured conversations with internal stakeholders to understand business goals, constraints, requirements, and perspectives. Stakeholder interviews align design work with organizational objectives and surface potential conflicts early.

**Examples**
- Interviewing product managers, engineers, and executives before starting discovery research
- Speaking with customer support teams to understand common user issues

**Do's and Don'ts**

*Do's*
- Interview stakeholders from diverse roles and departments
- Ask about goals, constraints, and success metrics
- Listen for conflicting priorities across stakeholders
- Document assumptions and requirements
- Conduct early in the project
- Use insights to inform research strategy

*Don'ts*
- Treat stakeholder opinions as user needs
- Skip stakeholder alignment in favor of only user research
- Interview only the project sponsor
- Ignore organizational politics and constraints
- Make promises you can't keep
- Let stakeholder preferences override user needs

**References**
- [Nielsen Norman Group: Stakeholder Interview Questions](https://www.nngroup.com/articles/stakeholder-interview-questions/)
- [UX Collective: Stakeholder Interviews](https://uxdesign.cc/how-to-conduct-stakeholder-interviews-a-guide-for-ux-designers-c5e4e4b3b6d8)

---
## Stakeholder Map
**Category:** strategy | **Type:** tool | **Tags:** strategy

Influence interest power prioritization matrix.

**Examples**
- VP Product: High power high interest
- Legal: High power low interest
- 23 stakeholders plotted
- Engagement strategy per quadrant

**Do's and Don'ts**

*Do's*
- Power x Interest matrix
- Regular stakeholder refresh
- Engagement plan per quadrant
- Cross-team validation

*Don'ts*
- Informal stakeholder list
- Never updated
- All treated equally
- Power assumed not assessed

**References**
- [ProductPlan: Stakeholder Mapping](https://www.productplan.com/glossary/stakeholder-mapping/)

---
## Starfish Retrospective
**Category:** management | **Type:** tool | **Tags:** ideation

Five-category retrospective: keep, more, less, stop, start.

**Examples**
- Keep daily standups
- More user testing
- Less meetings
- Stop scope creep
- Start documentation

**Do's and Don'ts**

*Do's*
- Equal time per category
- Specific examples
- Vote on priorities
- Create action items

*Don'ts*
- Skip categories
- Vague feedback
- No follow-through
- Blame-focused items

**References**
- [Atlassian: Retrospectives](https://www.atlassian.com/team-playbook/plays/retrospective)
- [Retromat](https://retromat.org/)

---
## Status Bar Behavior
**Category:** ui | **Type:** pattern | **Tags:** mobile

Top bar shows/hides based on scroll/content needs.

**Examples**
- Scroll away hides status
- Modal full-screen status
- Landscape orientation rules
- Notch-aware behavior

**Do's and Don'ts**

*Do's*
- Platform standard behavior
- Test all orientations
- Smooth hide/show animation
- Respect user preference

*Don'ts*
- Always hidden status
- Jarring show/hide
- Desktop title bar only
- Inconsistent behavior

**References**
- [Apple HIG: Status Bars](https://developer.apple.com/design/human-interface-guidelines/status-bars)
- [Material Design](https://m2.material.io/)

---
## Stepper
**Category:** ui | **Type:** pattern | **Tags:** navigation

Linear multi-step process navigation (Step 1 of 4).

**Examples**
- Checkout process (Cart > Address > Payment > Confirm)
- Onboarding wizard
- Form wizard
- Multi-step configuration

**Do's and Don'ts**

*Do's*
- Show progress clearly
- Allow back navigation
- Skip optional steps
- Mobile-responsive steppers

*Don'ts*
- No progress indication
- No back button
- Force linear progression
- Poor error recovery

**References**
- [Material Design: Steppers](https://m3.material.io/components/stepper/overview)
- [UXPin: Stepper Patterns](https://www.uxpin.com/studio/blog/ux-design-stepper/)

---
## Stickiness Ratio
**Category:** ux | **Type:** tool | **Tags:** analytics

DAU/MAU ratio measures daily engagement.

**Examples**
- DAU/MAU 18% industry 14%
- Power users 42% stickiness
- Feature stickiness matrix
- Cohort stickiness curves

**Do's and Don'ts**

*Do's*
- Track vs industry benchmarks
- Segment user types
- Feature-level analysis
- Historical trending

*Don'ts*
- Monthly average only
- All users equal
- No benchmarking
- Single timepoint

**References**
- [Amplitude: Stickiness](https://amplitude.com/blog/stickiness/)

---
## Sticky Navigation Bar
**Category:** ui | **Type:** pattern | **Tags:** web, navigation

Navigation stays fixed during scroll.

**Examples**
- Top nav sticky on scroll
- Sidebar sticky sections
- Mobile bottom nav sticky
- Threshold-based stickiness

**Do's and Don'ts**

*Do's*
- Smooth scroll transitions
- Z-index management
- Mobile viewport height
- Performance optimized

*Don'ts*
- Always sticky (flash)
- Blocks content
- Poor mobile handling
- Performance issues

**References**
- [CSS-Tricks: Position Sticky](https://css-tricks.com/position-sticky-and-table-headers/)
- [MDN](https://developer.mozilla.org/en-US/)

---
## Storytelling Arc
**Category:** strategy | **Type:** pattern | **Tags:** strategy

Problem solution impact narrative structure.

**Examples**
- Problem: Slow checkout
- Agitation: Cart abandonment
- Solution: 1-click checkout
- Proof: +23% conversion

**Do's and Don'ts**

*Do's*
- Problem Agitate Solve
- Customer story format
- Data proof points
- Emotional connection

*Don'ts*
- Feature presentation
- Jargon technical details
- No proof validation
- Team benefit focus

**References**
- [Product Talk: Storytelling for PMs](https://www.producttalk.org/2017/07/storytelling-for-product-managers/)
- [Storytelling with Data](https://storytellingwithdata.com/)

---
## Style Guide
**Category:** ui | **Type:** tool | **Tags:** design-systems, documentation

Comprehensive reference document detailing visual, interaction, and content guidelines for consistent design application.

**Examples**
- Color palette with usage rules
- Typography scale with pairing guide
- Component anatomy diagrams
- Iconography principles and library

**Do's and Don'ts**

*Do's*
- Make accessible and searchable
- Include code examples
- Update with version history
- Include dos/don'ts examples

*Don'ts*
- Create as static PDF only
- Ignore developer needs
- Let it become outdated
- Make it design-only focused

**References**
- [Figma: Style Guide Best Practices](https://www.figma.com/best-practices/style-guide/)
- [Living Style Guide](https://livingstyleguide.org/)

---
## Surveys
**Category:** ux | **Type:** methodology | **Tags:** research

A structured research method using questionnaires to collect quantitative and qualitative data from a large number of respondents. Surveys measure attitudes, behaviors, satisfaction, and demographics across representative samples.

**Examples**
- Sending a post-purchase survey to measure customer satisfaction with checkout experience
- Running an annual user survey to understand feature priorities and usage patterns

**Do's and Don'ts**

*Do's*
- Start with clear research objectives
- Use validated scales when possible
- Keep surveys concise and focused
- Pilot test before launching widely
- Include a mix of question types
- Ensure response options are mutually exclusive and comprehensive

*Don'ts*
- Ask leading or biased questions
- Make surveys too long
- Use jargon or complex language
- Ask two questions in one
- Rely on surveys alone for decision-making
- Survey too frequently

**References**
- [Nielsen Norman Group: Survey Design](https://www.nngroup.com/articles/survey-design/)
- [Qualtrics: Survey Research Guide](https://www.qualtrics.com/experience-management/research/survey-research/)

---
## SUS Questionnaire
**Category:** ux | **Type:** tool | **Tags:** research, testing

10-question standardized usability scale benchmark.

**Examples**
- SUS score 82/100
- Benchmark vs industry 68
- Pre/post redesign comparison
- Cross-product comparison

**Do's and Don'ts**

*Do's*
- Always 10 questions
- Alternate odd/even first
- Benchmark against norms
- Report confidence intervals

*Don'ts*
- Modified SUS questions
- Single administration
- No industry benchmarking
- Ignore response patterns

**References**
- [MeasuringU: SUS](https://measuringu.com/sus/)
- [Usability Net](https://www.usabilitynet.org/)

---
## SUS Score
**Category:** ux | **Type:** tool | **Tags:** analytics, research

10-question standardized usability benchmark 0-100.

**Examples**
- SUS 82 vs industry 68
- Pre-post redesign delta
- Cross-product comparison
- Confidence intervals

**Do's and Don'ts**

*Do's*
- Full 10 questions always
- Industry benchmarking
- Alternate odd/even order
- Large sample 20+

*Don'ts*
- Modified questions
- Single administration
- No benchmarking
- Small sample

**References**
- [MeasuringU: SUS](https://measuringu.com/sus/)
- [UsabilityNet](https://usabilitynet.org/)

---
## Tab Bar
**Category:** ui | **Type:** pattern | **Tags:** navigation

Horizontal tabs switching between related content views (Content 1 | Content 2).

**Examples**
- Details | Reviews | Shipping tabs
- Inbox | Sent | Drafts
- Profile | Activity | Settings
- Categories within section

**Do's and Don'ts**

*Do's*
- Related, equal-importance content
- Clear active/inactive states
- Consistent tab sizing
- Touch target minimums

*Don'ts*
- Hierarchy/content priority
- More than 5 tabs
- Nested tab structures
- Unrelated tab content

**References**
- [NN/g: Tab Patterns](https://www.nngroup.com/articles/tabs-used-right/)
- [Material Design: Tabs](https://m3.material.io/components/tabs/overview)

---
## Tagging System
**Category:** ux | **Type:** methodology | **Tags:** information-architecture

Descriptive keywords assigned to content for findability.

**Examples**
- Post tagged: ux, research, testing
- Product: wireless, bluetooth, earbuds
- Support article: billing, credit-card
- Design file: mobile, onboarding

**Do's and Don'ts**

*Do's*
- Consistent tag formats
- Limit 5-8 per item
- Hierarchical when needed
- User testing validation

*Don'ts*
- Free-for-all tagging
- Overly specific tags
- No tag guidelines
- Hidden from users

**References**
- [Content Strategy Inc](https://www.contentstrategyinc.com/)
- [NN/g](https://nngroup.com/)

---
## Task Completion Testing
**Category:** ux | **Type:** methodology | **Tags:** testing

Success rates time-on-task metrics measurement.

**Examples**
- 87% checkout success 2m23s
- 64% form completion 1m18s
- Error-free task completion
- Confidence rating scale

**Do's and Don'ts**

*Do's*
- 3-5 realistic tasks
- Time on task recording
- Error classification
- SUS questionnaire follow-up

*Don'ts*
- Unrealistic lab tasks
- No error categorization
- Single task only
- No confidence ratings

**References**
- [MeasuringU: Task Success](https://www.measuringu.com/task-success/)
- [NN/g](https://www.nngroup.com/)

---
## Task Flow
**Category:** ux | **Type:** methodology | **Tags:** information-architecture

Simplified flow focusing on a single user goal and decision points.

**Examples**
- Reset password: email > code > new pw
- Book appointment: date > time > confirm
- Upload file: select > preview > submit
- Cancel subscription flow

**Do's and Don'ts**

*Do's*
- Limit to 3-5 steps
- Highlight decision points
- Include error states
- Test completion rates

*Don'ts*
- Include account setup
- Show full application flow
- Complex branching logic
- No validation testing

**References**
- [Interaction Design Foundation](https://www.interaction-design.org/)
- [Whimsical](https://whimsical.com/)

---
## Task Success Rate
**Category:** ux | **Type:** methodology | **Tags:** research, testing

Percentage completing tasks without assistance.

**Examples**
- 87% found product category
- 64% completed checkout
- 92% navigation success
- 45% form completion rate

**Do's and Don'ts**

*Do's*
- Clear success criteria
- Time on task measurement
- Error rate correlation
- Confidence rating follow-up

*Don'ts*
- Subjective success judgment
- No time measurement
- Assisted completion counted
- Single task metric

**References**
- [MeasuringU: Task Success](https://www.measuringu.com/task-success/)
- [NN/g](https://www.nngroup.com/)

---
## Taxonomy
**Category:** ux | **Type:** methodology | **Tags:** information-architecture

Controlled vocabulary and classification system for content.

**Examples**
- Product categories: shoes > sneakers > running
- Support docs: billing > payments > refunds
- Knowledge base topic tree
- Ecommerce facet hierarchy

**Do's and Don'ts**

*Do's*
- Use singular consistent terms
- Allow 1-2 parents per item
- Document relationships
- Test findability

*Don'ts*
- Free-for-all categories
- Deep nesting >3 levels
- Inconsistent pluralization
- No cross-references

**References**
- [Taxonomy Warehouse](https://www.taxonomywarehouse.com/)
- [NN/g](https://nngroup.com/)

---
## Team OKR Cascading
**Category:** management | **Type:** methodology | **Tags:** strategy

Company → team → individual objective connection.

**Examples**
- Company: Double MAU
- Team: Improve onboarding 30%
- Individual: Onboarding NPS +15
- Quarterly alignment

**Do's and Don'ts**

*Do's*
- Line-of-sight connection
- 3-5 team OKRs
- Individual contribution clear
- Regular check-ins

*Don'ts*
- Siloed individual OKRs
- Too many OKRs
- No company connection
- Annual alignment

**References**
- [What Matters: OKR Alignment](https://www.whatmatters.com/guides/okr-alignment)
- [re:Work](https://rework.withgoogle.com/)

---
## Test Scenario Development
**Category:** ux | **Type:** methodology | **Tags:** testing, processes

Realistic user goal-based tasks for testing.

**Examples**
- 'Book flight under $300'
- 'Cancel existing reservation'
- 'Find vegan restaurant nearby'
- 'Update payment method'

**Do's and Don'ts**

*Do's*
- Real user goals
- Representative data
- Edge cases included
- Success criteria defined

*Don'ts*
- Click-this-button tasks
- Admin-only scenarios
- Perfect data assumptions
- Vague success criteria

**References**
- [NN/g: Test Scenarios](https://www.nngroup.com/articles/test-scenarios/)
- [Usability.gov](https://www.usability.gov/)

---
## Text Alignment
**Category:** ui | **Type:** tool | **Tags:** typography

Positioning of text relative to margins or guides: left-aligned, center-aligned, right-aligned, or justified. Text alignment affects readability, visual flow, and information hierarchy in UI layouts.

**Examples**
- Left-aligning body text for optimal readability
- Center-aligning headlines and hero text
- Right-aligning numbers in data tables for easy comparison
- Using justified text in print-inspired editorial layouts

**Do's and Don'ts**

*Do's*
- Use left-alignment for body text (most readable)
- Center-align headlines and display text
- Use justified text only for specific editorial contexts
- Maintain consistent alignment within content blocks

*Don'ts*
- Justify body text on screens (causes uneven spacing)
- Right-align body text (difficult to read)
- Mix alignment styles randomly
- Use center alignment for lengthy paragraphs

**References**
- [UX Planet: Principles of Typography in UI Design](https://uxplanet.org/principles-of-typography-in-ui-design)
- [Interaction Design Foundation: The UX Designer's Guide to Typography](https://www.interaction-design.org/literature/article/the-ux-designer-s-guide-to-typography)

---
## Text Alternative
**Category:** ui | **Type:** principle | **Tags:** accessibility

Non-visual descriptions for images/media (alt text, captions).

**Examples**
- alt='Profile avatar of John Doe'
- Decorative images: alt=''
- Complex charts: longdesc
- Video captions + transcripts

**Do's and Don'ts**

*Do's*
- Descriptive alt text
- Empty alt for decorative
- Long descriptions for charts
- Audio descriptions video

*Don'ts*
- alt='image.jpg'
- Missing alt attributes
- Generic 'logo' descriptions
- No caption transcripts

**References**
- [WCAG 1.1.1: Non-text Content](https://www.w3.org/WAI/WCAG21/Understanding/non-text-content.html)
- [WebAIM: Alt Text Guide](https://webaim.org/techniques/alttext/)

---
## Text Resizing
**Category:** ui | **Type:** principle | **Tags:** accessibility, typography

Content readable up to 200% zoom without loss of functionality.

**Examples**
- 200% browser zoom works
- Responsive viewport scaling
- No horizontal scroll
- Functionality preserved

**Do's and Don'ts**

*Do's*
- Test 200%, 400% zoom
- Responsive units (rem/em)
- Proper viewport meta tag
- No fixed heights/widths

*Don'ts*
- Fixed pixel font sizes
- Break at 200% zoom
- Horizontal scroll needed
- Lost functionality

**References**
- [WCAG 1.4.4: Resize Text](https://www.w3.org/WAI/WCAG21/Understanding/resize-text.html)
- [WebAIM: Zoom Testing](https://webaim.org/techniques/responsive/)

---
## Thematic Analysis
**Category:** ux | **Type:** methodology | **Tags:** research

A qualitative research method for identifying, analyzing, and reporting patterns (themes) within data. Thematic analysis systematically organizes and describes research findings by coding data and grouping codes into meaningful themes.

**Examples**
- Analyzing 20 user interview transcripts to identify recurring pain points and needs
- Coding survey open-ended responses to find patterns in customer feedback

**Do's and Don'ts**

*Do's*
- Familiarize yourself with the data through multiple readings
- Code data systematically with clear definitions
- Look for patterns and themes across the dataset
- Involve multiple researchers when possible
- Document your coding process and decisions
- Validate themes against original data

*Don'ts*
- Start coding without understanding the full dataset
- Force data to fit preconceived themes
- Ignore outliers and contradictory data
- Use overly broad or vague themes
- Skip reviewing and refining themes
- Work in isolation without peer review

**References**
- [Nielsen Norman Group: Thematic Analysis](https://www.nngroup.com/articles/thematic-analysis/)
- [Interaction Design Foundation: Thematic Analysis](https://www.interaction-design.org/literature/article/how-to-do-a-thematic-analysis-of-user-interviews)

---
## Think-Aloud Protocol
**Category:** ux | **Type:** methodology | **Tags:** research, testing

Users verbalize thoughts while completing tasks.

**Examples**
- 'I'm clicking this because...'
- 'Can't find the button because...'
- 'Prefer this layout since...'
- Real-time problem discovery

**Do's and Don'ts**

*Do's*
- Concurrent verbalization
- Don't explain why
- Probe gently if silent
- Record everything

*Don'ts*
- Retrospective explanation
- Lead user thinking
- Interrupt flow
- Silent observation only

**References**
- [NN/g: Thinking Aloud](https://www.nngroup.com/articles/thinking-aloud/)
- [MeasuringU](https://measuringu.com/)

---
## Time on Task
**Category:** ux | **Type:** tool | **Tags:** analytics, testing

Average completion time standard tasks.

**Examples**
- Checkout 2m18s benchmark 3m
- Onboarding 4m12s
- Search to purchase 1m42s
- Mobile vs desktop delta

**Do's and Don'ts**

*Do's*
- Realistic benchmark tasks
- First-time user baseline
- Platform comparison
- Learnability improvement

*Don'ts*
- Lab-only timing
- Expert user baseline
- No platform comparison
- Average all tasks

**References**
- [NN/g: Time on Task](https://www.nngroup.com/articles/time-task/)
- [MeasuringU](https://measuringu.com/)

---
## Touch Target
**Category:** ui | **Type:** principle | **Tags:** interaction, mobile

Minimum interactive area size for comfortable finger interaction.

**Examples**
- 44x44px minimum (iOS)
- 48x48dp minimum (Android)
- 9mm physical size minimum
- Adequate spacing between targets

**Do's and Don'ts**

*Do's*
- Minimum 44px touch targets
- Adequate target spacing
- Test on actual devices
- Responsive target scaling

*Don'ts*
- Targets smaller than 44px
- Overlapping touch targets
- Inconsistent target sizing
- Ignore finger precision

**References**
- [Apple HIG: Touch Target Size](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Material Design: Touch Targets](https://m3.material.io/foundations/accessible-design/accessibility-basics)

---
## Tree Testing
**Category:** ux | **Type:** methodology | **Tags:** testing, navigation

A usability method that evaluates the findability and labeling of topics in a navigation structure by asking participants to locate items in a text-only hierarchy. Tree testing validates information architecture before visual design.

**Examples**
- Testing a website's navigation structure to see if users can find "Return Policy" in the menu hierarchy
- Validating app navigation by having users locate features using only the menu structure

**Do's and Don'ts**

*Do's*
- Test before investing in visual design
- Use realistic task scenarios
- Test with 30-50 participants for reliable data
- Measure success rate, directness, and time
- Compare multiple navigation structures
- Iterate based on results

*Don'ts*
- Include visual design or branding
- Use vague or ambiguous task descriptions
- Test with internal stakeholders only
- Rely on tree testing alone
- Skip validation after changes
- Make navigation too deep without testing

**References**
- [Nielsen Norman Group: Tree Testing](https://www.nngroup.com/articles/tree-testing/)
- [Optimal Workshop: Tree Testing Guide](https://www.optimalworkshop.com/learn/101s/tree-testing/)

---
## Type Scale
**Category:** ui | **Type:** tool | **Tags:** typography, design-systems

A system of font sizes based on mathematical ratios (e.g., 1.125, 1.25, 1.618) for consistent sizing across UI elements. Type scale ensures visual hierarchy and coherence without arbitrary font size choices.

**Examples**
- Using a 1.25 (major third) ratio to generate heading sizes from body text
- Implementing a modular scale: 12, 15, 19, 24, 30, 37px
- Applying golden ratio (1.618) for dramatic size differences in editorial design
- Documenting type scale in a design system for consistent usage

**Do's and Don'ts**

*Do's*
- Use established ratios (golden ratio 1.618, major third 1.25, minor third 1.125)
- Document type scale in design systems
- Apply type scale consistently across all components
- Scale type responsively for mobile and desktop

*Don'ts*
- Use arbitrary font sizes without ratios
- Create type scales with too many steps
- Ignore type scale in responsive design
- Break type scale for special cases without documenting

**References**
- [Material Design 3: Typography](https://m3.material.io/styles/typography)
- [UX Design Institute: Typography Best Practices](https://www.uxdesigninstitute.com/blog/typography-best-practices/)

---
## Typography Baseline
**Category:** ui | **Type:** concept | **Tags:** typography

Imaginary line upon which letters sit, serving as a reference for alignment. Baseline is fundamental for vertical rhythm and text alignment in UI layouts.

**Examples**
- Aligning text across multiple columns to a shared baseline grid
- Using baseline alignment to create visual harmony in card layouts
- Establishing an 8px baseline grid for consistent vertical spacing
- Aligning icons and text to a common baseline

**Do's and Don'ts**

*Do's*
- Align all text to a consistent baseline grid
- Use baseline grid for multi-line text blocks
- Maintain baseline alignment across different font sizes
- Apply baseline alignment in design systems

*Don'ts*
- Ignore baseline alignment in layouts
- Mix text with different baseline positions
- Use visual alignment instead of grid-based alignment
- Forget baseline impact on vertical rhythm

**References**
- [FlowMapp: 20 Basic Typographic Terms for UI Designers](https://www.flowmapp.com/blog/typographic-terms)
- [Interaction Design Foundation: The UX Designer's Guide to Typography](https://www.interaction-design.org/literature/article/the-ux-designer-s-guide-to-typography)

---
## Typography Contrast
**Category:** ui | **Type:** principle | **Tags:** typography, visual-hierarchy

Difference in weight, size, color, or style between typographic elements. Contrast creates visual interest, guides focus, and establishes hierarchy to improve scannability and user comprehension.

**Examples**
- Pairing a bold headline with light body text
- Using size contrast between H1 and H2 headings
- Applying color contrast between primary and secondary text
- Combining serif headings with sans-serif body for stylistic contrast

**Do's and Don'ts**

*Do's*
- Use high contrast for key information
- Combine multiple contrast dimensions (size + weight + color)
- Ensure sufficient contrast for accessibility (WCAG AA minimum)
- Apply contrast strategically throughout interface

*Don'ts*
- Use low contrast that reduces readability
- Create too many contrast levels (overwhelming)
- Ignore accessibility contrast requirements
- Use contrast solely for decoration

**References**
- [UX Planet: Principles of Typography in UI Design](https://uxplanet.org/principles-of-typography-in-ui-design)
- [W3C: WCAG 2.1 Contrast Requirements](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)

---
## Typography Legibility
**Category:** ui | **Type:** principle | **Tags:** typography, accessibility

Ease of distinguishing individual characters from one another. Legibility depends on font design, size, spacing, and contrast. High legibility is essential for accessible, user-friendly interfaces.

**Examples**
- Choosing fonts where 'I', 'l', and '1' are clearly distinguishable
- Testing character clarity at small sizes (12-14px)
- Ensuring adequate contrast between text and background
- Selecting fonts with open apertures for better character recognition

**Do's and Don'ts**

*Do's*
- Choose fonts with clear character distinction
- Use adequate font size (minimum 12px for body text)
- Ensure sufficient contrast (WCAG AA: 4.5:1 for normal text)
- Test legibility at actual usage sizes

*Don'ts*
- Use overly decorative fonts for body text
- Use font sizes below 12px for extended reading
- Use low contrast (fails accessibility standards)
- Ignore individual character clarity

**References**
- [NN/g: Typography Terms Glossary](https://www.nngroup.com/articles/typography-terms-ux/)
- [W3C: WCAG 2.1 Contrast Requirements](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)

---
## Typography Readability
**Category:** ui | **Type:** principle | **Tags:** typography, accessibility

Ease of reading and comprehending blocks of text. Readability encompasses legibility, line length, line height, color contrast, and overall layout. It measures how comfortably users can consume content.

**Examples**
- Setting optimal line height (1.5x) for comfortable paragraph reading
- Maintaining 50-60 characters per line for body text
- Using sufficient contrast between text and background
- Adding adequate spacing between paragraphs

**Do's and Don'ts**

*Do's*
- Use adequate line height (1.4-1.6x for web)
- Maintain optimal line length (45-75 characters)
- Use high contrast for text and background
- Add sufficient margins and padding around text

*Don'ts*
- Use cramped line spacing
- Use excessively long or short lines
- Use low-contrast text
- Ignore paragraph spacing and margins

**References**
- [UX Planet: Principles of Typography in UI Design](https://uxplanet.org/principles-of-typography-in-ui-design)
- [Interaction Design Foundation: The UX Designer's Guide to Typography](https://www.interaction-design.org/literature/article/the-ux-designer-s-guide-to-typography)

---
## Typography Rhythm
**Category:** ui | **Type:** principle | **Tags:** typography

Consistent vertical flow and spacing created by leading, line height, and baseline grids. Rhythm creates visual harmony, improves scanability, and establishes visual continuity across typography.

**Examples**
- Establishing an 8px baseline grid for all text elements
- Maintaining consistent spacing between paragraphs and headings
- Aligning text across multiple columns to the same vertical rhythm
- Using multiples of base unit for all vertical spacing

**Do's and Don'ts**

*Do's*
- Establish consistent vertical rhythm with baseline grids
- Apply rhythm consistently across all text elements
- Use rhythm to guide visual flow
- Scale rhythm proportionally for responsive design

*Don'ts*
- Break rhythm for visual variation
- Use inconsistent spacing between text blocks
- Ignore rhythm in mobile layouts
- Create too complex rhythm systems

**References**
- [UX Design Institute: Typography Best Practices](https://www.uxdesigninstitute.com/blog/typography-best-practices/)
- [Marketer-UX: Typography in UI/UX Design](https://marketer-ux.com/typography-in-ui-ux-design/)

---
## UI Transition
**Category:** ui | **Type:** tool | **Tags:** interaction

Smooth property change between states (color, position, opacity) with duration and easing.

**Examples**
- Button color transition 200ms ease
- Modal fade-in 300ms cubic-bezier
- Menu slide 400ms ease-out
- Scale transition on hover

**Do's and Don'ts**

*Do's*
- Use appropriate easing curves
- Match duration to distance
- Limit concurrent transitions
- Test 60fps performance

*Don'ts*
- Abrupt state changes
- Long transitions (>500ms)
- Competing transitions
- Generic easing everywhere

**References**
- [CSS-Tricks: CSS Transitions](https://css-tricks.com/almanac/properties/t/transition/)
- [Material Design: Motion](https://m3.material.io/styles/motion/overview)

---
## Usability Testing
**Category:** ux | **Type:** methodology | **Tags:** testing

A research method where representative users attempt realistic tasks with a product or prototype while observers watch, listen, and take notes. Usability testing reveals where users struggle, identifying design problems and opportunities for improvement.

**Examples**
- Watching 5-8 users complete a checkout process to identify friction points and errors
- Testing a mobile app's navigation by having users find specific features while thinking aloud

**Do's and Don'ts**

*Do's*
- Test with 5-8 users per round for best ROI
- Use realistic tasks that match actual use cases
- Encourage thinking aloud during tasks
- Observe without helping or explaining
- Take notes on behavior, not just opinions
- Test iteratively throughout development

*Don'ts*
- Test with too many users in one round
- Help users or explain how things work
- Ask leading questions during tasks
- Rely only on post-task surveys
- Test only once at the end
- Ignore small usability issues

**References**
- [Nielsen Norman Group: Usability Testing 101](https://www.nngroup.com/articles/usability-testing-101/)
- [Nielsen Norman Group: Why You Only Need to Test with 5 Users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/)

---
## Usage Guidelines
**Category:** ui | **Type:** tool | **Tags:** documentation, design-systems

Rules explaining when and how to apply specific design elements correctly.

**Examples**
- When to use primary vs secondary buttons
- Icon sizing relative to text
- Color usage by importance hierarchy
- Spacing rules for different contexts

**Do's and Don'ts**

*Do's*
- Use plain language
- Include visual examples
- Cover common mistakes
- Link to related guidelines

*Don'ts*
- Write legal-style rules
- Only say what not to do
- Assume designer knowledge
- No visual examples

**References**
- [Design Systems Guidelines](https://www.designsystems.com/guidelines/)
- [Buefy](https://buefy.org/)

---
## User Flow
**Category:** ux | **Type:** methodology | **Tags:** 

Ordered sequence of steps a user takes to accomplish a task.

**Examples**
- Checkout: cart > shipping > payment > confirm
- Onboarding: signup > preferences > tutorial
- Search to purchase flow
- Support ticket creation

**Do's and Don'ts**

*Do's*
- Include decision points
- Show error recovery paths
- Test with real users
- Document assumptions

*Don'ts*
- Linear happy path only
- Developer task focus
- More than 7 steps
- No mobile validation

**References**
- [NN/g: User Flows](https://www.nngroup.com/articles/user-flows/)

---
## User Interviews
**Category:** ux | **Type:** methodology | **Tags:** research

One-on-one conversations with users to understand their needs, behaviors, motivations, and pain points. User interviews collect qualitative data through open-ended questions and are typically conducted in the early discovery stages or to complement other research methods.

**Examples**
- Conducting 30-minute interviews with 8-10 target users to understand their daily workflows before designing a productivity app
- Speaking with customers who recently churned to identify usability issues and unmet needs
- Interviewing expert users to uncover advanced use cases and feature requests
- Running discovery interviews with potential users to validate problem space before building

**Do's and Don'ts**

*Do's*
- Ask open-ended questions that encourage storytelling
- Listen more than you talk (80/20 rule)
- Follow up on interesting responses with "why" and "tell me more"
- Record sessions (with permission) to capture nuances
- Take notes on body language and emotional reactions
- Prepare a discussion guide but remain flexible

*Don'ts*
- Ask leading questions that bias responses
- Jump to solutions during the interview
- Interview only power users or only novices
- Rely on what users say they want instead of observing behavior
- Conduct interviews without clear research objectives
- Skip synthesis and analysis after interviews

**References**
- [Nielsen Norman Group: User Interviews 101](https://www.nngroup.com/articles/user-interviews/)
- [Nielsen Norman Group: 5 Qualitative Research Methods](https://www.nngroup.com/videos/5-qualitative-research-methods/)
- [Interaction Design Foundation: How to Conduct User Interviews](https://www.interaction-design.org/literature/article/how-to-conduct-user-interviews)

---
## UX Style Guide
**Category:** ui | **Type:** tool | **Tags:** documentation, design-systems

Standards for user flows, microcopy, and interaction consistency.

**Examples**
- Error message tone guidelines
- Loading state patterns
- Success confirmation flows
- Progressive disclosure rules

**Do's and Don'ts**

*Do's*
- Cover tone and voice
- Document all user states
- Include microcopy examples
- Specify feedback timing

*Don'ts*
- Focus only on visuals
- Generic placeholder text
- Ignore error states
- Desktop only

**References**
- [NN/g: Style Guides](https://www.nngroup.com/articles/style-guides/)
- [UX Design](https://uxdesign.cc/)

---
## Value Proposition Testing
**Category:** strategy | **Type:** methodology | **Tags:** strategy, testing

Validate product-market assumptions experiments.

**Examples**
- Landing page test
- 247 signups 7-day waitlist
- Concierge MVP test
- Wizard of Oz experiment

**Do's and Don'ts**

*Do's*
- Riskiest assumption first
- Quantitative measure
- Timeboxed experiment
- Clear success criteria

*Don'ts*
- Feature testing only
- Qualitative only
- Unlimited experiment time
- Safe assumptions

**References**
- [Strategyzer: Testing Value Propositions](https://strategyzer.com/library/testing-value-propositions)
- [Lean Stack](https://leanstack.com/)

---
## Value vs Effort Matrix
**Category:** strategy | **Type:** framework | **Tags:** strategy

A 2x2 prioritization framework plotting initiatives based on their expected value to users or business and the effort required to implement. Also called Impact-Effort Matrix, it helps identify quick wins and avoid low-value, high-effort work.

**Examples**
- Plotting feature requests on a matrix to identify "quick wins" (high value, low effort) for next sprint
- Using the matrix to explain why certain high-effort, low-value features should be deprioritized

**Do's and Don'ts**

*Do's*
- Involve cross-functional teams in scoring
- Use relative rather than absolute scoring
- Focus on the quadrants (quick wins, big bets, fill-ins, time sinks)
- Revisit and update the matrix regularly
- Consider value to both users and business
- Use the matrix to facilitate prioritization discussions

*Don'ts*
- Spend too much time on precise scoring
- Only do "quick wins" and ignore strategic big bets
- Let personal preferences bias value estimates
- Ignore the "time sinks" quadrant (low value, high effort)
- Make the matrix overly complex
- Use effort alone as the deciding factor

**References**
- [Nielsen Norman Group: Prioritization Matrices](https://www.nngroup.com/articles/prioritization-matrices/)
- [Interaction Design Foundation: Value vs Complexity Matrix](https://www.interaction-design.org/literature/article/the-value-vs-complexity-matrix-a-prioritization-tool-that-works)

---
## Variable Fonts
**Category:** ui | **Type:** tool | **Tags:** typography

Single font file multiple weights widths styles.

**Examples**
- var(--font-weight, 100-900)
- Variable axis animation
- Weight gradient text
- Compact font loading

**Do's and Don'ts**

*Do's*
- Single font file optimized
- Axis ranges documented
- Fallback static weights
- Performance testing

*Don'ts*
- Multiple static files
- Unsupported browser ignore
- Over-animated variable
- No performance gain

**References**
- [Variable Fonts](https://variablefonts.typenetwork.com/)
- [Google Developers](https://developers.google.com/)

---
## Version Documentation
**Category:** ui | **Type:** tool | **Tags:** documentation, design-systems, processes

Changelog and migration guides for design system updates.

**Examples**
- v2.0: New spacing scale
- Breaking: color-primary renamed
- Migration script provided
- Deprecated components listed

**Do's and Don'ts**

*Do's*
- Clear migration paths
- Automated changelog
- Backward compatibility notes
- Release candidate previews

*Don'ts*
- Buried in commit messages
- No migration support
- Silent breaking changes
- Version numbers only

**References**
- [Keep a Changelog](https://keepachangelog.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---
## View Transitions API
**Category:** ui | **Type:** tool | **Tags:** web, interaction

Declarative page transition animations.

**Examples**
- view-transition-name: hero
- Smooth DOM element transitions
- SPA-like page changes
- Cross-document transitions

**Do's and Don'ts**

*Do's*
- Semantic transition names
- Performance budget respect
- Reduced motion compliant
- Fallback smooth scroll

*Don'ts*
- Animate everything
- Performance regressions
- No reduced motion
- Complex naming

**References**
- [Chrome: View Transitions](https://developer.chrome.com/docs/web-platform/view-transition/)
- [CSS-Tricks](https://css-tricks.com/)

---
## Viewport Meta Tag
**Category:** ui | **Type:** tool | **Tags:** web, mobile

HTML tag controlling mobile zoom scaling behavior.

**Examples**
- <meta name=viewport content=width=device-width initial-scale=1>
- maximum-scale=1.0 user-scalable=no
- viewport-fit=cover iPhone X
- width=device-width shrink-to-fit=no

**Do's and Don'ts**

*Do's*
- Always include viewport tag
- Test zoom behavior
- Support pinch-zoom
- Document mobile behavior

*Don'ts*
- Omit viewport tag
- Disable all zooming
- Fixed scale=1.0 only
- Ignore Safari iOS quirks

**References**
- [MDN: Viewport Meta Tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag)
- [CSS-Tricks: Viewport Meta Tag](https://css-tricks.com/snippets/html/viewport-metatag/)

---
## Viral Coefficient
**Category:** ux | **Type:** tool | **Tags:** analytics, strategy

Average new users per existing user referral.

**Examples**
- k-factor 1.2 growth
- Organic 23% acquisition
- Channel-specific viral
- Time decay analysis

**Do's and Don'ts**

*Do's*
- Track by acquisition channel
- Time-decay modeling
- >1.0 growth target
- Sustainable viral loops

*Don'ts*
- All channels averaged
- No time decay
- Short-term spikes only
- Ignore sustainability

**References**
- [Reforge: Viral Loops Metrics](https://www.reforge.com/guides/viral-loops-metrics)
- [GrowthHackers](https://growthhackers.com/)

---
## Visual Hierarchy
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy

Size position color organize content by importance.

**Examples**
- H1 48px > H2 32px > body 16px
- Primary CTA largest button
- Hero section viewport height
- Supporting content smaller

**Do's and Don'ts**

*Do's*
- Largest = most important
- F-pattern scanning layout
- Consistent hierarchy system
- Test eye tracking patterns

*Don'ts*
- Equal font sizes
- Decorative elements largest
- Bottom-up information flow
- Inconsistent sizing

**References**
- [NN/g: Visual Hierarchy](https://www.nngroup.com/articles/visual-hierarchy/)
- [UX Movement](https://uxmovement.com/)

---
## Visual Hierarchy Priority
**Category:** ui | **Type:** principle | **Tags:** data-visualization, visual-hierarchy

Size position color prioritize most important data elements.

**Examples**
- KPI largest font top-left
- Secondary metrics smaller
- Detail charts bottom-right
- Context last

**Do's and Don'ts**

*Do's*
- Eye tracking F-pattern
- Largest = most important
- Consistent across dashboard
- Test scan effectiveness

*Don'ts*
- Equal visual weights
- Decorative elements largest
- Text hierarchy reversed
- Bottom-heavy layout

**References**
- [NN/g: Visual Hierarchy](https://www.nngroup.com/articles/visual-hierarchy/)
- [UX Movement](https://uxmovement.com/)

---
## Visual Language Guide
**Category:** ui | **Type:** tool | **Tags:** documentation, iconography

Rules for icons, illustrations, and graphical element usage.

**Examples**
- Icon weight matching typography
- Illustration style mood board
- Metaphor consistency rules
- Diagram type selection guide

**Do's and Don'ts**

*Do's*
- Show style evolution
- Include simplification rules
- Specify when to customize
- Cover motion guidelines

*Don'ts*
- Generic stock graphics
- Inconsistent styles
- No simplification rules
- Missing motion specs

**References**
- [Illustro](https://www.illustro.com/)
- [DrawKit](https://drawkit.com/)

---
## Visual Regression Failures
**Category:** ui | **Type:** methodology | **Tags:** design-systems, analytics, testing

Number of visual differences detected between design mockups and implemented components during automated testing.

**Examples**
- 3 failures in button variants
- 12 card layout shifts
- 1 color token mismatch
- Monthly failures: 16

**Do's and Don'ts**

*Do's*
- Integrate into CI/CD pipeline
- Prioritize high-impact failures
- Distinguish bugs from variances
- Track resolution time

*Don'ts*
- Disable tests for convenience
- Ignore small pixel differences
- Test only on one browser
- Blame other teams

**References**
- [Chromatic](https://www.chromatic.com/)

---
## Visual Repetition
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy, design-systems

Consistent styling unifying interface and reinforcing visual relationships.

**Examples**
- All buttons styled same across pages
- Icon treatment consistency
- Typography scale applied uniformly
- Color palette repeated in components

**Do's and Don'ts**

*Do's*
- Repeat component styles
- Document in design systems
- Reinforce hierarchy patterns
- Test consistency

*Don'ts*
- Random repetition
- Break patterns inconsistently
- Excessive visual repetition
- Ignore responsive consistency

**References**
- [99designs: Hierarchy Principles](https://99designs.com/blog/tips/visual-hierarchy-design-principles/)
- [ParallelHQ: Techniques](https://www.parallelhq.com/blog/visual-hierarchy/)

---
## Von Restorff Effect
**Category:** ux | **Type:** principle | **Tags:** visual-hierarchy

Unique items remembered better than uniform ones.

**Examples**
- Single red CTA button
- Animated hero element
- Unique card highlighting
- Bouncing notification badge

**Do's and Don'ts**

*Do's*
- Strategic uniqueness only
- Important elements distinct
- Consistent background uniformity
- Test memory retention

*Don'ts*
- Every element unique
- Random differentiation
- Noise distracting from content
- Overuse of animations

**References**
- [Psychology Today](https://www.psychologytoday.com/)
- [UX Movement](https://uxmovement.com/)

---
## Wayfinding
**Category:** ui | **Type:** concept | **Tags:** navigation

Environmental cues helping users orient and navigate complex information spaces.

**Examples**
- Breadcrumbs + sidebar in documentation
- Progress indicators in wizards
- Section headers + TOC
- Visual hierarchy guiding flow

**Do's and Don'ts**

*Do's*
- Multiple wayfinding methods
- Consistent orientation cues
- Support spatial memory
- Test complex navigation paths

*Don'ts*
- Rely on memory alone
- Inconsistent wayfinding
- Poor orientation cues
- Complex without guidance

**References**
- [NN/g: Wayfinding in UX](https://www.nngroup.com/articles/wayfinding-ux/)
- [Interaction Design Foundation: Navigation](https://www.interaction-design.org/literature/topics/navigation-design)

---
## WCAG
**Category:** ui | **Type:** framework | **Tags:** accessibility

Web Content Accessibility Guidelines - W3C international standard (A, AA, AAA levels).

**Examples**
- WCAG 2.1 AA: 4.5:1 contrast ratio
- WCAG Success Criterion 1.4.3
- 38 must-pass criteria for AA conformance
- POUR principles (Perceivable, Operable, Understandable, Robust)

**Do's and Don'ts**

*Do's*
- Target WCAG 2.1 AA compliance
- Use WCAG checklist systematically
- Test against all success criteria
- Document conformance level

*Don'ts*
- Claim conformance without testing
- Pick and choose criteria
- Ignore AAA where practical
- Skip WCAG-EM evaluation

**References**
- [W3C: WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM: WCAG Checklist](https://webaim.org/standards/wcag/checklist)

---
## WCAG Success Criteria
**Category:** ux | **Type:** framework | **Tags:** accessibility

Measurable testable accessibility requirements.

**Examples**
- 1.4.3 Contrast Minimum
- 2.4.7 Focus Visible
- 4.1.2 Name Role Value
- 87/112 criteria coverage

**Do's and Don'ts**

*Do's*
- Priority order AA AAA
- Automated + manual test
- Cross-platform validation
- Documentation coverage

*Don'ts*
- Read guidelines only
- Automated scans complete
- Ignore AAA criteria
- No manual verification

**References**
- [W3C: WCAG Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [Accessibility.com](https://www.accessibility.com/)

---
## Wear OS Complications
**Category:** ui | **Type:** pattern | **Tags:** mobile

Customizable glanceable data watch face.

**Examples**
- Weather complication
- Steps fitness tracker
- Calendar next event
- Custom complication API

**Do's and Don'ts**

*Do's*
- Glanceable information
- Tap for details
- Battery efficient
- Contextual relevance

*Don'ts*
- Dense information
- Deep interaction required
- Battery drain
- Static data

**References**
- [Android: Complications](https://developer.android.com/wear/complications)
- [Android Developers](https://developer.android.com/)

---
## Web Share API
**Category:** ui | **Type:** tool | **Tags:** web, interaction

Native browser sharing interface.

**Examples**
- Share button triggers native
- navigator.share() API
- Fallback copy link
- Mobile optimized sharing

**Do's and Don'ts**

*Do's*
- Request permission first
- Fallback gracefully
- Mobile-first implementation
- Test all platforms

*Don'ts*
- Assume universal support
- Ugly custom modals
- Desktop-only sharing
- No fallback copy

**References**
- [MDN: Web Share API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Share_API)
- [Web.dev: Web Share](https://web.dev/web-share/)

---
## Weighted Shortest Job First
**Category:** strategy | **Type:** framework | **Tags:** strategy

Cost of Delay ÷ Job Size = priority score.

**Examples**
- Feature A: CoD 100 size 5 = 20
- Feature B: CoD 50 size 10 = 5
- Business value duration
- Team capacity planning

**Do's and Don'ts**

*Do's*
- Quantify business value
- Predict job duration
- Regular recalculation
- Cross-team alignment

*Don'ts*
- Gut feel prioritization
- Size estimation only
- Never recalculate
- Team siloed scoring

**References**
- [SAFe: WSJF](https://scaledagileframework.com/wsjf/)
- [LeanKit](https://leankit.com/)

---
## White Space
**Category:** ui | **Type:** principle | **Tags:** visual-hierarchy

Strategic empty areas isolating focal points and creating content separation.

**Examples**
- Generous margins around primary CTA button
- Breathing room between card components
- Blank space directing focus to content
- Section padding creating visual hierarchy

**Do's and Don'ts**

*Do's*
- Generous space around CTAs
- Hierarchy of whitespace amounts
- Consistent spacing scales
- Guide eye with whitespace

*Don'ts*
- Fill all available space
- Inconsistent spacing
- Ignore mobile whitespace
- Confuse whitespace with clutter

**References**
- [NN/g: Visual Hierarchy](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/)
- [Loop11: Visual Hierarchy](https://www.loop11.com/visual-hierarchy/)

---
## Wireframe Specification
**Category:** ui | **Type:** tool | **Tags:** documentation

Annotated wireframes with functional and content requirements.

**Examples**
- Content hierarchy marked on wireframe
- Interaction callouts with specs
- Responsive state annotations
- Content type specifications

**Do's and Don'ts**

*Do's*
- Use standard annotations
- Specify content requirements
- Mark interaction zones
- Include flow connections

*Don'ts*
- Clean wireframes only
- Missing content specs
- Vague interaction notes
- No responsive states

**References**
- [Axure](https://www.axure.com/)
- [Balsamiq](https://www.balsamiq.com/)

---
## Wizard of Oz Testing
**Category:** ux | **Type:** methodology | **Tags:** testing

A testing method where users interact with what appears to be a functioning system, but a human operator manually provides responses behind the scenes. Wizard of Oz testing validates concepts and interactions before building complex functionality.

**Examples**
- Testing a chatbot concept where a person manually responds to messages while users believe it's automated
- Simulating voice commands by having a team member manually trigger actions based on spoken requests

**Do's and Don'ts**

*Do's*
- Make the simulation realistic and believable
- Use to test expensive or complex features early
- Brief operators thoroughly on how to respond
- Observe user behavior and expectations
- Validate demand and usability together
- Use findings to inform actual implementation

*Don'ts*
- Let users discover they're being manually operated during testing
- Use Wizard of Oz for features that can be easily prototyped normally
- Skip planning operator responses and timing
- Test without clear research questions
- Forget to debrief participants afterward
- Promise functionality you can't deliver

**References**
- [Nielsen Norman Group: Wizard of Oz Testing](https://www.nngroup.com/articles/wizard-of-oz/)
- [Interaction Design Foundation: Wizard of Oz Prototyping](https://www.interaction-design.org/literature/article/wizard-of-oz-prototyping)

---
## Worst Idea Generation
**Category:** ux | **Type:** tool | **Tags:** ideation

Deliberately generate bad ideas then reverse into solutions.

**Examples**
- Worst onboarding flow
- Most confusing navigation
- Ugliest UI possible
- Slowest checkout process

**Do's and Don'ts**

*Do's*
- Embrace absurdity
- Find reversal insights
- Use for stuck teams
- Document flip ideas

*Don'ts*
- Take ideas literally
- Skip reversal phase
- Criticize contributors
- Use as only method

**References**
- [NN/g: Ideation Methods](https://www.nngroup.com/articles/ideation-in-practice/)
- [Gamestorming](https://gamestorming.com/)

---
## XY Scatter Plot
**Category:** ui | **Type:** tool | **Tags:** data-visualization

Points on coordinate plane reveal correlations between two variables.

**Examples**
- Age vs income distribution
- Exercise vs weight loss
- Study hours vs exam scores
- Price vs demand relationship

**Do's and Don'ts**

*Do's*
- Clear axis labeling
- Trend line when relevant
- Size/color for 3rd variable
- Jitter overlapping points

*Don'ts*
- No trend correlation
- Too many points (>1000)
- Missing context grid
- Arbitrary axis scaling

**References**
- [Scatter Chart](https://www.scatterchart.com/)
- [Towards Data Science](https://towardsdatascience.com/)

---
## Z-Pattern
**Category:** ui | **Type:** pattern | **Tags:** visual-hierarchy

Simple layout scan path (left→right→left→right) following natural eye movement.

**Examples**
- Email template layout
- Simple landing page flow
- Product comparison side-by-side
- Two-column form layout

**Do's and Don'ts**

*Do's*
- Place CTAs on Z-path
- Simple layouts only
- Test with eye-tracking
- Adapt for RTL languages

*Don'ts*
- Force on complex layouts
- Ignore reading patterns
- Place key content off-path
- Use without testing

**References**
- [Interaction Design Foundation: Z-Pattern](https://www.interaction-design.org/literature/article/z-pattern)
- [CareerFoundry: Layout Examples](https://careerfoundry.com/en/blog/ui-design/visual-hierarchy/)

---
## Zeigarnik Effect
**Category:** ux | **Type:** principle | **Tags:** interaction

Incomplete tasks remembered better than completed.

**Examples**
- Progress bars incomplete
- Save for later cart items
- Drafts folder prominence
- Step indicators showing progress

**Do's and Don'ts**

*Do's*
- Show remaining steps
- Save incomplete work
- Progress visualization
- Recovery from abandonment

*Don'ts*
- Hide incomplete tasks
- Auto-clear abandoned carts
- No progress indication
- Force task completion

**References**
- [NN/g: Zeigarnik Effect](https://www.nngroup.com/articles/zeigarnik-effect/)
- [UX Design CC](https://uxdesign.cc/)
