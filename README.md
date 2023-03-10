# KRR-FP-ErrandsInEvanston

## Running things
Make sure all necessary libraries are installed using ```pip install``` and then run the program (including front-end) using main.py

You can run the following commands using pipenv to manage the dependencies:

```
pipenv install haversine
pipenv install tk
pipenv install geopy
```

Finally run with 
```pipenv run python3 main.py```

## Using the Interface
1) write up to five places from the selection above(make sure to separate them with commas instead of spaces).

2) write a starting address in Evanston

3) press the "Plan my day!" button


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
