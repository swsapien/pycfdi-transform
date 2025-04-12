import os

from pycfdi_transform import CFDI40SAXHandler
from pycfdi_transform.formatters.concepts.efisco_concepts_detail_with_taxes_formatter import EfiscoConceptsDetailWithTaxesFormatter
import unittest
import time


class TestEfiscoConceptsFormatter(unittest.TestCase):

    def test_columns_names_concepts(self):
        columns_expected = [
            "VERSION",
            "SERIE",
            "FOLIO",
            "FECHA",
            "NOCERTIFICADO",
            "SUBTOTAL",
            "DESCUENTO",
            "TOTAL",
            "MONEDA",
            "TIPOCAMBIO",
            "TIPODECOMPROBANTE",
            "METODOPAGO",
            "FORMAPAGO",
            "CONDICIONESDEPAGO",
            "LUGAREXPEDICION",
            "EMISORRFC",
            "EMISORNOMBRE",
            "EMISORREGIMENFISCAL",
            "RECEPTORRFC",
            "RECEPTORNOMBRE",
            "RECEPTORUSOCFDI",
            "RECEPTORDOMICILIOFISCAL",
            "RECEPTORREGIMENFISCAL",
            "UUID",
            "FECHATIMBRADO",
            "C_ID",
            "C_CLAVEPRODSERV",
            "C_NOIDENTIFICACION",
            "C_CANTIDAD",
            "C_CLAVEUNIDAD",
            "C_UNIDAD",
            "C_DESCRIPCION",
            "C_VALORUNITARIO",
            "C_DESCUENTO",
            "C_IMPORTE",
            "TERCERONOMBRE",
            "TERCERORFC",
            "TOTAL_IMPUESTOS_TRASLADOS",
            "TOTAL_IMPUESTOS_RETENCIONES",
        ]
        self.assertListEqual(columns_expected, EfiscoConceptsDetailWithTaxesFormatter.get_columns_names())

    def test_formatter_concepts_cfdi_40_with_taxes_01(self):
        start = time.time()
        sax_handler = CFDI40SAXHandler().use_concepts_cfdi40().use_concepts_with_taxes()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/cfdi40/cfdi40_concepts_with_taxes_01.xml')
        expected_columns = [["4.0", "Arizona", "89601772", "2025-04-08T17:00:21", "30001000000500003416", "200.00", "", "228.00", "MXN", "1", "I", "PUE", "01", "30 días", "45070", "EKU9003173C9", "ESCUELA KEMPER URGATE", "601", "URE180429TM6", "UNIVERSIDAD ROBOTICA ESPAÑOLA", "G03", "86991", "601", "81B3DBC2-8A68-4850-9FA5-2D017A98D26F", "2025-04-08T17:00:22", 1, "01010101", "", "1.000000", "EA", "PZA", "TEST", "100.00", "", "100.00", "", "", "16.0", "2.0"], ["4.0", "Arizona", "89601772", "2025-04-08T17:00:21", "30001000000500003416", "200.00", "", "228.00", "MXN", "1", "I", "PUE", "01", "30 días", "45070", "EKU9003173C9", "ESCUELA KEMPER URGATE", "601", "URE180429TM6", "UNIVERSIDAD ROBOTICA ESPAÑOLA", "G03", "86991", "601", "81B3DBC2-8A68-4850-9FA5-2D017A98D26F", "2025-04-08T17:00:22", 2, "01010101", "", "1.000000", "EA", "PZA", "TEST", "100.00", "", "100.00", "", "", "16.0", "2.0"]]
        formatter = EfiscoConceptsDetailWithTaxesFormatter(cfdi_data)
        result_columns = formatter.dict_to_columns()
        print(result_columns)
        end_time = time.time() - start
        self.assertListEqual(expected_columns, result_columns)
        self.assertLess(end_time, 0.01)
        
    
    def test_formatter_concepts_cfdi_40_with_taxes_02(self):
        start = time.time()
        sax_handler = CFDI40SAXHandler().use_concepts_cfdi40().use_concepts_with_taxes()
        cfdi_data = sax_handler.transform_from_file(os.path.dirname(__file__) + '/Resources/cfdi40/cfdi40_concepts_with_taxes_02.xml')
        expected_columns = [["4.0", "A", "21", "2025-03-06T12:43:41", "30001000000500003416", "92844.45", "", "88511.67", "MXN", "", "I", "PUE", "03", "", "45070", "EKU9003173C9", "ESCUELA KEMPER URGATE", "612", "URE180429TM6", "UNIVERSIDAD ROBOTICA ESPAÑOLA", "G03", "45027", "601", "81B3DBC2-8A68-4850-9FA5-2D017A98D26F", "2025-04-08T17:00:22", 1, "81111504", "SERVICIO02", "1.00", "E48", "Servicio", "Servicios de programación de aplicaciones", "92844.450000", "", "92844.450000", "", "", "14855.112", "19187.883948000002"]]
        formatter = EfiscoConceptsDetailWithTaxesFormatter(cfdi_data)
        result_columns = formatter.dict_to_columns()
        print(result_columns)
        end_time = time.time() - start
        self.assertListEqual(expected_columns, result_columns)
        self.assertLess(end_time, 0.01)
