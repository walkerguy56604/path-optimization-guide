import os
import re
from datetime import datetime

# === Configuration ===
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
    
    # Quick entries: steps
    steps_matches = re.findall(r"(\d+(?:,\d+)?) steps", log_content)
    summary['total_steps'] = sum(int(s.replace(",", "")) for s in steps_matches) if steps_matches else 0
    
    # Quick entries: calories
    calories_matches = re.findall(r"(\d+) cal", log_content)
    summary['total_calories'] = sum(int(c) for c in calories_matches) if calories_matches else 0
    
    # Symptoms section
    symptoms_section = re.search(r"## 4\. Symptoms / Health Notes(.*?)##", log_content, re.DOTALL)
    summary['symptoms'] = symptoms_section.group(1).strip() if symptoms_section else "No symptoms recorded"
    
    return summary

def parse_table(log_content, table_title):
    """Basic placeholder to extract table content by section title."""
    pattern = rf"## {table_title}(.*?)(\n##|\Z)"
    match = re.search(pattern, log_content, re.DOTALL)
    if not match:
        return None
    table_text = match.group(1).strip()
    # Split lines and remove empty lines
    lines = [line.strip().split("|")[1:-1] for line in table_text.split("\n") if "|" in line]
    return lines

# === Main Execution ===
log_content = read_daily_log(log_file_path)
if log_content:
    summary = extract_summary(log_content)
    print("=== Daily Summary ===")
    print(f"Total Steps: {summary['total_steps']}")
    print(f"Total Calories: {summary['total_calories']}")
    print("Key Symptoms / Notes:")
    print(summary['symptoms'])
    
    # Example: parse today's Activity Log table
    activity_table = parse_table(log_content, "Activity Log")
    if activity_table:
        print("\nActivity Table Found:")
        for row in activity_table:
            print(row)
    else:
        print("\nNo Activity Table Found.")
    
else:
    print("No log content to process.")

# === Future Enhancements ===
# TODO: Automatically calculate steps/calories from tables
# TODO: Generate charts with matplotlib
# TODO: Store extracted data in CSV or database for trends
