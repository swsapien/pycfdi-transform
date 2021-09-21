from __future__ import annotations

class BaseHandler(object):
    def __init__(self, empty_char = '', safe_numerics = False) -> BaseHandler:
        super().__init__()
        self._data = {
            'uuid': empty_char,
            'fecha_timbrado': empty_char,
            'rfc_prov_cert': empty_char,
            'sello_cfd': empty_char
        }