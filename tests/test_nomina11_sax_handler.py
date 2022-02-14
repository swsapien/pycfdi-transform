from pycfdi_transform import CFDI32SAXHandler
import unittest

class TestNomina11SAXHandler(unittest.TestCase):

      def test_transform_file_nomina11_complete_nom(self):
         sax_handler = CFDI32SAXHandler().use_nomina11()
         cfdi_data = sax_handler.transform_from_file("./tests/Resources/nomina11/nom_complete.xml")
         self.assertIsNotNone(cfdi_data)
         expected_dict = {
            "cfdi32":{
               "version":"3.2",
               "serie":"A",
               "folio":"1",
               "fecha":"2015-03-05T10:33:48",
               "no_certificado":"20001000000100005867",
               "subtotal":"35000.00",
               "descuento":"0.00",
               "total":"40600.00",
               "moneda":"Pesos",
               "tipo_cambio":"",
               "tipo_comprobante":"egreso",
               "metodo_pago":"No Identificado",
               "forma_pago":"PAGO EN UNA SOLA EXHIBICION",
               "condiciones_pago":"",
               "lugar_expedicion":"Zapopan, Jalisco",
               "sello":"XXXXXXXXXX",
               "certificado":"XXXXXXXX",
               "emisor":{
                  "rfc":"AAA010101AAA",
                  "nombre":"Empresa de Pruebas SA DE CV",
                  "regimen_fiscal":[
                     "Regimen General de Ley Personas Morales de Prueba"
                  ]
               },
               "receptor":{
                  "rfc":"CACX7605101P8",
                  "nombre":"EMPLEADO DE PRUEBA"
               },
               "conceptos":[

               ],
               "impuestos":{
                  "retenciones":[
                     {
                        "impuesto":"ISR",
                        "importe":"0.00"
                     },
                     {
                        "impuesto":"IVA",
                        "importe":"0.00"
                     }
                  ],
                  "traslados":[
                     {
                        "impuesto":"IVA",
                        "tasa":"16.00",
                        "importe":"5600.00"
                     }
                  ],
                  "total_impuestos_traslados":"5600.00",
                  "total_impuestos_retenidos":"0.00"
               },
               "complementos":"Nomina TimbreFiscalDigital",
               "addendas":""
            },
            "tfd10":[
               {
                  "version":"1.0",
                  "no_certificado_sat":"20001000000100005761",
                  "uuid":"CD13D35E-2FCF-4A23-ADCA-51F2E48B8018",
                  "fecha_timbrado":"2014-04-03T18:17:02",
                  "sello_cfd":"MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=",
                  "sello_sat":"KzZwap6lXpYzVpFtgaHKkbjzxo0BYxpKRDoxAHXgt5PCvhE4S5r9YU7KRegCHYf4S/K7WeKMtO/4ReAPPCL7oyUiO5JkRisrva3C1mYBcOBBMoLoCgbjjIw1OlHWr3x+U9rQcRT3ENVs9tmFICqL37F66JYnHzpRbeBBkri86wA="
               }
            ],
            "nomina11":[
               {
                  "version":"1.1",
                  "registro_patronal":"A0000000000",
                  "num_empleado":"9872",
                  "curp":"XEXX010101HNEXXXA4",
                  "tipo_regimen":"1",
                  "num_seguridad_social":"00000000000",
                  "fecha_pago":"2013-11-15",
                  "fecha_inicial_pago":"2014-11-01",
                  "fecha_final_pago":"2014-11-15",
                  "num_dias_pagados":"15",
                  "departamento":"DPTO",
                  "clabe":"000000000000000000",
                  "banco":"113",
                  "fecha_inicio_rel_laboral":"2009-06-01",
                  "antiguedad":"228",
                  "puesto":"ADMIN",
                  "tipo_contrato":"Base",
                  "tipo_jornada":"Diurna",
                  "periodicidad_pago":"Quincenal",
                  "salario_base_cot_apor":"10000.00",
                  "riesgo_puesto":"1",
                  "salario_diario_integrado":"696.80",
                  "percepciones":{
                     "total_gravado":"13000.00",
                     "total_exento":"379.00",
                     "percepcion":[
                        {
                           "tipo_percepcion":"001",
                           "clave":"139",
                           "concepto":"Sueldos, Salarios Rayas y Jornales",
                           "importe_gravado":"10000.00",
                           "importe_exento":"0.00"
                        },
                        {
                           "tipo_percepcion":"002",
                           "clave":"164",
                           "concepto":"Gratificación Anual (Aguinaldo)",
                           "importe_gravado":"1000.00",
                           "importe_exento":"0.00"
                        },
                        {
                           "tipo_percepcion":"004",
                           "clave":"112",
                           "concepto":"Reembolso gastos médicos dentales",
                           "importe_gravado":"1000.00",
                           "importe_exento":"0.00"
                        },
                        {
                           "tipo_percepcion":"029",
                           "clave":"563",
                           "concepto":"Bonos de Despensa",
                           "importe_gravado":"0.00",
                           "importe_exento":"379.00"
                        },
                        {
                           "tipo_percepcion":"019",
                           "clave":"545",
                           "concepto":"Horas Extra",
                           "importe_gravado":"1000.00",
                           "importe_exento":"0.00"
                        }
                     ]
                  },
                  "deducciones":{
                     "total_gravado":"3332.1",
                     "total_exento":"0.00",
                     "deduccion":[
                        {
                           "tipo_deduccion":"001",
                           "clave":"223",
                           "concepto":"Seguro Social",
                           "importe_gravado":"278.39",
                           "importe_exento":"0.00"
                        },
                        {
                           "tipo_deduccion":"002",
                           "clave":"231",
                           "concepto":"ISR",
                           "importe_gravado":"2053.71",
                           "importe_exento":"0.00"
                        },
                        {
                           "tipo_deduccion":"020",
                           "clave":"653",
                           "concepto":"Ausencia",
                           "importe_gravado":"1000.00",
                           "importe_exento":"0.00"
                        },
                        {
                           "tipo_deduccion":"007",
                           "clave":"262",
                           "concepto":"Pensión alimenticia",
                           "importe_gravado":"0.00",
                           "importe_exento":"0.00"
                        }
                     ]
                  },
                  "incapacidades":{
                     "incapacidad":[
                        {
                           "dias_incapacidad":"2",
                           "tipo_incapacidad":"1",
                           "descuento":"300.00"
                        }
                     ]
                  },
                  "horas_extras":{
                     "horas_extra":[
                        {
                           "dias":"2",
                           "tipo_horas":"Dobles",
                           "horas_extra":"3",
                           "importe_pagado":"2653.42"
                        }
                     ]
                  }
               }
            ]
         }
         self.assertDictEqual(cfdi_data, expected_dict)

      def test_transform_file_nomina11_safe_numerics(self):
         sax_handler = CFDI32SAXHandler(safe_numerics=True).use_nomina11()
         cfdi_data = sax_handler.transform_from_file("./tests/Resources/nomina11/nom_safe_numerics.xml")
         self.assertIsNotNone(cfdi_data)
         expected_dict = {
            "cfdi32":{
               "version":"3.2",
               "serie":"A",
               "folio":"1",
               "fecha":"2015-03-05T10:33:48",
               "no_certificado":"20001000000100005867",
               "subtotal":"35000.00",
               "descuento":"0.00",
               "total":"40600.00",
               "moneda":"Pesos",
               "tipo_cambio":"1.00",
               "tipo_comprobante":"egreso",
               "metodo_pago":"No Identificado",
               "forma_pago":"PAGO EN UNA SOLA EXHIBICION",
               "condiciones_pago":"",
               "lugar_expedicion":"Zapopan, Jalisco",
               "sello":"XXXXXXXXXX",
               "certificado":"XXXXXXXX",
               "emisor":{
                  "rfc":"AAA010101AAA",
                  "nombre":"Empresa de Pruebas SA DE CV",
                  "regimen_fiscal":[
                     "Regimen General de Ley Personas Morales de Prueba"
                  ]
               },
               "receptor":{
                  "rfc":"CACX7605101P8",
                  "nombre":"EMPLEADO DE PRUEBA"
               },
               "conceptos":[

               ],
               "impuestos":{
                  "retenciones":[
                     {
                        "impuesto":"ISR",
                        "importe":"0.00"
                     },
                     {
                        "impuesto":"IVA",
                        "importe":"0.00"
                     }
                  ],
                  "traslados":[
                     {
                        "impuesto":"IVA",
                        "tasa":"16.00",
                        "importe":"5600.00"
                     }
                  ],
                  "total_impuestos_traslados":"5600.00",
                  "total_impuestos_retenidos":"0.00"
               },
               "complementos":"Nomina TimbreFiscalDigital",
               "addendas":""
            },
            "tfd10":[
               {
                  "version":"1.0",
                  "no_certificado_sat":"20001000000100005761",
                  "uuid":"CD13D35E-2FCF-4A23-ADCA-51F2E48B8018",
                  "fecha_timbrado":"2014-04-03T18:17:02",
                  "sello_cfd":"MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=",
                  "sello_sat":"KzZwap6lXpYzVpFtgaHKkbjzxo0BYxpKRDoxAHXgt5PCvhE4S5r9YU7KRegCHYf4S/K7WeKMtO/4ReAPPCL7oyUiO5JkRisrva3C1mYBcOBBMoLoCgbjjIw1OlHWr3x+U9rQcRT3ENVs9tmFICqL37F66JYnHzpRbeBBkri86wA="
               }
            ],
            "nomina11":[
               {
                  "version":"1.1",
                  "registro_patronal":"A0000000000",
                  "num_empleado":"9872",
                  "curp":"XEXX010101HNEXXXA4",
                  "tipo_regimen":"1",
                  "num_seguridad_social":"00000000000",
                  "fecha_pago":"2013-11-15",
                  "fecha_inicial_pago":"2014-11-01",
                  "fecha_final_pago":"2014-11-15",
                  "num_dias_pagados":"15",
                  "departamento":"DPTO",
                  "clabe":"000000000000000000",
                  "banco":"113",
                  "fecha_inicio_rel_laboral":"2009-06-01",
                  "antiguedad":"228",
                  "puesto":"ADMIN",
                  "tipo_contrato":"Base",
                  "tipo_jornada":"Diurna",
                  "periodicidad_pago":"Quincenal",
                  "salario_base_cot_apor":"0.00",
                  "riesgo_puesto":"1",
                  "salario_diario_integrado":"0.00",
                  "percepciones":{
                     "total_gravado":"0.00",
                     "total_exento":"0.00",
                     "percepcion":[
                        {
                           "tipo_percepcion":"001",
                           "clave":"139",
                           "concepto":"Sueldos, Salarios Rayas y Jornales",
                           "importe_gravado":"0.00",
                           "importe_exento":"0.00"
                        }
                     ]
                  },
                  "deducciones":{
                     "total_gravado":"0.00",
                     "total_exento":"0.00",
                     "deduccion":[
                        {
                           "tipo_deduccion":"001",
                           "clave":"223",
                           "concepto":"Seguro Social",
                           "importe_gravado":"0.00",
                           "importe_exento":"0.00"
                        }
                     ]
                  },
                  "incapacidades":{
                     "incapacidad":[
                        {
                           "dias_incapacidad":"2",
                           "tipo_incapacidad":"1",
                           "descuento":"0.00"
                        }
                     ]
                  },
                  "horas_extras":{
                     "horas_extra":[
                        {
                           "dias":"2",
                           "tipo_horas":"Dobles",
                           "horas_extra":"3",
                           "importe_pagado":"0.00"
                        }
                     ]
                  }
               }
            ]
         }
         self.assertDictEqual(cfdi_data, expected_dict)

      def test_transform_file_nomina11_empty_char(self):
         sax_handler = CFDI32SAXHandler(empty_char='~').use_nomina11()
         cfdi_data = sax_handler.transform_from_file("./tests/Resources/nomina11/nom_empty_chars.xml")
         self.assertIsNotNone(cfdi_data)
         expected_dict = {
            "cfdi32":{
               "version":"3.2",
               "serie":"A",
               "folio":"1",
               "fecha":"2015-03-05T10:33:48",
               "no_certificado":"20001000000100005867",
               "subtotal":"35000.00",
               "descuento":"0.00",
               "total":"40600.00",
               "moneda":"Pesos",
               "tipo_cambio":"~",
               "tipo_comprobante":"egreso",
               "metodo_pago":"No Identificado",
               "forma_pago":"PAGO EN UNA SOLA EXHIBICION",
               "condiciones_pago":"~",
               "lugar_expedicion":"Zapopan, Jalisco",
               "sello":"XXXXXXXXXX",
               "certificado":"XXXXXXXX",
               "emisor":{
                  "rfc":"AAA010101AAA",
                  "nombre":"Empresa de Pruebas SA DE CV",
                  "regimen_fiscal":[
                     "Regimen General de Ley Personas Morales de Prueba"
                  ]
               },
               "receptor":{
                  "rfc":"CACX7605101P8",
                  "nombre":"EMPLEADO DE PRUEBA"
               },
               "conceptos":[

               ],
               "impuestos":{
                  "retenciones":[
                     {
                        "impuesto":"ISR",
                        "importe":"0.00"
                     },
                     {
                        "impuesto":"IVA",
                        "importe":"0.00"
                     }
                  ],
                  "traslados":[
                     {
                        "impuesto":"IVA",
                        "tasa":"16.00",
                        "importe":"5600.00"
                     }
                  ],
                  "total_impuestos_traslados":"5600.00",
                  "total_impuestos_retenidos":"0.00"
               },
               "complementos":"Nomina TimbreFiscalDigital",
               "addendas":"~"
            },
            "tfd10":[
               {
                  "version":"1.0",
                  "no_certificado_sat":"20001000000100005761",
                  "uuid":"CD13D35E-2FCF-4A23-ADCA-51F2E48B8018",
                  "fecha_timbrado":"2014-04-03T18:17:02",
                  "sello_cfd":"MUIy85bMjr2K7CLZcj1PnUU3a56KmrqOvF7ubEnaa0beidmPqi7S0YVznA5EKs76c4sJFBGhR73WA47RVNqUFbGdWrd43Mv326SJ+4eRAiJ/2AzAdMX742cxiZ76K9FavCz9sRYkHJLvRkAOk8JewVRWGglEnJLReBr4SX/zGfg=",
                  "sello_sat":"KzZwap6lXpYzVpFtgaHKkbjzxo0BYxpKRDoxAHXgt5PCvhE4S5r9YU7KRegCHYf4S/K7WeKMtO/4ReAPPCL7oyUiO5JkRisrva3C1mYBcOBBMoLoCgbjjIw1OlHWr3x+U9rQcRT3ENVs9tmFICqL37F66JYnHzpRbeBBkri86wA="
               }
            ],
            "nomina11":[
               {
                  "version":"1.1",
                  "registro_patronal":"~",
                  "num_empleado":"9872",
                  "curp":"XEXX010101HNEXXXA4",
                  "tipo_regimen":"1",
                  "num_seguridad_social":"~",
                  "fecha_pago":"2013-11-15",
                  "fecha_inicial_pago":"2014-11-01",
                  "fecha_final_pago":"2014-11-15",
                  "num_dias_pagados":"15",
                  "departamento":"DPTO",
                  "clabe":"000000000000000000",
                  "banco":"113",
                  "fecha_inicio_rel_laboral":"~",
                  "antiguedad":"~",
                  "puesto":"~",
                  "tipo_contrato":"~",
                  "tipo_jornada":"~",
                  "periodicidad_pago":"Quincenal",
                  "salario_base_cot_apor":"~",
                  "riesgo_puesto":"1",
                  "salario_diario_integrado":"~",
                  "percepciones":{
                     "total_gravado":"~",
                     "total_exento":"~",
                     "percepcion":[
                        {
                           "tipo_percepcion":"001",
                           "clave":"139",
                           "concepto":"Sueldos, Salarios Rayas y Jornales",
                           "importe_gravado":"~",
                           "importe_exento":"~"
                        }
                     ]
                  },
                  "deducciones":{
                     "total_gravado":"~",
                     "total_exento":"~",
                     "deduccion":[
                        {
                           "tipo_deduccion":"001",
                           "clave":"223",
                           "concepto":"Seguro Social",
                           "importe_gravado":"~",
                           "importe_exento":"~"
                        }
                     ]
                  },
                  "incapacidades":{
                     "incapacidad":[
                        {
                           "dias_incapacidad":"2",
                           "tipo_incapacidad":"1",
                           "descuento":"~"
                        }
                     ]
                  },
                  "horas_extras":{
                     "horas_extra":[
                        {
                           "dias":"2",
                           "tipo_horas":"Dobles",
                           "horas_extra":"3",
                           "importe_pagado":"~"
                        }
                     ]
                  }
               }
            ]
         }
         self.assertDictEqual(cfdi_data, expected_dict)

      def test_transform_file_nomina11_bad_version(self):
         sax_handler = CFDI32SAXHandler().use_nomina11()
         with self.assertRaises(ValueError) as context:
            sax_handler.transform_from_file("./tests/Resources/nomina11/nom_bad_version.xml")
         exception = context.exception
         self.assertIn('Incorrect type of Nomina, this handler only support Nomina version 1.1', str(exception),
                       'Not expected error message')