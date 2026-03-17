from abc import ABC, abstractmethod  # ABC = Abstract Base Class, Python's built-in way of defining interfaces
from dataclasses import dataclass


# @dataclass automatically generates __init__, __repr__, and __eq__ methods for us.
# Without it, we'd have to write:
#   def __init__(self, role: str, content: str):
#       self.role = role
#       self.content = content
# With it, Python generates that boilerplate for free. It's just a cleaner way
# to define a simple class that holds data and nothing else.
@dataclass
class Message:
    role: str     # "user" or "assistant"
    content: str  # the text of the message
    # This is the standard message format both Ollama and OpenAI understand,
    # so we use it everywhere and translate to each provider's format as needed.


# LLMService is the "contract" — any LLM provider (Ollama, OpenAI, etc.) must implement this.
# The @abstractmethod decorator means subclasses MUST implement chat(), or Python throws an error.
class LLMService(ABC):

    @abstractmethod
    async def chat(self, messages: list[Message], system_prompt: str) -> str:
        """Send a conversation to the LLM and return its text response."""
        # async def means this is asynchronous — FastAPI can handle other requests
        # while waiting for the LLM to respond, keeping the app responsive.
        #
        # system_prompt is where we pass the tutor's personality and instructions,
        # e.g. "You are a German tutor. Always respond in German..."
        ...
