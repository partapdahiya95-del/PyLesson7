print("===Welcome to Ride Builder!2===")
print("1 - Bike, 2 - Car")
choice = input("Choose 1 or 2: ")
if (choice == "1"):
    print("1 for Scooty, 2 for Mountain Bike")
    bike_type = input("Choose 1 or 2: ")
    if (bike_type == "1"):
        print("You are going to ride Scooty with top speed of 80Km. In city.")
    elif (bike_type == "2"):
        print("You are going to ride Mountain Bike with top speed of 40Km. At Mountains.")
    else :
        print("Invalid choice.")
elif (choice == "2"):
    print("1 for sedan, 2 for SUV")
    car_type = input("Choose 1 or 2: ")
    if (car_type == "1"):
        print("You are going to ride a sedan with 5 passenger seat.")
    elif (car_type == "2"):
        print("you are going to ride a SUV with 7 passenger seat.")
    else :
        print("Invalid choice.")
else :
    print("Invalid choice.")
print("===Your custom ride is ready!===")