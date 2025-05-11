from llama_cpp import Llama
import os

# Path to your downloaded Mistral model
MODEL_PATH = os.path.join("models", "mistral-7b-instruct-v0.2.Q4_K_M.gguf")

# Load the model (this may take some seconds on first run)
llm = Llama(model_path=MODEL_PATH)

def ask_mistral(prompt: str) -> str:
    """Generate a response from the Mistral model."""
    response = llm(prompt,max_tokens=200)
    return response["choices"][0]["text"].strip()
