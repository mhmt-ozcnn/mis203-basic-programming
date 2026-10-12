# Starting balance validation 
balance = int(input("Enter starting balance: "))
while balance < 0:
    print("Invalid input. Starting balance cannot be negative.")
    balance = float(input("Enter starting balance: "))

# Monthly deposit validation 
deposit = int(input("Enter monthly deposit: "))
while deposit <= 0:
    print("Invalid input. Deposit must be positive.")
    deposit = float(input("Enter monthly deposit: "))

# Monthly interest rate validation 
rate = int(input("Enter monthly interest rate (%): "))
while rate < 0:
    print("Invalid input. Interest rate cannot be negative.")
    rate = float(input("Enter monthly interest rate (%): "))

# Savings goal validation 
goal = int(input("Enter savings goal: "))
while goal <= 0:
    print("Invalid input. Goal must be positive.")
    goal = float(input("Enter savings goal: "))

print()

# Check if the starting balance already meets or exceeds the goal
if balance >= goal:
    print("Starting balance already meets or exceeds the savings goal.")
    print(f"Final balance: ${balance:.2f}")
    print("Total interest earned: $0.00")
else:
    total_interest = 0.0
    goal_reached = False
    months = 0

    print(f"{'Month':<7} | {'Interest Earned':<17} | {'Balance':<12}")

    for month in range(1, 61):
        months = month

        # Calculate interest on the current balance first
        monthly_interest = balance * (rate / 100.0)
        # Add both interest and deposit to the balance
        balance += monthly_interest + deposit
        total_interest += monthly_interest

        print(f"{month:<7} | ${monthly_interest:<16.2f} | ${balance:<11.2f}")

        # Break early if the balance reaches or exceeds the goal
        if balance >= goal:
            goal_reached = True
            break

    print("-" * 42)
    if goal_reached:
        print(f"Goal reached in {months} month(s)!")
    else:
        print("Goal was not reached within 60 months.")

    print(f"Final balance: ${balance:.2f}")
    print(f"Total interest earned: ${total_interest:.2f}")