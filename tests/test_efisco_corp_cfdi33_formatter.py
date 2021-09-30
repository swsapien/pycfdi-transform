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
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/implocal/cfdi33_implocal01.xml')
        formatter = EfiscoCorpCFDI33Formatter(cfdi_data)
        data_columns = formatter.dict_to_columns()
        self.assertFalse(formatter.can_format())
        self.assertIsNone(formatter.get_errors())
        self.assertCountEqual(data_columns,formatter.get_columns_names())
        self.assertEquals(data_columns['cfdi33']['implocal10']['total_traslados_impuestos_locales'],'0.000000')