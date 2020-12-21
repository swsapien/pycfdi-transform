import os
from pycfdi_transform.__t_sax_base__ import TSaxBase
from pycfdi_transform.sax.cfdi32_handler import CFDI32Handler


class TSaxCfdi32(TSaxBase):
    def __init__(self):
        super().__init__()

    def to_columns_from_file(self, xml_file):
        if ('.xml' in xml_file):
            try:
                handler = CFDI32Handler()
                self.parse_file(handler, xml_file)
                return handler.get_result()
            except Exception as ex:
                print(ex)
                return

    def to_columns_from_string(self, string_xml):
        try:
            handler = CFDI32Handler()
            self.parse_string(handler, string_xml)
            return handler.get_result()
        except Exception as ex:
            print(ex)
            return

    def get_column_names(self):
        return ['VERSION', 'SERIE', 'FOLIO', 'FECHA', 'NOCERTIFICADO', 'SUBTOTAL', 'DESCUENTO', 'TOTAL', 'MONEDA', 'TIPOCAMBIO', 'TIPODECOMPROBANTE', 'METODOPAGO', 'FORMAPAGO', 'CONDICIONESDEPAGO', 'LUGAREXPEDICION', 'EMISORRFC', 'EMISORNOMBRE', 'EMISORREGIMENFISCAL', 'RECEPTORRFC', 'RECEPTORNOMBRE', 'RESIDENCIAFISCAL', 'NUMREGIDTRIB', 'RECEPTORUSOCFDI', 'CLAVEPRODSERV', 'IVATRASLADO', 'IEPSTRASLADO', 'TOTALIMPUESTOSTRASLADOS', 'ISRRETENIDO', 'IVARETENIDO', 'IEPSRETENIDO', 'TOTALIMPUESTOSRETENIDOS', 'TOTALTRASLADOSIMPUESTOSLOCALES', 'TOTALRETENCIONESIMPUESTOSLOCALES', 'COMPLEMENTOS', 'UUID', 'FECHATIMBRADO', 'RFCPROVCERTIF', 'SELLOCFD']
