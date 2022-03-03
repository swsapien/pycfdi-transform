from pycfdi_transform import CFDI33SAXHandler
from pycfdi_transform import CFDI32SAXHandler
from pycfdi_transform.formatters.concepts.efisco_core_concepts_detail_formatter import EfiscoCoreConceptsDetailFormatter
import unittest
import time

class TestEfiscoCoreConceptosFormatter(unittest.TestCase):

    def test_columns_names_concepts(self):
        formatter = EfiscoCoreConceptsDetailFormatter({'cfdi33': {}})
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
            "C_IMPORTE"
        ]
        self.assertListEqual(columns_expected, formatter.get_columns_names())


    def test_formatter_concept_can_format_ok(self):
        sax_handler = CFDI33SAXHandler().use_concepts_cfdi33()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi33/cfdi33_01.xml')
        formatter = EfiscoCoreConceptsDetailFormatter(cfdi_data)
        self.assertTrue(formatter.can_format())

    def test_formatter_concepts_cfdi33(self):
        start = time.time()
        sax_handler = CFDI33SAXHandler().use_concepts_cfdi33()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi33/cfdi33_01.xml')
        expected_columns = [['3.3', 'VF', '001002004', '2020-04-30T22:36:13', '30001000000400002434', '10.00', '', '11.60', 'MXN', '', 'I', 'PPD', '01', 'NET15', '84094', 'EKU9003173C9', 'ESCUELA KEMPER URGATE SA DE CV', '601', 'XAXX010101000', 'PUBLICO EN GENERAL', 'G03', '9D81C696-0401-4F85-B703-6E0D3AFD6056', '2020-05-02T00:36:50', 0, '01010101', 'productoInventario', '1.0000', '3G', '', 'Detalle factura', '10.0000', '', '10.00']]
        formatter = EfiscoCoreConceptsDetailFormatter(cfdi_data)
        result_columns = formatter.dict_to_columns()
        print(result_columns)
        end_time = time.time() - start
        self.assertListEqual(expected_columns, result_columns)
        self.assertLess(end_time, 0.01)

    def test_formatter_concepts_cfdi32(self):
        start = time.time()
        sax_handler = CFDI32SAXHandler().use_concepts_cfdi32()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi32/cfdi32_01.xml')
        expected_columns = [
            ['3.2', 'Z', '007', '2017-11-07T23:35:52', '30001000000300023708', '1333.00', '', '1546.28', 'MXN', '1.0000', 'ingreso', 'NA', 'Pago en una sola exhibición', '', 'ZAPOPAN, JALISCO', 'IIA040805DZ4', 'MI SUPER CUENTA DE DESSARROLLO', ['GENERAL DE LEY PERSONAS MORALES', 'GENERAL DE LEY PERSONAS MORALES DOBLE REGIMEN'], 'CACX7605101P8', 'PUBLICO GENERAL', '', '9ECB9AF2-3998-4C1F-BB97-CEB5512F149C', '2017-11-07T23:40:27', 0, '', 'UT421511', '1', '', 'No Aplica', '123', '1333', '', '1333.000000'],
            ['3.2', 'Z', '007', '2017-11-07T23:35:52', '30001000000300023708', '1333.00', '', '1546.28', 'MXN', '1.0000', 'ingreso', 'NA', 'Pago en una sola exhibición', '', 'ZAPOPAN, JALISCO', 'IIA040805DZ4', 'MI SUPER CUENTA DE DESSARROLLO', ['GENERAL DE LEY PERSONAS MORALES', 'GENERAL DE LEY PERSONAS MORALES DOBLE REGIMEN'], 'CACX7605101P8', 'PUBLICO GENERAL', '', '9ECB9AF2-3998-4C1F-BB97-CEB5512F149C', '2017-11-07T23:40:27', 0, '', 'UT421511', '1', '', 'No Aplica', '123', '1333', '', '1333.000000']
        ]
        formatter = EfiscoCoreConceptsDetailFormatter(cfdi_data)
        result_columns = formatter.dict_to_columns()
        print(result_columns)
        end_time = time.time() - start
        self.assertListEqual(expected_columns, result_columns)
        self.assertLess(end_time, 0.01)
