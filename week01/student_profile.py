# Collect user details using input function.
name = input("Enter your name: ")
department = input("Enter your department: ")
age = input("Enter your age: ")
career_goal = input("Enter your career goal: ")

# Display the formatted profile and i used here 'f string method' for printing variables also used '\n' method for adding newline for output.
print("--- Student Profile ---")
print(f"\nName: {name}")
print(f"Department: {department}")
print(f"Age: {age}")
print(f"Career Goal: {career_goal}")