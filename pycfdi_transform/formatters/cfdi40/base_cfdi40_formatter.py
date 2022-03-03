from __future__ import annotations
from abc import ABC, abstractmethod
from pycfdi_transform.formatters.formatter_interface import FormatterInterface
from pycfdi_transform.helpers.string_helper import StringHelper


class BaseCFDI40Formatter(FormatterInterface, ABC):
    """Class to format cfdi_data obtained from `CFDI40SAXHandler` in columnar form.

    Args:
        cfdi_data : dict 
                    Data obtained from `CFDI40SAXHandler`.
        empty_char : str, default: ''
                    Data added if the field has not data.
        safe_numerics : bool, default: False
                    If definied numeric data with not value is presented as 0.00 or 1.00 in case of TIPOCAMBIO.
    """

    def __init__(self, cfdi_data: dict, empty_char: str = '', safe_numerics: bool = False) -> BaseCFDI40Formatter:
        super().__init__(cfdi_data, empty_char, safe_numerics)
        assert 'cfdi40' in self._cfdi_data, 'Este formatter únicamente soporta datos de cfdi40.'
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
        if self._cfdi_data['cfdi40']['conceptos'] and len(self._cfdi_data['cfdi40']['conceptos']) > 0 and key in self._cfdi_data['cfdi40']['conceptos'][0]:
            return self._cfdi_data['cfdi40']['conceptos'][0][key]
        else:
            return self._config["empty_char"]

    def can_format(self) -> bool:
        """Validates if the provided data is valid and has TFD.
        This method allow to validate data previus of the process and avoid posible errors or exceptions.

        Usage example:
        ```
        formatter = EfiscoCorpCFDI40Formatter(cfdi_data)
        if formatter.can_format():
            data_columns = formatter.dict_to_columns()
        else:
            print(formatter.get_errors())
        ```

        Returns:
            bool: True if has valid data, otherwise False.
        """
        if not 'tfd11' in self._cfdi_data or len(self._cfdi_data['tfd11']) == 0:
            self._errors.append('Not tfd11 in data.')
        if not 'cfdi40' in self._cfdi_data or len(self._cfdi_data['cfdi40']) == 0:
            self._errors.append('Not cfdi data in dict provided.')
        return len(self._errors) == 0

    def get_errors(self) -> str:
        """Gets detailed errors in text format if method can_format returns false.

        Returns:
            str: Description with pipe separated errors. Returns empty string if no errors present.
        """
        return '|'.join(self._errors)

    def has_addenda(self) -> bool:
        """Checks if has addendas in cfdi_data

        Returns:
            bool: True if has addendas. False if equals to empty char or not definied field.
        """
        return 'addendas' in self._cfdi_data['cfdi40'] and self._cfdi_data['cfdi40']['addendas'] != self._config['empty_char']

    def get_addendas(self) -> str:
        """Gets field addendas of cfdi_data if has addendas.
        If not addendas present will return empty string.

        Returns:
            str: Addendas space separated.
        """
        return self._cfdi_data['cfdi40']['addendas'] if self.has_addenda() else ''

    @abstractmethod
    def dict_to_columns(self) -> list[list]:
        """Format data contained in dict to list matching every column with its asociated column.
        For complete list of columns use "get_columns_names".

        Usage example:
        ```
        formatter = EfiscoCorpCFDI40Formatter(cfdi_data)
        if formatter.can_format():
            data_columns = formatter.dict_to_columns()
            dict_columns = dict(zip(formatter.get_columns_names(), data_columns[0]))
        else:
            print(formatter.get_errors())
        ```

        Returns:
            list[list]: List of lists where each element is disctint TFD (if invoice only have 1 TFD expect only 1 element) 
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def get_columns_names() -> list[str]:
        """Gets a full list with columns names

        Returns:
            list[str]: List with columns names.
        """
        raise NotImplementedError
