from decimal import Decimal, InvalidOperation
class StringHelper:
    DEFAULT_SAFE_NUMBER_CERO = '0.00'
    DEFAULT_SAFE_NUMBER_ONE = '1.00'

    @staticmethod
    def file_path_to_string(file_path:str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    @staticmethod
    def compact_string(delimiters,string) -> str:
        if not string:
            return string
        new_str = string.translate(str.maketrans('', '', '\n\t\r'+delimiters))
        while '  ' in new_str:
            new_str = new_str.replace('  ', ' ')
        return new_str.strip()
    
    @staticmethod
    def sum_strings(first_val, second_val) -> str:
        if not first_val:
            return second_val
        elif not second_val:
            return first_val
        
        return str(StringHelper.try_parse_decimal(first_val) + StringHelper.try_parse_decimal(second_val))
    
    @staticmethod
    def try_parse_decimal(val)->Decimal:
        try:
            Decimal(val)
        except InvalidOperation:
            return Decimal(0.00)
        else:
            return Decimal(val)
