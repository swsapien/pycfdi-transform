from __future__ import annotations
from pycfdi_transform.formatters.formatter_interface import FormatterInterface

class EfiscoCoreConceptsDetailFormatter(FormatterInterface):
    def __init__(self, cfdi_data: dict, empty_char:str = '', safe_numerics:bool = False) -> EfiscoCoreConceptsDetailFormatter:
        super().__init__(cfdi_data, empty_char, safe_numerics)

    def dict_to_columns(self) -> list[list]:
        results = []
        version = self.get_version()
        cfdi_version = version['cfdi']
        for tfd in self._cfdi_data[version['tfd']]:
            cfdi_row = [
                self._cfdi_data[cfdi_version]['version'],
                self._get_str_value(self._cfdi_data[cfdi_version]['serie']),
                self._get_str_value(self._cfdi_data[cfdi_version]['folio']),
                self._cfdi_data[cfdi_version]['fecha'],
                self._cfdi_data[cfdi_version]['no_certificado'],
                self._cfdi_data[cfdi_version]['subtotal'],
                self._get_numeric_value(self._cfdi_data[cfdi_version]['descuento']),
                self._cfdi_data[cfdi_version]['total'],
                self._cfdi_data[cfdi_version]['moneda'],
                self._get_numeric_tipo_cambio_value(self._cfdi_data[cfdi_version]['tipo_cambio']),
                self._cfdi_data[cfdi_version]['tipo_comprobante'],
                self._get_str_value(self._cfdi_data[cfdi_version]['metodo_pago']),
                self._get_str_value(self._cfdi_data[cfdi_version]['forma_pago']),
                self._get_str_value(self._cfdi_data[cfdi_version]['condiciones_pago']),
                self._cfdi_data[cfdi_version]['lugar_expedicion'],
                self._cfdi_data[cfdi_version]['emisor']['rfc'],
                self._get_str_value(self._cfdi_data[cfdi_version]['emisor']['nombre']),
                self._cfdi_data[cfdi_version]['emisor']['regimen_fiscal'],
                self._cfdi_data[cfdi_version]['receptor']['rfc'],
                self._get_str_value(self._cfdi_data[cfdi_version]['receptor']['nombre']),
                self._cfdi_data[cfdi_version]['receptor'].get('uso_cfdi', self._config['empty_char']),
                tfd['uuid'],
                tfd['fecha_timbrado'],
            ]

            for  idx, concept in enumerate(self._cfdi_data[cfdi_version]['conceptos']):

                concept_row = [
                    idx,
                    concept.get('clave_prod_serv', self._config['empty_char']),
                    concept.get('no_identificacion', self._config['empty_char']),
                    concept.get('cantidad', self._config['empty_char']),
                    concept.get('clave_unidad', self._config['empty_char']),
                    concept.get('unidad', self._config['empty_char']),
                    concept.get('descripcion', self._config['empty_char']),
                    concept.get('valor_unitario', self._config['empty_char']),
                    concept.get('descuento', self._config['empty_char']),
                    concept.get('importe', self._config['empty_char'])
                ]
                results.append(cfdi_row + concept_row)
        return results

    def get_version(self):
        if 'cfdi32' in self._cfdi_data:
            return {'cfdi': 'cfdi32', 'tfd': 'tfd10'}
        elif 'cfdi40' in self._cfdi_data:
            return {'cfdi': 'cfdi40', 'tfd': 'tfd11'}

        return {'cfdi': 'cfdi33', 'tfd': 'tfd11' }

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
            "SERIE",
            "FOLIO",
            "FECHA",
            "NOCERTIFICADO",
            "SUBTOTAL",
            "DESCUENTO",
            "TOTAL",
            "MONEDA",
            "TIPOCAMBIO",
            "TIPODECOMPROBANTE",
            "METODOPAGO",
            "FORMAPAGO",
            "CONDICIONESDEPAGO",
            "LUGAREXPEDICION",
            "EMISORRFC",
            "EMISORNOMBRE",
            "EMISORREGIMENFISCAL",
            "RECEPTORRFC",
            "RECEPTORNOMBRE",
            "RECEPTORUSOCFDI",
            "UUID",
            "FECHATIMBRADO",
            "C_ID",
            "C_CLAVEPRODSERV",
            "C_NOIDENTIFICACION",
            "C_CANTIDAD",
            "C_CLAVEUNIDAD",
            "C_UNIDAD",
            "C_DESCRIPCION",
            "C_VALORUNITARIO",
            "C_DESCUENTO",
            "C_IMPORTE"
        ]