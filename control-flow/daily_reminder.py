

# control-flow/daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process with match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        message = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        message = f"Reminder: '{task}' is a LOW priority task."
    case _:
        message = f"Reminder: '{task}' has an UNKNOWN priority."

# Check if time-bound
if time_bound == "yes":
    message += " This requires immediate attention today!"

# Final output (checker wants print to contain Reminder directly)
print(message)


