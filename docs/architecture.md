# Architecture

This document provides a high-level overview of the Rugby Council AI architecture.

- Orchestration: `council.py` coordinates the council stages (individual plans, peer review, synthesis).
- Models: Configured in `config.py` and accessed via LM Studio.
- Data: Sessions are stored in `sessions/` (gitignored) while curated examples live in `examples/`.
- Documentation: All user-facing docs live in `docs/`.