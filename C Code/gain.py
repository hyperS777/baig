from google import genai
from PIL import Image

client = genai.Client(api_key="AIzaSyBS-ebVNLxuWT89maskJq4sPKqzAASaTyk")

print("Welcome to Gemini Vision!")
print("Make sure your image is in the same folder as this script.\n")

image_name = input("Type the name of your image (e.g., photo.jpg): ")
user_question = input("What do you want to ask about this image?: ")

try:
    my_image = Image.open(image_name)
    
    print("\nThinking...")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[user_question, my_image]
    )
    
    print("\nGemini:", response.text)

except FileNotFoundError:
    print(f"\nError: Could not find '{image_name}'. Did you type the name correctly?")
except Exception as e:
    print(f"\nAn error occurred: {e}")