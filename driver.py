import json 

f = open('evanston_data.json')
data = json.load(f)
i = 0 

class Place:
  def __init__(self, name, amenity, latlong):
    self.name = name
    self.amenity = amenity
    self.latlong = latlong
  def __str__(self):
    return ' '.join([self.name, self.amenity, " ".join(str(x) for x in self.latlong)])

list_of_places = []
type_amenities = []

for item in data["features"]:
    place_temp = Place(item["properties"]["name"], item["properties"]["amenity"], item["geometry"]["coordinates"]) 
    list_of_places.append(Place)
    if item["properties"]["amenity"] not in type_amenities:
        type_amenities.append(item["properties"]["amenity"])

print(type_amenities)