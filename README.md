# Queue and Stack Algorithms

This repository contains solutions to three tasks involving data structures such as queues and stacks in Python. Each task focuses on a specific algorithmic challenge, including request handling with queues, palindrome checking using a deque, and bracket balancing using a stack.

## Table of Contents

- [Task 1: Request Handling Simulation](#task-1-request-handling-simulation)
- [Task 2: Palindrome Check Using Deque](#task-2-palindrome-check-using-deque)
- [Task 3: Bracket Balancing Using a Stack](#task-3-bracket-balancing-using-a-stack)
- [How to Run](#how-to-run)
- [Examples](#examples)
- [Requirements](#requirements)
- [License](#license)

## Task 1: Request Handling Simulation

Simulates a service center that accepts and processes incoming requests using a queue.

- **Description**:

  - Requests are automatically generated and added to a queue.
  - Requests are processed in the order they were received (FIFO - First In, First Out).
  - When the queue is empty, a message is displayed.

- **Usage**:

  - `generate_request()`: Generates a new request and adds it to the queue.
  - `process_request()`: Processes the first request in the queue.

- **Key Concepts**: Queue, FIFO, request generation and processing.

## Task 2: Palindrome Check Using Deque

Checks whether a given string is a palindrome using a deque.

- **Description**:

  - Adds all characters of the input string into a deque.
  - Compares characters from both ends of the deque to check for symmetry.
  - Ignores case and spaces.

- **Usage**:

  - `is_palindrome(input_string)`: Returns `True` if the input string is a palindrome, `False` otherwise.

- **Key Concepts**: Deque, palindrome, character comparison.

## Task 3: Bracket Balancing Using a Stack

Validates whether the sequence of brackets in a string is balanced.

- **Description**:

  - Uses a stack to track opening brackets.
  - Checks for corresponding closing brackets to ensure they match.
  - Handles various types of brackets including `()`, `{}`, and `[]`.

- **Usage**:

  - `check_brackets(expression)`: Returns `Symmetric` if the brackets are balanced, `Not symmetric` otherwise.

- **Key Concepts**: Stack, LIFO (Last In, First Out), bracket matching.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Iryna-Holova/goit-algo-hw-02.git
   cd goit-algo-hw-02
   ```

2. Ensure you have Python 3 installed. Run each Python file corresponding to the task:

   ```bash
   python task1.py
   python task2.py
   python task3.py
   ```

3. Follow the instructions in each file to see the output.

## Examples

### Example output for Task 1:

```python
Generating request #1
Processing Request #1
Request #1 has been processed
Generating request #2
Processing Request #2
Request #2 has been processed
...
```

### Example for Task 2:

```python
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
print(is_palindrome("Hello"))                        # Output: False
```

### Example for Task 3:

```python
print(check_brackets("( ){[ 1 ]( 1 + 3 )( ){ }}")) # Output: Symmetric
print(check_brackets("( 23 ( 2 - 3);"))            # Output: Not symmetric
print(check_brackets("{[()]}"))                    # Output: Symmetric
print(check_brackets("{[(])}"))                    # Output: Not symmetric
```

## Requirements

- Python 3.7+
- Standard Python libraries: `queue`, `collections`

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
