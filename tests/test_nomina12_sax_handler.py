from pycfdi_transform import CFDI33SAXHandler, SchemaHelper
from lxml import etree
import unittest

class TestNomina12SAXHandler(unittest.TestCase):
    def test_transform_file_complete_nom(self):
        sax_handler = CFDI33SAXHandler().use_nomina12()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/nomina12/nom_complete.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': '"',
                'folio': '/>KA',
                'fecha': '2018-01-10T07:22:51',
                'no_certificado': '47217725691977968749',
                'subtotal': '5858580.234906',
                'descuento': '9061950.234906',
                'total': '7679420.234906',
                'moneda': 'SGD',
                'tipo_cambio': '8016540.234907',
                'tipo_comprobante': 'N',
                'metodo_pago': 'PPD',
                'forma_pago': '01',
                'condiciones_pago': '}_',
                'lugar_expedicion': '45734',
                'sello':'string',
                'certificado':'string',
                'confirmacion':'8p7F3',
                'emisor': {
                    'rfc': 'J&O750807563',
                    'nombre': 'Q~',
                    'regimen_fiscal': '611'
                },
                'receptor': {
                    'rfc': 'ÑÑD68010919A',
                    'nombre': '^*p_',
                    'residencia_fiscal': 'PRI',
                    'num_reg_id_trib': 'string',
                    'uso_cfdi': 'D01'
                },
                'conceptos': [],
                'impuestos': {
                    'retenciones': [
                        {
                            'impuesto': '001', 
                            'importe': '1900460.234906'
                        }, 
                        {
                            'impuesto': '002', 
                            'importe': '8425580.234906'
                        }, 
                        {
                            'impuesto': '003', 
                            'importe': '6550940.234906'
                        }
                    ],
                    'traslados': [
                        {
                            'impuesto': '001', 
                            'tipo_factor': 'Cuota', 
                            'tasa_o_cuota': '5992320.234906', 
                            'importe': '3311220.234906'
                        }
                    ], 
                    'total_impuestos_traslados': '5553360.234906',
                    'total_impuestos_retenidos': '8065990.234906'
                },
                'complementos': 'Nomina',
                'addendas': ''
            },
            'tfd11': [],
            'nomina12': [
                {
                    'version': '1.2',
                    'tipo_nomina': 'O',
                    'fecha_pago': '1972-01-05',
                    'fecha_inicial_pago': '1994-08-28',
                    'fecha_final_pago': '1995-04-17',
                    'num_dias_pagados': '2997.357',
                    'total_percepciones': '6450960.23',
                    'total_deducciones': '4226100.23',
                    'total_otros_pagos': '7815140.23',
                    'emisor': {
                        'curp': 'JAQE081121MOCZGNW2',
                        'registro_patronal': '"}~',
                        'rfc_patron_origen': 'KOÑ7908288LA',
                        'entidad_SNCF': {
                            'origen_recurso': 'IP',
                            'monto_recurso_propio': '9301520.23'
                        }
                    },
                    'receptor': {
                        'curp': 'VXNL701131HQTRYB07',
                        'num_seguridad_social': '59904',
                        'fecha_inicio_rel_laboral': '2010-09-02',
                        'antigüedad': 'P2Y2D',
                        'tipo_contrato': '09',
                        'sindicalizado': 'Sí',
                        'tipo_jornada': '05',
                        'tipo_regimen': '09',
                        'num_empleado': '~~',
                        'departamento': 'W',
                        'puesto': '}}8',
                        'riesgo_puesto': '3',
                        'periodicidad_pago': '06',
                        'banco': '647',
                        'cuenta_bancaria': '1234567890',
                        'salario_base_cot_apor': '8635520.23',
                        'salario_diario_integrado': '2928750.23',
                        'clave_ent_fed': 'VT',
                        'subcontratacion': [
                            {
                                'rfc_labora': '&ÑEL561104H5A',
                                'porcentaje_tiempo': '91.44'
                            }, 
                            {
                                'rfc_labora': 'ÑÑL&020703408',
                                'porcentaje_tiempo': '50.81'
                            }
                        ]
                    },
                    'percepciones': {
                        'total_sueldos': '4960830.23',
                        'total_separacion_indemnizacion': '3741880.23',
                        'total_jubilacion_pension_retiro': '7499380.23',
                        'total_gravado': '2472530.23',
                        'total_exento': '8274700.23',
                        'percepcion': [
                            {
                                'tipo_percepcion': '019',
                                'clave': '9~}m', 
                                'concepto': '~K', 
                                'importe_gravado': '9232380.23', 
                                'importe_exento': '6681000.23', 
                                'horas_extra': []
                            }, 
                            {
                                'tipo_percepcion': '031', 
                                'clave': '~^["4}~a', 
                                'concepto': '}U~', 
                                'importe_gravado': '6444510.23', 
                                'importe_exento': '190260.23', 
                                'horas_extra': [
                                    {
                                        'dias': '4890', 
                                        'tipo_horas': '03', 
                                        'horas_extra': '7170', 
                                        'importe_pagado': '4190840.23'
                                    }
                                ], 
                                'acciones_o_titulos': {
                                    'valor_mercado': '5791520.234907', 
                                    'precio_al_otorgarse': '2416940.234907'
                                }
                            }, 
                            {
                                'tipo_percepcion': '013', 
                                'clave': '~eeE}}', 
                                'concepto': '~', 
                                'importe_gravado': '3007460.23', 
                                'importe_exento': '352260.23', 
                                'horas_extra': [
                                    {
                                        'dias': '4444', 
                                        'tipo_horas': '01', 
                                        'horas_extra': '7306', 
                                        'importe_pagado': '4568110.23'
                                    }, 
                                    {
                                        'dias': '559', 
                                        'tipo_horas': '01', 
                                        'horas_extra': '1594', 
                                        'importe_pagado': '1797550.23'
                                    }
                                ]
                            }, 
                            {
                                'tipo_percepcion': '046',
                                'clave': '~fL',
                                'concepto': '8Fe}~9}y}]',
                                'importe_gravado': '3250080.23',
                                'importe_exento': '7428920.23',
                                'horas_extra': [
                                    {
                                        'dias': '6641', 
                                        'tipo_horas': '03', 
                                        'horas_extra': '5424',
                                        'importe_pagado': '828280.23'
                                    }, 
                                    {
                                        'dias': '2317', 
                                        'tipo_horas': '03', 
                                        'horas_extra': '5749', 
                                        'importe_pagado': '64260.23'
                                    }
                                ]
                            }
                        ],
                        'jubilacion_pension_retiro': {
                            'total_una_exhibicion': '', 
                            'total_parcialidad': '', 
                            'monto_diario': '3890550.23', 
                            'ingreso_acumulable': '9102650.23', 
                            'ingreso_no_acumulable': '857060.23'
                        }, 
                        'separacion_indemnizacion': {
                            'total_pagado': '6595300.23', 
                            'num_años_servicio': '90', 
                            'ultimo_sueldo_mens_ord': '6493240.23', 
                            'ingreso_acumulable': '5732610.23', 
                            'ingreso_no_acumulable': '2531860.23'
                        }
                    },
                    'deducciones': {
                        'total_otras_deducciones': '3965300.23', 
                        'total_impuestos_retenidos': '4272620.23', 
                        'deduccion': [
                            {
                                'tipo_deduccion': '057', 
                                'clave': '1(lL`}~R', 
                                'concepto': '}}}}vlf', 
                                'importe': '8329690.23'
                            }, 
                            {
                                'tipo_deduccion': '100', 
                                'clave': '~qc}', 
                                'concepto': '}X~', 
                                'importe': '524170.23'
                            }, 
                            {
                                'tipo_deduccion': '104', 
                                'clave': '4}L},~L', 
                                'concepto': '~~}f', 
                                'importe': '40660.23'
                            }, 
                            {
                                
                                'tipo_deduccion': '009', 
                                'clave': 'W}}}}', 
                                'concepto': 'D^', 
                                'importe': '9265310.23'
                            }, 
                            {
                                'tipo_deduccion': '099', 
                                'clave': 'y}}', 
                                'concepto': '~J}', 
                                'importe': '4072880.23'
                            }
                        ]
                    },
                    'otros_pagos': {
                        'otro_pago': [
                            {
                                'tipo_otro_pago': '007', 
                                'clave': '}O~VM~', 
                                'concepto': '}}', 
                                'importe': '9359660.23'
                            }, 
                            {
                                'tipo_otro_pago': '003', 
                                'clave': 'j{}$', 
                                'concepto': '^}}~', 
                                'importe': '1808190.23', 
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '8913760.23'
                                }
                            }, 
                            {
                                'tipo_otro_pago': '003', 
                                'clave': '}~}I', 
                                'concepto': 'pM}', 
                                'importe': '7909810.23', 
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '8574770.23'
                                }
                            }, 
                            {
                                'tipo_otro_pago': '005', 
                                'clave': '}}~Ij~', 
                                'concepto': '}(', 
                                'importe': '2642840.23', 
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '3608130.23'
                                }
                            }, 
                            {
                                'tipo_otro_pago': '005', 
                                'clave': '~}~}~~~L}i}', 
                                'concepto': '}~', 
                                'importe': '4736020.23', 
                                'compensacion_saldos_a_favor': {
                                    'saldo_a_favor': '6382120.23', 
                                    'año': '9858', 
                                    'remanente_sal_fav': 
                                    '888430.23'
                                }
                            }
                        ]
                    }, 
                    'incapacidades': {
                        'incapacidad': [
                            {
                                'dias_incapacidad': '7842', 
                                'tipo_incapacidad': '04', 
                                'importe_monetario': '664540.23'
                            }, 
                            {
                                'dias_incapacidad': '4894', 
                                'tipo_incapacidad': '01', 
                                'importe_monetario': '6949690.23'
                            }, 
                            {
                                'dias_incapacidad': '9391', 
                                'tipo_incapacidad': '04', 
                                'importe_monetario': ''
                            }, 
                            {
                                'dias_incapacidad': '6033', 
                                'tipo_incapacidad': '03', 
                                'importe_monetario': '1414180.23'
                            }, 
                            {
                                'dias_incapacidad': '8309', 
                                'tipo_incapacidad': '04', 
                                'importe_monetario': '7558760.23'
                            }
                        ]
                    }
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)

    def test_transform_file_complete_nom_safe_numerics(self):
        sax_handler = CFDI33SAXHandler(safe_numerics=True).use_nomina12()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/nomina12/nom_complete.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': '"',
                'folio': '/>KA',
                'fecha': '2018-01-10T07:22:51',
                'no_certificado': '47217725691977968749',
                'subtotal': '5858580.234906',
                'descuento': '9061950.234906',
                'total': '7679420.234906',
                'moneda': 'SGD',
                'tipo_cambio': '8016540.234907',
                'tipo_comprobante': 'N',
                'metodo_pago': 'PPD',
                'forma_pago': '01',
                'condiciones_pago': '}_',
                'lugar_expedicion': '45734',
                'sello':'string',
                'certificado':'string',
                'confirmacion':'8p7F3',
                'emisor': {
                    'rfc': 'J&O750807563',
                    'nombre': 'Q~',
                    'regimen_fiscal': '611'
                },
                'receptor': {
                    'rfc': 'ÑÑD68010919A',
                    'nombre': '^*p_',
                    'residencia_fiscal': 'PRI',
                    'num_reg_id_trib': 'string',
                    'uso_cfdi': 'D01'
                },
                'conceptos': [],
                'impuestos': {
                    'retenciones': [
                        {
                            'impuesto': '001', 
                            'importe': '1900460.234906'
                        }, 
                        {
                            'impuesto': '002', 
                            'importe': '8425580.234906'
                        }, 
                        {
                            'impuesto': '003', 
                            'importe': '6550940.234906'
                        }
                    ],
                    'traslados': [
                        {
                            'impuesto': '001', 
                            'tipo_factor': 'Cuota', 
                            'tasa_o_cuota': '5992320.234906', 
                            'importe': '3311220.234906'
                        }
                    ], 
                    'total_impuestos_traslados': '5553360.234906',
                    'total_impuestos_retenidos': '8065990.234906'
                },
                'complementos': 'Nomina',
                'addendas': ''
            },
            'tfd11': [],
            'nomina12': [
                {
                    'version': '1.2',
                    'tipo_nomina': 'O',
                    'fecha_pago': '1972-01-05',
                    'fecha_inicial_pago': '1994-08-28',
                    'fecha_final_pago': '1995-04-17',
                    'num_dias_pagados': '2997.357',
                    'total_percepciones': '6450960.23',
                    'total_deducciones': '4226100.23',
                    'total_otros_pagos': '7815140.23',
                    'emisor': {
                        'curp': 'JAQE081121MOCZGNW2',
                        'registro_patronal': '"}~',
                        'rfc_patron_origen': 'KOÑ7908288LA',
                        'entidad_SNCF': {
                            'origen_recurso': 'IP',
                            'monto_recurso_propio': '9301520.23'
                        }
                    },
                    'receptor': {
                        'curp': 'VXNL701131HQTRYB07',
                        'num_seguridad_social': '59904',
                        'fecha_inicio_rel_laboral': '2010-09-02',
                        'antigüedad': 'P2Y2D',
                        'tipo_contrato': '09',
                        'sindicalizado': 'Sí',
                        'tipo_jornada': '05',
                        'tipo_regimen': '09',
                        'num_empleado': '~~',
                        'departamento': 'W',
                        'puesto': '}}8',
                        'riesgo_puesto': '3',
                        'periodicidad_pago': '06',
                        'banco': '647',
                        'cuenta_bancaria': '1234567890',
                        'salario_base_cot_apor': '8635520.23',
                        'salario_diario_integrado': '2928750.23',
                        'clave_ent_fed': 'VT',
                        'subcontratacion': [
                            {
                                'rfc_labora': '&ÑEL561104H5A',
                                'porcentaje_tiempo': '91.44'
                            }, 
                            {
                                'rfc_labora': 'ÑÑL&020703408',
                                'porcentaje_tiempo': '50.81'
                            }
                        ]
                    },
                    'percepciones': {
                        'total_sueldos': '4960830.23',
                        'total_separacion_indemnizacion': '3741880.23',
                        'total_jubilacion_pension_retiro': '7499380.23',
                        'total_gravado': '2472530.23',
                        'total_exento': '8274700.23',
                        'percepcion': [
                            {
                                'tipo_percepcion': '019',
                                'clave': '9~}m', 
                                'concepto': '~K', 
                                'importe_gravado': '9232380.23', 
                                'importe_exento': '6681000.23', 
                                'horas_extra': []
                            }, 
                            {
                                'tipo_percepcion': '031', 
                                'clave': '~^["4}~a', 
                                'concepto': '}U~', 
                                'importe_gravado': '6444510.23', 
                                'importe_exento': '190260.23', 
                                'horas_extra': [
                                    {
                                        'dias': '4890', 
                                        'tipo_horas': '03', 
                                        'horas_extra': '7170', 
                                        'importe_pagado': '4190840.23'
                                    }
                                ], 
                                'acciones_o_titulos': {
                                    'valor_mercado': '5791520.234907', 
                                    'precio_al_otorgarse': '2416940.234907'
                                }
                            }, 
                            {
                                'tipo_percepcion': '013', 
                                'clave': '~eeE}}', 
                                'concepto': '~', 
                                'importe_gravado': '3007460.23', 
                                'importe_exento': '352260.23', 
                                'horas_extra': [
                                    {
                                        'dias': '4444', 
                                        'tipo_horas': '01', 
                                        'horas_extra': '7306', 
                                        'importe_pagado': '4568110.23'
                                    }, 
                                    {
                                        'dias': '559', 
                                        'tipo_horas': '01', 
                                        'horas_extra': '1594', 
                                        'importe_pagado': '1797550.23'
                                    }
                                ]
                            }, 
                            {
                                'tipo_percepcion': '046',
                                'clave': '~fL',
                                'concepto': '8Fe}~9}y}]',
                                'importe_gravado': '3250080.23',
                                'importe_exento': '7428920.23',
                                'horas_extra': [
                                    {
                                        'dias': '6641', 
                                        'tipo_horas': '03', 
                                        'horas_extra': '5424',
                                        'importe_pagado': '828280.23'
                                    }, 
                                    {
                                        'dias': '2317', 
                                        'tipo_horas': '03', 
                                        'horas_extra': '5749', 
                                        'importe_pagado': '64260.23'
                                    }
                                ]
                            }
                        ],
                        'jubilacion_pension_retiro': {
                            'total_una_exhibicion': '0.00', 
                            'total_parcialidad': '0.00', 
                            'monto_diario': '3890550.23', 
                            'ingreso_acumulable': '9102650.23', 
                            'ingreso_no_acumulable': '857060.23'
                        }, 
                        'separacion_indemnizacion': {
                            'total_pagado': '6595300.23', 
                            'num_años_servicio': '90', 
                            'ultimo_sueldo_mens_ord': '6493240.23', 
                            'ingreso_acumulable': '5732610.23', 
                            'ingreso_no_acumulable': '2531860.23'
                        }
                    },
                    'deducciones': {
                        'total_otras_deducciones': '3965300.23', 
                        'total_impuestos_retenidos': '4272620.23', 
                        'deduccion': [
                            {
                                'tipo_deduccion': '057', 
                                'clave': '1(lL`}~R', 
                                'concepto': '}}}}vlf', 
                                'importe': '8329690.23'
                            }, 
                            {
                                'tipo_deduccion': '100', 
                                'clave': '~qc}', 
                                'concepto': '}X~', 
                                'importe': '524170.23'
                            }, 
                            {
                                'tipo_deduccion': '104', 
                                'clave': '4}L},~L', 
                                'concepto': '~~}f', 
                                'importe': '40660.23'
                            }, 
                            {
                                
                                'tipo_deduccion': '009', 
                                'clave': 'W}}}}', 
                                'concepto': 'D^', 
                                'importe': '9265310.23'
                            }, 
                            {
                                'tipo_deduccion': '099', 
                                'clave': 'y}}', 
                                'concepto': '~J}', 
                                'importe': '4072880.23'
                            }
                        ]
                    },
                    'otros_pagos': {
                        'otro_pago': [
                            {
                                'tipo_otro_pago': '007', 
                                'clave': '}O~VM~', 
                                'concepto': '}}', 
                                'importe': '9359660.23'
                            }, 
                            {
                                'tipo_otro_pago': '003', 
                                'clave': 'j{}$', 
                                'concepto': '^}}~', 
                                'importe': '1808190.23', 
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '8913760.23'
                                }
                            }, 
                            {
                                'tipo_otro_pago': '003', 
                                'clave': '}~}I', 
                                'concepto': 'pM}', 
                                'importe': '7909810.23', 
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '8574770.23'
                                }
                            }, 
                            {
                                'tipo_otro_pago': '005', 
                                'clave': '}}~Ij~', 
                                'concepto': '}(', 
                                'importe': '2642840.23', 
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '3608130.23'
                                }
                            }, 
                            {
                                'tipo_otro_pago': '005', 
                                'clave': '~}~}~~~L}i}', 
                                'concepto': '}~', 
                                'importe': '4736020.23', 
                                'compensacion_saldos_a_favor': {
                                    'saldo_a_favor': '6382120.23', 
                                    'año': '9858', 
                                    'remanente_sal_fav': 
                                    '888430.23'
                                }
                            }
                        ]
                    }, 
                    'incapacidades': {
                        'incapacidad': [
                            {
                                'dias_incapacidad': '7842', 
                                'tipo_incapacidad': '04', 
                                'importe_monetario': '664540.23'
                            }, 
                            {
                                'dias_incapacidad': '4894', 
                                'tipo_incapacidad': '01', 
                                'importe_monetario': '6949690.23'
                            }, 
                            {
                                'dias_incapacidad': '9391', 
                                'tipo_incapacidad': '04', 
                                'importe_monetario': '0.00'
                            }, 
                            {
                                'dias_incapacidad': '6033', 
                                'tipo_incapacidad': '03', 
                                'importe_monetario': '1414180.23'
                            }, 
                            {
                                'dias_incapacidad': '8309', 
                                'tipo_incapacidad': '04', 
                                'importe_monetario': '7558760.23'
                            }
                        ]
                    }
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_complete_nom_safe_numerics_empty_char(self):
        sax_handler = CFDI33SAXHandler(safe_numerics=True, empty_char='-').use_nomina12()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/nomina12/nom_complete.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': '"',
                'folio': '/>KA',
                'fecha': '2018-01-10T07:22:51',
                'no_certificado': '47217725691977968749',
                'subtotal': '5858580.234906',
                'descuento': '9061950.234906',
                'total': '7679420.234906',
                'moneda': 'SGD',
                'tipo_cambio': '8016540.234907',
                'tipo_comprobante': 'N',
                'metodo_pago': 'PPD',
                'forma_pago': '01',
                'condiciones_pago': '}_',
                'lugar_expedicion': '45734',
                'sello':'string',
                'certificado':'string',
                'confirmacion':'8p7F3',
                'emisor': {
                    'rfc': 'J&O750807563',
                    'nombre': 'Q~',
                    'regimen_fiscal': '611'
                },
                'receptor': {
                    'rfc': 'ÑÑD68010919A',
                    'nombre': '^*p_',
                    'residencia_fiscal': 'PRI',
                    'num_reg_id_trib': 'string',
                    'uso_cfdi': 'D01'
                },
                'conceptos': [],
                'impuestos': {
                    'retenciones': [
                        {
                            'impuesto': '001', 
                            'importe': '1900460.234906'
                        }, 
                        {
                            'impuesto': '002', 
                            'importe': '8425580.234906'
                        }, 
                        {
                            'impuesto': '003', 
                            'importe': '6550940.234906'
                        }
                    ],
                    'traslados': [
                        {
                            'impuesto': '001', 
                            'tipo_factor': 'Cuota', 
                            'tasa_o_cuota': '5992320.234906', 
                            'importe': '3311220.234906'
                        }
                    ], 
                    'total_impuestos_traslados': '5553360.234906',
                    'total_impuestos_retenidos': '8065990.234906'
                },
                'complementos': 'Nomina',
                'addendas': '-'
            },
            'tfd11': [],
            'nomina12': [
                {
                    'version': '1.2',
                    'tipo_nomina': 'O',
                    'fecha_pago': '1972-01-05',
                    'fecha_inicial_pago': '1994-08-28',
                    'fecha_final_pago': '1995-04-17',
                    'num_dias_pagados': '2997.357',
                    'total_percepciones': '6450960.23',
                    'total_deducciones': '4226100.23',
                    'total_otros_pagos': '7815140.23',
                    'emisor': {
                        'curp': 'JAQE081121MOCZGNW2',
                        'registro_patronal': '"}~',
                        'rfc_patron_origen': 'KOÑ7908288LA',
                        'entidad_SNCF': {
                            'origen_recurso': 'IP',
                            'monto_recurso_propio': '9301520.23'
                        }
                    },
                    'receptor': {
                        'curp': 'VXNL701131HQTRYB07',
                        'num_seguridad_social': '59904',
                        'fecha_inicio_rel_laboral': '2010-09-02',
                        'antigüedad': 'P2Y2D',
                        'tipo_contrato': '09',
                        'sindicalizado': 'Sí',
                        'tipo_jornada': '05',
                        'tipo_regimen': '09',
                        'num_empleado': '~~',
                        'departamento': 'W',
                        'puesto': '}}8',
                        'riesgo_puesto': '3',
                        'periodicidad_pago': '06',
                        'banco': '647',
                        'cuenta_bancaria': '1234567890',
                        'salario_base_cot_apor': '8635520.23',
                        'salario_diario_integrado': '2928750.23',
                        'clave_ent_fed': 'VT',
                        'subcontratacion': [
                            {
                                'rfc_labora': '&ÑEL561104H5A',
                                'porcentaje_tiempo': '91.44'
                            }, 
                            {
                                'rfc_labora': 'ÑÑL&020703408',
                                'porcentaje_tiempo': '50.81'
                            }
                        ]
                    },
                    'percepciones': {
                        'total_sueldos': '4960830.23',
                        'total_separacion_indemnizacion': '3741880.23',
                        'total_jubilacion_pension_retiro': '7499380.23',
                        'total_gravado': '2472530.23',
                        'total_exento': '8274700.23',
                        'percepcion': [
                            {
                                'tipo_percepcion': '019',
                                'clave': '9~}m', 
                                'concepto': '~K', 
                                'importe_gravado': '9232380.23', 
                                'importe_exento': '6681000.23', 
                                'horas_extra': []
                            }, 
                            {
                                'tipo_percepcion': '031', 
                                'clave': '~^["4}~a', 
                                'concepto': '}U~', 
                                'importe_gravado': '6444510.23', 
                                'importe_exento': '190260.23', 
                                'horas_extra': [
                                    {
                                        'dias': '4890', 
                                        'tipo_horas': '03', 
                                        'horas_extra': '7170', 
                                        'importe_pagado': '4190840.23'
                                    }
                                ], 
                                'acciones_o_titulos': {
                                    'valor_mercado': '5791520.234907', 
                                    'precio_al_otorgarse': '2416940.234907'
                                }
                            }, 
                            {
                                'tipo_percepcion': '013', 
                                'clave': '~eeE}}', 
                                'concepto': '~', 
                                'importe_gravado': '3007460.23', 
                                'importe_exento': '352260.23', 
                                'horas_extra': [
                                    {
                                        'dias': '4444', 
                                        'tipo_horas': '01', 
                                        'horas_extra': '7306', 
                                        'importe_pagado': '4568110.23'
                                    }, 
                                    {
                                        'dias': '559', 
                                        'tipo_horas': '01', 
                                        'horas_extra': '1594', 
                                        'importe_pagado': '1797550.23'
                                    }
                                ]
                            }, 
                            {
                                'tipo_percepcion': '046',
                                'clave': '~fL',
                                'concepto': '8Fe}~9}y}]',
                                'importe_gravado': '3250080.23',
                                'importe_exento': '7428920.23',
                                'horas_extra': [
                                    {
                                        'dias': '6641', 
                                        'tipo_horas': '03', 
                                        'horas_extra': '5424',
                                        'importe_pagado': '828280.23'
                                    }, 
                                    {
                                        'dias': '2317', 
                                        'tipo_horas': '03', 
                                        'horas_extra': '5749', 
                                        'importe_pagado': '64260.23'
                                    }
                                ]
                            }
                        ],
                        'jubilacion_pension_retiro': {
                            'total_una_exhibicion': '0.00', 
                            'total_parcialidad': '0.00', 
                            'monto_diario': '3890550.23', 
                            'ingreso_acumulable': '9102650.23', 
                            'ingreso_no_acumulable': '857060.23'
                        }, 
                        'separacion_indemnizacion': {
                            'total_pagado': '6595300.23', 
                            'num_años_servicio': '90', 
                            'ultimo_sueldo_mens_ord': '6493240.23', 
                            'ingreso_acumulable': '5732610.23', 
                            'ingreso_no_acumulable': '2531860.23'
                        }
                    },
                    'deducciones': {
                        'total_otras_deducciones': '3965300.23', 
                        'total_impuestos_retenidos': '4272620.23', 
                        'deduccion': [
                            {
                                'tipo_deduccion': '057', 
                                'clave': '1(lL`}~R', 
                                'concepto': '}}}}vlf', 
                                'importe': '8329690.23'
                            }, 
                            {
                                'tipo_deduccion': '100', 
                                'clave': '~qc}', 
                                'concepto': '}X~', 
                                'importe': '524170.23'
                            }, 
                            {
                                'tipo_deduccion': '104', 
                                'clave': '4}L},~L', 
                                'concepto': '~~}f', 
                                'importe': '40660.23'
                            }, 
                            {
                                
                                'tipo_deduccion': '009', 
                                'clave': 'W}}}}', 
                                'concepto': 'D^', 
                                'importe': '9265310.23'
                            }, 
                            {
                                'tipo_deduccion': '099', 
                                'clave': 'y}}', 
                                'concepto': '~J}', 
                                'importe': '4072880.23'
                            }
                        ]
                    },
                    'otros_pagos': {
                        'otro_pago': [
                            {
                                'tipo_otro_pago': '007', 
                                'clave': '}O~VM~', 
                                'concepto': '}}', 
                                'importe': '9359660.23'
                            }, 
                            {
                                'tipo_otro_pago': '003', 
                                'clave': 'j{}$', 
                                'concepto': '^}}~', 
                                'importe': '1808190.23', 
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '8913760.23'
                                }
                            }, 
                            {
                                'tipo_otro_pago': '003', 
                                'clave': '}~}I', 
                                'concepto': 'pM}', 
                                'importe': '7909810.23', 
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '8574770.23'
                                }
                            }, 
                            {
                                'tipo_otro_pago': '005', 
                                'clave': '}}~Ij~', 
                                'concepto': '}(', 
                                'importe': '2642840.23', 
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '3608130.23'
                                }
                            }, 
                            {
                                'tipo_otro_pago': '005', 
                                'clave': '~}~}~~~L}i}', 
                                'concepto': '}~', 
                                'importe': '4736020.23', 
                                'compensacion_saldos_a_favor': {
                                    'saldo_a_favor': '6382120.23', 
                                    'año': '9858', 
                                    'remanente_sal_fav': 
                                    '888430.23'
                                }
                            }
                        ]
                    }, 
                    'incapacidades': {
                        'incapacidad': [
                            {
                                'dias_incapacidad': '7842', 
                                'tipo_incapacidad': '04', 
                                'importe_monetario': '664540.23'
                            }, 
                            {
                                'dias_incapacidad': '4894', 
                                'tipo_incapacidad': '01', 
                                'importe_monetario': '6949690.23'
                            }, 
                            {
                                'dias_incapacidad': '9391', 
                                'tipo_incapacidad': '04', 
                                'importe_monetario': '0.00'
                            }, 
                            {
                                'dias_incapacidad': '6033', 
                                'tipo_incapacidad': '03', 
                                'importe_monetario': '1414180.23'
                            }, 
                            {
                                'dias_incapacidad': '8309', 
                                'tipo_incapacidad': '04', 
                                'importe_monetario': '7558760.23'
                            }
                        ]
                    }
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_double_nom(self):
        sax_handler = CFDI33SAXHandler().use_nomina12()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/nomina12/double_nomina01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': '',
                'folio': '',
                'fecha': '2021-06-04T11:00:00',
                'no_certificado': '00000000000000000000',
                'subtotal': '73942.79',
                'descuento': '5369.93',
                'total': '68572.86',
                'moneda': 'MXN',
                'tipo_cambio': '',
                'tipo_comprobante': 'N',
                'metodo_pago': 'PUE',
                'forma_pago': '99',
                'condiciones_pago': '',
                'lugar_expedicion': '77560',
                'sello':'sign',
                'certificado':'cert',
                'confirmacion':'',
                'emisor': {
                    'rfc': 'EKU9003173C9',
                    'nombre': 'NOMBRE EMISOR',
                    'regimen_fiscal': '601'
                },
                'receptor': {
                    'rfc': 'KICR630120NX3',
                    'nombre': 'NOMBRE RECEPTOR',
                    'residencia_fiscal': '',
                    'num_reg_id_trib': '',
                    'uso_cfdi': 'P01'
                },
                'conceptos': [],
                'impuestos': {
                    'retenciones': [],
                    'traslados': [],
                    'total_impuestos_traslados' :'',
                    'total_impuestos_retenidos' :''
                },
                'complementos': 'Nomina TimbreFiscalDigital',
                'addendas': ''
            },
            'tfd11': [
                {
                    'version': '1.1',
                    'no_certificado_sat': '00000000000000000000',
                    'uuid': 'EB9F91C0-2FF0-41D9-B607-4655E3686E41',
                    'fecha_timbrado': '2021-06-04T11:00:00',
                    'rfc_prov_cert': 'IXS7607092R5',
                    'sello_cfd': 'sign',
                    'sello_sat': 'sign'
                }
            ],
            'nomina12': [
                {
                    'version': '1.2',
                    'tipo_nomina': 'E',
                    'fecha_pago': '2021-07-31',
                    'fecha_inicial_pago': '2021-07-31',
                    'fecha_final_pago': '2021-07-31',
                    'num_dias_pagados': '1.000',
                    'total_percepciones': '9786.15',
                    'total_deducciones': '5369.93',
                    'total_otros_pagos': '0.00',
                    'emisor': {
                        'curp': '',
                        'registro_patronal': '00000000000',
                        'rfc_patron_origen': '',
                        'entidad_SNCF': {
                            'origen_recurso': '',
                            'monto_recurso_propio': ''
                        }
                    },
                    'receptor': {
                        'curp': 'XEXX010101HNEXXXA4',
                        'num_seguridad_social': '00000000000',
                        'fecha_inicio_rel_laboral': '2018-11-26',
                        'antigüedad': 'P139W',
                        'tipo_contrato': '02',
                        'sindicalizado': '',
                        'tipo_jornada': '01',
                        'tipo_regimen': '02',
                        'num_empleado': '2855',
                        'departamento': '15-055-001-002 SEGURIDAD Y SALUD EN EL TRABAJO',
                        'puesto': '',
                        'riesgo_puesto': '1',
                        'periodicidad_pago': '99',
                        'banco': '',
                        'cuenta_bancaria': '',
                        'salario_base_cot_apor': '509.67',
                        'salario_diario_integrado': '534.80',
                        'clave_ent_fed': 'ROO',
                        'subcontratacion': []
                    },
                    'percepciones': {
                        'total_sueldos': '9786.15',
                        'total_separacion_indemnizacion': '',
                        'total_jubilacion_pension_retiro': '',
                        'total_gravado': '6231.81',
                        'total_exento': '3554.34',
                        'percepcion': [
                            {
                                'tipo_percepcion': '001',
                                'clave': '408',
                                'concepto': 'PROPORCION DE VACACIONES',
                                'importe_gravado': '3460.66',
                                'importe_exento': '0.00',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '001',
                                'clave': '409',
                                'concepto': 'VACACIONES PENDIENTES',
                                'importe_gravado': '1019.34',
                                'importe_exento': '0.00',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '002',
                                'clave': '426',
                                'concepto': 'AGUINALDO',
                                'importe_gravado': '1751.81',
                                'importe_exento': '2688.60',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '021',
                                'clave': '427',
                                'concepto': 'PRIMA VACACIONAL',
                                'importe_gravado': '0.00',
                                'importe_exento': '865.74',
                                'horas_extra': []
                            }
                        ]
                    },
                    'deducciones': {
                        'total_otras_deducciones': '',
                        'total_impuestos_retenidos': '5369.93',
                        'deduccion': [
                            {
                                'tipo_deduccion': '002',
                                'clave': '601',
                                'concepto': 'ISR',
                                'importe': '600.99'
                            },
                            {
                                'tipo_deduccion': '002',
                                'clave': '604',
                                'concepto': 'ISR LIQUIDACION',
                                'importe': '4768.94'
                            }
                        ]
                    },
                    'otros_pagos': {
                        'otro_pago': [
                            {
                                'tipo_otro_pago': '002',
                                'clave': '105',
                                'concepto': 'SUBSIDIO AL EMPLEO PAGADO ESP',
                                'importe': '0.00',
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '0.00'
                                }
                            }
                        ]
                    },
                    'incapacidades': {
                        'incapcidad': []
                    }
                },
                {
                    'version': '1.2',
                    'tipo_nomina': 'E',
                    'fecha_pago': '2021-07-31',
                    'fecha_inicial_pago': '2021-07-31',
                    'fecha_final_pago': '2021-07-31',
                    'num_dias_pagados': '1.000',
                    'total_percepciones': '64156.64',
                    'total_deducciones': '',
                    'total_otros_pagos': '',
                    'emisor': {
                        'curp': '',
                        'registro_patronal': '',
                        'rfc_patron_origen': '',
                        'entidad_SNCF': {
                            'origen_recurso': '',
                            'monto_recurso_propio': ''
                        }
                    },
                    'receptor': {
                        'curp': 'XEXX010101HNEXXXA4',
                        'num_seguridad_social': '',
                        'fecha_inicio_rel_laboral': '',
                        'antigüedad': '',
                        'tipo_contrato': '99',
                        'sindicalizado': '',
                        'tipo_jornada': '',
                        'tipo_regimen': '13',
                        'num_empleado': '2855',
                        'departamento': '15-055-001-002 SEGURIDAD Y SALUD EN EL TRABAJO',
                        'puesto': '',
                        'riesgo_puesto': '',
                        'periodicidad_pago': '99',
                        'banco': '',
                        'cuenta_bancaria': '',
                        'salario_base_cot_apor': '',
                        'salario_diario_integrado': '',
                        'clave_ent_fed': 'ROO',
                        'subcontratacion': []
                    },
                    'percepciones': {
                        'total_sueldos': '',
                        'total_separacion_indemnizacion': '64156.64',
                        'total_jubilacion_pension_retiro': '',
                        'total_gravado': '39959.24',
                        'total_exento': '24197.40',
                        'percepcion': [
                            {
                                'tipo_percepcion': '025',
                                'clave': '130',
                                'concepto': 'GRAVADO INDEMNIZACION',
                                'importe_gravado': '39959.24',
                                'importe_exento': '24197.40',
                                'horas_extra': []
                            }
                        ],
                        'separacion_indemnizacion': {
                            'total_pagado': '64156.64',
                            'num_años_servicio': '3',
                            'ultimo_sueldo_mens_ord': '15290.10',
                            'ingreso_acumulable': '15290.10',
                            'ingreso_no_acumulable': '24669.14'
                        }
                    },
                    'deducciones': {
                        'total_otras_deducciones': '',
                        'total_impuestos_retenidos': '',
                        'deduccion': []
                    },
                    'otros_pagos': {
                        'otro_pago': []
                    },
                    'incapacidades': {
                        'incapcidad': []
                    }
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_double_nom_break_lines(self):
        sax_handler = CFDI33SAXHandler().use_nomina12()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/nomina12/double_breaks_nomina01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': '',
                'folio': '',
                'fecha': '2021-06-04T11:00:00',
                'no_certificado': '00000000000000000000',
                'subtotal': '780109.05',
                'descuento': '227493.44',
                'total': '552615.61',
                'moneda': 'MXN',
                'tipo_cambio': '',
                'tipo_comprobante': 'N',
                'metodo_pago': 'PUE',
                'forma_pago': '99',
                'condiciones_pago': '',
                'lugar_expedicion': '77560',
                'sello':'sign',
                'certificado':'cert',
                'confirmacion':'',
                'emisor': {
                    'rfc': 'EKU9003173C9',
                    'nombre': 'NOMBRE EMISOR',
                    'regimen_fiscal': '601'
                },
                'receptor': {
                    'rfc': 'KICR630120NX3',
                    'nombre': 'NOMBRE RECEPTOR with \\r\\n spaces and breaks',
                    'residencia_fiscal': '',
                    'num_reg_id_trib': '',
                    'uso_cfdi': 'P01'
                },
                'conceptos': [],
                'impuestos': {
                    'retenciones': [],
                    'traslados': [],
                    'total_impuestos_traslados' :'',
                    'total_impuestos_retenidos' :''
                },
                'complementos': 'Nomina TimbreFiscalDigital',
                'addendas': ''
            },
            'tfd11': [
                {
                    'version': '1.1',
                    'no_certificado_sat': '00000000000000000000',
                    'uuid': 'EB9F91C0-2FF0-41D9-B607-4655E3686E41',
                    'fecha_timbrado': '2021-06-04T11:00:00',
                    'rfc_prov_cert': 'IXS7607092R5',
                    'sello_cfd': 'sign',
                    'sello_sat': 'sign'
                }
            ],
            'nomina12': [
                {
                    'version': '1.2',
                    'tipo_nomina': 'E',
                    'fecha_pago': '2021-07-23',
                    'fecha_inicial_pago': '2021-07-23',
                    'fecha_final_pago': '2021-07-23',
                    'num_dias_pagados': '8.000',
                    'total_percepciones': '229962.91',
                    'total_deducciones': '227493.44',
                    'total_otros_pagos': '0.00',
                    'emisor': {
                        'curp': '',
                        'registro_patronal': '00000000000',
                        'rfc_patron_origen': '',
                        'entidad_SNCF': {
                            'origen_recurso': '',
                            'monto_recurso_propio': ''
                        }
                    },
                    'receptor': {
                        'curp': 'XEXX010101HNEXXXA4',
                        'num_seguridad_social': '00000000000',
                        'fecha_inicio_rel_laboral': '2020-03-16',
                        'antigüedad': 'P70W',
                        'tipo_contrato': '02',
                        'sindicalizado': '',
                        'tipo_jornada': '01',
                        'tipo_regimen': '02',
                        'num_empleado': '3123',
                        'departamento': '15-058-000-000 DIR DE SISTEMAS DE INFORMACION',
                        'puesto': '',
                        'riesgo_puesto': '1',
                        'periodicidad_pago': '99',
                        'banco': '',
                        'cuenta_bancaria': '',
                        'salario_base_cot_apor': '2240.50',
                        'salario_diario_integrado': '6435.14',
                        'clave_ent_fed': 'ROO',
                        'subcontratacion': []
                    },
                    'percepciones': {
                        'total_sueldos': '229962.91',
                        'total_separacion_indemnizacion': '',
                        'total_jubilacion_pension_retiro': '',
                        'total_gravado': '225930.01',
                        'total_exento': '4032.90',
                        'percepcion': [
                            {
                                'tipo_percepcion': '001',
                                'clave': '201',
                                'concepto': 'SUELDO TIMBRADO',
                                'importe_gravado': '40409.92',
                                'importe_exento': '0.00',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '001',
                                'clave': '408',
                                'concepto': 'PROPORCION DE VACACIONES',
                                'importe_gravado': '32134.19',
                                'importe_exento': '0.00',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '001',
                                'clave': '409',
                                'concepto': 'VACACIONES PENDIENTES',
                                'importe_gravado': '90922.35',
                                'importe_exento': '0.00',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '049',
                                'clave': '418',
                                'concepto': 'PREMIO DE ASISTENCIA',
                                'importe_gravado': '4040.99',
                                'importe_exento': '0.00',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '010',
                                'clave': '419',
                                'concepto': 'PREMIO POR PUNTUALIDAD',
                                'importe_gravado': '4040.99',
                                'importe_exento': '0.00',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '002',
                                'clave': '426',
                                'concepto': 'AGUINALDO',
                                'importe_gravado': '39658.78',
                                'importe_exento': '2688.60',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '021',
                                'clave': '427',
                                'concepto': 'PRIMA VACACIONAL',
                                'importe_gravado': '14722.79',
                                'importe_exento': '1344.30',
                                'horas_extra': []
                            }
                        ]
                    },
                    'deducciones': {
                        'total_otras_deducciones': '488.79',
                        'total_impuestos_retenidos': '227004.65',
                        'deduccion': [
                            {
                                'tipo_deduccion': '002',
                                'clave': '601',
                                'concepto': 'ISR',
                                'importe': '68245.79'
                            },
                            {
                                'tipo_deduccion': '002',
                                'clave': '604',
                                'concepto': 'ISR LIQUIDACION',
                                'importe': '158758.86'
                            },
                            {
                                'tipo_deduccion': '001',
                                'clave': '644',
                                'concepto': 'IMSS',
                                'importe': '488.79'
                            }
                        ]
                    },
                    'otros_pagos': {
                        'otro_pago': [
                            {
                                'tipo_otro_pago': '002',
                                'clave': '105',
                                'concepto': 'SUBSIDIO AL EMPLEO PAGADO ESP',
                                'importe': '0.00',
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '0.00'
                                }
                            }
                        ]
                    },
                    'incapacidades': {
                        'incapcidad': []
                    }
                },
                {
                    'version': '1.2',
                    'tipo_nomina': 'E',
                    'fecha_pago': '2021-07-23',
                    'fecha_inicial_pago': '2021-07-23',
                    'fecha_final_pago': '2021-07-23',
                    'num_dias_pagados': '8.000',
                    'total_percepciones': '550146.14',
                    'total_deducciones': '',
                    'total_otros_pagos': '',
                    'emisor': {
                        'curp': '',
                        'registro_patronal': '',
                        'rfc_patron_origen': '',
                        'entidad_SNCF': {
                            'origen_recurso': '',
                            'monto_recurso_propio': ''
                        }
                    },
                    'receptor': {
                        'curp': 'XEXX010101HNEXXXA4',
                        'num_seguridad_social': '',
                        'fecha_inicio_rel_laboral': '',
                        'antigüedad': '',
                        'tipo_contrato': '99',
                        'sindicalizado': '',
                        'tipo_jornada': '',
                        'tipo_regimen': '13',
                        'num_empleado': '3123',
                        'departamento': '15-058-000-000 DIR DE SISTEMAS DE INFORMACION',
                        'puesto': '',
                        'riesgo_puesto': '',
                        'periodicidad_pago': '99',
                        'banco': '',
                        'cuenta_bancaria': '',
                        'salario_base_cot_apor': '',
                        'salario_diario_integrado': '',
                        'clave_ent_fed': 'ROO',
                        'subcontratacion': []
                    },
                    'percepciones': {
                        'total_sueldos': '',
                        'total_separacion_indemnizacion': '550146.14',
                        'total_jubilacion_pension_retiro': '',
                        'total_gravado': '542070.83',
                        'total_exento': '8075.31',
                        'percepcion': [
                            {
                                'tipo_percepcion': '025',
                                'clave': '130',
                                'concepto': 'GRAVADO INDEMNIZACION',
                                'importe_gravado': '542070.83',
                                'importe_exento': '8075.31',
                                'horas_extra': []
                            }
                        ],
                        'separacion_indemnizacion': {
                            'total_pagado': '550146.14',
                            'num_años_servicio': '1',
                            'ultimo_sueldo_mens_ord': '181844.70',
                            'ingreso_acumulable': '181844.70',
                            'ingreso_no_acumulable': '360226.13'
                        }
                    },
                    'deducciones': {
                        'total_otras_deducciones': '',
                        'total_impuestos_retenidos': '',
                        'deduccion': []
                    },
                    'otros_pagos': {
                        'otro_pago': []
                    },
                    'incapacidades': {
                        'incapcidad': []
                    }
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_double_nom_break_lines_xsdvalidation(self):
        schema_validator = SchemaHelper.get_schema_validator_cfdi33()
        sax_handler = CFDI33SAXHandler(schema_validator=schema_validator).use_nomina12()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/nomina12/double_breaks_nomina01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': '',
                'folio': '',
                'fecha': '2021-06-04T11:00:00',
                'no_certificado': '00000000000000000000',
                'subtotal': '780109.05',
                'descuento': '227493.44',
                'total': '552615.61',
                'moneda': 'MXN',
                'tipo_cambio': '',
                'tipo_comprobante': 'N',
                'metodo_pago': 'PUE',
                'forma_pago': '99',
                'condiciones_pago': '',
                'lugar_expedicion': '77560',
                'sello':'sign',
                'certificado':'cert',
                'confirmacion':'',
                'emisor': {
                    'rfc': 'EKU9003173C9',
                    'nombre': 'NOMBRE EMISOR',
                    'regimen_fiscal': '601'
                },
                'receptor': {
                    'rfc': 'KICR630120NX3',
                    'nombre': 'NOMBRE RECEPTOR with \\r\\n spaces and breaks',
                    'residencia_fiscal': '',
                    'num_reg_id_trib': '',
                    'uso_cfdi': 'P01'
                },
                'conceptos': [],
                'impuestos': {
                    'retenciones': [],
                    'traslados': [],
                    'total_impuestos_traslados' :'',
                    'total_impuestos_retenidos' :''
                },
                'complementos': 'Nomina TimbreFiscalDigital',
                'addendas': ''
            },
            'tfd11': [
                {
                    'version': '1.1',
                    'no_certificado_sat': '00000000000000000000',
                    'uuid': 'EB9F91C0-2FF0-41D9-B607-4655E3686E41',
                    'fecha_timbrado': '2021-06-04T11:00:00',
                    'rfc_prov_cert': 'IXS7607092R5',
                    'sello_cfd': 'sign',
                    'sello_sat': 'sign'
                }
            ],
            'nomina12': [
                {
                    'version': '1.2',
                    'tipo_nomina': 'E',
                    'fecha_pago': '2021-07-23',
                    'fecha_inicial_pago': '2021-07-23',
                    'fecha_final_pago': '2021-07-23',
                    'num_dias_pagados': '8.000',
                    'total_percepciones': '229962.91',
                    'total_deducciones': '227493.44',
                    'total_otros_pagos': '0.00',
                    'emisor': {
                        'curp': '',
                        'registro_patronal': '00000000000',
                        'rfc_patron_origen': '',
                        'entidad_SNCF': {
                            'origen_recurso': '',
                            'monto_recurso_propio': ''
                        }
                    },
                    'receptor': {
                        'curp': 'XEXX010101HNEXXXA4',
                        'num_seguridad_social': '00000000000',
                        'fecha_inicio_rel_laboral': '2020-03-16',
                        'antigüedad': 'P70W',
                        'tipo_contrato': '02',
                        'sindicalizado': '',
                        'tipo_jornada': '01',
                        'tipo_regimen': '02',
                        'num_empleado': '3123',
                        'departamento': '15-058-000-000 DIR DE SISTEMAS DE INFORMACION',
                        'puesto': '',
                        'riesgo_puesto': '1',
                        'periodicidad_pago': '99',
                        'banco': '',
                        'cuenta_bancaria': '',
                        'salario_base_cot_apor': '2240.50',
                        'salario_diario_integrado': '6435.14',
                        'clave_ent_fed': 'ROO',
                        'subcontratacion': []
                    },
                    'percepciones': {
                        'total_sueldos': '229962.91',
                        'total_separacion_indemnizacion': '',
                        'total_jubilacion_pension_retiro': '',
                        'total_gravado': '225930.01',
                        'total_exento': '4032.90',
                        'percepcion': [
                            {
                                'tipo_percepcion': '001',
                                'clave': '201',
                                'concepto': 'SUELDO TIMBRADO',
                                'importe_gravado': '40409.92',
                                'importe_exento': '0.00',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '001',
                                'clave': '408',
                                'concepto': 'PROPORCION DE VACACIONES',
                                'importe_gravado': '32134.19',
                                'importe_exento': '0.00',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '001',
                                'clave': '409',
                                'concepto': 'VACACIONES PENDIENTES',
                                'importe_gravado': '90922.35',
                                'importe_exento': '0.00',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '049',
                                'clave': '418',
                                'concepto': 'PREMIO DE ASISTENCIA',
                                'importe_gravado': '4040.99',
                                'importe_exento': '0.00',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '010',
                                'clave': '419',
                                'concepto': 'PREMIO POR PUNTUALIDAD',
                                'importe_gravado': '4040.99',
                                'importe_exento': '0.00',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '002',
                                'clave': '426',
                                'concepto': 'AGUINALDO',
                                'importe_gravado': '39658.78',
                                'importe_exento': '2688.60',
                                'horas_extra': []
                            },
                            {
                                'tipo_percepcion': '021',
                                'clave': '427',
                                'concepto': 'PRIMA VACACIONAL',
                                'importe_gravado': '14722.79',
                                'importe_exento': '1344.30',
                                'horas_extra': []
                            }
                        ]
                    },
                    'deducciones': {
                        'total_otras_deducciones': '488.79',
                        'total_impuestos_retenidos': '227004.65',
                        'deduccion': [
                            {
                                'tipo_deduccion': '002',
                                'clave': '601',
                                'concepto': 'ISR',
                                'importe': '68245.79'
                            },
                            {
                                'tipo_deduccion': '002',
                                'clave': '604',
                                'concepto': 'ISR LIQUIDACION',
                                'importe': '158758.86'
                            },
                            {
                                'tipo_deduccion': '001',
                                'clave': '644',
                                'concepto': 'IMSS',
                                'importe': '488.79'
                            }
                        ]
                    },
                    'otros_pagos': {
                        'otro_pago': [
                            {
                                'tipo_otro_pago': '002',
                                'clave': '105',
                                'concepto': 'SUBSIDIO AL EMPLEO PAGADO ESP',
                                'importe': '0.00',
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '0.00'
                                }
                            }
                        ]
                    },
                    'incapacidades': {
                        'incapcidad': []
                    }
                },
                {
                    'version': '1.2',
                    'tipo_nomina': 'E',
                    'fecha_pago': '2021-07-23',
                    'fecha_inicial_pago': '2021-07-23',
                    'fecha_final_pago': '2021-07-23',
                    'num_dias_pagados': '8.000',
                    'total_percepciones': '550146.14',
                    'total_deducciones': '',
                    'total_otros_pagos': '',
                    'emisor': {
                        'curp': '',
                        'registro_patronal': '',
                        'rfc_patron_origen': '',
                        'entidad_SNCF': {
                            'origen_recurso': '',
                            'monto_recurso_propio': ''
                        }
                    },
                    'receptor': {
                        'curp': 'XEXX010101HNEXXXA4',
                        'num_seguridad_social': '',
                        'fecha_inicio_rel_laboral': '',
                        'antigüedad': '',
                        'tipo_contrato': '99',
                        'sindicalizado': '',
                        'tipo_jornada': '',
                        'tipo_regimen': '13',
                        'num_empleado': '3123',
                        'departamento': '15-058-000-000 DIR DE SISTEMAS DE INFORMACION',
                        'puesto': '',
                        'riesgo_puesto': '',
                        'periodicidad_pago': '99',
                        'banco': '',
                        'cuenta_bancaria': '',
                        'salario_base_cot_apor': '',
                        'salario_diario_integrado': '',
                        'clave_ent_fed': 'ROO',
                        'subcontratacion': []
                    },
                    'percepciones': {
                        'total_sueldos': '',
                        'total_separacion_indemnizacion': '550146.14',
                        'total_jubilacion_pension_retiro': '',
                        'total_gravado': '542070.83',
                        'total_exento': '8075.31',
                        'percepcion': [
                            {
                                'tipo_percepcion': '025',
                                'clave': '130',
                                'concepto': 'GRAVADO INDEMNIZACION',
                                'importe_gravado': '542070.83',
                                'importe_exento': '8075.31',
                                'horas_extra': []
                            }
                        ],
                        'separacion_indemnizacion': {
                            'total_pagado': '550146.14',
                            'num_años_servicio': '1',
                            'ultimo_sueldo_mens_ord': '181844.70',
                            'ingreso_acumulable': '181844.70',
                            'ingreso_no_acumulable': '360226.13'
                        }
                    },
                    'deducciones': {
                        'total_otras_deducciones': '',
                        'total_impuestos_retenidos': '',
                        'deduccion': []
                    },
                    'otros_pagos': {
                        'otro_pago': []
                    },
                    'incapacidades': {
                        'incapcidad': []
                    }
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_complete_nom_validation(self):
        schema_validator = SchemaHelper.get_schema_validator_cfdi33()
        sax_handler = CFDI33SAXHandler(schema_validator=schema_validator).use_nomina12()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/nomina12/nom_complete.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': '"',
                'folio': '/>KA',
                'fecha': '2018-01-10T07:22:51',
                'no_certificado': '47217725691977968749',
                'subtotal': '5858580.234906',
                'descuento': '9061950.234906',
                'total': '7679420.234906',
                'moneda': 'SGD',
                'tipo_cambio': '8016540.234907',
                'tipo_comprobante': 'N',
                'metodo_pago': 'PPD',
                'forma_pago': '01',
                'condiciones_pago': '}_',
                'lugar_expedicion': '45734',
                'sello':'string',
                'certificado':'string',
                'confirmacion':'8p7F3',
                'emisor': {
                    'rfc': 'J&O750807563',
                    'nombre': 'Q~',
                    'regimen_fiscal': '611'
                },
                'receptor': {
                    'rfc': 'ÑÑD68010919A',
                    'nombre': '^*p_',
                    'residencia_fiscal': 'PRI',
                    'num_reg_id_trib': 'string',
                    'uso_cfdi': 'D01'
                },
                'conceptos': [],
                'impuestos': {
                    'retenciones': [
                        {
                            'impuesto': '001', 
                            'importe': '1900460.234906'
                        }, 
                        {
                            'impuesto': '002', 
                            'importe': '8425580.234906'
                        }, 
                        {
                            'impuesto': '003', 
                            'importe': '6550940.234906'
                        }
                    ],
                    'traslados': [
                        {
                            'impuesto': '001', 
                            'tipo_factor': 'Cuota', 
                            'tasa_o_cuota': '5992320.234906', 
                            'importe': '3311220.234906'
                        }
                    ], 
                    'total_impuestos_traslados': '5553360.234906',
                    'total_impuestos_retenidos': '8065990.234906'
                },
                'complementos': 'Nomina',
                'addendas': ''
            },
            'tfd11': [],
            'nomina12': [
                {
                    'version': '1.2',
                    'tipo_nomina': 'O',
                    'fecha_pago': '1972-01-05',
                    'fecha_inicial_pago': '1994-08-28',
                    'fecha_final_pago': '1995-04-17',
                    'num_dias_pagados': '2997.357',
                    'total_percepciones': '6450960.23',
                    'total_deducciones': '4226100.23',
                    'total_otros_pagos': '7815140.23',
                    'emisor': {
                        'curp': 'JAQE081121MOCZGNW2',
                        'registro_patronal': '"}~',
                        'rfc_patron_origen': 'KOÑ7908288LA',
                        'entidad_SNCF': {
                            'origen_recurso': 'IP',
                            'monto_recurso_propio': '9301520.23'
                        }
                    },
                    'receptor': {
                        'curp': 'VXNL701131HQTRYB07',
                        'num_seguridad_social': '59904',
                        'fecha_inicio_rel_laboral': '2010-09-02',
                        'antigüedad': 'P2Y2D',
                        'tipo_contrato': '09',
                        'sindicalizado': 'Sí',
                        'tipo_jornada': '05',
                        'tipo_regimen': '09',
                        'num_empleado': '~~',
                        'departamento': 'W',
                        'puesto': '}}8',
                        'riesgo_puesto': '3',
                        'periodicidad_pago': '06',
                        'banco': '647',
                        'cuenta_bancaria': '1234567890',
                        'salario_base_cot_apor': '8635520.23',
                        'salario_diario_integrado': '2928750.23',
                        'clave_ent_fed': 'VT',
                        'subcontratacion': [
                            {
                                'rfc_labora': '&ÑEL561104H5A',
                                'porcentaje_tiempo': '91.44'
                            }, 
                            {
                                'rfc_labora': 'ÑÑL&020703408',
                                'porcentaje_tiempo': '50.81'
                            }
                        ]
                    },
                    'percepciones': {
                        'total_sueldos': '4960830.23',
                        'total_separacion_indemnizacion': '3741880.23',
                        'total_jubilacion_pension_retiro': '7499380.23',
                        'total_gravado': '2472530.23',
                        'total_exento': '8274700.23',
                        'percepcion': [
                            {
                                'tipo_percepcion': '019',
                                'clave': '9~}m', 
                                'concepto': '~K', 
                                'importe_gravado': '9232380.23', 
                                'importe_exento': '6681000.23', 
                                'horas_extra': []
                            }, 
                            {
                                'tipo_percepcion': '031', 
                                'clave': '~^["4}~a', 
                                'concepto': '}U~', 
                                'importe_gravado': '6444510.23', 
                                'importe_exento': '190260.23', 
                                'horas_extra': [
                                    {
                                        'dias': '4890', 
                                        'tipo_horas': '03', 
                                        'horas_extra': '7170', 
                                        'importe_pagado': '4190840.23'
                                    }
                                ], 
                                'acciones_o_titulos': {
                                    'valor_mercado': '5791520.234907', 
                                    'precio_al_otorgarse': '2416940.234907'
                                }
                            }, 
                            {
                                'tipo_percepcion': '013', 
                                'clave': '~eeE}}', 
                                'concepto': '~', 
                                'importe_gravado': '3007460.23', 
                                'importe_exento': '352260.23', 
                                'horas_extra': [
                                    {
                                        'dias': '4444', 
                                        'tipo_horas': '01', 
                                        'horas_extra': '7306', 
                                        'importe_pagado': '4568110.23'
                                    }, 
                                    {
                                        'dias': '559', 
                                        'tipo_horas': '01', 
                                        'horas_extra': '1594', 
                                        'importe_pagado': '1797550.23'
                                    }
                                ]
                            }, 
                            {
                                'tipo_percepcion': '046',
                                'clave': '~fL',
                                'concepto': '8Fe}~9}y}]',
                                'importe_gravado': '3250080.23',
                                'importe_exento': '7428920.23',
                                'horas_extra': [
                                    {
                                        'dias': '6641', 
                                        'tipo_horas': '03', 
                                        'horas_extra': '5424',
                                        'importe_pagado': '828280.23'
                                    }, 
                                    {
                                        'dias': '2317', 
                                        'tipo_horas': '03', 
                                        'horas_extra': '5749', 
                                        'importe_pagado': '64260.23'
                                    }
                                ]
                            }
                        ],
                        'jubilacion_pension_retiro': {
                            'total_una_exhibicion': '', 
                            'total_parcialidad': '', 
                            'monto_diario': '3890550.23', 
                            'ingreso_acumulable': '9102650.23', 
                            'ingreso_no_acumulable': '857060.23'
                        }, 
                        'separacion_indemnizacion': {
                            'total_pagado': '6595300.23', 
                            'num_años_servicio': '90', 
                            'ultimo_sueldo_mens_ord': '6493240.23', 
                            'ingreso_acumulable': '5732610.23', 
                            'ingreso_no_acumulable': '2531860.23'
                        }
                    },
                    'deducciones': {
                        'total_otras_deducciones': '3965300.23', 
                        'total_impuestos_retenidos': '4272620.23', 
                        'deduccion': [
                            {
                                'tipo_deduccion': '057', 
                                'clave': '1(lL`}~R', 
                                'concepto': '}}}}vlf', 
                                'importe': '8329690.23'
                            }, 
                            {
                                'tipo_deduccion': '100', 
                                'clave': '~qc}', 
                                'concepto': '}X~', 
                                'importe': '524170.23'
                            }, 
                            {
                                'tipo_deduccion': '104', 
                                'clave': '4}L},~L', 
                                'concepto': '~~}f', 
                                'importe': '40660.23'
                            }, 
                            {
                                
                                'tipo_deduccion': '009', 
                                'clave': 'W}}}}', 
                                'concepto': 'D^', 
                                'importe': '9265310.23'
                            }, 
                            {
                                'tipo_deduccion': '099', 
                                'clave': 'y}}', 
                                'concepto': '~J}', 
                                'importe': '4072880.23'
                            }
                        ]
                    },
                    'otros_pagos': {
                        'otro_pago': [
                            {
                                'tipo_otro_pago': '007', 
                                'clave': '}O~VM~', 
                                'concepto': '}}', 
                                'importe': '9359660.23'
                            }, 
                            {
                                'tipo_otro_pago': '003', 
                                'clave': 'j{}$', 
                                'concepto': '^}}~', 
                                'importe': '1808190.23', 
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '8913760.23'
                                }
                            }, 
                            {
                                'tipo_otro_pago': '003', 
                                'clave': '}~}I', 
                                'concepto': 'pM}', 
                                'importe': '7909810.23', 
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '8574770.23'
                                }
                            }, 
                            {
                                'tipo_otro_pago': '005', 
                                'clave': '}}~Ij~', 
                                'concepto': '}(', 
                                'importe': '2642840.23', 
                                'subsidio_al_empleo': {
                                    'subsidio_causado': '3608130.23'
                                }
                            }, 
                            {
                                'tipo_otro_pago': '005', 
                                'clave': '~}~}~~~L}i}', 
                                'concepto': '}~', 
                                'importe': '4736020.23', 
                                'compensacion_saldos_a_favor': {
                                    'saldo_a_favor': '6382120.23', 
                                    'año': '9858', 
                                    'remanente_sal_fav': 
                                    '888430.23'
                                }
                            }
                        ]
                    }, 
                    'incapacidades': {
                        'incapacidad': [
                            {
                                'dias_incapacidad': '7842', 
                                'tipo_incapacidad': '04', 
                                'importe_monetario': '664540.23'
                            }, 
                            {
                                'dias_incapacidad': '4894', 
                                'tipo_incapacidad': '01', 
                                'importe_monetario': '6949690.23'
                            }, 
                            {
                                'dias_incapacidad': '9391', 
                                'tipo_incapacidad': '04', 
                                'importe_monetario': ''
                            }, 
                            {
                                'dias_incapacidad': '6033', 
                                'tipo_incapacidad': '03', 
                                'importe_monetario': '1414180.23'
                            }, 
                            {
                                'dias_incapacidad': '8309', 
                                'tipo_incapacidad': '04', 
                                'importe_monetario': '7558760.23'
                            }
                        ]
                    }
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_bad_version(self):
        sax_handler = CFDI33SAXHandler().use_nomina12()
        with self.assertRaises(ValueError) as context:
            sax_handler.transform_from_file("./tests/Resources/nomina12/bad_version_nomina01.xml")
        exception = context.exception
        self.assertIn('Incorrect type of CFDI, this handler only support CFDI version 3.3', str(exception), 'Not expected error message')
    
    def test_transform_file_bad_version_xsdvalidation(self):
        schema_validator = SchemaHelper.get_schema_validator_cfdi33()
        sax_handler = CFDI33SAXHandler(schema_validator=schema_validator).use_nomina12()
        with self.assertRaises(etree.DocumentInvalid) as context:
            sax_handler.transform_from_file("./tests/Resources/nomina12/bad_version_nomina01.xml")
        exception = context.exception
        self.assertIn("The value 'Zapopan, Jalisco' has a length of '16'; this differs from the allowed length of '5'", str(exception), 'Not expected error message')
    
    def test_transform_file_broken_xml(self):
        sax_handler = CFDI33SAXHandler().use_nomina12()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/nomina12/broken_nomina12_01.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            "cfdi33": {
                "version": "3.3",
                "serie": "",
                "folio": "123456",
                "fecha": "2021-05-27T09:49:02",
                "no_certificado": "30001000000400002434",
                "subtotal": "1782.11",
                "descuento": "748.07",
                "total": "1034.04",
                "moneda": "MXN",
                "tipo_cambio": "",
                "tipo_comprobante": "N",
                "metodo_pago": "PUE",
                "forma_pago": "99",
                "condiciones_pago": "",
                "lugar_expedicion": "45400",
                'sello':'gT69zVFxYPjldjsihtnBp0/K7TijUNAMRE/3WdItaIYl2bvMjbqRUyvHxlHl2TcL/nS9LuaYZiESqx2+z17lW+XGr8eG95Evy79cfYJXXGoLp2DDoiNGnjPJml8CtpyzTq02Ltw4CJoA9pA3luxoR4bThMRdtoujwg5whSMRPoYKRc3ulTa+A79WEPLfiU7klhdaZ1E6Bxb6SWnLzgTItcCUSy+nfw6a3EeJOD9qC7+lmPG0Dt2CR+mgkQMfcFinb+kWZJViGKc8D0BKGScdePGN7PiXRHGpjqYC426hQaDsmcgPH4obMNSngYshRljWS/B5fYxqrH4CiaKFHFvbMg==',
                'certificado':'MIIFuzCCA6OgAwIBAgIUMzAwMDEwMDAwMDA0MDAwMDI0MzQwDQYJKoZIhvcNAQELBQAwggErMQ8wDQYDVQQDDAZBQyBVQVQxLjAsBgNVBAoMJVNFUlZJQ0lPIERFIEFETUlOSVNUUkFDSU9OIFRSSUJVVEFSSUExGjAYBgNVBAsMEVNBVC1JRVMgQXV0aG9yaXR5MSgwJgYJKoZIhvcNAQkBFhlvc2Nhci5tYXJ0aW5lekBzYXQuZ29iLm14MR0wGwYDVQQJDBQzcmEgY2VycmFkYSBkZSBjYWRpejEOMAwGA1UEEQwFMDYzNzAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBDSVVEQUQgREUgTUVYSUNPMREwDwYDVQQHDAhDT1lPQUNBTjERMA8GA1UELRMIMi41LjQuNDUxJTAjBgkqhkiG9w0BCQITFnJlc3BvbnNhYmxlOiBBQ0RNQS1TQVQwHhcNMTkwNjE3MTk0NDE0WhcNMjMwNjE3MTk0NDE0WjCB4jEnMCUGA1UEAxMeRVNDVUVMQSBLRU1QRVIgVVJHQVRFIFNBIERFIENWMScwJQYDVQQpEx5FU0NVRUxBIEtFTVBFUiBVUkdBVEUgU0EgREUgQ1YxJzAlBgNVBAoTHkVTQ1VFTEEgS0VNUEVSIFVSR0FURSBTQSBERSBDVjElMCMGA1UELRMcRUtVOTAwMzE3M0M5IC8gWElRQjg5MTExNlFFNDEeMBwGA1UEBRMVIC8gWElRQjg5MTExNk1HUk1aUjA1MR4wHAYDVQQLExVFc2N1ZWxhIEtlbXBlciBVcmdhdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN0peKpgfOL75iYRv1fqq+oVYsLPVUR/GibYmGKc9InHFy5lYF6OTYjnIIvmkOdRobbGlCUxORX/tLsl8Ya9gm6Yo7hHnODRBIDup3GISFzB/96R9K/MzYQOcscMIoBDARaycnLvy7FlMvO7/rlVnsSARxZRO8Kz8Zkksj2zpeYpjZIya/369+oGqQk1cTRkHo59JvJ4Tfbk/3iIyf4H/Ini9nBe9cYWo0MnKob7DDt/vsdi5tA8mMtA953LapNyCZIDCRQQlUGNgDqY9/8F5mUvVgkcczsIgGdvf9vMQPSf3jjCiKj7j6ucxl1+FwJWmbvgNmiaUR/0q4m2rm78lFAgMBAAGjHTAbMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgbAMA0GCSqGSIb3DQEBCwUAA4ICAQBcpj1TjT4jiinIujIdAlFzE6kRwYJCnDG08zSp4kSnShjxADGEXH2chehKMV0FY7c4njA5eDGdA/G2OCTPvF5rpeCZP5Dw504RZkYDl2suRz+wa1sNBVpbnBJEK0fQcN3IftBwsgNFdFhUtCyw3lus1SSJbPxjLHS6FcZZ51YSeIfcNXOAuTqdimusaXq15GrSrCOkM6n2jfj2sMJYM2HXaXJ6rGTEgYmhYdwxWtil6RfZB+fGQ/H9I9WLnl4KTZUS6C9+NLHh4FPDhSk19fpS2S/56aqgFoGAkXAYt9Fy5ECaPcULIfJ1DEbsXKyRdCv3JY89+0MNkOdaDnsemS2o5Gl08zI4iYtt3L40gAZ60NPh31kVLnYNsmvfNxYyKp+AeJtDHyW9w7ftM0Hoi+BuRmcAQSKFV3pk8j51la+jrRBrAUv8blbRcQ5BiZUwJzHFEKIwTsRGoRyEx96sNnB03n6GTwjIGz92SmLdNl95r9rkvp+2m4S6q1lPuXaFg7DGBrXWC8iyqeWE2iobdwIIuXPTMVqQb12m1dAkJVRO5NdHnP/MpqOvOgLqoZBNHGyBg4Gqm4sCJHCxA1c8Elfa2RQTCk0tAzllL4vOnI1GHkGJn65xokGsaU4B4D36xh7eWrfj4/pgWHmtoDAYa8wzSwo2GVCZOs+mtEgOQB91/g==',
                'confirmacion':'',
                "emisor": {
                    "rfc": "EKU9003173C9",
                    "nombre": "EMISOR",
                    "regimen_fiscal": "601"
                },
                "receptor": {
                    "rfc": "KICR630120NX3",
                    "nombre": "RECEPTOR",
                    "residencia_fiscal": "",
                    "num_reg_id_trib": "",
                    "uso_cfdi": "P01"
                },
                "conceptos": [],
                "impuestos": {
                    "retenciones": [],
                    "traslados": [],
                    "total_impuestos_traslados" :"",
                    "total_impuestos_retenidos" :""
                },
                "complementos": "Nomina",
                "addendas": ""
            },
            "tfd11": [],
            "nomina12": [
                {
                    "version": "1.2",
                    "tipo_nomina": "O",
                    "fecha_pago": "2021-04-09",
                    "fecha_inicial_pago": "2021-04-05",
                    "fecha_final_pago": "2021-04-11",
                    "num_dias_pagados": "5.000",
                    "total_percepciones": "1730.34",
                    "total_deducciones": "748.07",
                    "total_otros_pagos": "51.77",
                    "emisor": {
                        "curp": "",
                        "registro_patronal": "A0000000000",
                        "rfc_patron_origen": "",
                        "entidad_SNCF": {
                            "origen_recurso": "",
                            "monto_recurso_propio": ""
                        }
                    },
                    "receptor": {
                        "curp": "XEXX010101HNEXXXA4",
                        "num_seguridad_social": "00000000000",
                        "fecha_inicio_rel_laboral": "2019-11-11",
                        "antigüedad": "P74W",
                        "tipo_contrato": "01",
                        "sindicalizado": "No",
                        "tipo_jornada": "01",
                        "tipo_regimen": "02",
                        "num_empleado": "1",
                        "departamento": "",
                        "puesto": "PUESTO",
                        "riesgo_puesto": "5",
                        "periodicidad_pago": "02",
                        "banco": "",
                        "cuenta_bancaria": "",
                        "salario_base_cot_apor": "281.27",
                        "salario_diario_integrado": "281.26",
                        "clave_ent_fed": "JAL",
                        "subcontratacion": []
                    },
                    "percepciones": {
                        "total_sueldos": "1730.34",
                        "total_separacion_indemnizacion": "",
                        "total_jubilacion_pension_retiro": "",
                        "total_gravado": "1427.12",
                        "total_exento": "303.22",
                        "percepcion": [
                            {
                                "tipo_percepcion": "001",
                                "clave": "P001",
                                "concepto": "Sueldo Normal",
                                "importe_gravado": "1248.73",
                                "importe_exento": "0.00",
                                "horas_extra": []
                            },
                            {
                                "tipo_percepcion": "001",
                                "clave": "P004",
                                "concepto": "Dia Festivo Laborado",
                                "importe_gravado": "178.39",
                                "importe_exento": "178.39",
                                "horas_extra": []
                            },
                            {
                                "tipo_percepcion": "005",
                                "clave": "P035",
                                "concepto": "Aportacion Fondo Empresa",
                                "importe_gravado": "0.00",
                                "importe_exento": "40.58",
                                "horas_extra": []
                            },
                            {
                                "tipo_percepcion": "029",
                                "clave": "P031",
                                "concepto": "Vales de Despensa",
                                "importe_gravado": "0.00",
                                "importe_exento": "58.00",
                                "horas_extra": []
                            },
                            {
                                "tipo_percepcion": "029",
                                "clave": "P032",
                                "concepto": "Canasta Basica",
                                "importe_gravado": "0.00",
                                "importe_exento": "26.25",
                                "horas_extra": []
                            }
                        ]
                    },
                    "deducciones": {
                        "total_otras_deducciones": "748.07",
                        "total_impuestos_retenidos": "",
                        "deduccion": [
                            {
                                "tipo_deduccion": "006",
                                "clave": "D003",
                                "concepto": "Falta Incapacidad Enfermedad General",
                                "importe": "356.78"
                            },
                            {
                                "tipo_deduccion": "004",
                                "clave": "D010",
                                "concepto": "Aportacion Fondo de Ahorro",
                                "importe": "40.58"
                            },
                            {
                                "tipo_deduccion": "001",
                                "clave": "D002",
                                "concepto": "Cuota IMSS",
                                "importe": "26.92"
                            },
                            {
                                "tipo_deduccion": "019",
                                "clave": "D011",
                                "concepto": "Cuota Sindical",
                                "importe": "11.60"
                            },
                            {
                                "tipo_deduccion": "020",
                                "clave": "D009",
                                "concepto": "Falta Proyecto",
                                "importe": "312.19"
                            }
                        ]
                    },
                    "otros_pagos": {
                        "otro_pago": [
                            {
                                "tipo_otro_pago": "002",
                                "clave": "SEAP",
                                "concepto": "SUBSIDIO PARA EMPLEO APLICADO",
                                "importe": "51.77",
                                "subsidio_al_empleo": {
                                    "subsidio_causado": "93.66"
                                }
                            }
                        ]
                    },
                    "incapacidades": {
                        "incapacidad": [
                            {
                                "dias_incapacidad": "2",
                                "tipo_incapacidad": "02",
                                "importe_monetario": "356.78"
                            }
                        ]
                    }
                }
            ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_broken_xml_validation(self):
        schema_validator = SchemaHelper.get_schema_validator_cfdi33()
        sax_handler = CFDI33SAXHandler(schema_validator=schema_validator).use_nomina12()
        with self.assertRaises(etree.DocumentInvalid) as context:
            sax_handler.transform_from_file("./tests/Resources/nomina12/broken_nomina12_01.xml")
        exception = context.exception
        self.assertIn("Element '{http://www.sat.gob.mx/nomina12}Receptor': This element is not expected. Expected is ( {http://www.sat.gob.mx/nomina12}EntidadSNCF )., line 1", str(exception), 'Not expected error message')