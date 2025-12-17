class parkingeerror(Exception):
    """Base class for parking-related exceptions."""
    
class invalidvehicleerror(parkingeerror):
    """Exception raised for invalid vehicle types."""
pass

class invalidspoterror(parkingeerror):
    """Exception raised for invalid spot types."""
pass

class parkingfullerror(parkingeerror):
    """Exception raised when the parking lot is full."""
pass

