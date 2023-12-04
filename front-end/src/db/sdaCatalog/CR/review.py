import json

reviews = list()

try:
    with open('front-end\\src\\db\\sdaCatalog\\Other\\sdaCatalog.json', 'r') as ourFile:
        ourData = json.load(ourFile)
        

except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")
