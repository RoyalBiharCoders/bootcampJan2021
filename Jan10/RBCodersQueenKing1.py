'''
A long time back in history... 
A cruel king has captured a queen. 
Queen wants to escape but she needs someone to help. 
Her friend senorita wants to help but king has laid 3 traps in her way if she choose wrong path. 
Also, if she selects right path, she gets gold coins. 
Help senorita getting maximum gold coins as well as saving the queen!

Below is the map for senorita to reach the queen as well as coins in the way:
Senorita - Forest(5), Road(3) - River(4), Cave(8) - Mountain(5), Valley(3) - Queen

Traps are laid in:
Forest, Cave, Valley
'''

#Solution
## Make a variable called myCoins. We will use it for collecting coins found in the way while saving the queen!
myCoins = 0
# Take input from senorita asking which path she choose
path_1 = input("Senorita! which path will you take? forest or valley?\n")
if(path_1 == "road"):
  # Stage 1 clear! Now add 3 coins to myCoins variable that she found on her way
  myCoins += 3
  print("Stage 1 clear!")
  # Take input from senorita asking which path she choose in 2nd stage
  path_2 = input("Which path this time? river or cave?\n")
  if(path_2 == "river"):
    # Stage 2 clear! Now add 4 coins to myCoins variable that she found on her way
    myCoins += 4
    print("Stage 2 clear!")
    # Take input from senorita asking which path she choose in 3rd stage
    path_3 = input("This is final round.. if you find right path, you will save queen! which path will you choose? mountain or valley?\n")
    if(path_3 == "mountain"):
      # Stage 3 clear! Now add 5 coins to myCoins variable that she found on her way
      myCoins += 5
      print("Congratulations! you saved the queen..\n")
      # Print total collected coins
      print("Your collected coins: "+ str(myCoins))
    else:
      print("Better luck next time")
  else:
    print("Sorry! you fell in trap..")
else:
  print("Sorry! you fell in trap..")
