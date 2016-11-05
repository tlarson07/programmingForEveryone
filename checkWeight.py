weight = raw_input("How much do you weight?: ")
try:
    weight = int(weight) #if the input entered was an integer it will continue or...
except:
    print "Invalid entry."
    quit()
moonWeight = weight/6.0
print moonWeight
