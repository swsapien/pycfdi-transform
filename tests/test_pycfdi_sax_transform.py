import unittest
import os
import io
import pycfdi_transform as ct


class TestPycfdiSaxTransform(unittest.TestCase):

    def test_cfdi33_01_from_file_ok(self):
        path_xml = "./tests/Resources/cfdi33_01.xml"
        transformer = ct.TSaxCfdi33()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==1)
        self.assertTrue(len(result_columns[0])==37)
    
if __name__ == '__main__':
    unittest.main()
