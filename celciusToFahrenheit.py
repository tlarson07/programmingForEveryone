tempFahrenheit = raw_input("What is the current temperature in Fahreheit: ")
tempCelsius = (int(tempFahrenheit) - 32.0) * 5 / 9 #answer shows decimals because of the .0 after 32
tempCelsiusRounded = round(tempCelsius, 2) #rounds 2 place values after decimal
print tempCelsiusRounded
