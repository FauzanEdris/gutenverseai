import pandas as pd
import json

def csv_to_json(csv_filepath, json_filepath, instruction):
    """Mengonversi file CSV ke file JSON dengan menambahkan key 'instruction'.

    Args:
        csv_filepath: Path ke file CSV input.
        json_filepath: Path ke file JSON output.
        instruction: Instruksi yang akan ditambahkan ke setiap objek JSON.
    """
    try:
        df = pd.read_csv(csv_filepath)
    except FileNotFoundError:
        print(f"Error: File CSV tidak ditemukan di: {csv_filepath}")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: File CSV kosong: {csv_filepath}")
        return
    except pd.errors.ParserError:
        print(f"Error: Gagal memparsing file CSV: {csv_filepath}. Pastikan formatnya benar.")
        return

    if "input" not in df.columns or "output" not in df.columns:
        print(f"Error: File CSV harus memiliki kolom 'input' dan 'output'. Kolom yang ada: {df.columns}")
        return
    
    data = []
    for _, row in df.iterrows():
        # Tambahkan key 'instruction' ke setiap objek JSON
        json_object = {
            "instruction": instruction,  # Tambahkan instruksi
            "text_input": row["input"],  # Kolom 'input' dari CSV
            "output": row["output"]  # Kolom 'output' dari CSV
        }
        data.append(json_object)

    try:
        with open(json_filepath, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)  # indent untuk format yang mudah dibaca
        print(f"File CSV '{csv_filepath}' berhasil dikonversi menjadi file JSON '{json_filepath}'.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menulis file JSON: {e}")

# Contoh penggunaan:
csv_file = "data-2025-02-06.csv"  # Ganti dengan nama file CSV Anda
json_file = "data-2025-02-06-w-i.json"  # Nama file JSON yang akan dibuat

# Definisikan instruksi yang akan ditambahkan
instruction = "You are a specialized assistant trained to generate JSON definitions for WordPress block based on user-provided details. Your response must strictly follow the required JSON structure, adhering to the WordPress block editor standards without any tab just plain JSON."

# Panggil fungsi untuk mengonversi CSV ke JSON
csv_to_json(csv_file, json_file, instruction)