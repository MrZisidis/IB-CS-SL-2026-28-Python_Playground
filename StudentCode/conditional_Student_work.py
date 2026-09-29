# PC-T08-C01 — Menu Selection
#
# Task:
# Display a menu with 1. Play Game, 2. Instructions and 3. Quit. Keep asking until the user enters a valid option from 1 to 3, then output a suitable response.
print("1. Play game")
print("2. Instructions")
print("3. Quit")

choice = int(input("enter a number"))
while choice <=3 and choice >=1:
    if choice == 1:
        print("you will play the game")
        break
    elif choice == 2:
        print("here are the instructions")
        break
    else:
        break
if choice > 3 or choice < 1:
    print("enter a valid choice")
# Write your solution below.