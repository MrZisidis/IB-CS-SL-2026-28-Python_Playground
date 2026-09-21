wage= float(input("Hourly Wage:"))
hours = float(input("Hours Worked:"))
day= input("Day of the week:").lower()
if day== "sunday":
    print(wage*hours*2)
else:
    print(wage*hours)

# number= int(input("Please type in a number: "))
# if number>100 :
#     print("The number was greater than one hundred!")
#     print("Now its value has decreased by one hundred")
#     number = number -100
#     print("Its value now is :", number)
# print (number, "must be my lucky number!")
# print("Have a nice day!")