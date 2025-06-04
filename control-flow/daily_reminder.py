# Prompt the user for task information
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Output a customized reminder using match-case and if conditions
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Try to handle it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Plan to do it soon.")
    case "low":
        if time_bound == "yes":
            print(f"\nNote: '{task}' is a low priority task, but it's time-sensitive. Don’t forget to do it today!")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("\nInvalid priority entered. Please enter high, medium, or low.")

