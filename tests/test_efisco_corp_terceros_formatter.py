import os

from pycfdi_transform import CFDI33SAXHandler
from pycfdi_transform import CFDI40SAXHandler
from pycfdi_transform.formatters.efisco_corp_terceros_formatter import EfiscoCorpTercerosFormatter
import unittest
import time

class TestEfiscoCorpTercerosFormatter(unittest.TestCase):

    def test_columns_names_concepts(self):
        formatter = EfiscoCorpTercerosFormatter({'cfdi33': {}})
        columns_expected = [
            "VERSION",
            "UUID",
            "FECHATIMBRADO",
            "TERCERONOMBRE",
            "TERCERORFC"
        ]
        self.assertListEqual(columns_expected, formatter.get_columns_names())

    def test_formatter_concepts_cfdi33_terceros(self):
        start = time.time()
        sax_handler = CFDI33SAXHandler().use_concepts_cfdi33()
        cfdi_data = sax_handler.transform_from_file((os.path.dirname(__file__) + '/Resources/terceros/terceros11_33.xml'))
        expected_columns = [
            ['3.3', '87542154-C64A-1AB9-AE81-0000000000', '2020-06-05T08:35:27', '', 'DCM000125IY6']
        ]

        formatter = EfiscoCorpTercerosFormatter(cfdi_data)
        result_columns = formatter.dict_to_columns()
        print(result_columns)
        end_time = time.time() - start
        self.assertListEqual(expected_columns, result_columns)
        self.assertLess(end_time, 0.01)

    def test_formatter_concepts_cfdi_40_terceros(self):
        sax_handler = CFDI40SAXHandler().use_concepts_cfdi40()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/terceros/terceros_40.xml')
        formatter = EfiscoCorpTercerosFormatter(cfdi_data)
        result_columns = formatter.dict_to_columns()
        expected_columns = [
            ['4.0',  'D69E0C63-8F17-4FB3-9838-D834FD901474', '2022-02-09T01:22:19', 'ADRIANA JUAREZ FERNANDEZ', 'JUFA7608212V6']
        ]
        self.assertListEqual(expected_columns, result_columns)
