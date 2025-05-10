 
# memory.py

class ChatMemory:
    def __init__(self):
        self.history = []

    def add_message(self, role: str, message: str):
        """Store a message with the sender's role ('user' or 'assistant')."""
        self.history.append({"role": role, "message": message})

    def get_context(self) -> str:
        """Return the chat history as a formatted string to use as prompt."""
        return "\n".join([f"{msg['role'].capitalize()}: {msg['message']}" for msg in self.history])

    def clear(self):
        """Reset the memory."""
        self.history = []
