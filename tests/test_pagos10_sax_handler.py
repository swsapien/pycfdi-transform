from pycfdi_transform import CFDI33SAXHandler, SchemaHelper
from lxml import etree
import unittest

class TestPagos10SAXHandler(unittest.TestCase):
    def test_transform_file_pagos10_complete(self):
        sax_handler = CFDI33SAXHandler().use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago_complete.xml')
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': '"',
                'folio': '/>KA',
                'fecha': '2018-01-10T07:22:51',
                'no_certificado': '47217725691977968749',
                'subtotal': '5858580.234906',
                'descuento': '9061950.234906',
                'total': '7679420.234906',
                'moneda': 'SGD',
                'tipo_cambio': '8016540.234907',
                'tipo_comprobante': 'N',
                'metodo_pago': 'PPD',
                'forma_pago': '01',
                'condiciones_pago': '}_',
                'lugar_expedicion': '45734',
                'sello':'string',
                'certificado':'string',
                'confirmacion':'8p7F3',
                'emisor': {
                    'rfc': 'J&O750807563',
                    'nombre': 'Q~',
                    'regimen_fiscal': '611'
                },
                'receptor': {
                    'rfc': 'ÑÑD68010919A',
                    'nombre': '^*p_',
                    'residencia_fiscal': 'PRI',
                    'num_reg_id_trib': 'string',
                    'uso_cfdi': 'D01'
                },
                'conceptos': [],
                'impuestos': {
                    'retenciones': [
                        {
                            'impuesto': '001',
                            'importe': '1900460.234906'
                        },
                        {
                            'impuesto': '002',
                            'importe': '8425580.234906'
                        },
                        {
                            'impuesto': '003',
                            'importe': '6550940.234906'
                        }
                    ],
                    'traslados': [
                        {
                            'impuesto': '001',
                            'tipo_factor': 'Cuota',
                            'tasa_o_cuota': '5992320.234906',
                            'importe': '3311220.234906'
                        }
                    ],
                    'total_impuestos_traslados': '5553360.234906',
                    'total_impuestos_retenidos': '8065990.234906'
                },
                'complementos': 'Pagos',
                'addendas': ''
            },
            'tfd11': [],
            'pagos10': [
                {
                    'pago': [
                        {
                            'fecha_pago': '2015-01-06T06:10:27',
                            'forma_de_pago_p': '26',
                            'moneda_p': 'XBA',
                            'tipo_cambio_p': '4026190.234907',
                            'monto': '8426440.234906',
                            'num_operacion': '}',
                            'rfc_emisor_cta_ord': '&ÑÑ941216Z6A',
                            'nom_banco_ord_ext': '~',
                            'cta_ordenante': '__LN__5__4',
                            'rfc_emisor_cta_ben': '&&Ñ411106M7A',
                            'cta_beneficiario': '_L_T0DRB_6',
                            'tipo_cad_pago': '01',
                            'cert_pago': 'YTM0NZomIzI2OTsmIzM0NTueYQ==',
                            'cad_pago': 'string',
                            'sello_pago': 'YTM0NZomIzI2OTsmIzM0NTueYQ==',
                            'docto_relacionado': [
                                {
                                    'id_documento': 'BcfEc9ED-e6fE-3a98-13b0-A9c97bEcBcEd',
                                    'serie': '',
                                    'folio': '',
                                    'moneda_dr': 'MUR',
                                    'tipo_cambio_dr': '',
                                    'metodo_de_pago_dr': 'PPD',
                                    'num_parcialidad': '',
                                    'imp_saldo_ant': '',
                                    'imp_pagado': '9752350.234906',
                                    'imp_saldo_insoluto': '82970.234906'
                                },
                                {
                                    'id_documento': 'be6dcDE2-ab9B-7DcF-Aaa2-CB8679f2fa01',
                                    'serie': '',
                                    'folio': 'c!}~r',
                                    'moneda_dr': 'HKD',
                                    'tipo_cambio_dr': '',
                                    'metodo_de_pago_dr': 'PPD',
                                    'num_parcialidad': '',
                                    'imp_saldo_ant': '8563470.234906',
                                    'imp_pagado': '5255780.234906',
                                    'imp_saldo_insoluto': ''
                                }
                            ],
                            'impuestos': [
                                {
                                    'retenciones': [],
                                    'traslados': [
                                        {
                                            'impuesto': '002',
                                            'tipo_factor': 'Tasa',
                                            'tasa_o_cuota': '5129830.234906',
                                            'importe': '6554470.234906'
                                        },
                                        {
                                            'impuesto': '002',
                                            'tipo_factor': 'Tasa',
                                            'tasa_o_cuota': '961040.234906',
                                            'importe': '8886330.234906'
                                        }
                                    ],
                                    'total_impuestos_retenidos': '5031130.234906',
                                    'total_impuestos_trasladados': '1252680.234906'
                                }
                            ]
                        },
                        {
                            'fecha_pago': '2015-04-15T09:02:29',
                            'forma_de_pago_p': '29',
                            'moneda_p': 'BHD',
                            'tipo_cambio_p': '2027230.234907',
                            'monto': '2211890.234906',
                            'num_operacion': '~\\',
                            'rfc_emisor_cta_ord': '&ÑR880531UH8',
                            'nom_banco_ord_ext': '~',
                            'cta_ordenante': 'JS_O33J_3_L3',
                            'rfc_emisor_cta_ben': 'ÑÑX930431318',
                            'cta_beneficiario': 'FV485__M__',
                            'tipo_cad_pago': '01',
                            'cert_pago': 'YTM0NZomIzI2OTsmIzM0NTueYQ==',
                            'cad_pago': 'string',
                            'sello_pago': 'YTM0NZomIzI2OTsmIzM0NTueYQ==',
                            'docto_relacionado': [
                                {
                                    'id_documento': 'eafcbCE2-Da9c-D0AE-6dd0-eCBeF5422bBe',
                                    'serie': '',
                                    'folio': '',
                                    'moneda_dr': 'PYG',
                                    'tipo_cambio_dr': '',
                                    'metodo_de_pago_dr': 'PUE',
                                    'num_parcialidad': '55',
                                    'imp_saldo_ant': '2349050.234906',
                                    'imp_pagado': '',
                                    'imp_saldo_insoluto': '9332080.234906'
                                },
                                {
                                    'id_documento': 'B64DDDF2-fECA-fcDe-430d-D1A5F02ea844',
                                    'serie': 'e',
                                    'folio': '',
                                    'moneda_dr': 'MXN',
                                    'tipo_cambio_dr': '',
                                    'metodo_de_pago_dr': 'PPD',
                                    'num_parcialidad': '',
                                    'imp_saldo_ant': '',
                                    'imp_pagado': '1070880.234906',
                                    'imp_saldo_insoluto': '6193010.234906'
                                },
                                {
                                    'id_documento': '415-53-638204948',
                                    'serie': 'qm3}',
                                    'folio': '',
                                    'moneda_dr': 'PYG',
                                    'tipo_cambio_dr': '',
                                    'metodo_de_pago_dr': 'PPD',
                                    'num_parcialidad': '',
                                    'imp_saldo_ant': '',
                                    'imp_pagado': '5300650.234906',
                                    'imp_saldo_insoluto': '1336720.234906'
                                },
                                {
                                    'id_documento': 'AB614e3E-8fB7-afce-5Acb-b6B6C332EeEa',
                                    'serie': '',
                                    'folio': '',
                                    'moneda_dr': 'CLP',
                                    'tipo_cambio_dr': '',
                                    'metodo_de_pago_dr': 'PPD',
                                    'num_parcialidad': '',
                                    'imp_saldo_ant': '',
                                    'imp_pagado': '',
                                    'imp_saldo_insoluto': ''
                                },
                                {
                                    'id_documento': 'ebCA4FBe-3b90-daFC-DDCD-a2b6A296DDcD',
                                    'serie': '',
                                    'folio': '',
                                    'moneda_dr': 'AWG',
                                    'tipo_cambio_dr': '',
                                    'metodo_de_pago_dr': 'PPD',
                                    'num_parcialidad': '99',
                                    'imp_saldo_ant': '',
                                    'imp_pagado': '',
                                    'imp_saldo_insoluto': '6085410.234906'
                                }
                            ],
                            'impuestos': [
                                {
                                    'retenciones': [],
                                    'traslados': [],
                                    'total_impuestos_retenidos': '',
                                    'total_impuestos_trasladados': '5810390.234906'
                                },
                                {
                                    'retenciones': [
                                        {
                                            'impuesto': '001',
                                            'importe': '3754030.234906'
                                        },
                                        {
                                            'impuesto': '001',
                                            'importe': '1992140.234906'
                                        },
                                        {
                                            'impuesto': '002',
                                            'importe': '7050840.234906'
                                        },
                                        {
                                            'impuesto': '002',
                                            'importe': '401230.234906'
                                        },
                                        {
                                            'impuesto': '001',
                                            'importe': '9557180.234906'
                                        }
                                    ],
                                    'traslados': [
                                        {
                                            'impuesto': '002',
                                            'tipo_factor': 'Tasa',
                                            'tasa_o_cuota': '833200.234906',
                                            'importe': '2251880.234906'
                                        },
                                        {
                                            'impuesto': '003',
                                            'tipo_factor': 'Cuota',
                                            'tasa_o_cuota': '7427110.234906',
                                            'importe': '1682630.234906'
                                        },
                                        {
                                            'impuesto': '003',
                                            'tipo_factor': 'Tasa',
                                            'tasa_o_cuota': '8958170.234906',
                                            'importe': '4763590.234906'
                                        },
                                        {
                                            'impuesto': '001',
                                            'tipo_factor': 'Cuota',
                                            'tasa_o_cuota': '5392680.234906',
                                            'importe': '4104790.234906'
                                        }
                                    ],
                                    'total_impuestos_retenidos': '',
                                    'total_impuestos_trasladados': '3799760.234906'
                                }
                            ]
                        },
                        {
                            'fecha_pago': '2015-08-06T06:10:27',
                            'forma_de_pago_p': '26',
                            'moneda_p': 'MXN',
                            'tipo_cambio_p': '',
                            'monto': '8426440.234906',
                            'num_operacion': '5459',
                            'rfc_emisor_cta_ord': 'AVV941216Z6A',
                            'nom_banco_ord_ext': '',
                            'cta_ordenante': '',
                            'rfc_emisor_cta_ben': '',
                            'cta_beneficiario': '',
                            'tipo_cad_pago': '',
                            'cert_pago': '',
                            'cad_pago': '',
                            'sello_pago': '',
                            'docto_relacionado': [],
                            'impuestos': []
                        }
                    ],
                    'version': '1.0'
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)

    def test_transform_file_pagos10_01(self):
        sax_handler = CFDI33SAXHandler().use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago10_01.xml')
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi33": {
                "version": "3.3",
                "serie": "PA",
                "folio": "1",
                "fecha": "2019-03-29T17:37:19",
                "no_certificado": "00000000000000000000",
                "subtotal": "0",
                "descuento": "",
                "total": "0",
                "moneda": "XXX",
                "tipo_cambio": "",
                "tipo_comprobante": "P",
                "metodo_pago": "",
                "forma_pago": "",
                "condiciones_pago": "",
                "lugar_expedicion": "45110",
                "sello": None,
                "certificado":"",
                "confirmacion":"",
                "emisor": {
                    "rfc": "XAXX010101000",
                    "nombre": "xxx",
                    "regimen_fiscal": "601"
                },
                "receptor": {
                    "rfc": "XAXX010101000",
                    "nombre": "PUBLICO EN GENERAL",
                    "residencia_fiscal": "",
                    "num_reg_id_trib": "",
                    "uso_cfdi": "P01"
                },
                "conceptos": [],
                "impuestos": {
                    "retenciones": [],
                    "traslados": [],
                    'total_impuestos_traslados' :'',
                    'total_impuestos_retenidos' :''
                },
                "complementos": "Pagos TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd11": [
                {
                    "version": "1.1",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "94C4AA76-9DD5-41AD-A10B-267024761951",
                    "fecha_timbrado": "2019-03-29T17:42:38",
                    "rfc_prov_cert": "AAA010101AAA",
                    "sello_cfd": "",
                    "sello_sat": ""
                }
            ],
            "pagos10": [
                {
                    "pago": [
                        {
                            "fecha_pago": "2019-03-29T16:14:52",
                            "forma_de_pago_p": "03",
                            "moneda_p": "MXN",
                            "tipo_cambio_p": "",
                            "monto": "58000.00",
                            "num_operacion": "",
                            "rfc_emisor_cta_ord": "",
                            "nom_banco_ord_ext": "",
                            "cta_ordenante": "",
                            "rfc_emisor_cta_ben": "",
                            "cta_beneficiario": "",
                            "tipo_cad_pago": "",
                            "cert_pago": "",
                            "cad_pago": "",
                            "sello_pago": "",
                            "docto_relacionado": [
                                {
                                    "id_documento": "",
                                    "serie": "i",
                                    "folio": "3463",
                                    "moneda_dr": "MXN",
                                    "tipo_cambio_dr": "",
                                    "metodo_de_pago_dr": "PPD",
                                    "num_parcialidad": "2",
                                    "imp_saldo_ant": "138040.00",
                                    "imp_pagado": "58000.00",
                                    "imp_saldo_insoluto": "80040.00"
                                }
                            ],
                            "impuestos": []
                        }
                    ],
                    "version": "1.0"
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_pagos10_safenumerics_01(self):
        sax_handler = CFDI33SAXHandler(safe_numerics=True).use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago10_01.xml')
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi33": {
                "version": "3.3",
                "serie": "PA",
                "folio": "1",
                "fecha": "2019-03-29T17:37:19",
                "no_certificado": "00000000000000000000",
                "subtotal": "0",
                "descuento": "0.00",
                "total": "0",
                "moneda": "XXX",
                "tipo_cambio": "1.00",
                "tipo_comprobante": "P",
                "metodo_pago": "",
                "forma_pago": "",
                "condiciones_pago": "",
                "lugar_expedicion": "45110",
                "sello": None,
                "certificado":"",
                "confirmacion":"",
                "emisor": {
                    "rfc": "XAXX010101000",
                    "nombre": "xxx",
                    "regimen_fiscal": "601"
                },
                "receptor": {
                    "rfc": "XAXX010101000",
                    "nombre": "PUBLICO EN GENERAL",
                    "residencia_fiscal": "",
                    "num_reg_id_trib": "",
                    "uso_cfdi": "P01"
                },
                "conceptos": [],
                "impuestos": {
                    "retenciones": [],
                    "traslados": [],
                    'total_impuestos_traslados' :'0.00',
                    'total_impuestos_retenidos' :'0.00'
                },
                "complementos": "Pagos TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd11": [
                {
                    "version": "1.1",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "94C4AA76-9DD5-41AD-A10B-267024761951",
                    "fecha_timbrado": "2019-03-29T17:42:38",
                    "rfc_prov_cert": "AAA010101AAA",
                    "sello_cfd": "",
                    "sello_sat": ""
                }
            ],
            "pagos10": [
                {
                    "pago": [
                        {
                            "fecha_pago": "2019-03-29T16:14:52",
                            "forma_de_pago_p": "03",
                            "moneda_p": "MXN",
                            "tipo_cambio_p": "1.00",
                            "monto": "58000.00",
                            "num_operacion": "",
                            "rfc_emisor_cta_ord": "",
                            "nom_banco_ord_ext": "",
                            "cta_ordenante": "",
                            "rfc_emisor_cta_ben": "",
                            "cta_beneficiario": "",
                            "tipo_cad_pago": "",
                            "cert_pago": "",
                            "cad_pago": "",
                            "sello_pago": "",
                            "docto_relacionado": [
                                {
                                    "id_documento": "",
                                    "serie": "i",
                                    "folio": "3463",
                                    "moneda_dr": "MXN",
                                    "tipo_cambio_dr": "1.00",
                                    "metodo_de_pago_dr": "PPD",
                                    "num_parcialidad": "2",
                                    "imp_saldo_ant": "138040.00",
                                    "imp_pagado": "58000.00",
                                    "imp_saldo_insoluto": "80040.00"
                                }
                            ],
                            "impuestos": []
                        }
                    ],
                    "version": "1.0"
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_pagos10_emptychar_01(self):
        sax_handler = CFDI33SAXHandler(empty_char='-').use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago10_01.xml')
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi33": {
                "version": "3.3",
                "serie": "PA",
                "folio": "1",
                "fecha": "2019-03-29T17:37:19",
                "no_certificado": "00000000000000000000",
                "subtotal": "0",
                "descuento": "-",
                "total": "0",
                "moneda": "XXX",
                "tipo_cambio": "-",
                "tipo_comprobante": "P",
                "metodo_pago": "-",
                "forma_pago": "-",
                "condiciones_pago": "-",
                "lugar_expedicion": "45110",
                "sello": None,
                "certificado":"",
                "confirmacion":"-",
                "emisor": {
                    "rfc": "XAXX010101000",
                    "nombre": "xxx",
                    "regimen_fiscal": "601"
                },
                "receptor": {
                    "rfc": "XAXX010101000",
                    "nombre": "PUBLICO EN GENERAL",
                    "residencia_fiscal": "-",
                    "num_reg_id_trib": "-",
                    "uso_cfdi": "P01"
                },
                "conceptos": [],
                "impuestos": {
                    "retenciones": [],
                    "traslados": [],
                    'total_impuestos_traslados' :'-',
                    'total_impuestos_retenidos' :'-'
                },
                "complementos": "Pagos TimbreFiscalDigital",
                "addendas": "-"
            },
            "tfd11": [
                {
                    "version": "1.1",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "94C4AA76-9DD5-41AD-A10B-267024761951",
                    "fecha_timbrado": "2019-03-29T17:42:38",
                    "rfc_prov_cert": "AAA010101AAA",
                    "sello_cfd": "",
                    "sello_sat": ""
                }
            ],
            "pagos10": [
                {
                    "pago": [
                        {
                            "fecha_pago": "2019-03-29T16:14:52",
                            "forma_de_pago_p": "03",
                            "moneda_p": "MXN",
                            "tipo_cambio_p": "-",
                            "monto": "58000.00",
                            "num_operacion": "-",
                            "rfc_emisor_cta_ord": "-",
                            "nom_banco_ord_ext": "-",
                            "cta_ordenante": "-",
                            "rfc_emisor_cta_ben": "-",
                            "cta_beneficiario": "-",
                            "tipo_cad_pago": "-",
                            "cert_pago": "-",
                            "cad_pago": "-",
                            "sello_pago": "-",
                            "docto_relacionado": [
                                {
                                    "id_documento": "",
                                    "serie": "i",
                                    "folio": "3463",
                                    "moneda_dr": "MXN",
                                    "tipo_cambio_dr": "-",
                                    "metodo_de_pago_dr": "PPD",
                                    "num_parcialidad": "2",
                                    "imp_saldo_ant": "138040.00",
                                    "imp_pagado": "58000.00",
                                    "imp_saldo_insoluto": "80040.00"
                                }
                            ],
                            "impuestos": []
                        }
                    ],
                    "version": "1.0"
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_pagos10_complete_validation(self):
        schema_validator = SchemaHelper.get_schema_validator_cfdi33()
        sax_handler = CFDI33SAXHandler(schema_validator=schema_validator).use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago_complete.xml')
        self.assertIsNotNone(cfdi_data)
    
    def test_transform_file_pagos10_broken_validation(self):
        schema_validator = SchemaHelper.get_schema_validator_cfdi33()
        sax_handler = CFDI33SAXHandler(schema_validator=schema_validator).use_pagos10()
        with self.assertRaises(etree.DocumentInvalid) as context:
            sax_handler.transform_from_file('./tests/Resources/pagos10/pago10_broken_01.xml')
        exception = context.exception
        self.assertIn("Element '{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital': This element is not expected. Expected is ( {http://www.sat.gob.mx/Pagos}Pago ).", str(exception), 'Different error expected.')
    
    def test_transform_file_pagos10_broken(self):
        sax_handler = CFDI33SAXHandler().use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago10_broken_01.xml')
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi33": {
                "version": "3.3",
                "serie": "PA",
                "folio": "1",
                "fecha": "2019-03-29T17:37:19",
                "no_certificado": "00000000000000000000",
                "subtotal": "0",
                "descuento": "",
                "total": "0",
                "moneda": "XXX",
                "tipo_cambio": "",
                "tipo_comprobante": "P",
                "metodo_pago": "",
                "forma_pago": "",
                "condiciones_pago": "",
                "lugar_expedicion": "45110",
                "sello": "",
                "certificado":"",
                "confirmacion":"",
                "emisor": {
                    "rfc": "XAXX010101000",
                    "nombre": "xxx",
                    "regimen_fiscal": "601"
                },
                "receptor": {
                    "rfc": "XAXX010101000",
                    "nombre": "PUBLICO EN GENERAL",
                    "residencia_fiscal": "",
                    "num_reg_id_trib": "",
                    "uso_cfdi": "P01"
                },
                "conceptos": [],
                "impuestos": {
                    "retenciones": [],
                    "traslados": [],
                    'total_impuestos_traslados' :'',
                    'total_impuestos_retenidos' :''
                },
                "complementos": "Pagos",
                "addendas": ""
            },
            "tfd11": [],
            "pagos10": [
                {
                    "pago": [
                        {
                            "fecha_pago": "2019-03-29T16:14:52",
                            "forma_de_pago_p": "03",
                            "moneda_p": "MXN",
                            "tipo_cambio_p": "",
                            "monto": "58000.00",
                            "num_operacion": "",
                            "rfc_emisor_cta_ord": "",
                            "nom_banco_ord_ext": "",
                            "cta_ordenante": "",
                            "rfc_emisor_cta_ben": "",
                            "cta_beneficiario": "",
                            "tipo_cad_pago": "",
                            "cert_pago": "",
                            "cad_pago": "",
                            "sello_pago": "",
                            "docto_relacionado": [
                                {
                                    "id_documento": "94c4aa76-9dd5-41ad-a10b-267024761951",
                                    "serie": "i",
                                    "folio": "3463",
                                    "moneda_dr": "MXN",
                                    "tipo_cambio_dr": "",
                                    "metodo_de_pago_dr": "PPD",
                                    "num_parcialidad": "2",
                                    "imp_saldo_ant": "138040.00",
                                    "imp_pagado": "58000.00",
                                    "imp_saldo_insoluto": "80040.00"
                                }
                            ],
                            "impuestos": []
                        }
                    ],
                    "version": "1.0"
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_pagos10_nondr(self):
        sax_handler = CFDI33SAXHandler().use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago10NonDr.xml')
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi33": {
                "version": "3.3",
                "serie": "A",
                "folio": "0013",
                "fecha": "2021-01-18T10:27:16",
                "no_certificado": "0",
                "subtotal": "0",
                "descuento": "",
                "total": "0",
                "moneda": "XXX",
                "tipo_cambio": "",
                "tipo_comprobante": "P",
                "metodo_pago": "",
                "forma_pago": "",
                "condiciones_pago": "",
                "lugar_expedicion": "77536",
                "sello": "",
                "certificado": "",
                "confirmacion": "",
                "emisor": {
                    "rfc": "XAXX010101000",
                    "nombre": "\"xxxxx\"",
                    "regimen_fiscal": "601"
                },
                "receptor": {
                    "rfc": "XAXX010101000",
                    "nombre": "xxxx",
                    "residencia_fiscal": "",
                    "num_reg_id_trib": "",
                    "uso_cfdi": "P01"
                },
                "conceptos": [],
                "impuestos": {
                    "retenciones": [],
                    "traslados": [],
                    'total_impuestos_traslados' :'',
                    'total_impuestos_retenidos' :''
                },
                "complementos": "Pagos TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd11": [
                {
                    "version": "1.1",
                    "no_certificado_sat": "000",
                    "uuid": "000000",
                    "fecha_timbrado": "2021-01-18T10:56:44",
                    "rfc_prov_cert": "ssss",
                    "sello_cfd": "GrDwJ",
                    "sello_sat": "QMsTRNHL..."
                }
            ],
            "pagos10": [
                {
                    "pago": [
                        {
                            "fecha_pago": "2021-01-13T00:00:00",
                            "forma_de_pago_p": "03",
                            "moneda_p": "MXN",
                            "tipo_cambio_p": "",
                            "monto": "35674.83",
                            "num_operacion": "",
                            "rfc_emisor_cta_ord": "",
                            "nom_banco_ord_ext": "",
                            "cta_ordenante": "",
                            "rfc_emisor_cta_ben": "",
                            "cta_beneficiario": "0103271668",
                            "tipo_cad_pago": "01",
                            "cert_pago": "",
                            "cad_pago": "21010007",
                            "sello_pago": "",
                            "docto_relacionado": [],
                            "impuestos": []
                        }
                    ],
                    "version": "1.0"
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)