import stop_points
import stops
import lines
import csv

def printRows(rows):
    for row in rows:
        print(row)

with open("../data/csv/wienerlinien-ogd-linien.csv", "r") as linien:
    reader = csv.DictReader(linien)
    rows = list(reader)
lines = lines.Lines(rows)

with open("../data/csv/wienerlinien-ogd-haltestellen.csv", "r") as stop:
    rows.clear()
    for punkt in stop:
        punkt = punkt.removesuffix("\n").split(";")
        rows.append(punkt)
rows.pop(0)
stops = stops.Stops(rows)

with open("../data/csv/wienerlinien-ogd-haltepunkte.csv", "r") as haltepunkte:
    rows.clear()
    for punkt in haltepunkte:
        punkt = punkt.removesuffix("\n").split(";")
        rows.append(punkt)
rows.pop(0)
stoppoints = stop_points.StopPoints(rows, stops)

print(lines.getByID(301))
print(stops.getByID(60200004))
print(stoppoints.getByID(13))
