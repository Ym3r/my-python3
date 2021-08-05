 # 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Create a variable for bill
bill = 0

#Code logic shows that there are 3 items to calculate: pizza sizze, pepperoni and cheese. Three if/else sets must be made for each.

#First if set
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

#Second if set with 2 ifs based on pepperoni and pizza size.
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

#Third if set adding cheese.
if extra_cheese == "Y":
  bill += 1

#Finally, f-str showing final bill. 
print(f"Your final bill is ${bill}") 

