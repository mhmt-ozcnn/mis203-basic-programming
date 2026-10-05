order_amount = input("Order amount (TRY): ").strip()
available_stock = input("Available stock: ").strip()
requested_quantity = input("Requested quantity: ").strip()
is_member = input("Is the customer a member? (yes/no): ").strip().lower()

if not order_amount.replace(".", "", 1).isdigit(): # its check if there is a decimal '.' or text it will return invalid order amount.
    print("Invalid order amount.")
elif not available_stock.isdigit(): # it should be a integer this code check this.
    print("Invalid available stock.")
elif not requested_quantity.isdigit(): # it should be a integer.
    print("Invalid requested quantity.")
else: #converting values float and int.
    order_amount = float(order_amount) 
    available_stock = int(available_stock)
    requested_quantity = int(requested_quantity)
#its check the conditions. and output results.
    if requested_quantity <= 0:
        print("Order rejected: requested quantity must be greater than zero.")
    elif requested_quantity > available_stock:
        print("Order rejected: insufficient stock.")
    elif is_member not in ["yes", "no"]:
        print("Please answer yes or no for membership.")
    elif is_member == "yes" and order_amount >= 500:
        final_price = order_amount * 0.90
        print("Order approved: member discount applied.")
        print(f"Final price: {final_price:.2f} TRY")
    else:
        final_price = order_amount
        print("Order approved: stock is available.")
        print(f"Final price: {final_price:.2f} TRY")
