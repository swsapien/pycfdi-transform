from __future__ import annotations
import logging
from pycfdi_transform.helpers.string_helper import StringHelper
from pycfdi_transform.sax.pagos10.base_handler import BaseHandler
from lxml import etree

class Pagos10SAXHandler(BaseHandler):
    def __init__(self, empty_char = '', safe_numerics = False,esc_delimiters:str = "") -> Pagos10SAXHandler:
        super().__init__(empty_char, safe_numerics,esc_delimiters)
        self._logger = logging.getLogger('Pagos10SAXHandler')
    
    def transform_from_string(self, xml_str:str) -> dict:
        try:
            xml_parser = etree.XMLParser(encoding='utf-8', recover=True)
            tree = etree.XML(xml_str, parser=xml_parser)
            context = etree.iterwalk(tree, events=("start", "end"))
            self.__handle_events(context)
            return self._data
        except Exception as ex:
            self._logger.exception(f'Caugth Exception at tranforming xml string.')
            raise ex
    
    def __handle_events(self, context:etree.iterwalk) -> None:
        for action, elem in context:
            if action == 'start':
                if elem.tag == '{http://www.sat.gob.mx/Pagos}Pagos':
                    self.__transform_pagos(elem)
            elif action == 'end':
                if elem.tag == '{http://www.sat.gob.mx/Pagos}Pago':
                    self.__transform_pago(elem)

    
    def __transform_pagos(self, element:etree._Element) -> None:
        if not 'Version' in element.attrib or element.attrib['Version'] != '1.0':
            raise ValueError('Incorrect type of Pagos, this handler only support Pagos version 1.0')
        self._data['version'] = element.attrib.get('Version')
    
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
            'impuestos': []
        }
        for child in element.getchildren():
            if child.tag == '{http://www.sat.gob.mx/Pagos}DoctoRelacionado':
                pago['docto_relacionado'].append(
                    {
                        'id_documento': child.attrib.get('IdDocumento'),
                        'serie': StringHelper.compact_string(self._config['esc_delimiters'],child.attrib.get('Serie', self._config['empty_char'])),
                        'folio': StringHelper.compact_string(self._config['esc_delimiters'],child.attrib.get('Folio', self._config['empty_char'])),
                        'moneda_dr': child.attrib.get('MonedaDR'),
                        'tipo_cambio_dr': child.attrib.get('TipoCambioP', StringHelper.DEFAULT_SAFE_NUMBER_ONE if self._config['safe_numerics'] else self._config['empty_char']),
                        'metodo_de_pago_dr': child.attrib.get('MetodoDePagoDR'),
                        'num_parcialidad': child.attrib.get('NumParcialidad', self._config['empty_char']),
                        'imp_saldo_ant': child.attrib.get('ImpSaldoAnt', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
                        'imp_pagado': child.attrib.get('ImpPagado', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
                        'imp_saldo_insoluto': child.attrib.get('ImpSaldoInsoluto', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
                    }
                )
            elif child.tag == '{http://www.sat.gob.mx/Pagos}Impuestos':
                pago['impuestos'].append(self.__transform_impuestos(child))
        self._data['pago'].append(pago)

    def __transform_impuestos(self, element:etree._Element) -> object:
        impuestos = {
            'retenciones': [],
            'traslados': [],
            'total_impuestos_retenidos': element.attrib.get('TotalImpuestosRetenidos', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_impuestos_trasladados': element.attrib.get('TotalImpuestosTrasladados', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
        }
        for child in element.getchildren():
            if child.tag == '{http://www.sat.gob.mx/Pagos}Retenciones':
                impuestos['retenciones'] = self.__transform_retencion(child.getchildren())
            elif child.tag == '{http://www.sat.gob.mx/Pagos}Traslados':
                impuestos['traslados'] = self.__transform_traslado(child.getchildren())
        return impuestos

    def __transform_retencion(self, list_elements:list[etree._Element]) -> list[object]:
        retenciones = []
        for element in list_elements:
            retenciones.append(
                {
                    'impuesto': element.attrib.get('Impuesto'),
                    'importe': element.attrib.get('Importe')
                }
            )
        return retenciones
    
    def __transform_traslado(self, list_elements:list[etree._Element]) -> list[object]:
        traslados = []
        for element in list_elements:
            traslados.append(
                {
                    'impuesto': element.attrib.get('Impuesto'),
                    'tipo_factor': element.attrib.get('TipoFactor'),
                    'tasa_o_cuota': element.attrib.get('TasaOCuota'),
                    'importe': element.attrib.get('Importe')
                }
            )
        return traslados