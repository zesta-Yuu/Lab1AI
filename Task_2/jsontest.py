import json
#import io
import os

path="data"

#file_name = "game-of-thrones-characters-groups.json"
json_files = [os.path.join(root, name) 
              for root, dirs, files in os.walk(path) 
              for name in files 
              if name.endswith((".json"))] #If we needed to read several files extensions: if name.endswith((".ext1", ".ext2"))

#print('Number of JSON files ready to be loaded: ' + str(len(json_files)))

#print(json_files)

#print('Path to the first file: '+json_files[0])

#Open the file using the name of the json file witn open() function
#Read the json file using load() and put the json data into a variable.
if len(json_files) ==1:
   with open(json_files[0]) as f:
      json_data = json.load(f)
else: print("failed")
   

#print(json_data)
#print(json_data.keys()) #the top-level variable