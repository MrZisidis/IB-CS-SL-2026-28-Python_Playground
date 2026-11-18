my_list = [5, 2, 3, 1, 4]

max_num = 0
min_num = 0
total = 0

for num in my_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
    total += num   #total = total + num

print(max_num)
print(min_num)
print(total)