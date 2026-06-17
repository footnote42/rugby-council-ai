# Rugby Council AI

A multi-agent AI system that orchestrates a "council" of local language models to collaboratively design rugby training sessions. Three models independently produce plans, critique each other's work anonymously, then a designated chairman synthesises everything into a final output — all running locally, with no data leaving the machine.

Built as a practical experiment in agentic AI orchestration using the [Trojans RFC Coaching Framework](coaching_framework.md) as the domain knowledge layer.

---

## What problem this solves

Asking a single AI model to design a session produces one perspective. It cannot critique its own blind spots or notice when it has skimped on a framework requirement. This system applies a structured debate-and-synthesis pattern across three models with distinct personas, producing a final plan that is more complete and framework-compliant than any individual model achieves alone.

The practical result: a ready-to-use coaching session plan that explicitly addresses every element of the club's coaching framework — five coaching habits, TREDS values, APES principles, age-appropriate safety notes, and STEP progressions with concrete measurements.

---

## Architecture

The system runs through three sequential stages, orchestrated by `council.py`:

```
Session parameters + Coaching Framework
              │
              ▼
┌─────────────────────────────────┐
│  STAGE 1: Independent Planning  │
│                                 │
│  Analytical Coach  ─────────┐  │
│  Structured Coach  ─────────┤  │
│  Creative Coach    ─────────┘  │
│  (no cross-visibility)         │
└──────────────┬──────────────────┘
               │ Three session plans
               ▼
┌─────────────────────────────────┐
│  STAGE 2: Anonymous Peer Review │
│                                 │
│  Plans labelled A / B / C       │
│  (author identity removed)      │
│                                 │
│  Each model reviews all three,  │
│  ranks them, identifies gaps    │
└──────────────┬──────────────────┘
               │ Three sets of critiques
               ▼
┌─────────────────────────────────┐
│  STAGE 3: Chairman Synthesis    │
│                                 │
│  Receives all plans + reviews   │
│  Combines best elements         │
│  Addresses identified weaknesses│
│  Produces final session plan    │
└──────────────┬──────────────────┘
               │
               ▼
     sessions/council_session_[timestamp].md
```

`council.py` calls LM Studio's local REST API (OpenAI-compatible `/v1/chat/completions`) for each model call. Because LM Studio loads one model at a time on consumer hardware, the script pauses between model calls and prompts the operator to switch models manually. This makes the system accessible without requiring multiple GPUs or cloud API keys.

Long session plans are intelligently truncated before passing to Stage 2 and Stage 3 — preserving the first 60% (objectives, structure) and last 20% (coaching points, summary) of each plan. This keeps the council functional on 8B models with limited context windows.

---

## Why local model hosting

All inference runs through LM Studio on local hardware. No prompts, no session data, and no domain knowledge leave the machine.

This matters in any context where the content being processed is sensitive — coaching data, organisational frameworks, operational knowledge. Running locally eliminates the network dependency, removes third-party data handling considerations, and keeps the operator in full control of what models are used and when they are updated.

The tradeoff is inference speed (8B models at 6–15 tokens/sec on consumer hardware) and manual model switching. For a use case like session planning — where you run the council once and use the output — this is an acceptable cost.

---

## Models used

Tested configuration (December 2025):

| Role | Model | Characteristics |
|------|-------|-----------------|
| Analytical Coach | `Ministral-3-8B-Reasoning` | Step-by-step reasoning, explicit framework mapping |
| Structured Coach | `Ministral-3-8B-Instruct` | Clean output formatting, practical implementation detail |
| Creative Coach | `Qwen2.5-8B-Instruct` | Player-centred ideas, engagement focus, novel activities |
| **Chairman** | `Ministral-3-8B-Reasoning` | Synthesises all input |

Models are configured in `config.py`. Any LM Studio-compatible models can be substituted — the model names must match exactly what appears in LM Studio's interface.

---

## What the council produces

From the [first successful session](docs/case-studies/first-successful-session.md) (U10 breakdown decision-making, December 2025):

The three models produced genuinely different plans. Peer review identified real gaps: missing safety notes, vague STEP progressions, unlinked coaching habit references. The chairman's synthesised plan addressed every identified weakness and drew activities from all three individual plans — not simply selecting the highest-ranked plan.

**Total processing time**: 45 minutes on a 16GB consumer laptop

Full example output: [U10 Breakdown Decision Making](examples/session-outputs/u10-breakdown-decision.md)

---

## Setup

### Prerequisites

- [LM Studio](https://lmstudio.ai/) installed with models downloaded
- Python 3.8+

### 1. Start LM Studio server

Open LM Studio → Local Server → Start Server. Verify it shows `Running on http://localhost:1234`.

### 2. Python environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure models

Edit `config.py` to match the model names as they appear in your LM Studio:

```python
COUNCIL_MODELS = {
    "reasoning": {
        "name": "mistral-3-8b-reasoning",   # Must match LM Studio exactly
        "role": "Analytical Coach"
    },
    "instruct": {
        "name": "mistral-3-8b",
        "role": "Structured Coach"
    },
    "gpt": {
        "name": "Qwen3-8b",
        "role": "Creative Coach"
    }
}

CHAIRMAN_MODEL = "reasoning"
TEMPERATURE = 0.7
MAX_TOKENS = 2000
```

---

## Running the council

```bash
python council.py
```

The script pauses between model calls and prompts you to switch models in LM Studio. Total operator interactions: 7 model switches. Total elapsed time: 30–45 minutes on 8B models.

### Session parameters

Edit near the bottom of `council.py`:

```python
session_params = "60 minutes, U10s, 24 players, 4 coaches, focus on decision making around the breakdown"
```

---

## Project structure

```
rugby-council-ai/
├── council.py                        # Main orchestration script
├── config.py                         # Model roster and settings
├── coaching_framework.md             # Trojans RFC framework (domain knowledge)
├── requirements.txt
├── sessions/                         # Generated outputs (gitignored, local only)
├── examples/
│   └── session-outputs/
│       └── u10-breakdown-decision.md
└── docs/
    ├── case-studies/
    │   └── first-successful-session.md
    ├── guides/
    │   ├── getting-started.md
    │   └── troubleshooting.md
    └── research/
        ├── methodology.md
        └── findings.md
```

---

## Extending the system

The council pattern is domain-agnostic. Replacing `coaching_framework.md` with any structured domain knowledge document and adjusting the prompts in `council.py` adapts this to policy analysis, code review, lesson planning, or any other domain where multi-perspective critique adds value before synthesis.

---

## Hardware notes

Tested on a 16GB RAM laptop. 8B parameter models require approximately 5–6GB of RAM each. If you have a GPU, LM Studio will use it automatically and inference speed improves significantly. The 600-second API timeout accommodates CPU-only inference.

---

Author: Wayne Ellis — December 2025
