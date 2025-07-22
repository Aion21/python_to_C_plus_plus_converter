from typing import Generator
from pathlib import Path

from core import get_messages
from models import OpenAIClient, ClaudeClient, GeminiClient


class CodeConverter:
    """Handles the conversion of Python code to C++ using various AI models."""

    def __init__(self, model: str = "GPT"):
        """Initialize the code converter with the specified model.

        Args:
            model: The AI model to use for conversion ("GPT" or "Claude").
        """
        self.model_name = model
        self.model = self._initialize_model(model)

    def _initialize_model(self, model_name: str):
        """Initialize the appropriate AI model client.

        Args:
            model_name: Name of the model ("GPT", "Claude", or "Gemini").

        Returns:
            An instance of the appropriate model client.

        Raises:
            ValueError: If an unknown model is specified.
        """
        model_upper = model_name.upper()
        if model_upper == "GPT":
            return OpenAIClient()
        elif model_upper == "CLAUDE":
            return ClaudeClient()
        elif model_upper == "GEMINI":
            return GeminiClient()
        else:
            raise ValueError(f"Unknown model: {model_name}")

    def convert(self, python_code: str) -> Generator[str, None, None]:
        """Convert Python code to C++ using the selected model.

        Args:
            python_code: The Python code to convert.

        Yields:
            Chunks of the converted C++ code as they become available.
        """
        messages = get_messages(python_code)
        system_message = messages[0]["content"]
        user_message = messages[1]["content"]

        if isinstance(self.model, OpenAIClient):
            stream = self.model.stream_completion([
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ])
        elif isinstance(self.model, ClaudeClient):
            stream = self.model.stream_completion(
                [{"role": "user", "content": user_message}],
                system=system_message
            )
        else:  # Gemini
            stream = self.model.stream_completion(
                [{"role": "user", "content": user_message}],
                system=system_message
            )

        for chunk in stream:
            # Clean up the response by removing markdown code blocks
            clean_chunk = chunk.replace('```cpp\n', '').replace('```', '')
            yield clean_chunk

    def save_code(self, code: str, filename: str = "optimized.cpp") -> None:
        """Save the generated code to a file.
        
        Args:
            code: The code to save.
            filename: The name of the file to save to.
        """
        # Clean the code of markdown code blocks
        clean_code = code.replace("```cpp\n", "").replace("```", "")

        # Ensure the directory exists
        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        # Write the code to the file
        with open(filename, "w") as f:
            f.write(clean_code)
