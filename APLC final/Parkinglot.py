from Exceptions import SpotAlreadyOccupiedError, InvalidParkingSpotError
from concurrent.futures import ThreadPoolExecutor
import json

class ParkingLot:
    def __init__(self, spots: list, json_file: str):
        self.spots = spots
        self.parked_vehicles = {}  # Map plate -> spot
        self.json_file = json_file
        self.load_vehicles_from_json()

    def _check_spot(self, spot_vehicle_pair):
        spot, vehicle = spot_vehicle_pair
        if spot.available and (spot.size == vehicle.size or spot.size == "large"):
            return spot
        return None

    def assign_spot(self, vehicle):
        with ThreadPoolExecutor() as executor:
            results = executor.map(
                self._check_spot,
                [(spot, vehicle) for spot in self.spots]
            )

        for spot in results:
            if spot:
                spot.assign()
                self.parked_vehicles[vehicle.plate] = spot
                print(f"Vehicle {vehicle.plate} assigned to spot {spot.spot_id}")
                self.save_to_json(vehicle, spot, assign=True)
                return spot

        raise SpotAlreadyOccupiedError("No suitable spots available.")

    def release_spot(self, spot_id: str):
        for spot in self.spots:
            if spot.spot_id == spot_id:
                plate_to_remove = None
                for plate, v_spot in list(self.parked_vehicles.items()):
                    if v_spot.spot_id == spot_id:
                        plate_to_remove = plate
                        del self.parked_vehicles[plate]
                        break

                spot.release()  # Make sure Spot class has this method
                print(f"Spot {spot_id} released")

                if plate_to_remove:
                    self.save_to_json(plate_to_remove, spot, assign=False)
                return

        raise InvalidParkingSpotError(f"Spot {spot_id} not found.")

    def load_vehicles_from_json(self):
        """Load initial vehicles from JSON for parked vehicles dict"""
        with open(self.json_file, "r") as file:
            data = json.load(file)

        for vehicle_data in data.get("vehicles", []):
            plate = vehicle_data["plate"]
            size = vehicle_data["size"]
            # Find assigned spot
            for spot in self.spots:
                if not spot.available and (spot.size == size or spot.size == "large"):
                    self.parked_vehicles[plate] = spot
                    break

    def save_to_json(self, vehicle_or_plate, spot, assign=True):
        """Update JSON file when a vehicle is assigned or released"""
        with open(self.json_file, "r") as file:
            data = json.load(file)

        # Update spot availability
        for s in data["parkingSpots"]:
            if s["id"] == spot.spot_id:
                s["available"] = assign

        # Update vehicles list
        if assign:
            vehicle_dict = {"plate": vehicle_or_plate.plate, "size": vehicle_or_plate.size}
            if vehicle_dict not in data.get("vehicles", []):
                data.setdefault("vehicles", []).append(vehicle_dict)
        else:
            data["vehicles"] = [v for v in data.get("vehicles", []) if v["plate"] != vehicle_or_plate]

        # Save back to JSON
        with open(self.json_file, "w") as file:
            json.dump(data, file, indent=2)

