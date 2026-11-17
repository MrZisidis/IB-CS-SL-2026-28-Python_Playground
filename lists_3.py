# my_list = [1, 2, 3, 4, 5, 6]
#
# my_list.pop(2)
# print(my_list)
# my_list.pop(3)
# print(my_list)


my_list = [1, 2, 3, 4, 5, 6]

my_list.remove(2)
print(my_list)

try:
    my_list.remove(2)
except ValueError:
    print("not in list")

print(my_list)
my_list.remove(5)
print(my_list)