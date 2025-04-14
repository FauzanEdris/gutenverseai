import google.generativeai as genai

genai.configure(api_key="AIzaSyDYvwJcun3O4Pxb0cB1JKAwQ4FAYnLuid8")

model = genai.GenerativeModel(model_name="tunedModels/increment-2vq8egemdxm")
result = model.generate_content("Saya adalah pendekar dari gunung gede!")
print(result.text)  # "IV"

