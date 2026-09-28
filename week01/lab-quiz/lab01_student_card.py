#Input function getting information from user it stores 'string' data type.
#Print shows what we write in input.
get_name = input("What is your name: ")
get_id = int(input("What is your student ID: "))
get_dep = input("What is your Department: ")
get_git_username = input("What is your GitHub username: ")
get_goal = input("What is your programming goal: ")
print("---Student Introduction Card---\n")
print(f"* Name: {get_name}")
print(f"* Student ID: {get_id}")
print(f"* Department: {get_dep}")
print(f"* GitHub username: {get_git_username}")
print(f"* Your programming goal: {get_goal}")
