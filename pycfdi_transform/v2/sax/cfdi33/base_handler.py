from __future__ import annotations
from abc import ABC, abstractmethod
from lxml import etree
from pycfdi_transform.v2.helpers.string_helper import StringHelper
from pycfdi_transform.v2.sax.tfd.sax_handler import TFDSAXHandler
from pycfdi_transform.v2.sax.implocal.sax_handler import ImpLocalSAXHandler
from pycfdi_transform.v2.sax.nomina12.sax_handler import Nomina12SAXHandler
from pycfdi_transform.v2.sax.pagos10.sax_handler import Pagos10SAXHandler

class BaseHandler(ABC):
    def __init__(self, empty_char:str = '', safe_numerics:bool = False, schema_validator:etree.XMLSchema = None) -> BaseHandler:
        super().__init__()
        self._schema_validator = schema_validator
        self._config = {
            'concepts': False,
            'empty_char': empty_char,
            'safe_numerics': safe_numerics
        }
        self._complements = {
            '{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital': {
                'class': TFDSAXHandler,
                'key': 'tfd'
            },
            '{http://www.sat.gob.mx/implocal}ImpuestosLocales': {
                'class': ImpLocalSAXHandler,
                'key': 'implocal'
            }
        }
        self._data = {
            'cfdi33': {
                'version': empty_char,
                'serie': empty_char,
                'folio': empty_char,
                'fecha': empty_char,
                'no_certificado': empty_char,
                'subtotal': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
                'descuento': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
                'total': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
                'moneda': empty_char,
                'tipo_cambio': StringHelper.DEFAULT_SAFE_NUMBER_ONE if safe_numerics else empty_char,
                'tipo_comprobante': empty_char,
                'metodo_pago': empty_char,
                'forma_pago': empty_char,
                'condiciones_pago': empty_char,
                'lugar_expedicion': empty_char,
                'emisor': {
                    'rfc': empty_char,
                    'nombre': empty_char,
                    'regimen_fiscal': empty_char
                },
                'receptor': {
                    'rfc': empty_char,
                    'nombre': empty_char,
                    'residencia_fiscal': empty_char,
                    'num_reg_id_trib': empty_char,
                    'uso_cfdi': empty_char,
                },
                'conceptos': [],
                'impuestos': {
                    'retenciones': [],
                    'traslados': []
                },
                'complementos': empty_char,
                'addendas': empty_char
            },
            'tfd': [],
            'implocal': []
        }
    
    def use_nomina12(self) -> BaseHandler:
        if not '{http://www.sat.gob.mx/nomina12}Nomina' in self._complements:
            self._complements['{http://www.sat.gob.mx/nomina12}Nomina'] = {
                'class': Nomina12SAXHandler,
                'key': 'nomina12'
            }
        return self
    
    def use_concepts_cfdi33(self) -> BaseHandler:
        self._config['concepts'] = True
        return self
    
    def use_pagos10(self) -> BaseHandler:
        if not '{http://www.sat.gob.mx/Pagos}Pagos' in self._complements:
            self._complements['{http://www.sat.gob.mx/Pagos}Pagos'] = {
                'class': Pagos10SAXHandler,
                'key': 'pagos10'
            }
        return self
    
    @abstractmethod
    def transform_from_file(self, file_path:str) -> dict:
        pass
    
    @abstractmethod
    def transform_from_string(self, xml_str:str) -> dict:
        pass