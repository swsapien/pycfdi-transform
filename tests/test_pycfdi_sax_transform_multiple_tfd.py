import unittest
import os
import io
import pycfdi_transform as ct



class TestPycfdiSaxTransformMultipleTFD(unittest.TestCase):

    def test_sax_cfdi33(self):
        path_xml = './tests/Resources/cfdi33_nomina_multiple_tfd.xml'
        transformer = ct.TSaxCfdi33()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 2)
        self.assertTrue(len(result_columns[0]) == 38)
        self.assertTrue(result_columns[0][33] == '8936cb73-2a13-4230-9e01-6e9b0edd7cde'.upper())
        self.assertTrue(result_columns[1][33] == 'a89a5f34-7725-46fa-8d25-01d4862c5cd2'.upper())