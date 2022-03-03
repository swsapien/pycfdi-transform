from __future__ import annotations
from pycfdi_transform.formatters.formatter_interface import FormatterInterface
from pycfdi_transform.helpers.string_helper import StringHelper


class EfiscoNomina11Formatter(FormatterInterface):
    def __init__(self, cfdi_data: dict, empty_char: str = '', safe_numerics: bool = False) -> EfiscoNomina11Formatter:
        super().__init__(cfdi_data, empty_char, safe_numerics)
        assert 'cfdi32' in self._cfdi_data, 'Este formatter únicamente soporta datos de cfdi32.'

    def __get_nomina_total_by_property(self, property_name):
        total = None
        for nomina11 in self._cfdi_data['nomina11']:
            if nomina11[property_name]:
                total = StringHelper.sum_strings(total, nomina11[property_name])
        return self._get_numeric_value(total)

    def __get_total_by_element_and_property(self, element_name: str, property_name: str):
        total = None
        for nomina11 in self._cfdi_data['nomina11']:
            if nomina11[element_name][property_name]:
                total = StringHelper.sum_strings(total, nomina11[element_name][property_name])
        return self._get_numeric_value(total)

    def __get_total_percepciones(self):
        return self.__get_nomina_total_by_property('total_percepciones')

    def __get_total_deducciones(self):
        return self.__get_nomina_total_by_property('total_deducciones')

    def __get_total_otros_pagos(self):
        return self.__get_nomina_total_by_property('total_otros_pagos')

    def __get_percepciones_total_by_property_name(self, property_name):
        return self.__get_total_by_element_and_property('percepciones', property_name)

    def __get_deducciones_total_by_property_name(self, property_name):
        return self.__get_total_by_element_and_property('deducciones', property_name)

    def _get_part_complement(self) -> list:
        results = []
        for nomina11 in self._cfdi_data['nomina11']:
            row = [
                "",  # tipoNomina
                nomina11['fecha_pago'],
                nomina11['fecha_inicial_pago'],
                nomina11['fecha_final_pago'],
                nomina11['num_dias_pagados'],
                "",  # TOTAL PERCEPCIONES
                "",  # TOTAL DEDUCCIONES
                "",  # OTROS_PAGOS
                "",  # EMISOR CURP
                self._get_str_value(nomina11['registro_patronal']),
                "",  # RFC_PATRON_ORIGEN
                nomina11['curp'],
                self._get_str_value(nomina11['num_seguridad_social']),
                nomina11['fecha_inicio_rel_laboral'],
                "",  # sindicalizado
                self._get_str_value(nomina11['tipo_jornada']),
                nomina11['tipo_regimen'],
                nomina11['num_empleado'],
                self._get_str_value(nomina11['departamento']),
                self._get_str_value(nomina11['puesto']),
                self._get_str_value(nomina11['riesgo_puesto']),
                self._get_str_value(nomina11['banco']),
                self._get_str_value(nomina11['clabe']),  # cuenta_bancaria
                self._get_str_value(nomina11['antiguedad']),
                nomina11['tipo_contrato'],
                nomina11['periodicidad_pago'],
                self._get_numeric_value(nomina11['salario_base_cot_apor']),
                self._get_numeric_value(nomina11['salario_diario_integrado']),
                "",  # RECEPTOR CLAVEENTFED
                "",  # TOTALSUELDOS
                "",  # TOTALSEPARACIONINDEM
                "",  # TOTALJUBILACION
                self.__get_percepciones_total_by_property_name('total_gravado'),
                self.__get_percepciones_total_by_property_name('total_exento'),
                "",  # TOTALOTRASDEDUCC
                "",  # TOTALIMPRET
            ]

            if len(nomina11['percepciones']['percepcion']) > 0:
                for percepcion in nomina11['percepciones']['percepcion']:
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
            if len(nomina11['deducciones']['deduccion']) > 0:
                for deduccion in nomina11['deducciones']['deduccion']:
                    results.append(
                        row + [
                            'D',
                            deduccion['clave'],
                            deduccion['tipo_deduccion'],
                            deduccion['concepto'],
                            deduccion['importe_gravado'],
                            '0.00',
                        ]
                    )

        return results

    def dict_to_columns(self) -> list[list]:
        results = []
        nomina_list = self._get_part_complement()
        for tfd in self._cfdi_data['tfd10']:
            row = [
                self._cfdi_data['cfdi32']['version'],
                self._get_str_value(self._cfdi_data['cfdi32']['serie']),
                self._get_str_value(self._cfdi_data['cfdi32']['folio']),
                self._cfdi_data['cfdi32']['fecha'],
                self._cfdi_data['cfdi32']['no_certificado'],
                self._cfdi_data['cfdi32']['subtotal'],
                self._get_numeric_value(self._cfdi_data['cfdi32']['descuento']),
                self._cfdi_data['cfdi32']['total'],
                self._cfdi_data['cfdi32']['moneda'],
                self._get_numeric_tipo_cambio_value(self._cfdi_data['cfdi32']['tipo_cambio']),
                self._cfdi_data['cfdi32']['tipo_comprobante'],
                self._get_str_value(self._cfdi_data['cfdi32']['metodo_pago']),
                self._get_str_value(self._cfdi_data['cfdi32']['forma_pago']),
                self._get_str_value(self._cfdi_data['cfdi32']['condiciones_pago']),
                self._cfdi_data['cfdi32']['lugar_expedicion'],
                self._cfdi_data['cfdi32']['emisor']['rfc'],
                self._get_str_value(self._cfdi_data['cfdi32']['emisor']['nombre']),
                self._get_str_value(self._cfdi_data['cfdi32']['emisor']['regimen_fiscal'][0]),
                self._cfdi_data['cfdi32']['receptor']['rfc'],
                self._cfdi_data['cfdi32']['receptor']['nombre'],
                "",  # USOCFDI
                tfd['uuid'],
                tfd['fecha_timbrado'],
                "",  # RFCPROVECERT
                tfd['sello_cfd']
            ]
            for nomina_row in nomina_list:
                results.append(row + nomina_row)
        return results

    def can_format(self) -> bool:
        if not 'nomina11' in self._cfdi_data or len(self._cfdi_data['nomina11']) == 0:
            self._errors.append('Not nomina11 in data.')
        elif not 'tfd10' in self._cfdi_data or len(self._cfdi_data['tfd10']) == 0:
            self._errors.append('Not tfd10 in data.')
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
            "IMPORTEEXENTO",
        ]
