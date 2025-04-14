import os
from openai import OpenAI

# Set API key OpenAI
client = OpenAI(
    api_key="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",  # This is the default and can be omitted
)

# Fungsi untuk membuat JSON WordPress block
def generate_block(prompt):
    # Instruction to the model (System message for clarity)
    system_instruction = (
        "You are an assistant that generates JSON output for WordPress blocks. "
        "When given a prompt, respond with JSON that matches the structure of WordPress blocks."
    )
    
    # Requesting completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Atau gunakan "gpt-4" jika tersedia
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Create a {prompt}"}
        ],
        temperature=0.7,
        max_tokens=200
    )
    
    # Return the generated JSON
    return response['choices'][0]['message']['content']

# Contoh penggunaan
prompt = "heading block with text 'Welcome to OpenAI'"
result = generate_block(prompt)
print(result)
