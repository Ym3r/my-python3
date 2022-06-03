#Basta Fazoolin' Project

#Step 9: Create Business class
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

#Step 5: Create a Franchise class
class Franchise:
  #Give Franchise a constructor that takes address and menus
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  #Step 7: Give Franchise a str rep to tell us the address of the restaurant
  def __repr__(self):
    return self.address

  #Step 8: Give Franchise another method that takes time para
  def available_menus(self, time):
    available_menus = []
    #Iterate through time to rtn Menu objects available at that time
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

#Step1: Create a Menu class
class Menu:
  #Give Menu a constructor with 5 parameters
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  #Step 3
  #Give Menu class a str representation that will tell you the name of menu and when available.
  def __repr__(self):
    return self.name + " menu is available from " + str(self.start_time) + " - " + str(self.end_time)

  #Step 4: Give menu a method(function) with 2 parameters
  def calculate_bill(self, purchased_items):
    bill = 0
    #Return the total price of a purchase consisting of items in purchased_items
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

#Step 2: Create several menus by first creating a menu items dict
#Brunch items dict
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
#Brunch Menu object
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)

#print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))

#Early bird items dict
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

#Early Bird Menu object
early_bird_menu = Menu('Early Bird', early_bird_items, 1500, 1800)

#print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

#Dinner items dict
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

#Diiner Menu object
dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)

#Kids items dict
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

#Kids Menu object
kids_menu = Menu('Kids', kids_items, 1100, 2100)

#Combine all 4 menus for Step 6
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

#Step 6: Create two franchises and pass all 4 menus
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

#Step 10: Create the first Business along with the two franchises
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

#Arepa items dict
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

#Arepa menu 
arepas_menu = Menu("Take a' Arepa", arepas_items, 1000, 2000)

#Create new Arepa Franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

#Create new Arepa Business
arepa = Business("Take a' Arepa", [arepas_place])

#Test
print(arepa.franchises[0].menus[0])