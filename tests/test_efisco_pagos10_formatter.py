from pycfdi_transform import CFDI33SAXHandler
from pycfdi_transform.formatters.pagos10.efisco_pagos10_formatter import EfiscoPagos10Formatter
import unittest
import time

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
        self.assertEqual(len(row_list), 1, 'No rows returned.')
        for row in row_list:
            self.assertEqual(len(row), len(formatter.get_columns_names()), 'Different length of columns')
        first_row = ['3.3', 'PA', '1', '2019-03-29T17:37:19', '00000000000000000000', '0', '', '0', 'XXX', '', 'P', '', '', '', '45110', 'XAXX010101000', 'xxx', '601', 'XAXX010101000', 'PUBLICO EN GENERAL', 'P01', '94C4AA76-9DD5-41AD-A10B-267024761951', '2019-03-29T17:42:38', 'AAA010101AAA', '', 'CP1_P1_DR1', '2019-03-29T16:14:52', '03', 'MXN', '', '58000.00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'i', '3463', 'MXN', '', 'PPD', '2', '138040.00', '58000.00', '80040.00']
        self.assertListEqual(first_row, row_list[0])
    
    def test_rows_pagos10_01_empty_char(self):
        start = time.time()
        sax_handler = CFDI33SAXHandler().use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago10_01.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoPagos10Formatter(cfdi_data, empty_char='-')
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        end_time = start - time.time()
        first_row = ['3.3', 'PA', '1', '2019-03-29T17:37:19', '00000000000000000000', '0', '-', '0', 'XXX', '-', 'P', '-', '-', '-', '45110', 'XAXX010101000', 'xxx', '601', 'XAXX010101000', 'PUBLICO EN GENERAL', 'P01', '94C4AA76-9DD5-41AD-A10B-267024761951', '2019-03-29T17:42:38', 'AAA010101AAA', '', 'CP1_P1_DR1', '2019-03-29T16:14:52', '03', 'MXN', '-', '58000.00', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '', 'i', '3463', 'MXN', '-', 'PPD', '2', '138040.00', '58000.00', '80040.00']
        self.assertListEqual(first_row, row_list[0])
        self.assertLess(end_time, 0.01)
    
    def test_rows_pagos10_01_safe_numerics(self):
        start = time.time()
        sax_handler = CFDI33SAXHandler().use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago10_01.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoPagos10Formatter(cfdi_data, safe_numerics=True)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        end_time = start - time.time()
        first_row = ['3.3', 'PA', '1', '2019-03-29T17:37:19', '00000000000000000000', '0', '0.00', '0', 'XXX', '1.00', 'P', '', '', '', '45110', 'XAXX010101000', 'xxx', '601', 'XAXX010101000', 'PUBLICO EN GENERAL', 'P01', '94C4AA76-9DD5-41AD-A10B-267024761951', '2019-03-29T17:42:38', 'AAA010101AAA', '', 'CP1_P1_DR1', '2019-03-29T16:14:52', '03', 'MXN', '1.00', '58000.00', '', '', '', '', '', '', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '', 'i', '3463', 'MXN', '1.00', 'PPD', '2', '138040.00', '58000.00', '80040.00']
        self.assertListEqual(first_row, row_list[0])
        self.assertLess(end_time, 0.01)
    
    def test_rows_pagos10_01_empty_char_safe_numerics(self):
        start = time.time()
        sax_handler = CFDI33SAXHandler().use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago10_01.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoPagos10Formatter(cfdi_data, empty_char='-', safe_numerics=True)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        end_time = start - time.time()
        first_row = ['3.3', 'PA', '1', '2019-03-29T17:37:19', '00000000000000000000', '0', '0.00', '0', 'XXX', '1.00', 'P', '-', '-', '-', '45110', 'XAXX010101000', 'xxx', '601', 'XAXX010101000', 'PUBLICO EN GENERAL', 'P01', '94C4AA76-9DD5-41AD-A10B-267024761951', '2019-03-29T17:42:38', 'AAA010101AAA', '', 'CP1_P1_DR1', '2019-03-29T16:14:52', '03', 'MXN', '1.00', '58000.00', '-', '-', '-', '-', '-', '-', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '', 'i', '3463', 'MXN', '1.00', 'PPD', '2', '138040.00', '58000.00', '80040.00']
        self.assertListEqual(first_row, row_list[0])
        self.assertLess(end_time, 0.01)
    
    def test_rows_pagos10_multi_tfd(self):
        sax_handler = CFDI33SAXHandler().use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago10_multiple_tfd.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoPagos10Formatter(cfdi_data)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        self.assertEqual(len(row_list), 2, 'Different rows returned.')
        for row in row_list:
            self.assertEqual(len(row), len(formatter.get_columns_names()), 'Different length of columns')
        expected_rows = [
            ['3.3', 'PA', '1', '2019-03-29T17:37:19', '30001000000400002434', '0', '', '0', 'XXX', '', 'P', '', '', '', '45400', 'EKU9003173C9', 'ESCUELA KEMPER URGATE SA DE CV', '601', 'XAXX010101000', 'PUBLICO EN GENERAL', 'P01', '9D81C696-0401-4F85-B703-6E0D3AFD6057', '2019-03-29T17:42:38', 'AAA010101AAA', 'G3knPza1r8hfxSb+46JBRAYoQIUTVU2Uqlw/qiMLbzKkqrUs2zs5GVRjf0DJEm5mIGZIC3/+q/FdU1A4zr9RCXWM66QmtK7AAlkT4HSrX9NlCoJylwRzRW6bxuchfy8ryFmWIetAOU2U1brWLSSYqCtc86m4iIBId6kDOSIr+/Tpz2Q3rDHhmtlJyJ2ovy1rjLO0mZpbwhwOKg6Mo1+NeEuGk4UfQu8gfRgv9mOnbiNkfiJHzvuRJnUXYrL/9D1gDQ6gjW8t75W/yYN+Gf2TmpyTnOkYZbFqrJ8udt7rZjXsODLapD7cV4bjsLIYxOWHgXEIgrTjB57m2POrfb72wQ==', 'CP1_P1_DR1', '2019-03-29T16:14:52', '03', 'MXN', '', '58000.00', '', '', '', '', '', '', '', '', '', '', '', '', '', '16961ec1-c744-4a12-9f77-0e03bbceca16', 'i', '3463', 'MXN', '', 'PPD', '2', '138040.00', '58000.00', '80040.00'],
            ['3.3', 'PA', '1', '2019-03-29T17:37:19', '30001000000400002434', '0', '', '0', 'XXX', '', 'P', '', '', '', '45400', 'EKU9003173C9', 'ESCUELA KEMPER URGATE SA DE CV', '601', 'XAXX010101000', 'PUBLICO EN GENERAL', 'P01', '1D81C696-0401-4F85-B703-6E0D3AFD6057', '2019-03-29T17:42:38', 'AAA010101AAA', 'G3knPza1r8hfxSb+46JBRAYoQIUTVU2Uqlw/qiMLbzKkqrUs2zs5GVRjf0DJEm5mIGZIC3/+q/FdU1A4zr9RCXWM66QmtK7AAlkT4HSrX9NlCoJylwRzRW6bxuchfy8ryFmWIetAOU2U1brWLSSYqCtc86m4iIBId6kDOSIr+/Tpz2Q3rDHhmtlJyJ2ovy1rjLO0mZpbwhwOKg6Mo1+NeEuGk4UfQu8gfRgv9mOnbiNkfiJHzvuRJnUXYrL/9D1gDQ6gjW8t75W/yYN+Gf2TmpyTnOkYZbFqrJ8udt7rZjXsODLapD7cV4bjsLIYxOWHgXEIgrTjB57m2POrfb72wQ==', 'CP1_P1_DR1', '2019-03-29T16:14:52', '03', 'MXN', '', '58000.00', '', '', '', '', '', '', '', '', '', '', '', '', '', '16961ec1-c744-4a12-9f77-0e03bbceca16', 'i', '3463', 'MXN', '', 'PPD', '2', '138040.00', '58000.00', '80040.00']
        ]
        self.assertListEqual(expected_rows, row_list)
    
    def test_rows_pagos10_complete(self):
        sax_handler = CFDI33SAXHandler().use_pagos10()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos10/pago_complete.xml')
        #Fix missing TFD in file.
        cfdi_data['tfd11'] = [{'version': '1.1', 'no_certificado_sat': '20001000000300022323', 'uuid': '9D81C696-0401-4F85-B703-6E0D3AFD6057', 'fecha_timbrado': '2019-03-29T17:42:38', 'rfc_prov_cert': 'AAA010101AAA', 'sello_cfd': 'G3knPza1r8hfxSb+46JBRAYoQIUTVU2Uqlw/qiMLbzKkqrUs2zs5GVRjf0DJEm5mIGZIC3/+q/FdU1A4zr9RCXWM66QmtK7AAlkT4HSrX9NlCoJylwRzRW6bxuchfy8ryFmWIetAOU2U1brWLSSYqCtc86m4iIBId6kDOSIr+/Tpz2Q3rDHhmtlJyJ2ovy1rjLO0mZpbwhwOKg6Mo1+NeEuGk4UfQu8gfRgv9mOnbiNkfiJHzvuRJnUXYrL/9D1gDQ6gjW8t75W/yYN+Gf2TmpyTnOkYZbFqrJ8udt7rZjXsODLapD7cV4bjsLIYxOWHgXEIgrTjB57m2POrfb72wQ==', 'sello_sat': 'ULW1tcO5xJKR9ZLcY9+ls9Zg8rPXROVvbVVTWOnOJ/H88Om4ZRXWdjrHzrPv+Zre4gS0mcDaxuzwNHRhU5YKvONbFgme31mgsadWubTQyh10JGzhuYIzsGhnFBuYmNaKVR/vYbd9X4RBRfiggRW+tSIv8qFZGZZ1RSznmxc3FUP//tR1uGKVVnivs590DQV5UxKAVKXtF0T/dPwncKuOHcheFP6PdL+ToJB9mRz8Xl9Ag7x+WuHOBwdzx2lpEj8yms1d/CKgxWGFOXUEhpKsQXGm1MYYMLCo5/wNG6oC6F9FkvcV5rNji3Qna/P4OHXduL0UIz2FqvIK65NeRxgilQ=='}]
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoPagos10Formatter(cfdi_data)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        self.assertEqual(len(row_list), 8, 'Different rows returned.')
        for row in row_list:
            self.assertEqual(len(row), len(formatter.get_columns_names()), 'Different length of columns')
        expected_rows = [
            ['3.3', '"', '/>KA', '2018-01-10T07:22:51', '47217725691977968749', '5858580.234906', '9061950.234906', '7679420.234906', 'SGD', '8016540.234907', 'N', 'PPD', '01', '}_', '45734', 'J&O750807563', 'Q~', '611', 'ÑÑD68010919A', '^*p_', 'D01', '9D81C696-0401-4F85-B703-6E0D3AFD6057', '2019-03-29T17:42:38', 'AAA010101AAA', 'G3knPza1r8hfxSb+46JBRAYoQIUTVU2Uqlw/qiMLbzKkqrUs2zs5GVRjf0DJEm5mIGZIC3/+q/FdU1A4zr9RCXWM66QmtK7AAlkT4HSrX9NlCoJylwRzRW6bxuchfy8ryFmWIetAOU2U1brWLSSYqCtc86m4iIBId6kDOSIr+/Tpz2Q3rDHhmtlJyJ2ovy1rjLO0mZpbwhwOKg6Mo1+NeEuGk4UfQu8gfRgv9mOnbiNkfiJHzvuRJnUXYrL/9D1gDQ6gjW8t75W/yYN+Gf2TmpyTnOkYZbFqrJ8udt7rZjXsODLapD7cV4bjsLIYxOWHgXEIgrTjB57m2POrfb72wQ==', 'CP1_P1_DR1', '2015-01-06T06:10:27', '26', 'XBA', '4026190.234907', '8426440.234906', '}', '&ÑÑ941216Z6A', '~', '__LN__5__4', '&&Ñ411106M7A', '_L_T0DRB_6', '15440800.469812', '0.00', '1252680.234906', '0.00', '0.00', '0.00', '5031130.234906', 'BcfEc9ED-e6fE-3a98-13b0-A9c97bEcBcEd', '', '', 'MUR', '', 'PPD', '', '', '9752350.234906', '82970.234906'],
            ['3.3', '"', '/>KA', '2018-01-10T07:22:51', '47217725691977968749', '5858580.234906', '9061950.234906', '7679420.234906', 'SGD', '8016540.234907', 'N', 'PPD', '01', '}_', '45734', 'J&O750807563', 'Q~', '611', 'ÑÑD68010919A', '^*p_', 'D01', '9D81C696-0401-4F85-B703-6E0D3AFD6057', '2019-03-29T17:42:38', 'AAA010101AAA', 'G3knPza1r8hfxSb+46JBRAYoQIUTVU2Uqlw/qiMLbzKkqrUs2zs5GVRjf0DJEm5mIGZIC3/+q/FdU1A4zr9RCXWM66QmtK7AAlkT4HSrX9NlCoJylwRzRW6bxuchfy8ryFmWIetAOU2U1brWLSSYqCtc86m4iIBId6kDOSIr+/Tpz2Q3rDHhmtlJyJ2ovy1rjLO0mZpbwhwOKg6Mo1+NeEuGk4UfQu8gfRgv9mOnbiNkfiJHzvuRJnUXYrL/9D1gDQ6gjW8t75W/yYN+Gf2TmpyTnOkYZbFqrJ8udt7rZjXsODLapD7cV4bjsLIYxOWHgXEIgrTjB57m2POrfb72wQ==', 'CP1_P1_DR2', '2015-01-06T06:10:27', '26', 'XBA', '4026190.234907', '8426440.234906', '}', '&ÑÑ941216Z6A', '~', '__LN__5__4', '&&Ñ411106M7A', '_L_T0DRB_6', '15440800.469812', '0.00', '1252680.234906', '0.00', '0.00', '0.00', '5031130.234906', 'be6dcDE2-ab9B-7DcF-Aaa2-CB8679f2fa01', '', 'c!}~r', 'HKD', '', 'PPD', '', '8563470.234906', '5255780.234906', ''],
            ['3.3', '"', '/>KA', '2018-01-10T07:22:51', '47217725691977968749', '5858580.234906', '9061950.234906', '7679420.234906', 'SGD', '8016540.234907', 'N', 'PPD', '01', '}_', '45734', 'J&O750807563', 'Q~', '611', 'ÑÑD68010919A', '^*p_', 'D01', '9D81C696-0401-4F85-B703-6E0D3AFD6057', '2019-03-29T17:42:38', 'AAA010101AAA', 'G3knPza1r8hfxSb+46JBRAYoQIUTVU2Uqlw/qiMLbzKkqrUs2zs5GVRjf0DJEm5mIGZIC3/+q/FdU1A4zr9RCXWM66QmtK7AAlkT4HSrX9NlCoJylwRzRW6bxuchfy8ryFmWIetAOU2U1brWLSSYqCtc86m4iIBId6kDOSIr+/Tpz2Q3rDHhmtlJyJ2ovy1rjLO0mZpbwhwOKg6Mo1+NeEuGk4UfQu8gfRgv9mOnbiNkfiJHzvuRJnUXYrL/9D1gDQ6gjW8t75W/yYN+Gf2TmpyTnOkYZbFqrJ8udt7rZjXsODLapD7cV4bjsLIYxOWHgXEIgrTjB57m2POrfb72wQ==', 'CP1_P2_DR1', '2015-04-15T09:02:29', '29', 'BHD', '2027230.234907', '2211890.234906', '~\\', '&ÑR880531UH8', '~', 'JS_O33J_3_L3', 'ÑÑX930431318', 'FV485__M__', '2251880.234906', '6446220.469812', '9610150.469812', '15303350.704718', '7452070.469812', '0.00', '0.00', 'eafcbCE2-Da9c-D0AE-6dd0-eCBeF5422bBe', '', '', 'PYG', '', 'PUE', '55', '2349050.234906', '', '9332080.234906'],
            ['3.3', '"', '/>KA', '2018-01-10T07:22:51', '47217725691977968749', '5858580.234906', '9061950.234906', '7679420.234906', 'SGD', '8016540.234907', 'N', 'PPD', '01', '}_', '45734', 'J&O750807563', 'Q~', '611', 'ÑÑD68010919A', '^*p_', 'D01', '9D81C696-0401-4F85-B703-6E0D3AFD6057', '2019-03-29T17:42:38', 'AAA010101AAA', 'G3knPza1r8hfxSb+46JBRAYoQIUTVU2Uqlw/qiMLbzKkqrUs2zs5GVRjf0DJEm5mIGZIC3/+q/FdU1A4zr9RCXWM66QmtK7AAlkT4HSrX9NlCoJylwRzRW6bxuchfy8ryFmWIetAOU2U1brWLSSYqCtc86m4iIBId6kDOSIr+/Tpz2Q3rDHhmtlJyJ2ovy1rjLO0mZpbwhwOKg6Mo1+NeEuGk4UfQu8gfRgv9mOnbiNkfiJHzvuRJnUXYrL/9D1gDQ6gjW8t75W/yYN+Gf2TmpyTnOkYZbFqrJ8udt7rZjXsODLapD7cV4bjsLIYxOWHgXEIgrTjB57m2POrfb72wQ==', 'CP1_P2_DR2', '2015-04-15T09:02:29', '29', 'BHD', '2027230.234907', '2211890.234906', '~\\', '&ÑR880531UH8', '~', 'JS_O33J_3_L3', 'ÑÑX930431318', 'FV485__M__', '2251880.234906', '6446220.469812', '9610150.469812', '15303350.704718', '7452070.469812', '0.00', '0.00', 'B64DDDF2-fECA-fcDe-430d-D1A5F02ea844', 'e', '', 'MXN', '', 'PPD', '', '', '1070880.234906', '6193010.234906'],
            ['3.3', '"', '/>KA', '2018-01-10T07:22:51', '47217725691977968749', '5858580.234906', '9061950.234906', '7679420.234906', 'SGD', '8016540.234907', 'N', 'PPD', '01', '}_', '45734', 'J&O750807563', 'Q~', '611', 'ÑÑD68010919A', '^*p_', 'D01', '9D81C696-0401-4F85-B703-6E0D3AFD6057', '2019-03-29T17:42:38', 'AAA010101AAA', 'G3knPza1r8hfxSb+46JBRAYoQIUTVU2Uqlw/qiMLbzKkqrUs2zs5GVRjf0DJEm5mIGZIC3/+q/FdU1A4zr9RCXWM66QmtK7AAlkT4HSrX9NlCoJylwRzRW6bxuchfy8ryFmWIetAOU2U1brWLSSYqCtc86m4iIBId6kDOSIr+/Tpz2Q3rDHhmtlJyJ2ovy1rjLO0mZpbwhwOKg6Mo1+NeEuGk4UfQu8gfRgv9mOnbiNkfiJHzvuRJnUXYrL/9D1gDQ6gjW8t75W/yYN+Gf2TmpyTnOkYZbFqrJ8udt7rZjXsODLapD7cV4bjsLIYxOWHgXEIgrTjB57m2POrfb72wQ==', 'CP1_P2_DR3', '2015-04-15T09:02:29', '29', 'BHD', '2027230.234907', '2211890.234906', '~\\', '&ÑR880531UH8', '~', 'JS_O33J_3_L3', 'ÑÑX930431318', 'FV485__M__', '2251880.234906', '6446220.469812', '9610150.469812', '15303350.704718', '7452070.469812', '0.00', '0.00', '415-53-638204948', 'qm3}', '', 'PYG', '', 'PPD', '', '', '5300650.234906', '1336720.234906'],
            ['3.3', '"', '/>KA', '2018-01-10T07:22:51', '47217725691977968749', '5858580.234906', '9061950.234906', '7679420.234906', 'SGD', '8016540.234907', 'N', 'PPD', '01', '}_', '45734', 'J&O750807563', 'Q~', '611', 'ÑÑD68010919A', '^*p_', 'D01', '9D81C696-0401-4F85-B703-6E0D3AFD6057', '2019-03-29T17:42:38', 'AAA010101AAA', 'G3knPza1r8hfxSb+46JBRAYoQIUTVU2Uqlw/qiMLbzKkqrUs2zs5GVRjf0DJEm5mIGZIC3/+q/FdU1A4zr9RCXWM66QmtK7AAlkT4HSrX9NlCoJylwRzRW6bxuchfy8ryFmWIetAOU2U1brWLSSYqCtc86m4iIBId6kDOSIr+/Tpz2Q3rDHhmtlJyJ2ovy1rjLO0mZpbwhwOKg6Mo1+NeEuGk4UfQu8gfRgv9mOnbiNkfiJHzvuRJnUXYrL/9D1gDQ6gjW8t75W/yYN+Gf2TmpyTnOkYZbFqrJ8udt7rZjXsODLapD7cV4bjsLIYxOWHgXEIgrTjB57m2POrfb72wQ==', 'CP1_P2_DR4', '2015-04-15T09:02:29', '29', 'BHD', '2027230.234907', '2211890.234906', '~\\', '&ÑR880531UH8', '~', 'JS_O33J_3_L3', 'ÑÑX930431318', 'FV485__M__', '2251880.234906', '6446220.469812', '9610150.469812', '15303350.704718', '7452070.469812', '0.00', '0.00', 'AB614e3E-8fB7-afce-5Acb-b6B6C332EeEa', '', '', 'CLP', '', 'PPD', '', '', '', ''],
            ['3.3', '"', '/>KA', '2018-01-10T07:22:51', '47217725691977968749', '5858580.234906', '9061950.234906', '7679420.234906', 'SGD', '8016540.234907', 'N', 'PPD', '01', '}_', '45734', 'J&O750807563', 'Q~', '611', 'ÑÑD68010919A', '^*p_', 'D01', '9D81C696-0401-4F85-B703-6E0D3AFD6057', '2019-03-29T17:42:38', 'AAA010101AAA', 'G3knPza1r8hfxSb+46JBRAYoQIUTVU2Uqlw/qiMLbzKkqrUs2zs5GVRjf0DJEm5mIGZIC3/+q/FdU1A4zr9RCXWM66QmtK7AAlkT4HSrX9NlCoJylwRzRW6bxuchfy8ryFmWIetAOU2U1brWLSSYqCtc86m4iIBId6kDOSIr+/Tpz2Q3rDHhmtlJyJ2ovy1rjLO0mZpbwhwOKg6Mo1+NeEuGk4UfQu8gfRgv9mOnbiNkfiJHzvuRJnUXYrL/9D1gDQ6gjW8t75W/yYN+Gf2TmpyTnOkYZbFqrJ8udt7rZjXsODLapD7cV4bjsLIYxOWHgXEIgrTjB57m2POrfb72wQ==', 'CP1_P2_DR5', '2015-04-15T09:02:29', '29', 'BHD', '2027230.234907', '2211890.234906', '~\\', '&ÑR880531UH8', '~', 'JS_O33J_3_L3', 'ÑÑX930431318', 'FV485__M__', '2251880.234906', '6446220.469812', '9610150.469812', '15303350.704718', '7452070.469812', '0.00', '0.00', 'ebCA4FBe-3b90-daFC-DDCD-a2b6A296DDcD', '', '', 'AWG', '', 'PPD', '99', '', '', '6085410.234906'],
            ['3.3', '"', '/>KA', '2018-01-10T07:22:51', '47217725691977968749', '5858580.234906', '9061950.234906', '7679420.234906', 'SGD', '8016540.234907', 'N', 'PPD', '01', '}_', '45734', 'J&O750807563', 'Q~', '611', 'ÑÑD68010919A', '^*p_', 'D01', '9D81C696-0401-4F85-B703-6E0D3AFD6057', '2019-03-29T17:42:38', 'AAA010101AAA', 'G3knPza1r8hfxSb+46JBRAYoQIUTVU2Uqlw/qiMLbzKkqrUs2zs5GVRjf0DJEm5mIGZIC3/+q/FdU1A4zr9RCXWM66QmtK7AAlkT4HSrX9NlCoJylwRzRW6bxuchfy8ryFmWIetAOU2U1brWLSSYqCtc86m4iIBId6kDOSIr+/Tpz2Q3rDHhmtlJyJ2ovy1rjLO0mZpbwhwOKg6Mo1+NeEuGk4UfQu8gfRgv9mOnbiNkfiJHzvuRJnUXYrL/9D1gDQ6gjW8t75W/yYN+Gf2TmpyTnOkYZbFqrJ8udt7rZjXsODLapD7cV4bjsLIYxOWHgXEIgrTjB57m2POrfb72wQ==', 'CP1_P3_DR1', '2015-08-06T06:10:27', '26', 'MXN', '', '8426440.234906', '5459', 'AVV941216Z6A', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ]
        self.assertListEqual(expected_rows, row_list)