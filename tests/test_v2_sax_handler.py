import unittest
import pycfdi_transform.v2.sax.cfdi33.sax_handler as ct
from pycfdi_transform.v2.helpers.schema_helper import SchemaHelper
from lxml import etree
import time

class TestHanderCfdi33Tests(unittest.TestCase):
    def test_build_basic_object(self):
        sax_handler = ct.SAXHandler()
        self.assertIsNotNone(sax_handler)
        self.assertIsNotNone(sax_handler._data)
        self.assertIsNotNone(sax_handler._config)
        self.assertFalse(sax_handler._config['safe_numerics'])
        self.assertTrue(sax_handler._config['empty_char'] == '')
    
    def test_transform_file(self):
        sax_handler = ct.SAXHandler()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': 'VF',
                'folio': '001002004',
                'fecha': '2020-04-30T22:36:13',
                'no_certificado': '30001000000400002434',
                'subtotal': '10.00',
                'descuento': '',
                'total': '11.60',
                'moneda': 'MXN',
                'tipo_cambio': '',
                'tipo_comprobante': 'I',
                'metodo_pago': 'PPD',
                'forma_pago': '01',
                'condiciones_pago': 'NET15',
                'lugar_expedicion': '84094',
                'emisor': {
                    'rfc': 'EKU9003173C9',
                    'nombre': 'ESCUELA KEMPER URGATE SA DE CV',
                    'regimen_fiscal': '601',
                },
                'receptor': {
                    'rfc': 'XAXX010101000',
                    'nombre': 'PUBLICO EN GENERAL',
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
                            'importe': '1.60'
                        }
                    ],
                    'total_impuestos_traslados': '1.60',
                    'total_impuestos_retenidos': '',
                },
                'complementos': 'TimbreFiscalDigital',
                'addendas': '',
            },
            'tfd': [
                {
                    'version': '1.1',
                    'no_certificado_sat': '20001000000300022323',
                    'uuid': '9D81C696-0401-4F85-B703-6E0D3AFD6056',
                    'fecha_timbrado': '2020-05-02T00:36:50',
                    'rfc_prov_cert': 'AAA010101AAA',
                    'sello_cfd': 'SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw=='
                }
            ],
            'implocal': []
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_safe_numerics(self):
        sax_handler = ct.SAXHandler(safe_numerics=True)
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': 'VF',
                'folio': '001002004',
                'fecha': '2020-04-30T22:36:13',
                'no_certificado': '30001000000400002434',
                'subtotal': '10.00',
                'descuento': '0.00',
                'total': '11.60',
                'moneda': 'MXN',
                'tipo_cambio': '1.00',
                'tipo_comprobante': 'I',
                'metodo_pago': 'PPD',
                'forma_pago': '01',
                'condiciones_pago': 'NET15',
                'lugar_expedicion': '84094',
                'emisor': {
                    'rfc': 'EKU9003173C9',
                    'nombre': 'ESCUELA KEMPER URGATE SA DE CV',
                    'regimen_fiscal': '601',
                },
                'receptor': {
                    'rfc': 'XAXX010101000',
                    'nombre': 'PUBLICO EN GENERAL',
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
                            'importe': '1.60'
                        }
                    ],
                    'total_impuestos_traslados': '1.60',
                    'total_impuestos_retenidos': '0.00',
                },
                'complementos': 'TimbreFiscalDigital',
                'addendas': '',
            },
            'tfd': [
                {
                    'version': '1.1',
                    'no_certificado_sat': '20001000000300022323',
                    'uuid': '9D81C696-0401-4F85-B703-6E0D3AFD6056',
                    'fecha_timbrado': '2020-05-02T00:36:50',
                    'rfc_prov_cert': 'AAA010101AAA',
                    'sello_cfd': 'SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw=='
                }
            ],
            'implocal': []
        }
        self.assertDictEqual(cfdi_data, expected_dict)

    
    def test_transform_file_with_concepts(self):
        sax_handler = ct.SAXHandler().use_concepts_cfdi33()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': 'VF',
                'folio': '001002004',
                'fecha': '2020-04-30T22:36:13',
                'no_certificado': '30001000000400002434',
                'subtotal': '10.00',
                'descuento': '',
                'total': '11.60',
                'moneda': 'MXN',
                'tipo_cambio': '',
                'tipo_comprobante': 'I',
                'metodo_pago': 'PPD',
                'forma_pago': '01',
                'condiciones_pago': 'NET15',
                'lugar_expedicion': '84094',
                'emisor': {
                    'rfc': 'EKU9003173C9',
                    'nombre': 'ESCUELA KEMPER URGATE SA DE CV',
                    'regimen_fiscal': '601',
                },
                'receptor': {
                    'rfc': 'XAXX010101000',
                    'nombre': 'PUBLICO EN GENERAL',
                    'residencia_fiscal': '',
                    'num_reg_id_trib': '',
                    'uso_cfdi': 'G03',
                },
                'conceptos': [
                    {
                        'clave_prod_serv': '01010101',
                        'no_identificacion': 'productoInventario',
                        'cantidad': '1.0000',
                        'clave_unidad': '3G',
                        'unidad': '',
                        'descripcion': 'Detalle factura',
                        'valor_unitario': '10.0000',
                        'importe': '10.00',
                        'descuento': '',
                    }
                ],
                'impuestos': {
                    'retenciones': [],
                    'traslados': [
                        {
                            'impuesto': '002', 
                            'tipo_factor': 'Tasa', 
                            'tasa_o_cuota': '0.160000', 
                            'importe': '1.60'
                        }
                    ],
                    'total_impuestos_traslados': '1.60',
                    'total_impuestos_retenidos': '',
                },
                'complementos': 'TimbreFiscalDigital',
                'addendas': '',
            },
            'tfd': [
                {
                    'version': '1.1',
                    'no_certificado_sat': '20001000000300022323',
                    'uuid': '9D81C696-0401-4F85-B703-6E0D3AFD6056',
                    'fecha_timbrado': '2020-05-02T00:36:50',
                    'rfc_prov_cert': 'AAA010101AAA',
                    'sello_cfd': 'SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw=='
                }
            ],
            'implocal': []
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_global(self):
        start_time = time.time()
        sax_handler = ct.SAXHandler()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_large_01.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 1.0, 'Too much time to transform global cfdi')
        self.assertIsNotNone(cfdi_data)

    def test_transform_file_with_concepts_global(self):
        start_time = time.time()
        sax_handler = ct.SAXHandler().use_concepts_cfdi33()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_large_01.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 1.5, 'Too much time to transform global cfdi')
        self.assertIsNotNone(cfdi_data)
        self.assertGreater(len(cfdi_data['cfdi33']['conceptos']), 50000, 'To less concepts')

    def test_transform_file_with_concepts_validation(self):
        start_time = time.time()
        schema_validator = SchemaHelper.get_schema_validator_cfdi33()
        sax_handler = ct.SAXHandler(schema_validator=schema_validator).use_concepts_cfdi33()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_01.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 1, 'Too much time to validate xsd')
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': 'VF',
                'folio': '001002004',
                'fecha': '2020-04-30T22:36:13',
                'no_certificado': '30001000000400002434',
                'subtotal': '10.00',
                'descuento': '',
                'total': '11.60',
                'moneda': 'MXN',
                'tipo_cambio': '',
                'tipo_comprobante': 'I',
                'metodo_pago': 'PPD',
                'forma_pago': '01',
                'condiciones_pago': 'NET15',
                'lugar_expedicion': '84094',
                'emisor': {
                    'rfc': 'EKU9003173C9',
                    'nombre': 'ESCUELA KEMPER URGATE SA DE CV',
                    'regimen_fiscal': '601',
                },
                'receptor': {
                    'rfc': 'XAXX010101000',
                    'nombre': 'PUBLICO EN GENERAL',
                    'residencia_fiscal': '',
                    'num_reg_id_trib': '',
                    'uso_cfdi': 'G03',
                },
                'conceptos': [
                    {
                        'clave_prod_serv': '01010101',
                        'no_identificacion': 'productoInventario',
                        'cantidad': '1.0000',
                        'clave_unidad': '3G',
                        'unidad': '',
                        'descripcion': 'Detalle factura',
                        'valor_unitario': '10.0000',
                        'importe': '10.00',
                        'descuento': '',
                    }
                ],
                'impuestos': {
                    'retenciones': [],
                    'traslados': [
                        {
                            'impuesto': '002', 
                            'tipo_factor': 'Tasa', 
                            'tasa_o_cuota': '0.160000', 
                            'importe': '1.60'
                        }
                    ],
                    'total_impuestos_traslados': '1.60',
                    'total_impuestos_retenidos': '',
                },
                'complementos': 'TimbreFiscalDigital',
                'addendas': '',
            },
            'tfd': [
                {
                    'version': '1.1',
                    'no_certificado_sat': '20001000000300022323',
                    'uuid': '9D81C696-0401-4F85-B703-6E0D3AFD6056',
                    'fecha_timbrado': '2020-05-02T00:36:50',
                    'rfc_prov_cert': 'AAA010101AAA',
                    'sello_cfd': 'SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw=='
                }
            ],
            'implocal': []
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_with_concepts_validation_failing(self):
        schema_validator = SchemaHelper.get_schema_validator_cfdi33()
        sax_handler = ct.SAXHandler(schema_validator=schema_validator).use_concepts_cfdi33()
        with self.assertRaises(etree.DocumentInvalid) as context:
            sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_bad_structure_01.xml")
        exception = context.exception
        self.assertIn("Element '{http://www.sat.gob.mx/cfd/3}Comprobante', attribute 'Total': 'abc' is not a valid value of the atomic type '{http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI}t_Importe", str(exception))
    
    def test_transform_file_with_concepts_validation_global(self):
        start_time = time.time()
        schema_validator = SchemaHelper.get_schema_validator_cfdi33()
        sax_handler = ct.SAXHandler(schema_validator=schema_validator).use_concepts_cfdi33()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_large_01.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 2, 'Too much time to validate xsd')
        self.assertIsNotNone(cfdi_data)
    
    def test_transform_file_validation_global(self):
        start_time = time.time()
        schema_validator = SchemaHelper.get_schema_validator_cfdi33()
        sax_handler = ct.SAXHandler(schema_validator=schema_validator)
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_large_01.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 1.5, 'Too much time to validate xsd')
        self.assertIsNotNone(cfdi_data)