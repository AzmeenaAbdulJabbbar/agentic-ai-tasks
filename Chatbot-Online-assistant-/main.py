import os
from dotenv import load_dotenv
import litellm
import chainlit as cl
from litellm import completion

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "openrouter/google/gemini-2.5-flash-preview-05-20"

if not API_KEY:
    raise ValueError("Please set the OPENROUTER_API_KEY in your .env file.")

# ✅ Correctly register the model (no keyword args like model_name or custom_llm_provider)
litellm.register_model({
    MODEL: {
        "api_key": API_KEY,
        "api_base": BASE_URL,
        "provider": "openrouter"
    }
})

@cl.on_message
async def handle_message(message: cl.Message):
    response = completion(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.content}
        ]
    )

    await cl.Message(content=response["choices"][0]["message"]["content"]).send()
