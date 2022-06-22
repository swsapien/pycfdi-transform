from __future__ import annotations
import logging
from pycfdi_transform.helpers.string_helper import StringHelper
from pycfdi_transform.sax.terceros11.base_handler import BaseHandler
from lxml import etree

"""This handler is used internally in concepts node on use_concepts_cfdi32 and use_concepts_cfdi33

    Returns:
        Terceros11SAXHandler: Instance of configured class.
    """
class Terceros11SAXHandler(BaseHandler):
    def __init__(self, empty_char='', safe_numerics=False, esc_delimiters: str = "") -> Terceros11SAXHandler:
        super().__init__(empty_char, safe_numerics, esc_delimiters)
        self._logger = logging.getLogger('Terceros11SAXHandler')

    def transform_from_string(self, xml_str: str) -> dict:
        try:
            xml_parser = etree.XMLParser(encoding='utf-8', recover=True)
            tree = etree.XML(xml_str, parser=xml_parser)
            context = etree.iterwalk(tree, events=("start",))
            self.__handle_events(context)
            return self._data
        except Exception as ex:
            self._logger.exception(f'Caugth Exception at tranforming xml string.')
            raise ex

    def __handle_events(self, context: etree.iterwalk) -> None:
        for action, elem in context:
            if action == 'start':
                if elem.tag == '{http://www.sat.gob.mx/terceros}PorCuentadeTerceros':
                    self.__transform_por_cuenta_terceros(elem)
                if elem.tag == '{http://www.sat.gob.mx/terceros}InformacionFiscalTercero':
                    self.__transform_informacion_fiscal_tercero(elem)
                if elem.tag == '{http://www.sat.gob.mx/terceros}InformacionAduanera':
                    self.__transform_informacion_aduanera(elem)
                if elem.tag == '{http://www.sat.gob.mx/terceros}CuentaPredial':
                    self.__transform_cuenta_predial(elem)
                if elem.tag == '{http://www.sat.gob.mx/terceros}Retencion':
                    self.__transform_retencion(elem)
                if elem.tag == '{http://www.sat.gob.mx/terceros}Traslado':
                    self.__transform_traslado(elem)

    def __transform_por_cuenta_terceros(self, element: etree._Element) -> None:
        if not 'version' in element.attrib or element.attrib['version'] != '1.1':
            raise ValueError('Incorrect type of Pagos, this handler only support PorCuentadeTerceros version 1.1')
        self._data['version'] = element.attrib.get('version')
        self._data['rfc'] = element.attrib.get('rfc')
        self._data['nombre'] = element.attrib.get('nombre', self._config['empty_char'])

    def __transform_informacion_fiscal_tercero(self, element: etree._Element) -> None:
        self._data['informacionFiscal'] = {
            'calle': StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('calle')),
            'noExterior': element.attrib.get('noExterior', self._config['empty_char']),
            'noInterior': element.attrib.get('noInterior', self._config['empty_char']),
            'colonia': element.attrib.get('colonia', self._config['empty_char']),
            'localidad': element.attrib.get('localidad', self._config['empty_char']),
            'referencia': StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('referencia')),
            'municipio': element.attrib.get('municipio', self._config['empty_char']),
            'estado': element.attrib.get('estado', self._config['empty_char']),
            'pais': element.attrib.get('pais', self._config['empty_char']),
            'codigoPostal': element.attrib.get('codigoPostal', self._config['empty_char']),
        }

    def __transform_informacion_aduanera(self, element: etree._Element) -> None:
        self._data['informacionAduanera'] = {
            'numero': element.attrib.get('numero', self._config['empty_char']),
            'fecha': element.attrib.get('fecha', self._config['empty_char']),
            'aduana': element.attrib.get('aduana', self._config['empty_char']),
        }

    def __transform_cuenta_predial(self, element: etree._Element) -> None:
        self._data['cuentaPredial'] = {
            'numero': element.attrib.get('numero', self._config['empty_char']),
        }

    def __transform_retencion(self, element: etree._Element) -> None:
        self._data['impuestos']['retenciones'].append({
            'impuesto': element.attrib.get('impuesto', self._config['empty_char']),
            'importe': element.attrib.get('importe', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
        })

    def __transform_traslado(self, element: etree._Element) -> None:
        self._data['impuestos']['traslados'].append({
            'impuesto': element.attrib.get('impuesto', self._config['empty_char']),
            'tasa': element.attrib.get('tasa', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'importe': element.attrib.get('importe', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
        })