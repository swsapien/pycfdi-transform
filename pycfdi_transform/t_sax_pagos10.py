import os
from pycfdi_transform.__t_sax_base__ import TSaxBase
from pycfdi_transform.sax_handlers.pagos10_handler import Pagos10Handler


class TSaxPagos10(TSaxBase):
    def __init__(self):
        super().__init__()

    def to_columns_from_file(self, xml_file):
        handler = Pagos10Handler()
        self.parse(handler, xml_file)
        return handler.get_result()

    def get_column_names(self):
        return [
            "VERSION",
            "SERIE",
            "FOLIO",
            "FECHA",
            "NOCERTIFICADO",
            "SUBTOTAL",
            "DESCUENTO",
            "TOTAL",
            "MONEDA",
            "TIPOCAMBIO",
            "TIPODECOMPROBANTE",
            "METODOPAGO",
            "FORMAPAGO",
            "CONDICIONESDEPAGO",
            "LUGAREXPEDICION",
            "EMISORRFC",
            "EMISORNOMBRE",
            "EMISORREGIMENFISCAL",
            "RECEPTORRFC",
            "RECEPTORNOMBRE",
            "RECEPTORUSOCFDI",
            "UUID",
            "FECHATIMBRADO",
            "RFCPROVCERTIF",
            "SELLOCFD",
            "P_IDENTIFICADOR_PAGO",
            "FECHAPAGO",
            "FORMADEPAGOP",
            "MONEDAP",
            "TIPOCAMBIOP",
            "MONTO",
            "NUMOPERACION",
            "RFCEMISORCTAORD",
            "NOMBANCOORDEXT",
            "CTAORDENANTE",
            "RFCEMISORCTABEN",
            "CTABENEFICIARIO",
            "IVATRASLADO",
            "IEPSTRASLADO",
            "TOTALIMPUESTOSTRASLADADOS",
            "ISRRETENCION",
            "IVARETENCION",
            "IEPSRETENCION",
            "TOTALIMPUESTOSRETENIDOS",
            "DR_IDDOCUMENTO",
            "DR_SERIE",
            "DR_FOLIO",
            "DR_MONEDADR",
            "DR_TIPOCAMBIODR",
            "DR_METODODEPAGODR",
            "DR_NUMPARCIALIDAD",
            "DR_IMPSALDOANT",
            "DR_IMPPAGADO",
            "DR_IMPSALDOINSOLUTO"
        ]
