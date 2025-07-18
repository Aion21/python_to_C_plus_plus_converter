from typing import Dict, List

SYSTEM_MESSAGE = (
    "You are an assistant that reimplements Python code in high performance C++ for an M1 Mac. "
    "Respond only with C++ code; use comments sparingly and do not provide any explanation other than occasional comments. "
    "The C++ response needs to produce an identical output in the fastest possible time."
)

def build_user_prompt(python_code: str) -> str:
    """Construct the user prompt for code conversion.
    
    Args:
        python_code: The Python code to be converted to C++.
        
    Returns:
        A formatted prompt string.
    """
    prompt = (
        "Rewrite this Python code in C++ with the fastest possible implementation that produces identical output in the least time. "
        "Respond only with C++ code; do not explain your work other than a few comments. "
        "Pay attention to number types to ensure no int overflows. "
        "IMPORTANT: You MUST include all necessary C++ headers at the top of the file, including:"
        "#include <iostream> for input/output"
        "#include <iomanip> for std::setprecision and other I/O manipulators"
        "#include <chrono> for timing functions"
        "#include <cmath> for math functions"
        
        "Make sure to use proper C++ types (like size_t, int64_t, etc.) and include <cstdint> if needed.\n\n"
        f"{python_code}"
    )
    return prompt

def get_messages(python_code: str) -> List[Dict[str, str]]:
    """Get the messages for the AI model.
    
    Args:
        python_code: The Python code to be converted.
        
    Returns:
        A list of message dictionaries for the AI model.
    """
    return [
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": build_user_prompt(python_code)}
    ]
