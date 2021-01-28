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
        self.assertTrue(result_columns[0][34] == '8936CB73-2A13-4230-9E01-6E9B0EDD7CDE') 
        self.assertTrue(result_columns[1][34] == 'A89A5F34-7725-46FA-8D25-01D4862C5CD2')

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
        self.assertTrue(result_columns[0][21] == '8936CB73-2A13-4230-9E01-6E9B0EDD7CDE') 
        self.assertTrue(result_columns[1][21] == 'A89A5F34-7725-46FA-8D25-01D4862C5CD2')

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
        