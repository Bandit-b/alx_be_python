# Mad Libs Story Generator with Conditional Statements

# Prompt the user for descriptive words
weather = input("What is the weather like today? (e.g., sunny, rainy): ").lower()
adjective1 = input("Enter an adjective (to describe a day): ")
adjective2 = input("Enter another adjective (to describe a monkey): ")
adjective3 = input("Enter a third adjective (to describe a lion): ")
adjective4 = input("Enter one more adjective (to describe an experience): ")

# Conditional twist: Customize the opening based on the weather
if weather == "sunny":
    intro = "It was a bright and cheerful day."
elif weather == "rainy":
    intro = "Despite the gloomy rain, I decided to explore."
else:
    intro = f"It was a rather {weather} day, but I felt adventurous."

# Construct the Mad Libs story
story = (
    f"{intro} On a beautiful {adjective1} day, I went to the zoo. "
    f"I saw a funny {adjective2} monkey swinging from the trees. "
    f"Then, I spotted a majestic {adjective3} lion lounging in the sun. "
    f"What a wild and {adjective4} experience!"
)

# Print the final story
print("\n--- Your Mad Libs Story ---\n")
print(story)
