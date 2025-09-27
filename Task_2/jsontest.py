import os
import json

json_folder = "data"  

repo_root = os.getcwd()
full_json_folder = os.path.join(repo_root, json_folder)

json_files = [os.path.join(root, name)
              for root, dirs, files in os.walk(full_json_folder)
              for name in files
              if name.endswith(".json")]


# --- Load the first JSON file ---
with open(json_files[0], 'r', encoding='utf-8') as f:
    json_data = json.load(f)
