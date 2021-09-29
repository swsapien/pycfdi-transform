from __future__ import annotations
from pycfdi_transform.helpers.string_helper import StringHelper

class CFDI33BaseFormatter():
    def __init__(self, cfdi_data: dict, empty_char:str = '', safe_numerics:bool = False) -> CFDI33BaseFormatter:
        super().__init__(cfdi_data)
        assert 'cfdi33' in self._cfdi_data, 'Este formatter únicamente soporta datos de cfdi33.'
        self._config = {
            'empty_char': empty_char,
            'safe_numerics': safe_numerics
        }
        self._errors = []
    
    @staticmethod
    def _get_total_taxes_by_type(taxes:list, tax_classification:str, tax_type:str) -> str:
        total = '0.00'
        taxes_classificated = taxes[tax_classification]
        for tax in taxes_classificated:
            if tax['impuesto'] == tax_type:
                total = StringHelper.sum_strings(total, tax['importe'])
        return total
    
    def _get_implocal10_total_retenciones(self) -> list:
        if 'implocal10' in self._cfdi_data:
            return self._cfdi_data['implocal10']['total_retenciones_impuestos_locales']
        else:
            return self._get_numeric_default_value()
    
    def _get_implocal10_total_traslados(self) -> list:
        if 'implocal10' in self._cfdi_data:
            return self._cfdi_data['implocal10']['total_traslados_impuestos_locales']
        else:
            return self._get_numeric_default_value()
    
    def _get_numeric_default_value(self)->str:
        return StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']
        
    def can_format(self) -> bool:
        if not 'tfd11' in self._cfdi_data or len(self._cfdi_data['tfd11']) == 0:
            self._errors.append('Not tfd11 in data.')
        return len(self._errors) == 0
    
    def get_errors(self) -> str:
        return '|'.join(self._errors)