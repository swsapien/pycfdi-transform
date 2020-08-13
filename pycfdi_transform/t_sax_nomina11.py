import os
from pycfdi_transform.__t_sax_base__ import TSaxBase
from pycfdi_transform.sax_handlers.nomina11_handler import Nomina11Handler


class TSaxNomina11(TSaxBase):
    def __init__(self):
        super().__init__()

    def to_columns_from_file(self, xml_file):
        handler = Nomina11Handler()
        self.parse(handler, xml_file)
        return handler.get_result()
