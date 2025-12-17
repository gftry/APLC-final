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

from Exceptions import (
    ParkingError,
    InvalidVehicleError,
    InvalidParkingSpotError,
    ParkingLotFullError,
    SpotAlreadyOccupiedError,
    SpotNotOccupiedError,
    DisableParkingLot
)

try:
    # Example actions that may fail
    vehicle = Vehicle("ABC123", "medium")
    spot = ParkingLot.assign_spot(vehicle)

    # Force an error (assign again to same spot)
    spot.assign_vehicle(vehicle)

    # Force another error (release twice)
    spot.release_vehicle()
    spot.release_vehicle()

except InvalidVehicleError:
    print("Error: Vehicle data is invalid.")

except InvalidParkingSpotError:
    print("Error: Parking spot data is invalid.")

except ParkingLotFullError:
    print("Error: Parking lot is full. No spots available.")

except SpotAlreadyOccupiedError:
    print("Error: This parking spot is already occupied.")

except SpotNotOccupiedError:
    print("Error: Cannot release an empty parking spot.")
    
except DisableParkingLot:
    print("Error: Cannot park in this spot.")

except ParkingError:
    print("Error: A general parking system error occurred.")

except Exception as e:
    print("Unexpected error:", e)
