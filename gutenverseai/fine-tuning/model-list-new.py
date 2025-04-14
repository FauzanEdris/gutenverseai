from google import genai

client = genai.Client(api_key='AIzaSyDYvwJcun3O4Pxb0cB1JKAwQ4FAYnLuid8')

# Check which models are available for tuning.
for m in client.models.list():
  for action in m.supported_actions:
    if action == "createTunedModel":
      print(m.name) 
      break