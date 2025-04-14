import pandas as pd
import json

def csv_to_json(csv_filepath, json_filepath, input_col="input", output_col="output", chunk_size=4000):
    """Mengonversi file CSV ke file JSON dan membuat chunk jika output melebihi batas.

    Args:
        csv_filepath: Path ke file CSV input.
        json_filepath: Path ke file JSON output.
        input_col: Nama kolom input di file CSV. Defaultnya adalah "input".
        output_col: Nama kolom output di file CSV. Defaultnya adalah "output".
        chunk_size: Ukuran chunk yang diinginkan. Defaultnya adalah 4000.
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

    if input_col not in df.columns or output_col not in df.columns:
        print(f"Error: File CSV harus memiliki kolom '{input_col}' dan '{output_col}'. Kolom yang ada: {df.columns}")
        return

    data = []
    for _, row in df.iterrows():
        input_text = row[input_col]
        output_text = row[output_col]

        if isinstance(output_text, str) and len(output_text) > 5000:
            chunks = bagi_teks_menjadi_chunk(output_text, chunk_size)
            for i, chunk in enumerate(chunks):
                data.append({
                    "text_input": input_text,
                    "output": chunk,
                    # "chunk_number": i + 1,  # Tambahkan nomor chunk untuk informasi tambahan
                    # "total_chunks": len(chunks)
                })
        elif isinstance(output_text, str):
            data.append({"text_input": input_text, "output": output_text})
        else:
            print(f"Warning: Output for input '{input_text}' is not a string. Skipping.")

    try:
        with open(json_filepath, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)
        print(f"File CSV '{csv_filepath}' berhasil dikonversi menjadi file JSON '{json_filepath}'.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menulis file JSON: {e}")


def bagi_teks_menjadi_chunk(teks, ukuran_chunk):
    """Membagi teks menjadi beberapa chunk dengan ukuran tertentu."""
    chunks = []
    for i in range(0, len(teks), ukuran_chunk):
        chunks.append(teks[i:i + ukuran_chunk])
    return chunks


# Contoh penggunaan:
csv_file = "data.csv"
json_file = "data.json"

csv_to_json(csv_file, json_file, input_col="input", output_col="output")