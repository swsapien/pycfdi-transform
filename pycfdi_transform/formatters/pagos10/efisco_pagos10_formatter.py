from __future__ import annotations
from pycfdi_transform.formatters.formatter_interface import FormatterInterface
from pycfdi_transform.helpers.string_helper import StringHelper

class EfiscoPagos10Formatter(FormatterInterface):
    def __init__(self, cfdi_data: dict, empty_char:str = '', safe_numerics:bool = False) -> EfiscoPagos10Formatter:
        super().__init__(cfdi_data, empty_char, safe_numerics)
        assert 'cfdi33' in self._cfdi_data, 'Este formatter únicamente soporta datos de cfdi33.'
    
    @staticmethod
    def _get_id_pago(count_complement:int, count_pago:int, count_dr:int) -> str:
        return f"CP{count_complement}_P{count_pago}_DR{count_dr}"
    
    @staticmethod
    def _get_total_taxes(taxes:list, key:str) -> str:
        total = '0.00'
        for tax in taxes:
            total = StringHelper.sum_strings(total, tax[key])
        return total
    
    @staticmethod
    def _get_total_taxes_by_type(taxes:list, tax_classification:str, tax_type:str) -> str:
        total = '0.00'
        for tax in taxes:
            taxes_classificated = tax[tax_classification]
            for tax_classificated in taxes_classificated:
                if tax_classificated['impuesto'] == tax_type:
                    total = StringHelper.sum_strings(total, tax_classificated['importe'])
        return total

    def _get_part_complement(self) -> list:
        count_complement_pago = 1
        results = []
        for pagos10 in self._cfdi_data['pagos10']:
            count_pago = 1
            for pago in pagos10['pago']:
                count_dr = 1
                row = [
                    self._get_id_pago(count_complement_pago, count_pago, count_dr),
                    pago['fecha_pago'],
                    pago['forma_de_pago_p'],
                    pago['moneda_p'],
                    self._get_numeric_tipo_cambio_value(pago['tipo_cambio_p']),
                    pago['monto'],
                    self._get_str_value(pago['num_operacion']),
                    self._get_str_value(pago['rfc_emisor_cta_ord']),
                    self._get_str_value(pago['nom_banco_ord_ext']),
                    self._get_str_value(pago['cta_ordenante']),
                    self._get_str_value(pago['rfc_emisor_cta_ben']),
                    self._get_str_value(pago['cta_beneficiario']),
                ]

                if len(pago['impuestos']) > 0:
                    row.append(self._get_total_taxes_by_type(pago['impuestos'], 'traslados', '002'))
                    row.append(self._get_total_taxes_by_type(pago['impuestos'], 'traslados', '003'))
                    row.append(self._get_total_taxes(pago['impuestos'], 'total_impuestos_trasladados'))
                    row.append(self._get_total_taxes_by_type(pago['impuestos'], 'retenciones', '001'))
                    row.append(self._get_total_taxes_by_type(pago['impuestos'], 'retenciones', '002'))
                    row.append(self._get_total_taxes_by_type(pago['impuestos'], 'retenciones', '003'))
                    row.append(self._get_total_taxes(pago['impuestos'], 'total_impuestos_retenidos'))
                else:
                    row.extend(
                        [
                            self._get_numeric_default_value(),
                            self._get_numeric_default_value(),
                            self._get_numeric_default_value(),
                            self._get_numeric_default_value(),
                            self._get_numeric_default_value(),
                            self._get_numeric_default_value(),
                            self._get_numeric_default_value()
                        ]
                    )
                
                if len(pago['docto_relacionado']) > 0:
                    for docto in pago['docto_relacionado']:
                        row[0] = self._get_id_pago(count_complement_pago, count_pago, count_dr)
                        results.append(
                            row + [
                                docto['id_documento'],
                                self._get_str_value(docto['serie']),
                                self._get_str_value(docto['folio']),
                                docto['moneda_dr'],
                                self._get_numeric_tipo_cambio_value(docto['tipo_cambio_dr']),
                                docto['metodo_de_pago_dr'],
                                self._get_str_value(docto['num_parcialidad']),
                                self._get_numeric_value(docto['imp_saldo_ant']),
                                self._get_numeric_value(docto['imp_pagado']),
                                self._get_numeric_value(docto['imp_saldo_insoluto']),
                            ]
                        )
                        count_dr += 1
                else:
                    results.append(row + [
                        self._config['empty_char'],
                        self._config['empty_char'],
                        self._config['empty_char'],
                        self._config['empty_char'],
                        StringHelper.DEFAULT_SAFE_NUMBER_ONE if self._config['safe_numerics'] else self._config['empty_char'],
                        self._config['empty_char'],
                        self._config['empty_char'],
                        self._get_numeric_default_value(),
                        self._get_numeric_default_value(),
                        self._get_numeric_default_value()
                    ])
                count_pago += 1
            count_complement_pago += 1
        return results
        
    def dict_to_columns(self) -> list[list]:
        results = []
        pagos_list = self._get_part_complement()
        for tdf in self._cfdi_data['tfd11']:
            row = [
                self._cfdi_data['cfdi33']['version'],
                self._get_str_value(self._cfdi_data['cfdi33']['serie']),
                self._get_str_value(self._cfdi_data['cfdi33']['folio']),
                self._cfdi_data['cfdi33']['fecha'],
                self._cfdi_data['cfdi33']['no_certificado'],
                self._cfdi_data['cfdi33']['subtotal'],
                self._get_numeric_value(self._cfdi_data['cfdi33']['descuento']),
                self._cfdi_data['cfdi33']['total'],
                self._cfdi_data['cfdi33']['moneda'],
                self._get_numeric_tipo_cambio_value(self._cfdi_data['cfdi33']['tipo_cambio']),
                self._cfdi_data['cfdi33']['tipo_comprobante'],
                self._get_str_value(self._cfdi_data['cfdi33']['metodo_pago']),
                self._get_str_value(self._cfdi_data['cfdi33']['forma_pago']),
                self._get_str_value(self._cfdi_data['cfdi33']['condiciones_pago']),
                self._cfdi_data['cfdi33']['lugar_expedicion'],
                self._cfdi_data['cfdi33']['emisor']['rfc'],
                self._get_str_value(self._cfdi_data['cfdi33']['emisor']['nombre']),
                self._cfdi_data['cfdi33']['emisor']['regimen_fiscal'],
                self._cfdi_data['cfdi33']['receptor']['rfc'],
                self._get_str_value(self._cfdi_data['cfdi33']['receptor']['nombre']),
                self._cfdi_data['cfdi33']['receptor']['uso_cfdi'],
                tdf['uuid'],
                tdf['fecha_timbrado'],
                tdf['rfc_prov_cert'],
                tdf['sello_cfd']
            ]
            for pago_row in pagos_list:
                results.append(row + pago_row)
        return results
    
    def can_format(self) -> bool:
        if not 'pagos10' in self._cfdi_data or len(self._cfdi_data['pagos10']) == 0:
            self._errors.append('Not pagos10 in data.')
        elif not 'tfd11' in self._cfdi_data or len(self._cfdi_data['tfd11']) == 0:
            self._errors.append('Not tfd11 in data.')
        return len(self._errors) == 0
    
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
            "RFCPROVCERTIF",
            "SELLOCFD",
            "P_IDENTIFICADOR_PAGO",
            "P_FECHAPAGO",
            "P_FORMADEPAGOP",
            "P_MONEDAP",
            "P_TIPOCAMBIOP",
            "P_MONTO",
            "P_NUMOPERACION",
            "P_RFCEMISORCTAORD",
            "P_NOMBANCOORDEXT",
            "P_CTAORDENANTE",
            "P_RFCEMISORCTABEN",
            "P_CTABENEFICIARIO",
            "P_IVATRASLADO",
            "P_IEPSTRASLADO",
            "P_TOTALIMPUESTOSTRASLADADOS",
            "P_ISRRETENCION",
            "P_IVARETENCION",
            "P_IEPSRETENCION",
            "P_TOTALIMPUESTOSRETENIDOS",
            "P_DR_IDDOCUMENTO",
            "P_DR_SERIE",
            "P_DR_FOLIO",
            "P_DR_MONEDADR",
            "P_DR_TIPOCAMBIODR",
            "P_DR_METODODEPAGODR",
            "P_DR_NUMPARCIALIDAD",
            "P_DR_IMPSALDOANT",
            "P_DR_IMPPAGADO",
            "P_DR_IMPSALDOINSOLUTO"
        ]