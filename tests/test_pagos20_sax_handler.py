from pycfdi_transform import CFDI40SAXHandler, SchemaHelper
import unittest

class TestPagos20SAXHandler(unittest.TestCase):
    
    def test_transform_file_pagos20_complete(self):
        sax_handler = CFDI40SAXHandler().use_pagos20()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos20/pago_complete.xml')
        self.assertIsNotNone(cfdi_data)
        expected_dict = {
           "cfdi40":{
              "version":"4.0",
              "serie":"Serie",
              "folio":"Folio",
              "fecha":"2021-12-16T15:40:21",
              "no_certificado":"30001000000400002444",
              "subtotal":"0",
              "descuento":"",
              "total":"0.0",
              "moneda":"XXX",
              "tipo_cambio":"",
              "tipo_comprobante":"P",
              "metodo_pago":"",
              "forma_pago":"",
              "condiciones_pago":"",
              "exportacion":"01",
              "lugar_expedicion":"20008",
              "sello":"RaO1PmPrKzLHLOfbi+FjJU83PRbEIlpicZGHT1qGENItdZ5VVi85Vsq6w/YnzbG0QA433mKtcirn/OUrB5jAt+X4WQ6BWEagXqHHxvmjjro5YGPcYtwnvcxh3Bt920P9/Pky4D92OR5hoz7p8hq0YA2jMegegugt1r7bnmnOWG42osW2PGMvzRtSkPPoPNKRY5+NVRIREbe3+ckj/YiJ5tyRLDyN0ea66N4ImWKJzKtxcGU5BrgYJpzuJm9B1X8ODeaC7KrOqvdX3Jg7CcYRoInDBj7/Js+F7UCeA1djy0Kg9VNnA+oSS50/q9erkTeMfHSh3UTciTEM/uGe0n7Vig==",
              "certificado":"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",
              "confirmacion":"",
              "emisor":{
                 "rfc":"XAXX010101000",
                 "nombre":"PUBLICO GENERAL",
                 "regimen_fiscal":"601",
                 "fac_atr_adquirente":""
              },
              "receptor":{
                 "rfc":"XAXX010101000",
                 "nombre":"Nombre",
                 "domicilio_fiscal_receptor":"45000",
                 "residencia_fiscal":"",
                 "num_reg_id_trib":"",
                 "regimen_fiscal_receptor":"601",
                 "uso_cfdi":"G01"
              },
              "conceptos":[

              ],
              "impuestos":{
                 "retenciones":[

                 ],
                 "traslados":[

                 ],
                 "total_impuestos_traslados":"",
                 "total_impuestos_retenidos":""
              },
              "complementos":"Pagos",
              "addendas":""
           },
           "tfd11":[

           ],
           "pagos20":[
              {
                 "pago":[
                    {
                       "fecha_pago":"2021-12-02T00:18:10",
                       "forma_de_pago_p":"01",
                       "moneda_p":"USD",
                       "tipo_cambio_p":"1",
                       "monto":"14000.00",
                       "num_operacion":"1",
                       "rfc_emisor_cta_ord":"XAXX010101000",
                       "nom_banco_ord_ext":"NomBancoOrdExt1",
                       "cta_ordenante":"003293323",
                       "rfc_emisor_cta_ben":"XAXX010101000",
                       "cta_beneficiario":"003293324",
                       "tipo_cad_pago":"1",
                       "cert_pago":"004004040",
                       "cad_pago":"CadPago",
                       "sello_pago":"SelloPago",
                       "docto_relacionado":[
                          {
                             "id_documento":"BEDC8964-7E57-4604-9968-7E01378E8706",
                             "serie":"Serie3",
                             "folio":"Folio3",
                             "moneda_dr":"MXN",
                             "equivalencia_dr":"1.329310",
                             "num_parcialidad":"1",
                             "imp_saldo_ant":"5000.00",
                             "imp_pagado":"2000.00",
                             "imp_saldo_insoluto":"3000.00",
                             "objecto_imp_dr":"02",
                             "impuestos_dr":[
                                {
                                   "retenciones_dr":[
                                      {
                                         "base_dr":"1",
                                         "impuesto_dr":"001",
                                         "tipo_factor_dr":"Tasa",
                                         "tasa_o_cuota_dr":"0.300000",
                                         "importe_dr":"0.300000"
                                      }
                                   ],
                                   "traslados_dr":[
                                      {
                                         "base_dr":"625000.00",
                                         "impuesto_dr":"002",
                                         "tipo_factor_dr":"Tasa",
                                         "tasa_o_cuota_dr":"0.160000",
                                         "importe_dr":"100000.00"
                                      },
                                      {
                                         "base_dr":"22166372.13",
                                         "impuesto_dr":"002",
                                         "tipo_factor_dr":"Tasa",
                                         "tasa_o_cuota_dr":"0.080000",
                                         "importe_dr":"1773309.77"
                                      },
                                      {
                                         "base_dr":"22166372.13",
                                         "impuesto_dr":"002",
                                         "tipo_factor_dr":"Tasa",
                                         "tasa_o_cuota_dr":"0.000000",
                                         "importe_dr":"0"
                                      },
                                      {
                                         "base_dr":"1",
                                         "impuesto_dr":"002",
                                         "tipo_factor_dr":"Exento",
                                         "tasa_o_cuota_dr":"",
                                         "importe_dr":""
                                      }
                                   ]
                                }
                             ]
                          },
                          {
                             "id_documento":"BEDC8964-7E57-4604-9968-7E01378E8706",
                             "serie":"Serie3",
                             "folio":"Folio3",
                             "moneda_dr":"MXN",
                             "equivalencia_dr":"23.5728",
                             "num_parcialidad":"1",
                             "imp_saldo_ant":"5000.00",
                             "imp_pagado":"2000.00",
                             "imp_saldo_insoluto":"3000.00",
                             "objecto_imp_dr":"02",
                             "impuestos_dr":[
                                {
                                   "retenciones_dr":[

                                   ],
                                   "traslados_dr":[
                                      {
                                         "base_dr":"11083186.11",
                                         "impuesto_dr":"002",
                                         "tipo_factor_dr":"Tasa",
                                         "tasa_o_cuota_dr":"0.160000",
                                         "importe_dr":"1773309.77"
                                      },
                                      {
                                         "base_dr":"1250000.00",
                                         "impuesto_dr":"002",
                                         "tipo_factor_dr":"Tasa",
                                         "tasa_o_cuota_dr":"0.080000",
                                         "importe_dr":"100000.00"
                                      },
                                      {
                                         "base_dr":"1",
                                         "impuesto_dr":"002",
                                         "tipo_factor_dr":"Exento",
                                         "tasa_o_cuota_dr":"",
                                         "importe_dr":""
                                      }
                                   ]
                                }
                             ]
                          }
                       ],
                       "impuestos_p":[
                          {
                             "retenciones_p":[
                                {
                                   "impuesto_p":"001",
                                   "importe_p":"2"
                                }
                             ],
                             "traslados_p":[
                                {
                                   "base_p":"940337.15",
                                   "impuesto_p":"002",
                                   "tipo_factor_p":"Tasa",
                                   "tasa_o_cuota_p":"0.160000",
                                   "importe_p":"150453.94"
                                },
                                {
                                   "base_p":"16728123.41",
                                   "impuesto_p":"002",
                                   "tipo_factor_p":"Tasa",
                                   "tasa_o_cuota_p":"0.080000",
                                   "importe_p":"1338249.87"
                                },
                                {
                                   "base_p":"16675096.20",
                                   "impuesto_p":"002",
                                   "tipo_factor_p":"Tasa",
                                   "tasa_o_cuota_p":"0.000000",
                                   "importe_p":"0"
                                },
                                {
                                   "base_p":"0.79",
                                   "impuesto_p":"002",
                                   "tipo_factor_p":"Exento",
                                   "tasa_o_cuota_p":"",
                                   "importe_p":""
                                }
                             ]
                          }
                       ]
                    }
                 ],
                 "totales":{
                    "total_retenciones_iva":"0.00",
                    "total_retenciones_isr":"0",
                    "total_retenciones_ieps":"0",
                    "total_traslados_base_iva_16":"940337.15",
                    "total_traslados_impuesto_iva_16":"150453.94",
                    "total_traslados_base_iva_8":"16728123.41",
                    "total_traslados_impuesto_iva_8":"1338249.87",
                    "total_traslados_base_iva_0":"16675096.20",
                    "total_traslados_impuesto_iva_0":"0",
                    "total_traslados_base_iva_exento":"10.79",
                    "monto_total_pagos":"4000.00"
                 },
                 "version":"2.0"
              }
           ]
        }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_pagos20_safenumerics(self):
        sax_handler = CFDI40SAXHandler(safe_numerics=True).use_pagos20()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos20/pago_safe_numbers.xml')
        self.assertIsNotNone(cfdi_data)
        expected_dict ={
         "cfdi40":{
            "version":"4.0",
            "serie":"Serie",
            "folio":"Folio",
            "fecha":"2021-12-16T15:40:21",
            "no_certificado":"30001000000400002444",
            "subtotal":"0",
            "descuento":"0.00",
            "total":"0.0",
            "moneda":"XXX",
            "tipo_cambio":"1.00",
            "tipo_comprobante":"P",
            "metodo_pago":"",
            "forma_pago":"",
            "condiciones_pago":"",
            "exportacion":"01",
            "lugar_expedicion":"20008",
            "sello":"RaO1PmPrKzLHLOfbi+FjJU83PRbEIlpicZGHT1qGENItdZ5VVi85Vsq6w/YnzbG0QA433mKtcirn/OUrB5jAt+X4WQ6BWEagXqHHxvmjjro5YGPcYtwnvcxh3Bt920P9/Pky4D92OR5hoz7p8hq0YA2jMegegugt1r7bnmnOWG42osW2PGMvzRtSkPPoPNKRY5+NVRIREbe3+ckj/YiJ5tyRLDyN0ea66N4ImWKJzKtxcGU5BrgYJpzuJm9B1X8ODeaC7KrOqvdX3Jg7CcYRoInDBj7/Js+F7UCeA1djy0Kg9VNnA+oSS50/q9erkTeMfHSh3UTciTEM/uGe0n7Vig==",
            "certificado":"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",
            "confirmacion":"",
            "emisor":{
               "rfc":"XAXX010101000",
               "nombre":"PUBLICO GENERAL",
               "regimen_fiscal":"601",
               "fac_atr_adquirente":""
            },
            "receptor":{
               "rfc":"XAXX010101000",
               "nombre":"Nombre",
               "domicilio_fiscal_receptor":"45000",
               "residencia_fiscal":"",
               "num_reg_id_trib":"",
               "regimen_fiscal_receptor":"601",
               "uso_cfdi":"G01"
            },
            "conceptos":[

            ],
            "impuestos":{
               "retenciones":[

               ],
               "traslados":[

               ],
               "total_impuestos_traslados":"0.00",
               "total_impuestos_retenidos":"0.00"
            },
            "complementos":"Pagos",
            "addendas":""
         },
         "tfd11":[

         ],
         "pagos20":[
            {
               "pago":[
                  {
                     "fecha_pago":"2021-12-02T00:18:10",
                     "forma_de_pago_p":"01",
                     "moneda_p":"USD",
                     "tipo_cambio_p":"1.00",
                     "monto":"14000.00",
                     "num_operacion":"",
                     "rfc_emisor_cta_ord":"",
                     "nom_banco_ord_ext":"",
                     "cta_ordenante":"",
                     "rfc_emisor_cta_ben":"",
                     "cta_beneficiario":"",
                     "tipo_cad_pago":"",
                     "cert_pago":"",
                     "cad_pago":"",
                     "sello_pago":"",
                     "docto_relacionado":[
                        {
                           "id_documento":"BEDC8964-7E57-4604-9968-7E01378E8706",
                           "serie":"Serie3",
                           "folio":"Folio3",
                           "moneda_dr":"MXN",
                           "equivalencia_dr":"1.329310",
                           "num_parcialidad":"1",
                           "imp_saldo_ant":"5000.00",
                           "imp_pagado":"2000.00",
                           "imp_saldo_insoluto":"3000.00",
                           "objecto_imp_dr":"02",
                           "impuestos_dr":[
                              {
                                 "retenciones_dr":[
                                    {
                                       "base_dr":"1",
                                       "impuesto_dr":"001",
                                       "tipo_factor_dr":"Tasa",
                                       "tasa_o_cuota_dr":"0.300000",
                                       "importe_dr":"0.300000"
                                    }
                                 ],
                                 "traslados_dr":[
                                    {
                                       "base_dr":"625000.00",
                                       "impuesto_dr":"002",
                                       "tipo_factor_dr":"Tasa",
                                       "tasa_o_cuota_dr":"0.160000",
                                       "importe_dr":"100000.00"
                                    },
                                    {
                                       "base_dr":"22166372.13",
                                       "impuesto_dr":"002",
                                       "tipo_factor_dr":"Tasa",
                                       "tasa_o_cuota_dr":"0.080000",
                                       "importe_dr":"1773309.77"
                                    },
                                    {
                                       "base_dr":"22166372.13",
                                       "impuesto_dr":"002",
                                       "tipo_factor_dr":"Tasa",
                                       "tasa_o_cuota_dr":"0.000000",
                                       "importe_dr":"0"
                                    },
                                    {
                                       "base_dr":"1",
                                       "impuesto_dr":"002",
                                       "tipo_factor_dr":"Exento",
                                       "tasa_o_cuota_dr":"0.00",
                                       "importe_dr":"0.00"
                                    }
                                 ]
                              }
                           ]
                        },
                        {
                           "id_documento":"BEDC8964-7E57-4604-9968-7E01378E8706",
                           "serie":"Serie3",
                           "folio":"Folio3",
                           "moneda_dr":"MXN",
                           "equivalencia_dr":"23.5728",
                           "num_parcialidad":"",
                           "imp_saldo_ant":"5000.00",
                           "imp_pagado":"2000.00",
                           "imp_saldo_insoluto":"3000.00",
                           "objecto_imp_dr":"02",
                           "impuestos_dr":[
                              {
                                 "retenciones_dr":[

                                 ],
                                 "traslados_dr":[
                                    {
                                       "base_dr":"11083186.11",
                                       "impuesto_dr":"002",
                                       "tipo_factor_dr":"Tasa",
                                       "tasa_o_cuota_dr":"0.160000",
                                       "importe_dr":"1773309.77"
                                    },
                                    {
                                       "base_dr":"1250000.00",
                                       "impuesto_dr":"002",
                                       "tipo_factor_dr":"Tasa",
                                       "tasa_o_cuota_dr":"0.080000",
                                       "importe_dr":"100000.00"
                                    },
                                    {
                                       "base_dr":"1",
                                       "impuesto_dr":"002",
                                       "tipo_factor_dr":"Exento",
                                       "tasa_o_cuota_dr":"0.00",
                                       "importe_dr":"0.00"
                                    }
                                 ]
                              }
                           ]
                        }
                     ],
                     "impuestos_p":[
                        {
                           "retenciones_p":[
                              {
                                 "impuesto_p":"001",
                                 "importe_p":"2"
                              }
                           ],
                           "traslados_p":[
                              {
                                 "base_p":"940337.15",
                                 "impuesto_p":"002",
                                 "tipo_factor_p":"Tasa",
                                 "tasa_o_cuota_p":"0.160000",
                                 "importe_p":"150453.94"
                              },
                              {
                                 "base_p":"16728123.41",
                                 "impuesto_p":"002",
                                 "tipo_factor_p":"Tasa",
                                 "tasa_o_cuota_p":"0.080000",
                                 "importe_p":"1338249.87"
                              },
                              {
                                 "base_p":"16675096.20",
                                 "impuesto_p":"002",
                                 "tipo_factor_p":"Tasa",
                                 "tasa_o_cuota_p":"0.000000",
                                 "importe_p":"0.00"
                              },
                              {
                                 "base_p":"0.79",
                                 "impuesto_p":"002",
                                 "tipo_factor_p":"Exento",
                                 "tasa_o_cuota_p":"0.00",
                                 "importe_p":"0.00"
                              }
                           ]
                        }
                     ]
                  }
               ],
               "totales":{
                  "total_retenciones_iva":"0.00",
                  "total_retenciones_isr":"0.00",
                  "total_retenciones_ieps":"0.00",
                  "total_traslados_base_iva_16":"0.00",
                  "total_traslados_impuesto_iva_16":"0.00",
                  "total_traslados_base_iva_8":"0.00",
                  "total_traslados_impuesto_iva_8":"0.00",
                  "total_traslados_base_iva_0":"0.00",
                  "total_traslados_impuesto_iva_0":"0.00",
                  "total_traslados_base_iva_exento":"0.00",
                  "monto_total_pagos":"0.00"
               },
               "version":"2.0"
            }
         ]
      }
        self.assertDictEqual(cfdi_data, expected_dict)
    
    def test_transform_file_pagos20_emptychar(self):
        sax_handler = CFDI40SAXHandler(empty_char='-').use_pagos20()
        cfdi_data = sax_handler.transform_from_file('./tests/Resources/pagos20/pago_empty_chars.xml')
        self.assertIsNotNone(cfdi_data)
        expected_dict ={
         "cfdi40":{
            "version":"4.0",
            "serie":"Serie",
            "folio":"Folio",
            "fecha":"2021-12-16T15:40:21",
            "no_certificado":"30001000000400002444",
            "subtotal":"0",
            "descuento":"-",
            "total":"0.0",
            "moneda":"XXX",
            "tipo_cambio":"-",
            "tipo_comprobante":"P",
            "metodo_pago":"-",
            "forma_pago":"-",
            "condiciones_pago":"-",
            "exportacion":"01",
            "lugar_expedicion":"20008",
            "sello":"RaO1PmPrKzLHLOfbi+FjJU83PRbEIlpicZGHT1qGENItdZ5VVi85Vsq6w/YnzbG0QA433mKtcirn/OUrB5jAt+X4WQ6BWEagXqHHxvmjjro5YGPcYtwnvcxh3Bt920P9/Pky4D92OR5hoz7p8hq0YA2jMegegugt1r7bnmnOWG42osW2PGMvzRtSkPPoPNKRY5+NVRIREbe3+ckj/YiJ5tyRLDyN0ea66N4ImWKJzKtxcGU5BrgYJpzuJm9B1X8ODeaC7KrOqvdX3Jg7CcYRoInDBj7/Js+F7UCeA1djy0Kg9VNnA+oSS50/q9erkTeMfHSh3UTciTEM/uGe0n7Vig==",
            "certificado":"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",
            "confirmacion":"-",
            "emisor":{
               "rfc":"XAXX010101000",
               "nombre":"PUBLICO GENERAL",
               "regimen_fiscal":"601",
               "fac_atr_adquirente":"-"
            },
            "receptor":{
               "rfc":"XAXX010101000",
               "nombre":"Nombre",
               "domicilio_fiscal_receptor":"45000",
               "residencia_fiscal":"-",
               "num_reg_id_trib":"-",
               "regimen_fiscal_receptor":"601",
               "uso_cfdi":"G01"
            },
            "conceptos":[

            ],
            "impuestos":{
               "retenciones":[

               ],
               "traslados":[

               ],
               "total_impuestos_traslados":"-",
               "total_impuestos_retenidos":"-"
            },
            "complementos":"Pagos",
            "addendas":"-"
         },
         "tfd11":[

         ],
         "pagos20":[
            {
               "pago":[
                  {
                     "fecha_pago":"2021-12-02T00:18:10",
                     "forma_de_pago_p":"01",
                     "moneda_p":"USD",
                     "tipo_cambio_p":"-",
                     "monto":"14000.00",
                     "num_operacion":"-",
                     "rfc_emisor_cta_ord":"-",
                     "nom_banco_ord_ext":"-",
                     "cta_ordenante":"-",
                     "rfc_emisor_cta_ben":"-",
                     "cta_beneficiario":"-",
                     "tipo_cad_pago":"-",
                     "cert_pago":"-",
                     "cad_pago":"-",
                     "sello_pago":"-",
                     "docto_relacionado":[
                        {
                           "id_documento":"BEDC8964-7E57-4604-9968-7E01378E8706",
                           "serie":"Serie3",
                           "folio":"Folio3",
                           "moneda_dr":"MXN",
                           "equivalencia_dr":"1.329310",
                           "num_parcialidad":"1",
                           "imp_saldo_ant":"5000.00",
                           "imp_pagado":"2000.00",
                           "imp_saldo_insoluto":"3000.00",
                           "objecto_imp_dr":"02",
                           "impuestos_dr":[
                              {
                                 "retenciones_dr":[
                                    {
                                       "base_dr":"1",
                                       "impuesto_dr":"001",
                                       "tipo_factor_dr":"Tasa",
                                       "tasa_o_cuota_dr":"0.300000",
                                       "importe_dr":"0.300000"
                                    }
                                 ],
                                 "traslados_dr":[
                                    {
                                       "base_dr":"625000.00",
                                       "impuesto_dr":"002",
                                       "tipo_factor_dr":"Tasa",
                                       "tasa_o_cuota_dr":"0.160000",
                                       "importe_dr":"100000.00"
                                    },
                                    {
                                       "base_dr":"22166372.13",
                                       "impuesto_dr":"002",
                                       "tipo_factor_dr":"Tasa",
                                       "tasa_o_cuota_dr":"0.080000",
                                       "importe_dr":"1773309.77"
                                    },
                                    {
                                       "base_dr":"22166372.13",
                                       "impuesto_dr":"002",
                                       "tipo_factor_dr":"Tasa",
                                       "tasa_o_cuota_dr":"0.000000",
                                       "importe_dr":"0"
                                    },
                                    {
                                       "base_dr":"1",
                                       "impuesto_dr":"002",
                                       "tipo_factor_dr":"Exento",
                                       "tasa_o_cuota_dr":"-",
                                       "importe_dr":"-"
                                    }
                                 ]
                              }
                           ]
                        },
                        {
                           "id_documento":"BEDC8964-7E57-4604-9968-7E01378E8706",
                           "serie":"Serie3",
                           "folio":"Folio3",
                           "moneda_dr":"MXN",
                           "equivalencia_dr":"23.5728",
                           "num_parcialidad":"-",
                           "imp_saldo_ant":"5000.00",
                           "imp_pagado":"2000.00",
                           "imp_saldo_insoluto":"3000.00",
                           "objecto_imp_dr":"02",
                           "impuestos_dr":[
                              {
                                 "retenciones_dr":[

                                 ],
                                 "traslados_dr":[
                                    {
                                       "base_dr":"11083186.11",
                                       "impuesto_dr":"002",
                                       "tipo_factor_dr":"Tasa",
                                       "tasa_o_cuota_dr":"0.160000",
                                       "importe_dr":"1773309.77"
                                    },
                                    {
                                       "base_dr":"1250000.00",
                                       "impuesto_dr":"002",
                                       "tipo_factor_dr":"Tasa",
                                       "tasa_o_cuota_dr":"0.080000",
                                       "importe_dr":"100000.00"
                                    },
                                    {
                                       "base_dr":"1",
                                       "impuesto_dr":"002",
                                       "tipo_factor_dr":"Exento",
                                       "tasa_o_cuota_dr":"-",
                                       "importe_dr":"-"
                                    }
                                 ]
                              }
                           ]
                        }
                     ],
                     "impuestos_p":[
                        {
                           "retenciones_p":[
                              {
                                 "impuesto_p":"001",
                                 "importe_p":"2"
                              }
                           ],
                           "traslados_p":[
                              {
                                 "base_p":"940337.15",
                                 "impuesto_p":"002",
                                 "tipo_factor_p":"Tasa",
                                 "tasa_o_cuota_p":"0.160000",
                                 "importe_p":"150453.94"
                              },
                              {
                                 "base_p":"16728123.41",
                                 "impuesto_p":"002",
                                 "tipo_factor_p":"Tasa",
                                 "tasa_o_cuota_p":"0.080000",
                                 "importe_p":"1338249.87"
                              },
                              {
                                 "base_p":"16675096.20",
                                 "impuesto_p":"002",
                                 "tipo_factor_p":"Tasa",
                                 "tasa_o_cuota_p":"0.000000",
                                 "importe_p":"-"
                              },
                              {
                                 "base_p":"0.79",
                                 "impuesto_p":"002",
                                 "tipo_factor_p":"Exento",
                                 "tasa_o_cuota_p":"-",
                                 "importe_p":"-"
                              }
                           ]
                        }
                     ]
                  }
               ],
               "totales":{
                  "total_retenciones_iva":"-",
                  "total_retenciones_isr":"-",
                  "total_retenciones_ieps":"-",
                  "total_traslados_base_iva_16":"-",
                  "total_traslados_impuesto_iva_16":"-",
                  "total_traslados_base_iva_8":"-",
                  "total_traslados_impuesto_iva_8":"-",
                  "total_traslados_base_iva_0":"-",
                  "total_traslados_impuesto_iva_0":"-",
                  "total_traslados_base_iva_exento":"-",
                  "monto_total_pagos":"-"
               },
               "version":"2.0"
            }
         ]
      }
        self.assertDictEqual(cfdi_data, expected_dict)
        
    def test_trasnform_file_pagos20_bad_version(self):
         sax_handler = CFDI40SAXHandler().use_pagos20()
         with self.assertRaises(ValueError) as context:
            sax_handler.transform_from_file("./tests/Resources/pagos20/pago_bad_version.xml")
         exception = context.exception
         self.assertIn('Incorrect type of Pagos, this handler only support Pagos version 2.0', str(exception), 'Not expected error message')
    