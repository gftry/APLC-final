from Vehicle import Vehicle
from Parkinglot import ParkingLot

# Exceptions

class ParkingError(Exception):
    """Base exception for parking system."""
    pass

#The vehicle data is incorrect or incomplete
class InvalidVehicleError(ParkingError):
    """The vehicle data is incorrect or incomplete"""
    pass

#The parking spot data is invalid
class InvalidParkingSpotError(ParkingError):
    """The parking spot data is invalid"""
    pass

#No suitable parking spots are available
class ParkingLotFullError(ParkingError):
    """No suitable parking spots are available"""
    pass

#Someone tried to park a vehicle in a spot that’s already taken
class SpotAlreadyOccupiedError(ParkingError):
    """Someone tried to park a vehicle in a spot that’s already taken"""
    pass

#Someone tried to remove a vehicle from an empty spot
class SpotNotOccupiedError(ParkingError):
    """Someone tried to remove a vehicle from an empty spot"""
    pass


class DisableParkingLot(ParkingError):
    """This is only for disability"""
    pass