from __future__ import annotations

from pycfdi_transform.formatters.cfdi40.base_cfdi40_formatter import BaseCFDI40Formatter


class EfiscoCorpCFDI40Formatter(BaseCFDI40Formatter):
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
        results = []
        for tfd in self._cfdi_data['tfd11']:
            row = [
                # VERSION
                self._cfdi_data['cfdi40']['version'],
                # SERIE
                self._get_str_value(self._cfdi_data['cfdi40']['serie']),
                # FOLIO
                self._get_str_value(self._cfdi_data['cfdi40']['folio']),
                # FECHA
                self._cfdi_data['cfdi40']['fecha'],
                # NOCERTIFICADO
                self._cfdi_data['cfdi40']['no_certificado'],
                # SUBTOTAL
                self._cfdi_data['cfdi40']['subtotal'],
                # DESCUENTO
                self._get_numeric_value(self._cfdi_data['cfdi40']['descuento']),
                # TOTAL
                self._cfdi_data['cfdi40']['total'],
                # MONEDA
                self._cfdi_data['cfdi40']['moneda'],
                # TIPOCAMBIO
                self._get_numeric_tipo_cambio_value(self._cfdi_data['cfdi40']['tipo_cambio']),
                # TIPODECOMPROBANTE
                self._cfdi_data['cfdi40']['tipo_comprobante'],
                # METODOPAGO
                self._get_str_value(self._cfdi_data['cfdi40']['metodo_pago']),
                # FORMAPAGO
                self._get_str_value(self._cfdi_data['cfdi40']['forma_pago']),
                # CONDICIONESDEPAGO
                self._get_str_value(self._cfdi_data['cfdi40']['condiciones_pago']),
                # LUGAREXPEDICION
                self._cfdi_data['cfdi40']['lugar_expedicion'],
                # EMISORRFC
                self._cfdi_data['cfdi40']['emisor']['rfc'],
                # EMISORNOMBRE
                self._get_str_value(self._cfdi_data['cfdi40']['emisor']['nombre']),
                # EMISORREGIMENFISCAL
                self._cfdi_data['cfdi40']['emisor']['regimen_fiscal'],
                # RECEPTORRFC
                self._cfdi_data['cfdi40']['receptor']['rfc'],
                # RECEPTORNOMBRE
                self._get_str_value(self._cfdi_data['cfdi40']['receptor']['nombre']),
                # RESIDENCIAFISCAL                
                self._get_str_value(self._cfdi_data['cfdi40']['receptor']['residencia_fiscal']),
                # NUMREGIDTRIB
                self._get_str_value(self._cfdi_data['cfdi40']['receptor']['num_reg_id_trib']),
                # RECEPTORUSOCFDI
                self._cfdi_data['cfdi40']['receptor']['uso_cfdi'],
                # CLAVEPRODSERV
                self._get_concept_value_by_key('clave_prod_serv'),
                # C_DESCRIPCION
                self._get_concept_value_by_key('descripcion'),
                # IVATRASLADO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi40']['impuestos'], 'traslados', '002'),
                # IEPSTRASLADO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi40']['impuestos'], 'traslados', '003'),
                # TOTALIMPUESTOSTRASLADOS
                self._get_numeric_value(self._cfdi_data['cfdi40']['impuestos']['total_impuestos_traslados']),
                # ISRRETENIDO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi40']['impuestos'], 'retenciones', '001'),
                # IVARETENIDO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi40']['impuestos'], 'retenciones', '002'),
                # IEPSRETENIDO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi40']['impuestos'], 'retenciones', '003'),
                # TOTALIMPUESTOSRETENIDOS
                self._get_numeric_value(self._cfdi_data['cfdi40']['impuestos']['total_impuestos_retenidos']),
                # TOTALTRASLADOSIMPUESTOSLOCALES
                self._get_implocal10_total_traslados(),
                # TOTALRETENCIONESIMPUESTOSLOCALES
                self._get_implocal10_total_retenciones(),
                # COMPLEMENTOS
                self._get_str_value(self._cfdi_data['cfdi40']['complementos']),
                # UUID                
                tfd['uuid'],
                # FECHATIMBRADO
                tfd['fecha_timbrado'],
                # RFCPROVCERTIF
                tfd['rfc_prov_cert'],
                # SELLOCFD
                tfd['sello_cfd'],
                # FORMAPAGO32
                '',
                # METODOPAGO32
                '',
                # MONEDA32
                '',
                # EMISORREGIMENFISCAL32
                '',
            ]
            results.append(row)
        return results

    @staticmethod
    def get_columns_names() -> list[str]:
        return [
            'VERSION',
            'SERIE',
            'FOLIO',
            'FECHA',
            'NOCERTIFICADO',
            'SUBTOTAL',
            'DESCUENTO',
            'TOTAL',
            'MONEDA',
            'TIPOCAMBIO',
            'TIPODECOMPROBANTE',
            'METODOPAGO',
            'FORMAPAGO',
            'CONDICIONESDEPAGO',
            'LUGAREXPEDICION',
            'EMISORRFC',
            'EMISORNOMBRE',
            'EMISORREGIMENFISCAL',
            'RECEPTORRFC',
            'RECEPTORNOMBRE',
            'RESIDENCIAFISCAL',
            'NUMREGIDTRIB',
            'RECEPTORUSOCFDI',
            'CLAVEPRODSERV',
            'C_DESCRIPCION',
            'IVATRASLADO',
            'IEPSTRASLADO',
            'TOTALIMPUESTOSTRASLADOS',
            'ISRRETENIDO',
            'IVARETENIDO',
            'IEPSRETENIDO',
            'TOTALIMPUESTOSRETENIDOS',
            'TOTALTRASLADOSIMPUESTOSLOCALES',
            'TOTALRETENCIONESIMPUESTOSLOCALES',
            'COMPLEMENTOS',
            'UUID',
            'FECHATIMBRADO',
            'RFCPROVCERTIF',
            'SELLOCFD',
            'METODOPAGO32',
            'FORMAPAGO32',
            'MONEDA32',
            'EMISORREGIMENFISCAL32'
        ]
