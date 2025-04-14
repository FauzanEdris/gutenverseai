import json

# Load file asli
with open("./new/dataset.json", "r") as f:
    raw_data = json.load(f)

# Normalisasi field
formatted_data = []
for item in raw_data:
    block = item.get("blockName")
    attrs = item.get("attributes", [])

    # pastikan semuanya dalam bentuk dict valid
    if not isinstance(block, str) or not isinstance(attrs, list):
        continue

    formatted_data.append({
        "block": block,
        "attributes": attrs
    })

# Simpan ke file baru
with open("./new/gutenverse-block-options-dataset.json", "w") as f:
    json.dump(formatted_data, f, indent=2)

print("✅ JSON siap untuk diupload ke Hugging Face.")
