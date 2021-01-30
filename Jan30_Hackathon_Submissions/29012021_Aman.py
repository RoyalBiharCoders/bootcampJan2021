#Prayer to Sun GOD....!
print('O Lord Surya, you Govern the Universe and Treasure PEACE. You remove all kinds of diseases. Bless me with long life, good health, wealth and prosperity.\n')
print('\n')
print('Ghat Allocation System\n')
ghatname= ['G1','G2','G3','G4']
G1 = [10]
G2 = [40]
G3 = [20]
G4 = [30]

print('Ghats availabe - G1 , G2 , G3 , G4')
a=input('Choose your desired Ghat and check if space is availabe :')
b=int(input('Enter number of family members going along with you :'))
if(a==ghatname[0]):
    if(b<=9):
        print('Area reserved for :'+ str(b)+'People')
        print('G1 Allocated...!')
        G1=[10-b]
        print('Space available in G1 :'+ str(G1))
    else:
        print("Space is full..!\n")
        print("\n")
        print("Choose another Ghat!\n")
        print('Ghats availabe - G2 , G3 , G4')
        a=input('Choose your desired Ghat and check if space is availabe :')
        b=int(input('Enter number of family members going along with you :'))
if(a==ghatname[1]):
    if(b<=39):
        print('Area reserved for :' + str(b)+'People')
        print('Ghat 2 Allocated...!')
        G2=[40-b]
        print('Space Aavailable in G2:'+ str(G2))
    else:
       print("Space is full..!\n")
       print("\n")
       print("Choose another Ghat!\n")
       print('Ghats availabe - G1 , G3 , G4')
       a=input('Choose your desired Ghat and check if space is availabe :')
       b=int(input('Enter number of family members going along with you :'))
if(a==ghatname[2]):
    if(b<=19):
        print('Area reserved for :' + str(b)+'People')
        print('Ghat 3 Allocated...!')
        G3=[20-b]
        print('Space Aavailable in G2:'+ str(G3))
    else:
       print("Space is full..!\n")
       print("\n")
       print("Choose another Ghat!\n")
       print('Ghats availabe - G1 , G2 , G4')
       a=input('Choose your desired Ghat and check if space is availabe :')
       b=int(input('Enter number of family members going along with you :'))
if(a==ghatname[3]):
    if(b<=29):
        print('Area reserved for:' + str(b)+'People')
        print('Ghat 4 Allocated...!')
        G4=[30-b]
        print('Space Aavailable in G4:'+ str(G4))
    else:
        print("Space is full..!\n")
        print("\n")
        print("Choose another Ghat!\n")
        print('Ghats availabe - G1 , G2 , G3')
        a=input('Choose your desired Ghat and check if space is availabe :')
        b=int(input('Enter number of family members going along with you :'))
   
