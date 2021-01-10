'''
Take 3 distinct numbers from user and print greatest number 

Logic: Choose randomly two numbers and compare them. 
Now pick the greater one and compare with third number. 
If it is still greater then it is greatest of all. 
For example, if you choose a and b and a>b is true then check again for a>c. 
If a>c is also true then a is greatest of all and if a>c is not true then c is greatest of all. 
Now if a>b is false then this means, b is greater. 
Hence, compare b with c now. If b>c returns true then b is greatest else c is greatest.
'''

# Take the input with input() and convert it to integer with int() . So it becomes, int(input())
a = int(input("Your first number: "))
b = int(input("Your second number: "))
c = int(input("Your third number: "))

if(a>b):
  if(a>c):
    print(str(a) + " is greatest!")
  else:
    print(str(c) + " is greatest!")
elif(b>a):
  if(b>c):
    print(str(b) + " is greatest!")
  else:
    print(str(c) + " is greatest!")


