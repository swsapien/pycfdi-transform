from __future__ import annotations
from abc import ABC, abstractmethod

class FormatterInterface(ABC):
    def __init__(self, cfdi_data:dict, empty_char:str = '', safe_numerics:bool = False) -> FormatterInterface:
        super().__init__()
        assert type(cfdi_data) == dict, 'El Formatter debe recibir el objeto devuelto por la transformación el debe ser un dict.'
        self._cfdi_data = cfdi_data
        self._config = {
            'empty_char': empty_char,
            'safe_numerics': safe_numerics
        }
        self._errors = []
    
    @abstractmethod
    def dict_to_columns(self) -> list[list]:
        raise NotImplementedError
    
    @abstractmethod
    def get_columns_names(self) -> list[str]:
        raise NotImplementedError
    
    @abstractmethod
    def can_format(self) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def get_errors(self) -> str:
        raise NotImplementedError