from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Part 2: Calculate a future date
def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main execution
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
