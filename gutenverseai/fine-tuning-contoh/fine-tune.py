import google.generativeai as genai
import time

genai.configure(api_key="AIzaSyDYvwJcun3O4Pxb0cB1JKAwQ4FAYnLuid8")

base_model = "models/gemini-1.5-flash-001-tuning"

training_data = [
    {"text_input": "Halo, apa kabar?", "output": "Hello, how are you?"},
    {"text_input": "Selamat pagi.", "output": "Good morning."},
    {"text_input": "Selamat siang.", "output": "Good afternoon."},
    {"text_input": "Selamat malam.", "output": "Good night."},
    {"text_input": "Terima kasih.", "output": "Thank you."},
    {"text_input": "Terima kasih banyak.", "output": "Thank you very much."},
    {"text_input": "Sama-sama.", "output": "You're welcome."},
    {"text_input": "Permisi.", "output": "Excuse me."},
    {"text_input": "Maaf.", "output": "Sorry."},
    {"text_input": "Ya.", "output": "Yes."},
    {"text_input": "Tidak.", "output": "No."},
    {"text_input": "Sampai jumpa.", "output": "Goodbye."},
    {"text_input": "Sampai jumpa lagi.", "output": "See you later."},
    {"text_input": "Siapa nama Anda?", "output": "What is your name?"},
    {"text_input": "Nama saya ...", "output": "My name is ..."},
    {"text_input": "Saya dari Indonesia.", "output": "I am from Indonesia."},
    {"text_input": "Saya tinggal di ...", "output": "I live in ..."},
    {"text_input": "Saya suka ...", "output": "I like ..."},
    {"text_input": "Saya tidak suka ...", "output": "I don't like ..."},
    {"text_input": "Berapa harganya?", "output": "How much does it cost?"},
    {"text_input": "Saya lapar.", "output": "I am hungry."},
    {"text_input": "Saya haus.", "output": "I am thirsty."},
    {"text_input": "Saya lelah.", "output": "I am tired."},
    {"text_input": "Di mana toilet?", "output": "Where is the toilet?"},
    {"text_input": "Bisakah Anda membantu saya?", "output": "Can you help me?"},
    {"text_input": "Saya tidak mengerti.", "output": "I don't understand."},
    {"text_input": "Apa yang Anda lakukan?", "output": "What are you doing?"},
    {"text_input": "Saya sedang bekerja.", "output": "I am working."},
    {"text_input": "Hari ini hari Senin.", "output": "Today is Monday."},
    {"text_input": "Besok hari Selasa.", "output": "Tomorrow is Tuesday."},
    {"text_input": "Senang bertemu denganmu.", "output": "Nice to meet you."},
    {"text_input": "Selamat ulang tahun!", "output": "Happy birthday!"},
    {"text_input": "Semoga harimu menyenangkan!", "output": "Have a nice day!"},
    {"text_input": "Selamat berlibur!", "output": "Happy holidays!"},
    {"text_input": "Apa kabar hari ini?", "output": "How are you today?"},
    {"text_input": "Saya baik-baik saja, terima kasih.", "output": "I'm fine, thank you."},
    {"text_input": "Darimana asalmu?", "output": "Where are you from?"},
    {"text_input": "Saya suka bepergian.", "output": "I like to travel."},
    {"text_input": "Apa hobimu?", "output": "What are your hobbies?"},
    {"text_input": "Hobi saya adalah membaca dan menulis.", "output": "My hobbies are reading and writing."},
    {"text_input": "Selamat menikmati makananmu!", "output": "Enjoy your meal!"},
    {"text_input": "Bantuan!", "output": "Help!"},
    {"text_input": "Kebakaran!", "output": "Fire!"},
    {"text_input": "Polisi!", "output": "Police!"},
    {"text_input": "Dokter!", "output": "Doctor!"}
]
operation = genai.create_tuned_model(
    # You can use a tuned model here too. Set `source_model="tunedModels/..."`
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
# # You can plot the loss curve with:
# snapshots = pd.DataFrame(result.tuning_task.snapshots)
# sns.lineplot(data=snapshots, x='epoch', y='mean_loss')

model = genai.GenerativeModel(model_name=result.name)
result = model.generate_content("III")
print(result.text)  # IV