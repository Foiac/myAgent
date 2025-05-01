from dataclasses import dataclass

@dataclass
class Prompt:
    user_input: str
    context: str = """
    You are a helpful agent who can talk to users about the weather.¨

    - ATENTION

    1 - You will to talk ONLY about weather
    """