#Inventory list
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]


#My code
#How many items in inventory?
inventory_len = len(inventory)
print(inventory_len)

#First element saved to new variable
first = inventory[0]
print(first)

#Last element saved to new variable
last = inventory[-1]
print(last)

#Slicing items 2 - 5
inventory_2_6 = inventory[2:6]
print(inventory_2_6)

#How to select first 3 items
first_3 = inventory[:3]
print(first_3)

#Counting an item inside list
twin_beds = inventory.count("twin bed")

#Removing the 5th element from my list (0,1,2,3,4)
removed_item = inventory.pop(4)

#Inserting a new item into the list as the 11th element
inventory.insert(10, "19th Century Bed Frame")

#Sorting the list was the sort function
inventory.sort()
print(inventory)