print("Welcome to Uber!")
choice = input("What kind of ride do you want?\n1. Bike\n2.Car")
if choice == "Bike":
    BikeChoice = input("What kind of bike?\nScooty\n2. Sports")
    if BikeChoice == "Scooty":
        print("The fare is 250rs.")
    else:
        print("The fare is 500rs.")
else:
    CarChoice = input("What kind of car?\n1. Sedan\n2. SUV")
    if CarChoice == "Sedan":
        print("The fare is 250rs.")
    else:
        print("The fare is 500rs.")