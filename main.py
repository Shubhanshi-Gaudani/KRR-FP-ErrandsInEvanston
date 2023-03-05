#PROCESSING THE KB INTO OUR OWN DATATYPE
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

#DEFINING FUNCTIONS
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


#CREATING THE FRONTEND
import tkinter as tk
window = tk.Tk()
#making all the GUI components
title = tk.Label(text="🎼 Evanston Task Planner 🚗", width=20, height=3, font=("Arial", 20))
title.pack()
#description of functionality
desc = tk.Label(text="This program helps you minimize distance as you perform your tasks and go around Evanston.", width=100, height=2, font=("Arial", 10))
desc.pack()
#amenity classes
classes = tk.Label(text="Here are the kinds of places you can go to: ['school', 'place_of_worship', 'library', 'fuel', 'restaurant', 'pharmacy', 'fast_food', 'cinema', 'pub', 'cafe', 'car_rental', 'bank', 'dentist', 'spa', 'bar', 'post_office', 'parking', 'atm', 'brewery', 'animal_shelter', 'doctors', 'clinic', 'money_transfer', 'theatre', 'music_school', 'police', 'ice_cream', 'kindergarten', 'dance_theater', 'salon', 'social_facility', 'veterinary', 'parking_entrance', 'nursing_home', 'bicycle_rental', 'charging_station', 'arts_centre']", width=100, wraplength=700, height=5, font=("Arial", 10))
classes.pack()
#entering categories
category_entry_label = tk.Label(text="Please enter up to five types of places you would like to go to from the list above, separated by semicolons.", height = 2, font=("Helvetica", 10))
categories = tk.Entry(width=100)
category_entry_label.pack()
categories.pack()
#entering address
location_entry_label = tk.Label(text="What is your current location? A sample answer would be: '1228 Davis St.'", font=("Helvetica", 10), height=2)
location = tk.Entry(width=100)
location_entry_label.pack()
location.pack()
#submit button
submit_button = tk.Button(text="Plan my day!",width=25)
submit_button.pack()
#results
result_label = tk.Label(text="Results:", font=("Helvetica", 10), height=2)
result = tk.Text(width=100)
result_label.pack()
result.pack()


#HANDLING ACTUAL INPUT

#from geopy import Nominatim
from geopy.geocoders import Nominatim
from geopy.distance import geodesic as GD

locator = Nominatim(user_agent="myGeocoder")

def handle_click(event):
    result.delete("1.0", tk.END) #clearing the box
    try:
        #getting current location
        location_input = location.get()
        foo = locator.geocode(location_input + ' Evanston, IL 60201')
        current_location = [foo.latitude, foo.longitude]
        categories_input = categories.get()
        #getting inputted categories
        categories_input = categories_input.split(';')

        #doing the calculations
        places_to_go = get_list_of_places(categories_input)
        result_list = optimizer(places_to_go, current_location)
        output_string = 'The best order (that minimizes distance travelled) for you to accomplish these tasks in is: \n\n'
        for item in result_list[1:]:
            output_string += item.name
            output_string += '\n'

        result.insert('1.0',output_string)
    except:
        result.insert('1.0','There seems to be an error in your input. Please check that the formatting is appropriate.')

submit_button.bind("<Button-1>", handle_click)
window.mainloop()
