import json
with open("data.json","r") as file:
    jsonData = json.load(file)
print("Datatype of variable: ", type(jsonData))
for i in jsonData:
    print(i, jsonData[i])