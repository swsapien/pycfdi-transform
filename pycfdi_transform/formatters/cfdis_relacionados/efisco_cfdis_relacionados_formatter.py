from __future__ import annotations

from pycfdi_transform.formatters.formatter_interface import FormatterInterface

class EfiscoCfdisRelacionadosFormatter(FormatterInterface):
    def __init__(self, cfdi_data: dict, empty_char: str = '', safe_numerics: bool = False) -> EfiscoCfdisRelacionadosFormatter:
        super().__init__(cfdi_data, empty_char, safe_numerics)
        assert 'cfdi33' in self._cfdi_data or 'cfdi40' in self._cfdi_data, 'Este formatter únicamente soporta datos de cfdi33 o cfdi40.'

    def dict_to_columns(self) -> list[list]:
        results = []
        version = self.get_version()
        cfdi_version = version['cfdi']
        for tfd in self._cfdi_data[version['tfd']]:
            cfdi_row = [
                tfd['uuid']
            ]

            for idx, related_cfdi in enumerate(self._cfdi_data[cfdi_version]['cfdis_relacionados']):
                related_cfdi_row = [
                    related_cfdi.get('tipo_relacion', self._config['empty_char']),
                    related_cfdi.get('uuid', self._config['empty_char'])
                ]
                results.append(cfdi_row + related_cfdi_row)

        return results

    def get_version(self):
        if 'cfdi32' in self._cfdi_data:
            return {'cfdi': 'cfdi32', 'tfd': 'tfd10'}
        elif 'cfdi40' in self._cfdi_data:
            return {'cfdi': 'cfdi40', 'tfd': 'tfd11'}

        return {'cfdi': 'cfdi33', 'tfd': 'tfd11'}

    def can_format(self) -> bool:
        version = self.get_version()
        cfdi_version = version['cfdi']
        if 'cfdis_relacionados' in self._cfdi_data[cfdi_version]:
            return True
        self._errors.append('No related cfdis')
        return False

    def get_errors(self) -> str:
        return '|'.join(self._errors)

    @staticmethod
    def get_columns_names() -> list[str]:
        return [
            "UUID",
            "TIPORELACION",
            "IDDOCUMENTO"
        ]
