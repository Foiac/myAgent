import os
from dotenv import load_dotenv
from openai import OpenAI
from app.application.use_cases.generate_response import GenerateResponseUseCase
from app.adapters.output.openai_adapter import OpenAIAdapter

def get_generate_response_use_case() -> GenerateResponseUseCase:

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY não encontrada no .env")
    
    generator = OpenAIAdapter(api_key=api_key)
    return GenerateResponseUseCase(generator_service=generator)
