from __future__ import annotations
import logging
from pycfdi_transform.helpers.string_helper import StringHelper
from pycfdi_transform.sax.pagos20.base_handler import BaseHandler
from lxml import etree

class Pagos20SAXHandler(BaseHandler):
    def __init__(self, empty_char = '', safe_numerics = False,esc_delimiters:str = "") -> Pagos20SAXHandler:
        super().__init__(empty_char, safe_numerics,esc_delimiters)
        self._logger = logging.getLogger('Pagos20SAXHandler')
    
    def transform_from_string(self, xml_str:str) -> dict:
        try:
            xml_parser = etree.XMLParser(encoding='utf-8', recover=True)
            tree = etree.XML(xml_str, parser=xml_parser)
            context = etree.iterwalk(tree, events=("start",))
            self.__handle_events(context)
            return self._data
        except Exception as ex:
            self._logger.exception(f'Caugth Exception at tranforming xml string.')
            raise ex
    
    def __handle_events(self, context:etree.iterwalk) -> None:
        for action, elem in context:
            if action == 'start':
                if elem.tag == '{http://www.sat.gob.mx/Pagos20}Pagos':
                    self.__transform_pagos(elem)
                if elem.tag == '{http://www.sat.gob.mx/Pagos20}Totales':
                    self.__transform_totales(elem)
                if elem.tag == '{http://www.sat.gob.mx/Pagos20}Pago':
                    self.__transform_pago(elem)

    
    def __transform_pagos(self, element:etree._Element) -> None:
        if not 'Version' in element.attrib or element.attrib['Version'] != '2.0':
            raise ValueError('Incorrect type of Pagos, this handler only support Pagos version 2.0')
        self._data['version'] = element.attrib.get('Version')
    
    def __transform_totales(self, element: etree._Element) -> None:
        totales = {
            'total_retenciones_iva': element.attrib.get('TotalRetencionesIVA', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_retenciones_isr': element.attrib.get('TotalRetencionesISR', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_retenciones_ieps': element.attrib.get('TotalRetencionesIEPS', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_traslados_base_iva_16': element.attrib.get('TotalTrasladosBaseIVA16', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_traslados_impuesto_iva_16': element.attrib.get('TotalTrasladosImpuestoIVA16', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_traslados_base_iva_8': element.attrib.get('TotalTrasladosBaseIVA8', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_traslados_impuesto_iva_8': element.attrib.get('TotalTrasladosImpuestoIVA8', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_traslados_base_iva_0': element.attrib.get('TotalTrasladosBaseIVA0', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_traslados_impuesto_iva_0': element.attrib.get('TotalTrasladosImpuestoIVA0', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_traslados_base_iva_exento': element.attrib.get('TotalTrasladosBaseIVAExento', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'monto_total_pagos': element.attrib.get('MontoTotalPagos', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
        }
        self._data['totales'] = totales
        
    def __transform_pago(self, element:etree._Element) -> None:
        pago = {
            'fecha_pago': element.attrib.get('FechaPago'),
            'forma_de_pago_p': element.attrib.get('FormaDePagoP'),
            'moneda_p': element.attrib.get('MonedaP'),
            'tipo_cambio_p': element.attrib.get('TipoCambioP', StringHelper.DEFAULT_SAFE_NUMBER_ONE if self._config['safe_numerics'] else self._config['empty_char']),
            'monto': element.attrib.get('Monto'),
            'num_operacion': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('NumOperacion', self._config['empty_char'])),
            'rfc_emisor_cta_ord': element.attrib.get('RfcEmisorCtaOrd', self._config['empty_char']),
            'nom_banco_ord_ext': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('NomBancoOrdExt', self._config['empty_char'])),
            'cta_ordenante': element.attrib.get('CtaOrdenante', self._config['empty_char']),
            'rfc_emisor_cta_ben': element.attrib.get('RfcEmisorCtaBen', self._config['empty_char']),
            'cta_beneficiario': element.attrib.get('CtaBeneficiario', self._config['empty_char']),
            'tipo_cad_pago': element.attrib.get('TipoCadPago', self._config['empty_char']),
            'cert_pago': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('CertPago', self._config['empty_char'])),
            'cad_pago': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('CadPago', self._config['empty_char'])),
            'sello_pago': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('SelloPago', self._config['empty_char'])),
            'docto_relacionado': [],
            'impuestos_p': []
        }
        for child in element.getchildren():
            if child.tag == '{http://www.sat.gob.mx/Pagos20}DoctoRelacionado':
                pago['docto_relacionado'].append(self.__transform_docto_relacionado(child))
            elif child.tag == '{http://www.sat.gob.mx/Pagos20}ImpuestosP':
                pago['impuestos_p'].append(self.__transform_impuestos_p(child))
        self._data['pago'].append(pago)
        
    def __transform_docto_relacionado(self, element: etree._Element) -> object:
        docto_relacionado = {
            'id_documento': element.attrib.get('IdDocumento'),
            'serie': StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('Serie', self._config['empty_char'])),
            'folio': StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('Folio', self._config['empty_char'])),
            'moneda_dr': element.attrib.get('MonedaDR'),
            'equivalencia_dr': element.attrib.get('EquivalenciaDR', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'num_parcialidad': element.attrib.get('NumParcialidad', self._config['empty_char']),
            'imp_saldo_ant': element.attrib.get('ImpSaldoAnt', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'imp_pagado': element.attrib.get('ImpPagado', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'imp_saldo_insoluto': element.attrib.get('ImpSaldoInsoluto', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'objecto_imp_dr': element.attrib.get('ObjetoImpDR'),
            'impuestos_dr': []
        }
        for child in element.getchildren():
            if child.tag == '{http://www.sat.gob.mx/Pagos20}ImpuestosDR':
                docto_relacionado['impuestos_dr'].append(self.__transform_impuestos_dr(child))

        return docto_relacionado

    def __transform_impuestos_dr(self, element:etree._Element) -> object:
        impuestos = {
            'retenciones_dr': [],
            'traslados_dr': []
        }
        for child in element.getchildren():
            if child.tag == '{http://www.sat.gob.mx/Pagos20}RetencionesDR':
                impuestos['retenciones_dr'] = self.__transform_impuestos_dr_child(child.getchildren())
            elif child.tag == '{http://www.sat.gob.mx/Pagos20}TrasladosDR':
                impuestos['traslados_dr'] = self.__transform_impuestos_dr_child(child.getchildren())
        return impuestos


    def __transform_impuestos_p(self, element:etree._Element) -> object:
        impuestos = {
            'retenciones_p': [],
            'traslados_p': []
        }
        for child in element.getchildren():
            if child.tag == '{http://www.sat.gob.mx/Pagos20}RetencionesP':
                impuestos['retenciones_p'] = self.__transform_retencion_p(child.getchildren())
            elif child.tag == '{http://www.sat.gob.mx/Pagos20}TrasladosP':
                impuestos['traslados_p'] = self.__transform_traslado_p(child.getchildren())
        return impuestos

    def __transform_retencion_p(self, list_elements:list[etree._Element]) -> list[object]:
        retenciones = []
        for element in list_elements:
            retenciones.append(
                {
                    'impuesto_p': element.attrib.get('ImpuestoP'),
                    'importe_p': element.attrib.get('ImporteP')
                }
            )
        return retenciones
    
    def __transform_traslado_p(self, list_elements:list[etree._Element]) -> list[object]:
        traslados = []
        for element in list_elements:
            traslados.append(
                {
                    'base_p': element.attrib.get('BaseP'),
                    'impuesto_p': element.attrib.get('ImpuestoP'),
                    'tipo_factor_p': element.attrib.get('TipoFactorP'),
                    'tasa_o_cuota_p': element.attrib.get('TasaOCuotaP', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
                    'importe_p': element.attrib.get('ImporteP', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])

                }
            )
        return traslados
    
    
    def __transform_impuestos_dr_child(self, list_elements:list[etree._Element]) -> list[object]:
        items = []
        for element in list_elements:
            items.append(
                {
                    'base_dr': element.attrib.get('BaseDR'),
                    'impuesto_dr': element.attrib.get('ImpuestoDR'),
                    'tipo_factor_dr': element.attrib.get('TipoFactorDR'),
                    'tasa_o_cuota_dr': element.attrib.get('TasaOCuotaDR', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
                    'importe_dr': element.attrib.get('ImporteDR', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
                }
            )
        return items