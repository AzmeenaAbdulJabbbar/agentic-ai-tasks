from litellm import completion
import os

os.environ["GEMINI_API_KEY"] = "AIzaSyAmGR6uStySNjzS12-_1aLev8iXVTYWuzg"

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{"content": "Hello, how are you?", "role": "user"}]
    )
    print(response.choices[0].message.content.strip())

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{"content": "Hello, how are you?", "role": "user"}]
    )
    print(response.choices[0].message.content.strip())

# Call the functions
gemini()
gemini2()
