import json

jsondata = """[
 {
  "name":"Pen",
  "unit_price":5
 },
 {
  "name":"Eraser",
  "unit_price":3
 },
 {
  "name":"Pencil",
  "unit_price":10
 },
 {
  "name":"White paper",
  "unit_price":15
 }
]"""

items = json.loads(jsondata)

# Input the item name that you want to search
item = input("Enter an item name:\n")

# Define a function to search the item
def search_price (name):
 for keyval in items:
  if name.lower() == keyval['name'].lower():
   return keyval['unit_price']

# Check the return value and print message
if (search_price(item) != None):
  print("The price is:", search_price(item))
else:
  print("Item is not found")