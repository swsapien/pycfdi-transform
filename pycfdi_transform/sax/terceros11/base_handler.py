from __future__ import annotations
from abc import ABC, abstractmethod


class BaseHandler(ABC):
    def __init__(self, empty_char='', safe_numerics=False, esc_delimiters: str = "") -> BaseHandler:
        super().__init__()
        self._config = {
            'empty_char': empty_char,
            'safe_numerics': safe_numerics,
            'esc_delimiters': esc_delimiters
        }
        self._data = {
            'version': empty_char,
            'rfc': empty_char,
            'nombre': empty_char,
            'informacionFiscal': {
                'calle': empty_char,
                'noExterior': empty_char,
                'noInterior': empty_char,
                'colonia': empty_char,
                'localidad': empty_char,
                'referencia': empty_char,
                'municipio': empty_char,
                'estado': empty_char,
                'pais': empty_char,
                'codigoPostal': empty_char
            },
            'cuentaPredial': {
                'numero': empty_char
            },
            'informacionAduanera': {
                'numero': empty_char,
                'fecha': empty_char,
                'aduana': empty_char
            },
            'impuestos': {
                'traslados': [],
                'retenciones': []
            }
        }

    @abstractmethod
    def transform_from_string(self, xml_str: str) -> dict:
        raise NotImplementedError
