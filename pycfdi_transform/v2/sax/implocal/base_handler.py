from __future__ import annotations
from abc import ABC, abstractmethod
from pycfdi_transform.v2.helpers.string_helper import StringHelper

class BaseHandler(ABC):
    def __init__(self, empty_char = '', safe_numerics = False) -> BaseHandler:
        super().__init__()
        self._config = {
            'empty_char': empty_char,
            'safe_numerics': safe_numerics
        }
        self._data = {
            'total_traslados_impuestos_locales': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
            'total_retenciones_impuestos_locales': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
        }

    @abstractmethod
    def transform_from_string(self, xml_str:str) -> dict:
        pass