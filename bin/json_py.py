import json

file = open("data.json")

data = json.load(file)

for x in data['book']:
	print(x)