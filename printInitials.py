#GOAL = Print the first, middle and last initial for the names in the list

listOfUsers = ["Tanner", "Jennings", "Larson", "Lauren", "Brooke", "Larson", "Jennifer", "Lynn", "Larson", "Bruce", "Arther", "Larson"]

currentPosition = 0
for words in listOfUsers:
    currentName = listOfUsers[currentPosition]
    currentChar = currentName[0]
    if currentPosition % 3 == 0:
        print currentChar
    currentPosition += 1
