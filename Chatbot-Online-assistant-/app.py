import chainlit as cl
import os
from dotenv import load_dotenv
import litellm
import logging
import json

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('client_hunting_chatbot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "openrouter/google/gemini-2.5-flash-preview-05-20"

if not API_KEY:
    raise ValueError("Please set the OPENROUTER_API_KEY environment variable in your .env file.")

# LiteLLM configuration
litellm.telemetry = False
litellm.register_model({
    MODEL: {
        "api_base": BASE_URL,
        "api_key": API_KEY,
        "provider": "openrouter"
    }
})

# Knowledge base (English)
client_hunting_kb = {
    "greet": "Hello! Thank you for reaching out. May I know your name?",
    "industry_query": "What industry or business do you work in?",
    "needs_query": "Could you please share some of your business challenges or needs?",
    "service_intro": "We offer digital marketing and IT consultancy services.",
    "meeting_offer": "Would you like to schedule a meeting? We are available tomorrow at 3 PM or Thursday at 11 AM.",
    "meeting_confirmed": "Thank you! Your meeting has been confirmed. A confirmation email will be sent to you.",
    "follow_up": "Do you need any further assistance? I'm here to help with any questions."
}

def client_hunting_tool(query: str) -> str:
    query = query.lower()
    if any(x in query for x in ["hello", "hi", "assalam", "salam"]):
        return client_hunting_kb["greet"]
    if any(x in query for x in ["industry", "business", "field"]):
        return client_hunting_kb["industry_query"]
    if any(x in query for x in ["need", "challenge", "problem", "requirement"]):
        return client_hunting_kb["needs_query"]
    if any(x in query for x in ["service", "offer", "help", "what do you do"]):
        return client_hunting_kb["service_intro"]
    if any(x in query for x in ["meeting", "schedule", "appoint", "call"]):
        return client_hunting_kb["meeting_offer"]
    if any(x in query for x in ["confirm", "booked", "ok", "done"]):
        return client_hunting_kb["meeting_confirmed"]
    if any(x in query for x in ["thank", "thanks", "bye", "no"]):
        return client_hunting_kb["follow_up"]
    return "I'm sorry, I didn't quite understand. Could you please rephrase your question?"

client_hunting_tool_schema = {
    "type": "function",
    "function": {
        "name": "client_hunting_tool",
        "description": "Handles client qualification and meeting scheduling.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "User's message for the chatbot."
                }
            },
            "required": ["query"]
        }
    }
}

class ClientHuntingChatbotAgent:
    def __init__(self, name, instructions, model, tools_list):
        self.name = name
        self.instructions = instructions
        self.model = model
        self.tools = {"client_hunting_tool": client_hunting_tool}
        self.tools_config = tools_list

    async def generate_response(self, messages: list):
        try:
            response = await litellm.acompletion(
                model=self.model,
                messages=messages,
                api_key=API_KEY,
                api_base=BASE_URL,
                tools=self.tools_config,
                tool_choice="auto",
                temperature=0.7,
                max_tokens=300
            )
            msg = response.choices[0].message
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                tool_call = msg.tool_calls[0]
                func_name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                if func_name in self.tools:
                    tool_output = self.tools[func_name](**args)
                    messages.append(msg)
                    messages.append({"role": "tool", "name": func_name, "content": tool_output})
                    follow_up = await litellm.acompletion(
                        model=self.model,
                        messages=messages,
                        api_key=API_KEY,
                        api_base=BASE_URL,
                        tools=self.tools_config,
                        tool_choice="auto",
                        temperature=0.7,
                        max_tokens=300
                    )
                    return follow_up.choices[0].message.content
            return msg.content
        except Exception as e:
            logger.error(f"Error: {e}", exc_info=True)
            return "Oops! Something went wrong. Please try again later."

client_hunting_agent = ClientHuntingChatbotAgent(
    name="ClientHuntingBot",
    instructions="You are a polite and helpful chatbot that assists in understanding clients' business needs.",
    model=MODEL,
    tools_list=[client_hunting_tool_schema]
)

@cl.on_chat_start
async def start():
    cl.user_session.set("messages", [
        {"role": "system", "content": client_hunting_agent.instructions},
        {"role": "assistant", "content": "Hello! I am your client hunting assistant. May I know your name?"}
    ])
    await cl.Message(content="Hello! I am your client hunting assistant. May I know your name?").send()

@cl.on_message
async def respond(message: cl.Message):
    messages = cl.user_session.get("messages")
    messages.append({"role": "user", "content": message.content})
    reply = await client_hunting_agent.generate_response(messages)
    messages.append({"role": "assistant", "content": reply})
    await cl.Message(content=reply).send()
