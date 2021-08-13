import unittest
import os
import io
import pycfdi_transform as ct



class TestPycfdiSaxTransform(unittest.TestCase):

    def test_sax_cfdi33_01_from_file_ok(self):
        path_xml = './tests/Resources/cfdi33_01.xml'
        transformer = ct.TSaxCfdi33()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==1)
        self.assertTrue(len(result_columns[0])==38)
        self.assertTrue(result_columns[0][1] == 'VF')
    
    def test_sax_cfdi33_get_column_names_ok(self):
        transformer = ct.TSaxCfdi33()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 38)
        self.assertTrue(result_columns[4] == 'NOCERTIFICADO')
        self.assertFalse(result_columns[17] == 'SERIE')
    def test_sax_cfdi33_01_description_from_file_ok(self):
        path_xml = './tests/Resources/cfdi33_01.xml'
        transformer = ct.TSaxCfdi33Description()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==1)
        self.assertTrue(len(result_columns[0])==39)
        self.assertTrue(result_columns[0][24] == 'Detalle factura')
    def test_sax_cfdi33_01_description_from_file_ok_2(self):
        path_xml = './tests/Resources/cfd33_description_01.xml'
        transformer = ct.TSaxCfdi33Description()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==1)
        self.assertTrue(len(result_columns[0])==39)
        self.assertTrue(result_columns[0][24] == 'Cigarros Correcto')
    
    def test_sax_cfdi33_description_get_column_names_ok(self):
        transformer = ct.TSaxCfdi33Description()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 39)
        self.assertTrue(result_columns[4] == 'NOCERTIFICADO')
        self.assertTrue(result_columns[24] == 'C_DESCRIPCION')

    def test_sax_cfdi32_01_from_file_ok(self):
        path_xml = './tests/Resources/cfdi32_01.xml'
        transformer = ct.TSaxCfdi32()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 1)
        self.assertTrue(len(result_columns[0]) == 38)
        self.assertTrue(result_columns[0][14] == 'ZAPOPAN,JALISCO')
        self.assertFalse(result_columns[0][1] == 'VF')
    
    def test_sax_cfdi32_get_column_names_ok(self):
        transformer = ct.TSaxCfdi32()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 38)
        self.assertTrue(result_columns[4] == 'NOCERTIFICADO')
        self.assertFalse(result_columns[17] == 'SERIE')
    
    def test_sax_pago10_01_from_file_ok(self):
        path_xml = './tests/Resources/pago10_01.xml'
        transformer = ct.TSaxPagos10()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 1)
        self.assertTrue(len(result_columns[0]) == 54)
    def test_sax_pago10_01_non_dr_from_file_ok(self):
        path_xml = './tests/Resources/pago10NonDr.xml'
        transformer = ct.TSaxPagos10()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 1)
    
    def test_sax_pago10_get_column_names_ok(self):
        transformer = ct.TSaxPagos10()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 54)
        self.assertFalse(result_columns[0] == 'SERIE')
        self.assertTrue(result_columns[12] == 'FORMAPAGO')
        self.assertTrue(result_columns[36] == 'CTABENEFICIARIO')
    
    def test_sax_nomina12_01_from_file_ok(self):
        path_xml = './tests/Resources/nomina12_02.xml'
        transformer = ct.TSaxNomina12()
        columns = transformer.get_column_names()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 1)
        self.assertTrue(result_columns[0][57] == '87703.08')
        self.assertTrue(result_columns[0][58] == '27835.199999999997')
        self.assertTrue(len(result_columns[0]) == 440)
        self.assertTrue(len(result_columns[0]) == len(columns))
    
    def test_sax_nomina12_get_column_names_ok(self):
        transformer = ct.TSaxNomina12()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 440)
        self.assertFalse(result_columns[0] == 'FOLIO')
        self.assertTrue(result_columns[12] == 'FORMAPAGO')
        self.assertTrue(result_columns[36] == 'CURPRECEPTOR')
    
    def test_sax_nomina11_01_from_file_ok(self):
        path_xml = './tests/Resources/nomina11_01.xml'
        transformer = ct.TSaxNomina11()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 1)
        self.assertTrue(len(result_columns[0]) == 440)

    def test_sax_nomina11_get_column_names_ok(self):
        transformer = ct.TSaxNomina11()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 439)
        self.assertFalse(result_columns[0] == 'FOLIO')
        self.assertTrue(result_columns[12] == 'FORMAPAGO')
        self.assertTrue(result_columns[36] == 'CURPRECEPTOR')
    
    def test_sax_cfdi33_detail_01_from_file_ok(self):
        path_xml = './tests/Resources/0B7B5AA2-2443-49A2-810D-C0A9A813F8EF.xml'
        transformer = ct.TSaxCfdi33Detail()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 1026)
        self.assertTrue(len(result_columns[0]) == 33)

    def test_sax_cfdi33_detail_get_column_names_ok(self):
        transformer = ct.TSaxCfdi33Detail()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 33)

    def test_sax_cfdi32_detail_01_from_file_ok(self):
        path_xml = './tests/Resources/cfdi32_01.xml'
        transformer = ct.TSaxCfdi32Detail()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 2)
        self.assertTrue(len(result_columns[0]) == 33)

    def test_sax_cfdi32_detail_get_column_names_ok(self):
        transformer = ct.TSaxCfdi32Detail()
        result_columns = transformer.get_column_names()
        self.assertFalse(result_columns is None)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 33)

    def test_sax_cfdi33_addenda_from_file_ok(self):
        path_xml = './tests/Resources/cfdi33_addenda.xml'
        transformer = ct.TSaxCfdi33()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns)==1)
        self.assertTrue(len(result_columns[0])==38)
        self.assertTrue(transformer.has_addendas())
        self.assertTrue(transformer.get_addendas() == 'NombreAdenda, xmlAtt')

if __name__ == '__main__':
    unittest.main()
