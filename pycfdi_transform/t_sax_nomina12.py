import os
from pycfdi_transform.__t_sax_base__ import TSaxBase
from pycfdi_transform.sax_handlers.nomina12_handler import Nomina12Handler


class TSaxNomina12(TSaxBase):
    def __init__(self):
        super().__init__()

    def to_columns_from_file(self, xml_file):
        handler = Nomina12Handler()
        self.parse(handler, xml_file)
        return handler.get_result()
