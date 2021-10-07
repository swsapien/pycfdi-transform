from pycfdi_transform import CFDI33SAXHandler, SchemaHelper
from lxml.etree import DocumentInvalid
from lxml import etree
import unittest

class TestImpLocal10SAXHandler(unittest.TestCase):
    def test_transform_file_implocal(self):
        sax_handler = CFDI33SAXHandler().use_implocal10()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/implocal/cfdi33_implocal01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': 'G',
                'folio': '370',
                'fecha': '2020-02-25T23:17:37',
                'no_certificado': '00000000000000000000',
                'subtotal': '1290.00',
                'descuento': '',
                'total': '1419.00',
                'moneda': 'MXN',
                'tipo_cambio': '',
                'tipo_comprobante': 'I',
                'metodo_pago': 'PPD',
                'forma_pago': '99',
                'condiciones_pago': '',
                'lugar_expedicion': '56400',
                'sello':'',
                'certificado':'',
                'confirmacion':'',
                'emisor': {
                    'rfc': 'XIA190128J61',
                    'nombre': 'XIA190128J61',
                    'regimen_fiscal': '601',
                },
                'receptor': {
                    'rfc': 'XIA190128J61',
                    'nombre': 'XIA190128J61',
                    'residencia_fiscal': '',
                    'num_reg_id_trib': '',
                    'uso_cfdi': 'G03',
                },
                'conceptos': [],
                'impuestos': {
                    'retenciones': [], 
                    'traslados': [
                        {
                            'impuesto': '002', 
                            'tipo_factor': 'Tasa', 
                            'tasa_o_cuota': '0.160000', 
                            'importe': '206.400000'
                        }
                    ], 
                    'total_impuestos_traslados': '206.40', 
                    'total_impuestos_retenidos': ''
                },
                'complementos': 'ImpuestosLocales',
                'addendas': '',
            },
            'tfd11': [],
            'implocal10': [
                {
                    'total_traslados_impuestos_locales': '0.000000',
                    'total_retenciones_impuestos_locales': '77.400000'
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_implocal_validation(self):
        schema_validator = SchemaHelper.get_schema_validator_cfdi33()
        sax_handler = CFDI33SAXHandler(schema_validator=schema_validator).use_implocal10()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/implocal/cfdi33_implocal01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': 'G',
                'folio': '370',
                'fecha': '2020-02-25T23:17:37',
                'no_certificado': '00000000000000000000',
                'subtotal': '1290.00',
                'descuento': '',
                'total': '1419.00',
                'moneda': 'MXN',
                'tipo_cambio': '',
                'tipo_comprobante': 'I',
                'metodo_pago': 'PPD',
                'forma_pago': '99',
                'condiciones_pago': '',
                'lugar_expedicion': '56400',
                'sello':'',
                'certificado':'',
                'confirmacion':'',
                'emisor': {
                    'rfc': 'XIA190128J61',
                    'nombre': 'XIA190128J61',
                    'regimen_fiscal': '601',
                },
                'receptor': {
                    'rfc': 'XIA190128J61',
                    'nombre': 'XIA190128J61',
                    'residencia_fiscal': '',
                    'num_reg_id_trib': '',
                    'uso_cfdi': 'G03',
                },
                'conceptos': [],
                'impuestos': {
                    'retenciones': [], 
                    'traslados': [
                        {
                            'impuesto': '002', 
                            'tipo_factor': 'Tasa', 
                            'tasa_o_cuota': '0.160000', 
                            'importe': '206.400000'
                        }
                    ], 
                    'total_impuestos_traslados': '206.40', 
                    'total_impuestos_retenidos': ''
                },
                'complementos': 'ImpuestosLocales',
                'addendas': '',
            },
            'tfd11': [],
            'implocal10': [
                {
                    'total_traslados_impuestos_locales': '0.000000',
                    'total_retenciones_impuestos_locales': '77.400000'
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_implocal_safe_numerics(self):
        sax_handler = CFDI33SAXHandler(safe_numerics=True).use_implocal10()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/implocal/cfdi33_implocal01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': 'G',
                'folio': '370',
                'fecha': '2020-02-25T23:17:37',
                'no_certificado': '00000000000000000000',
                'subtotal': '1290.00',
                'descuento': '0.00',
                'total': '1419.00',
                'moneda': 'MXN',
                'tipo_cambio': '1.00',
                'tipo_comprobante': 'I',
                'metodo_pago': 'PPD',
                'forma_pago': '99',
                'condiciones_pago': '',
                'lugar_expedicion': '56400',
                'sello':'',
                'certificado':'',
                'confirmacion':'',
                'emisor': {
                    'rfc': 'XIA190128J61',
                    'nombre': 'XIA190128J61',
                    'regimen_fiscal': '601',
                },
                'receptor': {
                    'rfc': 'XIA190128J61',
                    'nombre': 'XIA190128J61',
                    'residencia_fiscal': '',
                    'num_reg_id_trib': '',
                    'uso_cfdi': 'G03',
                },
                'conceptos': [],
                'impuestos': {
                    'retenciones': [], 
                    'traslados': [
                        {
                            'impuesto': '002', 
                            'tipo_factor': 'Tasa', 
                            'tasa_o_cuota': '0.160000', 
                            'importe': '206.400000'
                        }
                    ], 
                    'total_impuestos_traslados': '206.40', 
                    'total_impuestos_retenidos': '0.00'
                },
                'complementos': 'ImpuestosLocales',
                'addendas': '',
            },
            'tfd11': [],
            'implocal10': [
                {
                    'total_traslados_impuestos_locales': '0.000000',
                    'total_retenciones_impuestos_locales': '77.400000'
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_implocal_broken_file_validation(self):
        schema_validator = SchemaHelper.get_schema_validator_cfdi33()
        sax_handler = CFDI33SAXHandler(schema_validator=schema_validator).use_implocal10()
        with self.assertRaises(etree.DocumentInvalid) as ex:
            cfdi_data = sax_handler.transform_from_file("./tests/Resources/implocal/cfdi33_implocal_broken.xml")
            print(cfdi_data)
        exception = ex.exception
        self.assertIn("Element '{http://www.sat.gob.mx/implocal}RetencionesLocales': Character content is not allowed, because the content type is empty", str(exception))