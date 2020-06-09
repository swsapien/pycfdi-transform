import unittest
import os
import io
import pycfdi_transform as ct

class TestReportGenerator(unittest.TestCase):
    def test_cfdi33_01_from_file_ok(self):
        path_xml = "./tests/Resources/cfdi33_01.xml"
        transformer = ct.TCfdi33()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==1)
        self.assertTrue(len(result_columns[0])==37)
    
    def test_cfdi33_01_from_bytes_ok(self):
        path_xml = "./tests/Resources/cfdi33_01.xml"
        xml_bytes = None
        with io.open(path_xml, 'r', encoding='utf8') as f:
            xml_bytes = f.read()
        xml_bytes = bytes(bytearray(xml_bytes, encoding= 'utf-8'))
        transformer = ct.TCfdi33()
        result_columns = transformer.to_columns_from_bytes(xml_bytes)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==1)
        self.assertTrue(len(result_columns[0])==37)
    
    def test_cfdi33_get_column_names_ok(self):
        transformer = ct.TCfdi33()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)        
        self.assertTrue(len(result_columns)==37)
    
    def test_pago10_01_from_file_ok(self):
        path_xml = "./tests/Resources/pago10_01.xml"
        transformer = ct.TPago10()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)       
        self.assertTrue(len(result_columns)==1)
        self.assertTrue(len(result_columns[0])==54)
    
    def test_pago10_01_from_bytes_ok(self):
        path_xml = "./tests/Resources/pago10_01.xml"
        xml_bytes = None
        with io.open(path_xml, 'r', encoding='utf8') as f:
            xml_bytes = f.read()
        xml_bytes = bytes(bytearray(xml_bytes, encoding= 'utf-8'))
        transformer = ct.TPago10()
        result_columns = transformer.to_columns_from_bytes(xml_bytes)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==1)
        self.assertTrue(len(result_columns[0])==54)

    def test_pago10_get_column_names_ok(self):
        transformer = ct.TPago10()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==54)
    
    def test_nomina12_01_from_file_ok(self):
        path_xml = "./tests/Resources/nomina12_01.xml"
        transformer = ct.TNomina12()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertTrue(len(result_columns) == 4)
        self.assertTrue(len(result_columns[0])==67)
    
    def test_nomina12_01_from_bytes_ok(self):
        path_xml = "./tests/Resources/nomina12_01.xml"
        xml_bytes = None
        with io.open(path_xml, 'r', encoding='utf8') as f:
            xml_bytes = f.read()
        xml_bytes = bytes(bytearray(xml_bytes, encoding= 'utf-8'))
        transformer = ct.TNomina12()
        result_columns = transformer.to_columns_from_bytes(xml_bytes)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 4)
        self.assertTrue(len(result_columns[0])==67)

    def test_nomina12_get_column_names_ok(self):
        transformer = ct.TNomina12()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==67)
    
    def test_cfdi32_01_from_file_ok(self):
        path_xml = "./tests/Resources/cfdi32_01.xml"
        transformer = ct.TCfdi32()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==1)
        self.assertTrue(len(result_columns[0])==37)
    
    def test_cfdi32_01_from_bytes_ok(self):
        path_xml = "./tests/Resources/cfdi32_01.xml"
        xml_bytes = None
        with io.open(path_xml, 'r', encoding='utf8') as f:
            xml_bytes = f.read()
        xml_bytes = bytes(bytearray(xml_bytes, encoding= 'utf-8'))
        transformer = ct.TCfdi32()
        result_columns = transformer.to_columns_from_bytes(xml_bytes)        
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==1)
        self.assertTrue(len(result_columns[0])==37)

    def test_cfdi32_get_column_names_ok(self):
        transformer = ct.TCfdi32()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==37)

    def test_nomina_01_from_file_ok(self):
        path_xml = "./tests/Resources/nomina_01.xml"
        transformer = ct.TNomina12()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertTrue(len(result_columns) == 2)
        self.assertTrue(len(result_columns[0])==67)
    
    def test_nomina_01_from_bytes_ok(self):
        path_xml = "./tests/Resources/nomina_01.xml"
        xml_bytes = None
        with io.open(path_xml, 'r', encoding='utf8') as f:
            xml_bytes = f.read()
        xml_bytes = bytes(bytearray(xml_bytes, encoding= 'utf-8'))
        transformer = ct.TNomina12()
        result_columns = transformer.to_columns_from_bytes(xml_bytes)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 2)
        self.assertTrue(len(result_columns[0])==67)

    def test_nomina_get_column_names_ok(self):
        transformer = ct.TNomina12()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==67)

    def test_cfdi33_detail_01_from_file_ok(self):
        path_xml = "./tests/Resources/cfd33_detail_01.xml"
        transformer = ct.TCfdi33Detail()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertTrue(len(result_columns) == 1026)
        self.assertTrue(len(result_columns[0])==33)
    
    def test_cfdi33_detail_01_from_bytes_ok(self):
        path_xml = "./tests/Resources/cfd33_detail_01.xml"
        xml_bytes = None
        with io.open(path_xml, 'r', encoding='utf8') as f:
            xml_bytes = f.read()
        xml_bytes = bytes(bytearray(xml_bytes, encoding= 'utf-8'))
        transformer = ct.TCfdi33Detail()
        result_columns = transformer.to_columns_from_bytes(xml_bytes)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 1026)
        self.assertTrue(len(result_columns[0])==33)
    
    def test_cfdi33_detail_get_column_names_ok(self):
        transformer = ct.TCfdi33Detail()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==33)

    def test_cfdi32_detail_01_from_file_ok(self):
        path_xml = "./tests/Resources/cfdi32_01.xml"
        transformer = ct.TCfdi32Detail()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertTrue(len(result_columns) == 2)
        self.assertTrue(len(result_columns[0])==33)
        
    def test_cfdi32_detail_01_from_bytes_ok(self):
        path_xml = "./tests/Resources/cfdi32_01.xml"
        xml_bytes = None
        with io.open(path_xml, 'r', encoding='utf8') as f:
            xml_bytes = f.read()
        xml_bytes = bytes(bytearray(xml_bytes, encoding= 'utf-8'))
        transformer = ct.TCfdi32Detail()
        result_columns = transformer.to_columns_from_bytes(xml_bytes)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 2)
        self.assertTrue(len(result_columns[0])==33)

    def test_cfdi32_detail_get_column_names_ok(self):
        transformer = ct.TCfdi32Detail()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==33)

if __name__ == '__main__':
    unittest.main()