import os

from pycfdi_transform import CFDI33SAXHandler
from pycfdi_transform import CFDI32SAXHandler
from pycfdi_transform import CFDI40SAXHandler
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
            "C_IMPORTE",
            "TERCERONOMBRE",
            "TERCERORFC"
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
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi33/cfdi33_01_conceptos.xml')
        expected_columns = [['3.3', 'VF', '001002004', '2020-04-30T22:36:13', '30001000000400002434', '10.00', '', '11.60', 'MXN', '', 'I', 'PPD', '01', 'NET15', '84094', 'EKU9003173C9', 'ESCUELA KEMPER URGATE SA DE CV', '601', 'XAXX010101000', 'PUBLICO EN GENERAL', 'G03', '9D81C696-0401-4F85-B703-6E0D3AFD6056', '2020-05-02T00:36:50', 1, '01010101', 'productoInventario', '1.0000', '3G', '', 'Detalle factura', '10.0000', '', '10.00', '', ''],
                            ['3.3', 'VF', '001002004', '2020-04-30T22:36:13', '30001000000400002434', '10.00', '', '11.60', 'MXN', '', 'I', 'PPD', '01', 'NET15', '84094', 'EKU9003173C9', 'ESCUELA KEMPER URGATE SA DE CV', '601', 'XAXX010101000', 'PUBLICO EN GENERAL', 'G03', '9D81C696-0401-4F85-B703-6E0D3AFD6056', '2020-05-02T00:36:50', 2, '2300403', 'prodüctoInventarió', '1.0000', '3G', '', 'Detalle factura', '10.0000', '', '10.00', '', '']]
        formatter = EfiscoCoreConceptsDetailFormatter(cfdi_data)
        result_columns = formatter.dict_to_columns()
        print(result_columns)
        end_time = time.time() - start
        self.assertListEqual(expected_columns, result_columns)
        self.assertLess(end_time, 0.01)

    def test_formatter_concepts_cfdi33_terceros(self):
        start = time.time()
        sax_handler = CFDI33SAXHandler().use_concepts_cfdi33()
        cfdi_data = sax_handler.transform_from_file((os.path.dirname(__file__) + '/Resources/terceros/terceros11_33.xml'))
        expected_columns = [
            ['3.3', 'A', '40421', '2021-11-05T06:33:21', '00001000000000000001', '5215.03', '', '6027.53', 'MXN', '1', 'I', 'PUE', '04', 'Pago en una sola exhibicion', '55620', 'ASXXXX010101', 'SERVICIOS EMISIÓN TESTING', '608', 'EZXXXX020202', 'SERVICIOS RECEPCIÓN TESTING', 'P01', '87542154-C64A-1AB9-AE81-0000000000', '2020-06-05T08:35:27', 1, '12312321', '00000000001', '1', 'E48', 'NA', 'TERCEROS TESTING', '398.68', '', '398.68', '', ''],
            ['3.3', 'A', '40421', '2021-11-05T06:33:21', '00001000000000000001', '5215.03', '', '6027.53', 'MXN', '1', 'I', 'PUE', '04', 'Pago en una sola exhibicion', '55620', 'ASXXXX010101', 'SERVICIOS EMISIÓN TESTING', '608', 'EZXXXX020202', 'SERVICIOS RECEPCIÓN TESTING', 'P01', '87542154-C64A-1AB9-AE81-0000000000', '2020-06-05T08:35:27', 2, '33333333333', '00000000002', '1', 'E48', 'NA', 'TERCEROS TESTING 2da Edición', '4816.35', '', '4816.35', '', 'DCM000125IY6']
        ]
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
            ['3.2', 'Z', '007', '2017-11-07T23:35:52', '30001000000300023708', '1333.00', '', '1546.28', 'MXN', '1.0000', 'ingreso', 'NA', 'Pago en una sola exhibición', '', 'ZAPOPAN, JALISCO', 'IIA040805DZ4', 'MI SUPER CUENTA DE DESSARROLLO', ['GENERAL DE LEY PERSONAS MORALES', 'GENERAL DE LEY PERSONAS MORALES DOBLE REGIMEN'], 'CACX7605101P8', 'PUBLICO GENERAL', '', '9ECB9AF2-3998-4C1F-BB97-CEB5512F149C', '2017-11-07T23:40:27', 1, '', 'UT421511', '1', '', 'No Aplica', '123', '1333', '', '1333.000000', '', ''],
            ['3.2', 'Z', '007', '2017-11-07T23:35:52', '30001000000300023708', '1333.00', '', '1546.28', 'MXN', '1.0000', 'ingreso', 'NA', 'Pago en una sola exhibición', '', 'ZAPOPAN, JALISCO', 'IIA040805DZ4', 'MI SUPER CUENTA DE DESSARROLLO', ['GENERAL DE LEY PERSONAS MORALES', 'GENERAL DE LEY PERSONAS MORALES DOBLE REGIMEN'], 'CACX7605101P8', 'PUBLICO GENERAL', '', '9ECB9AF2-3998-4C1F-BB97-CEB5512F149C', '2017-11-07T23:40:27', 1, '', 'UT421511', '1', '', 'No Aplica', '123', '1333', '', '1333.000000', '', '']
        ]
        formatter = EfiscoCoreConceptsDetailFormatter(cfdi_data)
        result_columns = formatter.dict_to_columns()
        print(result_columns)
        end_time = time.time() - start
        self.assertListEqual(expected_columns, result_columns)
        self.assertLess(end_time, 0.01)

    def test_formatter_concepts_cfdi_32_terceros(self):
        sax_handler = CFDI32SAXHandler().use_concepts_cfdi32()
        cfdi_data = sax_handler.transform_from_file((os.path.dirname(__file__) + '/Resources/terceros/terceros11_32.xml'))
        formatter = EfiscoCoreConceptsDetailFormatter(cfdi_data)
        result_columns = formatter.dict_to_columns()
        expected_columns = [
            ['3.2', 'C', '38', '2015-03-05T10:33:52', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'ingreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Monterrey, Nuevo León', 'AAA010101AAA', 'Empresa de Pruebas SA', ['Regimen General de Ley Personas Morales de Prueba'], 'E&Ñ831019M53', 'Exportadora de Ganado HOLSTEIN S.A.', '', '5D777512-F544-41CE-AA0C-4C36ED254FC8', '2015-03-05T10:33:52', 1, '', '', '1', '', 'LTE', 'Pago por cuenta de terceros', '35000.00', '', '35000.00', 'EMPRESA DE PRUEBA S.A. DE C.V.', 'AAA010101AAA']
        ]
        self.assertListEqual(expected_columns, result_columns)

    def test_formatter_concepts_cfdi_40_terceros(self):
        sax_handler = CFDI40SAXHandler().use_concepts_cfdi40()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/terceros/terceros_40.xml')
        formatter = EfiscoCoreConceptsDetailFormatter(cfdi_data)
        result_columns = formatter.dict_to_columns()
        expected_columns = [
            ['4.0', 'Serie', '2080427802', '2022-02-08T19:04:49', '30001000000400002434', '200', '', '180', 'MXN', '1', 'I', 'PPD', '99', 'CondicionesDePago', '20000', 'EKU9003173C9', 'ESCUELA KEMPER URGATE', '601', 'URE180429TM6', 'UNIVERSIDAD ROBOTICA ESPAÑOLA', 'G03', 'D69E0C63-8F17-4FB3-9838-D834FD901474', '2022-02-09T01:22:19', 1, '50211503', 'UT421511', '1', 'H87', 'Pieza', 'Cigarros', '200.00', '', '200.00', 'ADRIANA JUAREZ FERNANDEZ', 'JUFA7608212V6']
        ]
        self.assertListEqual(expected_columns, result_columns)

    def test_formatter_concepts_cfdi_40(self):
        start = time.time()
        sax_handler = CFDI40SAXHandler().use_concepts_cfdi40()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/cfdi40/cfdi40_01.xml')
        expected_columns = [
            ['4.0', 'IFDG~', '41741985~', '2021-12-01T05:56:56', '30001000000400002434', '4959440.234906', '3308870.234906', '6078640.234906', 'IRR', '2378590.234907', 'I', 'PPD', '01', 'NET15', '45400', 'SKDR690105TM0', 'ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~', '624', '&ÑOZ291130QPA', 'kghfhg~', 'I06', '9D81C696-0401-4F85-B703-6E0D3AFD6056', '2020-05-02T00:36:50', 1, '51101903', '~55515', '9253280.234907', 'A58', '', 'b!~asdasfg85418816', '5835760.234906', '', '3916480.234906', '', ''],
            ['4.0', 'IFDG~', '41741985~', '2021-12-01T05:56:56', '30001000000400002434', '4959440.234906', '3308870.234906', '6078640.234906', 'IRR', '2378590.234907', 'I', 'PPD', '01', 'NET15', '45400', 'SKDR690105TM0', 'ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~', '624', '&ÑOZ291130QPA', 'kghfhg~', 'I06', '9D81C696-0401-4F85-B703-6E0D3AFD6056', '2020-05-02T00:36:50', 2, '50321559', '/1852821)', '1993740.234907', 'G55', '', '}&~', '315930.234906', '7520980.234906', '2922160.234906', '}ni,os', 'ÑÑ&Ñ270414O01'],
            ['4.0', 'IFDG~', '41741985~', '2021-12-01T05:56:56', '30001000000400002434', '4959440.234906', '3308870.234906', '6078640.234906', 'IRR', '2378590.234907', 'I', 'PPD', '01', 'NET15', '45400', 'SKDR690105TM0', 'ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~', '624', '&ÑOZ291130QPA', 'kghfhg~', 'I06', '9D81C696-0401-4F85-B703-6E0D3AFD6056', '2020-05-02T00:36:50', 3, '50466301', '}r}~&', '5592790.234907', 'H84', '7', '!#{k*', '4334580.234906', '', '325840.234906', '', ''],
            ['4.0', 'IFDG~', '41741985~', '2021-12-01T05:56:56', '30001000000400002434', '4959440.234906', '3308870.234906', '6078640.234906', 'IRR', '2378590.234907', 'I', 'PPD', '01', 'NET15', '45400', 'SKDR690105TM0', 'ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~', '624', '&ÑOZ291130QPA', 'kghfhg~', 'I06', '9D81C696-0401-4F85-B703-6E0D3AFD6056', '2020-05-02T00:36:50', 4, '25174800', '', '577420.234907', 'P28', '', 'E', '8775650.234906', '', '9380680.234906', 'munuiok~efsd8/4589hgrf', 'ÑHD7811238G3'],
            ['4.0', 'IFDG~', '41741985~', '2021-12-01T05:56:56', '30001000000400002434', '4959440.234906', '3308870.234906', '6078640.234906', 'IRR', '2378590.234907', 'I', 'PPD', '01', 'NET15', '45400', 'SKDR690105TM0', 'ESCUELÄ KEMPER ÚRGATE SA DE CV`}}}~', '624', '&ÑOZ291130QPA', 'kghfhg~', 'I06', '9D81C696-0401-4F85-B703-6E0D3AFD6056', '2020-05-02T00:36:50', 5, '10302150', '}9}z~}', '52990.234907', 'XDC', '', 'dm~}~', '8833520.234906', '', '6441520.234906', '', '']
        ]
        formatter = EfiscoCoreConceptsDetailFormatter(cfdi_data)
        result_columns = formatter.dict_to_columns()
        print(result_columns)
        end_time = time.time() - start
        self.assertListEqual(expected_columns, result_columns)
        self.assertLess(end_time, 0.01)
