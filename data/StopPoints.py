class StopPoint:
    sPointID: int
    diva: int
    sPointName: str
    longitude: float
    latitude: float

    def __init__(self, data: list):
        self.sPointID = int(data[0])
        self.diva = data[1]
        self.sPointName = data[2]
        self.longitude = float(data[5])
        self.latitude = float(data[6])

    def __str__(self):
        return str(self.sPointID) + ": " + self.sPointName


class StopPoints:
    sPoints: dict[int, StopPoint]

    def __init__(self, data: list):
        self.sPoints = {}
        for row in data:
            sPoint = StopPoint(row)
            self.sPoints[sPoint.sPointID] = sPoint
        print("done")

    def getByID(self, sPointID: int) -> StopPoint:
        return self.sPoints[sPointID]

