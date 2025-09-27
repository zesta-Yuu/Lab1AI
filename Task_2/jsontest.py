import json
#import io
import os

script_dir = os.path.dirname(__file__)  

json_filename = "game-of-thrones-characters-groups.json"

json_path = os.path.join(script_dir, json_filename)

#open and load file
with open(json_path, 'r', encoding='utf-8') as f:
    json_data = json.load(f)


#print('Number of JSON files ready to be loaded: ' + str(len(json_files)))
#print(json_data)
#print(json_data.keys()) #the top-level variable