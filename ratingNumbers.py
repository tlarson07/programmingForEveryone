#Learn how to make a boolean so it keeps asking you until you type in a number

def numberTest():
    number = raw_input("Please enter a number: ")
    try:
        number = int(number)
    except:
        print "Invalid entry."
        quit()
    if number >=8:
        print "Cool"
    elif number >=6:
        print "Good"
    elif number >=4:
        print "Meh"
    elif number >=2:
        print "Nevermind"
    elif number >= 0:
        print "Ouch!"
    else:
        print "Please enter a whole number, 0 or bigger!"

numberTest ()
