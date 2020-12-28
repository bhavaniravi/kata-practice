import re


class Calculator:
    split_regex = "\n|,"
    default_regex = "//(.+)\n"

    def check_negatives(self, numbers):
        negatives = [num for num in numbers if num < 0]
        if negatives:
            raise AttributeError("Negatives not supported")

    def get_delimiter(self, numbers):
        if numbers.startswith("//"):
            delimiter_section = numbers.split("\n")[0].strip("//") 
            if "[" in delimiter_section:
                return "|".join(map(re.escape, re.findall(r'\[([^]]*)\]',delimiter_section)))
            return delimiter_section
        else:
            return self.split_regex
    
    def filter_1000(self, numbers):
        return [num for num in numbers if num < 1000]

    def add(self, numbers):
        if not numbers:
            return 0
            
        delimiter = self.get_delimiter(numbers)
        if "//" in numbers:
            numbers = numbers.split("\n")[1]

        numbers = list(map(int, re.split(delimiter, numbers)))
        
        self.check_negatives(numbers)
        numbers = self.filter_1000(numbers)
        return sum(numbers)