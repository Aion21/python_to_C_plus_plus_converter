import gradio as gr
from pathlib import Path
from typing import Optional

from core import CodeConverter, execute_python, execute_cpp

# Default Python example code
DEFAULT_PYTHON_CODE = """
import time

def calculate(iterations, param1, param2):
    result = 1.0
    for i in range(1, iterations+1):
        j = i * param1 - param2
        result -= (1/j)
        j = i * param1 + param2
        result += (1/j)
    return result

start_time = time.time()
result = calculate(100_000_000, 4, 1) * 4
end_time = time.time()

print(f"Result: {result:.12f}")
print(f"Execution Time: {(end_time - start_time):.6f} seconds")
"""


class CodeConverterApp:
    """Gradio-based UI for the Python to C++ code converter."""

    def __init__(self):
        """Initialize the application with default values."""
        self.converter = None
        self.current_cpp_code = ""

        # Set up the Gradio interface
        self._setup_interface()

    def _setup_interface(self):
        """Set up the Gradio interface components and layout."""
        self.css = """
        .python {background-color: #306998;}
        .cpp {background-color: #050;}
        """

        with gr.Blocks(css=self.css, title="Python to C++ Converter") as self.ui:
            gr.Markdown("# Python to C++ Code Converter")

            with gr.Row():
                self.model_selector = gr.Dropdown(
                    ["GPT", "Claude"],
                    label="AI Model",
                    value="GPT"
                )

            with gr.Row():
                self.python_input = gr.Code(
                    label="Python Code",
                    value=DEFAULT_PYTHON_CODE,
                    language="python",
                    lines=20
                )
                self.cpp_output = gr.Code(
                    label="C++ Code",
                    language="cpp",
                    lines=20,
                    interactive=True
                )

            with gr.Row():
                self.convert_btn = gr.Button("Convert to C++")

            with gr.Row():
                self.run_python_btn = gr.Button("Run Python")
                self.run_cpp_btn = gr.Button("Run C++")

            with gr.Row():
                self.python_result = gr.TextArea(
                    label="Python Execution Result",
                    elem_classes=["python"],
                    interactive=False
                )
                self.cpp_result = gr.TextArea(
                    label="C++ Execution Result",
                    elem_classes=["cpp"],
                    interactive=False
                )

            # Connect the UI components to their handlers
            self.convert_btn.click(
                self._on_convert_click,
                inputs=[self.python_input, self.model_selector],
                outputs=[self.cpp_output]
            )

            self.run_python_btn.click(
                self._on_run_python_click,
                inputs=[self.python_input],
                outputs=[self.python_result]
            )

            self.run_cpp_btn.click(
                self._on_run_cpp_click,
                inputs=[self.cpp_output],
                outputs=[self.cpp_result]
            )

    def _on_convert_click(self, python_code: str, model: str) -> str:
        """Handle the convert button click event."""
        try:
            self.converter = CodeConverter(model)
            output = ""
            for chunk in self.converter.convert(python_code):
                output = chunk
                yield output
            self.current_cpp_code = output
        except Exception as e:
            return f"Error during conversion: {str(e)}"

    def _on_run_python_click(self, python_code: str) -> str:
        """Handle the run Python button click event."""
        try:
            return execute_python(python_code)
        except Exception as e:
            return f"Error executing Python code: {str(e)}"

    def _on_run_cpp_click(self, cpp_code: str) -> str:
        """Handle the run C++ button click event."""
        try:
            output, error = execute_cpp(cpp_code)
            if error:
                return f"Error: {error}"
            return output
        except Exception as e:
            return f"Error executing C++ code: {str(e)}"

    def launch(self, **kwargs):
        """Launch the Gradio interface."""
        return self.ui.launch(**kwargs)
