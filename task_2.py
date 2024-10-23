"""
A program that checks if a string is a palindrome using a deque.
Ignores spaces and is case insensitive.

The program takes a string as input and checks if it is a palindrome.
If the string is a palindrome, the program prints "True", otherwise it prints
"False".
"""

from collections import deque


def is_palindrome(input_string):
    """
    Checks if the provided string is a palindrome using a deque.
    Ignores spaces and is case insensitive.

    Args:
        input_string (str): The input string to be checked.

    Returns:
        bool: True if the input string is a palindrome, False otherwise.
    """
    # Convert the string to lowercase and remove spaces
    sanitized_string = ''.join(input_string.lower().split())

    # Add characters to a deque
    char_deque = deque(sanitized_string)

    # Compare characters from both ends of the deque
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


# Example usage
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("racecar"))  # True
