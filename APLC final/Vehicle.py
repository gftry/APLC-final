from Exceptions import InvalidVehicleError

class Vehicle:
    def __init__(self, plate: str, size: str):
        if size not in ("compact", "large"):
            raise InvalidVehicleError("Invalid vehicle size")

        self.plate = plate
        self.size = size
