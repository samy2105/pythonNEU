class vehicle(object):
    def __init__(self, brand, model, kilometers, service_date):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.service_date = service_date

    def brand_model(self):
        return self.brand + " " + self.model


def list_vehicles(vehicles):
    for index, car in enumerate(vehicles):
        print "ID " + str(index)
        print car.brand_model()
        print "kilometers: " + car.kilometers
        print "service date: " + car.service_date
        print ""


def edit_vehicle(vehicles):
    print "Select the vehicle you want to edit: "

    for index, car in enumerate(vehicles):
        print str(index) + ") "+ car.brand_model()

    print ""
    selected_id = raw_input("Enter the ID of the vehicle you want to edit: ")
    selected_vehicle = vehicles[int(selected_id)]

    edit_km = raw_input("Please enter the kilometers of %s: " % selected_vehicle.brand_model())
    selected_vehicle.kilometers = edit_km

    edit_service = raw_input("Please enter the new service date for %s: " % selected_vehicle.brand_model())
    selected_vehicle.service_date = edit_service

    print ""
    print "Kilometers and service date are refreshed."


def add_new(vehicles):
    brand = raw_input("Enter the name of the brand: ")
    model = raw_input("Enter the name of the model: ")
    kilometers = raw_input("Enter the kilometers driven: ")
    service_date = raw_input("Enter the general service date: ")

    new = vehicle(brand=brand, model=model, kilometers=kilometers, service_date=service_date)
    vehicles.append(new)

    print ""
    print "%s was added to your list" % new.brand_model()


def main():
    print "Welcome to the VMP!"

    mercedes = vehicle("mercedes", "XL", "20000", "1.1.2000")
    opel = vehicle("opel", "superclass", "12010", "1.1.2010")
    bmw = vehicle("bmw", "solala", "52020", "1.1.2020")
    vehicles = [mercedes, opel, bmw]

    while True:
        print ""
        print "Please choose one of these options:"
        print "a) See the list of your vehicles"
        print "b) Edit kilometers and the general service date"
        print "c) Add a new vehicle"
        print "d) Finish and save the list to a text file."
        print ""

        selection = raw_input("Enter your selection (a, b, c or d): ")
        print ""

        if selection.lower() == "a":
            list_vehicles(vehicles)
        elif selection.lower() == "b":
            edit_vehicle(vehicles)
        elif selection.lower() == "c":
            add_new(vehicles)
        elif selection.lower() == "d":
            print "\nYour current vehicle list will be saved in a text-file: "

            with open("VCM.txt", "w+") as car_list:
                car_list.write("list of your vehicles:\n")
                for index, car in enumerate(vehicles):
                    car_list.write("ID " + str(index))
                    car_list.write ("\n")
                    car_list.write(" " + car.brand_model())
                    car_list.write("\n")
                    car_list.write(" kilometers: " + car.kilometers)
                    car_list.write("\n")
                    car_list.write(" service date: " + car.service_date)
                    car_list.write("\n\n")


            print "good bye & see ya"
            break
        else:
            print "Please enter a, b, c or d."
            continue


if __name__ == "__main__":
        main()