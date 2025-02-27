import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        numbers = re.split(r"[\n,]", numbers)
        return sum(int(n) for n in numbers)
