from __future__ import annotations
from abc import ABC, abstractmethod

class BaseHandler(ABC):
    def __init__(self, empty_char = '', safe_numerics = False,esc_delimiters:str = "") -> BaseHandler:
        super().__init__()
        self._config = {
            'empty_char': empty_char,
            'safe_numerics': safe_numerics,
            'esc_delimiters':esc_delimiters
        }
        self._data = {
            'version': empty_char,
            'no_certificado_sat': empty_char,
            'uuid': empty_char,
            'fecha_timbrado': empty_char,
            'rfc_prov_cert': empty_char,
            'sello_cfd': empty_char
        }
    
    @abstractmethod
    def transform_from_string(self, xml_str:str) -> dict:
        raise NotImplementedError