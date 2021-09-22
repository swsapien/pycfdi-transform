import unittest
import pycfdi_transform.v2.sax.cfdi33.sax_handler as ct

class TestHanderCfdi33Pagos10Tests(unittest.TestCase):
    def test_transform_file_pagos10(self):
        sax_handler = ct.SAXHandler().use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago_complete.xml')
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': '"',
                'folio': '/>KA',
                'fecha': '2018-01-10T07:22:51.20',
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
            'tfd': [],
            'implocal': [],
            'pagos10': [
                {
                    'pago': [
                        {
                            'fecha_pago': '2005-01-06T06:10:27.07',
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
                                    'IdDocumento': 'BcfEc9ED-e6fE-3a98-13b0-A9c97bEcBcEd',
                                    'Serie': '',
                                    'Folio': '',
                                    'MonedaDR': 'MUR',
                                    'TipoCambioDR': '',
                                    'MetodoDePagoDR': 'PPD',
                                    'NumParcialidad': '',
                                    'ImpSaldoAnt': '',
                                    'ImpPagado': '9752350.234906',
                                    'ImpSaldoInsoluto': '82970.234906'
                                },
                                {
                                    'IdDocumento': 'be6dcDE2-ab9B-7DcF-Aaa2-CB8679f2fa01',
                                    'Serie': '',
                                    'Folio': '',
                                    'MonedaDR': 'HKD',
                                    'TipoCambioDR': '',
                                    'MetodoDePagoDR': 'PPD',
                                    'NumParcialidad': '',
                                    'ImpSaldoAnt': '8563470.234906',
                                    'ImpPagado': '5255780.234906',
                                    'ImpSaldoInsoluto': ''
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
                            'fecha_pago': '1973-04-15T09:02:29.56',
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
                                    'IdDocumento': 'eafcbCE2-Da9c-D0AE-6dd0-eCBeF5422bBe',
                                    'Serie': '',
                                    'Folio': '',
                                    'MonedaDR': 'PYG',
                                    'TipoCambioDR': '',
                                    'MetodoDePagoDR': 'PUE',
                                    'NumParcialidad': '3133',
                                    'ImpSaldoAnt': '2349050.234906',
                                    'ImpPagado': '',
                                    'ImpSaldoInsoluto': '9332080.234906'
                                },
                                {
                                    'IdDocumento': 'B64DDDF2-fECA-fcDe-430d-D1A5F02ea844',
                                    'Serie': '',
                                    'Folio': '',
                                    'MonedaDR': 'MXN',
                                    'TipoCambioDR': '',
                                    'MetodoDePagoDR': 'PPD',
                                    'NumParcialidad': '',
                                    'ImpSaldoAnt': '',
                                    'ImpPagado': '1070880.234906',
                                    'ImpSaldoInsoluto': '6193010.234906'
                                },
                                {
                                    'IdDocumento': '415-53-638204948',
                                    'Serie': '',
                                    'Folio': '',
                                    'MonedaDR': 'PYG',
                                    'TipoCambioDR': '',
                                    'MetodoDePagoDR': 'PPD',
                                    'NumParcialidad': '',
                                    'ImpSaldoAnt': '',
                                    'ImpPagado': '5300650.234906',
                                    'ImpSaldoInsoluto': '1336720.234906'
                                },
                                {
                                    'IdDocumento': 'AB614e3E-8fB7-afce-5Acb-b6B6C332EeEa',
                                    'Serie': '',
                                    'Folio': '',
                                    'MonedaDR': 'CLP',
                                    'TipoCambioDR': '',
                                    'MetodoDePagoDR': 'PPD',
                                    'NumParcialidad': '',
                                    'ImpSaldoAnt': '',
                                    'ImpPagado': '',
                                    'ImpSaldoInsoluto': ''
                                },
                                {
                                    'IdDocumento': 'ebCA4FBe-3b90-daFC-DDCD-a2b6A296DDcD',
                                    'Serie': '',
                                    'Folio': '',
                                    'MonedaDR': 'AWG',
                                    'TipoCambioDR': '',
                                    'MetodoDePagoDR': 'PPD',
                                    'NumParcialidad': '462',
                                    'ImpSaldoAnt': '',
                                    'ImpPagado': '',
                                    'ImpSaldoInsoluto': '6085410.234906'
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
                            'fecha_pago': '2015-08-06T06:10:27.07',
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