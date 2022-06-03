# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Shortcut: years_remaining = 90 - age_as_int, days_remaining = years_remaining * 365, weeks_remaining = years_remaining * 52, months_remaining = years_remaining * 12

#Change age from str > int by creating new variables
age_as_int = int(age)

#Create variables to calculate max ages for all categories
max_age_in_days = 365 * 90
max_age_in_weeks = 52 * 90
max_age_in_months = 12 * 90

#Create variables to calculate formula for max age - current age 

current_age_days = age_as_int * 365
current_age_weeks = age_as_int * 52
current_age_months = age_as_int * 12

#Create formula to calculate max age - current

age_left_days = int(max_age_in_days - current_age_days)
age_left_weeks = int(max_age_in_weeks - current_age_weeks)
age_left_months = int(max_age_in_months - current_age_months) 

#Print new str include f"" by making all data types similar

message = f"You have {age_left_days} days, {age_left_weeks} weeks, and {age_left_months} months left.")
print(message)

