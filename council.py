"""
Rugby Council AI - Main Orchestration Script

This script orchestrates a "council" of AI models to collaboratively design
rugby training sessions based on the Trojans RFC Coaching Framework.

The process works in three stages:
1. Each model independently creates a session plan
2. Each model reviews and critiques all the plans (anonymously)
3. A chairman model synthesizes everything into a final plan

Author: Wayne (with AI assistance)
Date: December 2024
"""

import requests
import json
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List
import config

# Load the Trojans Coaching Framework
# This reads your framework file so models have the context they need
def load_coaching_framework() -> str:
    """
    Loads the Trojans Coaching Framework from file.
    Returns the framework as a string to include in prompts.
    """
    framework_path = Path(__file__).parent / "coaching_framework.md"
    
    if not framework_path.exists():
        print(f"⚠️  Warning: Coaching framework not found at {framework_path}")
        print("   Using basic framework template instead.")
        return "Basic rugby coaching principles apply."
    
    with open(framework_path, 'r', encoding='utf-8') as f:
        return f.read()


def call_lm_studio(prompt: str, model_name: str, temperature: float = 0.7) -> str:
    """
    Makes an API call to LM Studio to get a response from a model.
    
    This function handles all the technical details of talking to LM Studio.
    Think of it as your messenger that carries questions to the models
    and brings back their answers.
    
    Args:
        prompt: The question or instruction to send to the model
        model_name: Which model to use (must match name in LM Studio)
        temperature: How creative vs focused (0.0 = focused, 1.0 = creative)
    
    Returns:
        The model's response as a string
    """
    
    # Prepare the request payload
    # This is the data we're sending to LM Studio
    # It follows the OpenAI API format, which LM Studio understands
    payload = {
        "model": model_name,  # Which model to use
        "messages": [
            {
                "role": "user",  # We're the user asking a question
                "content": prompt  # This is what we're asking
            }
        ],
        "temperature": temperature,  # Controls randomness
        "max_tokens": config.MAX_TOKENS,  # Maximum length of response
        "stream": False  # We want the complete response, not streaming
    }
    
    try:
        # Send the request to LM Studio
        # This is like knocking on LM Studio's door and handing over the question
        response = requests.post(
            f"{config.LM_STUDIO_BASE_URL}/chat/completions",
            json=payload,
            timeout=300  # Wait up to 5 minutes for a response
        )
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Extract the actual text response from the JSON reply
        # LM Studio wraps the response in a specific format
        result = response.json()
        return result['choices'][0]['message']['content']
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Cannot connect to LM Studio")
        print("   Make sure LM Studio is running and the server is started")
        print(f"   Expected URL: {config.LM_STUDIO_BASE_URL}")
        raise
        
    except requests.exceptions.Timeout:
        print("\n❌ Error: Request timed out")
        print("   The model took too long to respond (>5 minutes)")
        raise
        
    except Exception as e:
        print(f"\n❌ Error calling LM Studio API: {e}")
        raise


def wait_for_model_switch(model_name: str):
    """
    Pauses the script to give you time to switch models in LM Studio.
    
    Since LM Studio can only run one model at a time, you need to manually
    switch between models during the Council process. This function makes
    that clear and gives you time to do it.
    """
    print(f"\n{'='*70}")
    print(f"⏸️  PLEASE LOAD MODEL IN LM STUDIO:")
    print(f"   {model_name}")
    print(f"{'='*70}")
    print("\nSteps:")
    print("1. Go to LM Studio")
    print("2. Click on the model in the left sidebar")
    print("3. Wait for it to load (you'll see it in the chat interface)")
    print("4. Come back here and press Enter to continue")
    print(f"{'='*70}")
    input("\nPress Enter when ready...")


def stage_1_individual_responses(session_params: str, framework: str) -> Dict[str, str]:
    """
    STAGE 1: Get individual session plans from each model.
    
    Each model works independently, like asking three coaches to each
    design a session without seeing what the others are doing.
    
    Args:
        session_params: The session requirements (e.g., "60 mins, U10s, 24 players...")
        framework: The Trojans Coaching Framework text
    
    Returns:
        Dictionary mapping model names to their responses
    """
    print("\n" + "="*70)
    print("STAGE 1: INDIVIDUAL SESSION PLANS")
    print("="*70)
    print("\nAsking each model to independently design a session...")
    
    responses = {}
    
    # Create the prompt that all models will receive
    # This ensures they all have the same information to work with
    prompt = f"""You are an experienced rugby coach working with Trojans RFC.

COACHING FRAMEWORK:
{framework}

SESSION PARAMETERS:
{session_params}

Your task is to design a complete training session that:
1. Follows the Trojans Coaching Framework principles
2. Incorporates all five Trojans Coaching Habits (Shared Purpose, Progression, Praise, Review, Choice)
3. Aligns with TREDS values and APES principles
4. Meets the specified session parameters

Please provide a detailed session plan including:
- Session objectives linked to the Player Framework
- Warm-up activity
- Main skill development activities (with progressions using STEP)
- Game-based activity
- Cool-down and review
- Specific coaching points for each activity
- How the five coaching habits are integrated

Be specific and practical - this should be a plan a coach can actually use."""

    # Loop through each model and get their response
    for model_key, model_info in config.COUNCIL_MODELS.items():
        print(f"\n📝 Requesting plan from {model_info['role']} ({model_key})...")
        
        # Pause for model switching
        wait_for_model_switch(model_info['name'])
        
        # Get the response
        response = call_lm_studio(prompt, model_info['name'], config.TEMPERATURE)
        responses[model_key] = response
        
        # Show a preview of the response
        preview = response[:200] + "..." if len(response) > 200 else response
        print(f"✅ Received plan ({len(response)} characters)")
        print(f"   Preview: {preview}")
    
    return responses


def truncate_plan_for_review(plan: str, max_chars: int = 3000) -> str:
    """
    Intelligently truncates a session plan for review to stay within context limits.
    
    This keeps the beginning (objectives, structure) and end (coaching points, summary)
    while noting that middle sections are abbreviated.
    
    Args:
        plan: The full session plan text
        max_chars: Maximum characters to keep
    
    Returns:
        Truncated version that preserves key information
    """
    if len(plan) <= max_chars:
        return plan
    
    # Keep first 60% and last 20% of the character limit
    # This preserves objectives at start and summary at end
    first_section = int(max_chars * 0.6)
    last_section = int(max_chars * 0.2)
    
    truncated = (
        plan[:first_section] + 
        f"\n\n[... middle sections abbreviated for length ...]\n\n" +
        plan[-last_section:]
    )
    
    return truncated


def stage_2_peer_review(responses: Dict[str, str], framework: str) -> Dict[str, str]:
    """
    STAGE 2: Each model reviews all the plans (including their own).
    
    The plans are anonymized so models can't play favorites.
    Each model ranks the plans and provides constructive feedback.
    
    NOTE: Session plans are truncated to fit within context window limits.
    This preserves the key structural elements while reducing overall size.
    
    Args:
        responses: Dictionary of model responses from Stage 1
        framework: The Trojans Coaching Framework text
    
    Returns:
        Dictionary mapping model names to their review responses
    """
    print("\n" + "="*70)
    print("STAGE 2: PEER REVIEW")
    print("="*70)
    print("\nEach model will now review all three plans...")
    print("(Plans are truncated to fit context limits while preserving key info)")
    
    reviews = {}
    
    # Create anonymized versions of the plans for review
    # This removes bias by hiding which model created which plan
    plan_labels = ['Plan A', 'Plan B', 'Plan C']
    model_keys = list(responses.keys())
    
    # Build the plans section for the review prompt
    # Truncate each plan to avoid context window issues
    plans_text = ""
    for label, model_key in zip(plan_labels, model_keys):
        truncated_plan = truncate_plan_for_review(responses[model_key], max_chars=3000)
        plans_text += f"\n{'='*70}\n"
        plans_text += f"{label}:\n\n{truncated_plan}\n"
        
        # Show truncation info
        original_length = len(responses[model_key])
        truncated_length = len(truncated_plan)
        if original_length > truncated_length:
            print(f"   {label}: truncated from {original_length} to {truncated_length} chars")
    
    # Create the review prompt
    review_prompt = f"""You are reviewing three different rugby session plans for Trojans RFC.

COACHING FRAMEWORK:
{framework}

SESSION PLANS TO REVIEW:
{plans_text}

Your task is to:
1. Evaluate each plan against the Trojans Coaching Framework
2. Identify strengths and weaknesses in each plan
3. Rank the plans from best to worst (1st, 2nd, 3rd)
4. Provide specific constructive feedback

Consider:
- How well does each plan incorporate the five Coaching Habits?
- Does each plan align with TREDS values and APES principles?
- Are the activities age-appropriate and engaging for U10s?
- Is there clear progression using STEP?
- Are the plans practical and executable?

Provide your review in this format:
**Rankings:**
1st: [Plan X] - [brief reason]
2nd: [Plan Y] - [brief reason]
3rd: [Plan Z] - [brief reason]

**Detailed Feedback:**
[Your detailed analysis of strengths and weaknesses of each plan]

**Recommended Improvements:**
[Specific suggestions for how to improve the plans]"""

    # Get each model's review
    for model_key, model_info in config.COUNCIL_MODELS.items():
        print(f"\n📊 Requesting review from {model_info['role']} ({model_key})...")
        
        wait_for_model_switch(model_info['name'])
        
        review = call_lm_studio(review_prompt, model_info['name'], config.TEMPERATURE)
        reviews[model_key] = review
        
        print(f"✅ Received review ({len(review)} characters)")
    
    return reviews


def stage_3_chairman_synthesis(
    responses: Dict[str, str], 
    reviews: Dict[str, str],
    session_params: str,
    framework: str
) -> str:
    """
    STAGE 3: Chairman model synthesizes all input into final plan.
    
    The chairman reviews all the original plans and all the critiques,
    then creates a final session plan that incorporates the best ideas
    and addresses the identified weaknesses.
    
    NOTE: Plans and reviews may be truncated to fit context window limits.
    
    Args:
        responses: Original session plans from Stage 1
        reviews: Peer reviews from Stage 2
        session_params: Original session parameters
        framework: The Trojans Coaching Framework text
    
    Returns:
        The final synthesized session plan
    """
    print("\n" + "="*70)
    print("STAGE 3: CHAIRMAN SYNTHESIS")
    print("="*70)
    
    chairman_info = config.COUNCIL_MODELS[config.CHAIRMAN_MODEL]
    print(f"\n🎯 {chairman_info['role']} will now create the final plan...")
    print("(Content may be truncated to fit context limits)")
    
    # Compile all the information for the chairman
    # Truncate individual plans to manage context window
    all_plans = ""
    for model_key, response in responses.items():
        model_role = config.COUNCIL_MODELS[model_key]['role']
        truncated_plan = truncate_plan_for_review(response, max_chars=2500)
        all_plans += f"\n{'='*70}\n"
        all_plans += f"Plan from {model_role}:\n\n{truncated_plan}\n"
    
    # Keep reviews at full length since they're typically shorter
    all_reviews = ""
    for model_key, review in reviews.items():
        model_role = config.COUNCIL_MODELS[model_key]['role']
        # Truncate reviews too if needed, but with a higher limit
        truncated_review = truncate_plan_for_review(review, max_chars=4000)
        all_reviews += f"\n{'='*70}\n"
        all_reviews += f"Review from {model_role}:\n\n{truncated_review}\n"
    
    # Create the synthesis prompt
    synthesis_prompt = f"""You are the Chairman of the Trojans RFC coaching council.

You have received three independent session plans and peer reviews from your coaching team.
Your task is to synthesize these into a single, optimized session plan.

COACHING FRAMEWORK:
{framework}

SESSION PARAMETERS:
{session_params}

ORIGINAL PLANS:
{all_plans}

PEER REVIEWS:
{all_reviews}

Based on all this input, create a final session plan that:
1. Incorporates the best ideas from all three plans
2. Addresses weaknesses identified in the reviews
3. Fully embodies the Trojans Coaching Framework
4. Is practical, detailed, and ready to use

Provide the final plan in the same format as requested in Stage 1:
- Session objectives
- Warm-up activity
- Main skill development activities (with STEP progressions)
- Game-based activity
- Cool-down and review
- Coaching points
- Integration of the five Coaching Habits

Make this the best possible session for these players."""

    wait_for_model_switch(chairman_info['name'])
    
    final_plan = call_lm_studio(synthesis_prompt, chairman_info['name'], config.TEMPERATURE)
    
    print(f"✅ Final plan created ({len(final_plan)} characters)")
    
    return final_plan


def save_council_session(
    session_params: str,
    responses: Dict[str, str],
    reviews: Dict[str, str],
    final_plan: str
):
    """
    Saves all the Council outputs to a file for review.
    
    This creates a complete record of the entire Council meeting:
    what each model said, how they reviewed each other, and the final plan.
    """
    # Create sessions directory if it doesn't exist
    sessions_dir = Path(__file__).parent / "sessions"
    sessions_dir.mkdir(exist_ok=True)
    
    # Create filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = sessions_dir / f"council_session_{timestamp}.md"
    
    # Build the output content
    content = f"""# Rugby Council AI - Session Output

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

**Session Parameters:** {session_params}

---

## STAGE 1: Individual Plans

"""
    
    for model_key, response in responses.items():
        model_info = config.COUNCIL_MODELS[model_key]
        content += f"### {model_info['role']} ({model_key})\n\n{response}\n\n---\n\n"
    
    content += "## STAGE 2: Peer Reviews\n\n"
    
    for model_key, review in reviews.items():
        model_info = config.COUNCIL_MODELS[model_key]
        content += f"### Review by {model_info['role']} ({model_key})\n\n{review}\n\n---\n\n"
    
    content += "## STAGE 3: Final Synthesized Plan\n\n"
    content += final_plan
    
    # Save to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n💾 Session saved to: {filename}")
    return filename


def run_council(session_params: str):
    """
    Main function that orchestrates the entire Council process.
    
    This is the conductor of the orchestra - it calls each stage in order
    and coordinates all the models working together.
    """
    print("\n" + "="*70)
    print("🏉 RUGBY COUNCIL AI - SESSION PLANNER")
    print("="*70)
    print(f"\nSession Parameters: {session_params}")
    print(f"Models in Council: {len(config.COUNCIL_MODELS)}")
    print(f"Chairman: {config.COUNCIL_MODELS[config.CHAIRMAN_MODEL]['role']}")
    
    # Load the coaching framework
    framework = load_coaching_framework()
    print(f"Coaching Framework: Loaded ({len(framework)} characters)")
    
    # Run the three stages
    responses = stage_1_individual_responses(session_params, framework)
    reviews = stage_2_peer_review(responses, framework)
    final_plan = stage_3_chairman_synthesis(responses, reviews, session_params, framework)
    
    # Save everything
    output_file = save_council_session(session_params, responses, reviews, final_plan)
    
    print("\n" + "="*70)
    print("✅ COUNCIL COMPLETE")
    print("="*70)
    print(f"\nAll outputs saved to: {output_file}")
    print("\nYou can now review:")
    print("- Individual plans from each model")
    print("- Peer reviews and rankings")
    print("- Final synthesized session plan")


if __name__ == "__main__":
    """
    This is the entry point when you run the script.
    
    You can modify the session_params below to request different sessions.
    Format: "duration, age group, player count, coach count, focus areas"
    """
    
    # Example session request
    # Modify this to request different types of sessions
    session_params = "60 minutes, U10s, 24 players, 4 coaches, focus on decision making around the breakdown"
    
    try:
        run_council(session_params)
    except KeyboardInterrupt:
        print("\n\n⏹️  Council interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        print("\nPlease check that:")
        print("1. LM Studio is running")
        print("2. The server is started in LM Studio")
        print("3. The model names in config.py match LM Studio exactly")