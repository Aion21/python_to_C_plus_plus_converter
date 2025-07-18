# Python to C++ Code Converter

A tool that converts Python code to optimized C++ for improved performance, featuring a user-friendly web interface for testing and comparing execution results.

## Features

- **AI-Powered Conversion**: Utilizes advanced AI models (GPT and Claude) to convert Python code to optimized C++
- **Performance Comparison**: Run and compare execution times between Python and C++ implementations
- **User-Friendly Interface**: Built with Gradio for an intuitive web-based experience
- **Multiple AI Models**: Choose between different AI models for conversion
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
   - Add your OpenAI and/or Anthropic API keys:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ANTHROPIC_API_KEY=your_anthropic_api_key
     ```

## Usage

Run the application:
```bash
python main.py
```

The application will start a local web server, and you can access it in your browser at `http://localhost:7860` or another available port.

### How to Use

1. Enter or paste your Python code in the input area
2. Select your preferred AI model (GPT or Claude)
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
```

## Requirements

- Python 3.8+
- C++ compiler (clang++ recommended for M1 Mac)
- OpenAI API key (for GPT models)
- Anthropic API key (for Claude models)

## Dependencies

- openai >= 1.0.0
- anthropic >= 0.7.0
- gradio >= 4.0.0
- python-dotenv >= 1.0.0

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
