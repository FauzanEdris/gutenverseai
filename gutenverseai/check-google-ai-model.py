import google.generativeai as genai

genai.configure(api_key="AIzaSyDYvwJcun3O4Pxb0cB1JKAwQ4FAYnLuid8")

for model_info in genai.list_tuned_models():
    print(model_info.name)