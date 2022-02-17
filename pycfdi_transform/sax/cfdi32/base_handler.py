from __future__ import annotations
from abc import ABC, abstractmethod
from pycfdi_transform.helpers.string_helper import StringHelper
from pycfdi_transform.sax.tfd10.sax_handler import TFD10SAXHandler
from pycfdi_transform.sax.implocal10.sax_handler import ImpLocal10SAXHandler
from pycfdi_transform.sax.nomina12.sax_handler import Nomina12SAXHandler
from pycfdi_transform.sax.nomina11.sax_handler import Nomina11SAXHandler
from pycfdi_transform.sax.pagos10.sax_handler import Pagos10SAXHandler


class BaseHandler(ABC):
    def __init__(self, empty_char: str = '', safe_numerics: bool = False, esc_delimiters: str = "") -> BaseHandler:
        super().__init__()
        self._config = {
            'concepts': False,
            'empty_char': empty_char,
            'safe_numerics': safe_numerics,
            'esc_delimiters': esc_delimiters
        }
        self._complements = {
            '{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital': {
                'class': TFD10SAXHandler,
                'key': 'tfd10'
            }
        }
        self.data = self._get_default_data()

    def _get_default_data(self):
        return {
            'cfdi32': {
                'version': self._config['empty_char'],
                'serie': self._config['empty_char'],
                'folio': self._config['empty_char'],
                'fecha': self._config['empty_char'],
                'no_certificado': self._config['empty_char'],
                'subtotal': StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],
                'descuento': StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],
                'total': StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],
                'moneda': self._config['empty_char'],
                'tipo_cambio': StringHelper.DEFAULT_SAFE_NUMBER_ONE if self._config['safe_numerics'] else self._config['empty_char'],
                'tipo_comprobante': self._config['empty_char'],
                'metodo_pago': self._config['empty_char'],
                'forma_pago': self._config['empty_char'],
                'condiciones_pago': self._config['empty_char'],
                'lugar_expedicion': self._config['empty_char'],
                'sello': self._config['empty_char'],
                'certificado': self._config['empty_char'],
                'emisor': {
                    'rfc': self._config['empty_char'],
                    'nombre': self._config['empty_char'],
                    'regimen_fiscal': []
                },
                'receptor': {
                    'rfc': self._config['empty_char'],
                    'nombre': self._config['empty_char']
                },
                'conceptos': [],
                'impuestos': {
                    'retenciones': [],
                    'traslados': [],
                    'total_impuestos_traslados': StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],
                    'total_impuestos_retenidos': StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']
                },
                'complementos': self._config['empty_char'],
                'addendas': self._config['empty_char']
            },
            'tfd10': []
        }

    def use_nomina11(self) -> BaseHandler:
        if not '{http://www.sat.gob.mx/nomina}Nomina' in self._complements:
            self._complements['{http://www.sat.gob.mx/nomina}Nomina'] = {
                'class': Nomina11SAXHandler,
                'key': 'nomina11'
            }
        return self

    def use_concepts_cfdi32(self) -> BaseHandler:
        self._config['concepts'] = True
        return self

    def use_implocal10(self) -> BaseHandler:
        if not '{http://www.sat.gob.mx/implocal}ImpuestosLocales' in self._complements:
            self._complements['{http://www.sat.gob.mx/implocal}ImpuestosLocales'] = {
                'class': ImpLocal10SAXHandler,
                'key': 'implocal10'
            }
        return self

    def _clean_data(self) -> None:
        self._data = self.data = self._get_default_data()

    @abstractmethod
    def transform_from_file(self, file_path: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    def transform_from_string(self, xml_str: str) -> dict:
        raise NotImplementedError
