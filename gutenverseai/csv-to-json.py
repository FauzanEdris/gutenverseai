import pandas as pd
import json

def csv_to_json(csv_filepath, json_filepath):
    """Mengonversi file CSV ke file JSON.

    Args:
        csv_filepath: Path ke file CSV input.
        json_filepath: Path ke file JSON output.
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
        json_object = {"text_input": row["input"], "output": row["output"]}
        data.append(json_object)

    try:
        with open(json_filepath, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False) # indent untuk format yang mudah dibaca
        print(f"File CSV '{csv_filepath}' berhasil dikonversi menjadi file JSON '{json_filepath}'.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menulis file JSON: {e}")

# Contoh penggunaan:
# csv_file = "data.csv" #Ganti dengan nama file csv anda
# json_file = "data.json" #Nama file yang akan dibuat

csv_file = "data-2025-02-06.csv" #Ganti dengan nama file csv anda
json_file = "data-2025-02-06.json" #Nama file yang akan dibuat
csv_to_json(csv_file, json_file)