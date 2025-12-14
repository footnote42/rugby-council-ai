# Case Study: First Successful Council Session

**Date**: December 14, 2024  
**Session Focus**: U10 Decision Making Around the Breakdown  
**Models**: Ministral-3-8B-Reasoning, Ministral-3-8B-Instruct, Qwen2.5-8B-Instruct  
**Total Processing Time**: 45 minutes  

## Overview

This document presents the first complete execution of the Rugby Council AI system, demonstrating how three AI models collaborated through a structured three-stage process to design a rugby training session. Rather than simply presenting the raw output, this case study walks through what happened at each stage and analyzes whether the council approach actually added value.

## The Challenge

Design a 60-minute rugby training session for:
- **Age Group**: U10s (9-10 year olds)
- **Players**: 24 children
- **Coaches**: 4 adult coaches
- **Focus**: Decision making around the breakdown (ruck/maul situations)
- **Framework**: Must align with Trojans RFC Coaching Framework

This is a realistic coaching scenario that requires balancing multiple constraints: age-appropriate content, framework compliance, practical implementation with available coaches, and engaging activities that develop specific skills.

## Stage 1: Three Independent Perspectives

Each model received identical prompts containing the Trojans Coaching Framework and session parameters. They worked independently without seeing each other's responses.

### The Analytical Coach (Reasoning Model)

**Approach**: Systematic, step-by-step breakdown showing its thinking process through `[THINK]` tags.

**Key Activities Proposed**:
- "Breakdown Drills Circus" - Station-based warm-up
- "Ruck Battle" - 3v3 tactical decision-making drill
- "Maul Maze" - Navigation through decision points
- "Breakdown Tag" - Game combining collection objectives with breakdown scenarios

**Distinctive Characteristics**:
- Explicitly mapped every activity to Player Framework dimensions
- Systematically showed how TREDS values were integrated
- Detailed progressions using STEP principles
- Engineering-minded approach: objectives → activities → progressions → validation

**Framework Compliance**: Strong. Explicitly addressed all five Coaching Habits and APES principles.

### The Structured Coach (Instruct Model)

**Approach**: Clean formatting with tables, clear time allocations, and practical implementation details.

**Key Activities Proposed**:
- "Ruck & Roll Circuit" - Dynamic warm-up with four stations
- "Ruck Decision Race" - Competitive drill with clear winning conditions
- "Support Sprint Relay" - Speed and support positioning
- Structured game with explicit scoring rules

**Distinctive Characteristics**:
- Heavy emphasis on practical details (equipment lists, coach positioning)
- Clear timing breakdowns for each activity
- Table-based formats for easy coach reference
- Implementation-focused: how to actually run each activity

**Framework Compliance**: Excellent. Strong on progression and practical application of habits.

### The Creative Coach (Qwen Model)

**Approach**: Player-centered with emphasis on engagement and enjoyment.

**Key Activities Proposed**:
- "Dynamic Duo Warm-Up" - Partner-based activation
- "Breakdown Battle Game" - Multiple scoring variations
- Creative variations on traditional drills
- Strong emphasis on player choice and autonomy

**Distinctive Characteristics**:
- Most innovative warm-up concepts
- Focused on making activities fun and accessible
- Considered different ability levels within activities
- Player engagement prioritized alongside skill development

**Framework Compliance**: Good. Strong on Enjoyment and Choice habits, slightly less detail on Progression.

### Initial Comparison

At this stage, we have three genuinely different session plans. None is obviously "best" - each has strengths:
- Reasoning model: Most systematic and thorough
- Instruct model: Most practical and implementable
- Qwen model: Most creative and engaging

A coach could use any of these plans and run a decent session. The question becomes: can combining them create something better than any individual plan?

## Stage 2: Anonymous Peer Review

Plans were truncated to preserve key information while fitting context window limits (~2500 characters each). They were presented anonymously as "Plan A," "Plan B," and "Plan C." Each model reviewed all three plans and ranked them.

### What the Reviews Revealed

**The Models Were Genuinely Critical**:

Example critiques:
- "Plan A lacks explicit details on how each habit is integrated"
- "Missing safety measures: No explicit mention of age-appropriate risk management"
- "STEP principles are not clearly defined with specific examples"
- "Incomplete execution: abbreviated sections make it hard to assess full compliance"

These are specific, actionable critiques, not generic praise.

**Consensus on Quality Markers**:

All three reviewers independently valued:
1. Explicit integration of all five Coaching Habits
2. Clear STEP progressions with measurements (not vague "increase difficulty")
3. Age-appropriate safety considerations explicitly stated
4. Specific praise examples linked to TREDS values
5. Practical implementation details

This consensus suggests these are genuinely important quality markers, not arbitrary preferences.

**Rankings**:

While Plan B received highest marks from all reviewers, the specific reasoning varied:
- One reviewer emphasized framework compliance
- Another focused on practical implementation
- A third prioritized safety and age-appropriateness

This variance suggests independent evaluation rather than pattern matching.

**Constructive Recommendations**:

Each review concluded with specific improvements:
- "Add safety guidelines: emphasize light contact and safe zones during rucks/mauls"
- "Detail Coaching Habits: Explicitly link praise, review, and choice to TREDS values"
- "Elaborate Progression Steps: Provide concrete examples of how STEP principles are applied"

These are the kind of feedback a coaching mentor might give.

### The Value of Peer Review

This stage demonstrated something important: having multiple evaluators identify weaknesses creates a more comprehensive quality control process than a single reviewer would provide. Different reviewers noticed different gaps.

## Stage 3: Chairman Synthesis

The Reasoning model reviewed all three plans and all three peer reviews, then created a final synthesized session plan.

### Evidence of True Synthesis (Not Just Selection)

The final plan wasn't simply Plan B (the highest-ranked). It demonstrably combined elements:

**From Plan A**:
- "Breakdown Circus" warm-up concept
- Emphasis on systematic framework integration

**From Plan B**:
- "Ruck Decision Race" structure and timing
- Clear equipment and coach deployment strategies

**From Plan C**:
- "Pressure Maze" activity approach
- Focus on player choice and autonomy

### Addressing Peer Review Feedback

The chairman systematically fixed issues identified in Stage 2:

**Missing Safety Notes** → Added throughout:
- "Light contact only at U10 level"
- "Safe zones marked with cones"
- "Coaches monitor for over-commitment to contact"

**Vague Progressions** → Made Concrete:
- Changed "increase difficulty" to "20m between lines, reduce to 15m"
- Changed "add more players" to "Start 2v2, progress to 3v3"
- Specified exact STEP parameters for each activity

**Missing Choice Examples** → Explicitly Designed In:
- Players choose which hand to use in warm-up
- Players choose path through Pressure Maze
- Players choose roles at start of game

**Generic Praise** → Specific Examples Linked to Framework:
- "Great body control! That's how we dominate the ball!" (Core Strength)
- "Quick decision! You chose to pass and that created space!" (Decision Making, Teamwork)
- "Quick recovery! You got back on your feet after being knocked off!" (Resilience)

### The Final Session Plan

The complete synthesized plan is [available here](../sessions/council_session_20251214_145206.md).

**Structure**:
- Warm-up: "Breakdown Circus" (12 minutes) - 3 stations, rotational
- Activity 1: "Ruck Decision Race" (15 minutes) - Competitive drill with progressions
- Activity 2: "Pressure Maze" (15 minutes) - Decision-making under constraint
- Game: "Breakdown Showdown" (15 minutes) - Full application in game context
- Cool-down & Review (8 minutes) - Player-led reflection

**Framework Integration**:
- Shared Purpose: Clearly stated and linked to Player Framework
- Progression: Explicit STEP implementation with measurements
- Praise: Specific examples throughout
- Review: Question-based reviews embedded in activities
- Choice: Player options designed into each activity

**Practical Considerations**:
- Four coaches deployed across stations
- Equipment list clearly specified
- Age-appropriate contact guidelines
- Time allocations total 65 minutes (slightly over, but manageable)

## Critical Assessment: Did the Council Add Value?

This is the fundamental research question. Here's the evidence:

### Arguments FOR Council Value:

**1. Idea Combination**: The final plan contains concepts from all three models, not just the "winner." This is genuine synthesis, not selection.

**2. Weakness Elimination**: Specific gaps identified in Stage 2 (safety notes, vague progressions, missing habits) were systematically addressed in Stage 3. The final plan is more complete than any individual plan.

**3. Refinement Through Critique**: The peer review process articulated what makes a quality session plan, and the chairman incorporated these criteria. This iterative refinement is difficult to achieve with single-model generation.

**4. Framework Compliance**: The final plan addresses 100% of required framework elements explicitly. Individual plans had gaps.

### Arguments AGAINST or NEUTRAL:

**1. Time Investment**: 45 minutes of processing time vs. instant single-model response. This overhead might not be justified for all use cases.

**2. Baseline Unknown**: We don't have a controlled comparison (same parameters, single model with equivalent prompt engineering) to prove the council approach is definitively better.

**3. Diminishing Returns**: The third model (Qwen) added creative ideas but might not have added enough value to justify the additional processing time compared to a two-model council.

**4. Prompt Engineering Alternative**: A single model with a carefully engineered prompt that included "consider multiple approaches," "identify weaknesses," and "synthesize ideas" might achieve similar results.

### Verdict

**Based on this single execution, the council approach demonstrably added value** in the following ways:

1. **Diversity of Ideas**: Three genuinely different approaches emerged
2. **Quality Control**: Peer review identified real weaknesses
3. **Comprehensive Output**: Final plan more complete than individuals
4. **Framework Adherence**: 100% compliance vs. partial in individuals

**However, this is preliminary evidence.** To definitively prove value, we need:
- Controlled comparison with single-model baseline
- Multiple sessions to test consistency
- Evaluation by professional coaches blind to generation method
- Cost-benefit analysis of time vs. quality improvement

## Technical Implementation Notes

### Hardware Constraints

This execution required navigating real hardware limitations:
- Initial attempt with 20B parameter model failed (12.34GB required vs. 16GB available)
- Replaced with 8B parameter model for reliable operation
- Context window limitations required content truncation in Stages 2-3
- Different models showed vastly different inference speeds (6 vs. 15+ tokens/sec)

These constraints are fundamental to local AI deployment and shape what's possible.

### Configuration That Worked

**Models**:
- Analytical: Ministral-3-8B-Reasoning (chairman)
- Structured: Ministral-3-8B-Instruct
- Creative: Qwen2.5-8B-Instruct

**Settings**:
- Temperature: 0.7 (balance between creativity and consistency)
- Max tokens: 2000 per response
- Timeout: 600 seconds (10 minutes) to accommodate slower models
- Context window: 16384 tokens for chairman synthesis

**Truncation Strategy**:
- Stage 2: Plans truncated to 3000 characters (preserving first 60% and last 20%)
- Stage 3: Plans to 2500 characters, reviews to 4000 characters
- This preserved essential information while respecting context limits

## Lessons for Other Implementers

If you're considering implementing a similar council approach:

**1. Start with Hardware Assessment**:
- Calculate actual memory requirements (model size × 2-3)
- Test model loading before designing complex workflows
- Plan for the slowest model in your council

**2. Design for Context Limits**:
- Don't assume you can send everything to every stage
- Implement intelligent truncation from the start
- Test with maximum-length outputs to find breaking points

**3. Expect Model Personality Differences**:
- Different models have different strengths
- This diversity is valuable, not a problem to solve
- Consider model selection carefully for each role

**4. Build in Quality Control**:
- The peer review stage was crucial to value-add
- Don't skip critique even if it adds time
- Anonymous review prevents bias

**5. Document Thoroughly**:
- You'll forget why you made certain decisions
- Capture both successes and failures
- Hardware constraints are as important as code

## Future Experiments

This successful execution opens several research directions:

**Comparison Studies**:
- Same parameters, single model (establish baseline)
- Two-model vs. three-model council (optimal size?)
- Different chairman selection (does it matter who synthesizes?)

**Variations**:
- Different session types (fitness, skills-only, tournament prep)
- Different temperature settings (creativity vs. consistency)
- Different model combinations (all reasoning, all instruct, etc.)

**Improvements**:
- Automated model switching (if multiple LM Studio instances possible)
- Configurable truncation strategies
- Output quality scoring rubric
- Comparison to human-generated sessions

**Generalization**:
- Does this work for other coaching domains?
- Does it work for code generation?
- Does it work for policy analysis or other planning tasks?

## Conclusion

The Rugby Council AI successfully demonstrated that multi-model orchestration with structured critique can produce comprehensive, framework-compliant coaching content. The council approach showed clear value in this execution through idea combination, weakness identification, and systematic refinement.

However, this is one data point. The next phase requires controlled comparison to quantify whether the quality improvement justifies the time investment, and whether this approach generalizes to other contexts.

This implementation demonstrates that the council pattern can be successfully adapted to local models with careful attention to hardware constraints and context window management. The key innovation here wasn't the council structure itself (credit to Karpathy's original concept) but rather making it work reliably with local 8B models through intelligent truncation and timeout management.

The complete session output, all code, and ongoing learning documentation is available in the [GitHub repository](https://github.com/footnote42/rugby-council-ai).

---

**Next**: Controlled comparison experiment with single-model baseline to quantify value-add.