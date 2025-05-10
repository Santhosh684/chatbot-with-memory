 
# interface.py

import gradio as gr
from memory import ChatMemory
from prompts import build_prompt
from mistral_model import ask_mistral

# Create global memory instance
memory = ChatMemory()

def chat(user_input):
    if user_input.strip().lower() in ["clear", "reset"]:
        memory.clear()
        return "🔄 Memory cleared. Start fresh!"

    memory.add_message("user", user_input)
    prompt = build_prompt(memory.get_context(), user_input)

    try:
        response = ask_mistral(prompt)
    except Exception as e:
        return f"❌ Error: {e}"

    memory.add_message("assistant", response)
    return response

# Launch Gradio interface
gr.ChatInterface(chat).launch()
