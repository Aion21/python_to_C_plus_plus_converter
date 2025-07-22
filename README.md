# Python to C++ Code Converter

A tool that converts Python code to optimized C++ for improved performance, featuring a user-friendly web interface for testing and comparing execution results.

> **Important Security Notice**

This application executes Python and C++ code on your local machine using `exec()`. For security reasons:

1. **Only run this application locally** - Never expose it to the internet or untrusted networks
2. **Execute with caution** - The application runs code with the same permissions as the user
3. **Review all code** - Always inspect AI-generated code before execution
4. **Use in a controlled environment** - Consider using a virtual machine or container for additional isolation
5. **Monitor resource usage** - Some operations might be resource-intensive

By using this application, you acknowledge that you understand these risks and accept full responsibility for any consequences of running the generated code.

## Features

- **AI-Powered Conversion**: Utilizes advanced AI models (GPT, Claude, and Gemini) to convert Python code to optimized C++
- **Performance Comparison**: Run and compare execution times between Python and C++ implementations
- **User-Friendly Interface**: Built with Gradio for an intuitive web-based experience
- **Multiple AI Models**: Choose between different AI models for conversion (GPT, Claude, Gemini)
- **Real-time Execution**: Execute both Python and C++ code directly from the interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Aion21/python_to_C_plus_plus_converter.git
   cd python_to_C_plus_plus_converter
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your API keys:
   - Create a `.env` file in the project root
   - Add your API keys (at least one is required):
     ```
     # Required: At least one of these API keys must be provided
     OPENAI_API_KEY=your_openai_api_key
     ANTHROPIC_API_KEY=your_anthropic_api_key
     GEMINI_API_KEY=your_gemini_api_key
     ```

## Usage

Run the application:
```bash
python main.py
```

The application will start a local web server, and you can access it in your browser at `http://localhost:7860` or another available port.

### How to Use

1. Enter or paste your Python code in the input area
2. Select your preferred AI model (GPT, Claude, or Gemini)
3. Click "Convert to C++" to generate the C++ equivalent
4. Use the "Run Python" and "Run C++" buttons to execute and compare the performance

## Examples

### Input (Python)
```python
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
```

### Output (C++)
```cpp
#include <iostream>
#include <iomanip>
#include <chrono>

int main() {
    auto start = std::chrono::high_resolution_clock::now();
    
    // Implementation of the calculate function
    auto calculate = [](size_t iterations, double param1, double param2) {
        double result = 1.0;
        for (size_t i = 1; i <= iterations; ++i) {
            double j = i * param1 - param2;
            result -= (1.0 / j);
            j = i * param1 + param2;
            result += (1.0 / j);
        }
        return result;
    };
    
    double result = calculate(100000000, 4.0, 1.0) * 4.0;
    
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    
    std::cout << std::fixed << std::setprecision(12);
    std::cout << "Result: " << result << std::endl;
    std::cout << "Execution Time: " << duration.count() << " seconds" << std::endl;
    
    return 0;
}

## Requirements

- Python 3.8+
- At least one of the following API keys is required:
  - OpenAI API key (for GPT models)
  - Anthropic API key (for Claude models)
  - Google AI API key (for Gemini models)

## Dependencies

- openai >= 1.0.0
- anthropic >= 0.7.0
- gradio >= 4.0.0
- python-dotenv >= 1.0.0

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
