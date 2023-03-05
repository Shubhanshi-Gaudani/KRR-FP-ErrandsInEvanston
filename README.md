# KRR-FP-ErrandsInEvanston

## Running things
Make sure all necessary libraries are installed using ```pip install``` and then run the program (including front-end) using main.py

## KB Creation
The KB is built by querying the Overpass API (an API for the Open Street Map KB). We collect all [amenities](https://wiki.openstreetmap.org/wiki/Key:amenity) into a JSON file. This gives us a host of information that we can process into a KB. 

The query that we ran on Overpass Turbo: 

```
area["name"="Evanston"]->.a;
(
   node["amenity"]["name"](area.a);
);
out center;
```
