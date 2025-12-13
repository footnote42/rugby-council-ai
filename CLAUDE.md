# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Rugby Council AI is a multi-model AI orchestration system that collaboratively designs rugby training sessions. It implements a three-stage council process where multiple AI models work together like a coaching staff meeting:

1. **Stage 1 - Individual Plans**: Each model independently creates a complete session plan
2. **Stage 2 - Peer Review**: Models anonymously critique and rank all plans
3. **Stage 3 - Chairman Synthesis**: A designated chairman model creates the final optimized plan

The system uses local LLM models via LM Studio to generate rugby training sessions aligned with the Trojans RFC Coaching Framework.

## Development Commands

### Environment Setup
```bash
# Create virtual environment (first time only)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
# Ensure LM Studio is running with server started on port 1234
# Run the council
python council.py
```

The script will pause at each stage to allow you to manually switch models in LM Studio, as LM Studio can only load one model at a time.

### Modifying Session Parameters
Edit `council.py` around line 513 to change session requirements:
```python
session_params = "60 minutes, U10s, 24 players, 4 coaches, focus on decision making around the breakdown"
```

### Configuring Models
Edit `config.py` to:
- Change which models are used (model names must match LM Studio exactly)
- Set which model acts as chairman (default: "reasoning")
- Adjust temperature (creativity level, 0.0-1.0, default: 0.7)
- Modify max tokens per response (default: 2000)

## Architecture

### Core Components

**council.py** - Main orchestration script (524 lines)
- `load_coaching_framework()`: Loads the Trojans framework from coaching_framework.md
- `call_lm_studio(prompt, model_name, temperature)`: Handles all LM Studio API communication
- `wait_for_model_switch(model_name)`: Pauses execution for manual model switching
- `stage_1_individual_responses()`: Collects independent session plans from each model
- `truncate_plan_for_review(plan, max_chars)`: Intelligently truncates plans to fit context limits
- `stage_2_peer_review()`: Anonymizes and truncates plans, collects peer reviews with rankings
- `stage_3_chairman_synthesis()`: Chairman model creates final synthesis from truncated inputs
- `save_council_session()`: Saves all outputs to sessions/ directory
- `run_council(session_params)`: Main entry point orchestrating the full process

**config.py** - Configuration settings
- `LM_STUDIO_BASE_URL`: API endpoint (default: http://localhost:1234/v1)
- `COUNCIL_MODELS`: Dictionary defining the three council members with roles
- `CHAIRMAN_MODEL`: Which model synthesizes the final plan
- `TEMPERATURE`: Response creativity level
- `MAX_TOKENS`: Maximum response length
- `ANONYMIZE_REVIEWS`: Whether peer reviews are anonymous (default: True)

**coaching_framework.md** - Trojans RFC Coaching Framework
Contains the complete coaching framework that constrains and guides all model outputs:
- Club vision and ethos
- Player Framework (Behaviours, Skills, Knowledge)
- Five Trojans Coaching Habits (Shared Purpose, Progression, Praise, Review, Choice)
- TREDS values (Teamwork, Respect, Enjoyment, Discipline, Sportsmanship)
- APES principles (Active, Purposeful, Enjoyable, Safe)

### Multi-Stage Process Flow

The council process is **sequential** and **blocking** by design:

1. **Stage 1**: For each of the 3 models:
   - Script pauses and prompts user to load specific model in LM Studio
   - Sends identical prompt with framework + session parameters
   - Receives independent session plan (no visibility of other plans)
   - All responses stored in `responses` dictionary

2. **Stage 2**: For each of the 3 models:
   - Script pauses for model switch
   - Plans are **truncated to ~3000 chars** each to fit context limits
   - Sends all 3 plans from Stage 1 with anonymized labels (Plan A, B, C)
   - Truncation preserves beginning (objectives) and end (summary) sections
   - Model ranks plans and provides critique
   - Reviews stored in `reviews` dictionary

3. **Stage 3**: Chairman model only:
   - Script pauses for chairman model load
   - Plans are **truncated to ~2500 chars** each, reviews to ~4000 chars
   - Receives all original plans + all peer reviews (truncated)
   - Synthesizes final optimized session plan
   - Final plan stored in `final_plan` string

4. **Save**: All outputs written to `sessions/council_session_TIMESTAMP.md`
   - Note: Saved file contains **full, untruncated** content from all stages
   - Truncation only affects what models see during review/synthesis

### LM Studio Integration

The system communicates with LM Studio using the OpenAI-compatible API format:
- Endpoint: `http://localhost:1234/v1/chat/completions`
- Method: POST with JSON payload
- Timeout: 300 seconds per request
- The `call_lm_studio()` function handles all API communication

**Critical constraint**: LM Studio can only run one model at a time, requiring manual model switching between stages. The script uses `wait_for_model_switch()` to pause and provide clear instructions.

### Context Window Management

To prevent exceeding model context limits, the system implements intelligent truncation:

**Truncation Strategy**:
- `truncate_plan_for_review()` reduces long plans while preserving key information
- Keeps first 60% and last 20% of content (objectives + summary)
- Inserts marker: `[... middle sections abbreviated for length ...]`

**Truncation Limits**:
- Stage 2 (peer review): Each plan truncated to max 3000 characters
- Stage 3 (synthesis): Plans to 2500 chars, reviews to 4000 chars
- Original full content always preserved in final output file

**Why This Matters**:
- Prevents context overflow errors with smaller models
- Maintains review quality by preserving critical plan sections
- Allows system to work with models that have limited context windows
- Full plans are still saved - truncation only affects model inputs

### Model Configuration

Three models with distinct roles (actual model names configured in `config.py`):
- **Analytical Coach** (default chairman): Reasoning model for step-by-step analysis
- **Structured Coach**: Instruction-following model for strong framework adherence
- **Creative Coach**: Larger model for creative solutions

**Current config.py models**: mistral-tiny (reasoning), mistral-latest (instruct), gpt-4o (creative)

The framework is loaded once at startup and included in every prompt to ensure consistent context.

### Output Structure

Generated files in `sessions/` contain:
- Session metadata (timestamp, parameters)
- Stage 1: All three individual plans with model roles
- Stage 2: All three peer reviews with rankings
- Stage 3: Final synthesized plan
- Markdown formatted for easy reading

## Framework Constraints

The Trojans Coaching Framework provides essential quality constraints that prevent generic AI responses. Every session plan must demonstrate:

**Five Coaching Habits** (non-negotiable in every session):
1. Shared Purpose - Clear aims linked to Player Framework
2. Progression - STEP principle (Space, Task, Equipment, People)
3. Praise - Specific examples linked to TREDS values
4. Review - Question-based player reflection
5. Choice - Player ownership and options

**TREDS Values**: Teamwork, Respect, Enjoyment, Discipline, Sportsmanship

**APES Principles**: Active, Purposeful, Enjoyable, Safe

**Player Framework Dimensions**: Behaviours, Skills, Knowledge

If a plan doesn't address these elements, it will be critiqued in peer review and improved in synthesis.

## Dependencies

Only two external packages (see requirements.txt):
- `requests>=2.31.0` - HTTP calls to LM Studio API
- `python-dotenv>=1.0.0` - Environment variable management (included for good practice, not currently used)

## Directory Structure

```
rugby-council-ai/
├── council.py                  # Main orchestration script
├── config.py                   # Configuration settings
├── coaching_framework.md       # Trojans RFC framework (loaded by council.py)
├── requirements.txt            # Python dependencies
├── sessions/                   # Auto-created output directory
│   └── council_session_*.md   # Generated session plans
├── venv/                       # Virtual environment (not committed)
└── README.md                   # User-facing documentation
```

## Common Modifications

**Change session parameters**: Edit the `session_params` string in `council.py:513`

**Change models**: Update `COUNCIL_MODELS` dictionary in `config.py` with exact model names from LM Studio

**Change chairman**: Set `CHAIRMAN_MODEL` in `config.py` to "reasoning", "instruct", or "gpt"

**Adjust creativity**: Modify `TEMPERATURE` in `config.py` (0.3-0.5 = focused, 0.7-0.9 = creative)

**Extend response length**: Increase `MAX_TOKENS` in `config.py` (default 2000)

## Troubleshooting

**"Cannot connect to LM Studio"**: Verify LM Studio server is running on port 1234

**"Request timed out"**: Model took >5 minutes - simplify session parameters or reduce MAX_TOKENS

**Generic responses**: Ensure coaching_framework.md exists and contains complete framework

**Model name errors**: Model names in config.py must match LM Studio exactly (case-sensitive)

## Design Principles

- **Synchronous blocking**: Each API call blocks until complete for simplicity and clarity
- **Manual orchestration**: User manually switches models (LM Studio limitation)
- **Complete transparency**: All intermediate outputs saved, nothing hidden
- **Framework-driven**: Coaching framework constrains all outputs for quality
- **Local-first**: All models run locally via LM Studio, zero cost per session
