from google import genai

client = genai.Client(api_key='AIzaSyDYvwJcun3O4Pxb0cB1JKAwQ4FAYnLuid8')

response = client.models.generate_content(
    model='gemini-2.0-flash', 
    contents='Tell me a story in 300 words.'
)

print(response.text)