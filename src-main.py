import os
import re

# === Configuration ===
log_file_path = "../daily_logs/2025-11-18.md"  # adjust path as needed

# === Functions ===
def read_daily_log(file_path):
    """Read the content of the daily Markdown log."""
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return None
    with open(file_path, "r") as f:
        return f.read()

def extract_summary(log_content):
    """Extract simple summary: steps, calories, and key symptoms."""
    summary = {}
    
    # Extract steps from Activity Log table or quick entries
    steps_matches = re.findall(r"(\d+(?:,\d+)?) steps", log_content)
    summary['total_steps'] = sum(int(s.replace(",", "")) for s in steps_matches) if steps_matches else 0
    
    # Extract calories from Nutrition Log table or quick entries
    calories_matches = re.findall(r"(\d+) cal", log_content)
    summary['total_calories'] = sum(int(c) for c in calories_matches) if calories_matches else 0
    
    # Extract key symptoms
    symptoms_section = re.search(r"## 4\. Symptoms / Health Notes(.*?)##", log_content, re.DOTALL)
    summary['symptoms'] = symptoms_section.group(1).strip() if symptoms_section else "No symptoms recorded"
    
    return summary

# === Main Execution ===
log_content = read_daily_log(log_file_path)
if log_content:
    summary = extract_summary(log_content)
    print("=== Daily Summary ===")
    print(f"Total Steps: {summary['total_steps']}")
    print(f"Total Calories: {summary['total_calories']}")
    print("Key Symptoms / Notes:")
    print(summary['symptoms'])
else:
    print("No log content to process.")

# === Future Enhancements ===
# TODO: Parse tables for detailed analysis
# TODO: Generate charts with matplotlib
# TODO: Store extracted data in CSV or database for trends
