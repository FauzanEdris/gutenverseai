import google.generativeai as genai
import time
import json
from datasets import Dataset

genai.configure(api_key="AIzaSyDYvwJcun3O4Pxb0cB1JKAwQ4FAYnLuid8")  # Ganti dengan API key Anda

base_model = "models/gemini-1.5-pro-001"

def bagi_teks_menjadi_chunk(teks, ukuran_chunk):
    """Membagi teks menjadi beberapa chunk dengan ukuran tertentu."""
    chunks = []
    for i in range(0, len(teks), ukuran_chunk):
        chunks.append(teks[i:i + ukuran_chunk])
    return chunks

def prepare_training_data(data, ukuran_chunk=4000):  # Ukuran chunk bisa disesuaikan
    """Menyiapkan data training dengan memecah output yang panjang."""
    training_data = []
    for item in data:
        input_teks = item["text_input"]
        output_teks = item["output"]

        if isinstance(output_teks, str) and len(output_teks) > 5000: #cek apakah output bertipe string dan panjangnya > 5000
            chunks_output = bagi_teks_menjadi_chunk(output_teks, ukuran_chunk)
            for chunk in chunks_output:
                training_data.append({"text_input": input_teks, "output": chunk})
        elif isinstance(output_teks, str): #jika output string dan kurang dari 5000 maka langsung dimasukkan
            training_data.append({"text_input": input_teks, "output": output_teks})
        else:
            print(f"Warning: Output for input '{input_teks}' is not a string. Skipping.")

    return training_data


with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

training_data = prepare_training_data(data)

# Sekarang training_data berisi data yang sudah di-chunk jika perlu
print(f"Jumlah data training setelah chunking: {len(training_data)}")
print(training_data)
operation = genai.create_tuned_model(
    display_name="increment",
    source_model=base_model,
    epoch_count=20,
    batch_size=4,
    learning_rate=0.001,
    training_data=training_data,
)

for status in operation.wait_bar():
    time.sleep(10)

result = operation.result()
print(result)

model = genai.GenerativeModel(model_name=result.name)
result = model.generate_content("III")
print(result.text)