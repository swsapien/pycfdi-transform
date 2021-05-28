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
        self.assertTrue(result_columns[0][34] == 'D237D7D1-CFAD-492A-89C1-BF3E6CED9E59') 
        self.assertTrue(result_columns[1][34] == '1931BBAD-DE49-4703-8F1A-9F4B663495D5')

    def test_sax_cfdi32(self):
        path_xml = './tests/Resources/cfdi32_multiple_tfd.xml'
        transformer = ct.TSaxCfdi32()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 3)
        self.assertTrue(len(result_columns[0]) == 38)
        self.assertTrue(result_columns[0][34] == '9d81c696-0401-4f85-b703-6e0d3afd6057'.upper()) 
        self.assertTrue(result_columns[1][34] == '1d81c696-0401-4f85-b703-6e0d3afd6057'.upper())
        self.assertTrue(result_columns[2][34] == '2d81c696-0401-4f85-b703-6e0d3afd6057'.upper())

    def test_sax_cfdi33_nomina(self):
        path_xml = './tests/Resources/cfdi33_nomina_multiple_tfd.xml'
        transformer = ct.TSaxNomina12()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 2)
        self.assertTrue(len(result_columns[0]) == 440)
        self.assertTrue(result_columns[0][21] == 'D237D7D1-CFAD-492A-89C1-BF3E6CED9E59') 
        self.assertTrue(result_columns[1][21] == '1931BBAD-DE49-4703-8F1A-9F4B663495D5')

    def test_sax_cfdi33_detail(self):
        path_xml = './tests/Resources/cfdi33_multiple_tfd.xml'
        transformer = ct.TSaxCfdi33Detail()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 2)
        self.assertTrue(len(result_columns[0]) == 33)
        self.assertTrue(result_columns[0][21] == '9D81C696-0401-4F85-B703-6E0D3AFD6056') 
        self.assertTrue(result_columns[1][21] == '1D81C696-0401-4F85-B703-6E0D3AFD6056')
    
    def test_sax_pago10(self):
        path_xml = './tests/Resources/pago10_multiple_tfd.xml'
        transformer = ct.TSaxPagos10()
        result_columns = transformer.to_columns_from_file(path_xml)
        self.assertFalse(result_columns is None)
        self.assertTrue(len(result_columns) == 2)
        self.assertTrue(len(result_columns[0]) == 54)
        self.assertTrue(result_columns[0][21] == '9d81c696-0401-4f85-b703-6e0d3afd6057'.upper()) 
        self.assertTrue(result_columns[1][21] == '1d81c696-0401-4f85-b703-6e0d3afd6057'.upper())
        