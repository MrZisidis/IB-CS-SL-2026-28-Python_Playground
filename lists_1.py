my_list = [7, 2, 2, 5, 2,4,5,2,-4]
days_of_the_week = ["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"]
vowels = ["a","e","i","o","u"]
counter = 0 #counting vowels
# my_list2 = [4,"hello",4,True]
# print(my_list)
# print(type(my_list))
# print(my_list2)
# print(type(my_list2[3]))
text= "helloooo"
# for letter in text:
#     print(letter)
#
for day in days_of_the_week:
    print(day)
    for letter in day:
        if letter in vowels:
            counter = counter + 1
    print(counter)

# for letter in text:
#     if letter in vowels:
#         counter = counter + 1
# print(counter)

# for item in my_list:
#     print(item)
#
# for index in range(len(my_list)):
#     print(my_list[index])