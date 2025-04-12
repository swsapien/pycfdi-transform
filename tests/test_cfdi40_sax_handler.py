import os
import unittest
from pycfdi_transform import CFDI40SAXHandler, SchemaHelper
import time
import json

class TestCFDI40SAXHandler(unittest.TestCase):
    def test_build_basic_object(self):
        sax_handler = CFDI40SAXHandler()
        self.assertIsNotNone(sax_handler)
        self.assertIsNotNone(sax_handler._config)
        self.assertFalse(sax_handler._config['safe_numerics'])
        self.assertTrue(sax_handler._config['empty_char'] == '')
    
    def test_transform_file(self):
        sax_handler = CFDI40SAXHandler()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi40": {
                "version": "4.0",
                "serie": "IFDG~",
                "folio": "41741985~",
                "fecha": "2021-12-01T05:56:56",
                "no_certificado": "30001000000400002434",
                "subtotal": "4959440.234906",
                "descuento": "3308870.234906",
                "total": "6078640.234906",
                "moneda": "IRR",
                "tipo_cambio": "2378590.234907",
                "tipo_comprobante": "I",
                "metodo_pago": "PPD",
                "forma_pago": "01",
                "condiciones_pago": "NET15",
                "exportacion": "01",
                "lugar_expedicion": "45400",
                "sello": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                "certificado": "MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==",
                "confirmacion": "62kpj",
                "emisor": {
                    "rfc": "SKDR690105TM0",
                    "nombre": "ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~",
                    "regimen_fiscal": "624",
                    "fac_atr_adquirente": "6521836835"
                },
                "receptor": {
                    "rfc": "&ÑOZ291130QPA",
                    "nombre": "kghfhg~",
                    "domicilio_fiscal_receptor": "72786",
                    "residencia_fiscal": "VGB",
                    "num_reg_id_trib": "string",
                    "regimen_fiscal_receptor": "603",
                    "uso_cfdi": "I06"
                },
                "conceptos": [],
                "impuestos": {
                    "retenciones": [
                        {
                            "impuesto": "001",
                            "importe": "5246790.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "1904550.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "7118250.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "3272020.234906"
                        },
                        {
                            "impuesto": "002",
                            "importe": "1379300.234906"
                        }
                    ],
                    "traslados": [
                        {
                            "base": "5649040.234906",
                            "impuesto": "002",
                            "tipo_factor": "Exento",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        },
                        {
                            "base": "5649040.234906",
                            "impuesto": "003",
                            "tipo_factor": "Tasa",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        }
                    ],
                    "total_impuestos_traslados": "5376690.234906",
                    "total_impuestos_retenidos": "4307870.234906"
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd11": [
                {
                    "version": "1.1",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
                    "fecha_timbrado": "2020-05-02T00:36:50",
                    "rfc_prov_cert": "AAA010101AAA",
                    "sello_cfd": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                    "sello_sat": "Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=="
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_reusable(self):
        sax_handler = CFDI40SAXHandler()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_01_large.xml")
        self.assertIsNotNone(cfdi_data)
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi40": {
                "version": "4.0",
                "serie": "IFDG~",
                "folio": "41741985~",
                "fecha": "2021-12-01T05:56:56",
                "no_certificado": "30001000000400002434",
                "subtotal": "4959440.234906",
                "descuento": "3308870.234906",
                "total": "6078640.234906",
                "moneda": "IRR",
                "tipo_cambio": "2378590.234907",
                "tipo_comprobante": "I",
                "metodo_pago": "PPD",
                "forma_pago": "01",
                "condiciones_pago": "NET15",
                "exportacion": "01",
                "lugar_expedicion": "45400",
                "sello": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                "certificado": "MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==",
                "confirmacion": "62kpj",
                "emisor": {
                    "rfc": "SKDR690105TM0",
                    "nombre": "ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~",
                    "regimen_fiscal": "624",
                    "fac_atr_adquirente": "6521836835"
                },
                "receptor": {
                    "rfc": "&ÑOZ291130QPA",
                    "nombre": "kghfhg~",
                    "domicilio_fiscal_receptor": "72786",
                    "residencia_fiscal": "VGB",
                    "num_reg_id_trib": "string",
                    "regimen_fiscal_receptor": "603",
                    "uso_cfdi": "I06"
                },
                "conceptos": [],
                "impuestos": {
                    "retenciones": [
                        {
                            "impuesto": "001",
                            "importe": "5246790.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "1904550.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "7118250.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "3272020.234906"
                        },
                        {
                            "impuesto": "002",
                            "importe": "1379300.234906"
                        }
                    ],
                    "traslados": [
                        {
                            "base": "5649040.234906",
                            "impuesto": "002",
                            "tipo_factor": "Exento",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        },
                        {
                            "base": "5649040.234906",
                            "impuesto": "003",
                            "tipo_factor": "Tasa",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        }
                    ],
                    "total_impuestos_traslados": "5376690.234906",
                    "total_impuestos_retenidos": "4307870.234906"
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd11": [
                {
                    "version": "1.1",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
                    "fecha_timbrado": "2020-05-02T00:36:50",
                    "rfc_prov_cert": "AAA010101AAA",
                    "sello_cfd": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                    "sello_sat": "Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=="
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_safe_numerics(self):
        sax_handler = CFDI40SAXHandler(safe_numerics=True)
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_01_minimal.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
                "cfdi40": {
                "version": "4.0",
                "serie": "",
                "folio": "",
                "fecha": "2021-12-01T05:56:56",
                "no_certificado": "30001000000400002434",
                "subtotal": "4959440.234906",
                "descuento": "0.00",
                "total": "6078640.234906",
                "moneda": "IRR",
                "tipo_cambio": "2378590.234907",
                "tipo_comprobante": "I",
                "metodo_pago": "PPD",
                "forma_pago": "01",
                "condiciones_pago": "",
                "exportacion": "01",
                "lugar_expedicion": "45400",
                "sello": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                "certificado": "MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==",
                "confirmacion": "",
                "emisor": {
                    "rfc": "SKDR690105TM0",
                    "nombre": "ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~",
                    "regimen_fiscal": "624",
                    "fac_atr_adquirente": ""
                },
                "receptor": {
                    "rfc": "&ÑOZ291130QPA",
                    "nombre": "kghfhg~",
                    "domicilio_fiscal_receptor": "72786",
                    "residencia_fiscal": "",
                    "num_reg_id_trib": "",
                    "regimen_fiscal_receptor": "603",
                    "uso_cfdi": "I06"
                },
                "conceptos": [],
                "impuestos": {
                    "retenciones": [],
                    "traslados": [],
                    "total_impuestos_traslados": "0.00",
                    "total_impuestos_retenidos": "0.00"
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd11": [
                {
                    "version": "1.1",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
                    "fecha_timbrado": "2020-05-02T00:36:50",
                    "rfc_prov_cert": "AAA010101AAA",
                    "sello_cfd": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                    "sello_sat": "Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=="
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_empty_char(self):
        sax_handler = CFDI40SAXHandler(empty_char='-')
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_01_minimal.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
                "cfdi40": {
                "version": "4.0",
                "serie": "-",
                "folio": "-",
                "fecha": "2021-12-01T05:56:56",
                "no_certificado": "30001000000400002434",
                "subtotal": "4959440.234906",
                "descuento": "-",
                "total": "6078640.234906",
                "moneda": "IRR",
                "tipo_cambio": "2378590.234907",
                "tipo_comprobante": "I",
                "metodo_pago": "PPD",
                "forma_pago": "01",
                "condiciones_pago": "-",
                "exportacion": "01",
                "lugar_expedicion": "45400",
                "sello": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                "certificado": "MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==",
                "confirmacion": "-",
                "emisor": {
                    "rfc": "SKDR690105TM0",
                    "nombre": "ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~",
                    "regimen_fiscal": "624",
                    "fac_atr_adquirente": "-"
                },
                "receptor": {
                    "rfc": "&ÑOZ291130QPA",
                    "nombre": "kghfhg~",
                    "domicilio_fiscal_receptor": "72786",
                    "residencia_fiscal": "-",
                    "num_reg_id_trib": "-",
                    "regimen_fiscal_receptor": "603",
                    "uso_cfdi": "I06"
                },
                "conceptos": [],
                "impuestos": {
                    "retenciones": [],
                    "traslados": [],
                    "total_impuestos_traslados": "-",
                    "total_impuestos_retenidos": "-"
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": "-"
            },
            "tfd11": [
                {
                    "version": "1.1",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
                    "fecha_timbrado": "2020-05-02T00:36:50",
                    "rfc_prov_cert": "AAA010101AAA",
                    "sello_cfd": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                    "sello_sat": "Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=="
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)

    def test_transform_file_with_concepts(self):
        sax_handler = CFDI40SAXHandler().use_concepts_cfdi40()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {'cfdi40': {'version': '4.0', 'serie': 'IFDG~', 'folio': '41741985~', 'fecha': '2021-12-01T05:56:56', 'no_certificado': '30001000000400002434', 'subtotal': '4959440.234906', 'descuento': '3308870.234906', 'total': '6078640.234906', 'moneda': 'IRR', 'tipo_cambio': '2378590.234907', 'tipo_comprobante': 'I', 'metodo_pago': 'PPD', 'forma_pago': '01', 'condiciones_pago': 'NET15', 'exportacion': '01', 'lugar_expedicion': '45400', 'sello': 'SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==', 'certificado': 'MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==', 'confirmacion': '62kpj', 'emisor': {'rfc': 'SKDR690105TM0', 'nombre': 'ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~', 'regimen_fiscal': '624', 'fac_atr_adquirente': '6521836835'}, 'receptor': {'rfc': '&ÑOZ291130QPA', 'nombre': 'kghfhg~', 'domicilio_fiscal_receptor': '72786', 'residencia_fiscal': 'VGB', 'num_reg_id_trib': 'string', 'regimen_fiscal_receptor': '603', 'uso_cfdi': 'I06'}, 'conceptos': [{'clave_prod_serv': '51101903', 'no_identificacion': '~55515', 'cantidad': '9253280.234907', 'clave_unidad': 'A58', 'unidad': '', 'descripcion': 'b!~asdasfg85418816', 'valor_unitario': '5835760.234906', 'importe': '3916480.234906', 'descuento': '', 'objeto_imp': '34', 'terceros': {}}, {'clave_prod_serv': '50321559', 'no_identificacion': '/1852821)', 'cantidad': '1993740.234907', 'clave_unidad': 'G55', 'unidad': '', 'descripcion': '}&~', 'valor_unitario': '315930.234906', 'importe': '2922160.234906', 'descuento': '7520980.234906', 'objeto_imp': '81', 'terceros': {'nombre': '}ni,os', 'rfc': 'ÑÑ&Ñ270414O01', 'domicilioFiscal': '', 'regimenFiscal': ''}}, {'clave_prod_serv': '50466301', 'no_identificacion': '}r}~&', 'cantidad': '5592790.234907', 'clave_unidad': 'H84', 'unidad': '7', 'descripcion': '!#{k*', 'valor_unitario': '4334580.234906', 'importe': '325840.234906', 'descuento': '', 'objeto_imp': '16', 'terceros': {}}, {'clave_prod_serv': '25174800', 'no_identificacion': '', 'cantidad': '577420.234907', 'clave_unidad': 'P28', 'unidad': '', 'descripcion': 'E', 'valor_unitario': '8775650.234906', 'importe': '9380680.234906', 'descuento': '', 'objeto_imp': '13', 'terceros': {'nombre': 'munuiok~efsd8/4589hgrf', 'rfc': 'ÑHD7811238G3', 'domicilioFiscal': '69822', 'regimenFiscal': '630'}}, {'clave_prod_serv': '44102103', 'no_identificacion': '}9}z~}', 'cantidad': '52990.234907', 'clave_unidad': 'XDC', 'unidad': '', 'descripcion': 'dm~}~', 'valor_unitario': '8833520.234906', 'importe': '6441520.234906', 'descuento': '', 'objeto_imp': '00', 'terceros': {}}], 'impuestos': {'retenciones': [{'impuesto': '001', 'importe': '5246790.234906'}, {'impuesto': '001', 'importe': '1904550.234906'}, {'impuesto': '001', 'importe': '7118250.234906'}, {'impuesto': '001', 'importe': '3272020.234906'}, {'impuesto': '002', 'importe': '1379300.234906'}], 'traslados': [{'base': '5649040.234906', 'impuesto': '002', 'tipo_factor': 'Exento', 'tasa_o_cuota': '2437280.234906', 'importe': '1615450.234906'}, {'base': '5649040.234906', 'impuesto': '003', 'tipo_factor': 'Tasa', 'tasa_o_cuota': '2437280.234906', 'importe': '1615450.234906'}], 'total_impuestos_traslados': '5376690.234906', 'total_impuestos_retenidos': '4307870.234906'}, 'complementos': 'TimbreFiscalDigital', 'addendas': ''}, 'tfd11': [{'version': '1.1', 'no_certificado_sat': '20001000000300022323', 'uuid': '9D81C696-0401-4F85-B703-6E0D3AFD6056', 'fecha_timbrado': '2020-05-02T00:36:50', 'rfc_prov_cert': 'AAA010101AAA', 'sello_cfd': 'SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==', 'sello_sat': 'Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=='}]}
        self.assertDictEqual(cfdi_data, expected_dict)
        
    def test_transform_file_with_concepts_with_taxes_01(self):
        sax_handler = CFDI40SAXHandler().use_concepts_cfdi40().use_concepts_with_taxes()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_concepts_with_taxes_01.xml")
        self.assertIsNotNone(cfdi_data)
        
        expected_dict = json.loads('{"cfdi40": {"version": "4.0", "serie": "Arizona", "folio": "89601772", "fecha": "2025-04-08T17:00:21", "no_certificado": "30001000000500003416", "subtotal": "200.00", "descuento": "", "total": "228.00", "moneda": "MXN", "tipo_cambio": "1", "tipo_comprobante": "I", "metodo_pago": "PUE", "forma_pago": "01", "condiciones_pago": "30 d\\u00edas", "exportacion": "01", "lugar_expedicion": "45070", "sello": "TgtJaytwymlqaO/AzrSY8/aAc3OaDqK33j/5HGcuwnTGBPDYwVsxo2Jgk6No5oiXYyvOUfz7TgtIgud/lJPcGdr1nmnNyaC6gq8SKBa3hXTDt0WfYv6eIBzlqMgN3lic8uKzmxIWj2DHE7yKbOSzXHRESr99XW1tdwVOuA5CP0zYwStFpBPE6cqwfMcn+EOAFrSnalmPKnuuzfcuXxrDdYiPQGJoeVBlhe73/IoVyN/8edE+IXECxFaYsw8zAy6b209pxTngJvUzCGPuvSC6/LM9iaFmU/ABJef6WNgr5CvlQHYGNSjuJ+KKRDZH/D5TlRJDD68D6XP+v1ad9IzMgQ==", "certificado": "MIIFsDCCA5igAwIBAgIUMzAwMDEwMDAwMDA1MDAwMDM0MTYwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWxpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMjMwNTE4MTE0MzUxWhcNMjcwNTE4MTE0MzUxWjCB1zEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gVkFEQTgwMDkyN0RKMzEeMBwGA1UEBRMVIC8gVkFEQTgwMDkyN0hTUlNSTDA1MRMwEQYDVQQLEwpTdWN1cnNhbCAxMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtmecO6n2GS0zL025gbHGQVxznPDICoXzR2uUngz4DqxVUC/w9cE6FxSiXm2ap8Gcjg7wmcZfm85EBaxCx/0J2u5CqnhzIoGCdhBPuhWQnIh5TLgj/X6uNquwZkKChbNe9aeFirU/JbyN7Egia9oKH9KZUsodiM/pWAH00PCtoKJ9OBcSHMq8Rqa3KKoBcfkg1ZrgueffwRLws9yOcRWLb02sDOPzGIm/jEFicVYt2Hw1qdRE5xmTZ7AGG0UHs+unkGjpCVeJ+BEBn0JPLWVvDKHZAQMj6s5Bku35+d/MyATkpOPsGT/VTnsouxekDfikJD1f7A1ZpJbqDpkJnss3vQIDAQABox0wGzAMBgNVHRMBAf8EAjAAMAsGA1UdDwQEAwIGwDANBgkqhkiG9w0BAQsFAAOCAgEAFaUgj5PqgvJigNMgtrdXZnbPfVBbukAbW4OGnUhNrA7SRAAfv2BSGk16PI0nBOr7qF2mItmBnjgEwk+DTv8Zr7w5qp7vleC6dIsZFNJoa6ZndrE/f7KO1CYruLXr5gwEkIyGfJ9NwyIagvHHMszzyHiSZIA850fWtbqtythpAliJ2jF35M5pNS+YTkRB+T6L/c6m00ymN3q9lT1rB03YywxrLreRSFZOSrbwWfg34EJbHfbFXpCSVYdJRfiVdvHnewN0r5fUlPtR9stQHyuqewzdkyb5jTTw02D2cUfL57vlPStBj7SEi3uOWvLrsiDnnCIxRMYJ2UA2ktDKHk+zWnsDmaeleSzonv2CHW42yXYPCvWi88oE1DJNYLNkIjua7MxAnkNZbScNw01A6zbLsZ3y8G6eEYnxSTRfwjd8EP4kdiHNJftm7Z4iRU7HOVh79/lRWB+gd171s3d/mI9kte3MRy6V8MMEMCAnMboGpaooYwgAmwclI2XZCczNWXfhaWe0ZS5PmytD/GDpXzkX0oEgY9K/uYo5V77NdZbGAjmyi8cE2B2ogvyaN2XfIInrZPgEffJ4AB7kFA2mwesdLOCh0BLD9itmCve3A1FGR4+stO2ANUoiI3w3Tv2yQSg4bjeDlJ08lXaaFCLW2peEXMXjQUk7fmpb5MNuOUTW6BE=", "confirmacion": "", "emisor": {"rfc": "EKU9003173C9", "nombre": "ESCUELA KEMPER URGATE", "regimen_fiscal": "601", "fac_atr_adquirente": ""}, "receptor": {"rfc": "URE180429TM6", "nombre": "UNIVERSIDAD ROBOTICA ESPA\\u00d1OLA", "domicilio_fiscal_receptor": "86991", "residencia_fiscal": "", "num_reg_id_trib": "", "regimen_fiscal_receptor": "601", "uso_cfdi": "G03"}, "conceptos": [{"clave_prod_serv": "01010101", "no_identificacion": "", "cantidad": "1.000000", "clave_unidad": "EA", "unidad": "PZA", "descripcion": "TEST", "valor_unitario": "100.00", "importe": "100.00", "descuento": "", "objeto_imp": "02", "terceros": {}, "traslados": [{"base": "100.00", "impuesto": "002", "tipo_factor": "Tasa", "tasa_o_cuota": "0.160000", "importe": "16.00"}], "retenciones": [{"impuesto": "002", "importe": "2.00"}]}, {"clave_prod_serv": "01010101", "no_identificacion": "", "cantidad": "1.000000", "clave_unidad": "EA", "unidad": "PZA", "descripcion": "TEST", "valor_unitario": "100.00", "importe": "100.00", "descuento": "", "objeto_imp": "02", "terceros": {}, "traslados": [{"base": "100.00", "impuesto": "002", "tipo_factor": "Tasa", "tasa_o_cuota": "0.160000", "importe": "16.00"}], "retenciones": [{"impuesto": "002", "importe": "2.00"}]}], "impuestos": {"retenciones": [{"impuesto": "002", "importe": "4.00"}], "traslados": [{"base": "200.00", "impuesto": "002", "tipo_factor": "Tasa", "tasa_o_cuota": "0.160000", "importe": "32.00"}], "total_impuestos_traslados": "32.00", "total_impuestos_retenidos": "4.00"}, "complementos": "INE TimbreFiscalDigital", "addendas": ""}, "tfd11": [{"version": "1.1", "no_certificado_sat": "30001000000500003456", "uuid": "81B3DBC2-8A68-4850-9FA5-2D017A98D26F", "fecha_timbrado": "2025-04-08T17:00:22", "rfc_prov_cert": "SPR190613I52", "sello_cfd": "TgtJaytwymlqaO/AzrSY8/aAc3OaDqK33j/5HGcuwnTGBPDYwVsxo2Jgk6No5oiXYyvOUfz7TgtIgud/lJPcGdr1nmnNyaC6gq8SKBa3hXTDt0WfYv6eIBzlqMgN3lic8uKzmxIWj2DHE7yKbOSzXHRESr99XW1tdwVOuA5CP0zYwStFpBPE6cqwfMcn+EOAFrSnalmPKnuuzfcuXxrDdYiPQGJoeVBlhe73/IoVyN/8edE+IXECxFaYsw8zAy6b209pxTngJvUzCGPuvSC6/LM9iaFmU/ABJef6WNgr5CvlQHYGNSjuJ+KKRDZH/D5TlRJDD68D6XP+v1ad9IzMgQ==", "sello_sat": "bl7Qf6fCzyeEJeZ7m4DOHCyBBIfAsKH/p/xrwHDGqtlf7r0gM3WiH0cnsWQCTZIEBCHBAvuK+FPq9nZw5jAJ/Spw6wi6mpaWsSn20/JXrfbgOLA/VoiHM2AP+Y4RZv6RzI3q7tesAhmfPsiviHJiuJ0P8/In/gigugse7wq6/7AcBLsDBUR1bQ9/EBgciF3e/tSw3yViI3RnRNybY5yEtblGcC1/hgA37jsl9EbVhS2t9LNiCIzs3kHYnx16tNy57BdAJmdDEzkDjKP3zzLJaLeDfqLEx07r326jF6A9Wkiao75NAH+ttefUBGic+A8FTJDnADsMVDXFgT/zNkzI0g=="}]}')
        self.assertDictEqual(cfdi_data, expected_dict)
        
    def test_transform_file_with_concepts_with_taxes_02(self):
        sax_handler = CFDI40SAXHandler().use_concepts_cfdi40().use_concepts_with_taxes()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_concepts_with_taxes_02.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = json.loads('{"cfdi40": {"version": "4.0", "serie": "A", "folio": "21", "fecha": "2025-03-06T12:43:41", "no_certificado": "30001000000500003416", "subtotal": "92844.45", "descuento": "", "total": "88511.67", "moneda": "MXN", "tipo_cambio": "", "tipo_comprobante": "I", "metodo_pago": "PUE", "forma_pago": "03", "condiciones_pago": "", "exportacion": "01", "lugar_expedicion": "45070", "sello": "Tn817CCAh2h9p9JqYwuYBWnUapI2c2iqvmig6imDAsuNFZPFrJpyV/x4n8DklEFxs4f5dhthoNrVtaNqDYcNvvjpSAJ+GyV3LERuSYrm0xUcdN4vtNBGcQUgWCNkHaQO6iByy3lvECjLok+bRhKz61uzf+Ua8py7D6cHIhyZuJHEEbtc0GCJanLBhU8GoyvJrm6XSjA+eh36/qqFokkgPP1qfxSZSZKB6RVaE/tj9o0PlOZx+kfArCfcTdRu3KUVGWb5kC5+iv+6ob5ZS0crQMoKKv8tZOX0tXV94VuGrshTKknIf3cPOnmeripCO8PSrdg5ctdPLyAy1sV11LiHJg==", "certificado": "MIIF1TCCA72gAwIBAgIUMDAwMDEwMDAwMDA1MDg4MjQxNjIwDQYJKoZIhvcNAQELBQAwggGEMSAwHgYDVQQDDBdBVVRPUklEQUQgQ0VSVElGSUNBRE9SQTEuMCwGA1UECgwlU0VSVklDSU8gREUgQURNSU5JU1RSQUNJT04gVFJJQlVUQVJJQTEaMBgGA1UECwwRU0FULUlFUyBBdXRob3JpdHkxKjAoBgkqhkiG9w0BCQEWG2NvbnRhY3RvLnRlY25pY29Ac2F0LmdvYi5teDEmMCQGA1UECQwdQVYuIEhJREFMR08gNzcsIENPTC4gR1VFUlJFUk8xDjAMBgNVBBEMBTA2MzAwMQswCQYDVQQGEwJNWDEZMBcGA1UECAwQQ0lVREFEIERFIE1FWElDTzETMBEGA1UEBwwKQ1VBVUhURU1PQzEVMBMGA1UELRMMU0FUOTcwNzAxTk4zMVwwWgYJKoZIhvcNAQkCE01yZXNwb25zYWJsZTogQURNSU5JU1RSQUNJT04gQ0VOVFJBTCBERSBTRVJWSUNJT1MgVFJJQlVUQVJJT1MgQUwgQ09OVFJJQlVZRU5URTAeFw0yMTA4MzExNTM3MjZaFw0yNTA4MzExNTM3MjZaMIGjMRwwGgYDVQQDExNIRVJNRVMgSklNRU5FWiBMVU5BMRwwGgYDVQQpExNIRVJNRVMgSklNRU5FWiBMVU5BMRwwGgYDVQQKExNIRVJNRVMgSklNRU5FWiBMVU5BMRYwFAYDVQQtEw1KSUxIODQxMTE3QVM5MRswGQYDVQQFExJKSUxIODQxMTE3SEpDTU5SMDQxEjAQBgNVBAsTCVByaW5jaXBhbDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAICvIwI3I4TxfGzMTwlbKej9cjzkjvPG6qSGrZLUyASvxEhuSYCCG8FeJmQX6t5et/M1vJvEVCxhlV1DKKc93XWWSbJEOjLir4sU5vx2lmwlXQEH+usgJeoRrvrsbNafJu8QvFBzyiSxnLgDcBxQs8rs+uJmgph2TugyBZ8g0Dx/ZaOUk+RqjVOOchy5wKwRbxq1LHckuxDgt0saQVS1cpyU17nnca4HtXvrEMYRtCGSqEXwfRvLfwkAPZRCeWBjgWU1JVlo8ANLUA7tnYOIwVMdfTxRaPqe5oOUvz1+q98TTnfiNQfsdmJWaPI9yXiu0E1TZjAAZp9rBQajYyLpdPUCAwEAAaMdMBswDAYDVR0TAQH/BAIwADALBgNVHQ8EBAMCBsAwDQYJKoZIhvcNAQELBQADggIBAKhIqwVlke0OeNpJjxkCaw8n58k3c1qOtKbO8IjREv+xa+OF0khOFNRY/LTCKTi5b1HUpnjs41n7OEUQ5J/xgskKDFQ9EdTF8Wf4t1yM0tVATnJRSf7aIbpBgtszDk4QAjPrlMkJdRSiXW6Fz5DsC5dtPzOO+M4KtdR4otbfGBiszr+tO4LthQpVmSSzTx+oeHmgpk9e9EOnBKbZpgp4IlPwCPxEf1xwdDbRGQzdwf+322slsTIn/nXx0hyOypHAKocmSW/DOSbt7KnvymLvA3X8AOktUGybs0jzITfLJzsQ3Le+Bm8jMrrRD0eToQ9imwxU2Q0xeNay9SnIAmmzk09Qw7t3ehnPbgz6KvAqtisYRSwxvL4ehAF7Ka1APxb5ZbbSXcVRIZDla557pv9cX5bgYFJYvYrf4b98go6UnoHMhNRthIZWGNrXB/4joSVyoLf4hMWg+u+Xmo7jVlwuSemo3LeNrWnD4Hp05KHRGK9VxZ3xrUhJS1JpKQQevzZk3EN1VT8WzQ48307nuUFAe1WsrbCBdKP5hFTpkmIykGy0J8i/d2SPBvx8SNdSxkJMC8UZwvtBnZDQsGCnNrS2O5BGVZmPhXDRRUzMG+Xvw9TL96LGFAb7moD/bLv7MxoN7FEx1orzdWXAMOti/cGJMuIlHh3QeLKf4CcXjoaf9FYW", "confirmacion": "", "emisor": {"rfc": "EKU9003173C9", "nombre": "ESCUELA KEMPER URGATE", "regimen_fiscal": "612", "fac_atr_adquirente": ""}, "receptor": {"rfc": "URE180429TM6", "nombre": "UNIVERSIDAD ROBOTICA ESPA\\u00d1OLA", "domicilio_fiscal_receptor": "45027", "residencia_fiscal": "", "num_reg_id_trib": "", "regimen_fiscal_receptor": "601", "uso_cfdi": "G03"}, "conceptos": [{"clave_prod_serv": "81111504", "no_identificacion": "SERVICIO02", "cantidad": "1.00", "clave_unidad": "E48", "unidad": "Servicio", "descripcion": "Servicios de programaci\\u00f3n de aplicaciones", "valor_unitario": "92844.450000", "importe": "92844.450000", "descuento": "", "objeto_imp": "02", "terceros": {}, "traslados": [{"base": "92844.450000", "impuesto": "002", "tipo_factor": "Tasa", "tasa_o_cuota": "0.160000", "importe": "14855.112000"}], "retenciones": [{"impuesto": "001", "importe": "9284.445000"}, {"impuesto": "002", "importe": "9903.438948"}]}], "impuestos": {"retenciones": [{"impuesto": "001", "importe": "9284.45"}, {"impuesto": "002", "importe": "9903.44"}], "traslados": [{"base": "92844.45", "impuesto": "002", "tipo_factor": "Tasa", "tasa_o_cuota": "0.160000", "importe": "14855.11"}], "total_impuestos_traslados": "14855.11", "total_impuestos_retenidos": "19187.89"}, "complementos": "TimbreFiscalDigital", "addendas": ""}, "tfd11": [{"version": "1.1", "no_certificado_sat": "30001000000500003456", "uuid": "81B3DBC2-8A68-4850-9FA5-2D017A98D26F", "fecha_timbrado": "2025-04-08T17:00:22", "rfc_prov_cert": "SPR190613I52", "sello_cfd": "TgtJaytwymlqaO/AzrSY8/aAc3OaDqK33j/5HGcuwnTGBPDYwVsxo2Jgk6No5oiXYyvOUfz7TgtIgud/lJPcGdr1nmnNyaC6gq8SKBa3hXTDt0WfYv6eIBzlqMgN3lic8uKzmxIWj2DHE7yKbOSzXHRESr99XW1tdwVOuA5CP0zYwStFpBPE6cqwfMcn+EOAFrSnalmPKnuuzfcuXxrDdYiPQGJoeVBlhe73/IoVyN/8edE+IXECxFaYsw8zAy6b209pxTngJvUzCGPuvSC6/LM9iaFmU/ABJef6WNgr5CvlQHYGNSjuJ+KKRDZH/D5TlRJDD68D6XP+v1ad9IzMgQ==", "sello_sat": "bl7Qf6fCzyeEJeZ7m4DOHCyBBIfAsKH/p/xrwHDGqtlf7r0gM3WiH0cnsWQCTZIEBCHBAvuK+FPq9nZw5jAJ/Spw6wi6mpaWsSn20/JXrfbgOLA/VoiHM2AP+Y4RZv6RzI3q7tesAhmfPsiviHJiuJ0P8/In/gigugse7wq6/7AcBLsDBUR1bQ9/EBgciF3e/tSw3yViI3RnRNybY5yEtblGcC1/hgA37jsl9EbVhS2t9LNiCIzs3kHYnx16tNy57BdAJmdDEzkDjKP3zzLJaLeDfqLEx07r326jF6A9Wkiao75NAH+ttefUBGic+A8FTJDnADsMVDXFgT/zNkzI0g=="}]}')
        self.assertDictEqual(cfdi_data, expected_dict)


    def test_transform_file_with_terceros(self):
        sax_handler = CFDI40SAXHandler().use_concepts_cfdi40()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/terceros/terceros_40.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {'cfdi40': {'version': '4.0', 'serie': 'Serie', 'folio': '2080427802', 'fecha': '2022-02-08T19:04:49', 'no_certificado': '30001000000400002434', 'subtotal': '200', 'descuento': '', 'total': '180', 'moneda': 'MXN', 'tipo_cambio': '1', 'tipo_comprobante': 'I', 'metodo_pago': 'PPD', 'forma_pago': '99', 'condiciones_pago': 'CondicionesDePago', 'exportacion': '01', 'lugar_expedicion': '20000', 'sello': 'WV2Uxv9/A5dQpfFK/btO5TazhRGVGVS4BRGqceI3ms9Ck/0XxBSP2oSl77StKCXfmUnb5M79v+UND6YAOrj2kJhOFkWfA4le/2nkUD2mORaA5Z16KGMl9RwAfu+Zgd7z7NrL7YFycrmcd3Je2yn3R6PK4VEtLmAtYR4WZu1KWQJunRD0FOUU24JZSVx2RUVfKN5VKtXoHJQKAGVpCeALwCL/7HewMc8MktGSdhraCPUR3eIIB4HHF7P8LIu/CI7N4o7gx673F7Kvp10q10ExqgZX4lgZp0kOBJh2j3SCKWHa2ZPv0J0pWg13C8NHnIlyFd7kQb+AjWYaVGdV+uQXCQ==', 'certificado': 'MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==', 'confirmacion': '', 'emisor': {'rfc': 'EKU9003173C9', 'nombre': 'ESCUELA KEMPER URGATE', 'regimen_fiscal': '601', 'fac_atr_adquirente': ''}, 'receptor': {'rfc': 'URE180429TM6', 'nombre': 'UNIVERSIDAD ROBOTICA ESPAÑOLA', 'domicilio_fiscal_receptor': '65000', 'residencia_fiscal': '', 'num_reg_id_trib': '', 'regimen_fiscal_receptor': '601', 'uso_cfdi': 'G03'}, 'conceptos': [{'clave_prod_serv': '50211503', 'no_identificacion': 'UT421511', 'cantidad': '1', 'clave_unidad': 'H87', 'unidad': 'Pieza', 'descripcion': 'Cigarros', 'valor_unitario': '200.00', 'importe': '200.00', 'descuento': '', 'objeto_imp': '02', 'terceros': {'nombre': 'ADRIANA JUAREZ FERNANDEZ', 'rfc': 'JUFA7608212V6', 'domicilioFiscal': '29133', 'regimenFiscal': '601'}}], 'impuestos': {'retenciones': [{'impuesto': '001', 'importe': '20'}], 'traslados': [], 'total_impuestos_traslados': '', 'total_impuestos_retenidos': '20'}, 'complementos': 'TimbreFiscalDigital', 'addendas': ''}, 'tfd11': [{'version': '1.1', 'no_certificado_sat': '30001000000400002495', 'uuid': 'D69E0C63-8F17-4FB3-9838-D834FD901474', 'fecha_timbrado': '2022-02-09T01:22:19', 'rfc_prov_cert': 'SPR190613I52', 'sello_cfd': 'WV2Uxv9/A5dQpfFK/btO5TazhRGVGVS4BRGqceI3ms9Ck/0XxBSP2oSl77StKCXfmUnb5M79v+UND6YAOrj2kJhOFkWfA4le/2nkUD2mORaA5Z16KGMl9RwAfu+Zgd7z7NrL7YFycrmcd3Je2yn3R6PK4VEtLmAtYR4WZu1KWQJunRD0FOUU24JZSVx2RUVfKN5VKtXoHJQKAGVpCeALwCL/7HewMc8MktGSdhraCPUR3eIIB4HHF7P8LIu/CI7N4o7gx673F7Kvp10q10ExqgZX4lgZp0kOBJh2j3SCKWHa2ZPv0J0pWg13C8NHnIlyFd7kQb+AjWYaVGdV+uQXCQ==', 'sello_sat': 'inshE0vd2KlI6gDTgHs69CYYylgwCc+jzGI8ae+8oGcJHbrTnBe/D8P+GvxVxDmOKh7xCkaitAnQ3A+qco65WY9z29dpZFWBjoeNVJ5P6K7G45OUukcTdxYD29YrbPcdsVa/5e2dzcdSUTpbEEc9etXMudynpvzMx+SrZwVN2ldmxY0v4/1xFsPfGD5Ow719g8GMN9RvyPJZjS5h8rCraFmksz5UCc2JxQUdBm0tlq8uGuOJDoL1F3cn3HIMsFRaOOQm6C4VKxKIfvOvQVzHpRXbdr4RATrOJfi7wYiehsIUYfS/AhSCnlpHPQXCWP1DcZaSufh/8d98DpmEoud2bg=='}]}
        self.assertDictEqual(cfdi_data, expected_dict)
        
    def test_transform_file_with_concepts_bad_description(self):
        sax_handler = CFDI40SAXHandler(esc_delimiters="~").use_concepts_cfdi40()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_01_bad_character.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi40": {
                "version": "4.0",
                "serie": "IFDG",
                "folio": "41741985",
                "fecha": "2021-12-01T05:56:56",
                "no_certificado": "30001000000400002434",
                "subtotal": "4959440.234906",
                "descuento": "3308870.234906",
                "total": "6078640.234906",
                "moneda": "IRR",
                "tipo_cambio": "2378590.234907",
                "tipo_comprobante": "I",
                "metodo_pago": "PPD",
                "forma_pago": "01",
                "condiciones_pago": "NET15",
                "exportacion": "01",
                "lugar_expedicion": "45400",
                "sello": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                "certificado": "MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==",
                "confirmacion": "62kpj",
                "emisor": {
                    "rfc": "SKDR690105TM0",
                    "nombre": "ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}",
                    "regimen_fiscal": "624",
                    "fac_atr_adquirente": "6521836835"
                },
                "receptor": {
                    "rfc": "&ÑOZ291130QPA",
                    "nombre": "PUBLICO EN GENERAL",
                    "domicilio_fiscal_receptor": "72786",
                    "residencia_fiscal": "VGB",
                    "num_reg_id_trib": "string",
                    "regimen_fiscal_receptor": "603",
                    "uso_cfdi": "I06"
                },
                "conceptos": [
                    {
                        "clave_prod_serv": "51101903",
                        "no_identificacion": "55515",
                        "cantidad": "9253280.234907",
                        "clave_unidad": "A58",
                        "unidad": "",
                        "descripcion": "b!asdasfg85418816",
                        "valor_unitario": "5835760.234906",
                        "importe": "3916480.234906",
                        "descuento": "",
                        "objeto_imp": "34",
                        "terceros": {}
                    },
                    {
                        "clave_prod_serv": "50321559",
                        "no_identificacion": "/1852821)",
                        "cantidad": "1993740.234907",
                        "clave_unidad": "G55",
                        "unidad": "",
                        "descripcion": "}&",
                        "valor_unitario": "315930.234906",
                        "importe": "2922160.234906",
                        "descuento": "7520980.234906",
                        "objeto_imp": "81",
                        "terceros": {'nombre': '}ni,os', 'rfc': 'ÑÑ&Ñ270414O01', 'domicilioFiscal': '', 'regimenFiscal': ''}
                    },
                    {
                        "clave_prod_serv": "50466301",
                        "no_identificacion": "}r}&",
                        "cantidad": "5592790.234907",
                        "clave_unidad": "H84",
                        "unidad": "7",
                        "descripcion": "!#{k*",
                        "valor_unitario": "4334580.234906",
                        "importe": "325840.234906",
                        "descuento": "",
                        "objeto_imp": "16",
                        "terceros": {}
                    },
                    {
                        "clave_prod_serv": "25174800",
                        "no_identificacion": "",
                        "cantidad": "577420.234907",
                        "clave_unidad": "P28",
                        "unidad": "",
                        "descripcion": "E",
                        "valor_unitario": "8775650.234906",
                        "importe": "9380680.234906",
                        "descuento": "",
                        "objeto_imp": "13",
                        "terceros": {'nombre': 'munuiokefsd8/4589hgrf', 'rfc': 'ÑHD7811238G3', 'domicilioFiscal': '69822', 'regimenFiscal': '630'}
                    },
                    {
                        "clave_prod_serv": "10302150",
                        "no_identificacion": "}9}z}",
                        "cantidad": "52990.234907",
                        "clave_unidad": "XDC",
                        "unidad": "",
                        "descripcion": "dm}",
                        "valor_unitario": "8833520.234906",
                        "importe": "6441520.234906",
                        "descuento": "",
                        "objeto_imp": "00",
                        "terceros": {}
                    }
                ],
                "impuestos": {
                    "retenciones": [
                        {
                            "impuesto": "001",
                            "importe": "5246790.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "1904550.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "7118250.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "3272020.234906"
                        },
                        {
                            "impuesto": "002",
                            "importe": "1379300.234906"
                        }
                    ],
                    "traslados": [
                        {
                            "base": "5649040.234906",
                            "impuesto": "002",
                            "tipo_factor": "Exento",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        },
                        {
                            "base": "5649040.234906",
                            "impuesto": "003",
                            "tipo_factor": "Tasa",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        }
                    ],
                    "total_impuestos_traslados": "5376690.234906",
                    "total_impuestos_retenidos": "4307870.234906"
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd11": [
                {
                    "version": "1.1",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
                    "fecha_timbrado": "2020-05-02T00:36:50",
                    "rfc_prov_cert": "AAA010101AAA",
                    "sello_cfd": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                    "sello_sat": "Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=="
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_global(self):
        start_time = time.time()
        sax_handler = CFDI40SAXHandler()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_01_large.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 1.0, 'Too much time to transform global cfdi')
        self.assertIsNotNone(cfdi_data)

    def test_transform_file_with_concepts_global(self):
        start_time = time.time()
        sax_handler = CFDI40SAXHandler().use_concepts_cfdi40()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_01_large.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 1.5, 'Too much time to transform global cfdi')
        self.assertIsNotNone(cfdi_data)
        self.assertGreater(len(cfdi_data['cfdi40']['conceptos']), 50000, 'To less concepts')
    
    def test_tranform_file_addenda(self):
        sax_handler = CFDI40SAXHandler()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_01_addenda.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
                "cfdi40": {
                "version": "4.0",
                "serie": "",
                "folio": "",
                "fecha": "2021-12-01T05:56:56",
                "no_certificado": "30001000000400002434",
                "subtotal": "4959440.234906",
                "descuento": "",
                "total": "6078640.234906",
                "moneda": "IRR",
                "tipo_cambio": "2378590.234907",
                "tipo_comprobante": "I",
                "metodo_pago": "PPD",
                "forma_pago": "01",
                "condiciones_pago": "",
                "exportacion": "01",
                "lugar_expedicion": "45400",
                "sello": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                "certificado": "MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==",
                "confirmacion": "",
                "emisor": {
                    "rfc": "SKDR690105TM0",
                    "nombre": "ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~",
                    "regimen_fiscal": "624",
                    "fac_atr_adquirente": ""
                },
                "receptor": {
                    "rfc": "&ÑOZ291130QPA",
                    "nombre": "kghfhg~",
                    "domicilio_fiscal_receptor": "72786",
                    "residencia_fiscal": "",
                    "num_reg_id_trib": "",
                    "regimen_fiscal_receptor": "603",
                    "uso_cfdi": "I06"
                },
                "conceptos": [],
                "impuestos": {
                    "retenciones": [],
                    "traslados": [],
                    "total_impuestos_traslados": "",
                    "total_impuestos_retenidos": ""
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": "NombreAdenda xmlAtt"
            },
            "tfd11": [
                {
                    "version": "1.1",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
                    "fecha_timbrado": "2020-05-02T00:36:50",
                    "rfc_prov_cert": "AAA010101AAA",
                    "sello_cfd": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                    "sello_sat": "Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=="
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_multi_tfd(self):
        sax_handler = CFDI40SAXHandler()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_01_multiple_tfd.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi40": {
                "version": "4.0",
                "serie": "IFDG~",
                "folio": "41741985~",
                "fecha": "2021-12-01T05:56:56",
                "no_certificado": "30001000000400002434",
                "subtotal": "4959440.234906",
                "descuento": "3308870.234906",
                "total": "6078640.234906",
                "moneda": "IRR",
                "tipo_cambio": "2378590.234907",
                "tipo_comprobante": "I",
                "metodo_pago": "PPD",
                "forma_pago": "01",
                "condiciones_pago": "NET15",
                "exportacion": "01",
                "lugar_expedicion": "45400",
                "sello": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                "certificado": "MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==",
                "confirmacion": "62kpj",
                "emisor": {
                    "rfc": "SKDR690105TM0",
                    "nombre": "ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~",
                    "regimen_fiscal": "624",
                    "fac_atr_adquirente": "6521836835"
                },
                "receptor": {
                    "rfc": "&ÑOZ291130QPA",
                    "nombre": "kghfhg~",
                    "domicilio_fiscal_receptor": "72786",
                    "residencia_fiscal": "VGB",
                    "num_reg_id_trib": "string",
                    "regimen_fiscal_receptor": "603",
                    "uso_cfdi": "I06"
                },
                "conceptos": [],
                "impuestos": {
                    "retenciones": [
                        {
                            "impuesto": "001",
                            "importe": "5246790.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "3272020.234906"
                        },
                        {
                            "impuesto": "002",
                            "importe": "1379300.234906"
                        }
                    ],
                    "traslados": [
                        {
                            "base": "5649040.234906",
                            "impuesto": "002",
                            "tipo_factor": "Exento",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        },
                        {
                            "base": "5649040.234906",
                            "impuesto": "003",
                            "tipo_factor": "Tasa",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        }
                    ],
                    "total_impuestos_traslados": "5376690.234906",
                    "total_impuestos_retenidos": "4307870.234906"
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd11": [
                {
                    "version": "1.1",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
                    "fecha_timbrado": "2020-05-02T00:36:50",
                    "rfc_prov_cert": "AAA010101AAA",
                    "sello_cfd": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                    "sello_sat": "Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=="
                },
                {
                    "version": "1.1",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "1D81C696-0401-4F85-B703-6E0D3AFD6056",
                    "fecha_timbrado": "2020-05-02T00:36:50",
                    "rfc_prov_cert": "AAA010101AAA",
                    "sello_cfd": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                    "sello_sat": "Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=="
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_cfdi40_sax_handler_with_break_lines_sellocfd(self):
        sax_handler = CFDI40SAXHandler()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/cfdi40/cfdi40_01.xml')
        self.assertIsNotNone(cfdi_data)
        # sello
        self.assertTrue('\n' not in str(cfdi_data['cfdi40']['sello']))
        self.assertTrue('\r' not in str(cfdi_data['cfdi40']['sello']))
        self.assertTrue('\t' not in str(cfdi_data['cfdi40']['sello']))
        # sello_tfd   
        self.assertTrue('\n' not in str(cfdi_data['tfd11'][0]['sello_cfd']))
        self.assertTrue('\r' not in str(cfdi_data['tfd11'][0]['sello_cfd']))
        self.assertTrue('\t' not in str(cfdi_data['tfd11'][0]['sello_cfd']))
    
    def test_transform_cfdi33(self):
        sax_handler = CFDI40SAXHandler(safe_numerics=True, empty_char='-')
        with self.assertRaises(ValueError) as context:
            cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/cfdi33/cfdi33_01.xml')
        self.assertTrue("does't have correct namespace for CFDI V4.0" in str(context.exception))

    def test_cfdi40_sax_handler_with_spaces(self):
        sax_handler = CFDI40SAXHandler()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_01_with_spaces.xml")
        self.assertIsNotNone(cfdi_data)
        # spaces
        self.assertTrue(' ' not in str(cfdi_data['cfdi40']['metodo_pago']))
        self.assertTrue(' ' not in str(cfdi_data['cfdi40']['forma_pago']))

        expected_dict = {
            "cfdi40": {
                "version": "4.0",
                "serie": "IFDG~",
                "folio": "41741985~",
                "fecha": "2021-12-01T05:56:56",
                "no_certificado": "30001000000400002434",
                "subtotal": "4959440.234906",
                "descuento": "3308870.234906",
                "total": "6078640.234906",
                "moneda": "IRR",
                "tipo_cambio": "2378590.234907",
                "tipo_comprobante": "I",
                "metodo_pago": "PPD",
                "forma_pago": "01",
                "condiciones_pago": "NET15",
                "exportacion": "01",
                "lugar_expedicion": "45400",
                "sello": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                "certificado": "MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==",
                "confirmacion": "62kpj",
                "emisor": {
                    "rfc": "SKDR690105TM0",
                    "nombre": "ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~",
                    "regimen_fiscal": "624",
                    "fac_atr_adquirente": "6521836835"
                },
                "receptor": {
                    "rfc": "&ÑOZ291130QPA",
                    "nombre": "kghfhg~",
                    "domicilio_fiscal_receptor": "72786",
                    "residencia_fiscal": "VGB",
                    "num_reg_id_trib": "string",
                    "regimen_fiscal_receptor": "603",
                    "uso_cfdi": "I06"
                },
                "conceptos": [],
                "impuestos": {
                    "retenciones": [
                        {
                            "impuesto": "001",
                            "importe": "5246790.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "1904550.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "7118250.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "3272020.234906"
                        },
                        {
                            "impuesto": "002",
                            "importe": "1379300.234906"
                        }
                    ],
                    "traslados": [
                        {
                            "base": "5649040.234906",
                            "impuesto": "002",
                            "tipo_factor": "Exento",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        },
                        {
                            "base": "5649040.234906",
                            "impuesto": "003",
                            "tipo_factor": "Tasa",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        }
                    ],
                    "total_impuestos_traslados": "5376690.234906",
                    "total_impuestos_retenidos": "4307870.234906"
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd11": [
                {
                    "version": "1.1",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
                    "fecha_timbrado": "2020-05-02T00:36:50",
                    "rfc_prov_cert": "AAA010101AAA",
                    "sello_cfd": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                    "sello_sat": "Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=="
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
        
    def test_transform_file_with_related_cfdis(self):
        sax_handler = CFDI40SAXHandler().use_related_cfdis()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi40/cfdi40_related_cfdis.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi40": {
                "version": "4.0",
                "serie": "IFDG~",
                "folio": "41741985~",
                "fecha": "2021-12-01T05:56:56",
                "no_certificado": "30001000000400002434",
                "subtotal": "4959440.234906",
                "descuento": "3308870.234906",
                "total": "6078640.234906",
                "moneda": "IRR",
                "tipo_cambio": "2378590.234907",
                "tipo_comprobante": "I",
                "metodo_pago": "PPD",
                "forma_pago": "01",
                "condiciones_pago": "NET15",
                "exportacion": "01",
                "lugar_expedicion": "45400",
                "sello": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                "certificado": "MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==",
                "confirmacion": "62kpj",
                "emisor": {
                    "rfc": "SKDR690105TM0",
                    "nombre": "ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~",
                    "regimen_fiscal": "624",
                    "fac_atr_adquirente": "6521836835"
                },
                "receptor": {
                    "rfc": "&ÑOZ291130QPA",
                    "nombre": "kghfhg~",
                    "domicilio_fiscal_receptor": "72786",
                    "residencia_fiscal": "VGB",
                    "num_reg_id_trib": "string",
                    "regimen_fiscal_receptor": "603",
                    "uso_cfdi": "I06"
                },
                "conceptos": [

                ],
                "impuestos": {
                    "retenciones": [
                        {
                            "impuesto": "001",
                            "importe": "5246790.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "1904550.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "7118250.234906"
                        },
                        {
                            "impuesto": "001",
                            "importe": "3272020.234906"
                        },
                        {
                            "impuesto": "002",
                            "importe": "1379300.234906"
                        }
                    ],
                    "traslados": [
                        {
                            "base": "5649040.234906",
                            "impuesto": "002",
                            "tipo_factor": "Exento",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        },
                        {
                            "base": "5649040.234906",
                            "impuesto": "003",
                            "tipo_factor": "Tasa",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        }
                    ],
                    "total_impuestos_traslados": "5376690.234906",
                    "total_impuestos_retenidos": "4307870.234906"
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": "",
                "cfdis_relacionados": [
                    {
                        "uuid": "CAAB1AFA-AC0D-BDAC-5CCF-AAD448CAFC08",
                        "tipo_relacion": "08"
                    },
                    {
                        "uuid": "2EB04CE0-F1ED-3EBC-B796-38FFE2DFEBEC",
                        "tipo_relacion": "08"
                    },
                    {
                        "uuid": "7FC2BBFD-E7E2-2FAA-39C7-D1DC6CF3FEEE",
                        "tipo_relacion": "08"
                    },
                    {
                        "uuid": "E06CCA24-CC8E-2AD9-906B-38BACCB5CE2D",
                        "tipo_relacion": "08"
                    }
                ]
            },
            "tfd11": [
                {
                    "version": "1.1",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
                    "fecha_timbrado": "2020-05-02T00:36:50",
                    "rfc_prov_cert": "AAA010101AAA",
                    "sello_cfd": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
                    "sello_sat": "Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=="
                }
            ]
        }

        self.assertDictEqual(cfdi_data, expected_dict)
