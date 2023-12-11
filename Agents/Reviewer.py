## Reviewer Class: Objective is to look over existing code and add in documentation, similar to the docstrings that exist in inbuilt Python libraries.

## VERDICT: As of 2023-11-14, does not work. For some reason, none of the strings are showing up properly.

import re

def extract_functions_from_code(code):
    """
    Extracts function/method blocks from a Python code string using regular expressions.

    Args:
        code (str): The Python code string.

    Returns:
        list: A list of tuples containing function/method name and its block.
    """
    # Regular expression to match function/method blocks
    pattern = re.compile(r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\([^)]*\)\s*:")
    
    # Find all matches in the code
    matches = pattern.finditer(code)
    
    # Extract function/method names and blocks
    functions = []
    for match in matches:
        function_name = match.group(1)
        
        # Find the start and end positions of the function block
        start_pos = match.end()
        end_pos = find_matching_brace(code, start_pos)
        
        if end_pos is not None:
            function_block = code[start_pos:end_pos]
            functions.append((function_name, function_block))
    
    return functions

def find_matching_brace(code, start_pos):
    """
    Finds the position of the matching closing brace for the opening brace at start_pos.

    Args:
        code (str): The Python code string.
        start_pos (int): The position of the opening brace.

    Returns:
        int: The position of the matching closing brace or None if not found.
    """
    count = 1
    current_pos = start_pos
    while count > 0 and current_pos < len(code):
        current_char = code[current_pos]
        if current_char == "{":
            count += 1
        elif current_char == "}":
            count -= 1
        current_pos += 1
    
    return current_pos if count == 0 else None

# Example usage:
with open("Reviewer.py", "r") as file:
    python_code = file.read()


functions = extract_functions_from_code(python_code)

# Print the detected functions and their blocks
for function_name, function_block in functions:
    print(f"Function/Method Name: {function_name}")
    print(f"Function/Method Block:\n{function_block}\n")

