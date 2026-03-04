import os

from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llama_2 = "llama-3.3-70b-versatile"
openai_1 = "openai/gpt-oss-120b"
llama_1 = "meta-llama/llama-4-maverick-17b-128e-instruct"
