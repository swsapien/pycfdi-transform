from __future__ import annotations

class BaseHandler(object):
    def __init__(self) -> BaseHandler:
        super().__init__()
        self._data = {
            'uuid': '',
            'fecha_timbrado': '',
            'rfc_prov_cert': '',
            'sello_cfd': ''
        }