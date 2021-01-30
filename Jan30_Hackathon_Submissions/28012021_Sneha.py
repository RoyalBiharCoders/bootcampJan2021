#there are four ghats in chhat puja G1, G2, G3, G4,
#we have to chose from them according to seats.
#number of members
print(
    "choose your ghat names namely- G1 G2 G3 G4 along with number of seats you want ")
p2 = 0
ghat1 = "G1"
ghat2 = "G2"
ghat3 = "G3"
ghat4 = "G4"
p1 = input("Your seat name : ")
p2 = int(input(" number of members :"))

if (p1 == ghat1):
    if (p2 <= 10):
        print("seat alloted")
        p2=10-p2
    else:
        print("seat not available\nchoose from G2, G3, G4")

if (p1 == ghat2):
    if (p2 <= 40):
        print("seat alloted")
        p2 = 40 - p2
    else:
        print("choose from G3 and G4")

if (p1 == ghat3):
    if (p2 <= 20):
        print("seat alloted")
        p2=20-p2
    else:
        print("  seats available in G4")

if (p1 == ghat4):
    if (p2 <= 30):
        print("seat alloted")
        p2=30-p2   
    else:
        print("not available")


