
def calculate_order(product, price=100, *quantities, **additional_order):
    print(f"Product Name: {product}")
    print(f"Price: {price}")
    print(f"Total Quantity: {sum(quantities)}")

    print("\nAdditional Order Details:")
    for key, value in additional_order.items():
        print(f"{key}: {value}")


calculate_order(
    "Laptop",
    50000,
    1, 2,
    customer="Sohel",
    city="Dhaka"
)