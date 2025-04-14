from huggingface_hub import login
from datasets import load_dataset

# Login ke Hugging Face
login(token="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")

# # Muat dataset dari file JSON
# dataset = load_dataset('json', data_files='data-2025-02-06-w-i.json')

# # Upload dataset ke Hugging Face Dataset Hub
# dataset.push_to_hub("fauzanedris/gutenverse-ai")