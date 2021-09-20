from __future__ import annotations
import logging
from lxml import etree
from pycfdi_transform.v2.sax.tfd.base_handler import BaseHandler

class TFDSAXHandler(BaseHandler):
    def __init__(self) -> TFDSAXHandler:
        super().__init__()
        self._logger = logging.getLogger('TFDSAXHandler')
    
    def transform_from_string(self, xml_str:str) -> object:
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
                if elem.tag == '{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital':
                    self.__transform_tfd(elem)
                else:
                    context.skip_subtree()
    
    def __transform_tfd(self, element:etree._Element) -> None:
        self._data['uuid'] = str(element.attrib['UUID']).upper()
        self._data['fecha_timbrado'] = element.attrib['FechaTimbrado']
        self._data['rfc_prov_cert'] = element.attrib['RfcProvCertif']
        self._data['sello_cfd'] = element.attrib['SelloCFD']