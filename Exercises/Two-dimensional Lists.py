#Creating a two-dimensional list

#Names, nationality, age:
aws_restart_class = [["Kenny", "American", 37], ["Tanya", "German", 29], ["Ed", "Indian", 24], ["Mike", "British", 19]]
print(aws_restart_class)


#Modifying my list using positive indices due to a birthday.
aws_restart_class[2][2] = 30
print(aws_restart_class)


#Modifying the list using negative indices.
aws_restart_class[-4][-3] = "Ken"
print(aws_restart_class)