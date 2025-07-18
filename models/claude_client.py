import anthropic
from typing import Generator

class ClaudeClient:
    """Client for interacting with Anthropic's Claude API."""
    
    def __init__(self, model: str = "claude-3-haiku-20240307"):
        """Initialize the Claude client.
        
        Args:
            model: The model to use for completions.
        """
        self.client = anthropic.Anthropic()
        self.model = model
    
    def stream_completion(self, messages: list[dict], system: str = "") -> Generator[str, None, None]:
        """Stream a completion from the model.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'.
            system: System message to guide the model's behavior.
            
        Yields:
            Chunks of the completion as they become available.
        """
        result = self.client.messages.stream(
            model=self.model,
            max_tokens=2000,
            system=system,
            messages=messages,
        )
        
        reply = ""
        with result as stream:
            for text in stream.text_stream:
                reply += text
                yield reply
    
    def get_completion(self, messages: list[dict], system: str = "") -> str:
        """Get a completion from the model (non-streaming).
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'.
            system: System message to guide the model's behavior.
            
        Returns:
            The full completion text.
        """
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            system=system,
            messages=messages,
        )
        return response.content[0].text
