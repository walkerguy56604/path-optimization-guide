import os

# Path to the daily log (adjust as needed)
log_file_path = "../daily_logs/2025-11-18.md"

def read_daily_log(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return None
    with open(file_path, "r") as f:
        content = f.read()
    return content

# Test reading
log_content = read_daily_log(log_file_path)
if log_content:
    print("Daily log loaded successfully!")
