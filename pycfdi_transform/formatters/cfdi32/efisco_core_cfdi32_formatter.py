from __future__ import annotations

from pycfdi_transform.formatters.cfdi32.base_cfdi32_formatter import BaseCFDI32Formatter


class EfiscoCoreCFDI32Formatter(BaseCFDI32Formatter):
    def dict_to_columns(self) -> list[list]:
        results = []
        for tfd in self._cfdi_data['tfd10']:
            row = [
                # VERSION
                self._cfdi_data['cfdi32']['version'],
                # SERIE
                self._get_str_value(self._cfdi_data['cfdi32']['serie']),
                # FOLIO
                self._get_str_value(self._cfdi_data['cfdi32']['folio']),
                # FECHA
                self._cfdi_data['cfdi32']['fecha'],
                # NOCERTIFICADO
                self._cfdi_data['cfdi32']['no_certificado'],
                # SUBTOTAL
                self._cfdi_data['cfdi32']['subtotal'],
                # DESCUENTO
                self._get_numeric_value(self._cfdi_data['cfdi32']['descuento']),
                # TOTAL
                self._cfdi_data['cfdi32']['total'],
                # MONEDA
                self._cfdi_data['cfdi32']['moneda'],
                # TIPOCAMBIO
                self._get_numeric_tipo_cambio_value(self._cfdi_data['cfdi32']['tipo_cambio']),
                # TIPODECOMPROBANTE
                self._cfdi_data['cfdi32']['tipo_comprobante'],
                # METODOPAGO
                self._get_str_value(self._cfdi_data['cfdi32']['metodo_pago']),
                # FORMAPAGO
                self._get_str_value(self._cfdi_data['cfdi32']['forma_pago']),
                # CONDICIONESDEPAGO
                self._get_str_value(self._cfdi_data['cfdi32']['condiciones_pago']),
                # LUGAREXPEDICION
                self._cfdi_data['cfdi32']['lugar_expedicion'],
                # EMISORRFC
                self._cfdi_data['cfdi32']['emisor']['rfc'],
                # EMISORNOMBRE
                self._get_str_value(self._cfdi_data['cfdi32']['emisor']['nombre']),
                # EMISORREGIMENFISCAL
                self._get_emisor_regimen_fiscal(self._cfdi_data['cfdi32']['emisor']['regimen_fiscal']),
                # RECEPTORRFC
                self._cfdi_data['cfdi32']['receptor']['rfc'],
                # RECEPTORNOMBRE
                self._get_str_value(self._cfdi_data['cfdi32']['receptor']['nombre']),
                # RESIDENCIAFISCAL
                "",
                # NUMREGIDTRIB
                "",
                # RECEPTORUSOCFDI
                "",
                # CLAVEPRODSERV
                self._get_concept_value_by_key('clave_prod_serv'),
                # IVATRASLADO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi32']['impuestos'], 'traslados', '002'),
                # IEPSTRASLADO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi32']['impuestos'], 'traslados', '003'),
                # TOTALIMPUESTOSTRASLADOS
                self._get_numeric_value(self._cfdi_data['cfdi32']['impuestos']['total_impuestos_traslados']),
                # ISRRETENIDO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi32']['impuestos'], 'retenciones', '001'),
                # IVARETENIDO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi32']['impuestos'], 'retenciones', '002'),
                # IEPSRETENIDO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi32']['impuestos'], 'retenciones', '003'),
                # TOTALIMPUESTOSRETENIDOS
                self._get_numeric_value(self._cfdi_data['cfdi32']['impuestos']['total_impuestos_retenidos']),
                # TOTALTRASLADOSIMPUESTOSLOCALES
                self._get_implocal10_total_traslados(),
                # TOTALRETENCIONESIMPUESTOSLOCALES
                self._get_implocal10_total_retenciones(),
                # COMPLEMENTOS
                self._get_str_value(self._cfdi_data['cfdi32']['complementos']),
                # UUID
                tfd['uuid'],
                # FECHATIMBRADO
                tfd['fecha_timbrado'],
                # RFCPROVCERTIF
                "",
                # SELLOCFD
                tfd['sello_cfd']
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
            'SELLOCFD']
