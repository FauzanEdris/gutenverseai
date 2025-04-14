import google.generativeai as genai

genai.configure(api_key="AIzaSyDYvwJcun3O4Pxb0cB1JKAwQ4FAYnLuid8")

# genai.delete_tuned_model("tunedModels/increment-g45a0g6a2h5o")
# genai.delete_tuned_model("tunedModels/increment-s2f0gjwx6g4u")

for model_info in genai.list_tuned_models():
    print(model_info.name)
    