from enum import Enum


class Line:
    lineID: int
    lineName: str
    sortHelp: int
    realTime: bool
    type: LineType

    def __init__(self, data: str):
        values = data.split(";")
        self.lineID = int(values[0])
        self.lineName = values[1]
        self.sortHelp = int(values[2])
        self.realTime = values[3] == "1"
        self.type = LineType[values[4]]

    def __str__(self):
        return str(self.lineID) + ": " + self.lineName


class Lines:
    lines: dict[int, Line]

    def __init__(self, data: list):
        self.lines = {}
        for row in data:
            line = Line(row[list(row.keys())[0]])
            self.lines[line.lineID] = line

    def getByID(self, lineID: int) -> Line:
        return self.lines[lineID]


class LineType(Enum):
    ptTramVRT = "Straßenbahn (VRT)"
    ptTramWLB = "Badner Bahn"
    ptMetro = "U-Bahn"
    ptTram = "Straßenbahn"
    ptTrainS = "S-Bahn"
    ptBusCity = "Bus"
    ptBusNight = "Nachtbus"
    ptRufBus = "Rufbus"
