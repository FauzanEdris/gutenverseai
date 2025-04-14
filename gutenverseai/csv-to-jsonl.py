import pandas as pd
import json

def csv_to_jsonl(csv_filepath, jsonl_filepath):
    """Mengonversi file CSV ke file JSONL.

    Args:
        csv_filepath: Path ke file CSV input.
        jsonl_filepath: Path ke file JSONL output.
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
    
    with open(jsonl_filepath, "w", encoding="utf-8") as outfile:
        for _, row in df.iterrows():
            json_object = {"text_input": row["input"], "output": row["output"]}
            json.dump(json_object, outfile, ensure_ascii=False)  # ensure_ascii=False untuk karakter non-ASCII
            outfile.write('\n')

# Contoh penggunaan:
csv_file = "data.csv" #Ganti dengan nama file csv anda
jsonl_file = "data.jsonl" #Nama file yang akan dibuat
csv_to_jsonl(csv_file, jsonl_file)
print(f"File CSV '{csv_file}' berhasil dikonversi menjadi file JSONL '{jsonl_file}'.")