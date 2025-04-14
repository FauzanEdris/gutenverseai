import os
import json

file_path = "/Users/fauzanjegstudio/Documents/gutenverseai/a/button.json"

dataset = []

# Read the JSON file
with open(file_path, "r") as file:
    data = json.load(file)

for item in data:
    section = item.get("title")

    for option in item.get("panelArray"):
        options = {"section": section}

        for attr_key, attr_val in option.items():
            # print(attr_key, attr_val)
            if(isinstance(attr_val, list) or isinstance(attr_val, dict)):
                options[attr_key] = json.dumps(attr_val)
            else:
                options[attr_key] = attr_val
        
        dataset.append(options)

# print(dataset)


output_path = "/Users/fauzanjegstudio/Documents/gutenverseai/a/dataset.json"

with open(output_path, "w") as f:
  json.dump(dataset, f, indent=2)
  
  

from datasets import Dataset


dataset = Dataset.from_list(dataset)

# Tentukan nama repo di HF Hub
user = "fauzanedris"  # ganti dengan username Anda
repo_dataset = f"{user}/gutenverse-block-button-options"

# Push to Hugging Face Hub
dataset.push_to_hub(repo_dataset)
print(f"Dataset pushed to Hugging Face Hub: {repo_dataset}")
