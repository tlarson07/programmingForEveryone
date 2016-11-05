def calculatingPay():
    rate = raw_input("What is your hourly wage: ")
    hours = raw_input("How many hours did you work: ")
    try:
        hours = int(hours)
        rate = int(rate)
    except:
        print "Invaild input, please only use numbers."
        quit()

    if hours < 0:
        print "No negatives :((("
        quit()
    elif hours < 40:
        pay = hours * rate
        print "Pay with standard rate = " + str(pay)
    else:
        overtimePay = (40 * rate) + ((hours - 40) * (rate*1.5))
        print "Pay with overtime bonus of 50% = " + str(overtimePay)
calculatingPay()
