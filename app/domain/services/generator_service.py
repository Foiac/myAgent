from app.domain.models.prompt import Prompt

class GeneratorService:
    def generate(self, prompt: Prompt) -> str:
        raise NotImplementedError("This method should be implemented by adapters.")