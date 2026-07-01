import argparse
import os
from agent.skills.analyze_skill import run_analysis
from agent.skills.mvp_skill import generate_mvp
from agent.skills.experiment_skill import design_experiment

def main():
    parser = argparse.ArgumentParser(description="Discovery Agent CLI")
    parser.add_argument("command", choices=["analyze", "experiment", "mvp"], help="Command to run")
    parser.add_argument("--case", required=True, help="Path to the study case directory")
    
    args = parser.parse_args()
    
    if args.command == "analyze":
        run_analysis(args.case)
    elif args.command == "experiment":
        design_experiment(args.case)
    elif args.command == "mvp":
        generate_mvp(args.case)
    else:
        print(f"Command '{args.command}' is not yet implemented.")

if __name__ == "__main__":
    main()
