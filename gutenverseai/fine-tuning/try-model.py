import google.generativeai as genai

genai.configure(api_key="AIzaSyDYvwJcun3O4Pxb0cB1JKAwQ4FAYnLuid8")

# model = genai.GenerativeModel(model_name="tunedModels/increment-s2f0gjwx6g4u")
# model = genai.GenerativeModel(model_name="tunedModels/increment-v6icx9ipuvyp")
# model = genai.GenerativeModel(model_name="tunedModels/increment-x4bcohi4ovus")
model = genai.GenerativeModel( "tunedModels/increment-q7b8xtwaiep6", system_instruction='Generate a WordPress Gutenberg block template in JSON format.', )

result = model.generate_content("Generate a WordPress Gutenberg block template in JSON format. prompt: create a fancy button for up selling my product about cakes! the tase is so good, it will make you want more and more. the button should be colorful and attractive with cake color, with a text that says 'buy now'")
print(result.text)  # "IV"

