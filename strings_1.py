# label = "review-ready-dsfd-sdfdf-"
# name = "firstname-secondname-fathersname"
#
# # print(len(label))
# # print(label.upper())
# # print(label[2])
# # print(label[:8])
# position=name.find("-")
# firstname=name[:position]
# print(firstname)
#
# tempname=name[position+1:]
# # print(tempname)
# secondposition=tempname.find("-")
# # print(secondposition)
#
# secondname=tempname[:secondposition]
# print(secondname)
# # print("firstname:",firstname)
# # print("secondname:",secondname)
#
# fathername=tempname[secondposition+1:]
# print(fathername)


course = "Computer Science Science"

subject = course[9:]                       # "Science"
rebuilt = course[:9] + "Systems"          # concatenate a new ending
replaced = course.replace("Science", "Systems")
position = course.find(" ")
print(position)

tempcourse= course[position+1:]
print(tempcourse)

position2=tempcourse.find(" ")
print(position2)

tempcourse2=tempcourse[position2+1:]
print(tempcourse2)
tempcourse2="Systems"
print(tempcourse2)

print(course[:position+position2+1]+tempcourse2)


# print(subject)
# print(rebuilt)
# print(replaced)