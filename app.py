# app.py

from memory import ChatMemory
from prompts import build_prompt
from mistral_model import ask_mistral

def main():
    memory = ChatMemory()

    print("🤖 Chatbot with Memory (Type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit']:
            print("Exiting... Goodbye! 👋")
            break

        # Add user message to memory
        memory.add_message("user", user_input)

        # Build full prompt using memory + new input
        prompt = build_prompt(memory.get_context(), user_input)

        # Get response from the Mistral model
        try:
            response = ask_mistral(prompt)
        except Exception as e:
            print("❌ Error from model:", e)
            continue

        # Add assistant response to memory and print it
        memory.add_message("assistant", response)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    main()
