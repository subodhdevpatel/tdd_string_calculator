import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = r"[,\n]"
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]

        num_list = list(map(int, re.split(delimiter, numbers)))
        negatives = [n for n in num_list if n < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")

        return sum(n for n in num_list if n <= 1000)
