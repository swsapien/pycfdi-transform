import unittest
from pycfdi_transform import CFDI40SAXHandler, SchemaHelper
import time

class TestCFDI40SAXHandler(unittest.TestCase):
    def test_build_basic_object(self):
        sax_handler = CFDI40SAXHandler()
        self.assertIsNotNone(sax_handler)
        self.assertIsNotNone(sax_handler._config)
        self.assertFalse(sax_handler._config['safe_numerics'])
        self.assertTrue(sax_handler._config['empty_char'] == '')
    
    def test_transform_file(self):
        sax_handler = CFDI40SAXHandler()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_01.xml")
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
                            "impuesto": "002",
                            "tipo_factor": "Exento",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        },
                        {
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
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_01_large.xml")
        self.assertIsNotNone(cfdi_data)
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_01.xml")
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
                            "impuesto": "002",
                            "tipo_factor": "Exento",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        },
                        {
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
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_01_minimal.xml")
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
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_01_minimal.xml")
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
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_01.xml")
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
                    {
                        "clave_prod_serv": "51101903",
                        "no_identificacion": "~55515",
                        "cantidad": "9253280.234907",
                        "clave_unidad": "A58",
                        "unidad": "",
                        "descripcion": "b!~asdasfg85418816",
                        "valor_unitario": "5835760.234906",
                        "importe": "3916480.234906",
                        "descuento": ""
                    },
                    {
                        "clave_prod_serv": "50321559",
                        "no_identificacion": "/1852821)",
                        "cantidad": "1993740.234907",
                        "clave_unidad": "G55",
                        "unidad": "",
                        "descripcion": "}&~",
                        "valor_unitario": "315930.234906",
                        "importe": "2922160.234906",
                        "descuento": "7520980.234906"
                    },
                    {
                        "clave_prod_serv": "50466301",
                        "no_identificacion": "}r}~&",
                        "cantidad": "5592790.234907",
                        "clave_unidad": "H84",
                        "unidad": "7",
                        "descripcion": "!#{k*",
                        "valor_unitario": "4334580.234906",
                        "importe": "325840.234906",
                        "descuento": ""
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
                        "descuento": ""
                    },
                    {
                        "clave_prod_serv": "10302150",
                        "no_identificacion": "}9}z~}",
                        "cantidad": "52990.234907",
                        "clave_unidad": "XDC",
                        "unidad": "",
                        "descripcion": "dm~}~",
                        "valor_unitario": "8833520.234906",
                        "importe": "6441520.234906",
                        "descuento": ""
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
                            "impuesto": "002",
                            "tipo_factor": "Exento",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        },
                        {
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
    def test_transform_file_with_concepts_bad_description(self):
        sax_handler = CFDI40SAXHandler(esc_delimiters="~").use_concepts_cfdi40()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_01_bad_character.xml")
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
                        "descuento": ""
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
                        "descuento": "7520980.234906"
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
                        "descuento": ""
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
                        "descuento": ""
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
                        "descuento": ""
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
                            "impuesto": "002",
                            "tipo_factor": "Exento",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        },
                        {
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
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_01_large.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 1.0, 'Too much time to transform global cfdi')
        self.assertIsNotNone(cfdi_data)

    def test_transform_file_with_concepts_global(self):
        start_time = time.time()
        sax_handler = CFDI40SAXHandler().use_concepts_cfdi40()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_01_large.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 1.5, 'Too much time to transform global cfdi')
        self.assertIsNotNone(cfdi_data)
        self.assertGreater(len(cfdi_data['cfdi40']['conceptos']), 50000, 'To less concepts')
    
    def test_tranform_file_addenda(self):
        sax_handler = CFDI40SAXHandler()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_01_addenda.xml")
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
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_01_multiple_tfd.xml")
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
                            "impuesto": "002",
                            "tipo_factor": "Exento",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        },
                        {
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
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi40/cfdi40_01.xml')
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
            cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi33/cfdi33_01.xml')
        self.assertTrue("does't have correct namespace for CFDI V4.0" in str(context.exception))

    def test_cfdi40_sax_handler_with_spaces(self):
        sax_handler = CFDI40SAXHandler()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_01_with_spaces.xml")
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
                            "impuesto": "002",
                            "tipo_factor": "Exento",
                            "tasa_o_cuota": "2437280.234906",
                            "importe": "1615450.234906"
                        },
                        {
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