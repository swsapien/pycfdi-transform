from __future__ import annotations
from abc import ABC, abstractmethod

class FormatterInterface(ABC):
    def __init__(self, cfdi_data:dict) -> FormatterInterface:
        super().__init__()
        assert type(cfdi_data) == dict, 'El Formatter debe recibir el objeto devuelto por la transformación el debe ser un dict.'
        self._cfdi_data = cfdi_data
    
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