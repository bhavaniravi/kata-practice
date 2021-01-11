import re
class Calculator:

    def get_delimiter(self, numbers):
        delimiter_section = numbers.split("\n")[0].strip("//") 
        if "[" in delimiter_section:
            return "".join(map(re.escape, re.findall(r'\[([^]]*)\]',delimiter_section)))
        return delimiter_section


    def add(self, string):
        if not string:
            return 0 
        delimiter = ",|\n"

        if string.startswith("//"):
            delimiter = self.get_delimiter(string)
            string = string.split("\n", maxsplit=1)[1]

        numbers = map(int, re.split(delimiter, string))
        new_numbers = []
        for num in numbers:
            if num < 0:
                raise Exception("Negatives not supported")
            if num < 1000:
                new_numbers.append(num)

        return sum(new_numbers)