# prevede json na dictionary

import json
json_data = '''{
"ser": 1,
"er": "value1",
"ers": "fd",
"ear": "fxcd",
"ear": null 
}'''

dictionary = json.loads(json_data)
print(type(dictionary))
print(dictionary)





