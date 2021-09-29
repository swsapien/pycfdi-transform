from pycfdi_transform import CFDI33SAXHandler
from pycfdi_transform.formatters.pagos10.efisco_pagos10_formatter import EfiscoPagos10Formatter
import unittest

class TestEfiscoPagos10Formatter(unittest.TestCase):

    def test_columns_names_pagos10(self):
        formatter = EfiscoPagos10Formatter({'cfdi33': {}})
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
            "RFCPROVCERTIF",
            "SELLOCFD",
            "P_IDENTIFICADOR_PAGO",
            "P_FECHAPAGO",
            "P_FORMADEPAGOP",
            "P_MONEDAP",
            "P_TIPOCAMBIOP",
            "P_MONTO",
            "P_NUMOPERACION",
            "P_RFCEMISORCTAORD",
            "P_NOMBANCOORDEXT",
            "P_CTAORDENANTE",
            "P_RFCEMISORCTABEN",
            "P_CTABENEFICIARIO",
            "P_IVATRASLADO",
            "P_IEPSTRASLADO",
            "P_TOTALIMPUESTOSTRASLADADOS",
            "P_ISRRETENCION",
            "P_IVARETENCION",
            "P_IEPSRETENCION",
            "P_TOTALIMPUESTOSRETENIDOS",
            "P_DR_IDDOCUMENTO",
            "P_DR_SERIE",
            "P_DR_FOLIO",
            "P_DR_MONEDADR",
            "P_DR_TIPOCAMBIODR",
            "P_DR_METODODEPAGODR",
            "P_DR_NUMPARCIALIDAD",
            "P_DR_IMPSALDOANT",
            "P_DR_IMPPAGADO",
            "P_DR_IMPSALDOINSOLUTO"
        ]
        self.assertListEqual(columns_expected, formatter.get_columns_names())
    
    def test_initialize_class_error_pagos10(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoPagos10Formatter(cfdi_data=None)
        self.assertEqual('El Formatter debe recibir el objeto devuelto por la transformación el debe ser un dict.', str(ex.exception))
    
    def test_initialize_class_error_version_pagos10(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoPagos10Formatter({'cfdi32': {}})
        self.assertEqual('Este formatter únicamente soporta datos de cfdi33.', str(ex.exception))
    
    def test_formatter_error_tfd_pagos10(self):
        sax_handler = CFDI33SAXHandler().use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago10_01.xml')
        cfdi_data.pop('tfd11')
        formatter = EfiscoPagos10Formatter(cfdi_data)
        self.assertFalse(formatter.can_format())
        self.assertEqual(formatter.get_errors(), 'Not tfd11 in data.')
    
    def test_formatter_error_tfdpagos_pagos10(self):
        sax_handler = CFDI33SAXHandler().use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago10_01.xml')
        cfdi_data.pop('pagos10')
        formatter = EfiscoPagos10Formatter(cfdi_data)
        self.assertFalse(formatter.can_format())
        self.assertEqual(formatter.get_errors(), 'Not pagos10 in data.')

    def test_rows_pagos10_01(self):
        sax_handler = CFDI33SAXHandler().use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago10_01.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoPagos10Formatter(cfdi_data)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        self.assertGreater(len(row_list), 0, 'No rows returned.')
        for row in row_list:
            self.assertEqual(len(row), len(formatter.get_columns_names()), 'Different length of columns')
        first_row = [
            "3.3",
            "PA",
            "1",
            "2019-03-29T17:37:19",
            "00000000000000000000",
            "0",
            "",
            "0",
            "XXX",
            "",
            "P",
            "",
            "",
            "",
            "45110",
            "XAXX010101000",
            "xxx",
            "601",
            "XAXX010101000",
            "PUBLICO EN GENERAL",
            "P01",
            "94C4AA76-9DD5-41AD-A10B-267024761951",
            "2019-03-29T17:42:38",
            "AAA010101AAA",
            "",
            "CP1_P1_DR1",
            "2019-03-29T16:14:52",
            "03",
            "MXN",
            "",
            "58000.00",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "MXN",
            "",
            "PPD",
            "2",
            "138040.00",
            "58000.00",
            "80040.00"
        ]
        self.assertListEqual(first_row, row_list[0])