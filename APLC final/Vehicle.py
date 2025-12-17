from Exceptions import invalidvehicleerror
class Vehicle:
    def __init__(self,plate: str, size: str):
        self.plate = plate
        self.size = size

        if size != "compact" and size != "large":
            raise invalidvehicleerror("Invalid size")
