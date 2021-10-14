from __future__ import annotations
from pycfdi_transform.formatters.formatter_interface import FormatterInterface
from pycfdi_transform.helpers.string_helper import StringHelper

class EfiscoNomina12Formatter(FormatterInterface):
    def __init__(self, cfdi_data: dict, empty_char:str = '', safe_numerics:bool = False) -> EfiscoNomina12Formatter:
        super().__init__(cfdi_data, empty_char, safe_numerics)
        assert 'cfdi33' in self._cfdi_data, 'Este formatter únicamente soporta datos de cfdi33.'
    
    def __get_nomina_total_by_property(self,property_name):
        total = None
        for nomina12 in self._cfdi_data['nomina12']:
            if nomina12[property_name]:
                total = StringHelper.sum_strings(total, nomina12[property_name])
        return self._get_numeric_value(total)
    
    def __get_total_by_element_and_property(self,element_name:str,property_name:str):
        total = None
        for nomina12 in self._cfdi_data['nomina12']:
            if nomina12[element_name][property_name]:
                total = StringHelper.sum_strings(total, nomina12[element_name][property_name])
        return self._get_numeric_value(total)

    def __get_total_percepciones(self):
        return self.__get_nomina_total_by_property('total_percepciones')
    
    def __get_total_deducciones(self):
        return self.__get_nomina_total_by_property('total_deducciones')
    
    def __get_total_otros_pagos(self):
        return self.__get_nomina_total_by_property('total_otros_pagos')
    
    def __get_percepciones_total_by_property_name(self,property_name):
        return self.__get_total_by_element_and_property('percepciones',property_name)
    
    def __get_deducciones_total_by_property_name(self,property_name):
        return self.__get_total_by_element_and_property('deducciones',property_name)
    
    def _get_part_complement(self) -> list:
        results = []
        for nomina12 in self._cfdi_data['nomina12']:
            row = [
                nomina12['tipo_nomina'],
                nomina12['fecha_pago'],
                nomina12['fecha_inicial_pago'],
                nomina12['fecha_final_pago'],
                nomina12['num_dias_pagados'],
                self.__get_total_percepciones(),
                self.__get_total_deducciones(),
                self.__get_total_otros_pagos(),
                self._get_str_value(nomina12['emisor']['curp']),
                self._get_str_value(nomina12['emisor']['registro_patronal']),
                self._get_str_value(nomina12['emisor']['rfc_patron_origen']),
                nomina12['receptor']['curp'],
                self._get_str_value(nomina12['receptor']['num_seguridad_social']),
                nomina12['receptor']['fecha_inicio_rel_laboral'],
                self._get_str_value(nomina12['receptor']['sindicalizado']),
                self._get_str_value(nomina12['receptor']['tipo_jornada']),
                nomina12['receptor']['tipo_regimen'],
                nomina12['receptor']['num_empleado'],
                self._get_str_value(nomina12['receptor']['departamento']),
                self._get_str_value(nomina12['receptor']['puesto']),
                self._get_str_value(nomina12['receptor']['riesgo_puesto']),
                self._get_str_value(nomina12['receptor']['banco']),
                self._get_str_value(nomina12['receptor']['cuenta_bancaria']),
                self._get_str_value(nomina12['receptor']['antigüedad']),
                nomina12['receptor']['tipo_contrato'],
                nomina12['receptor']['periodicidad_pago'],
                self._get_numeric_value(nomina12['receptor']['salario_base_cot_apor']),
                self._get_numeric_value(nomina12['receptor']['salario_diario_integrado']),
                nomina12['receptor']['clave_ent_fed'],
                self.__get_percepciones_total_by_property_name('total_sueldos'),
                self.__get_percepciones_total_by_property_name('total_separacion_indemnizacion'),
                self.__get_percepciones_total_by_property_name('total_jubilacion_pension_retiro'),
                self.__get_percepciones_total_by_property_name('total_gravado'),
                self.__get_percepciones_total_by_property_name('total_exento'),
                self.__get_deducciones_total_by_property_name('total_otras_deducciones'),
                self.__get_deducciones_total_by_property_name('total_impuestos_retenidos'),
            ]

            if len(nomina12['percepciones']['percepcion']) > 0:
                for percepcion in nomina12['percepciones']['percepcion']:
                    results.append(
                        row + [
                            'P',
                            percepcion['clave'],
                            percepcion['tipo_percepcion'],
                            percepcion['concepto'],
                            percepcion['importe_gravado'],
                            percepcion['importe_exento'],
                        ]
                    )
            if len(nomina12['deducciones']['deduccion']) > 0:
                for deduccion in nomina12['deducciones']['deduccion']:
                    results.append(
                        row + [
                            'D',
                            deduccion['clave'],
                            deduccion['tipo_deduccion'],
                            deduccion['concepto'],
                            deduccion['importe'],
                            '0.00',
                        ]
                    )
            if len(nomina12['otros_pagos']['otro_pago']) > 0:
                for otro_pago in nomina12['otros_pagos']['otro_pago']:
                    results.append(
                        row + [
                            'O',
                            otro_pago['clave'],
                            otro_pago['tipo_otro_pago'],
                            otro_pago['concepto'],
                            '0.00',
                            otro_pago['importe']
                        ]
                    )
        return results
        
    def dict_to_columns(self) -> list[list]:
        results = []
        nomina_list = self._get_part_complement()
        for tdf in self._cfdi_data['tfd11']:
            row = [
                self._cfdi_data['cfdi33']['version'],
                self._get_str_value(self._cfdi_data['cfdi33']['serie']),
                self._get_str_value(self._cfdi_data['cfdi33']['folio']),
                self._cfdi_data['cfdi33']['fecha'],
                self._cfdi_data['cfdi33']['no_certificado'],
                self._cfdi_data['cfdi33']['subtotal'],
                self._get_numeric_value(self._cfdi_data['cfdi33']['descuento']),
                self._cfdi_data['cfdi33']['total'],
                self._cfdi_data['cfdi33']['moneda'],
                self._get_numeric_tipo_cambio_value(self._cfdi_data['cfdi33']['tipo_cambio']),
                self._cfdi_data['cfdi33']['tipo_comprobante'],
                self._get_str_value(self._cfdi_data['cfdi33']['metodo_pago']),
                self._get_str_value(self._cfdi_data['cfdi33']['forma_pago']),
                self._get_str_value(self._cfdi_data['cfdi33']['condiciones_pago']),
                self._cfdi_data['cfdi33']['lugar_expedicion'],
                self._cfdi_data['cfdi33']['emisor']['rfc'],
                self._get_str_value(self._cfdi_data['cfdi33']['emisor']['nombre']),
                self._cfdi_data['cfdi33']['emisor']['regimen_fiscal'],
                self._cfdi_data['cfdi33']['receptor']['rfc'],
                self._get_str_value(self._cfdi_data['cfdi33']['receptor']['nombre']),
                self._cfdi_data['cfdi33']['receptor']['uso_cfdi'],
                tdf['uuid'],
                tdf['fecha_timbrado'],
                tdf['rfc_prov_cert'],
                tdf['sello_cfd']
            ]
            for nomina_row in nomina_list:
                results.append(row + nomina_row)
        return results
    
    def can_format(self) -> bool:
        if not 'nomina12' in self._cfdi_data or len(self._cfdi_data['nomina12']) == 0:
            self._errors.append('Not nomina12 in data.')
        elif not 'tfd11' in self._cfdi_data or len(self._cfdi_data['tfd11']) == 0:
            self._errors.append('Not tfd11 in data.')
        return len(self._errors) == 0
    
    def get_errors(self) -> str:
        return '|'.join(self._errors)
    
    @staticmethod
    def get_columns_names() -> list[str]:
        return [
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