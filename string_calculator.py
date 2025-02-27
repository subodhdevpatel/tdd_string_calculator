import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = r"[,\n]"
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiters = re.findall(r"\[(.*?)\]", parts[0])
            delimiter = (
                "|".join(map(re.escape, delimiters))
                if delimiters
                else re.escape(parts[0][2:])
            )
            numbers = parts[1]

        num_list = [int(n) for n in re.split(delimiter, numbers) if n]
        negatives = [n for n in num_list if n < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")

        return sum(n for n in num_list if n <= 1000)
