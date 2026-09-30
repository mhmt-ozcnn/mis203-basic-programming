base_price = 0
total_revenue = 0
free_tickets = 0
tickets_sold = 0
while True:
    customer_name = input("Customer name (or q to quit): ")

    if customer_name == "q" or customer_name == "Q":
        break
    get_age = input("Age: ")
    if not get_age.isdigit(): #if someone write down a letter age section there is probably execute error so i added here this controlling syntax.
        print("Invalid age.")
        continue
    age = int(get_age)
    if age < 0 or age > 120:
        print("Invalid age.")
        continue
    day = input("Day (weekday/weekend): ").strip().lower() #strip removes spaces and the lower function trasnform each letter lower case.

    if day not in ["weekend", "weekday"]: #its check there is different day name.
        print("Invalid day.")
        continue
    check_student = input("Student (yes/no): ").strip().lower()

    if check_student not in ["yes", "no"]:
        print("Please answer yes or no.")
        continue
    if day == "weekday":
        base_price = 200
    else:
        base_price = 250
    category = "Standard"
    discount = 0.0

    if age < 6 :
        category = "Free"
        discount = 1
    elif age >= 65:
        category = "Senior"
        discount = 0.5
    elif 6 <= age <= 12 :
        category = "Child"
        discount = 0.4
    elif check_student == "yes" and age <=25 :
        category = "Student"
        discount = 0.3
    else:
        category = "Standard"
        discount = 0
    price = base_price * (1.0 - discount) #ticket calculation
    total_revenue += price
    tickets_sold += 1
    if price == 0 :
        free_tickets += 1

    print(f"{customer_name}: {price:.2f} TRY ({category})")
if tickets_sold == 0:
    print ("No tickets sold.")
else:
    avg_price = total_revenue / tickets_sold
    print(
        f"Tickets sold: {tickets_sold} "
        f"Total revenue: {total_revenue:.2f} TRY "
        f"Average price: {avg_price:.2f} TRY "
        f"Free tickets: {free_tickets}"
    )