#1st version
# for i in range(10):    #start by default at zero (0). up to - excluding the input parameter.
#     print(i)

#2nd version  range(start, stop)   excluding stop
# for x in range(1, 11):
#     print("line", x)
#     if x == 5:
#         print("you have passed half way")

#3rd version   range(start, stop,step)
# for i in range(50,101,2):
#     print(i)

# for i in range(1, 4):
    # for j in range(1, 3):
    #     print(str(i) + "," + str(j))

# for step in range(10,4,-1):
#     print(step)

# for i in range (-3,0):  # --> range(0,-3)
#     print(i)

# while True:  #while user_input > 0:
#     number = int(input("Please type in a number: "))
#     if number == -1:
#         break
#     while number > 0:
#         print(number)
#         number -= 1
#

alphabet = ("abcdefghijklmnopqrstuvwxyz")
text = input("Please type in a text: ")
new_text = ""

for x  in text:
    print(x)
    print(alphabet.index(x))

    if alphabet.index(x) + 13> 26:
        new_index= 26 - alphabet.index(x) + 13
    else:
        new_index = alphabet.index(x) + 13
    print(alphabet[new_index])