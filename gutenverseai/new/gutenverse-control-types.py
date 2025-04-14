from huggingface_hub import notebook_login
notebook_login()


from datasets import load_dataset, Dataset
import json

# Load JSON file yang tadi
with open("gutenverse-control-types.json", "r") as f:
    data = json.load(f)

# Convert ke Hugging Face Dataset
ds = Dataset.from_list(data)

# Ganti dengan username kamu
your_username = "fauzanedris"
repo_name = "gutenverse-control-types"

# Push to Hub
ds.push_to_hub(f"{your_username}/{repo_name}")
