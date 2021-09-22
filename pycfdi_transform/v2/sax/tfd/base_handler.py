from __future__ import annotations
from abc import ABC, abstractmethod

class BaseHandler(ABC):
    def __init__(self, empty_char = '', safe_numerics = False) -> BaseHandler:
        super().__init__()
        self._config = {
            'empty_char': empty_char,
            'safe_numerics': safe_numerics
        }
        self._data = {
            'uuid': empty_char,
            'fecha_timbrado': empty_char,
            'rfc_prov_cert': empty_char,
            'sello_cfd': empty_char
        }
    
    @abstractmethod
    def transform_from_string(self, xml_str:str) -> dict:
        pass