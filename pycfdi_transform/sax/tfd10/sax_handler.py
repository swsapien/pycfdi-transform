from __future__ import annotations
import logging
from lxml import etree
from pycfdi_transform.sax.tfd10.base_handler import BaseHandler
from pycfdi_transform.helpers.string_helper import StringHelper


class TFD10SAXHandler(BaseHandler):
    def __init__(self, empty_char='', safe_numerics=False, esc_delimiters: str = "") -> TFD10SAXHandler:
        super().__init__(empty_char, safe_numerics, esc_delimiters)
        self._logger = logging.getLogger('TFD10SAXHandler')

    def transform_from_string(self, xml_str: str) -> dict:
        try:
            xml_parser = etree.XMLParser(encoding='utf-8', recover=True)
            tree = etree.XML(xml_str, parser=xml_parser)
            context = etree.iterwalk(tree, events=("start", "end"))
            self.__handle_events(context)
            return self._data
        except Exception as ex:
            self._logger.exception(f'Caugth Exception at tranforming xml string.')
            raise ex

    def __handle_events(self, context: etree.iterwalk) -> None:
        for action, elem in context:
            if action == 'start':
                if elem.tag == '{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital':
                    self.__transform_tfd(elem)
                else:
                    context.skip_subtree()

    def __transform_tfd(self, element: etree._Element) -> None:
        if not 'version' in element.attrib or element.attrib['version'] != '1.0':
            raise ValueError('Incorrect type of TFD, this handler only support TFD version 1.0')
        self._data['version'] = element.attrib.get('version')
        self._data['no_certificado_sat'] = element.attrib.get('noCertificadoSAT')
        self._data['uuid'] = str(element.attrib.get('UUID')).upper()
        self._data['fecha_timbrado'] = element.attrib.get('FechaTimbrado')
        self._data['sello_cfd'] = StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('selloCFD'))
        self._data['sello_sat'] = StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('selloSAT'))
