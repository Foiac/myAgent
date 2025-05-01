from dataclasses import dataclass

@dataclass
class Prompt:
    user_input: str
    context: str = ""