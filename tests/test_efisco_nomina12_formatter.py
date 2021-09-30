from pycfdi_transform import CFDI33SAXHandler
from pycfdi_transform.formatters.nomina12.efisco_nomina12_formatter import EfiscoNomina12Formatter
import unittest

class TestEfiscoNomina12Formatter(unittest.TestCase):

    def test_columns_names_nomina12(self):
        formatter = EfiscoNomina12Formatter({'cfdi33': {}})
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
    
    def test_initialize_class_error_nomina12(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoNomina12Formatter(cfdi_data=None)
        self.assertEqual('El Formatter debe recibir el objeto devuelto por la transformación el debe ser un dict.', str(ex.exception))
    
    def test_initialize_class_error_version_nomina12(self):
        with self.assertRaises(AssertionError) as ex:
            EfiscoNomina12Formatter({'cfdi32': {}})
        self.assertEqual('Este formatter únicamente soporta datos de cfdi33.', str(ex.exception))
    
    def test_formatter_error_tfd_nomina12(self):
        sax_handler = CFDI33SAXHandler().use_nomina12()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/nomina12/nom_complete.xml')
        formatter = EfiscoNomina12Formatter(cfdi_data)
        self.assertFalse(formatter.can_format())
        self.assertEqual(formatter.get_errors(), 'Not tfd11 in data.')
    
    def test_formatter_error_tfdpagos_nomina12(self):
        sax_handler = CFDI33SAXHandler().use_nomina12()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/nomina12/nom_complete.xml')
        cfdi_data.pop('nomina12')
        formatter = EfiscoNomina12Formatter(cfdi_data)
        self.assertFalse(formatter.can_format())
        self.assertEqual(formatter.get_errors(), 'Not nomina12 in data.')
    
    def test_rows_nomina12_01(self):
        sax_handler = CFDI33SAXHandler().use_nomina12()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/nomina12/nomina12_01.xml')
        self.assertIsNotNone(cfdi_data)
        formatter = EfiscoNomina12Formatter(cfdi_data)
        self.assertTrue(formatter.can_format())
        self.assertEqual(formatter.get_errors(), '', 'Errors obtained.')
        row_list = formatter.dict_to_columns()
        self.assertEqual(len(row_list), 4, 'No rows returned.')
        for row in row_list:
            self.assertEqual(len(row), len(formatter.get_columns_names()), 'Different length of columns')
        expected_rows = [
            ['3.3', '1', '1', '2021-05-28T09:46:01', '30001000000400002434', '1598.67', '98.61', '1500.06', 'MXN', '', 'N', 'PUE', '99', '', '45400', 'EKU9003173C9', 'ESCUELA KEMPER URGATE SA DE CV', '601', 'KICR630120NX3', 'EMPLEADO 001', 'P01', '862F8B0E-6B0B-4696-916F-CEA6F0C91AF7', '2021-05-28T13:19:16', 'SPR190613I52', 'Uh47FTmCHHGxgW6dkOSBIPZjwtr4TtRq6VHaTQnpM7jj8sFHIl656SZBl5XtfsAh1rkTtYOIBCTZ7AWr5JdNDSIwgiKjxbOqkzPaZv3RhQ3G4hnJcj3wG146bI5wrnKdetbqljajLEvIzdGZApLs7TffcEstko+4IzYBQ8QEVDapLbrmtL2XO8DoUf1JLZ4PDTH8QkRT7u8yOj5NYACFzUAQEN9hbN7+OAKWoxHP1U3Zs3M8WoisFOoBmLgzoE7EoWqxd4KJkGCVRNGj3b3KCVYGDdITjafx3VQ3R0Rp8FL9iOKpOQe9iMXeD6Fx8WNLF3r4D1BZSvC/fd8Kjgib/g==', 'O', '2019-08-30', '2019-08-26', '2019-09-01', '7', '1598.66', '98.61', '0.01', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2019-01-07', 'No', '02', '02', '222222', '', '', '2', '', '', 'P34W', '01', '02', '238.7', '228.38', 'JAL', '1598.66', '', '', '1598.66', '0.00', '39.68', '58.93', 'P', '001', '001', 'Sueldos, Salarios Rayas y Jornales', '1598.66', '0.00'],
            ['3.3', '1', '1', '2021-05-28T09:46:01', '30001000000400002434', '1598.67', '98.61', '1500.06', 'MXN', '', 'N', 'PUE', '99', '', '45400', 'EKU9003173C9', 'ESCUELA KEMPER URGATE SA DE CV', '601', 'KICR630120NX3', 'EMPLEADO 001', 'P01', '862F8B0E-6B0B-4696-916F-CEA6F0C91AF7', '2021-05-28T13:19:16', 'SPR190613I52', 'Uh47FTmCHHGxgW6dkOSBIPZjwtr4TtRq6VHaTQnpM7jj8sFHIl656SZBl5XtfsAh1rkTtYOIBCTZ7AWr5JdNDSIwgiKjxbOqkzPaZv3RhQ3G4hnJcj3wG146bI5wrnKdetbqljajLEvIzdGZApLs7TffcEstko+4IzYBQ8QEVDapLbrmtL2XO8DoUf1JLZ4PDTH8QkRT7u8yOj5NYACFzUAQEN9hbN7+OAKWoxHP1U3Zs3M8WoisFOoBmLgzoE7EoWqxd4KJkGCVRNGj3b3KCVYGDdITjafx3VQ3R0Rp8FL9iOKpOQe9iMXeD6Fx8WNLF3r4D1BZSvC/fd8Kjgib/g==', 'O', '2019-08-30', '2019-08-26', '2019-09-01', '7', '1598.66', '98.61', '0.01', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2019-01-07', 'No', '02', '02', '222222', '', '', '2', '', '', 'P34W', '01', '02', '238.7', '228.38', 'JAL', '1598.66', '', '', '1598.66', '0.00', '39.68', '58.93', 'D', '002', '002', 'ISR', '58.93', '0.00'],
            ['3.3', '1', '1', '2021-05-28T09:46:01', '30001000000400002434', '1598.67', '98.61', '1500.06', 'MXN', '', 'N', 'PUE', '99', '', '45400', 'EKU9003173C9', 'ESCUELA KEMPER URGATE SA DE CV', '601', 'KICR630120NX3', 'EMPLEADO 001', 'P01', '862F8B0E-6B0B-4696-916F-CEA6F0C91AF7', '2021-05-28T13:19:16', 'SPR190613I52', 'Uh47FTmCHHGxgW6dkOSBIPZjwtr4TtRq6VHaTQnpM7jj8sFHIl656SZBl5XtfsAh1rkTtYOIBCTZ7AWr5JdNDSIwgiKjxbOqkzPaZv3RhQ3G4hnJcj3wG146bI5wrnKdetbqljajLEvIzdGZApLs7TffcEstko+4IzYBQ8QEVDapLbrmtL2XO8DoUf1JLZ4PDTH8QkRT7u8yOj5NYACFzUAQEN9hbN7+OAKWoxHP1U3Zs3M8WoisFOoBmLgzoE7EoWqxd4KJkGCVRNGj3b3KCVYGDdITjafx3VQ3R0Rp8FL9iOKpOQe9iMXeD6Fx8WNLF3r4D1BZSvC/fd8Kjgib/g==', 'O', '2019-08-30', '2019-08-26', '2019-09-01', '7', '1598.66', '98.61', '0.01', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2019-01-07', 'No', '02', '02', '222222', '', '', '2', '', '', 'P34W', '01', '02', '238.7', '228.38', 'JAL', '1598.66', '', '', '1598.66', '0.00', '39.68', '58.93', 'D', '001', '001', 'Seguridad social', '39.68', '0.00'],
            ['3.3', '1', '1', '2021-05-28T09:46:01', '30001000000400002434', '1598.67', '98.61', '1500.06', 'MXN', '', 'N', 'PUE', '99', '', '45400', 'EKU9003173C9', 'ESCUELA KEMPER URGATE SA DE CV', '601', 'KICR630120NX3', 'EMPLEADO 001', 'P01', '862F8B0E-6B0B-4696-916F-CEA6F0C91AF7', '2021-05-28T13:19:16', 'SPR190613I52', 'Uh47FTmCHHGxgW6dkOSBIPZjwtr4TtRq6VHaTQnpM7jj8sFHIl656SZBl5XtfsAh1rkTtYOIBCTZ7AWr5JdNDSIwgiKjxbOqkzPaZv3RhQ3G4hnJcj3wG146bI5wrnKdetbqljajLEvIzdGZApLs7TffcEstko+4IzYBQ8QEVDapLbrmtL2XO8DoUf1JLZ4PDTH8QkRT7u8yOj5NYACFzUAQEN9hbN7+OAKWoxHP1U3Zs3M8WoisFOoBmLgzoE7EoWqxd4KJkGCVRNGj3b3KCVYGDdITjafx3VQ3R0Rp8FL9iOKpOQe9iMXeD6Fx8WNLF3r4D1BZSvC/fd8Kjgib/g==', 'O', '2019-08-30', '2019-08-26', '2019-09-01', '7', '1598.66', '98.61', '0.01', '', 'A0000000000', '', 'XEXX010101HNEXXXA4', '00000000000', '2019-01-07', 'No', '02', '02', '222222', '', '', '2', '', '', 'P34W', '01', '02', '238.7', '228.38', 'JAL', '1598.66', '', '', '1598.66', '0.00', '39.68', '58.93', 'O', '002', '002', 'Subsidio para el empleo (efectivamente entregado al trabajador)', '0.00', '0.01']
        ]
        self.assertListEqual(expected_rows, row_list)