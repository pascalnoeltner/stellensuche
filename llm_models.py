from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


def get_llm():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return ChatOpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo")
    

