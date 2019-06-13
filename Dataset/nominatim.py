# checking is boundingbox coordinates really coordinates of boundy box

osm_base = "https://nominatim.openstreetmap.org/search"
params = {
    "format": "json",
    "polygon_geojson": 1, 
    "q": "Yakutsk Airport"
}
req = requests.get(url = osm_base, params = params)
data = req.json()

for node in data:
    print(node['type'])
    if "aerodrome" in node['type']:
        aerodrome = node
        break
print(aerodrome['boundingbox'])
coordinates = aerodrome['geojson']['coordinates'][0]
xmin = coordinates[0][0]
ymin = coordinates[0][1]
xmax = coordinates[0][0]
ymax = coordinates[0][1]

for point in coordinates:
    if point[0] < xmin:
        xmin = point[0]
    elif point[0] > xmax:
        xmax = point[0]
        
    if point[1] < ymin:
        ymin = point[1]
    elif point[1] > ymax:
        ymax = point[1]
print(ymin, ymax, xmin, xmax)

#as we can see it's truth