'''
Royal Bihar Coders
Simple List Operations
'''

mySimpleList = []

#Simple Append -> Inserts element at last of the list
mySimpleList.append('apple')
print(mySimpleList)

#Simple Insert -> Inserts element at specified index of the list
mySimpleList.insert(0,'hello')
print(mySimpleList)

#Simple Insert example of inserting at index "1"
mySimpleList.insert(1,'sample')
print(mySimpleList)

#print all elements of list
for i in mySimpleList:
  print(i)

#one more way of printing all elements of list
print(*mySimpleList)

#print last element of list
print(mySimpleList[-1])

#skip every 2nd element of list and print all others
print (mySimpleList[::2])

#print only first two elements of list
print (mySimpleList[0:2])
