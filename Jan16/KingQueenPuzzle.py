'''
A long time back in history... A cruel king has captured a queen. Queen wants to escape but she needs someone to help. Her friend senorita wants to help but king has laid 3 traps in her way if she choose wrong path. Also, if she selects right path, she gets gold coins. Help senorita getting maximum gold coins as well as saving the queen!

Below is the map for senorita to reach the queen as well as coins in the way:
Senorita - Forest(5), Road(3) - River(4), Cave(8) - Mountain(5), Valley(3) - Queen

Traps are laid in:
Forest, Cave, Valley
'''

# A Data structure approach to solve
myTruePath = ['road','river','mountain']
myCoins = 0

p1 = input("Your First path: ")
p2 = input("Your Second path: ")
p3 = input("Your third path: ")

if (p1 == myTruePath[0]):
  myCoins = myCoins + 3
  if(p2 == myTruePath[1]):
    myCoins = myCoins + 4
    if (p3 == myTruePath[2]):
      myCoins = myCoins + 5
      print("Congratulations Senorita! You saved the queen..")
      print("Your collected coins: " + str(myCoins))
    else:
      print("You failed..")
  else:
    print("You failed..")
else:
  print("You failed..")
