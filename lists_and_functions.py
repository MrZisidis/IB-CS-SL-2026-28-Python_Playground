def median(my_list: list):
    ordered = sorted(my_list)
    list_centre = len(ordered) // 2
    return ordered[list_centre]
# print(median(mylist))
mylist = [1, 20, 13, -4, 5]
#1. ordering the list --> ordered  [-4,1,5,13,20]
#2. 5//2 --> 2
#3. ordered[2] --> 5

# Please write a function named length which takes a list as its argument and
# returns the length of the list.


def length(my_list: list):
    return len(my_list)
print("The length of my list is: ",length(mylist))

def mean(my_list: list):
    return sum(my_list) / len(my_list)

def range_of_list(my_list: list):
    return (max(my_list) - min (my_list))

my_list = [1, 2, 3, 4, 5]

print("The range of the list is: ", range_of_list(my_list))