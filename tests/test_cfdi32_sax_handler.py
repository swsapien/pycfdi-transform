import unittest
from pycfdi_transform import CFDI32SAXHandler, SchemaHelper
from lxml import etree
import time


class TestCFDI32SAXHandler(unittest.TestCase):
    def test_build_basic_object(self):
        sax_handler = CFDI32SAXHandler()
        self.assertIsNotNone(sax_handler)
        self.assertIsNotNone(sax_handler._config)
        self.assertFalse(sax_handler._config['safe_numerics'])
        self.assertTrue(sax_handler._config['empty_char'] == '')

    def test_transform_file(self):
        sax_handler = CFDI32SAXHandler()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi32/cfdi32_01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi32": {
                "version": "3.2",
                "serie": "Z",
                "folio": "007",
                "fecha": "2017-11-07T23:35:52",
                "no_certificado": "30001000000300023708",
                "subtotal": "1333.00",
                "descuento": "",
                "total": "1546.28",
                "moneda": "MXN",
                "tipo_cambio": "1.0000",
                "tipo_comprobante": "ingreso",
                "metodo_pago": "NA",
                "forma_pago": "Pago en una sola exhibición",
                "condiciones_pago": "",
                "lugar_expedicion": "ZAPOPAN, JALISCO",
                "sello": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                "certificado": "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",
                "emisor": {
                    "rfc": "IIA040805DZ4",
                    "nombre": "MI SUPER CUENTA DE DESSARROLLO",
                    "regimen_fiscal": [
                        "GENERAL DE LEY PERSONAS MORALES",
                        "GENERAL DE LEY PERSONAS MORALES DOBLE REGIMEN"
                    ]
                },
                "receptor": {
                    "rfc": "JILH841117AS9",
                    "nombre": "PUBLICO GENERAL"
                },
                "conceptos": [

                ],
                "impuestos": {
                    "retenciones": [

                    ],
                    "traslados": [
                        {
                            "impuesto": "IVA",
                            "tasa": "16",
                            "importe": "213.28"
                        }
                    ],
                    "total_impuestos_traslados": "",
                    "total_impuestos_retenidos": ""
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd10": [
                {
                    "version": "1.0",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9ECB9AF2-3998-4C1F-BB97-CEB5512F149C",
                    "fecha_timbrado": "2017-11-07T23:40:27",
                    "sello_cfd": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                    "sello_sat": "NBS9jzN9X8XXLa8qX7HAj3Fecl48f8Pzc4GI+QMbM6HEEcsSxfkDZDzpZo8WpcG+YMTmkNe/NALg9zWbb/vQ05iB8OxSh4WJ9r6bZsUXbgJNHjii4D5RIRC2FGMD2NMxaEc3Bc86Lead6Ze8UsmrFzamuCXlCh7+QnVRyBx92PSwYsVhdD4rT56KBoq34oDVoEA19MPlGugh1W+GFDxJJqvtZAjGDMNY6DKX3OwdQP5dTWnf00BS2stoHMj8oNbvvdj8CfJBNZ/5YNYFwsNPeMicBXLX4G3quYMIy6UzcvlxKNSp4PN+uLyLzCXPRkACkoV6cE/3VgvNhn3MgLjcSQ=="
                },
                {
                    "version": "1.0",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9ECB9AF2-3998-4C1F-BB97-CEB5512F149C",
                    "fecha_timbrado": "2017-11-07T23:40:27",
                    "sello_cfd": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                    "sello_sat": "NBS9jzN9X8XXLa8qX7HAj3Fecl48f8Pzc4GI+QMbM6HEEcsSxfkDZDzpZo8WpcG+YMTmkNe/NALg9zWbb/vQ05iB8OxSh4WJ9r6bZsUXbgJNHjii4D5RIRC2FGMD2NMxaEc3Bc86Lead6Ze8UsmrFzamuCXlCh7+QnVRyBx92PSwYsVhdD4rT56KBoq34oDVoEA19MPlGugh1W+GFDxJJqvtZAjGDMNY6DKX3OwdQP5dTWnf00BS2stoHMj8oNbvvdj8CfJBNZ/5YNYFwsNPeMicBXLX4G3quYMIy6UzcvlxKNSp4PN+uLyLzCXPRkACkoV6cE/3VgvNhn3MgLjcSQ=="
                }
            ]
        }

        self.assertDictEqual(cfdi_data, expected_dict)

    def test_transform_file_reusable(self):
        sax_handler = CFDI32SAXHandler()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi32/cfdi32_nomina_01.xml")
        self.assertIsNotNone(cfdi_data)
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi32/cfdi32_01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi32": {
                "version": "3.2",
                "serie": "Z",
                "folio": "007",
                "fecha": "2017-11-07T23:35:52",
                "no_certificado": "30001000000300023708",
                "subtotal": "1333.00",
                "descuento": "",
                "total": "1546.28",
                "moneda": "MXN",
                "tipo_cambio": "1.0000",
                "tipo_comprobante": "ingreso",
                "metodo_pago": "NA",
                "forma_pago": "Pago en una sola exhibición",
                "condiciones_pago": "",
                "lugar_expedicion": "ZAPOPAN, JALISCO",
                "sello": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                "certificado": "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",
                "emisor": {
                    "rfc": "IIA040805DZ4",
                    "nombre": "MI SUPER CUENTA DE DESSARROLLO",
                    "regimen_fiscal": [
                        "GENERAL DE LEY PERSONAS MORALES",
                        "GENERAL DE LEY PERSONAS MORALES DOBLE REGIMEN"
                    ]
                },
                "receptor": {
                    "rfc": "JILH841117AS9",
                    "nombre": "PUBLICO GENERAL"
                },
                "conceptos": [

                ],
                "impuestos": {
                    "retenciones": [

                    ],
                    "traslados": [
                        {
                            "impuesto": "IVA",
                            "tasa": "16",
                            "importe": "213.28"
                        }
                    ],
                    "total_impuestos_traslados": "",
                    "total_impuestos_retenidos": ""
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd10": [
                {
                    "version": "1.0",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9ECB9AF2-3998-4C1F-BB97-CEB5512F149C",
                    "fecha_timbrado": "2017-11-07T23:40:27",
                    "sello_cfd": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                    "sello_sat": "NBS9jzN9X8XXLa8qX7HAj3Fecl48f8Pzc4GI+QMbM6HEEcsSxfkDZDzpZo8WpcG+YMTmkNe/NALg9zWbb/vQ05iB8OxSh4WJ9r6bZsUXbgJNHjii4D5RIRC2FGMD2NMxaEc3Bc86Lead6Ze8UsmrFzamuCXlCh7+QnVRyBx92PSwYsVhdD4rT56KBoq34oDVoEA19MPlGugh1W+GFDxJJqvtZAjGDMNY6DKX3OwdQP5dTWnf00BS2stoHMj8oNbvvdj8CfJBNZ/5YNYFwsNPeMicBXLX4G3quYMIy6UzcvlxKNSp4PN+uLyLzCXPRkACkoV6cE/3VgvNhn3MgLjcSQ=="
                },
                {
                    "version": "1.0",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9ECB9AF2-3998-4C1F-BB97-CEB5512F149C",
                    "fecha_timbrado": "2017-11-07T23:40:27",
                    "sello_cfd": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                    "sello_sat": "NBS9jzN9X8XXLa8qX7HAj3Fecl48f8Pzc4GI+QMbM6HEEcsSxfkDZDzpZo8WpcG+YMTmkNe/NALg9zWbb/vQ05iB8OxSh4WJ9r6bZsUXbgJNHjii4D5RIRC2FGMD2NMxaEc3Bc86Lead6Ze8UsmrFzamuCXlCh7+QnVRyBx92PSwYsVhdD4rT56KBoq34oDVoEA19MPlGugh1W+GFDxJJqvtZAjGDMNY6DKX3OwdQP5dTWnf00BS2stoHMj8oNbvvdj8CfJBNZ/5YNYFwsNPeMicBXLX4G3quYMIy6UzcvlxKNSp4PN+uLyLzCXPRkACkoV6cE/3VgvNhn3MgLjcSQ=="
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)

    def test_transform_file_utf8chars(self):
        sax_handler = CFDI32SAXHandler()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi32/cfdi32_01_utf8chars.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi32": {
                "version": "3.2",
                "serie": "Z",
                "folio": "007",
                "fecha": "2017-11-07T23:35:52",
                "no_certificado": "30001000000300023708",
                "subtotal": "1333.00",
                "descuento": "",
                "total": "1546.28",
                "moneda": "MXN",
                "tipo_cambio": "1.0000",
                "tipo_comprobante": "ingreso",
                "metodo_pago": "NA",
                "forma_pago": "Pago en una sola exhibición",
                "condiciones_pago": "",
                "lugar_expedicion": "ZAPOPAN, JALISCO",
                "sello": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                "certificado": "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",
                "emisor": {
                    "rfc": "IIA040805DZ4",
                    "nombre": "ESCUELÄ KEMPER ÚRGATE SÁ DE CV",
                    "regimen_fiscal": [
                        "GENERAL DE LEY PERSONAS MORALES",
                        "GENERAL DE LEY PERSONAS MORALES DOBLE REGIMEN"
                    ]
                },
                "receptor": {
                    "rfc": "JILH841117AS9",
                    "nombre": "PUBLICO GENERAL"
                },
                "conceptos": [

                ],
                "impuestos": {
                    "retenciones": [

                    ],
                    "traslados": [
                        {
                            "impuesto": "IVA",
                            "tasa": "16",
                            "importe": "213.28"
                        }
                    ],
                    "total_impuestos_traslados": "",
                    "total_impuestos_retenidos": ""
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd10": [
                {
                    "version": "1.0",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9ECB9AF2-3998-4C1F-BB97-CEB5512F149C",
                    "fecha_timbrado": "2017-11-07T23:40:27",
                    "sello_cfd": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                    "sello_sat": "NBS9jzN9X8XXLa8qX7HAj3Fecl48f8Pzc4GI+QMbM6HEEcsSxfkDZDzpZo8WpcG+YMTmkNe/NALg9zWbb/vQ05iB8OxSh4WJ9r6bZsUXbgJNHjii4D5RIRC2FGMD2NMxaEc3Bc86Lead6Ze8UsmrFzamuCXlCh7+QnVRyBx92PSwYsVhdD4rT56KBoq34oDVoEA19MPlGugh1W+GFDxJJqvtZAjGDMNY6DKX3OwdQP5dTWnf00BS2stoHMj8oNbvvdj8CfJBNZ/5YNYFwsNPeMicBXLX4G3quYMIy6UzcvlxKNSp4PN+uLyLzCXPRkACkoV6cE/3VgvNhn3MgLjcSQ=="
                },
                {
                    "version": "1.0",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9ECB9AF2-3998-4C1F-BB97-CEB5512F149C",
                    "fecha_timbrado": "2017-11-07T23:40:27",
                    "sello_cfd": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                    "sello_sat": "NBS9jzN9X8XXLa8qX7HAj3Fecl48f8Pzc4GI+QMbM6HEEcsSxfkDZDzpZo8WpcG+YMTmkNe/NALg9zWbb/vQ05iB8OxSh4WJ9r6bZsUXbgJNHjii4D5RIRC2FGMD2NMxaEc3Bc86Lead6Ze8UsmrFzamuCXlCh7+QnVRyBx92PSwYsVhdD4rT56KBoq34oDVoEA19MPlGugh1W+GFDxJJqvtZAjGDMNY6DKX3OwdQP5dTWnf00BS2stoHMj8oNbvvdj8CfJBNZ/5YNYFwsNPeMicBXLX4G3quYMIy6UzcvlxKNSp4PN+uLyLzCXPRkACkoV6cE/3VgvNhn3MgLjcSQ=="
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)

    def test_transform_file_with_concepts(self):
        sax_handler = CFDI32SAXHandler().use_concepts_cfdi32()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi32/cfdi32_01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi32": {
                "version": "3.2",
                "serie": "Z",
                "folio": "007",
                "fecha": "2017-11-07T23:35:52",
                "no_certificado": "30001000000300023708",
                "subtotal": "1333.00",
                "descuento": "",
                "total": "1546.28",
                "moneda": "MXN",
                "tipo_cambio": "1.0000",
                "tipo_comprobante": "ingreso",
                "metodo_pago": "NA",
                "forma_pago": "Pago en una sola exhibición",
                "condiciones_pago": "",
                "lugar_expedicion": "ZAPOPAN, JALISCO",
                "sello": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                "certificado": "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",
                "emisor": {
                    "rfc": "IIA040805DZ4",
                    "nombre": "MI SUPER CUENTA DE DESSARROLLO",
                    "regimen_fiscal": [
                        "GENERAL DE LEY PERSONAS MORALES",
                        "GENERAL DE LEY PERSONAS MORALES DOBLE REGIMEN"
                    ]
                },
                "receptor": {
                    "rfc": "JILH841117AS9",
                    "nombre": "PUBLICO GENERAL"
                },
                "conceptos": [
                    {
                        "no_identificacion": "UT421511",
                        "cantidad": "1",
                        "unidad": "No Aplica",
                        "descripcion": "123",
                        "valor_unitario": "1333",
                        "importe": "1333.000000"
                    }
                ],
                "impuestos": {
                    "retenciones": [

                    ],
                    "traslados": [
                        {
                            "impuesto": "IVA",
                            "tasa": "16",
                            "importe": "213.28"
                        }
                    ],
                    "total_impuestos_traslados": "",
                    "total_impuestos_retenidos": ""
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd10": [
                {
                    "version": "1.0",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9ECB9AF2-3998-4C1F-BB97-CEB5512F149C",
                    "fecha_timbrado": "2017-11-07T23:40:27",
                    "sello_cfd": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                    "sello_sat": "NBS9jzN9X8XXLa8qX7HAj3Fecl48f8Pzc4GI+QMbM6HEEcsSxfkDZDzpZo8WpcG+YMTmkNe/NALg9zWbb/vQ05iB8OxSh4WJ9r6bZsUXbgJNHjii4D5RIRC2FGMD2NMxaEc3Bc86Lead6Ze8UsmrFzamuCXlCh7+QnVRyBx92PSwYsVhdD4rT56KBoq34oDVoEA19MPlGugh1W+GFDxJJqvtZAjGDMNY6DKX3OwdQP5dTWnf00BS2stoHMj8oNbvvdj8CfJBNZ/5YNYFwsNPeMicBXLX4G3quYMIy6UzcvlxKNSp4PN+uLyLzCXPRkACkoV6cE/3VgvNhn3MgLjcSQ=="
                },
                {
                    "version": "1.0",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9ECB9AF2-3998-4C1F-BB97-CEB5512F149C",
                    "fecha_timbrado": "2017-11-07T23:40:27",
                    "sello_cfd": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                    "sello_sat": "NBS9jzN9X8XXLa8qX7HAj3Fecl48f8Pzc4GI+QMbM6HEEcsSxfkDZDzpZo8WpcG+YMTmkNe/NALg9zWbb/vQ05iB8OxSh4WJ9r6bZsUXbgJNHjii4D5RIRC2FGMD2NMxaEc3Bc86Lead6Ze8UsmrFzamuCXlCh7+QnVRyBx92PSwYsVhdD4rT56KBoq34oDVoEA19MPlGugh1W+GFDxJJqvtZAjGDMNY6DKX3OwdQP5dTWnf00BS2stoHMj8oNbvvdj8CfJBNZ/5YNYFwsNPeMicBXLX4G3quYMIy6UzcvlxKNSp4PN+uLyLzCXPRkACkoV6cE/3VgvNhn3MgLjcSQ=="
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)

    def test_transform_file_safe_numerics(self):
        sax_handler = CFDI32SAXHandler(safe_numerics=True)
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi32/cfdi32_01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi32": {
                "version": "3.2",
                "serie": "Z",
                "folio": "007",
                "fecha": "2017-11-07T23:35:52",
                "no_certificado": "30001000000300023708",
                "subtotal": "1333.00",
                "descuento": "0.00",
                "total": "1546.28",
                "moneda": "MXN",
                "tipo_cambio": "1.0000",
                "tipo_comprobante": "ingreso",
                "metodo_pago": "NA",
                "forma_pago": "Pago en una sola exhibición",
                "condiciones_pago": "",
                "lugar_expedicion": "ZAPOPAN, JALISCO",
                "sello": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                "certificado": "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",
                "emisor": {
                    "rfc": "IIA040805DZ4",
                    "nombre": "MI SUPER CUENTA DE DESSARROLLO",
                    "regimen_fiscal": [
                        "GENERAL DE LEY PERSONAS MORALES",
                        "GENERAL DE LEY PERSONAS MORALES DOBLE REGIMEN"
                    ]
                },
                "receptor": {
                    "rfc": "JILH841117AS9",
                    "nombre": "PUBLICO GENERAL"
                },
                "conceptos": [

                ],
                "impuestos": {
                    "retenciones": [

                    ],
                    "traslados": [
                        {
                            "impuesto": "IVA",
                            "tasa": "16",
                            "importe": "213.28"
                        }
                    ],
                    "total_impuestos_traslados": "0.00",
                    "total_impuestos_retenidos": "0.00"
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd10": [
                {
                    "version": "1.0",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9ECB9AF2-3998-4C1F-BB97-CEB5512F149C",
                    "fecha_timbrado": "2017-11-07T23:40:27",
                    "sello_cfd": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                    "sello_sat": "NBS9jzN9X8XXLa8qX7HAj3Fecl48f8Pzc4GI+QMbM6HEEcsSxfkDZDzpZo8WpcG+YMTmkNe/NALg9zWbb/vQ05iB8OxSh4WJ9r6bZsUXbgJNHjii4D5RIRC2FGMD2NMxaEc3Bc86Lead6Ze8UsmrFzamuCXlCh7+QnVRyBx92PSwYsVhdD4rT56KBoq34oDVoEA19MPlGugh1W+GFDxJJqvtZAjGDMNY6DKX3OwdQP5dTWnf00BS2stoHMj8oNbvvdj8CfJBNZ/5YNYFwsNPeMicBXLX4G3quYMIy6UzcvlxKNSp4PN+uLyLzCXPRkACkoV6cE/3VgvNhn3MgLjcSQ=="
                },
                {
                    "version": "1.0",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9ECB9AF2-3998-4C1F-BB97-CEB5512F149C",
                    "fecha_timbrado": "2017-11-07T23:40:27",
                    "sello_cfd": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                    "sello_sat": "NBS9jzN9X8XXLa8qX7HAj3Fecl48f8Pzc4GI+QMbM6HEEcsSxfkDZDzpZo8WpcG+YMTmkNe/NALg9zWbb/vQ05iB8OxSh4WJ9r6bZsUXbgJNHjii4D5RIRC2FGMD2NMxaEc3Bc86Lead6Ze8UsmrFzamuCXlCh7+QnVRyBx92PSwYsVhdD4rT56KBoq34oDVoEA19MPlGugh1W+GFDxJJqvtZAjGDMNY6DKX3OwdQP5dTWnf00BS2stoHMj8oNbvvdj8CfJBNZ/5YNYFwsNPeMicBXLX4G3quYMIy6UzcvlxKNSp4PN+uLyLzCXPRkACkoV6cE/3VgvNhn3MgLjcSQ=="
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)

    def test_transform_file_with_concepts_bad_description(self):
        sax_handler = CFDI32SAXHandler(esc_delimiters="~").use_concepts_cfdi32()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi32/cfdi32_01_bad_character.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi32": {
                "version": "3.2",
                "serie": "Z",
                "folio": "007",
                "fecha": "2017-11-07T23:35:52",
                "no_certificado": "30001000000300023708",
                "subtotal": "1333.00",
                "descuento": "",
                "total": "1546.28",
                "moneda": "MXN",
                "tipo_cambio": "1.0000",
                "tipo_comprobante": "ingreso",
                "metodo_pago": "NA",
                "forma_pago": "Pago en una sola exhibición",
                "condiciones_pago": "",
                "lugar_expedicion": "ZAPOPAN, JALISCO",
                "sello": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                "certificado": "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",
                "emisor": {
                    "rfc": "IIA040805DZ4",
                    "nombre": "MI SUPER CUENTA DE DESSARROLLO",
                    "regimen_fiscal": [
                        "GENERAL DE LEY PERSONAS MORALES",
                        "GENERAL DE LEY PERSONAS MORALES DOBLE REGIMEN"
                    ]
                },
                "receptor": {
                    "rfc": "JILH841117AS9",
                    "nombre": "PUBLICO GENERAL"
                },
                "conceptos": [
                    {
                        "no_identificacion": "productoInventario",
                        "cantidad": "1",
                        "unidad": "No Aplica",
                        "descripcion": "Este \ Detalle factura",
                        "valor_unitario": "1333",
                        "importe": "1333.000000"
                    }
                ],
                "impuestos": {
                    "retenciones": [

                    ],
                    "traslados": [
                        {
                            "impuesto": "IVA",
                            "tasa": "16",
                            "importe": "213.28"
                        }
                    ],
                    "total_impuestos_traslados": "",
                    "total_impuestos_retenidos": ""
                },
                "complementos": "TimbreFiscalDigital",
                "addendas": ""
            },
            "tfd10": [
                {
                    "version": "1.0",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9ECB9AF2-3998-4C1F-BB97-CEB5512F149C",
                    "fecha_timbrado": "2017-11-07T23:40:27",
                    "sello_cfd": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                    "sello_sat": "NBS9jzN9X8XXLa8qX7HAj3Fecl48f8Pzc4GI+QMbM6HEEcsSxfkDZDzpZo8WpcG+YMTmkNe/NALg9zWbb/vQ05iB8OxSh4WJ9r6bZsUXbgJNHjii4D5RIRC2FGMD2NMxaEc3Bc86Lead6Ze8UsmrFzamuCXlCh7+QnVRyBx92PSwYsVhdD4rT56KBoq34oDVoEA19MPlGugh1W+GFDxJJqvtZAjGDMNY6DKX3OwdQP5dTWnf00BS2stoHMj8oNbvvdj8CfJBNZ/5YNYFwsNPeMicBXLX4G3quYMIy6UzcvlxKNSp4PN+uLyLzCXPRkACkoV6cE/3VgvNhn3MgLjcSQ=="
                },
                {
                    "version": "1.0",
                    "no_certificado_sat": "20001000000300022323",
                    "uuid": "9ECB9AF2-3998-4C1F-BB97-CEB5512F149C",
                    "fecha_timbrado": "2017-11-07T23:40:27",
                    "sello_cfd": "DklIMpsSPtfnZZPQFROaOb5yeJ/Y+ooZE0k3Pyw5u+HLRIHcCPM2QMJYMPqELBHu49khHOlL+Gbz7/lxTKQd2MBu70b48heBi06P/IJecYBwPs/rnzQkrsXaONj1eRHkH/0teSSNi+gqFYr7l0V7JC27Q32aOoGOsaFqPTaDej2jB40LfRa4ypEvUlw1qShTdT9JkBINn4GnpOf3/FSLQ4R6S77Nw5qMEzmlvjGdlmcnCNCShLTx1JAG39vrouRieyrUP/lr4/IM2FBccNndmH4B/WGaXch/zVuG0SVIcw2E8CJQbh+hN2YCsvP7gMxxJodXXPHYn7GgYgNfmEV8VQ==",
                    "sello_sat": "NBS9jzN9X8XXLa8qX7HAj3Fecl48f8Pzc4GI+QMbM6HEEcsSxfkDZDzpZo8WpcG+YMTmkNe/NALg9zWbb/vQ05iB8OxSh4WJ9r6bZsUXbgJNHjii4D5RIRC2FGMD2NMxaEc3Bc86Lead6Ze8UsmrFzamuCXlCh7+QnVRyBx92PSwYsVhdD4rT56KBoq34oDVoEA19MPlGugh1W+GFDxJJqvtZAjGDMNY6DKX3OwdQP5dTWnf00BS2stoHMj8oNbvvdj8CfJBNZ/5YNYFwsNPeMicBXLX4G3quYMIy6UzcvlxKNSp4PN+uLyLzCXPRkACkoV6cE/3VgvNhn3MgLjcSQ=="
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)

    def test_transform_file_global(self):
        start_time = time.time()
        sax_handler = CFDI32SAXHandler()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi32/cfdi32_large_01.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 1.0, 'Too much time to transform global cfdi')
        self.assertIsNotNone(cfdi_data)

    def test_transform_file_with_concepts_global(self):
        start_time = time.time()
        sax_handler = CFDI32SAXHandler().use_concepts_cfdi32()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi32/cfdi32_large_01.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 1.5, 'Too much time to transform global cfdi')
        self.assertIsNotNone(cfdi_data)
        self.assertGreater(len(cfdi_data['cfdi32']['conceptos']), 50000, 'To less concepts')

    # def test_transform_file_with_concepts_validation(self):
    #     start_time = time.time()
    #     schema_validator = SchemaHelper.get_schema_validator_cfdi33()
    #     sax_handler = CFDI32SAXHandler(schema_validator=schema_validator).use_concepts_cfdi33()
    #     cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_01.xml")
    #     total_seconds = time.time() - start_time
    #     self.assertLessEqual(total_seconds, 1, 'Too much time to validate xsd')
    #     self.assertIsNotNone(cfdi_data)
    #     expected_dict = {
    #         'cfdi33': {
    #             'version': '3.3',
    #             'serie': 'VF',
    #             'folio': '001002004',
    #             'fecha': '2020-04-30T22:36:13',
    #             'no_certificado': '30001000000400002434',
    #             'subtotal': '10.00',
    #             'descuento': '',
    #             'total': '11.60',
    #             'moneda': 'MXN',
    #             'tipo_cambio': '',
    #             'tipo_comprobante': 'I',
    #             'metodo_pago': 'PPD',
    #             'forma_pago': '01',
    #             'condiciones_pago': 'NET15',
    #             'lugar_expedicion': '84094',
    #             'sello': 'SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==',
    #             'certificado': 'MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==',
    #             'confirmacion': '',
    #             'emisor': {
    #                 'rfc': 'EKU9003173C9',
    #                 'nombre': 'ESCUELA KEMPER URGATE SA DE CV',
    #                 'regimen_fiscal': '601',
    #             },
    #             'receptor': {
    #                 'rfc': 'XAXX010101000',
    #                 'nombre': 'PUBLICO EN GENERAL',
    #                 'residencia_fiscal': '',
    #                 'num_reg_id_trib': '',
    #                 'uso_cfdi': 'G03',
    #             },
    #             'conceptos': [
    #                 {
    #                     'clave_prod_serv': '01010101',
    #                     'no_identificacion': 'productoInventario',
    #                     'cantidad': '1.0000',
    #                     'clave_unidad': '3G',
    #                     'unidad': '',
    #                     'descripcion': 'Detalle factura',
    #                     'valor_unitario': '10.0000',
    #                     'importe': '10.00',
    #                     'descuento': '',
    #                 }
    #             ],
    #             'impuestos': {
    #                 'retenciones': [],
    #                 'traslados': [
    #                     {
    #                         'impuesto': '002',
    #                         'tipo_factor': 'Tasa',
    #                         'tasa_o_cuota': '0.160000',
    #                         'importe': '1.60'
    #                     }
    #                 ],
    #                 'total_impuestos_traslados': '1.60',
    #                 'total_impuestos_retenidos': '',
    #             },
    #             'complementos': 'TimbreFiscalDigital',
    #             'addendas': '',
    #         },
    #         'tfd11': [
    #             {
    #                 'version': '1.1',
    #                 'no_certificado_sat': '20001000000300022323',
    #                 'uuid': '9D81C696-0401-4F85-B703-6E0D3AFD6056',
    #                 'fecha_timbrado': '2020-05-02T00:36:50',
    #                 'rfc_prov_cert': 'AAA010101AAA',
    #                 'sello_cfd': 'SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==',
    #                 'sello_sat': 'Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=='
    #             }
    #         ]
    #     }
    #     self.assertDictEqual(cfdi_data, expected_dict)
    #
    # def test_transform_file_with_concepts_validation_failing(self):
    #     schema_validator = SchemaHelper.get_schema_validator_cfdi33()
    #     sax_handler = CFDI32SAXHandler(schema_validator=schema_validator).use_concepts_cfdi33()
    #     with self.assertRaises(etree.DocumentInvalid) as context:
    #         sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_bad_structure_01.xml")
    #     exception = context.exception
    #     self.assertIn("Element '{http://www.sat.gob.mx/cfd/3}Comprobante', attribute 'Total': 'abc' is not a valid value of the atomic type '{http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI}t_Importe", str(exception))
    #
    # def test_transform_file_with_concepts_validation_global(self):
    #     start_time = time.time()
    #     schema_validator = SchemaHelper.get_schema_validator_cfdi33()
    #     sax_handler = CFDI32SAXHandler(schema_validator=schema_validator).use_concepts_cfdi33()
    #     cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_large_01.xml")
    #     total_seconds = time.time() - start_time
    #     self.assertLessEqual(total_seconds, 2, 'Too much time to validate xsd')
    #     self.assertIsNotNone(cfdi_data)
    #
    # def test_transform_file_validation_global(self):
    #     start_time = time.time()
    #     schema_validator = SchemaHelper.get_schema_validator_cfdi33()
    #     sax_handler = CFDI32SAXHandler(schema_validator=schema_validator)
    #     cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_large_01.xml")
    #     total_seconds = time.time() - start_time
    #     self.assertLessEqual(total_seconds, 2, 'Too much time to validate xsd')
    #     self.assertIsNotNone(cfdi_data)
    #
    # def test_tranform_file_addenda(self):
    #     sax_handler = CFDI32SAXHandler()
    #     cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_addenda_01.xml")
    #     self.assertIsNotNone(cfdi_data)
    #     expected_dict = {
    #         "cfdi33": {
    #             "version": "3.3",
    #             "serie": "F",
    #             "folio": "00603",
    #             "fecha": "2020-09-03T23:09:59",
    #             "no_certificado": "20001000000300022815",
    #             "subtotal": "1160.00",
    #             "descuento": "",
    #             "total": "1160.00",
    #             "moneda": "MXN",
    #             "tipo_cambio": "1",
    #             "tipo_comprobante": "I",
    #             "metodo_pago": "PUE",
    #             "forma_pago": "01",
    #             "condiciones_pago": "CONTADO",
    #             "lugar_expedicion": "68140",
    #             'sello': 'E3LaMuAYed0QdIalmjpvRFjAVKKzbs2qcLypvut5l5r1fo8YjaJEBQi8APdyT1ZF+XZZhu/BiBo2uKzIbKxKSKyZcEFZ5Jpcs+p5LnbysrY+3niKqwtGYr7U3Pcpo5h4BMl5oTmLcpBZjBUYF+fHY5Zxh5Q1wjogdJAZpWMXBpwjQ9xCPboh4yOTVjIWYIdjHMjcizD5LukRyGii9lkVTRbK/5nvne76F/j870GYOqOAX0CitWhbB+URnL7RTOT5JR9JsmyUsclkjsRXwvCYw4Zfl+dRMB7d9OSM5dQIxLsqA57xzzsZkjUWu5I1E7q9bORkkPN4DNO6a4i/IXSSEQ==',
    #             'certificado': 'MIIFxTCCA62gAwIBAgIUMjAwMDEwMDAwMDAzMDAwMjI4MTUwDQYJKoZIhvcNAQELBQAwggFmMSAwHgYDVQQDDBdBLkMuIDIgZGUgcHJ1ZWJhcyg0MDk2KTEvMC0GA1UECgwmU2VydmljaW8gZGUgQWRtaW5pc3RyYWNpw7NuIFRyaWJ1dGFyaWExODA2BgNVBAsML0FkbWluaXN0cmFjacOzbiBkZSBTZWd1cmlkYWQgZGUgbGEgSW5mb3JtYWNpw7NuMSkwJwYJKoZIhvcNAQkBFhphc2lzbmV0QHBydWViYXMuc2F0LmdvYi5teDEmMCQGA1UECQwdQXYuIEhpZGFsZ28gNzcsIENvbC4gR3VlcnJlcm8xDjAMBgNVBBEMBTA2MzAwMQswCQYDVQQGEwJNWDEZMBcGA1UECAwQRGlzdHJpdG8gRmVkZXJhbDESMBAGA1UEBwwJQ295b2Fjw6FuMRUwEwYDVQQtEwxTQVQ5NzA3MDFOTjMxITAfBgkqhkiG9w0BCQIMElJlc3BvbnNhYmxlOiBBQ0RNQTAeFw0xNjEwMjUyMTUyMTFaFw0yMDEwMjUyMTUyMTFaMIGxMRowGAYDVQQDExFDSU5ERU1FWCBTQSBERSBDVjEaMBgGA1UEKRMRQ0lOREVNRVggU0EgREUgQ1YxGjAYBgNVBAoTEUNJTkRFTUVYIFNBIERFIENWMSUwIwYDVQQtExxMQU43MDA4MTczUjUgLyBGVUFCNzcwMTE3QlhBMR4wHAYDVQQFExUgLyBGVUFCNzcwMTE3TURGUk5OMDkxFDASBgNVBAsUC1BydWViYV9DRkRJMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgvvCiCFDFVaYX7xdVRhp/38ULWto/LKDSZy1yrXKpaqFXqERJWF78YHKf3N5GBoXgzwFPuDX+5kvY5wtYNxx/Owu2shNZqFFh6EKsysQMeP5rz6kE1gFYenaPEUP9zj+h0bL3xR5aqoTsqGF24mKBLoiaK44pXBzGzgsxZishVJVM6XbzNJVonEUNbI25DhgWAd86f2aU3BmOH2K1RZx41dtTT56UsszJls4tPFODr/caWuZEuUvLp1M3nj7Dyu88mhD2f+1fA/g7kzcU/1tcpFXF/rIy93APvkU72jwvkrnprzs+SnG81+/F16ahuGsb2EZ88dKHwqxEkwzhMyTbQIDAQABox0wGzAMBgNVHRMBAf8EAjAAMAsGA1UdDwQEAwIGwDANBgkqhkiG9w0BAQsFAAOCAgEAJ/xkL8I+fpilZP+9aO8n93+20XxVomLJjeSL+Ng2ErL2GgatpLuN5JknFBkZAhxVIgMaTS23zzk1RLtRaYvH83lBH5E+M+kEjFGp14Fne1iV2Pm3vL4jeLmzHgY1Kf5HmeVrrp4PU7WQg16VpyHaJ/eonPNiEBUjcyQ1iFfkzJmnSJvDGtfQK2TiEolDJApYv0OWdm4is9Bsfi9j6lI9/T6MNZ+/LM2L/t72Vau4r7m94JDEzaO3A0wHAtQ97fjBfBiO5M8AEISAV7eZidIl3iaJJHkQbBYiiW2gikreUZKPUX0HmlnIqqQcBJhWKRu6Nqk6aZBTETLLpGrvF9OArV1JSsbdw/ZH+P88RAt5em5/gjwwtFlNHyiKG5w+UFpaZOK3gZP0su0sa6dlPeQ9EL4JlFkGqQCgSQ+NOsXqaOavgoP5VLykLwuGnwIUnuhBTVeDbzpgrg9LuF5dYp/zs+Y9ScJqe5VMAagLSYTShNtN8luV7LvxF9pgWwZdcM7lUwqJmUddCiZqdngg3vzTactMToG16gZA4CWnMgbU4E+r541+FNMpgAZNvs2CiW/eApfaaQojsZEAHDsDv4L5n3M1CC7fYjE/d61aSng1LaO6T1mh+dEfPvLzp7zyzz+UgWMhi5Cs4pcXx1eic5r7uxPoBwcCTt3YI1jKVVnV7/w=',
    #             'confirmacion': '',
    #             "emisor": {
    #                 "rfc": "LAN7008173R5",
    #                 "nombre": "Test Nombre",
    #                 "regimen_fiscal": "601"
    #             },
    #             "receptor": {
    #                 "rfc": "XAXX010101000",
    #                 "nombre": "Test Receptor",
    #                 "residencia_fiscal": "",
    #                 "num_reg_id_trib": "",
    #                 "uso_cfdi": "G03"
    #             },
    #             "conceptos": [],
    #             "impuestos": {
    #                 "retenciones": [],
    #                 "traslados": [
    #                     {
    #                         "impuesto": "002",
    #                         "tipo_factor": "Tasa",
    #                         "tasa_o_cuota": "0.160000",
    #                         "importe": "0.00"
    #                     }
    #                 ],
    #                 "total_impuestos_traslados": "0.00",
    #                 "total_impuestos_retenidos": ""
    #             },
    #             "complementos": "TimbreFiscalDigital",
    #             "addendas": "NombreAdenda xmlAtt"
    #         },
    #         "tfd11": [
    #             {
    #                 "version": "1.1",
    #                 "no_certificado_sat": "30001000000400002495",
    #                 "uuid": "26EB1086-A6F9-4CAD-8DDE-FF73E8FD7E8E",
    #                 "fecha_timbrado": "2020-09-04T22:30:14",
    #                 "rfc_prov_cert": "SPR190613I52",
    #                 "sello_cfd": "E3LaMuAYed0QdIalmjpvRFjAVKKzbs2qcLypvut5l5r1fo8YjaJEBQi8APdyT1ZF+XZZhu/BiBo2uKzIbKxKSKyZcEFZ5Jpcs+p5LnbysrY+3niKqwtGYr7U3Pcpo5h4BMl5oTmLcpBZjBUYF+fHY5Zxh5Q1wjogdJAZpWMXBpwjQ9xCPboh4yOTVjIWYIdjHMjcizD5LukRyGii9lkVTRbK/5nvne76F/j870GYOqOAX0CitWhbB+URnL7RTOT5JR9JsmyUsclkjsRXwvCYw4Zfl+dRMB7d9OSM5dQIxLsqA57xzzsZkjUWu5I1E7q9bORkkPN4DNO6a4i/IXSSEQ==",
    #                 "sello_sat": "E9dnPDyBKpI4RO9K8LEvIDbuRq1OSFTxL88zKfNwVoh5nCTkQDCl9MOUxKu6UDsfRZkOmNLzMMPkpt17Ls+iijbLHnjwSYqtBJWJSznYrQHUIvHK8+Kbp+kxDCDY3bNmD5ZQLCKP0SRtS/+QIg19KEeSx74YHAPTufiphy/dQ4pBzstWxHeyZkAuRqi4iI0j5FqY0//sqtbwiqPmUCxadIIZcKrybldxpqiuEuXWbMm/LDr+53nbz7xOHG6dNDI9SnhEUIExd6Jk6VXF4l4DaqLqvvSiV4KxpQDW3hZ5HPrrD1PjM/52tFKUZb5QQIsmstbipCV4sqF9T15BmGt0sg=="
    #             }
    #         ]
    #     }
    #     self.assertDictEqual(cfdi_data, expected_dict)
    #
    # def test_transform_file_multi_tfd(self):
    #     sax_handler = CFDI32SAXHandler()
    #     cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_multiple_tfd_01.xml")
    #     self.assertIsNotNone(cfdi_data)
    #     expected_dict = {
    #         "cfdi33": {
    #             "version": "3.3",
    #             "serie": "VF",
    #             "folio": "001002004",
    #             "fecha": "2020-04-30T22:36:13",
    #             "no_certificado": "30001000000400002434",
    #             "subtotal": "10.00",
    #             "descuento": "",
    #             "total": "11.60",
    #             "moneda": "MXN",
    #             "tipo_cambio": "",
    #             "tipo_comprobante": "I",
    #             "metodo_pago": "PPD",
    #             "forma_pago": "01",
    #             "condiciones_pago": "NET15",
    #             "lugar_expedicion": "84094",
    #             'sello': 'SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==',
    #             'certificado': 'MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==',
    #             'confirmacion': '',
    #             "emisor": {
    #                 "rfc": "EKU9003173C9",
    #                 "nombre": "ESCUELA KEMPER URGATE SA DE CV",
    #                 "regimen_fiscal": "601"
    #             },
    #             "receptor": {
    #                 "rfc": "XAXX010101000",
    #                 "nombre": "PUBLICO EN GENERAL",
    #                 "residencia_fiscal": "",
    #                 "num_reg_id_trib": "",
    #                 "uso_cfdi": "G03"
    #             },
    #             "conceptos": [],
    #             "impuestos": {
    #                 "retenciones": [],
    #                 "traslados": [
    #                     {
    #                         "impuesto": "002",
    #                         "tipo_factor": "Tasa",
    #                         "tasa_o_cuota": "0.160000",
    #                         "importe": "1.60"
    #                     }
    #                 ],
    #                 "total_impuestos_traslados": "1.60",
    #                 "total_impuestos_retenidos": ""
    #             },
    #             "complementos": "TimbreFiscalDigital",
    #             "addendas": ""
    #         },
    #         "tfd11": [
    #             {
    #                 "version": "1.1",
    #                 "no_certificado_sat": "20001000000300022323",
    #                 "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
    #                 "fecha_timbrado": "2020-05-02T00:36:50",
    #                 "rfc_prov_cert": "AAA010101AAA",
    #                 "sello_cfd": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
    #                 "sello_sat": "Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=="
    #             },
    #             {
    #                 "version": "1.1",
    #                 "no_certificado_sat": "20001000000300022323",
    #                 "uuid": "1D81C696-0401-4F85-B703-6E0D3AFD6056",
    #                 "fecha_timbrado": "2020-05-02T00:36:50",
    #                 "rfc_prov_cert": "AAA010101AAA",
    #                 "sello_cfd": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==",
    #                 "sello_sat": "Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=="
    #             }
    #         ]
    #     }
    #     self.assertDictEqual(cfdi_data, expected_dict)
    #
    # def test_cfdi33_sax_handler_with_spaces(self):
    #     sax_handler = CFDI32SAXHandler()
    #     cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi33/cfdi33_with_spaces.xml')
    #     self.assertIsNotNone(cfdi_data)
    #     # espacios
    #     self.assertTrue(' ' not in str(cfdi_data['cfdi33']['metodo_pago']))
    #     self.assertTrue(' ' not in str(cfdi_data['cfdi33']['forma_pago']))
    #
    #     expected_dict = {
    #         'cfdi33': {
    #             'version': '3.3',
    #             'serie': 'VF',
    #             'folio': '001002004',
    #             'fecha': '2020-04-30T22:36:13',
    #             'no_certificado': '30001000000400002434',
    #             'subtotal': '10.00',
    #             'descuento': '',
    #             'total': '11.60',
    #             'moneda': 'MXN',
    #             'tipo_cambio': '',
    #             'tipo_comprobante': 'I',
    #             'metodo_pago': 'PPD',
    #             'forma_pago': '01',
    #             'condiciones_pago': 'NET15',
    #             'lugar_expedicion': '84094',
    #             'sello': 'SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==',
    #             'certificado': 'MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==',
    #             'confirmacion': '',
    #             'emisor': {
    #                 'rfc': 'EKU9003173C9',
    #                 'nombre': 'ESCUELA KEMPER URGATE SA DE CV',
    #                 'regimen_fiscal': '601',
    #             },
    #             'receptor': {
    #                 'rfc': 'XAXX010101000',
    #                 'nombre': 'PUBLICO EN GENERAL',
    #                 'residencia_fiscal': '',
    #                 'num_reg_id_trib': '',
    #                 'uso_cfdi': 'G03',
    #             },
    #             'conceptos': [],
    #             'impuestos': {
    #                 'retenciones': [],
    #                 'traslados': [
    #                     {
    #                         'impuesto': '002',
    #                         'tipo_factor': 'Tasa',
    #                         'tasa_o_cuota': '0.160000',
    #                         'importe': '1.60'
    #                     }
    #                 ],
    #                 'total_impuestos_traslados': '1.60',
    #                 'total_impuestos_retenidos': '',
    #             },
    #             'complementos': 'TimbreFiscalDigital',
    #             'addendas': '',
    #         },
    #         'tfd11': [
    #             {
    #                 'version': '1.1',
    #                 'no_certificado_sat': '20001000000300022323',
    #                 'uuid': '9D81C696-0401-4F85-B703-6E0D3AFD6056',
    #                 'fecha_timbrado': '2020-05-02T00:36:50',
    #                 'rfc_prov_cert': 'AAA010101AAA',
    #                 'sello_cfd': 'SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw==',
    #                 'sello_sat': 'Agbj2cBP93wu9Tf6M9skOxjMxbDCqjtyr+wJbi8u1qgfLgEnT/Fz9CzYhWFvzPId0W9jn9QQnRRnmRbaE2XELAA9xMKFVUOvLs4IrxU2dabaM63EzsBEXCalWuq9Gm4iej7cPe0f3YAYwPOFyaJKXTXC6NdMXiOE2nITvDgZI/jDMOAIv7F+v+QUXBXq/Z2YrSFmbmvKXJx47wo8P+Qr5o+a1Ot8fPPfx9TOVDNc75tfhw0+QsxvJSyXxt+Yhf/M/ABIwK+jrB2U3umRrSpSvctSCLvfnKRZcrKqGdUn8Tr+BeY7ngpROjPludDB2G507qp09qrlKMaYUUqCkGNNqQ=='
    #             }
    #         ]
    #     }
    #     self.assertDictEqual(cfdi_data, expected_dict)
