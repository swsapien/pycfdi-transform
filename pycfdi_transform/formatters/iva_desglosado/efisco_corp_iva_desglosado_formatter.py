from __future__ import annotations
from pycfdi_transform.formatters.formatter_interface import FormatterInterface
from pycfdi_transform.helpers.string_helper import StringHelper


class EfiscoCorpIvaDesglosadoFormatter(FormatterInterface):
    def __init__(self, cfdi_data: dict, empty_char: str = '', safe_numerics: bool = False) -> EfiscoCorpIvaDesglosadoFormatter:
        super().__init__(cfdi_data, empty_char, safe_numerics)
        assert 'cfdi33' in self._cfdi_data or 'cfdi40' in self._cfdi_data, 'Este formatter únicamente soporta datos de cfdi33 o cfdi40.'

    def dict_to_columns(self) -> list[list]:
        results = []
        version = self.get_version()
        cfdi_version = version['cfdi']
        for tfd in self._cfdi_data[version['tfd']]:
            for tipo_impuesto, impuestos in (('Traslado', self._cfdi_data[cfdi_version]['impuestos']['traslados']), ('Retencion', self._cfdi_data[cfdi_version]['impuestos']['retenciones'])):
                for impuesto in impuestos:
                    cfdi_row = [
                        tfd.get('uuid', self._config['empty_char']),
                        "",  # Field only required for CFDI type P
                        "",  # Field only required for CFDI type P
                        tipo_impuesto,
                        impuesto.get('impuesto', self._config['empty_char']),
                        StringHelper.get_numeric_value(impuesto.get('importe'),  self._config['empty_char'], self._config['safe_numerics']),
                        StringHelper.get_numeric_value(impuesto.get('base'), self._config['empty_char'], self._config['safe_numerics']),
                        impuesto.get('tipo_factor', self._config['empty_char']),
                        StringHelper.get_numeric_value(impuesto.get('tasa_o_cuota'), self._config['empty_char'], self._config['safe_numerics']),
                    ]
                    results.append(cfdi_row)
            if 'pagos20' in self._cfdi_data:
                results.extend(self._get_rows_from_payments(tfd.get('uuid', self._config['empty_char']), self._cfdi_data['pagos20']))

        return results

    def _get_rows_from_payments(self, uuid, payments_node):
        rows = []
        for payment_node in payments_node:
            for pago in payment_node['pago']:
                for doc_relacionado in pago['docto_relacionado']:
                    for nodo_impuesto in doc_relacionado['impuestos_dr']:
                        for tipo_impuesto, impuestos_dr in (('TrasladoDR', nodo_impuesto['traslados_dr']), ('RetencionDR', nodo_impuesto['retenciones_dr'])):
                            for impuesto_dr in impuestos_dr:
                                row = [
                                    uuid,
                                    doc_relacionado.get('id_documento', self._config['empty_char']),
                                    doc_relacionado.get('num_parcialidad', self._config['empty_char']),
                                    tipo_impuesto,
                                    impuesto_dr.get('impuesto_dr', self._config['empty_char']),
                                    StringHelper.get_numeric_value(impuesto_dr.get('importe_dr'), self._config['empty_char'], self._config['safe_numerics']),
                                    StringHelper.get_numeric_value(impuesto_dr.get('base_dr'), self._config['empty_char'], self._config['safe_numerics']),
                                    impuesto_dr.get('tipo_factor_dr', self._config['empty_char']),
                                    StringHelper.get_numeric_value(impuesto_dr.get('tasa_o_cuota_dr'), self._config['empty_char'], self._config['safe_numerics']),
                                ]
                                rows.append(row)
        return rows


    def _get_string_value(self, value):
        return value if value else self._config['empty_char']

    def _get_numeric_value(self, value):
        return value if value else StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']

    def get_version(self):
        if 'cfdi32' in self._cfdi_data:
            return {'cfdi': 'cfdi32', 'tfd': 'tfd10'}
        elif 'cfdi40' in self._cfdi_data:
            return {'cfdi': 'cfdi40', 'tfd': 'tfd11'}

        return {'cfdi': 'cfdi33', 'tfd': 'tfd11'}

    def can_format(self) -> bool:
        version = self.get_version()
        cfdi_version = version['cfdi']
        if self._cfdi_data[cfdi_version]['tipo_comprobante'] in ('I', 'E', 'P'):
            return True
        self._errors.append('Este formatter solo puede formatear tipos de comprobante I, E y P.')
        return False

    def get_errors(self) -> str:
        return '|'.join(self._errors)

    @staticmethod
    def get_columns_names() -> list[str]:
        return [
            "UUID",
            "UUID_DR",
            "PARCIALIDAD",
            "TIPO_IMPUESTOS",
            "IMPUESTO",
            "IMPORTE",
            "BASE",
            "TIPO_FACTOR",
            "TASA_O_CUOTA",
        ]
