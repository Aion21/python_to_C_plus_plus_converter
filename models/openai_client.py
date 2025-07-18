from openai import OpenAI
from typing import Generator
from dotenv import load_dotenv


class OpenAIClient:
    """Client for interacting with OpenAI's API."""

    def __init__(self, model: str = "gpt-4o-mini"):
        """Initialize the OpenAI client.
        
        Args:
            model: The model to use for completions.
        """
        self.client = OpenAI()
        self.model = model

    def stream_completion(self, messages: list[dict]) -> Generator[str, None, None]:
        """Stream a completion from the model.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'.
            
        Yields:
            Chunks of the completion as they become available.
        """
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=True
        )

        reply = ""
        for chunk in stream:
            fragment = chunk.choices[0].delta.content or ""
            reply += fragment
            yield reply

    def get_completion(self, messages: list[dict]) -> str:
        """Get a completion from the model (non-streaming).
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'.
            
        Returns:
            The full completion text.
        """
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        return completion.choices[0].message.content
