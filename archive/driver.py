import requests

url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJN1t_tDeuEmsRUsoyG83frY4&fields=name%2Crating%2Cformatted_phone_number&key=AIzaSyB34fhiy56qjo0DUDOfz-KhwZoTAJiQoF4"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)