from huggingface_hub import whoami, login

# Replace with your token
login(token="hhf_...WPUY", write_token=False)

print(whoami())
