from pycfdi_transform import CFDI33SAXHandler
from pycfdi_transform.formatters.nomina12.efisco_core_nomina12_formatter import EfiscoCoreNomina12Formatter
from pycfdi_transform.formatters.concepts.efisco_core_concepts_detail_formatter import EfiscoCoreConceptsDetailFormatter
import unittest
import time

class TestEfiscoNomina12Formatter(unittest.TestCase):

    def test_columns_names_nomina11(self):
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
        cfdi_data = sax_handler.transform_from_file('./Resources/cfdi33/cfdi33_01.xml')
        formatter = EfiscoCoreConceptsDetailFormatter(cfdi_data)
        self.assertTrue(formatter.can_format())

    def test_formatter_concepts_cfdi33(self):
        start = time.time()
        sax_handler = CFDI33SAXHandler().use_concepts_cfdi33()
        cfdi_data = sax_handler.transform_from_file('./Resources/cfdi33/cfdi33_01.xml')
        expected_columns = [['3.3', 'VF', '001002004', '2020-04-30T22:36:13', '30001000000400002434', '10.00', '', '11.60', 'MXN', '', 'I', 'PPD', '01', 'NET15', '84094', 'EKU9003173C9', 'ESCUELA KEMPER URGATE SA DE CV', '601', 'XAXX010101000', 'PUBLICO EN GENERAL', 'G03', '9D81C696-0401-4F85-B703-6E0D3AFD6056', '2020-05-02T00:36:50', 0, '01010101', 'productoInventario', '1.0000', '3G', '', 'Detalle factura', '10.0000', '', '10.00']]
        formatter = EfiscoCoreConceptsDetailFormatter(cfdi_data)
        result_columns = formatter.dict_to_columns()
        print(result_columns)
        end_time = time.time() - start
        self.assertListEqual(expected_columns, result_columns)
        self.assertLess(end_time, 0.01)
