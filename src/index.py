from wldataprocessor import getcsvdata

urls: list = [
    "https://www.wienerlinien.at/ogd_realtime/doku/ogd/wienerlinien-ogd-haltepunkte.csv",  # stopPoints
    "https://www.wienerlinien.at/ogd_realtime/doku/ogd/wienerlinien-ogd-haltestellen.csv",  # stopGroups
    "https://www.wienerlinien.at/ogd_realtime/doku/ogd/wienerlinien-ogd-linien.csv",  # lines
]

getcsvdata(urls)
