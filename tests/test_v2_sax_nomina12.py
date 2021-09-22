import unittest
import pycfdi_transform.v2.sax.cfdi33.sax_handler as ct

class TestHanderCfdi33Nomina12Tests(unittest.TestCase):
    def test_transform_file_complete_nom(self):
        sax_handler = ct.SAXHandler().use_nomina12()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/nomina12/nom_complete.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': '"',
                'folio': '/>KA',
                'fecha': '2018-01-10T07:22:51.20',
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
            'tfd': [],
            'implocal': [],
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
                        'cuenta_bancaria': '2741',
                        'salario_base_cot_apor': '8635520.23',
                        'salario_diario_integrado': '2928750.23',
                        'clave_ent_fed': 'VT',
                        'subcontratacion': [
                            {
                                'rfc_labora': '&ÑEL561104H5A',
                                'porcentaje_tiempo': '91.4441937119451'
                            }, 
                            {
                                'rfc_labora': 'ÑÑL&020703408',
                                'porcentaje_tiempo': '50.8166999909451'
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
                        'TotalOtrasDeducciones': '3965300.23', 
                        'TotalImpuestosRetenidos': '4272620.23', 
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
        sax_handler = ct.SAXHandler(safe_numerics=True).use_nomina12()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/nomina12/nom_complete.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': '"',
                'folio': '/>KA',
                'fecha': '2018-01-10T07:22:51.20',
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
            'tfd': [],
            'implocal': [],
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
                        'cuenta_bancaria': '2741',
                        'salario_base_cot_apor': '8635520.23',
                        'salario_diario_integrado': '2928750.23',
                        'clave_ent_fed': 'VT',
                        'subcontratacion': [
                            {
                                'rfc_labora': '&ÑEL561104H5A',
                                'porcentaje_tiempo': '91.4441937119451'
                            }, 
                            {
                                'rfc_labora': 'ÑÑL&020703408',
                                'porcentaje_tiempo': '50.8166999909451'
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
                        'TotalOtrasDeducciones': '3965300.23', 
                        'TotalImpuestosRetenidos': '4272620.23', 
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
        sax_handler = ct.SAXHandler(safe_numerics=True, empty_char='-').use_nomina12()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/nomina12/nom_complete.xml")
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
            'cfdi33': {
                'version': '3.3',
                'serie': '"',
                'folio': '/>KA',
                'fecha': '2018-01-10T07:22:51.20',
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
            'tfd': [],
            'implocal': [],
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
                        'cuenta_bancaria': '2741',
                        'salario_base_cot_apor': '8635520.23',
                        'salario_diario_integrado': '2928750.23',
                        'clave_ent_fed': 'VT',
                        'subcontratacion': [
                            {
                                'rfc_labora': '&ÑEL561104H5A',
                                'porcentaje_tiempo': '91.4441937119451'
                            }, 
                            {
                                'rfc_labora': 'ÑÑL&020703408',
                                'porcentaje_tiempo': '50.8166999909451'
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
                        'TotalOtrasDeducciones': '3965300.23', 
                        'TotalImpuestosRetenidos': '4272620.23', 
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