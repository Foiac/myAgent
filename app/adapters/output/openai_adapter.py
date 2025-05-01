import os
from dotenv import load_dotenv
from openai import OpenAI
from app.domain.models.prompt import Prompt
from app.domain.services.generator_service import GeneratorService
from app.config.agent_config import get_agent_information

load_dotenv()

class OpenAIAdapter(GeneratorService):
    def __init__(self, api_key: str):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY não encontrada no .env")
        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt: Prompt) -> str:
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.1,
            messages=[
                {"role": "system", "content": get_agent_information()},
                {"role": "user", "content": prompt.user_input}
            ]
        )
        print(
                {"role": "system", "content": get_agent_information()},
                {"role": "user", "content": prompt.user_input}
            )
        return response.choices[0].message.content
