

def calculate_subtotal(items):
    #Return the sum of item price times quantity.
    return sum(price * quantity for price, quantity in items)


def discount_rate(subtotal):
    #Return 10% for orders of at least 500 TRY, otherwise 0%.
    if subtotal >= 500:
        return 0.10
    return 0.0


def shipping_fee(discounted_subtotal):
    #Return free shipping at 1000 TRY or more; otherwise 50 TRY.
    if discounted_subtotal >= 1000:
        return 0.0
    return 50.0


def final_total(subtotal, rate, shipping):
    #Return the discounted subtotal plus the shipping fee.
    return subtotal * (1 - rate) + shipping


# Assertions cover normal results and both pricing boundaries.
assert calculate_subtotal([(250, 2)]) == 500
assert discount_rate(499.99) == 0.0
assert discount_rate(500) == 0.10
assert shipping_fee(1000) == 0.0
assert final_total(500, 0.10, 50) == 500.0


orders = [
    {"name": "Small order", "items": [(120, 2), (80, 1)]},
    {"name": "Large order", "items": [(400, 2), (250, 1)]},
]

for order in orders:
    subtotal = calculate_subtotal(order["items"])
    rate = discount_rate(subtotal)
    discounted_subtotal = subtotal * (1 - rate)
    shipping = shipping_fee(discounted_subtotal)
    total = final_total(subtotal, rate, shipping)

    print(f"{order['name']}:")
    print(f"  Subtotal: {subtotal:.2f} TRY")
    print(f"  Discount: {rate:.0%}")
    print(f"  Shipping: {shipping:.2f} TRY")
    print(f"  Total: {total:.2f} TRY")


# print displays a value for a person. return gives a value back to the code
# that called a function, so the code can store or use it in calculations.
