from pathlib import Path
import Lines
import csv
import json

with open("../data/csv/wienerlinien-ogd-linien.csv", "r") as linien:
    reader = csv.DictReader(linien)
    rows = list(reader)
lines = Lines.Lines(rows)

print(lines.getByID(301))
