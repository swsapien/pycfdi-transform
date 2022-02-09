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
            'version': self._config['empty_char'],
            'registro_patronal': self._config['empty_char'],
            'num_empleado': self._config['empty_char'],
            'curp': self._config['empty_char'],
            'tipo_regimen': self._config['empty_char'],
            'num_seguridad_social': self._config['empty_char'],
            'fecha_pago': self._config['empty_char'],
            'fecha_inicial_pago': self._config['empty_char'],
            'fecha_final_pago': self._config['empty_char'],
            'num_dias_pagados': self._config['empty_char'],
            'departamento': self._config['empty_char'],
            'clabe': self._config['empty_char'],
            'banco': self._config['empty_char'],
            'fecha_inicio_rel_laboral': self._config['empty_char'],
            'antiguedad': self._config['empty_char'],
            'puesto': self._config['empty_char'],
            'tipo_contrato': self._config['empty_char'],
            'tipo_jornada': self._config['empty_char'],
            'periodicidad_pago': self._config['empty_char'],
            'salario_base_cot_apor':StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],
            'riesgo_puesto': self._config['empty_char'],
            'salario_diario_integrado': StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],
            'percepciones': {
                'total_gravado': StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],
                'total_exento': StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],
                'percepcion': []
            },
            'deducciones': {
                'total_gravado': StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],
                'total_exento': StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],
                'deduccion': []
            },
            'incapacidades': {
                'incapcidad': []
            },
            'horas_extras': {
                'horas_extra': []
            }
        }

    @abstractmethod
    def transform_from_string(self, xml_str:str) -> dict:
        raise NotImplementedError