# parking_spot.py

from threading import Lock
from Exceptions import InvalidParkingSpotError, SpotAlreadyOccupiedError


class ParkingSpot:
    def __init__(self, spot_id: str, size: str, available: bool = True):
        if size not in ["compact", "large"]:
            raise InvalidParkingSpotError(f"Invalid spot size: {size}")

        self.spot_id = spot_id
        self.size = size
        self.available = available
        self.lock = Lock()

    def can_fit(self, vehicle) -> bool:
        return self.available and (
            self.size == vehicle.size or self.size == "large"
        )

    def assign(self):
        with self.lock:
            if not self.available:
                raise SpotAlreadyOccupiedError("Spot already occupied")
            self.available = False

    def release(self):
        with self.lock:
            self.available = True
