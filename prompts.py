 
# prompts.py

def build_prompt(context: str, user_input: str) -> str:
    """
    Combines chat history and the current user input into a single prompt.
    Mistral expects simple instruction-following format.
    """
    base_instruction = "You are a helpful assistant.\n"
    
    if context:
        return f"{base_instruction}{context}\nUser: {user_input}\nAssistant:"
    else:
        return f"{base_instruction}User: {user_input}\nAssistant:"
