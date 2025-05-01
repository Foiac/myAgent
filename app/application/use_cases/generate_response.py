from app.domain.models.prompt import Prompt
from app.domain.services.generator_service import GeneratorService

class GenerateResponseUseCase:
    def __init__(self, generator_service: GeneratorService):
        self.generator_service = generator_service

    def execute(self, user_input: str, context: str = "") -> str:
        prompt = Prompt(user_input=user_input, context=context)
        return self.generator_service.generate(prompt)
