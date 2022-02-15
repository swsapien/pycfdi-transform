from pycfdi_transform.formatters.cfdi32.efisco_cfdi32_formatter import EfiscoCorpCFDI32Formatter
import unittest

from pycfdi_transform.sax.cfdi32.sax_handler import CFDI32SAXHandler


class TestEfiscoCorpCFDI32Formatter(unittest.TestCase):

    def test_columns_names_cfdi32(self):
        formatter = EfiscoCorpCFDI32Formatter({'cfdi32': {}})
        columns_expected = [
            'VERSION', 
            'SERIE', 
            'FOLIO', 
            'FECHA', 
            'NOCERTIFICADO', 
            'SUBTOTAL', 
            'DESCUENTO', 
            'TOTAL', 
            'MONEDA', 
            'TIPOCAMBIO', 
            'TIPODECOMPROBANTE', 
            'METODOPAGO', 
            'FORMAPAGO', 
            'CONDICIONESDEPAGO', 
            'LUGAREXPEDICION', 
            'EMISORRFC', 
            'EMISORNOMBRE', 
            'EMISORREGIMENFISCAL', 
            'RECEPTORRFC', 
            'RECEPTORNOMBRE', 
            'RESIDENCIAFISCAL', 
            'NUMREGIDTRIB', 
            'RECEPTORUSOCFDI', 
            'CLAVEPRODSERV',
            'C_DESCRIPCION',
            'IVATRASLADO', 
            'IEPSTRASLADO', 
            'TOTALIMPUESTOSTRASLADOS', 
            'ISRRETENIDO', 
            'IVARETENIDO', 
            'IEPSRETENIDO', 
            'TOTALIMPUESTOSRETENIDOS', 
            'TOTALTRASLADOSIMPUESTOSLOCALES', 
            'TOTALRETENCIONESIMPUESTOSLOCALES', 
            'COMPLEMENTOS', 
            'UUID', 
            'FECHATIMBRADO', 
            'RFCPROVCERTIF', 
            'SELLOCFD']
        self.assertListEqual(columns_expected, formatter.get_columns_names())
    
    def test_initialize_class_error_cfdi32(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoCorpCFDI32Formatter(cfdi_data=None)
        self.assertEqual('El Formatter debe recibir el objeto devuelto por la transformación el debe ser un dict.', str(ex.exception))
    
    def test_initialize_class_error_version_cfdi32(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoCorpCFDI32Formatter({'cfdi33': {}})
        self.assertEqual('Este formatter únicamente soporta datos de cfdi32.', str(ex.exception))

    def test_formatter_error_tfd_cfdi32(self):
        sax_handler = CFDI32SAXHandler()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi32/cfdi32_01.xml')
        cfdi_data.pop('tfd10')
        formatter = EfiscoCorpCFDI32Formatter(cfdi_data)
        self.assertFalse(formatter.can_format())
        self.assertEqual(formatter.get_errors(), 'Not tfd10 in data.')
    
    def test_formatter_cfdi32_implocal10_ok(self):
        sax_handler = CFDI32SAXHandler().use_implocal10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi32/cfdi32_01.xml')
        formatter = EfiscoCorpCFDI32Formatter(cfdi_data)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 2)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
    
    def test_formatter_cfdi32_implocal10_safe_numerics_1(self):
        sax_handler = CFDI32SAXHandler().use_implocal10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi32/cfdi32_01.xml')
        formatter = EfiscoCorpCFDI32Formatter(cfdi_data,empty_char='',safe_numerics=True)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 2)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
        self.assertEqual(data_columns[0][32],'0.00')
    
    def test_formatter_cfdi32_implocal10_safe_empty_char_1(self):
        sax_handler = CFDI32SAXHandler().use_implocal10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi32/cfdi32_01.xml')
        formatter = EfiscoCorpCFDI32Formatter(cfdi_data,empty_char='-',safe_numerics=False)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 2)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
        self.assertEqual(data_columns[0][32],'-')
    
    def test_formatter_cfdi32_implocal10_multiple_complements(self):
        sax_handler = CFDI32SAXHandler().use_implocal10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi32/cfdi32_01.xml')
        formatter = EfiscoCorpCFDI32Formatter(cfdi_data,empty_char='-',safe_numerics=False)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 2)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
        self.assertEqual(data_columns[0][32],'-')
        self.assertEqual(data_columns[0][33],'-')
    
    def test_formatter_line_breaks_cfdi32(self):
        sax_handler = CFDI32SAXHandler().use_concepts_cfdi32()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi32/cfdi32_01.xml')
        formatter = EfiscoCorpCFDI32Formatter(cfdi_data)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '')
        data_columns = formatter.dict_to_columns()
        self.assertEqual(len(data_columns), 2)
        self.assertEqual(len(data_columns[0]), len(formatter.get_columns_names()))
        named_column = dict(zip(formatter.get_columns_names(), data_columns[0]))
        self.assertEqual(named_column['CONDICIONESDEPAGO'], '')
        self.assertEqual(named_column['EMISORNOMBRE'], 'MI SUPER CUENTA DE DESSARROLLO')
        self.assertEqual(named_column['RECEPTORNOMBRE'], 'PUBLICO GENERAL')
        self.assertEqual(named_column['C_DESCRIPCION'], '123')
