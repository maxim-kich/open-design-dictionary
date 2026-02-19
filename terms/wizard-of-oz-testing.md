---
category: ux
type: methodology
tags: [testing]
---

# Wizard of Oz Testing

## Definition
A testing method where users interact with what appears to be a functioning system, but a human operator manually provides responses behind the scenes. Wizard of Oz testing validates concepts and interactions before building complex functionality.

## Examples
- Testing a chatbot concept where a person manually responds to messages while users believe it's automated
- Simulating voice commands by having a team member manually trigger actions based on spoken requests

## Do's and Don'ts

**Do's**
- Make the simulation realistic and believable
- Use to test expensive or complex features early
- Brief operators thoroughly on how to respond
- Observe user behavior and expectations
- Validate demand and usability together
- Use findings to inform actual implementation

**Don'ts**
- Let users discover they're being manually operated during testing
- Use Wizard of Oz for features that can be easily prototyped normally
- Skip planning operator responses and timing
- Test without clear research questions
- Forget to debrief participants afterward
- Promise functionality you can't deliver

## References
- [Nielsen Norman Group: Wizard of Oz Testing](https://www.nngroup.com/articles/wizard-of-oz/)
- [Interaction Design Foundation: Wizard of Oz Prototyping](https://www.interaction-design.org/literature/article/wizard-of-oz-prototyping)
