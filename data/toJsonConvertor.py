from unittest import skip

import StopPoints
import Lines
import csv


def printRows(rows):
    for row in rows:
        print(row)


with open("../data/csv/wienerlinien-ogd-linien.csv", "r") as linien:
    reader = csv.DictReader(linien)
    rows = list(reader)
lines = Lines.Lines(rows)

with open("../data/csv/wienerlinien-ogd-haltepunkte.csv", "r") as haltepunkte:
    rows.clear()
    for punkt in haltepunkte:
        punkt = punkt.removesuffix("\n").split(";")
        rows.append(punkt)
rows.pop(0)
stoppoints = StopPoints.StopPoints(rows)

print(lines.getByID(301))
print(stoppoints.getByID(13))
