import google.generativeai as genai

from PIL import Image

genai.configure(api_key="YOUR_KEY_HERE")
model = genai.GenerativeModel('gemini-pro-vision')

image = Image.new('RGB', (100, 100), (255, 255, 255))

response = model.generate_content(["Is the following image white?", image], stream=True)
response.resolve()

print(response.text)
