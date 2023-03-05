import json 
import random
import haversine as hs

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

def get_list_of_places(am_list):
    places_to_go = []
    for am in am_list:
        places_to_go.append(rand_amenity(am))
    return places_to_go

def calculate_distance(latlong_one, latlongtwo):
    coord_1 = (latlong_one[0], latlong_one[1])
    coord_2 = (latlongtwo[0], latlongtwo[1])
    x = hs.haversine(coord_1, coord_2)
    return x


def optimizer(places_to_go, current_location):
    order = [Place("Current Location", "temp", [current_location[0], current_location[1]])]
    while len(places_to_go) != 0:
        min_dist = 9999999999
        for place in places_to_go:
            curr_dist = calculate_distance(order[-1].latlong, place.latlong)
            if curr_dist < min_dist: 
                min_dist = curr_dist
                min_place = place
        order.append(min_place)
       #places_to_go.pop(min_place)
        places_to_go = [item for item in places_to_go if item != min_place]

    return order

query = ["bank", "cafe", "theatre"]
current_location = [42.058097, -87.682163]
places_to_go = get_list_of_places(query)
print(places_to_go)
result = optimizer(places_to_go, current_location)
print(result[0], result[1], result[2], result[3])

#now, given first location + list of places to go to . . . 
#order = []
#order[0] = closest place to starting location (iterate over list, calculate max)