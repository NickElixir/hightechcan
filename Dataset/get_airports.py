import requests
config = open("config.txt", "r")
config_list = config.readlines()
country = config_list[0][:-1].lower() #drop off \n and capital letters

osm_base = "https://nominatim.openstreetmap.org/search"
params = {
    "format": "json",
    "polygon_geojson": 1, 
    "q": "Yakutsk Airport"
}
source_file = open("airports.dat", "r")
airports_file = open(country + "_airports.txt", "w")

for line in source_file:
    data = line.split(",")
    if country.title() in data[3]:
        name = data[1].replace('"', '')
        params['q'] = name
        req = requests.get(url = osm_base, params = params)
        data = req.json()
        
        for node in data:
            if "aerodrome" in node['type']:
                aerodrome = node
                break
        airport = name
        for coordinate in aerodrome['boundingbox']:
            airport += " "
            airport += coordinate

        airports_file.write(airport)
source_file.close()
airports_file.close()