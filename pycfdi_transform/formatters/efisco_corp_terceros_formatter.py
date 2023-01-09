from __future__ import annotations
from pycfdi_transform.formatters.formatter_interface import FormatterInterface


class EfiscoCorpTercerosFormatter(FormatterInterface):
    def __init__(self, cfdi_data: dict, empty_char: str = '', safe_numerics: bool = False) -> EfiscoCorpTercerosFormatter:
        super().__init__(cfdi_data, empty_char, safe_numerics)

    def dict_to_columns(self) -> list[list]:
        results = []
        version = self.get_version()
        cfdi_version = version['cfdi']
        for tfd in self._cfdi_data[version['tfd']]:
            cfdi_row = [
                self._cfdi_data[cfdi_version]['version'],
                tfd['uuid'],
                tfd['fecha_timbrado'],
            ]

            for idx, concept in enumerate(self._cfdi_data[cfdi_version]['conceptos']):
                if concept['terceros'].get('nombre') or concept['terceros'].get('rfc'):
                    concept_row = [
                        concept['terceros'].get('nombre', self._config['empty_char']),
                        concept['terceros'].get('rfc', self._config['empty_char'])
                    ]
                    results.append(cfdi_row + concept_row)

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
        if 'conceptos' in self._cfdi_data[cfdi_version]:
            return True
        self._errors.append('No concepts key')
        return False

    def get_errors(self) -> str:
        return '|'.join(self._errors)

    @staticmethod
    def get_columns_names() -> list[str]:
        return [
            "VERSION",
            "UUID",
            "FECHATIMBRADO",
            "TERCERONOMBRE",
            "TERCERORFC"
        ]
