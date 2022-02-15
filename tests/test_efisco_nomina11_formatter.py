from pycfdi_transform import CFDI32SAXHandler
from pycfdi_transform.formatters.nomina11.efisco_nomina11_formatter import EfiscoNomina11Formatter

import unittest
import time

class TestEfiscoNomina11Formatter(unittest.TestCase):

    def test_columns_names_nomina11(self):
        formatter = EfiscoNomina11Formatter({'cfdi32': {}})
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
            "TIPONOMINA",
            "FECHAPAGO",
            "FECHAINICIALPAGO",
            "FECHAFINALPAGO",
            "NUMDIASPAGADOS",
            "TOTALPERCEPCIONES",
            "TOTALDEDUCCIONES",
            "TOTALOTROSPAGOS",
            "CURPEMISOR",
            "REGISTROPATRONAL",
            "RFCPATRONORIGEN",
            "CURPRECEPTOR",
            "NUMSEGURIDADSOCIAL",
            "FECHAINICIORELLABORAL",
            "SINDICALIZADO",
            "TIPOJORNADA",
            "TIPOREGIMEN",
            "NUMEMPLEADO",
            "DEPARTAMENTO",
            "PUESTO",
            "RIESGOPUESTO",
            "BANCO",
            "CUENTABANCARIA",
            "ANTIGÜEDAD",
            "TIPOCONTRATO",
            "PERIODICIDADPAGO",
            "SALARIOBASECOTAPOR",
            "SALARIODIARIOINTEGRADO",
            "CLAVEENTFED",
            "TOTALSUELDOS",
            "TOTALSEPARACIONINDEMNIZACION",
            "TOTALJUBILACIONPENSIONRETIRO",
            "TOTALGRAVADO",
            "TOTALEXENTO",
            "TOTALOTRASDEDUCCIONES",
            "TOTALIMPUESTOSRETENIDOSN",
            "DEDUCCION_PERCEPCION_OTROS",
            "CLAVE_DEDUCCION_PERCEPCION",
            "TIPO_DEDUCCION_PERCEPCION",
            "CONCEPTO",
            "IMPORTEGRAVADO",
            "IMPORTEEXENTO"
        ]
        self.assertListEqual(columns_expected, formatter.get_columns_names())
    
    def test_initialize_class_error_nomina11(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoNomina11Formatter(cfdi_data=None)
        self.assertEqual('El Formatter debe recibir el objeto devuelto por la transformación el debe ser un dict.', str(ex.exception))

    def test_initialize_class_error_version_nomina11(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoNomina11Formatter({'cfdi33': {}})
        self.assertEqual('Este formatter únicamente soporta datos de cfdi32.', str(ex.exception))

    def test_formatter_error_tfd_nomina11(self):
        sax_handler = CFDI32SAXHandler().use_nomina11()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/nomina11/nom_complete.xml')
        cfdi_data.pop('nomina11')
        formatter = EfiscoNomina11Formatter(cfdi_data)
        self.assertFalse(formatter.can_format())
        self.assertEqual(formatter.get_errors(), 'Not nomina11 in data.')

    def test_formatter_error_tfdpagos_nomina11(self):
        sax_handler = CFDI32SAXHandler().use_nomina11()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/nomina11/nom_complete.xml')
        cfdi_data.pop('nomina11')
        formatter = EfiscoNomina11Formatter(cfdi_data)
        self.assertFalse(formatter.can_format())
        self.assertEqual(formatter.get_errors(), 'Not nomina11 in data.')

    def test_rows_nomina11_01(self):
        sax_handler = CFDI32SAXHandler().use_nomina11()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/nomina11/nom_complete.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoNomina11Formatter(cfdi_data)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        self.assertEqual(len(row_list), 9, 'No rows returned.')
        d = len(formatter.get_columns_names())
        for row in row_list:
            self.assertEqual(len(row), len(formatter.get_columns_names()), 'Different length of columns')

        expected_rows = [
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'P', '139', '001', 'Sueldos, Salarios Rayas y Jornales', '10000.00', '0.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'P', '164', '002', 'Gratificación Anual (Aguinaldo)', '1000.00', '0.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'P', '112', '004', 'Reembolso gastos médicos dentales', '1000.00', '0.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'P', '563', '029', 'Bonos de Despensa', '0.00', '379.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'P', '545', '019', 'Horas Extra', '1000.00', '0.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'D', '223', '001', 'Seguro Social', '278.39', '0.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'D', '231', '002', 'ISR', '2053.71', '0.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'D', '653', '020', 'Ausencia', '1000.00', '0.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'D', '262', '007', 'Pensión alimenticia', '0.00', '0.00'],

        ]
        self.assertListEqual(expected_rows, row_list)


    def test_rows_nomina11_01_empty_char(self):
        sax_handler = CFDI32SAXHandler().use_nomina11()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/nomina11/nom_empty_chars.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoNomina11Formatter(cfdi_data, empty_char='-')
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()

        expected_rows = [
           ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '-', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '-', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', '-', '', 'XEXX010101HNEXXXA4', '-', '', '', '-', '1', '9872', 'DPTO', '-', '1', '113', '000000000000000000', '-', '', 'Quincenal', '-', '-', '', '', '', '', '-', '-', '', '', 'P', '139', '001', 'Sueldos, Salarios Rayas y Jornales', '', ''],
           ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '-', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '-', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', '-', '', 'XEXX010101HNEXXXA4', '-', '', '', '-', '1', '9872', 'DPTO', '-', '1', '113', '000000000000000000', '-', '', 'Quincenal', '-', '-', '', '', '', '', '-', '-', '', '', 'D', '223', '001', 'Seguro Social', '', '0.00']
        ]
        self.assertListEqual(expected_rows, row_list)


    def test_rows_nomina11_01_safe_numerics(self):
        sax_handler = CFDI32SAXHandler().use_nomina11()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/nomina11/nom_safe_numerics.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoNomina11Formatter(cfdi_data, safe_numerics=True)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        for row in row_list:
            print(row)
        expected_rows = [
          ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '1.00', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '0.00', '0.00', '', '', '', '', '0.00', '0.00', '', '', 'P', '139', '001', 'Sueldos, Salarios Rayas y Jornales', '', ''],
          ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '1.00', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '0.00', '0.00', '', '', '', '', '0.00', '0.00', '', '', 'D', '223', '001', 'Seguro Social', '', '0.00']
        ]
        self.assertListEqual(expected_rows, row_list)

    def test_rows_nomina11_01_empty_char_safe_numerics(self):
        sax_handler = CFDI32SAXHandler().use_nomina11()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/nomina11/nom_safe_numerics.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoNomina11Formatter(cfdi_data, empty_char='-', safe_numerics=True)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        self.assertEqual(len(row_list), 2, 'No rows returned.')
        for row in row_list:
            self.assertEqual(len(row), len(formatter.get_columns_names()), 'Different length of columns')
            print(row)
        expected_rows = [
          ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '1.00', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '-', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '0.00', '0.00', '', '', '', '', '0.00', '0.00', '', '', 'P', '139', '001', 'Sueldos, Salarios Rayas y Jornales', '', ''],
          ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '1.00', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '-', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '0.00', '0.00', '', '', '', '', '0.00', '0.00', '', '', 'D', '223', '001', 'Seguro Social', '', '0.00']

        ]

        self.assertListEqual(expected_rows, row_list)

    def test_rows_nomina11_02(self):
        start = time.time()
        sax_handler = CFDI32SAXHandler().use_nomina11()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/nomina11/nom_complete.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoNomina11Formatter(cfdi_data)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        self.assertEqual(len(row_list), 9, 'No rows returned.')
        for row in row_list:
            print(row)
            self.assertEqual(len(row), len(formatter.get_columns_names()), 'Different length of columns')
        expected_rows = [
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'P', '139', '001', 'Sueldos, Salarios Rayas y Jornales', '10000.00', '0.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'P', '164', '002', 'Gratificación Anual (Aguinaldo)', '1000.00', '0.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'P', '112', '004', 'Reembolso gastos médicos dentales', '1000.00', '0.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'P', '563', '029', 'Bonos de Despensa', '0.00', '379.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'P', '545', '019', 'Horas Extra', '1000.00', '0.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'D', '223', '001', 'Seguro Social', '278.39', '0.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'D', '231', '002', 'ISR', '2053.71', '0.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'D', '653', '020', 'Ausencia', '1000.00', '0.00'],
            ['3.2', 'A', '1', '2015-03-05T10:33:48', '20001000000100005867', '35000.00', '0.00', '40600.00', 'Pesos', '', 'egreso', 'No Identificado', 'PAGO EN UNA SOLA EXHIBICION', '', 'Zapopan, Jalisco', 'AAA010101AAA', 'Empresa de Pruebas SA DE CV', 'Regimen General de Ley Personas Morales de Prueba', 'CACX7605101P8', 'EMPLEADO DE PRUEBA', '', 'CD13D35E-2FCF-4A23-ADCA-51F2E48B8018', '2014-04-03T18:17:02', '', 'MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=', '', '2013-11-15', '2014-11-01', '2014-11-15', '15', '', '', '', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2009-06-01', '', 'Diurna', '1', '9872', 'DPTO', 'ADMIN', '1', '113', '000000000000000000', '228', 'Base', 'Quincenal', '10000.00', '696.80', '', '', '', '', '13000.00', '379.00', '', '', 'D', '262', '007', 'Pensión alimenticia', '0.00', '0.00'],
        ]
        self.assertListEqual(expected_rows, row_list)
        end_time = time.time() - start
        self.assertLess(end_time, 0.05)
