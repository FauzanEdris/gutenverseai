import json
import os
from google.cloud import aiplatform
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer, BitsAndBytesConfig
from datasets import Dataset

# Konfigurasi (Ganti dengan informasi Anda)
PROJECT_ID = "gutenverse-ai-448107" # Ganti dengan project ID Anda
REGION = "asia-southeast1" # Ganti dengan region Anda
BUCKET_NAME = "gutenverse-ai" # Ganti dengan nama bucket Anda
DATA_PATH = "gutenverse-ai/templates" # Path ke data Anda di bucket
MODEL_NAME = "gpt2"
OUTPUT_DIR = f"gs://{BUCKET_NAME}/tuned_model"

# Inisialisasi Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# Load data dari GCS (fungsi yang diperbaiki)
def load_json_from_gcs(bucket_name, data_path):
    from google.cloud import storage
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=data_path)
    data = []
    for blob in blobs:
        if blob.name.endswith(".json"):
            json_data = json.loads(blob.download_as_text())
            data.extend(json_data)
    return data

json_data = load_json_from_gcs(BUCKET_NAME, DATA_PATH)
dataset = Dataset.from_list(json_data)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Konfigurasi BitsAndBytes
quantization_config = BitsAndBytesConfig(
    load_in_8bit=True, # Atau load_in_4bit=True jika ingin kuantisasi 4-bit (membutuhkan memori GPU lebih sedikit lagi)
    llm_int8_threshold=6.0, # Sesuaikan threshold ini jika diperlukan
    llm_int8_has_fp16_weight=False # Biasanya False
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=quantization_config,
    device_map="auto"
)

def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length")

tokenized_datasets = dataset.map(tokenize_function, batched=True)

training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    gradient_accumulation_steps=4,
    num_train_epochs=3, # Bisa dinaikkan jika data banyak
    learning_rate=2e-5,
    weight_decay=0.01,
    fp16=True,
    push_to_hub=False,
    logging_steps=1,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
)

trainer.train()
trainer.save_model(OUTPUT_DIR)
print(f"Model saved to: {OUTPUT_DIR}")