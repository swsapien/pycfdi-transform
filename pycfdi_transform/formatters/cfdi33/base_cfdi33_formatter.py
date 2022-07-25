from __future__ import annotations
from abc import ABC, abstractmethod
from pycfdi_transform.formatters.formatter_interface import FormatterInterface
from pycfdi_transform.helpers.string_helper import StringHelper


class BaseCFDI33Formatter(FormatterInterface, ABC):
    def __init__(self, cfdi_data: dict, empty_char: str = '', safe_numerics: bool = False) -> BaseCFDI33Formatter:
        super().__init__(cfdi_data, empty_char, safe_numerics)
        assert 'cfdi33' in self._cfdi_data, 'Este formatter únicamente soporta datos de cfdi33.'
        self._config = {
            'empty_char': empty_char,
            'safe_numerics': safe_numerics
        }
        self._errors = []

    @staticmethod
    def _get_total_taxes_by_type(taxes: list, tax_classification: str, tax_type: str) -> str:
        total = '0.00'
        taxes_classificated = taxes[tax_classification]
        for tax in taxes_classificated:
            if tax['impuesto'] == tax_type:
                total = StringHelper.sum_strings(total, tax['importe'])
        return total

    def _get_implocal10_total_retenciones(self) -> list:
        total = self._get_numeric_default_value()
        if 'implocal10' in self._cfdi_data:
            for tax in self._cfdi_data['implocal10']:
                if tax['total_retenciones_impuestos_locales']:
                    total = StringHelper.sum_strings(total, tax['total_retenciones_impuestos_locales'])
        return total

    def _get_implocal10_total_traslados(self) -> list:
        total = self._get_numeric_default_value()
        if 'implocal10' in self._cfdi_data:
            for tax in self._cfdi_data['implocal10']:
                if tax['total_traslados_impuestos_locales']:
                    total = StringHelper.sum_strings(total, tax['total_traslados_impuestos_locales'])
        return total

    def _get_concept_value_by_key(self, key: str) -> str:
        if self._cfdi_data['cfdi33']['conceptos'] and len(self._cfdi_data['cfdi33']['conceptos']) > 0 and key in self._cfdi_data['cfdi33']['conceptos'][0]:
            return self._cfdi_data['cfdi33']['conceptos'][0][key]
        else:
            return self._config["empty_char"]

    def _get_concept_value_by_key_concatenated(self, key: str) -> str:
        if self._cfdi_data['cfdi33']['conceptos'] and len(self._cfdi_data['cfdi33']['conceptos']) > 0:
            items = [d for d in self._cfdi_data['cfdi33']['conceptos'] if key in d.keys()]
            itemsList = list((i[key] for i in items))
            itemsGroup = list(set(itemsList))
            itemsGroup.sort()
            return ','.join(itemsGroup)
        else:
            return self._config["empty_char"]

    def can_format(self) -> bool:
        if not 'tfd11' in self._cfdi_data or len(self._cfdi_data['tfd11']) == 0:
            self._errors.append('Not tfd11 in data.')
        return len(self._errors) == 0

    def get_errors(self) -> str:
        return '|'.join(self._errors)

    @abstractmethod
    def dict_to_columns(self) -> list[list]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def get_columns_names() -> list[str]:
        raise NotImplementedError
