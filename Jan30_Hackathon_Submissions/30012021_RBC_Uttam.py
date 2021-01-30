allGhats = {"G1": 10, "G2": 40, "G3": 20, "G4": 30}
reservationDone = False

while (reservationDone == False):
	selectedGhat = input().upper()
	selectedMembers = int(input())
	if (selectedGhat in allGhats and selectedMembers>0):
		currentlyAvailable = allGhats[selectedGhat]
		if (selectedMembers >= currentlyAvailable):
			print("This ghat is full. Select from available options below-\n")
			alternateGhatsCount = 0
			for key,value in allGhats.items():
				if int(value)>selectedMembers:
					print(key)
					alternateGhatsCount = alternateGhatsCount + 1
			if (alternateGhatsCount == 0):
				print("Sorry! No Alternate ghat found.. try with a lower capacity")
		else:
			remainingValue = currentlyAvailable - selectedMembers
			allGhats[selectedGhat] = remainingValue
			print("Allocated")
			reservationDone = True
	else:
		print("Select valid ghat/members!")