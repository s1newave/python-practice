import json


with open("data1.json") as file:
    data = json.load(file)

data.extend([
    {"userId": 3, "taskID": 3, "completed": False},
    {"userId": 4, "taskID": 1, "completed": True},
    {             "taskID": 4, "completed": False},
])

with open("data2.json", "w") as file:
    json.dump(data, file, indent=2)

with open("data2.json", "r") as file:
    data = json.load(file)

data = list(filter(lambda x: "userId" in x, data))

with open("data3.json", "w") as file:
    json.dump(data, file, indent=2)