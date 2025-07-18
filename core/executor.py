import subprocess
import sys
import io
from typing import Optional, Tuple

def execute_python(code: str) -> str:
    """Execute Python code and return the output.
    
    Args:
        code: Python code to execute.
        
    Returns:
        The output of the execution.
    """
    try:
        output = io.StringIO()
        sys.stdout = output
        exec(code)
    finally:
        sys.stdout = sys.__stdout__
    return output.getvalue()

def execute_cpp(code: str, output_file: str = "optimized") -> Tuple[str, Optional[str]]:
    """Compile and execute C++ code.
    
    Args:
        code: C++ code to compile and execute.
        output_file: Name of the output executable.
        
    Returns:
        A tuple of (stdout, stderr) from the execution.
    """
    # Write the C++ code to a file
    with open(f"{output_file}.cpp", "w") as f:
        f.write(code)
    
    try:
        # Compile the C++ code with optimizations for M1 Mac
        compile_cmd = [
            "clang++", 
            "-O3",
            "-std=c++17", 
            "-march=armv8.5-a", 
            "-mtune=apple-m1",
            "-mcpu=apple-m1",
            "-o", output_file, 
            f"{output_file}.cpp"
        ]
        
        compile_result = subprocess.run(
            compile_cmd, 
            check=True, 
            text=True, 
            capture_output=True
        )
        
        # Run the compiled executable
        run_result = subprocess.run(
            [f"./{output_file}"], 
            check=True, 
            text=True, 
            capture_output=True
        )
        
        return run_result.stdout, None
        
    except subprocess.CalledProcessError as e:
        return e.stdout, e.stderr
    except Exception as e:
        return "", str(e)
