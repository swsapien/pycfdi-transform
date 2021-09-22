import unittest
import pycfdi_transform.v2.sax.cfdi33.sax_handler as ct

class TestHanderCfdi33ImpLocalTests(unittest.TestCase):
    def test_transform_file_implocal(self):
        sax_handler = ct.SAXHandler()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33_implocal01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': 'G',
                'folio': '370',
                'fecha': '2020-02-25T23:17:37',
                'no_certificado': '',
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
                    'iva_traslado': '206.400000',
                    'ieps_traslado': '',
                    'isr_retenido': '',
                    'iva_retenido': '',
                    'ieps_retenido': '',
                    'total_impuestos_traslados': '206.40',
                    'total_impuestos_retenidos': '',
                },
                'complementos': 'ImpuestosLocales',
                'addendas': '',
            },
            'tfd': [],
            'implocal': [
                {
                    'total_traslados_impuestos_locales': '0.000000',
                    'total_retenciones_impuestos_locales': '77.400000'
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)