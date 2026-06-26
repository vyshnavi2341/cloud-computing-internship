bus_passes = {}

while True:
    print("\n1.Book Pass")
    print("2.View Pass")
    print("3.Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        name = input("Enter Name : ")
        route = input("Enter Route : ")
        fare = int(input("Enter Fare : "))

        bus_passes[name] = {
            "Route": route,
            "Fare": fare
        }

        print("Pass Booked Successfully")

    elif choice == 2:
        name = input("Enter Name : ")

        if name in bus_passes:
            print("\nPass Details")
            print("Name :", name)
            print("Route :", bus_passes[name]["Route"])
            print("Fare :", bus_passes[name]["Fare"])
        else:
            print("Pass Not Found")

    elif choice == 3:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
