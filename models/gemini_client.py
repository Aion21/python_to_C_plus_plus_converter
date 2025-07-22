import google.generativeai as genai
from typing import Generator
import os
from dotenv import load_dotenv

load_dotenv()


class GeminiClient:
    """Client for interacting with Google's Gemini API."""

    def __init__(self, model: str = "gemini-1.5-flash"):
        """Initialize the Gemini client.
        
        Args:
            model: The model to use for completions.
        """
        # Configure the API key
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        self.model = genai.GenerativeModel(model)
        self.model_name = model

    def stream_completion(self, messages: list[dict], system: str = "") -> Generator[str, None, None]:
        """Stream a completion from the model.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'.
            system: System message to guide the model's behavior.
            
        Yields:
            Chunks of the completion as they become available.
        """
        # Convert messages to Gemini format
        prompt = self._format_messages(messages, system)
        
        # Generate streaming response
        response = self.model.generate_content(
            prompt,
            stream=True,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=2000,
                temperature=0.7,
            )
        )
        
        reply = ""
        for chunk in response:
            if chunk.text:
                reply += chunk.text
                yield reply

    def get_completion(self, messages: list[dict], system: str = "") -> str:
        """Get a completion from the model (non-streaming).
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'.
            system: System message to guide the model's behavior.
            
        Returns:
            The full completion text.
        """
        # Convert messages to Gemini format
        prompt = self._format_messages(messages, system)
        
        # Generate response
        response = self.model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=2000,
                temperature=0.7,
            )
        )
        
        return response.text

    def _format_messages(self, messages: list[dict], system: str = "") -> str:
        """Format messages for Gemini API.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'.
            system: System message to guide the model's behavior.
            
        Returns:
            Formatted prompt string.
        """
        prompt_parts = []
        
        # Add system message if provided
        if system:
            prompt_parts.append(f"System: {system}\n")
        
        # Convert messages to a conversational format
        for message in messages:
            role = message.get('role', 'user')
            content = message.get('content', '')
            
            if role == 'user':
                prompt_parts.append(f"User: {content}")
            elif role == 'assistant':
                prompt_parts.append(f"Assistant: {content}")
            elif role == 'system':
                prompt_parts.append(f"System: {content}")
        
        return "\n\n".join(prompt_parts)
