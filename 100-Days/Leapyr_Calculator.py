# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Figure out logic by using a site like draw.io


if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"{year} is a leap year")
    else:
      print(f"{year} is not a leap year.")
  else:
    print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")

