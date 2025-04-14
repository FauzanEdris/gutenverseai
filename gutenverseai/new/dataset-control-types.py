import os
import json

# Path to extracted JSON block files
blocks_path = "/Users/fauzanjegstudio/Documents/Gutenverse List Block Options/minified"

# Initialize dataset list
chatml_dataset = []

# Define system message for ChatML format
system_message = {
    "role": "system",
    "content": "Anda adalah asisten AI yang hanya memberikan output dalam format JSON blok WordPress Gutenberg. Jangan berikan penjelasan tambahan apa pun."
}

# Helper: Ambil opsi pertama yang aman
def safe_parse_option(options):
    if not options:
        return "value"
    first = options[0]
    if isinstance(first, dict) and "value" in first:
        return first["value"]
    elif isinstance(first, str):
        return first
    return "value"

# Helper: Buat sample format ChatML
def build_chatml_sample(block_name, attribute_data):
    instruction = f"Buat sebuah blok '{block_name}' dengan beberapa konfigurasi default."
    user_message = {
        "role": "user",
        "content": instruction
    }
    assistant_message = {
        "role": "assistant",
        "content": json.dumps([{
            "attributes": attribute_data,
            "name": f"gutenverse/{block_name}"
        }])
    }
    return [system_message, user_message, assistant_message]

# Proses semua file block
for filename in os.listdir(blocks_path):
    if not filename.endswith(".json"):
        continue
    block_name = filename.replace(".json", "")
    file_path = os.path.join(blocks_path, filename)

    with open(file_path, "r") as f:
        try:
            block_config = json.load(f)
            block_attributes = {}

            for panel in block_config:
                for setting in panel.get("panelArray", []):
                    attr_id = setting.get("id")
                    if not attr_id:
                        continue

                    # Tangani berbagai kondisi atribut
                    if setting.get("type") == "boolean":
                        block_attributes[attr_id] = False
                    elif setting.get("options"):
                        block_attributes[attr_id] = safe_parse_option(setting["options"])
                    elif setting.get("allowDeviceControl"):
                        block_attributes[attr_id] = {
                            "Desktop": "value"
                        }
                    else:
                        block_attributes[attr_id] = "value"

            chatml_dataset.append({
                "messages": build_chatml_sample(block_name, block_attributes)
            })

        except Exception as e:
            print(f"[ERROR] {filename} - {e}")

# Simpan dataset ke file JSON
output_path = "./new/gutenverse-chatml-dataset.json"
with open(output_path, "w") as f:
    json.dump(chatml_dataset, f, indent=2)

print("✅ Dataset berhasil dibuat:", output_path)
