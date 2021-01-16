#Comparing 3 numbers - A Data Structure Approach

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

myList = [a,b,c]

currentMaximum = myList[0]

for i in myList:
  if i > currentMaximum:
    currentMaximum = i

print("your greatest number is: " + str(currentMaximum))
