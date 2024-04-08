# Convert JSON NULL values to None using Python

import json

my_json = r'{"name": "Bobby", "tasks": null, "age": null}'

my_dict = json.loads(my_json)

print(type(my_dict))  # 👉️ <class 'dict'>
print(my_dict)  # 👉️ {'name': 'Bobby', 'tasks': None, 'age': None}