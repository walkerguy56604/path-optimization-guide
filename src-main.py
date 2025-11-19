import os
import re
from datetime import datetime

# === Configuration ===
# Automatically get today's date and build the log filename
today_str = datetime.now().strftime("%Y-%m-%d")
log_file_path = f"../daily_logs/{today_str}.md"  # Adjust folder if needed

# === Functions ===
def read_daily_log(file_path):
    """Read the content of the daily Markdown log."""
    if not os.path.exists(file_path):
        print(f"File {file_path} not found: {file_path}")
        return None
    with open(file_path, "r") as f:
        return f.read()

def extract_summary(log_content):
    """Extract simple summary: steps, calories, and key symptoms."""
    summary = {}
    
    # Extract steps from any mentions in the log
    steps_matches = re.findall(r"(\d+(?:,\d+)?) steps", log_content)
    summary['total_steps'] = sum(int(s.replace(",", "")) for s in steps_matches) if steps_matches else 0
    
    # Extract calories from any mentions in the log
    calories_matches = re.findall(r"(\d+) cal", log_content)
    summary['total_calories'] = sum(int(c) for c in calories_matches) if calories_matches else 0
    
    # Extract Symptoms section if it exists
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
# TODO: Parse tables for more structured analysis
# TODO: Generate charts with matplotlib
# TODO: Store extracted data in CSV or database for trends
