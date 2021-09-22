from decimal import Decimal
class StringHelper:
    DEFAULT_SAFE_NUMBER_CERO = '0.00'
    DEFAULT_SAFE_NUMBER_ONE = '1.00'
    @staticmethod
    def file_path_to_string(file_path:str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    @staticmethod
    def compact_string(string) -> str:
        if not string:
            return string
        new_str = string.translate(str.maketrans('', '', '\n\t\r'))
        while '  ' in new_str:
            new_str = new_str.replace('  ', ' ')
        return new_str
    @staticmethod
    def sum_strings(first_val, second_val) -> str:
        if first_val == '':
            return second_val
        elif second_val == '':
            return first_val
        return str(Decimal(first_val) + Decimal(second_val))