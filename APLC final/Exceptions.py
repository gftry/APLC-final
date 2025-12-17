# Exceptions

class ParkingError(Exception):
    """Base exception for parking system."""
    pass

#The vehicle data is incorrect or incomplete
class InvalidVehicleError(ParkingError):
    pass

#The parking spot data is invalid
class InvalidParkingSpotError(ParkingError):
    pass

#No suitable parking spots are available
class ParkingLotFullError(ParkingError):
    pass

#Someone tried to park a vehicle in a spot that’s already taken
class SpotAlreadyOccupiedError(ParkingError):
    pass

#Someone tried to remove a vehicle from an empty spot
class SpotNotOccupiedError(ParkingError):
    pass


class DisableParkingLot(ParkingError):
    pass
