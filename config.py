"""
Rugby Council AI - Configuration File

This file contains all the settings for your LLM Council.
Think of it as the roster for your coaching staff meeting - 
it defines who's on the team and what role each person plays.

You can easily modify these settings without touching the main code.
"""

# LM Studio Connection Settings
# This is the address where LM Studio's API server runs
# If you changed the port in LM Studio, update it here
LM_STUDIO_BASE_URL = "http://localhost:1234/v1"

# Council Model Configuration
# These are the exact model names as they appear in LM Studio
# IMPORTANT: You can only load one model at a time in LM Studio,
# so the script will pause between each model to give you time to switch

COUNCIL_MODELS = {
    "reasoning": {
        "name": "mistral-3-8b-reasoning",
        "description": "Reasoning model - good for step-by-step analysis",
        "role": "Analytical Coach"
    },
    "instruct": {
        "name": "mistral-3-8b", 
        "description": "Instruction-following model - good for structured responses",
        "role": "Structured Coach"
    },
    "gpt": {
        "name": "gpt-oss-20b",
        "description": "Larger general model - good for creative solutions",
        "role": "Creative Coach"
    }
}

# Chairman Configuration
# This model synthesizes all the responses into a final session plan
# The reasoning model is a good choice because it thinks through problems step-by-step
CHAIRMAN_MODEL = "reasoning"

# Session Design Temperature Settings
# Temperature controls randomness in responses:
# - Lower (0.3-0.5) = more focused and consistent
# - Higher (0.7-0.9) = more creative and varied
# For session design, we want some creativity but also consistency
TEMPERATURE = 0.7

# Maximum tokens per response
# This controls how long each model's response can be
# For session plans, we want detailed responses so this is set high
MAX_TOKENS = 2000

# Review stage settings
# When models critique each other, should they see the model names?
# Setting to False makes the review more objective
ANONYMIZE_REVIEWS = True