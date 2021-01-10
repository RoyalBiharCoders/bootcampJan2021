'''
A Simple nested if
'''

# Can you eat chicken?

a = input("Are you veg or non veg?\n")
day = input("Which day is today?\n")

if(a == "nonveg"):
  if(day == "sunday"):
    print("You can eat chicken")
  else:
    print("It is not sunday! You cannot eat chicken..")
else:
  print("you are vegitarian! you cannot eat chicken!")
