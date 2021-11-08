from __future__ import annotations
from abc import ABC, abstractmethod
from pycfdi_transform.helpers.string_helper import StringHelper

class BaseHandler(ABC):
    def __init__(self, empty_char='', safe_numerics=False, esc_delimiters:str = "") -> BaseHandler:
        super().__init__()
        self._config = {
            'empty_char': empty_char,
            'safe_numerics': safe_numerics,
            'esc_delimiters':esc_delimiters
        }
        self._data = {
            'version': empty_char,
            'tipo_nomina': empty_char,
            'fecha_pago': empty_char,
            'fecha_inicial_pago': empty_char,
            'fecha_final_pago': empty_char,
            'num_dias_pagados': empty_char,
            'total_percepciones': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
            'total_deducciones': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
            'total_otros_pagos': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
            'emisor': {
                'curp': empty_char,
                'registro_patronal': empty_char,
                'rfc_patron_origen': empty_char,
                'entidad_SNCF': {
                    'origen_recurso': empty_char,
                    'monto_recurso_propio': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char
                }
            },
            'receptor': {
                'curp': empty_char,
                'num_seguridad_social': empty_char,
                'fecha_inicio_rel_laboral': empty_char,
                'antigüedad': empty_char,
                'tipo_contrato': empty_char,
                'sindicalizado': empty_char,
                'tipo_jornada': empty_char,
                'tipo_regimen': empty_char,
                'num_empleado': empty_char,
                'departamento': empty_char,
                'puesto': empty_char,
                'riesgo_puesto': empty_char,
                'periodicidad_pago': empty_char,
                'banco': empty_char,
                'cuenta_bancaria': empty_char,
                'salario_base_cot_apor': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
                'salario_diario_integrado': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
                'clave_ent_fed': empty_char,
                'subcontratacion': []
            },
            'percepciones': {
                'total_sueldos': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
                'total_separacion_indemnizacion': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
                'total_jubilacion_pension_retiro': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
                'total_gravado': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
                'total_exento': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
                'percepcion': []
            },
            'deducciones': {
                'total_otras_deducciones': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
                'total_impuestos_retenidos': StringHelper.DEFAULT_SAFE_NUMBER_CERO if safe_numerics else empty_char,
                'deduccion': []
            },
            'otros_pagos': {
                'otro_pago': []
            },
            'incapacidades': {
                'incapcidad': []
            }
        }

    @abstractmethod
    def transform_from_string(self, xml_str:str) -> dict:
        raise NotImplementedError