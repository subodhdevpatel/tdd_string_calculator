import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = r"[\n,]"
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]

        numbers = re.split(delimiter, numbers)
        return sum(int(n) for n in numbers)
