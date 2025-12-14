# Rugby Council AI

An AI-powered coaching council that collaboratively designs rugby training sessions based on the Trojans RFC Coaching Framework.

## What This Does

Instead of asking a single AI model to design a session, this system creates a "council" of three different AI models that work together through a three-stage process:

**Stage 1 - Individual Plans**: Each model independently creates a complete session plan based on your parameters and the Trojans Coaching Framework.

**Stage 2 - Peer Review**: The models then review and critique all three plans (anonymously) and rank them based on how well they follow the framework.

**Stage 3 - Chairman Synthesis**: A designated "chairman" model reviews all the plans and all the critiques, then creates a final optimized session plan that incorporates the best ideas.

This approach produces better results than a single model because it combines multiple perspectives and includes a critical review process.

## Models Used

This project uses three local models running in LM Studio. The default configuration uses:

- **Analytical Coach**: Reasoning model for step-by-step analysis
- **Structured Coach**: Instruction-following model for framework adherence
- **Creative Coach**: Larger model for innovative solutions

The analytical model acts as chairman by default, synthesizing all input into the final plan.

**Note**: The actual model names are configured in `config.py`. Make sure the model names in the config file match exactly what you have loaded in LM Studio.

## Project Structure

```
rugby-council-ai/
├── council.py                 # Main orchestration script
├── config.py                  # Configuration settings
├── coaching_framework.md      # Trojans RFC Coaching Framework
├── requirements.txt           # Python dependencies
├── sessions/                  # Output folder (created automatically, git-ignored)
│   └── council_session_*.md  # Generated session plans (not committed)
├── venv/                      # Python virtual environment
└── README.md                  # This file
```

**Note**: The `sessions/` folder is intentionally excluded from git (via `.gitignore`) because it contains generated output files. Each user maintains their own session history locally. This prevents repository bloat and merge conflicts.

## Setup Instructions

### 1. LM Studio Setup

First, make sure LM Studio is installed and configured:

1. **Download models** (if you haven't already):
   - Open LM Studio
   - Download the models you want to use (check `config.py` for current configuration)
   - Example models that work well:
     - Any Mistral-based reasoning or instruct models
     - Larger models like GPT variants for creative thinking
     - Ensure model names in `config.py` match exactly what appears in LM Studio

2. **Start the local server**:
   - Click "Local Server" in the left sidebar
   - Click "Start Server"
   - Verify it shows `Running on http://localhost:1234`
   - Keep LM Studio open while running the council

**Important**: LM Studio can only run one model at a time. The script will pause between stages to let you switch models. This is normal and expected.

### 2. Python Environment Setup

Open VS Code with your project folder, then open the integrated terminal (Control + backtick).

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment**:
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On Mac/Linux:
   ```bash
   source venv/bin/activate
   ```
   
   You should see `(venv)` appear in your terminal prompt.

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run the Council

### Basic Usage

1. **Make sure LM Studio server is running** (see Setup above)

2. **In VS Code terminal, activate your virtual environment** if it's not already active

3. **Run the council**:
   ```bash
   python council.py
   ```

4. **Follow the prompts**:
   - The script will tell you which model to load in LM Studio
   - Switch to LM Studio, load the requested model
   - Return to terminal and press Enter
   - Repeat for each stage

### Customizing Session Parameters

To request a different type of session, edit the session parameters in `council.py`:

```python
# Near the bottom of council.py, around line 513
session_params = "60 minutes, U10s, 24 players, 4 coaches, focus on decision making around the breakdown"
```

Change this to whatever you need, for example:
- `"45 minutes, U8s, 16 players, 3 coaches, focus on passing and catching"`
- `"90 minutes, U12s, 30 players, 5 coaches, focus on defensive organization"`

### Configuring Models

To change which models are used or which model acts as chairman, edit `config.py`:

```python
# Change the chairman model
CHAIRMAN_MODEL = "reasoning"  # Can be "reasoning", "instruct", or "gpt"

# Adjust creativity level (0.0 = focused, 1.0 = creative)
TEMPERATURE = 0.7
```

## What to Expect During Execution

When you run the council, here's what happens:

1. **Initialization**: The script loads your coaching framework and parameters

2. **Stage 1**: For each model (about 5-10 minutes per model):
   - Script tells you which model to load
   - You switch models in LM Studio
   - Press Enter in terminal
   - Model generates a session plan
   - You see a preview of the response

3. **Stage 2**: Same process, but models are reviewing plans (3-5 minutes per model)

4. **Stage 3**: Chairman model creates final synthesis (5-10 minutes)

5. **Completion**: All outputs are saved to `sessions/council_session_TIMESTAMP.md`

**Total time**: Expect 30-45 minutes for a complete council session.

## Understanding the Output

The output file contains everything that happened during the council meeting:

### Individual Plans (Stage 1)
Each model's original session plan. Compare these to see how different models interpret the same framework and parameters.

### Peer Reviews (Stage 2)
Each model's critique of all three plans, including rankings. This is fascinating because you see what each model values in a good session plan.

### Final Plan (Stage 3)
The chairman's synthesized plan that combines the best elements. This is your ready-to-use session plan.

## Tips for Best Results

**Be specific with parameters**: Instead of "focus on skills", say "focus on passing under pressure and decision making at the breakdown". The more specific you are, the better the models can design to your needs.

**Review the individual plans**: Don't just jump to the final plan. Reading the individual responses and reviews gives you insights into different coaching approaches.

**Experiment with different chairmen**: Try running the same session request with different models as chairman. You'll see how each model synthesizes information differently.

**Compare with your own planning**: Use this as a coaching development tool. How does the council's approach compare to how you'd plan the session? What did they think of that you didn't?

## Troubleshooting

**"Cannot connect to LM Studio"**
- Make sure LM Studio is running
- Check that the server is started (should show green "Running" status)
- Verify it's on port 1234 (the default)

**"Request timed out"**
- The model is taking too long (>5 minutes)
- This can happen with very complex requests
- Try simplifying your session parameters
- Or try a smaller model

**"Wrong model loaded" responses**
- Make sure you're loading the exact model the script requests
- The model names in `config.py` must match LM Studio exactly
- Check for typos in model names

**Models giving generic responses**
- Check that `coaching_framework.md` exists in your project folder
- Make sure the framework file wasn't corrupted
- Try increasing `MAX_TOKENS` in `config.py` if responses seem cut off

**Script crashes with Python errors**
- Make sure you activated the virtual environment (`venv`)
- Check that you installed requirements: `pip install -r requirements.txt`
- Verify you're using Python 3.8 or newer: `python --version`

## Next Steps and Experiments

Once you have the basic council working, try these experiments:

**Test different council compositions**: What happens if you use three of the same model? Or two instruct models and one reasoning model?

**Vary the temperature**: Lower temperature (0.3-0.5) gives more consistent results. Higher temperature (0.8-0.9) gives more creative variety.

**Add more models**: If you download additional models to LM Studio, add them to `config.py` and expand your council.

**Different session types**: Try having the council plan pre-season fitness sessions vs. in-season tactical sessions vs. tournament preparation.

**Compare to your own plans**: Ask the council to plan a session you've already run, then compare approaches.

## Technical Notes for Future Development

This project uses a simple, synchronous approach where each API call blocks until complete. This makes the code easy to understand but means sessions take significant time.

Possible improvements:
- Add async/await for concurrent model calls (though LM Studio still processes one at a time)
- Implement a queueing system for model switches
- Add a web interface for easier interaction
- Store sessions in a database for analysis over time
- Add visualization of how reviews influenced the final plan

## Contributing

This is a personal learning project, but if you're interested in rugby coaching with AI, feel free to fork and experiment.

## License

This project is for educational and personal use with Trojans RFC.

---

**Project**: Systematic AI Delegation  
**Author**: Wayne  
**Date**: December 2024  
**Purpose**: Exploring multi-model collaboration for rugby coaching