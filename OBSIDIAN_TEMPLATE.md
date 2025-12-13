# Rugby Council AI - Project Documentation

**Project Type**: Multi-Model AI Orchestration  
**Status**: Initial Implementation  
**Date Started**: December 2024  
**GitHub**: https://github.com/footnote42/rugby-council-ai

## Concept Overview

The Rugby Council AI implements a three-stage collaborative process where multiple AI models work together to design rugby training sessions. Rather than relying on a single model's perspective, this approach mirrors how a coaching staff meeting would work - individual coaches propose ideas, critique each other's work, and then synthesize the best approach.

### Why This Approach Works

Single-model responses can have blind spots or biases based on their training. By having multiple models with different strengths (reasoning, instruction-following, creative problem-solving) work together, we get more balanced and thoughtful outputs. The anonymous peer review stage is particularly powerful because it removes favoritism and focuses purely on quality against our coaching framework.

## Technical Architecture

### Three-Stage Process

**Stage 1 - Individual Opinions**: Each model receives identical prompts containing the Trojans Coaching Framework and session parameters. They work independently without seeing other models' responses. This ensures diverse perspectives rather than groupthink.

**Stage 2 - Anonymous Peer Review**: All three session plans are presented to each model with anonymized labels (Plan A, B, C). Each model ranks them and provides constructive feedback. This stage leverages competitive dynamics while maintaining objectivity.

**Stage 3 - Chairman Synthesis**: The designated chairman model (using the reasoning model by default) reviews all original plans and all peer feedback, then creates a final optimized session plan.

### Model Selection

The three models chosen represent different capabilities:

- **Ministral-3-8B-Reasoning**: Step-by-step analytical thinking, good for breaking down complex problems
- **Ministral-3-8B-Instruct**: Strong instruction following, good for adhering to frameworks
- **GPT-OSS-20B**: Larger parameter count, potentially more creative solutions

Using local models via LM Studio ensures zero cost per session and complete control over the process.

## Integration with Trojans Coaching Framework

The framework provides essential constraints that prevent generic AI responses. Every model must demonstrate understanding of:

- The five Trojans Coaching Habits (Shared Purpose, Progression, Praise, Review, Choice)
- TREDS values (Teamwork, Respect, Enjoyment, Discipline, Sportsmanship)
- APES principles (Active, Purposeful, Enjoyable, Safe)
- The Player Framework's three dimensions (Behaviours, Skills, Knowledge)

These constraints act as a quality filter. If a session plan doesn't address these elements, it will be critiqued in Stage 2 and improved in Stage 3.

## Learning Outcomes

### What I Learned About Python

*(Document your Python learnings as you work through the project)*

- How virtual environments isolate project dependencies
- Making HTTP requests to local API servers
- Structuring code with functions for reusability
- Using configuration files to separate settings from logic

### What I Learned About AI Orchestration

*(Document insights as you experiment)*

- How different models interpret the same prompt differently
- The value of peer review in improving AI outputs
- How model temperature affects response consistency vs. creativity
- The importance of clear, specific prompts with good context

### What I Learned About Session Design

*(Document coaching insights from reviewing council outputs)*

- Different valid approaches to the same coaching challenge
- How models prioritize different framework elements
- New activity ideas or progressions I hadn't considered
- Ways to better articulate coaching objectives

## Experiments Conducted

### Experiment 1: Initial Council Test
**Date**: [Date]  
**Session Parameters**: 60 minutes, U10s, 24 players, 4 coaches, focus on decision making around the breakdown  
**Outcome**: [Your notes on results]  
**GitHub Commit**: [Commit hash]  
**Key Insights**: [What you learned]

### Experiment 2: [Next experiment]
**Date**: [Date]  
**Session Parameters**: [Parameters]  
**Outcome**: [Your notes]  
**Key Insights**: [Learnings]

## Challenges and Solutions

### Challenge: Model Switching in LM Studio
**Problem**: LM Studio can only run one model at a time, requiring manual switching  
**Solution**: Script pauses with clear instructions for which model to load  
**Future Improvement**: Could explore running multiple LM Studio instances if hardware allows

### Challenge: Response Quality Variation
**Problem**: Sometimes models give generic responses that don't deeply engage with the framework  
**Solution**: [Your solutions as you discover them]

## Connection to Broader AI Delegation Research

This project demonstrates a key principle of systematic AI delegation: breaking complex tasks into stages where different AI capabilities can be leveraged. The coach isn't just asking for a session plan - they're orchestrating a collaborative process that:

1. Generates multiple perspectives (delegation to specialist "coaches")
2. Implements quality control (peer review stage)
3. Synthesizes into actionable output (chairman role)

This pattern could apply to other domains beyond coaching - product design, code review, policy analysis, etc.

## Next Steps

**Immediate**:
- [ ] Run first complete council session
- [ ] Document output quality
- [ ] Test with different session parameters
- [ ] Compare council output to own session plans

**Near Term**:
- [ ] Experiment with different model combinations
- [ ] Try different models as chairman
- [ ] Test with various session types (fitness, skills, tactics)
- [ ] Analyze patterns in what models value during peer review

**Future Exploration**:
- [ ] Extend to code generation experiments
- [ ] Build web interface for easier interaction
- [ ] Implement "manager-worker" pattern as alternative to council
- [ ] Create comparative analysis of council vs. single-model outputs

## Resources and References

**GitHub Repository**: https://github.com/footnote42/rugby-council-ai

**Related Projects**:
- LLM Council (Karpathy): https://github.com/footnote42/llm-council
- Multiple Model Orchestration: https://github.com/Brierley77/Multiple-Model-Orchestration

**Technical Documentation**:
- LM Studio API Documentation
- OpenAI API Reference (LM Studio compatible)
- Requests library documentation

**Coaching Resources**:
- Trojans Coaching Framework (this vault)
- RFU Regulation 15
- KYBO methodology

## Reflections

*(Use this space for ongoing reflections as you work with the system)*

### What's Working Well
[Your observations]

### What's Surprising
[Unexpected outcomes or behaviors]

### What Could Improve
[Ideas for enhancement]

### How This Changes My Coaching Approach
[Impact on your actual coaching practice]

---

**Tags**: #ai-delegation #rugby-coaching #multi-model-orchestration #python-learning #trojans-rfc

**Related Notes**:
- [[Trojans Coaching Framework]]
- [[Systematic AI Delegation]]
- [[Rugby Session Planner]]
- [[AI-Assisted Coaching Tools]]