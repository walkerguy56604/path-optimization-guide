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
    """Extract summary: steps, calories, and key symptoms."""
    summary = {}
    
    # Quick entries: steps
    steps_matches = re.findall(r"(\d+(?:,\d+)?) steps", log_content)
    quick_steps = sum(int(s.replace(",", "")) for s in steps_matches) if steps_matches else 0
    summary['quick_steps'] = quick_steps
    
    # Quick entries: calories
    calories_matches = re.findall(r"(\d+) cal", log_content)
    summary['total_calories'] = sum(int(c) for c in calories_matches) if calories_matches else 0
    
    # Symptoms section
    symptoms_section = re.search(r"## 4\. Symptoms / Health Notes(.*?)##", log_content, re.DOTALL)
    summary['symptoms'] = symptoms_section.group(1).strip() if symptoms_section else "No symptoms recorded"
    
    return summary

def parse_table(log_content, table_title):
    """Basic table parser by section title."""
    pattern = rf"## {table_title}(.*?)(\n##|\Z)"
    match = re.search(pattern, log_content, re.DOTALL)
    if not match:
        return None
    table_text = match.group(1).strip()
    lines = [line.strip().split("|")[1:-1] for line in table_text.split("\n") if "|" in line]
    return lines

def sum_steps_from_activity_table(table_lines):
    """Sum all steps in the Activity Log table."""
    total = 0
    for row in table_lines[1:]:  # Skip header
        try:
            steps = int(row[2].strip())  # Steps are in column 3
            total += steps
        except ValueError:
            continue  # Ignore non-integer entries
    return total

# === Main Execution ===
log_content = read_daily_log(log_file_path)
if log_content:
    summary = extract_summary(log_content)
    print("=== Daily Summary ===")
    print(f"Steps from Quick Entries: {summary['quick_steps']}")
    print(f"Total Calories: {summary['total_calories']}")
    print("Key Symptoms / Notes:")
    print(summary['symptoms'])
    
    # Parse Activity Log table
    activity_table = parse_table(log_content, "Activity Log")
    if activity_table:
        total_table_steps = sum_steps_from_activity_table(activity_table)
        print(f"Steps from Activity Log Table: {total_table_steps}")
    else:
        print("No Activity Log table found.")
else:
    print("No log content to process.")

# === Future Enhancements ===
# TODO: Parse Nutrition Log table for calories per meal
# TODO: Generate charts with matplotlib
# TODO: Store extracted data in CSV or database for trends
