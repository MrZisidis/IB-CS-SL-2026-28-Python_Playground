# try:
#     # Attempt to convert the user's input into a number
#     age = int(input("enter your age: "))
#     print(age)
#     number1 = int(input("enter your first number: "))
#     number2 = int(input("enter your second number: "))
#     result = number1/number2
# except ValueError:
#     # This runs if the input is not a valid number
#     print("Invalid number. Please enter digits.")
# except ZeroDivisionError:
#     # This runs if the input is not a valid number
#     print("Invalid division.")
# finally:
#     # This always runs
#    print("Input attempt finished.")

try:
   total = 120
   people = 0
   share = people //total
   print(share)
except ZeroDivisionError:
   print("Cannot divide by zero")