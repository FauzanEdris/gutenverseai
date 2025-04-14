import json

def deteksi_teks_panjang_json(input_file):
    """Mendeteksi teks yang melebihi 5000 karakter dalam file JSON dan melaporkan nomor barisnya.

    Args:
        input_file: Path ke file JSON input.

    Returns:
        List berisi nomor baris (berbasis 1) yang teksnya melebihi batas, atau None jika terjadi error.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File tidak ditemukan: {input_file}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Format JSON tidak valid di: {input_file}")
        return None
    except Exception as e:
        print(f"Error tak terduga: {e}")
        return None

    baris_melebihi_batas = []
    for i, item in enumerate(data):
        if "output" in item and isinstance(item["output"], str) and len(item["output"]) > 5000:
            baris_melebihi_batas.append(i + 1)  # Nomor baris dimulai dari 1
            print(f"Baris ke-{i+1}: Teks di kolom 'output' melebihi 5000 karakter ({len(item['output'])} karakter).")
        elif "output" not in item:
            print(f"Baris ke-{i+1}: Kolom 'output' tidak ditemukan.")
        elif not isinstance(item["output"], str):
            print(f"Baris ke-{i+1}: Kolom 'output' bukan bertipe string.")

    return baris_melebihi_batas

# Contoh penggunaan:
input_file = "data.json"  # Ganti dengan nama file JSON Anda
baris_bermasalah = deteksi_teks_panjang_json(input_file)

if baris_bermasalah is not None:
    if baris_bermasalah:
        print(f"Ditemukan teks yang melebihi batas pada baris: {baris_bermasalah}")
    else:
        print("Tidak ditemukan teks yang melebihi batas.")
else:
    print("Gagal memproses file.")