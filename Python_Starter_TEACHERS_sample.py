# Step 1: Define your function header with two parameters
def calculate_total(price, tax_rate):
    # Step 2: Calculate total and return it
    total = price + (price * tax_rate)
    return total

def calculate_discounted_total(price,tax,discount):
    # new_total = total - discount
    new_total = calculate_total(price,tax) - discount*price
    return new_total

#main code
# Step 3: Call function with $25.00 price and 0.05 tax rate
shirt_price = calculate_total(25.00, 0.05)
print(shirt_price)  # Expected Output: 26.25
# Step 4: Call function with $100.00 price and 0.10 tax rate
print(calculate_total(100.00, 0.10))  # Expected Output: 110.0

print(calculate_discounted_total(100,0.10,0.10))

