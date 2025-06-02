import chainlit as cl
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("OPEN_ROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

model = "deepseek/deepseek-chat"  # ya koi bhi OpenRouter model

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello! How can I help you today?").send()

@cl.on_message
async def on_message(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})

    try:
        response = await client.chat.completions.create(
            model=model,
            messages=history,
            max_tokens=500,   # 👈 LIMIT tokens to stay under free quota
            temperature=0.7
        )

        reply = response.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        cl.user_session.set("history", history)

        await cl.Message(content=reply).send()

    except Exception as e:
        await cl.Message(content=f"❌ Error: {str(e)}").send()
