import json
#import io
import os

# Folder where the script lives
script_dir = os.path.dirname(__file__)  # points to the folder containing this script

# Name of your JSON file
json_filename = "game-of-thrones-characters-groups.json"

# Full path to the JSON file
json_path = os.path.join(script_dir, json_filename)

# Safety check
if not os.path.exists(json_path):
    raise FileNotFoundError(f"JSON file not found: {json_path}")

# Open and load JSON
with open(json_path, 'r', encoding='utf-8') as f:
    json_data = json.load(f)

    
#print('Number of JSON files ready to be loaded: ' + str(len(json_files)))
#print(json_data)
#print(json_data.keys()) #the top-level variable