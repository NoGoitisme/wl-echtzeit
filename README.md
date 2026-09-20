# wl-echtzeit
Playing around with "Wiener Linien" (Vieannese Public Transport) public data. \
With the hopes of making it a Home Assistant integration some day, to be able to see live info for public transport nearby or specific stops.

If anyone sees this and asks: Hey, why not use the official Wiener Linien App? Or use an "API" that someone else has already built themselves?\
My answer is: Why not do it myself? I definitely have nothing better to do. 

### Done so far
A small script which downloads the csv files provided by the Wiener Linien.
With a script that parses those files and initializes the objects, so that for each type a dictionary exists, for easy access to the objects. 

## Data Source and their license

This repo uses data provided by the Wiener Linien on
Austria's [Open Government Data](https://data.gv.at) platform.

- **Provider**: Stadt Wien
- **Data URL**: https://www.data.gv.at/datasets/cfba4373-a654-3e0b-80f8-348738169f95
- **License**: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

All data is used in accordance with the license terms.