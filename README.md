# TDD String Calculator using Python

## Overview

This project implements a **String Calculator** using **Test-Driven Development (TDD)** in Python. The calculator processes input strings to compute the sum of numbers while handling various delimiters and edge cases.

## Features

- **Basic Addition**: Computes the sum of numbers in a string.
- **Custom Delimiters**: Supports single and multi-character delimiters.
- **Multiple Delimiters**: Allows multiple custom delimiters.
- **Handling of Large Numbers**: Ignores numbers greater than 1000.
- **Negative Number Handling**: Raises exceptions for negative numbers.
- **Trailing Delimiters**: Handles input with trailing delimiters without errors.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `pytest` for running tests

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/subodhdevpatel/tdd_string_calculator.git
   cd tdd_string_calculator
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

Execute the test suite using:

```bash
pytest
```

## Usage

### Importing the Calculator

```python
from string_calculator import StringCalculator
```

### Examples

```python
calc = StringCalculator()

# Basic usage
print(calc.add(""))            # Output: 0
print(calc.add("1"))           # Output: 1
print(calc.add("1,2,3"))       # Output: 6

# Using newline as delimiter
print(calc.add("1\n2,3"))      # Output: 6

# Custom single-character delimiter
print(calc.add("//;\n1;2"))    # Output: 3

# Custom multi-character delimiter
print(calc.add("//[***]\n1***2***3"))  # Output: 6

# Multiple custom delimiters
print(calc.add("//[*][%]\n1*2%3"))     # Output: 6
```

### Handling Exceptions

```python
# Raises ValueError: Negatives not allowed: [-1, -3]
calc.add("-1,2,-3")

# Numbers greater than 1000 are ignored
print(calc.add("1,1001,2"))    # Output: 3
```

## Project Structure

- `string_calculator.py`: Contains the `StringCalculator` class and the `add` method.
- `test_string_calculator.py`: Comprises unit tests for the `StringCalculator` class.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

## Acknowledgments

This project follows **TDD best practices**, focusing on test-first development and continuous refactoring for clean and maintainable code.
