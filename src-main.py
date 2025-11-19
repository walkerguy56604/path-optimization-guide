# === Print Summary ===
summary_text = f"""
=== Daily Summary ===
Steps from Quick Entries: {summary['quick_steps']}
Steps from Activity Log Table: {total_table_steps}
GRAND TOTAL STEPS: {grand_total_steps}

Calories from Quick Entries: {summary['quick_calories']}
Calories from Nutrition Log Table: {total_table_calories}
GRAND TOTAL CALORIES: {grand_total_calories}

Key Symptoms / Notes:
{summary['symptoms']}
"""

print(summary_text)

# === Save Summary to File ===
output_file_path = f"../daily_logs/{today_str}_summary.txt"  # Adjust folder if needed
with open(output_file_path, "w") as f:
    f.write(summary_text)

print(f"Daily summary saved to {output_file_path}")
