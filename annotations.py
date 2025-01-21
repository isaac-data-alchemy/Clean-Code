class Point:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long


def locate(latitude: float, longitude: float) -> Point:
    """Find an object in the map by its coordinateds"""
    pass

print(locate.__annotations__)