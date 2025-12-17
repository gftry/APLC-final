from Parkinglot import ParkingLot
from Exceptions import ParkingError, InvalidVehicleError
from Vehicle import Vehicle
from Parkingspot import ParkingSpot
import json

def load_data(sampledata):
    with open(sampledata, "r") as file:
        return json.load(file)

def main():
    try:
        data = load_data("sampledata.json")
        spots = [
            ParkingSpot(
                spot["id"],
                spot["size"],
                spot["available"]
            )
            for spot in data["parkingSpots"]
        ]
        parkinglot = ParkingLot(spots, "sampledata.json")


        print("*******Parking system*******")
        while True:
            print("\nChoose an option:")
            print("1. Assign new car")
            print("2. Release a car")
            print("3. Exit")

            option = input("Enter your option: ").strip()

            if option == "1":
                plate = input("Enter license plate: ").strip().upper()
                size = input("Enter vehicle size (compact/large): ").strip().lower()

                vehicle = Vehicle(plate, size)
                parkinglot.assign_spot(vehicle)

            elif option == "2":
                spotid = input("Enter parking spot ID to release: ").strip()
                parkinglot.release_spot(spotid)

            elif option == "3":
                print("Exiting...")
                break

            else:
                print("Invalid option. Try again.")

    except ParkingError as e:
        print(f"Parking error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
