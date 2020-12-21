import unittest
import os
import io
import pycfdi_transform as ct

class FileUtils():
    @staticmethod
    def file_to_string(path):
        with open (path, "r", encoding="utf-8") as file_obj:
            return file_obj.read()

class TestPycfdiSaxTransformString(unittest.TestCase):

    def test_sax_cfdi33_01_from_file_ok(self):
        path_xml = './tests/Resources/cfdi33_01.xml'
        str_xml = FileUtils.file_to_string(path_xml)
        transformer = ct.TSaxCfdi33()
        result_columns = transformer.to_columns_from_string(str_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==1)
        self.assertTrue(len(result_columns[0])==38)
        self.assertTrue(result_columns[0][1] == 'VF')

    def test_sax_cfdi32_01_from_file_ok(self):
        path_xml = './tests/Resources/cfdi32_01.xml'
        str_xml = FileUtils.file_to_string(path_xml)
        transformer = ct.TSaxCfdi32()
        result_columns = transformer.to_columns_from_string(str_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 1)
        self.assertTrue(len(result_columns[0]) == 38)
        self.assertTrue(result_columns[0][14] == 'ZAPOPAN,JALISCO')
        self.assertFalse(result_columns[0][1] == 'VF')
    
    def test_sax_pago10_01_from_file_ok(self):
        path_xml = './tests/Resources/pago10_01.xml'
        str_xml = FileUtils.file_to_string(path_xml)
        transformer = ct.TSaxPagos10()
        result_columns = transformer.to_columns_from_string(str_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 1)
        self.assertTrue(len(result_columns[0]) == 54)
    
    def test_sax_nomina12_01_from_file_ok(self):
        path_xml = './tests/Resources/nomina12_02.xml'
        str_xml = FileUtils.file_to_string(path_xml)
        transformer = ct.TSaxNomina12()
        columns = transformer.get_column_names()
        result_columns = transformer.to_columns_from_string(str_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 1)
        self.assertTrue(result_columns[0][57] == '87703.08')
        self.assertTrue(result_columns[0][58] == '27835.199999999997')
        self.assertTrue(len(result_columns[0]) == 440)
        self.assertTrue(len(result_columns[0]) == len(columns))
    
    def test_sax_nomina11_01_from_file_ok(self):
        path_xml = './tests/Resources/nomina11_01.xml'
        str_xml = FileUtils.file_to_string(path_xml)
        transformer = ct.TSaxNomina11()
        result_columns = transformer.to_columns_from_string(str_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 1)
        self.assertTrue(len(result_columns[0]) == 440)
    
    def test_sax_cfdi33_detail_01_from_file_ok(self):
        path_xml = './tests/Resources/0B7B5AA2-2443-49A2-810D-C0A9A813F8EF.xml'
        str_xml = FileUtils.file_to_string(path_xml)
        transformer = ct.TSaxCfdi33Detail()
        result_columns = transformer.to_columns_from_string(str_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 1026)
        self.assertTrue(len(result_columns[0]) == 33)

    def test_sax_cfdi32_detail_01_from_file_ok(self):
        path_xml = './tests/Resources/cfdi32_01.xml'
        str_xml = FileUtils.file_to_string(path_xml)
        transformer = ct.TSaxCfdi32Detail()
        result_columns = transformer.to_columns_from_string(str_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 2)
        self.assertTrue(len(result_columns[0]) == 33)

    def test_sax_cfdi33_addenda_from_file_ok(self):
        path_xml = './tests/Resources/cfdi33_addenda.xml'
        str_xml = FileUtils.file_to_string(path_xml)
        transformer = ct.TSaxCfdi33()
        result_columns = transformer.to_columns_from_string(str_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==1)
        self.assertTrue(len(result_columns[0])==38)
        self.assertTrue(transformer.has_addendas())
        self.assertTrue(transformer.get_addendas() == 'NombreAdenda, xmlAtt')

if __name__ == '__main__':
    unittest.main()
