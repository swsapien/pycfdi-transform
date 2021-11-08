from __future__ import annotations
from pycfdi_transform.sax.implocal10.base_handler import BaseHandler
from lxml import etree
import logging

class ImpLocal10SAXHandler(BaseHandler):
    def __init__(self, empty_char='', safe_numerics=False,esc_delimiters:str = "") -> ImpLocal10SAXHandler:
        super().__init__(empty_char, safe_numerics,esc_delimiters)
        self._logger = logging.getLogger('ImpLocal10SAXHandler')
    
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
                if elem.tag == '{http://www.sat.gob.mx/implocal}ImpuestosLocales':
                    self.__transform_implocal(elem)
                else:
                    context.skip_subtree()
    def __transform_implocal(self, element:etree._Element):
        if not 'version' in element.attrib or element.attrib['version'] != '1.0':
            raise ValueError('Incorrect type of ImpLocal, this handler only support ImpLocal version 1.0')
        self._data['total_traslados_impuestos_locales'] = element.attrib.get('TotaldeTraslados')
        self._data['total_retenciones_impuestos_locales'] = element.attrib.get('TotaldeRetenciones')