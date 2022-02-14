from pycfdi_transform import CFDI40SAXHandler
from pycfdi_transform.formatters.pagos20.efisco_pagos20_formatter import  EfiscoPagos20Formatter
import unittest
import time

class TestEfiscoPagos10Formatter(unittest.TestCase):

    def test_columns_names_pagos20(self):
        formatter = EfiscoPagos20Formatter({'cfdi40': {}})
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
            "P_DR_EQUIVALENCIADR",
            "P_DR_NUMPARCIALIDAD",
            "P_DR_IMPSALDOANT",
            "P_DR_IMPPAGADO",
            "P_DR_IMPSALDOINSOLUTO"
        ]
        self.assertListEqual(columns_expected, formatter.get_columns_names())
    
    def test_initialize_class_error_pagos20(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoPagos20Formatter(cfdi_data=None)
        self.assertEqual('El Formatter debe recibir el objeto devuelto por la transformación el debe ser un dict.', str(ex.exception))
    
    def test_initialize_class_error_version_pagos20(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoPagos20Formatter({'cfdi33': {}})
        self.assertEqual('Este formatter únicamente soporta datos de cfdi40.', str(ex.exception))
    
    def test_formatter_error_tfd_pagos20(self):
        sax_handler = CFDI40SAXHandler().use_pagos20()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos20/pago_stamped.xml')
        cfdi_data.pop('tfd11')
        formatter = EfiscoPagos20Formatter(cfdi_data)
        self.assertFalse(formatter.can_format())
        self.assertEqual(formatter.get_errors(), 'Not tfd11 in data.')
    
    def test_formatter_error_tfdpagos_pagos20(self):
        sax_handler = CFDI40SAXHandler().use_pagos20()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos20/pago_stamped.xml')
        cfdi_data.pop('pagos20')
        formatter = EfiscoPagos20Formatter(cfdi_data)
        self.assertFalse(formatter.can_format())
        self.assertEqual(formatter.get_errors(), 'Not pagos20 in data.')

    def test_rows_pagos20_01(self):
        sax_handler = CFDI40SAXHandler().use_pagos20()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos20/pago_stamped.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoPagos20Formatter(cfdi_data)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        self.assertEqual(len(row_list), 1, 'No rows returned.')
        for row in row_list:
            self.assertEqual(len(row), len(formatter.get_columns_names()), 'Different length of columns')
        first_row = ['4.0', 'Serie', 'Folio', '2022-02-08T00:18:10', '30001000000400002434', '0', '', '0.00', 'XXX', '', 'P', '', '', '', '20000', 'EKU9003173C9', 'ESCUELA KEMPER URGATE SA DE CV', '601', 'URE180429TM6', 'UNIVERSIDAD ROBOTICA ESPAÑOLA SA DE CV', 'G01', '080CF54E-F9DB-4470-BF0D-A8613DC10B24', '2022-02-08T21:58:56', 'SPR190613I52', 'WUCP5ykONZrtAg97dDf4bx/GIldE0diCw1LDmCUci3YI31ocsvAQJCRTrWJ9JNkr3UrD1CyO//vxhP65DvmuNGyK0+QrQn7FDvEX+vo0bslbMP+UprBevco4JYW3BLazIpU1rSmoiu1K0ViAZCpdRk+o13uV8be4SQGOPclLsTljUxcYdn2qHLlP+EhSyqEb7MNUTQvY44MpjPlRRfgHnhDVQZDGZyta1M5jHrQioIl625Ju6PFDNMMyt+VltFb9omWpa7QxWuIaQ/jpmtWxqVGZjjpNj6aT8g1gjnr+dqyBQ5FpRunDfj9YgQJAs5Dug4S6Mwzj474egKjLKYlUoQ==', 'CP1_P1_DR1', '2021-12-15T00:00:00', '01', 'MXN', '1', '200.00', '', '', '', '', '', '', '', '', '', '', '', '', '', 'bfc36522-4b8e-45c4-8f14-d11b289f9eb7', '', '', 'MXN', '1', '1', '200.00', '200.00', '0.00']
        self.assertListEqual(first_row, row_list[0])

 #DONE
    def test_rows_pagos20_01_empty_char(self):
        start = time.time()
        sax_handler = CFDI40SAXHandler().use_pagos20()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos20/pago_empty_chars.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoPagos20Formatter(cfdi_data, empty_char='-')
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        end_time = start - time.time()
        print(row_list[0])
        first_row = ['4.0', 'Serie', 'Folio', '2021-12-16T15:40:21', '30001000000400002444', '0', '-', '0.0', 'XXX', '-', 'P', '-', '-', '-', '20008', 'XAXX010101000', 'PUBLICO GENERAL', '601', 'XAXX010101000', 'Nombre', 'G01', '080CF54E-F9DB-4470-BF0D-A8613DC10B24', '2022-02-08T21:58:56', 'SPR190613I52', 'WUCP5ykONZrtAg97dDf4bx/GIldE0diCw1LDmCUci3YI31ocsvAQJCRTrWJ9JNkr3UrD1CyO//vxhP65DvmuNGyK0+QrQn7FDvEX+vo0bslbMP+UprBevco4JYW3BLazIpU1rSmoiu1K0ViAZCpdRk+o13uV8be4SQGOPclLsTljUxcYdn2qHLlP+EhSyqEb7MNUTQvY44MpjPlRRfgHnhDVQZDGZyta1M5jHrQioIl625Ju6PFDNMMyt+VltFb9omWpa7QxWuIaQ/jpmtWxqVGZjjpNj6aT8g1gjnr+dqyBQ5FpRunDfj9YgQJAs5Dug4S6Mwzj474egKjLKYlUoQ==', 'CP1_P1_DR1', '2021-12-02T00:18:10', '01', 'USD', '-', '14000.00', '-', '-', '-', '-', '-', '-', '1488703.81', '0.00', '2.00', '0.00', '0.00', 'BEDC8964-7E57-4604-9968-7E01378E8706', 'Serie3', 'Folio3', 'MXN', '1.329310', '1', '5000.00', '2000.00', '3000.00']
        self.assertListEqual(first_row, row_list[0])
        self.assertLess(end_time, 0.01)

    #DONE
    def test_rows_pagos20_01_safe_numerics(self):
        start = time.time()
        sax_handler = CFDI40SAXHandler().use_pagos20()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos20/pago_safe_numbers.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoPagos20Formatter(cfdi_data, safe_numerics=True)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        end_time = start - time.time()
        print(row_list[0])
        first_row = ['4.0', 'Serie', 'Folio', '2021-12-16T15:40:21', '30001000000400002444', '0', '0.00', '0.0', 'XXX', '1.00', 'P', '', '', '', '20008', 'XAXX010101000', 'PUBLICO GENERAL', '601', 'XAXX010101000', 'Nombre', 'G01', '080CF54E-F9DB-4470-BF0D-A8613DC10B24', '2022-02-08T21:58:56', 'SPR190613I52', 'WUCP5ykONZrtAg97dDf4bx/GIldE0diCw1LDmCUci3YI31ocsvAQJCRTrWJ9JNkr3UrD1CyO//vxhP65DvmuNGyK0+QrQn7FDvEX+vo0bslbMP+UprBevco4JYW3BLazIpU1rSmoiu1K0ViAZCpdRk+o13uV8be4SQGOPclLsTljUxcYdn2qHLlP+EhSyqEb7MNUTQvY44MpjPlRRfgHnhDVQZDGZyta1M5jHrQioIl625Ju6PFDNMMyt+VltFb9omWpa7QxWuIaQ/jpmtWxqVGZjjpNj6aT8g1gjnr+dqyBQ5FpRunDfj9YgQJAs5Dug4S6Mwzj474egKjLKYlUoQ==', 'CP1_P1_DR1', '2021-12-02T00:18:10', '01', 'USD', '1.00', '14000.00', '', '', '', '', '', '', '1488703.81', '0.00', '2.00', '0.00', '0.00', 'BEDC8964-7E57-4604-9968-7E01378E8706', 'Serie3', 'Folio3', 'MXN', '1.329310', '1', '5000.00', '2000.00', '3000.00']
        self.assertListEqual(first_row, row_list[0])
        self.assertLess(end_time, 0.01)

    def test_rows_pagos20_01_empty_char_safe_numerics(self):
        start = time.time()
        sax_handler = CFDI40SAXHandler().use_pagos20()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos20/pago_safe_numbers.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoPagos20Formatter(cfdi_data, empty_char='-', safe_numerics=True)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        end_time = start - time.time()
        print(row_list[0])
        first_row = ['4.0', 'Serie', 'Folio', '2021-12-16T15:40:21', '30001000000400002444', '0', '0.00', '0.0', 'XXX', '1.00', 'P', '-', '-', '-', '20008', 'XAXX010101000', 'PUBLICO GENERAL', '601', 'XAXX010101000', 'Nombre', 'G01', '080CF54E-F9DB-4470-BF0D-A8613DC10B24', '2022-02-08T21:58:56', 'SPR190613I52', 'WUCP5ykONZrtAg97dDf4bx/GIldE0diCw1LDmCUci3YI31ocsvAQJCRTrWJ9JNkr3UrD1CyO//vxhP65DvmuNGyK0+QrQn7FDvEX+vo0bslbMP+UprBevco4JYW3BLazIpU1rSmoiu1K0ViAZCpdRk+o13uV8be4SQGOPclLsTljUxcYdn2qHLlP+EhSyqEb7MNUTQvY44MpjPlRRfgHnhDVQZDGZyta1M5jHrQioIl625Ju6PFDNMMyt+VltFb9omWpa7QxWuIaQ/jpmtWxqVGZjjpNj6aT8g1gjnr+dqyBQ5FpRunDfj9YgQJAs5Dug4S6Mwzj474egKjLKYlUoQ==', 'CP1_P1_DR1', '2021-12-02T00:18:10', '01', 'USD', '1.00', '14000.00', '-', '-', '-', '-', '-', '-', '1488703.81', '0.00', '2.00', '0.00', '0.00', 'BEDC8964-7E57-4604-9968-7E01378E8706', 'Serie3', 'Folio3', 'MXN', '1.329310', '1', '5000.00', '2000.00', '3000.00']
        self.assertListEqual(first_row, row_list[0])
        self.assertLess(end_time, 0.01)

    def test_rows_pagos20_multi_tfd(self):
        sax_handler = CFDI40SAXHandler().use_pagos20()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos20/pago_stamped_multiple_tfd.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoPagos20Formatter(cfdi_data)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        self.assertEqual(len(row_list), 2, 'Different rows returned.')
        for row in row_list:
            self.assertEqual(len(row), len(formatter.get_columns_names()), 'Different length of columns')
        expected_rows = [
            ['4.0', 'Serie', 'Folio', '2022-02-08T00:18:10', '30001000000400002434', '0', '', '0.00', 'XXX', '', 'P',
             '', '', '', '20000', 'EKU9003173C9', 'ESCUELA KEMPER URGATE SA DE CV', '601', 'URE180429TM6',
             'UNIVERSIDAD ROBOTICA ESPAÑOLA SA DE CV', 'G01', '080CF54E-F9DB-4470-BF0D-A8613DC10B24',
             '2022-02-08T21:58:56', 'SPR190613I52',
             'WUCP5ykONZrtAg97dDf4bx/GIldE0diCw1LDmCUci3YI31ocsvAQJCRTrWJ9JNkr3UrD1CyO//vxhP65DvmuNGyK0+QrQn7FDvEX+vo0bslbMP+UprBevco4JYW3BLazIpU1rSmoiu1K0ViAZCpdRk+o13uV8be4SQGOPclLsTljUxcYdn2qHLlP+EhSyqEb7MNUTQvY44MpjPlRRfgHnhDVQZDGZyta1M5jHrQioIl625Ju6PFDNMMyt+VltFb9omWpa7QxWuIaQ/jpmtWxqVGZjjpNj6aT8g1gjnr+dqyBQ5FpRunDfj9YgQJAs5Dug4S6Mwzj474egKjLKYlUoQ==',
             'CP1_P1_DR1', '2021-12-15T00:00:00', '01', 'MXN', '1', '200.00', '', '', '', '', '', '', '', '', '', '',
             '', '', '', 'bfc36522-4b8e-45c4-8f14-d11b289f9eb7', '', '', 'MXN', '1', '1', '200.00', '200.00', '0.00'],
            ['4.0', 'Serie', 'Folio', '2022-02-08T00:18:10', '30001000000400002434', '0', '', '0.00', 'XXX', '', 'P',
             '', '', '', '20000', 'EKU9003173C9', 'ESCUELA KEMPER URGATE SA DE CV', '601', 'URE180429TM6',
             'UNIVERSIDAD ROBOTICA ESPAÑOLA SA DE CV', 'G01', '080CF54E-F9DB-4470-BF0D-A8613DC10B24',
             '2022-02-08T21:58:56', 'SPR190613I52',
             'WUCP5ykONZrtAg97dDf4bx/GIldE0diCw1LDmCUci3YI31ocsvAQJCRTrWJ9JNkr3UrD1CyO//vxhP65DvmuNGyK0+QrQn7FDvEX+vo0bslbMP+UprBevco4JYW3BLazIpU1rSmoiu1K0ViAZCpdRk+o13uV8be4SQGOPclLsTljUxcYdn2qHLlP+EhSyqEb7MNUTQvY44MpjPlRRfgHnhDVQZDGZyta1M5jHrQioIl625Ju6PFDNMMyt+VltFb9omWpa7QxWuIaQ/jpmtWxqVGZjjpNj6aT8g1gjnr+dqyBQ5FpRunDfj9YgQJAs5Dug4S6Mwzj474egKjLKYlUoQ==',
             'CP1_P1_DR1', '2021-12-15T00:00:00', '01', 'MXN', '1', '200.00', '', '', '', '', '', '', '', '', '', '',
             '', '', '', 'bfc36522-4b8e-45c4-8f14-d11b289f9eb7', '', '', 'MXN', '1', '1', '200.00', '200.00', '0.00']
        ]
        self.assertListEqual(expected_rows, row_list)
    
    def test_rows_pagos20_complete(self):
        sax_handler = CFDI40SAXHandler().use_pagos20()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos20/pago_stamped.xml')
        #Fix missing TFD in file.
        cfdi_data['tfd11'] = [{'version': '1.1', 'no_certificado_sat': '20001000000300022323', 'uuid': '9D81C696-0401-4F85-B703-6E0D3AFD6057', 'fecha_timbrado': '2019-03-29T17:42:38', 'rfc_prov_cert': 'AAA010101AAA', 'sello_cfd': 'G3knPza1r8hfxSb+46JBRAYoQIUTVU2Uqlw/qiMLbzKkqrUs2zs5GVRjf0DJEm5mIGZIC3/+q/FdU1A4zr9RCXWM66QmtK7AAlkT4HSrX9NlCoJylwRzRW6bxuchfy8ryFmWIetAOU2U1brWLSSYqCtc86m4iIBId6kDOSIr+/Tpz2Q3rDHhmtlJyJ2ovy1rjLO0mZpbwhwOKg6Mo1+NeEuGk4UfQu8gfRgv9mOnbiNkfiJHzvuRJnUXYrL/9D1gDQ6gjW8t75W/yYN+Gf2TmpyTnOkYZbFqrJ8udt7rZjXsODLapD7cV4bjsLIYxOWHgXEIgrTjB57m2POrfb72wQ==', 'sello_sat': 'ULW1tcO5xJKR9ZLcY9+ls9Zg8rPXROVvbVVTWOnOJ/H88Om4ZRXWdjrHzrPv+Zre4gS0mcDaxuzwNHRhU5YKvONbFgme31mgsadWubTQyh10JGzhuYIzsGhnFBuYmNaKVR/vYbd9X4RBRfiggRW+tSIv8qFZGZZ1RSznmxc3FUP//tR1uGKVVnivs590DQV5UxKAVKXtF0T/dPwncKuOHcheFP6PdL+ToJB9mRz8Xl9Ag7x+WuHOBwdzx2lpEj8yms1d/CKgxWGFOXUEhpKsQXGm1MYYMLCo5/wNG6oC6F9FkvcV5rNji3Qna/P4OHXduL0UIz2FqvIK65NeRxgilQ=='}]
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoPagos20Formatter(cfdi_data)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        self.assertEqual(len(row_list), 1, 'Different rows returned.')
        for row in row_list:
            print(len(formatter.get_columns_names()))
            self.assertEqual(len(row), len(formatter.get_columns_names()), 'Different length of columns')
            print(row)
        expected_rows = [
            ['4.0', 'Serie', 'Folio', '2022-02-08T00:18:10', '30001000000400002434', '0', '', '0.00', 'XXX', '', 'P',
             '', '', '', '20000', 'EKU9003173C9', 'ESCUELA KEMPER URGATE SA DE CV', '601', 'URE180429TM6',
             'UNIVERSIDAD ROBOTICA ESPAÑOLA SA DE CV', 'G01', '9D81C696-0401-4F85-B703-6E0D3AFD6057',
             '2019-03-29T17:42:38', 'AAA010101AAA',
             'G3knPza1r8hfxSb+46JBRAYoQIUTVU2Uqlw/qiMLbzKkqrUs2zs5GVRjf0DJEm5mIGZIC3/+q/FdU1A4zr9RCXWM66QmtK7AAlkT4HSrX9NlCoJylwRzRW6bxuchfy8ryFmWIetAOU2U1brWLSSYqCtc86m4iIBId6kDOSIr+/Tpz2Q3rDHhmtlJyJ2ovy1rjLO0mZpbwhwOKg6Mo1+NeEuGk4UfQu8gfRgv9mOnbiNkfiJHzvuRJnUXYrL/9D1gDQ6gjW8t75W/yYN+Gf2TmpyTnOkYZbFqrJ8udt7rZjXsODLapD7cV4bjsLIYxOWHgXEIgrTjB57m2POrfb72wQ==',
             'CP1_P1_DR1', '2021-12-15T00:00:00', '01', 'MXN', '1', '200.00', '', '', '', '', '', '', '', '', '', '',
             '', '', '', 'bfc36522-4b8e-45c4-8f14-d11b289f9eb7', '', '', 'MXN', '1', '1', '200.00', '200.00', '0.00']
        ]
        self.assertListEqual(expected_rows, row_list)