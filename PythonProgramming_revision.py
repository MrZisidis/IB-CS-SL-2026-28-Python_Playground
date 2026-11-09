# Write a program that repeatedly asks for item prices until the user enters q.
# Then display the number of items, the total,# and the average price.
# Give a 20% discount if the total is over €100.
# Reject non-numeric entries with a clear message,
# and handle the case where no prices were entered.
#
# Before calling it complete, test:
#
# q immediately;
# one price;
# several prices whose total is exactly €100;
# several prices whose total is above €100;
# invalid text instead of a price.

item_prices = 0
while item_prices != "q":

# while True:
    item_prices = (input("Enter your item price: "))
    if item_prices == "q":
        break
    try:
        item_prices = float(item_prices)
    except:
        print("Please enter a numeric value")


print("Thank you for using the program")