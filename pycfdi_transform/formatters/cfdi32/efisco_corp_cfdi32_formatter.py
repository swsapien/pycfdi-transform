from __future__ import annotations
from pycfdi_transform.formatters.formatter_interface import FormatterInterface
from pycfdi_transform.helpers.string_helper import StringHelper

class EfiscoCorpCFDI32Formatter(FormatterInterface):
    def __init__(self, cfdi_data: dict, empty_char:str = '', safe_numerics:bool = False) -> EfiscoCorpCFDI32Formatter:
        super().__init__(cfdi_data,empty_char,safe_numerics)
        assert 'cfdi32' in self._cfdi_data, 'Este formatter únicamente soporta datos de cfdi32.'
        self._config = {
            'empty_char': empty_char,
            'safe_numerics': safe_numerics
        }
        self._errors = []

    @staticmethod
    def _get_total_taxes_by_type(taxes:list, tax_classification:str, tax_type:str) -> str:
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

    def _get_concept_value_by_key(self,key: str)->str:
        if self._cfdi_data['cfdi32']['conceptos'] and len(self._cfdi_data['cfdi32']['conceptos']) > 0 and key in self._cfdi_data['cfdi32']['conceptos'][0]:
            return self._cfdi_data['cfdi32']['conceptos'][0][key]
        else: 
            return self._config["empty_char"]

    def can_format(self) -> bool:
        if not 'tfd10' in self._cfdi_data or len(self._cfdi_data['tfd10']) == 0:
            self._errors.append('Not tfd10 in data.')
        return len(self._errors) == 0
    
    def get_errors(self) -> str:
        return '|'.join(self._errors)
        
    def dict_to_columns(self) -> list[list]:
        results = []
        for tdf in self._cfdi_data['tfd10']:
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
                self._cfdi_data['cfdi32']['emisor']['regimen_fiscal'],
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
                # C_DESCRIPCION
                self._get_concept_value_by_key('descripcion'),
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
                tdf['uuid'],
                # FECHATIMBRADO
                tdf['fecha_timbrado'],
                # RFCPROVCERTIF
                "",
                # SELLOCFD
                tdf['sello_cfd']
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
            'SELLOCFD']