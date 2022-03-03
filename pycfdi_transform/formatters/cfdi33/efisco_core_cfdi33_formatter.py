from __future__ import annotations

from pycfdi_transform.formatters.cfdi33.base_cfdi33_formatter import BaseCFDI33Formatter


class EfiscoCoreCFDI33Formatter(BaseCFDI33Formatter):

    def dict_to_columns(self) -> list[list]:
        results = []
        for tfd in self._cfdi_data['tfd11']:
            row = [
                # VERSION
                self._cfdi_data['cfdi33']['version'],
                # SERIE
                self._get_str_value(self._cfdi_data['cfdi33']['serie']),
                # FOLIO
                self._get_str_value(self._cfdi_data['cfdi33']['folio']),
                # FECHA
                self._cfdi_data['cfdi33']['fecha'],
                # NOCERTIFICADO
                self._cfdi_data['cfdi33']['no_certificado'],
                # SUBTOTAL
                self._cfdi_data['cfdi33']['subtotal'],
                # DESCUENTO
                self._get_numeric_value(self._cfdi_data['cfdi33']['descuento']),
                # TOTAL
                self._cfdi_data['cfdi33']['total'],
                # MONEDA
                self._cfdi_data['cfdi33']['moneda'],
                # TIPOCAMBIO
                self._get_numeric_tipo_cambio_value(self._cfdi_data['cfdi33']['tipo_cambio']),
                # TIPODECOMPROBANTE
                self._cfdi_data['cfdi33']['tipo_comprobante'],
                # METODOPAGO
                self._get_str_value(self._cfdi_data['cfdi33']['metodo_pago']),
                # FORMAPAGO
                self._get_str_value(self._cfdi_data['cfdi33']['forma_pago']),
                # CONDICIONESDEPAGO
                self._get_str_value(self._cfdi_data['cfdi33']['condiciones_pago']),
                # LUGAREXPEDICION
                self._cfdi_data['cfdi33']['lugar_expedicion'],
                # EMISORRFC
                self._cfdi_data['cfdi33']['emisor']['rfc'],
                # EMISORNOMBRE
                self._get_str_value(self._cfdi_data['cfdi33']['emisor']['nombre']),
                # EMISORREGIMENFISCAL
                self._cfdi_data['cfdi33']['emisor']['regimen_fiscal'],
                # RECEPTORRFC
                self._cfdi_data['cfdi33']['receptor']['rfc'],
                # RECEPTORNOMBRE
                self._get_str_value(self._cfdi_data['cfdi33']['receptor']['nombre']),
                # RESIDENCIAFISCAL                
                self._get_str_value(self._cfdi_data['cfdi33']['receptor']['residencia_fiscal']),
                # NUMREGIDTRIB
                self._get_str_value(self._cfdi_data['cfdi33']['receptor']['num_reg_id_trib']),
                # RECEPTORUSOCFDI
                self._cfdi_data['cfdi33']['receptor']['uso_cfdi'],
                # C_DESCRIPCION
                self._get_concept_value_by_key('descripcion'),
                # IVATRASLADO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi33']['impuestos'], 'traslados', '002'),
                # IEPSTRASLADO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi33']['impuestos'], 'traslados', '003'),
                # TOTALIMPUESTOSTRASLADOS
                self._get_numeric_value(self._cfdi_data['cfdi33']['impuestos']['total_impuestos_traslados']),
                # ISRRETENIDO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi33']['impuestos'], 'retenciones', '001'),
                # IVARETENIDO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi33']['impuestos'], 'retenciones', '002'),
                # IEPSRETENIDO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi33']['impuestos'], 'retenciones', '003'),
                # TOTALIMPUESTOSRETENIDOS
                self._get_numeric_value(self._cfdi_data['cfdi33']['impuestos']['total_impuestos_retenidos']),
                # TOTALTRASLADOSIMPUESTOSLOCALES
                self._get_implocal10_total_traslados(),
                # TOTALRETENCIONESIMPUESTOSLOCALES
                self._get_implocal10_total_retenciones(),
                # COMPLEMENTOS
                self._get_str_value(self._cfdi_data['cfdi33']['complementos']),
                # UUID                
                tfd['uuid'],
                # FECHATIMBRADO
                tfd['fecha_timbrado'],
                # RFCPROVCERTIF
                tfd['rfc_prov_cert'],
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
