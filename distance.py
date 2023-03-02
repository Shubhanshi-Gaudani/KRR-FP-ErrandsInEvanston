#Make sure to have pip installed: 
#pip install geopy 
#pip install geopandas 

#from geopy import Nominatim
from geopy.geocoders import Nominatim
from geopy.distance import geodesic as GD

locator = Nominatim(user_agent="myGeobroder")
location = locator.geocode("8246 Kimball Ave, Skokie, Illinois")
print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
place_one = (location.latitude, location.longitude)
location = locator.geocode("2209 Ridge Avenue, Evanston, Illinois")
place_two = (location.latitude, location.longitude)

print("The distance between Place 1 and Place 2 is: ", GD(place_one, place_two).km)