import stops

class StopPoint:
    sPointID: int
    stop: stops.Stop
    sPointName: str
    longitude: float
    latitude: float

    def __init__(self, data: list,stops: stops.Stops):
        self.sPointID = int(data[0])
        self.stop = stops.getByID(int(data[1]))
        self.stop.addPoint(self)
        self.sPointName = data[2]
        self.longitude = float(data[5])
        self.latitude = float(data[6])

    def __str__(self):
        return str(self.sPointID) + ": " + self.sPointName


class StopPoints:
    sPoints: dict[int, StopPoint]

    def __init__(self, data: list, stops: stops.Stops):
        self.sPoints = {}
        for row in data:
            if  row[1] != '' and row[5] != "0000000000" and row[6] != "0000000000":
                sPoint = StopPoint(row, stops)
                self.sPoints[sPoint.sPointID] = sPoint
        print("Stop points done")

    def getByID(self, sPointID: int) -> StopPoint:
        return self.sPoints[sPointID]