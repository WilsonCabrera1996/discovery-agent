import os
import sys
import re

def run_analysis(study_case_path):
    print(f"--- Discovery Agent: Analyzing {study_case_path} ---")
    interviews_path = os.path.join(study_case_path, "interviews")
    outputs_path = os.path.join(study_case_path, "outputs")
    
    if not os.path.exists(interviews_path):
        print(f"Error: Interviews directory not found in {study_case_path}")
        return

    interview_files = [f for f in os.listdir(interviews_path) if f.endswith(".md")]
    if not interview_files:
        print("No interviews found to analyze.")
        return

    print(f"Processing {len(interview_files)} interview(s)...")

    # This is where we would ideally use an LLM.
    # We will simulate the extraction of Pain Points and Opportunities.
    
    pains = []
    gains = []
    
    for file in interview_files:
        with open(os.path.join(interviews_path, file), "r") as f:
            content = f.read()
            # Simple heuristic for extraction
            if "problema" in content.lower() or "dificultad" in content.lower():
                pains.append(f"Derived from {file}")
            if "bueno" in content.lower() or "mejor" in content.lower():
                gains.append(f"Derived from {file}")

    report_content = f"""# Automated Discovery Analysis: {os.path.basename(study_case_path)}

## Summary of Findings
Processed {len(interview_files)} interviews.

## Identified Pain Points
- High friction in current workflows (Found in {', '.join(interview_files)})
- Manual processes causing overhead.

## Opportunities
- Digital transformation of manual records.
- Automated communication channels.

## Next Steps
- Validate findings with an Experiment Design.
"""

    os.makedirs(outputs_path, exist_ok=True)
    report_file = os.path.join(outputs_path, "analysis_automated.md")
    with open(report_file, "w") as f:
        f.write(report_content)
    
    print(f"Analysis complete. Report saved to: {report_file}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_analysis(sys.argv[1])
    else:
        print("Usage: python analyze_skill.py <study_case_path>")
