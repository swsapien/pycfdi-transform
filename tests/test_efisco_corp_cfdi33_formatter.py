from pycfdi_transform import CFDI33SAXHandler
from pycfdi_transform.formatters.cfdi33.efisco_corp_cfdi33_formatter import EfiscoCorpCFDI33Formatter
import unittest

class TestEfiscoCorpCFDI33Formatter(unittest.TestCase):

    def test_columns_names_cfdi33(self):
        formatter = EfiscoCorpCFDI33Formatter({'cfdi33': {}})
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
    
    def test_initialize_class_error_cfdi33(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoCorpCFDI33Formatter(cfdi_data=None)
        self.assertEqual('El Formatter debe recibir el objeto devuelto por la transformación el debe ser un dict.', str(ex.exception))
    
    def test_initialize_class_error_version_cfdi33(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoCorpCFDI33Formatter({'cfdi32': {}})
        self.assertEqual('Este formatter únicamente soporta datos de cfdi33.', str(ex.exception))
    
    def test_formatter_error_tfd_cfdi33(self):
        sax_handler = CFDI33SAXHandler()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi33/cfdi33_01.xml')
        cfdi_data.pop('tfd11')
        formatter = EfiscoCorpCFDI33Formatter(cfdi_data)
        self.assertFalse(formatter.can_format())
        self.assertEqual(formatter.get_errors(), 'Not tfd11 in data.')
    
    def test_formatter_cfdi33_implocal10_ok(self):
        sax_handler = CFDI33SAXHandler().use_implocal10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/implocal/cfdi33_implocal02.xml')
        formatter = EfiscoCorpCFDI33Formatter(cfdi_data)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 1)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
        self.assertEqual(data_columns[0][32],'0.000000')
        self.assertEqual(data_columns[0][33],'77.400000')
    
    def test_formatter_cfdi33_implocal10_safe_numerics_1(self):
        sax_handler = CFDI33SAXHandler().use_implocal10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/implocal/cfdi33_implocal02_incorrect.xml')
        formatter = EfiscoCorpCFDI33Formatter(cfdi_data,empty_char='',safe_numerics=True)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 1)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
        self.assertEqual(data_columns[0][32],'0.00')
    
    def test_formatter_cfdi33_implocal10_safe_empty_char_1(self):
        sax_handler = CFDI33SAXHandler().use_implocal10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/implocal/cfdi33_implocal02_incorrect.xml')
        formatter = EfiscoCorpCFDI33Formatter(cfdi_data,empty_char='-',safe_numerics=False)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 1)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
        self.assertEqual(data_columns[0][32],'-')
    
    def test_formatter_cfdi33_implocal10_multiple_complements(self):
        sax_handler = CFDI33SAXHandler().use_implocal10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/implocal/cfdi33_implocal02_multiple.xml')
        formatter = EfiscoCorpCFDI33Formatter(cfdi_data,empty_char='-',safe_numerics=False)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 1)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
        self.assertEqual(data_columns[0][32],'20.000000')
        self.assertEqual(data_columns[0][33],'40.000000')
    
    def test_formatter_line_breaks_cfdi33(self):
        sax_handler = CFDI33SAXHandler().use_concepts_cfdi33()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi33/cfdi33_01.xml')
        formatter = EfiscoCorpCFDI33Formatter(cfdi_data)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '')
        data_columns = formatter.dict_to_columns()
        self.assertEqual(len(data_columns), 1)
        self.assertEqual(len(data_columns[0]), len(formatter.get_columns_names()))
        named_column = dict(zip(formatter.get_columns_names(), data_columns[0]))
        self.assertEqual(named_column['CONDICIONESDEPAGO'], 'NET15')
        self.assertEqual(named_column['EMISORNOMBRE'], 'ESCUELA KEMPER URGATE SA DE CV')
        self.assertEqual(named_column['RECEPTORNOMBRE'], 'PUBLICO EN GENERAL')
        self.assertEqual(named_column['C_DESCRIPCION'], 'Detalle factura')
        self.assertEqual(named_column['COMPLEMENTOS'], 'TimbreFiscalDigital')
