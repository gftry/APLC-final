class parkingerror(Exception):
    """Base class for parking-related exceptions."""
    
class invalidvehicleerror(parkingerror):
    """Exception raised for invalid vehicle types."""
pass

class invalidspoterror(parkingerror):
    """Exception raised for invalid spot types."""
pass

class parkingfullerror(parkingerror):
    """Exception raised when the parking lot is full."""
pass


