import json 
import random

f = open('evanston_data.json')
data = json.load(f)
i = 0 

#Declare the Place data type and the database 
class Place:
  def __init__(self, name, amenity, latlong):
    self.name = name
    self.amenity = amenity
    self.latlong = latlong
  def __str__(self):
    return ' '.join([self.name, self.amenity, " ".join(str(x) for x in self.latlong)])

list_of_places = []
type_amenities = []
amenity_sorted = {}

#Decode the master JSON datatype and convert it into our own data-type 
for item in data["features"]:
    place_temp = Place(item["properties"]["name"], item["properties"]["amenity"], item["geometry"]["coordinates"]) 
    list_of_places.append(Place)

    if place_temp.amenity not in list(amenity_sorted.keys()):
        amenity_sorted[item["properties"]["amenity"]] = [Place(item["properties"]["name"], item["properties"]["amenity"], item["geometry"]["coordinates"])]
    else:
        #print(amenity_sorted[item["properties"]["amenity"]])
        amenity_sorted[item["properties"]["amenity"]].append(Place(item["properties"]["name"], item["properties"]["amenity"], item["geometry"]["coordinates"]) )
    
    #if item["properties"]["amenity"] not in type_amenities:
    #    type_amenities.append(item["properties"]["amenity"])
    #print(place_temp.amenity)
    #print(amenity_sorted)

#print(type_amenities)

#Function 1: return a random place from that collection for a particular amenity: 
def rand_amenity(amenity): 
    return random.choice(amenity_sorted[amenity])

print(rand_amenity('bank'))

#now, given first location + list of places to go to . . . 
#order = []
#order[0] = closest place to starting location (iterate over list, calculate max)