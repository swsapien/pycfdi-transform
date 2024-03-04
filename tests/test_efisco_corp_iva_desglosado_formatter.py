import os
from pycfdi_transform import CFDI33SAXHandler
from pycfdi_transform import CFDI40SAXHandler
import unittest

from pycfdi_transform import EfiscoCorpIvaDesglosadoFormatter

class TestEfiscoCorpIvaDesglosadoFormatter(unittest.TestCase):

    def test_columns_names_cfdi33(self):
        formatter = EfiscoCorpIvaDesglosadoFormatter({'cfdi33': {}})
        columns_expected = [
            "UUID",
            "TIPO_IMPUESTOS",
            "IMPUESTO",
            "IMPORTE",
            "BASE",
            "TIPO_FACTOR",
            "TASA_O_CUOTA",
        ]
        self.assertListEqual(columns_expected, formatter.get_columns_names())
    
    def test_initialize_class_error_cfdi33(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoCorpIvaDesglosadoFormatter(cfdi_data=None)
        self.assertEqual('El Formatter debe recibir el objeto devuelto por la transformación el debe ser un dict.', str(ex.exception))
    
    def test_initialize_class_error_version_cfdi33(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoCorpIvaDesglosadoFormatter({'cfdi32': {}})
        self.assertEqual('Este formatter únicamente soporta datos de cfdi33 o cfdi40.', str(ex.exception))
    
    def test_formatter_tipo_comprobante(self):
        sax_handler = CFDI40SAXHandler()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/pagos20/pago_complete.xml')
        formatter = EfiscoCorpIvaDesglosadoFormatter(cfdi_data)
        self.assertFalse(formatter.can_format())
        self.assertEqual(formatter.get_errors(), 'Este formatter solo puede formatear tipos de comprobante I y E.')
    
    def test_formatter_cfdi33_iva_desglosado_ok(self):
        sax_handler = CFDI33SAXHandler()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/implocal/cfdi33_implocal02.xml')
        formatter = EfiscoCorpIvaDesglosadoFormatter(cfdi_data)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 1)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
        self.assertEqual(data_columns[0][3],'206.400000')
        self.assertEqual(data_columns[0][6],'0.160000')
    def test_formatter_cfdi40_iva_desglosado_ok(self):
        sax_handler = CFDI40SAXHandler()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/cfdi40/cfdi40_01.xml')
        formatter = EfiscoCorpIvaDesglosadoFormatter(cfdi_data)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 7)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
    
    def test_formatter_cfdi33_iva_desglosado_safe_numerics_ok(self):
        sax_handler = CFDI33SAXHandler()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/implocal/cfdi33_implocal02_incorrect.xml')
        formatter = EfiscoCorpIvaDesglosadoFormatter(cfdi_data,empty_char='', safe_numerics=True)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 1)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
        self.assertEqual('206.400000', data_columns[0][3])
        self.assertEqual('0.00', data_columns[0][4])
        self.assertEqual('0.160000', data_columns[0][6])

    

