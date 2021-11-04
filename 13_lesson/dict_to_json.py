# dictionary to json

import json
json_data = {"ser": 1,"er": "value1","ers": "fd","ear": "fxcd","ear": None, "ears": 0}

dictionary = json.dumps(json_data)
print(type(dictionary))
print(dictionary)

