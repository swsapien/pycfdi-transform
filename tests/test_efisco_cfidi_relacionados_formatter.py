from pycfdi_transform import CFDI33SAXHandler
from pycfdi_transform import CFDI40SAXHandler
from pycfdi_transform.formatters.cfdis_relacionados.efisco_cfdis_relacionados_formatter import EfiscoCfdisRelacionadosFormatter
import unittest
import time


class TestEfiscoCfdiRelacionadosFormatter(unittest.TestCase):

    def test_columns_names_related_cfdi(self):
        formatter = EfiscoCfdisRelacionadosFormatter({'cfdi33': {}})
        columns_expected = [
            "UUID",
            "TIPORELACION",
            "IDDOCUMENTO"
        ]
        self.assertListEqual(columns_expected, formatter.get_columns_names())

    def test_formatter_related_cfdi_can_format_ok(self):
        sax_handler = CFDI33SAXHandler().use_related_cfdis()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi33/cfdi33_related_cfdis.xml')
        formatter = EfiscoCfdisRelacionadosFormatter(cfdi_data)
        self.assertTrue(formatter.can_format())

    def test_formatter_related_cfdi_cfdi33(self):
        start = time.time()
        sax_handler = CFDI33SAXHandler().use_related_cfdis()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi33/cfdi33_related_cfdis.xml')
        expected_columns = [['48563590-F30B-4EFF-AE15-B2A900000000','04','1D0EA245-9147-492F-83EF-A7DD8E5D7094'],
                            ['48563590-F30B-4EFF-AE15-B2A900000000','04','1D0EA245-9147-492F-83EF-A7DD8E5D7095'],
                            ['48563590-F30B-4EFF-AE15-B2A900000000','02','1D0EA245-9147-492F-83EF-A7DD8E5D7096']
                            ]
        formatter = EfiscoCfdisRelacionadosFormatter(cfdi_data)
        result_columns = formatter.dict_to_columns()
        print(result_columns)
        end_time = time.time() - start
        self.assertListEqual(expected_columns, result_columns)
        self.assertLess(end_time, 0.01)

    def test_formatter_related_cfdi_40(self):
        start = time.time()
        sax_handler = CFDI40SAXHandler().use_related_cfdis()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi40/cfdi40_related_cfdis.xml')
        expected_columns = [
            ['9D81C696-0401-4F85-B703-6E0D3AFD6056', '08', 'CAAB1AFA-AC0D-BDAC-5CCF-AAD448CAFC08'],
            ['9D81C696-0401-4F85-B703-6E0D3AFD6056', '08', '2EB04CE0-F1ED-3EBC-B796-38FFE2DFEBEC'],
            ['9D81C696-0401-4F85-B703-6E0D3AFD6056', '08', '7FC2BBFD-E7E2-2FAA-39C7-D1DC6CF3FEEE'],
            ['9D81C696-0401-4F85-B703-6E0D3AFD6056', '08', 'E06CCA24-CC8E-2AD9-906B-38BACCB5CE2D']
        ]
        formatter = EfiscoCfdisRelacionadosFormatter(cfdi_data)
        result_columns = formatter.dict_to_columns()
        print(result_columns)
        end_time = time.time() - start
        self.assertListEqual(expected_columns, result_columns)
        self.assertLess(end_time, 0.01)
