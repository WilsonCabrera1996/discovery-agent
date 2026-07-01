import os
import sys

def design_experiment(study_case_path):
    print(f"--- Discovery Agent: Designing Experiment for {study_case_path} ---")
    analysis_path = os.path.join(study_case_path, "outputs", "analysis.md")
    if not os.path.exists(analysis_path):
        # Fallback to automated analysis
        analysis_path = os.path.join(study_case_path, "outputs", "analysis_automated.md")
    
    if not os.path.exists(analysis_path):
        print(f"Error: No analysis report found. Run 'analyze' first.")
        return

    outputs_path = os.path.join(study_case_path, "outputs")
    experiment_file = os.path.join(outputs_path, "experiment_design.md")

    # Simulated Experiment Design
    experiment_content = """# Experiment Design: WhatsApp Reminder Pilot

## Hypothesis
If we automate reminders via WhatsApp, then we will reduce no-shows by 20%.

## Method
1. Select 20 patients for next week.
2. Send manual WhatsApp messages using a standard template.
3. Compare no-show rate with the previous week.

## Metrics
- No-show rate (%).
- Time spent on reminders (minutes).
"""

    with open(experiment_file, "w") as f:
        f.write(experiment_content)
    
    print(f"Experiment Design complete. Saved to: {experiment_file}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        design_experiment(sys.argv[1])
    else:
        print("Usage: python experiment_skill.py <study_case_path>")
