"""
A program that checks if the brackets in the given expression are symmetric.
Ignores spaces and is case insensitive.

The program takes an expression as input and checks if the brackets in the
expression are symmetric. If the brackets are symmetric, the program prints
"Symmetric", otherwise it prints "Not symmetric".
"""


def check_brackets(expression):
    """
    Checks if the brackets in the given expression are symmetric.

    Args:
        expression (str): The input string containing bracket characters.

    Returns:
        str: "Symmetric" if the brackets are balanced, "Not symmetric"
        otherwise.
    """
    # Create a stack to keep track of opening brackets
    stack = []
    # Define pairs of matching brackets
    bracket_pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for char in expression:
        # If the character is an opening bracket, push it onto the stack
        if char in bracket_pairs:
            stack.append(char)
        # If the character is a closing bracket
        elif char in bracket_pairs.values():
            # Check if there is a corresponding opening bracket in the stack
            if not stack or bracket_pairs[stack.pop()] != char:
                return "Not symmetric"

    # If the stack is empty, all opening brackets have been matched
    return "Symmetric" if not stack else "Not symmetric"


# Example usage:
print(check_brackets("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Symmetric
print(check_brackets("( 23 ( 2 - 3);"))            # Not symmetric
print(check_brackets("( 11 }"))                    # Not symmetric
print(check_brackets("{[()]}"))                    # Symmetric
print(check_brackets("{[(])}"))                    # Not symmetric
