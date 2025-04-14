import os
import json

# Path to extracted JSON block files
blocks_path = "/Users/fauzanjegstudio/Documents/Gutenverse List Block Options/minified"

dataset = []

# Loop through all files in the directory
for filename in os.listdir(blocks_path):
	# Check if the file is a JSON file
	if filename.endswith(".json"):
		file_path = os.path.join(blocks_path, filename)
		
		# Read the JSON file
		with open(file_path, 'r') as file:
			data = json.load(file)
	
			entry = {
				"blockName": filename.replace(".json", ""),
				"attributes": json.dumps(data)
			}
   
			# Append the data to the dataset list
			dataset.append(entry)

# Simpan dataset ke file JSON
output_path = "./new/dataset.json"

with open(output_path, "w") as f:
  json.dump(dataset, f, indent=2)

print(f"Dataset saved to {output_path}")

from datasets import Dataset

# prep_data = []

# for data in dataset:
# 	print(data)

dataset = Dataset.from_list(dataset)

# Tentukan nama repo di HF Hub
user = "fauzanedris"  # ganti dengan username Anda
repo_dataset = f"{user}/gutenverse-block-options"

# Push to Hugging Face Hub
dataset.push_to_hub(repo_dataset)
print(f"Dataset pushed to Hugging Face Hub: {repo_dataset}")