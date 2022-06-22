import os
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
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi32/cfdi32_01.xml")
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
                    "rfc": "CACX7605101P8",
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
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi32/cfdi32_nomina_01.xml")
        self.assertIsNotNone(cfdi_data)
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi32/cfdi32_01.xml")
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
                    "rfc": "CACX7605101P8",
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
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi32/cfdi32_01_utf8chars.xml")
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
                    "rfc": "CACX7605101P8",
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
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi32/cfdi32_01.xml")
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
                    "rfc": "CACX7605101P8",
                    "nombre": "PUBLICO GENERAL"
                },
                "conceptos": [
                    {
                        "no_identificacion": "UT421511",
                        "cantidad": "1",
                        "unidad": "No Aplica",
                        "descripcion": "123",
                        "valor_unitario": "1333",
                        "importe": "1333.000000",
                        "terceros": {}
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

    def test_transform_file_with_terceros(self):
        sax_handler = CFDI32SAXHandler().use_concepts_cfdi32()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/terceros/terceros11_32.xml')
        self.assertIsNotNone(cfdi_data)
        expected_dict = {'cfdi32': {'version': '3.2', 'serie': 'C', 'folio': '38', 'fecha': '2015-03-05T10:33:52', 'no_certificado': '20001000000100005867', 'subtotal': '35000.00', 'descuento': '0.00', 'total': '40600.00', 'moneda': 'Pesos', 'tipo_cambio': '', 'tipo_comprobante': 'ingreso', 'metodo_pago': 'No Identificado', 'forma_pago': 'PAGO EN UNA SOLA EXHIBICION', 'condiciones_pago': '', 'lugar_expedicion': 'Monterrey, Nuevo León', 'sello': 'YFS5JN8N9mgHA2XjQ7hdlbEiEUaBYAox4kKUsBHrwueUhbIPVww4KHRAmFhQQMLt7pQ/H+Ffvv4kwre/2bL9dZfA7+5YbFmVxWQw1m5QGem8iFCbrc1YoPh1b0aOBUgTzCMWfwGv2hVhSaYyGsrSHsQJ5kAMB+Xoy14sygBcBc0=', 'certificado': 'MIIEdDCCA1ygAwIBAgIUMjAwMDEwMDAwMDAxMDAwMDU4NjcwDQYJKoZIhvcNAQEFBQAwggFvMRgwFgYDVQQDDA9BLkMuIGRlIHBydWViYXMxLzAtBgNVBAoMJlNlcnZpY2lvIGRlIEFkbWluaXN0cmFjacOzbiBUcmlidXRhcmlhMTgwNgYDVQQLDC9BZG1pbmlzdHJhY2nDs24gZGUgU2VndXJpZGFkIGRlIGxhIEluZm9ybWFjacOzbjEpMCcGCSqGSIb3DQEJARYaYXNpc25ldEBwcnVlYmFzLnNhdC5nb2IubXgxJjAkBgNVBAkMHUF2LiBIaWRhbGdvIDc3LCBDb2wuIEd1ZXJyZXJvMQ4wDAYDVQQRDAUwNjMwMDELMAkGA1UEBhMCTVgxGTAXBgNVBAgMEERpc3RyaXRvIEZlZGVyYWwxEjAQBgNVBAcMCUNveW9hY8OhbjEVMBMGA1UELRMMU0FUOTcwNzAxTk4zMTIwMAYJKoZIhvcNAQkCDCNSZXNwb25zYWJsZTogSMOpY3RvciBPcm5lbGFzIEFyY2lnYTAeFw0xMjA3MjcxNzAyMDBaFw0xNjA3MjcxNzAyMDBaMIHbMSkwJwYDVQQDEyBBQ0NFTSBTRVJWSUNJT1MgRU1QUkVTQVJJQUxFUyBTQzEpMCcGA1UEKRMgQUNDRU0gU0VSVklDSU9TIEVNUFJFU0FSSUFMRVMgU0MxKTAnBgNVBAoTIEFDQ0VNIFNFUlZJQ0lPUyBFTVBSRVNBUklBTEVTIFNDMSUwIwYDVQQtExxBQUEwMTAxMDFBQUEgLyBIRUdUNzYxMDAzNFMyMR4wHAYDVQQFExUgLyBIRUdUNzYxMDAzTURGUk5OMDkxETAPBgNVBAsTCFVuaWRhZCAxMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC2TTQSPONBOVxpXv9wLYo8jezBrb34i/tLx8jGdtyy27BcesOav2c1NS/Gdv10u9SkWtwdy34uRAVe7H0a3VMRLHAkvp2qMCHaZc4T8k47Jtb9wrOEh/XFS8LgT4y5OQYo6civfXXdlvxWU/gdM/e6I2lg6FGorP8H4GPAJ/qCNwIDAQABox0wGzAMBgNVHRMBAf8EAjAAMAsGA1UdDwQEAwIGwDANBgkqhkiG9w0BAQUFAAOCAQEATxMecTpMbdhSHo6KVUg4QVF4Op2IBhiMaOrtrXBdJgzGotUFcJgdBCMjtTZXSlq1S4DG1jr8p4NzQlzxsdTxaB8nSKJ4KEMgIT7E62xRUj15jI49qFz7f2uMttZLNThipunsN/NF1XtvESMTDwQFvas/Ugig6qwEfSZc0MDxMpKLEkEePmQwtZD+zXFSMVa6hmOu4M+FzGiRXbj4YJXn9Myjd8xbL/c+9UIcrYoZskxDvMxc6/6M3rNNDY3OFhBK+V/sPMzWWGt8S1yjmtPfXgFs1t65AZ2hcTwTAuHrKwDatJ1ZPfa482ZBROAAX1waz7WwXp0gso7sDCm2/yUVww==', 'emisor': {'rfc': 'AAA010101AAA', 'nombre': 'Empresa de Pruebas SA', 'regimen_fiscal': ['Regimen General de Ley Personas Morales de Prueba']}, 'receptor': {'rfc': 'E&Ñ831019M53', 'nombre': 'Exportadora de Ganado HOLSTEIN S.A.'}, 'conceptos': [{'no_identificacion': '', 'cantidad': '1', 'unidad': 'LTE', 'descripcion': 'Pago por cuenta de terceros', 'valor_unitario': '35000.00', 'importe': '35000.00', 'terceros': {'version': '1.1', 'rfc': 'AAA010101AAA', 'nombre': 'EMPRESA DE PRUEBA S.A. DE C.V.', 'informacionFiscal': {'calle': 'Finisterra', 'noExterior': '750', 'noInterior': '5-B', 'colonia': 'Centro', 'localidad': 'San Luisito', 'referencia': 'Esquina con Insurgentes', 'municipio': 'Monterrey', 'estado': 'Nuevo León', 'pais': 'México', 'codigoPostal': '64000'}, 'cuentaPredial': {'numero': '738212032FD271'}, 'informacionAduanera': {'numero': '', 'fecha': '', 'aduana': ''}, 'impuestos': {'traslados': [{'impuesto': 'IVA', 'tasa': '16.00', 'importe': '0.00'}], 'retenciones': [{'impuesto': 'IVA', 'importe': '0.00'}]}}}], 'impuestos': {'retenciones': [{'impuesto': 'ISR', 'importe': '0.00'}, {'impuesto': 'IVA', 'importe': '0.00'}], 'traslados': [{'impuesto': 'IVA', 'tasa': '16.00', 'importe': '5600.00'}], 'total_impuestos_traslados': '5600.00', 'total_impuestos_retenidos': '0.00'}, 'complementos': 'TimbreFiscalDigital', 'addendas': ''}, 'tfd10': [{'version': '1.0', 'no_certificado_sat': '20001000000100005761', 'uuid': '5D777512-F544-41CE-AA0C-4C36ED254FC8', 'fecha_timbrado': '2015-03-05T10:33:52', 'sello_cfd': 'YFS5JN8N9mgHA2XjQ7hdlbEiEUaBYAox4kKUsBHrwueUhbIPVww4KHRAmFhQQMLt7pQ/H+Ffvv4kwre/2bL9dZfA7+5YbFmVxWQw1m5QGem8iFCbrc1YoPh1b0aOBUgTzCMWfwGv2hVhSaYyGsrSHsQJ5kAMB+Xoy14sygBcBc0=', 'sello_sat': 'FtRoK4ZoBUaH0CPtku4fu5F3FQCevfzDmX+/ZVqzg8pjzf9GmEJgTY9H7BE0g5B4XV5moz30P9OaCVr9keB4lhdxW56JcObXCuOgU67HENVWZlxjRhX5RkLe+RQ4n5OHcbfyUm3ITtAtIZX+JJR0uvPc4jDuKioYRZjJoR4OuVk='}]}
        self.assertDictEqual(cfdi_data, expected_dict)

    def test_transform_file_safe_numerics(self):
        sax_handler = CFDI32SAXHandler(safe_numerics=True)
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi32/cfdi32_01.xml")
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
                    "rfc": "CACX7605101P8",
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
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi32/cfdi32_01_bad_character.xml")
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
                    "rfc": "CACX7605101P8",
                    "nombre": "PUBLICO GENERAL"
                },
                "conceptos": [
                    {
                        "no_identificacion": "productoInventario",
                        "cantidad": "1",
                        "unidad": "No Aplica",
                        "descripcion": "Este \ Detalle factura",
                        "valor_unitario": "1333",
                        "importe": "1333.000000",
                        "terceros": {}
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
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi32/cfdi32_large_01.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 1.0, 'Too much time to transform global cfdi')
        self.assertIsNotNone(cfdi_data)

    def test_transform_file_with_concepts_global(self):
        start_time = time.time()
        sax_handler = CFDI32SAXHandler().use_concepts_cfdi32()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi32/cfdi32_large_01.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 1.5, 'Too much time to transform global cfdi')
        self.assertIsNotNone(cfdi_data)
        self.assertGreater(len(cfdi_data['cfdi32']['conceptos']), 50000, 'To less concepts')

    @unittest.skip("Remains implement schema validator")
    def test_transform_file_with_concepts_validation(self):
        start_time = time.time()
        schema_validator = SchemaHelper.get_schema_validator_cfdi32()
        sax_handler = CFDI32SAXHandler(schema_validator=schema_validator).use_concepts_cfdi32()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi32/cfdi32_01.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 1, 'Too much time to validate xsd')
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
                "certificado": "MIIF+TCCA+GgAwIBAgIUMzAwMDEwMDAwMDAzMDAwMjM3MDgwDQYJKoZIhvcNAQELBQAwggFmMSAwHgYDVQQDDBdBLkMuIDIgZGUgcHJ1ZWJhcyg0MDk2KTEvMC0GA1UECgwmU2VydmljaW8gZGUgQWRtaW5pc3RyYWNpw7NuIFRyaWJ1dGFyaWExODA2BgNVBAsML0FkbWluaXN0cmFjacOzbiBkZSBTZWd1cmlkYWQgZGUgbGEgSW5mb3JtYWNpw7NuMSkwJwYJKoZIhvcNAQkBFhphc2lzbmV0QHBydWViYXMuc2F0LmdvYi5teDEmMCQGA1UECQwdQXYuIEhpZGFsZ28gNzcsIENvbC4gR3VlcnJlcm8xDjAMBgNVBBEMBTA2MzAwMQswCQYDVQQGEwJNWDEZMBcGA1UECAwQRGlzdHJpdG8gRmVkZXJhbDESMBAGA1UEBwwJQ295b2Fjw6FuMRUwEwYDVQQtEwxTQVQ5NzA3MDFOTjMxITAfBgkqhkiG9w0BCQIMElJlc3BvbnNhYmxlOiBBQ0RNQTAeFw0xNzA1MTgwMzU0NTZaFw0yMTA1MTgwMzU0NTZaMIHlMSkwJwYDVQQDEyBBQ0NFTSBTRVJWSUNJT1MgRU1QUkVTQVJJQUxFUyBTQzEpMCcGA1UEKRMgQUNDRU0gU0VSVklDSU9TIEVNUFJFU0FSSUFMRVMgU0MxKTAnBgNVBAoTIEFDQ0VNIFNFUlZJQ0lPUyBFTVBSRVNBUklBTEVTIFNDMSUwIwYDVQQtExxBQUEwMTAxMDFBQUEgLyBIRUdUNzYxMDAzNFMyMR4wHAYDVQQFExUgLyBIRUdUNzYxMDAzTURGUk5OMDkxGzAZBgNVBAsUEkNTRDAxX0FBQTAxMDEwMUFBQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJdUcsHIEIgwivvAantGnYVIO3+7yTdD1tkKopbL+tKSjRFo1ErPdGJxP3gxT5O+ACIDQXN+HS9uMWDYnaURalSIF9COFCdh/OH2Pn+UmkN4culr2DanKztVIO8idXM6c9aHn5hOo7hDxXMC3uOuGV3FS4ObkxTV+9NsvOAV2lMe27SHrSB0DhuLurUbZwXm+/r4dtz3b2uLgBc+Diy95PG+MIu7oNKM89aBNGcjTJw+9k+WzJiPd3ZpQgIedYBD+8QWxlYCgxhnta3k9ylgXKYXCYk0k0qauvBJ1jSRVf5BjjIUbOstaQp59nkgHh45c9gnwJRV618NW0fMeDzuKR0CAwEAAaMdMBswDAYDVR0TAQH/BAIwADALBgNVHQ8EBAMCBsAwDQYJKoZIhvcNAQELBQADggIBABKj0DCNL1lh44y+OcWFrT2icnKF7WySOVihx0oR+HPrWKBMXxo9KtrodnB1tgIx8f+Xjqyphhbw+juDSeDrb99PhC4+E6JeXOkdQcJt50Kyodl9URpCVWNWjUb3F/ypa8oTcff/eMftQZT7MQ1Lqht+xm3QhVoxTIASce0jjsnBTGD2JQ4uT3oCem8bmoMXV/fk9aJ3v0+ZIL42MpY4POGUa/iTaawklKRAL1Xj9IdIR06RK68RS6xrGk6jwbDTEKxJpmZ3SPLtlsmPUTO1kraTPIo9FCmU/zZkWGpd8ZEAAFw+ZfI+bdXBfvdDwaM2iMGTQZTTEgU5KKTIvkAnHo9O45SqSJwqV9NLfPAxCo5eRR2OGibd9jhHe81zUsp5GdE1mZiSqJU82H3cu6BiE+D3YbZeZnjrNSxBgKTIf8w+KNYPM4aWnuUMl0mLgtOxTUXi9MKnUccq3GZLA7bx7Zn211yPRqEjSAqybUMVIOho6aqzkfc3WLZ6LnGU+hyHuZUfPwbnClb7oFFz1PlvGOpNDsUb0qP42QCGBiTUseGugAzqOP6EYpVPC73gFourmdBQgfayaEvi3xjNanFkPlW1XEYNrYJB4yNjphFrvWwTY86vL2o8gZN0Utmc5fnoBTfM9r2zVKmEi6FUeJ1iaDaVNv47te9iS1ai4V4vBY8r",
                "emisor": {
                    "rfc": "IIA040805DZ4",
                    "nombre": "MI SUPER CUENTA DE DESSARROLLO",
                    "regimen_fiscal": [
                        "GENERAL DE LEY PERSONAS MORALES",
                        "GENERAL DE LEY PERSONAS MORALES DOBLE REGIMEN"
                    ]
                },
                "receptor": {
                    "rfc": "CACX7605101P8",
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

    @unittest.skip("Remains implement schema validator")
    def test_transform_file_with_concepts_validation_failing(self):
        schema_validator = SchemaHelper.get_schema_validator_cfdi32()
        sax_handler = CFDI32SAXHandler(schema_validator=schema_validator).use_concepts_cfdi32()
        with self.assertRaises(etree.DocumentInvalid) as context:
            sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi33/cfdi33_bad_structure_01.xml")
        exception = context.exception
        self.assertIn("Element '{http://www.sat.gob.mx/cfd/3}Comprobante', attribute 'Total': 'abc' is not a valid value of the atomic type '{http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI}t_Importe", str(exception))

    @unittest.skip("Remains implement schema validator")
    def test_transform_file_with_concepts_validation_global(self):
        start_time = time.time()
        schema_validator = SchemaHelper.get_schema_validator_cfdi32()
        sax_handler = CFDI32SAXHandler(schema_validator=schema_validator).use_concepts_cfdi32()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi33/cfdi33_large_01.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 2, 'Too much time to validate xsd')
        self.assertIsNotNone(cfdi_data)

    @unittest.skip("Remains implement schema validator")
    def test_transform_file_validation_global(self):
        start_time = time.time()
        schema_validator = SchemaHelper.get_schema_validator_cfdi32()
        sax_handler = CFDI32SAXHandler(schema_validator=schema_validator)
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi33/cfdi33_large_01.xml")
        total_seconds = time.time() - start_time
        self.assertLessEqual(total_seconds, 2, 'Too much time to validate xsd')
        self.assertIsNotNone(cfdi_data)

    def test_tranform_file_addenda(self):
        sax_handler = CFDI32SAXHandler()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + "/Resources/cfdi32/cfdi32_addenda_01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi32': {
                'version': '3.2',
                'serie': 'A',
                'folio': '',
                'fecha': '2014-12-17T08:14:08',
                'no_certificado': None,
                'subtotal': '1603',
                'descuento': '',
                'total': '1603',
                'moneda': 'MXN',
                'tipo_cambio': '',
                'tipo_comprobante': 'ingreso',
                'metodo_pago': 'EFECTIVO',
                'forma_pago': 'PAGO EN UNA SOLA EXHIBICION',
                'condiciones_pago': '',
                'lugar_expedicion': 'VICTORIA TAMPS',
                'sello': None,
                'certificado': None,
                'emisor': {
                    'rfc': 'WATM640917J45',
                    'nombre': 'MARIA WATEMBER TORRES',
                    'regimen_fiscal': [
                        'NO APLICA'
                    ]
                },
                'receptor': {
                    'rfc': 'KIJ0906199R1',
                    'nombre': 'KERNEL INDUSTIA JUGUETERA SA DE CV'
                },
                'conceptos': [

                ],
                'impuestos': {
                    'retenciones': [

                    ],
                    'traslados': [

                    ],
                    'total_impuestos_traslados': '0',
                    'total_impuestos_retenidos': ''
                },
                'complementos': '',
                'addendas': 'Documento'
            },
            'tfd10': [

            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
