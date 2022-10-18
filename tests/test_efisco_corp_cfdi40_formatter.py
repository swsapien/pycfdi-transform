import os
from pycfdi_transform import CFDI40SAXHandler
from pycfdi_transform.formatters.cfdi40.efisco_corp_cfdi40_formatter import EfiscoCorpCFDI40Formatter
import unittest

class TestEfiscoCorpCFDI40Formatter(unittest.TestCase):

    def test_columns_names_cfdi40(self):
        formatter = EfiscoCorpCFDI40Formatter({'cfdi40': {}})
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
            'RECEPTORDOMICILIOFISCAL',
            'RECEPTORREGIMENFISCAL',
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
            'SELLOCFD',
            'METODOPAGO32',
            'FORMAPAGO32',
            'MONEDA32',
            'EMISORREGIMENFISCAL32'
        ]
        self.assertListEqual(columns_expected, formatter.get_columns_names())
    
    def test_initialize_class_error_cfdi40(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoCorpCFDI40Formatter(cfdi_data=None)
        self.assertEqual('El Formatter debe recibir el objeto devuelto por la transformación el debe ser un dict.', str(ex.exception))
    
    def test_initialize_class_error_version_cfdi40(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoCorpCFDI40Formatter({'cfdi32': {}})
        self.assertEqual('Este formatter únicamente soporta datos de cfdi40.', str(ex.exception))
    
    def test_formatter_error_tfd_cfdi40(self):
        sax_handler = CFDI40SAXHandler()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/cfdi40/cfdi40_01.xml')
        cfdi_data.pop('tfd11')
        formatter = EfiscoCorpCFDI40Formatter(cfdi_data)
        self.assertFalse(formatter.can_format())
        self.assertEqual(formatter.get_errors(), 'Not tfd11 in data.')
    
    def test_formatter_cfdi40_implocal10_ok(self):
        sax_handler = CFDI40SAXHandler().use_implocal10()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/implocal/cfdi40_01_implocal.xml')
        formatter = EfiscoCorpCFDI40Formatter(cfdi_data)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 1)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
        self.assertEqual(data_columns[0][32],'0.00')
        self.assertEqual(data_columns[0][33],'')
    
    def test_formatter_cfdi40_implocal10_safe_numerics_1(self):
        sax_handler = CFDI40SAXHandler(safe_numerics=True).use_implocal10()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/implocal/cfdi40_01_implocal.xml')
        formatter = EfiscoCorpCFDI40Formatter(cfdi_data,empty_char='',safe_numerics=True)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 1)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
        named_dict = dict(zip(formatter.get_columns_names(), data_columns[0]))
        self.assertEqual(named_dict['DESCUENTO'],'0.00')
        self.assertEqual(named_dict['IVATRASLADO'],'0.00')
        self.assertEqual(named_dict['IEPSTRASLADO'],'0.00')
        self.assertEqual(named_dict['TOTALIMPUESTOSTRASLADOS'],'0.00')
        self.assertEqual(named_dict['ISRRETENIDO'],'0.00')
        self.assertEqual(named_dict['IVARETENIDO'],'0.00')
        self.assertEqual(named_dict['IEPSRETENIDO'],'0.00')
        self.assertEqual(named_dict['TOTALIMPUESTOSRETENIDOS'],'0.00')
    
    def test_formatter_cfdi40_implocal10_safe_empty_char_1(self):
        sax_handler = CFDI40SAXHandler().use_implocal10()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/implocal/cfdi40_01_implocal.xml')
        formatter = EfiscoCorpCFDI40Formatter(cfdi_data,empty_char='-',safe_numerics=False)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 1)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
        named_dict = dict(zip(formatter.get_columns_names(), data_columns[0]))
        self.assertEqual(named_dict['SERIE'],'-')
        self.assertEqual(named_dict['FOLIO'],'-')
        self.assertEqual(named_dict['CONDICIONESDEPAGO'],'-')
        self.assertEqual(named_dict['NUMREGIDTRIB'],'-')
    
    def test_formatter_cfdi40_implocal10_multiple_complements(self):
        sax_handler = CFDI40SAXHandler().use_implocal10()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/implocal/cfdi40_01_implocal_multiple.xml')
        formatter = EfiscoCorpCFDI40Formatter(cfdi_data,empty_char='-',safe_numerics=False)
        data_columns = formatter.dict_to_columns()
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(),'')
        self.assertTrue(len(data_columns) == 1)
        self.assertTrue(len(data_columns[0]) == len(formatter.get_columns_names()))
        self.assertEqual(data_columns[0][32],'0.00')
        self.assertEqual(data_columns[0][33],'-')
    
    def test_formatter_line_breaks_cfdi40(self):
        sax_handler = CFDI40SAXHandler().use_concepts_cfdi40()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/cfdi40/cfdi40_01.xml')
        formatter = EfiscoCorpCFDI40Formatter(cfdi_data)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '')
        data_columns = formatter.dict_to_columns()
        self.assertEqual(len(data_columns), 1)
        self.assertEqual(len(data_columns[0]), len(formatter.get_columns_names()))
        named_column = dict(zip(formatter.get_columns_names(), data_columns[0]))
        self.assertEqual(named_column['CONDICIONESDEPAGO'], 'NET15')
        self.assertEqual(named_column['EMISORNOMBRE'], 'ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~')
        self.assertEqual(named_column['RECEPTORNOMBRE'], 'kghfhg~')
        self.assertEqual(named_column['COMPLEMENTOS'], 'TimbreFiscalDigital')
    
    def test_formatter_concepts_cfdi40(self):
        sax_handler = CFDI40SAXHandler().use_concepts_cfdi40()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/cfdi40/cfdi40_01.xml')
        formatter = EfiscoCorpCFDI40Formatter(cfdi_data)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '')
        data_columns = formatter.dict_to_columns()
        self.assertEqual(len(data_columns), 1)
        self.assertEqual(len(data_columns[0]), len(formatter.get_columns_names()))
        named_column = dict(zip(formatter.get_columns_names(), data_columns[0]))
        self.assertEqual(named_column['CONDICIONESDEPAGO'], 'NET15')
        self.assertEqual(named_column['EMISORNOMBRE'], 'ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~')
        self.assertEqual(named_column['RECEPTORNOMBRE'], 'kghfhg~')
        self.assertEqual(named_column['COMPLEMENTOS'], 'TimbreFiscalDigital')
        claveProdList = data_columns[0][23].split(",")
        hasDuplicates = any(claveProdList.count(x) > 1 for x in claveProdList)
        self.assertFalse(hasDuplicates)

    def test_formatter_cfdi40_addenda(self):
        sax_handler = CFDI40SAXHandler(safe_numerics=True, empty_char='-')
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/cfdi40/cfdi40_01_addenda.xml')
        formatter = EfiscoCorpCFDI40Formatter(cfdi_data, safe_numerics=True, empty_char='-')
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '')
        self.assertTrue(formatter.has_addenda())
        self.assertTrue(formatter.get_addendas() is not None and formatter.get_addendas() == "NombreAdenda xmlAtt")
    
    def test_formatter_cfdi40_not_addenda(self):
        sax_handler = CFDI40SAXHandler(safe_numerics=True, empty_char='-')
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/cfdi40/cfdi40_01.xml')
        formatter = EfiscoCorpCFDI40Formatter(cfdi_data, safe_numerics=True, empty_char='-')
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '')
        self.assertFalse(formatter.has_addenda())
        self.assertTrue(formatter.get_addendas() is not None and formatter.get_addendas() == "")
        