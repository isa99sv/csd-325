## Colton Stone, November 30, 2025, Module 8.2 Assignment

# This code will test two different API urls to output them as JSON text

import requests
import json

#----Astro API----
"""response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)

def astro(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))

astro(response.json())"""




#----Star Wars API----
response = requests.get("http://swapi.dev/api/planets/1/")
print(response.status_code)
print()
print(response.json())
print()

def star(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))

star(response.json())

