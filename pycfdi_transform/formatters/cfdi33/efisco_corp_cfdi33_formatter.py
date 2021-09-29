from __future__ import annotations
from pycfdi_transform.formatters.formatter_interface import FormatterInterface
from pycfdi_transform.formatters.base.cfdi33_base_formatter import CFDI33BaseFormatter
from pycfdi_transform.helpers.string_helper import StringHelper

class EfiscoCFDI33Formatter(FormatterInterface,CFDI33BaseFormatter):
    def __init__(self, cfdi_data: dict, empty_char:str = '', safe_numerics:bool = False) -> EfiscoPagos10Formatter:
        super().__init__(cfdi_data,empty_char,safe_numerics)

    def _get_concept_value_by_key(self,key: str)->str:
        if self._cfdi_data['cfdi33']['conceptos'] and len(self._cfdi_data['cfdi33']['conceptos']) > 0 and key in self._cfdi_data['cfdi33']['conceptos'][0]:
            return self._cfdi_data['cfdi33']['conceptos'][0][key]
        else: 
            return self._config["empty_char"]
        
    def base_dict_to_columns(self) -> list[list]:
        results = []
        implocal10 = self._get_implocal10_complement()
        for tdf in self._cfdi_data['tfd11']:
            row = [
                # VERSION
                self._cfdi_data['cfdi33']['version'],
                # SERIE
                self._cfdi_data['cfdi33']['serie'],
                # FOLIO
                self._cfdi_data['cfdi33']['folio'],
                # FECHA
                self._cfdi_data['cfdi33']['fecha'],
                # NOCERTIFICADO
                self._cfdi_data['cfdi33']['no_certificado'],
                # SUBTOTAL
                self._cfdi_data['cfdi33']['subtotal'],
                # DESCUENTO
                self._cfdi_data['cfdi33']['descuento'],
                # TOTAL
                self._cfdi_data['cfdi33']['total'],
                # MONEDA
                self._cfdi_data['cfdi33']['moneda'],
                # TIPOCAMBIO
                self._cfdi_data['cfdi33']['tipo_cambio'],
                # TIPODECOMPROBANTE
                self._cfdi_data['cfdi33']['tipo_comprobante'],
                # METODOPAGO
                self._cfdi_data['cfdi33']['metodo_pago'],
                # FORMAPAGO
                self._cfdi_data['cfdi33']['forma_pago'],
                # CONDICIONESDEPAGO
                self._cfdi_data['cfdi33']['condiciones_pago'],
                # LUGAREXPEDICION
                self._cfdi_data['cfdi33']['lugar_expedicion'],
                # EMISORRFC
                self._cfdi_data['cfdi33']['emisor']['rfc'],
                # EMISORNOMBRE
                self._cfdi_data['cfdi33']['emisor']['nombre'],
                # EMISORREGIMENFISCAL
                self._cfdi_data['cfdi33']['emisor']['regimen_fiscal'],
                # RECEPTORRFC
                self._cfdi_data['cfdi33']['receptor']['rfc'],
                # RECEPTORNOMBRE
                self._cfdi_data['cfdi33']['receptor']['nombre'],
                # RESIDENCIAFISCAL                
                self._cfdi_data['cfdi33']['receptor']['residencia_fiscal'],
                # NUMREGIDTRIB
                self._cfdi_data['cfdi33']['receptor']['num_reg_id_trib'],
                # RECEPTORUSOCFDI
                self._cfdi_data['cfdi33']['receptor']['uso_cfdi'],
                # CLAVEPRODSERV
                self._get_concept_value_by_key('clave_prod_serv'),                    
                # C_DESCRIPCION
                self._get_concept_value_by_key('descripcion'),
                # IVATRASLADO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi33']['impuestos'], 'traslados', '002'),
                # IEPSTRASLADO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi33']['impuestos'], 'traslados', '003'),
                # TOTALIMPUESTOSTRASLADOS
                self._cfdi_data['cfdi33']['impuestos']['total_impuestos_traslados'],
                # ISRRETENIDO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi33']['impuestos'], 'retenciones', '001'),
                # IVARETENIDO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi33']['impuestos'], 'retenciones', '002'),
                # IEPSRETENIDO
                self._get_total_taxes_by_type(self._cfdi_data['cfdi33']['impuestos'], 'retenciones', '003'),
                # TOTALIMPUESTOSRETENIDOS
                self._cfdi_data['cfdi33']['impuestos']['total_impuestos_retenidos'],
                # TOTALTRASLADOSIMPUESTOSLOCALES
                self._get_implocal10_total_traslados(),
                # TOTALRETENCIONESIMPUESTOSLOCALES
                self._get_implocal10_total_retenciones(),
                # COMPLEMENTOS
                self._cfdi_data['cfdi33']['complementos'],
                # UUID                
                tdf['uuid'],
                # FECHATIMBRADO
                tdf['fecha_timbrado'],
                # RFCPROVCERTIF
                tdf['rfc_prov_cert'],
                # SELLOCFD
                tdf['sello_cfd']
            ]
            results.append(row)
        return results
    
    def get_columns_names(self) -> list[str]:
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
            'SELLOCFD']