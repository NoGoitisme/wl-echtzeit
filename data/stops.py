import stop_points

class Stop:
    diva: int
    platformName: str
    longitude: float
    latitude: float
    points: list[stop_points.StopPoint]

    def __init__(self, data: list):
        self.diva = int(data[0])
        self.platformName = data[1]
        self.longitude = float(data[4])
        self.latitude = float(data[5])
        self.points = []

    def addPoint(self, point: stop_points.StopPoint):
        self.points.append(point)

    def __str__(self):
        return str(self.diva) + ": " + self.platformName


class Stops:
    stops: dict[int, Stop]

    def __init__(self, data: list):
        self.stops = {}
        for row in data:
            stop = Stop(row)
            self.stops[stop.diva] = stop
        print("Stops done")

    def getByID(self, diva: int) -> Stop:
        return self.stops[diva]
