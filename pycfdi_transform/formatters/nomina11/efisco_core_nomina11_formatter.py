from __future__ import annotations
from pycfdi_transform.formatters.catalogs import catalogs
from pycfdi_transform.formatters.formatter_interface import FormatterInterface
from pycfdi_transform.helpers.string_helper import StringHelper

def _get_total_in_list(elements, attribute_name):
    return str(sum(StringHelper.try_parse_decimal(item[attribute_name]) for item in elements))

class EfiscoCoreNomina11Formatter(FormatterInterface):
    def __init__(self, cfdi_data: dict, empty_char: str = '', safe_numerics: bool = False) -> EfiscoCoreNomina11Formatter:
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

    def _get_part_complement(self) -> list:
        results = []
        for nomina11 in self._cfdi_data['nomina11']:
            row = [
                self._config['empty_char'], # TIPO NOMINA
                nomina11['fecha_pago'],
                nomina11['fecha_inicial_pago'],
                nomina11['fecha_final_pago'],
                nomina11['num_dias_pagados'],
                StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],  # TOTAL PERCEPCIONES
                StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],  # TOTAL DEDUCCIONES
                StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],  # OTROS_PAGOS
                StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],  # EMISOR CURP
                self._get_str_value(nomina11['registro_patronal']),
                self._config['empty_char'],  # RFC_PATRON_ORIGEN
                nomina11['curp'],
                self._get_str_value(nomina11['num_seguridad_social']),
                nomina11['fecha_inicio_rel_laboral'],
                self._config['empty_char'],  # SINDICALIZADO
                self._get_str_value(nomina11['tipo_jornada']),
                nomina11['tipo_regimen'],
                nomina11['num_empleado'],
                self._get_str_value(nomina11['departamento']),
                self._get_str_value(nomina11['puesto']),
                self._get_str_value(nomina11['riesgo_puesto']),
                self._get_str_value(nomina11['banco']),
                self._get_str_value(nomina11['clabe']),  # CUENTA BANCARIA
                self._get_str_value(nomina11['antiguedad']),
                nomina11['tipo_contrato'],
                nomina11['periodicidad_pago'],
                self._get_numeric_value(nomina11['salario_base_cot_apor']),
                self._get_numeric_value(nomina11['salario_diario_integrado']),
                self._config['empty_char'],  # RECEPTOR CLAVEENTFED
                StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],  # TOTALSUELDOS
                StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],  # TOTALSEPARACIONINDEM
                StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'],  # TOTALJUBILACION
                self.__get_total_by_element_and_property('percepciones', 'total_gravado'),
                self.__get_total_by_element_and_property('percepciones', 'total_exento')
            ]

            self._set_percepciones(nomina11, row)
            self._set_deducciones(nomina11, row)
            self._set_otros_pagos(row)

            results.append(row)

        return results

    def _set_otros_pagos(self, row):
        for tipo_otro_pago in catalogs.OTROS_PAGOS:
            row.extend(
                [self._config['empty_char'], self._config['empty_char']])  # nodo otros_pagos no existe en nomina 11

            if tipo_otro_pago == '002':
                row.extend([self._config['empty_char']])  # nodo subsidio al empleo no existe en nomina11
            elif tipo_otro_pago == '004':
                row.extend([self._config['empty_char'], self._config['empty_char'],
                            self._config['empty_char']])  # nodo compensasiones saldo a favor no existe en nomina11

    def _set_deducciones(self, nomina11, row):
        incapacidad = self._get_incapacidad(nomina11)
        row.append(self.__get_total_by_element_and_property('deducciones', 'total_gravado'))  # TOTAL OTRAS DEDUCCIONES
        row.append(self.__get_total_by_element_and_property('deducciones', 'total_exento'))  # TOTAL IMPUESTOS RETENIDOS
        for tipo_deduccion in catalogs.DEDUCCIONES:
            deducciones = [deduccion for deduccion in nomina11['deducciones']['deduccion'] if
                           deduccion['tipo_deduccion'] == tipo_deduccion]
            if len(deducciones) > 0:
                row.extend([tipo_deduccion,  str(sum(StringHelper.try_parse_decimal(item['importe_gravado']) + StringHelper.try_parse_decimal(item['importe_exento']) for item in deducciones))])
            else:
                row.extend([self._config['empty_char'], self._config['empty_char']])

            if tipo_deduccion == '006':
                row.extend(incapacidad)

    def _set_percepciones(self, nomina11, row):
        horas_extra = self._get_horas_extra(nomina11)
        for tipo_percepcion in catalogs.PERCEPCIONES:
            percepciones = [percepcion for percepcion in nomina11['percepciones']['percepcion'] if
                            percepcion['tipo_percepcion'] == tipo_percepcion]
            if len(percepciones) > 0:
                row.extend([tipo_percepcion,
                            _get_total_in_list(percepciones, 'importe_exento'),
                            _get_total_in_list(percepciones, 'importe_gravado')])
            else:
                row.extend([self._config['empty_char'], self._config['empty_char'], self._config['empty_char']])

            if tipo_percepcion == '019':
                row.extend(horas_extra)
            elif tipo_percepcion == '039':
                row.extend([self._config['empty_char'], self._config['empty_char'], self._config['empty_char'],
                            self._config['empty_char'],
                            self._config['empty_char']])  # nodo jubilacion_pension_retiro no existe en nomina11
            elif tipo_percepcion == '044':
                row.extend([self._config['empty_char'], self._config['empty_char'], self._config['empty_char'],
                            self._config['empty_char'],
                            self._config['empty_char']])  # nodo jubilacion_pension_retiro no existe en nomina11

    def _get_incapacidad(self, nomina11):
        if len(nomina11['incapacidades']['incapacidad']) > 0:
            item = nomina11['incapacidades']['incapacidad'][-1]
            return [item['descuento'], item['tipo_incapacidad'], item['dias_incapacidad']]
        else:
            return [self._config['empty_char'], self._config['empty_char'], self._config['empty_char']]

    def _get_horas_extra(self, nomina11):
        if len(nomina11['horas_extras']['horas_extra']) > 0:
            item = nomina11['horas_extras']['horas_extra'][-1]
            return [item['dias'], item['tipo_horas'], item['horas_extra'], item['importe_pagado']]
        else:
            return [self._config['empty_char'], self._config['empty_char'], self._config['empty_char'], self._config['empty_char']]

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
                self._config['empty_char'],  # USOCFDI
                tfd['uuid'],
                tfd['fecha_timbrado'],
                self._config['empty_char'],  # RFCPROVECERT
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

    def get_columns_names(self) -> list[str]:
        return [
            'VERSION',
            'SERIE',
            'FOLIO',
            'FECHA',
            'NOCERTIFICADO',
            'SUBTOTAL',
            'DESCUENTO',
            'TOTAL',
            'MONEDA',
            'TIPOCAMBIO',
            'TIPODECOMPROBANTE',
            'METODOPAGO',
            'FORMAPAGO',
            'CONDICIONESDEPAGO',
            'LUGAREXPEDICION',
            'EMISORRFC',
            'EMISORNOMBRE',
            'EMISORREGIMENFISCAL',
            'RECEPTORRFC',
            'RECEPTORNOMBRE',
            'RECEPTORUSOCFDI',
            'UUID',
            'FECHATIMBRADO',
            'RFCPROVCERTIF',
            'SELLOCFD',
            'TIPONOMINA',
            'FECHAPAGO',
            'FECHAINICIALPAGO',
            'FECHAFINALPAGO',
            'NUMDIASPAGADOS',
            'TOTALPERCEPCIONES',
            'TOTALDEDUCCIONES',
            'TOTALOTROSPAGOS',
            'CURPEMISOR',
            'REGISTROPATRONAL',
            'RFCPATRONORIGEN',
            'CURPRECEPTOR',
            'NUMSEGURIDADSOCIAL',
            'FECHAINICIORELLABORAL',
            'SINDICALIZADO',
            'TIPOJORNADA',
            'TIPOREGIMEN',
            'NUMEMPLEADO',
            'DEPARTAMENTO',
            'PUESTO',
            'RIESGOPUESTO',
            'BANCO',
            'CUENTABANCARIA',
            'ANTIGÜEDAD',
            'TIPOCONTRATO',
            'PERIODICIDADPAGO',
            'SALARIOBASECOTAPOR',
            'SALARIODIARIOINTEGRADO',
            'CLAVEENTFED',
            'TOTALSUELDOS',
            'TOTALSEPARACIONINDEMNIZACION',
            'TOTALJUBILACIONPENSIONRETIRO',
            'TOTALGRAVADO',
            'TOTALEXENTO',
            'P_001_SUELDOSSALARIOSRAYASYJORNALES',
            'P_001_IMPORTEEXCENTO',
            'P_001_IMPORTEGRAVADO',
            'P_002_GRATIFICACIÓNANUAL(AGUINALDO)',
            'P_002_IMPORTEEXCENTO',
            'P_002_IMPORTEGRAVADO',
            'P_003_PARTICIPACIÓNDELOSTRABAJADORESENLASUTILIDADESPTU',
            'P_003_IMPORTEEXCENTO',
            'P_003_IMPORTEGRAVADO',
            'P_004_REEMBOLSODEGASTOSMÉDICOSDENTALESYHOSPITALARIOS',
            'P_004_IMPORTEEXCENTO',
            'P_004_IMPORTEGRAVADO',
            'P_005_FONDODEAHORRO',
            'P_005_IMPORTEEXCENTO',
            'P_005_IMPORTEGRAVADO',
            'P_006_CAJADEAHORRO',
            'P_006_IMPORTEEXCENTO',
            'P_006_IMPORTEGRAVADO',
            'P_009_CONTRIBUCIONESACARGODELTRABAJADORPAGADASPORELPATRÓN',
            'P_009_IMPORTEEXCENTO',
            'P_009_IMPORTEGRAVADO',
            'P_010_PREMIOSPORPUNTUALIDAD',
            'P_010_IMPORTEEXCENTO',
            'P_010_IMPORTEGRAVADO',
            'P_011_PRIMADESEGURODEVIDA',
            'P_011_IMPORTEEXCENTO',
            'P_011_IMPORTEGRAVADO',
            'P_012_SEGURODEGASTOSMÉDICOSMAYORES',
            'P_012_IMPORTEEXCENTO',
            'P_012_IMPORTEGRAVADO',
            'P_013_CUOTASSINDICALESPAGADASPORELPATRÓN',
            'P_013_IMPORTEEXCENTO',
            'P_013_IMPORTEGRAVADO',
            'P_014_SUBSIDIOSPORINCAPACIDAD',
            'P_014_IMPORTEEXCENTO',
            'P_014_IMPORTEGRAVADO',
            'P_015_BECASPARATRABAJADORESY/OHIJOS',
            'P_015_IMPORTEEXCENTO',
            'P_015_IMPORTEGRAVADO',
            'P_019_HORASEXTRA',
            'P_019_IMPORTEEXCENTO',
            'P_019_IMPORTEGRAVADO',
            'P_019_DIAS',
            'P_019_TIPO_HORAS',
            'P_019_HORAS_EXTRA',
            'P_019_IMPORTE_HORAS_EXTRA',
            'P_020_PRIMADOMINICAL',
            'P_020_IMPORTEEXCENTO',
            'P_020_IMPORTEGRAVADO',
            'P_021_PRIMAVACACIONAL',
            'P_021_IMPORTEEXCENTO',
            'P_021_IMPORTEGRAVADO',
            'P_022_PRIMAPORANTIGÜEDAD',
            'P_022_IMPORTEEXCENTO',
            'P_022_IMPORTEGRAVADO',
            'P_023_PAGOSPORSEPARACIÓN',
            'P_023_IMPORTEEXCENTO',
            'P_023_IMPORTEGRAVADO',
            'P_024_SEGURODERETIRO',
            'P_024_IMPORTEEXCENTO',
            'P_024_IMPORTEGRAVADO',
            'P_025_INDEMNIZACIONES',
            'P_025_IMPORTEEXCENTO',
            'P_025_IMPORTEGRAVADO',
            'P_026_REEMBOLSOPORFUNERAL',
            'P_026_IMPORTEEXCENTO',
            'P_026_IMPORTEGRAVADO',
            'P_027_CUOTASDESEGURIDADSOCIALPAGADASPORELPATRÓN',
            'P_027_IMPORTEEXCENTO',
            'P_027_IMPORTEGRAVADO',
            'P_028_COMISIONES',
            'P_028_IMPORTEEXCENTO',
            'P_028_IMPORTEGRAVADO',
            'P_029_VALESDEDESPENSA',
            'P_029_IMPORTEEXCENTO',
            'P_029_IMPORTEGRAVADO',
            'P_030_VALESDERESTAURANTE',
            'P_030_IMPORTEEXCENTO',
            'P_030_IMPORTEGRAVADO',
            'P_031_VALESDEGASOLINA',
            'P_031_IMPORTEEXCENTO',
            'P_031_IMPORTEGRAVADO',
            'P_032_VALESDEROPA',
            'P_032_IMPORTEEXCENTO',
            'P_032_IMPORTEGRAVADO',
            'P_033_AYUDAPARARENTA',
            'P_033_IMPORTEEXCENTO',
            'P_033_IMPORTEGRAVADO',
            'P_034_AYUDAPARAARTÍCULOSESCOLARES',
            'P_034_IMPORTEEXCENTO',
            'P_034_IMPORTEGRAVADO',
            'P_035_AYUDAPARAANTEOJOS',
            'P_035_IMPORTEEXCENTO',
            'P_035_IMPORTEGRAVADO',
            'P_036_AYUDAPARATRANSPORTE',
            'P_036_IMPORTEEXCENTO',
            'P_036_IMPORTEGRAVADO',
            'P_037_AYUDAPARAGASTOSDEFUNERAL',
            'P_037_IMPORTEEXCENTO',
            'P_037_IMPORTEGRAVADO',
            'P_038_OTROSINGRESOSPORSALARIOS',
            'P_038_IMPORTEEXCENTO',
            'P_038_IMPORTEGRAVADO',
            'P_039_JUBILACIONESPENSIONESOHABERESDERETIRO',
            'P_039_IMPORTEEXCENTO',
            'P_039_IMPORTEGRAVADO',
            'P_039_INGRESONOACUMULABLE',
            'P_039_INGRESOACUMULABLE',
            'P_039_TOTALUNAEXHIBICION',
            'P_039_MONTODIARIO',
            'P_039_TOTALPARCIALIDAD',
            'P_044_JUBILACIONESPENSIONESOHABERESDERETIROENPARCIALIDADES',
            'P_044_IMPORTEEXCENTO',
            'P_044_IMPORTEGRAVADO',
            'P_044_INGRESONOACUMULABLE',
            'P_044_INGRESOACUMULABLE',
            'P_044_TOTALUNAEXHIBICION',
            'P_044_MONTODIARIO',
            'P_044_TOTALPARCIALIDAD',
            'P_045_INGRESOSENACCIONESOTÍTULOSVALORQUEREPRESENTANBIENES',
            'P_045_IMPORTEEXCENTO',
            'P_045_IMPORTEGRAVADO',
            'P_046_INGRESOSASIMILADOSASALARIOS',
            'P_046_IMPORTEEXCENTO',
            'P_046_IMPORTEGRAVADO',
            'P_047_ALIMENTACIÓN',
            'P_047_IMPORTEEXCENTO',
            'P_047_IMPORTEGRAVADO',
            'P_048_HABITACIÓN',
            'P_048_IMPORTEEXCENTO',
            'P_048_IMPORTEGRAVADO',
            'P_049_PREMIOSPORASISTENCIA',
            'P_049_IMPORTEEXCENTO',
            'P_049_IMPORTEGRAVADO',
            'P_050_VIÁTICOS',
            'P_050_IMPORTEEXCENTO',
            'P_050_IMPORTEGRAVADO',
            'P_051_PAGOSPORGRATIFICACIONESPRIMASCOMPENSACIONESRECOMPENSASUOTROSAEXTRABAJADORESDERIVADOSDEJUBILACIÓNENPARCIALIDADES',
            'P_051_IMPORTEEXCENTO',
            'P_051_IMPORTEGRAVADO',
            'P_052_PAGOSQUESEREALICENAEXTRABAJADORESQUEOBTENGANUNAJUBILACIÓNENPARCIALIDADESDERIVADOSDELAEJECUCIÓNDERESOLUCIONESJUDICIALODEUNLAUDO',
            'P_052_IMPORTEEXCENTO',
            'P_052_IMPORTEGRAVADO',
            'P_053_PAGOSQUESEREALICENAEXTRABAJADORESQUEOBTENGANUNAJUBILACIÓNENUNASOLAEXHIBICIÓNDERIVADOSDELAEJECUCIÓNDERESOLUCIONESJUDICIALODEUNLAUDO',
            'P_053_IMPORTEEXCENTO',
            'P_053_IMPORTEGRAVADO',
            'TOTALOTRASDEDUCCIONES',
            'TOTALIMPUESTOSRETENIDOSN',
            'D_001_SEGURIDADSOCIAL',
            'D_001_IMPORTE',
            'D_002_ISR',
            'D_002_IMPORTE',
            'D_003_APORTACIONESARETIROCESANTÍAENEDADAVANZADAYVEJEZ',
            'D_003_IMPORTE',
            'D_004_OTROS',
            'D_004_IMPORTE',
            'D_005_APORTACIONESAFONDODEVIVIENDA',
            'D_005_IMPORTE',
            'D_006_DESCUENTOPORINCAPACIDAD',
            'D_006_IMPORTE',
            'D_006_IMPORTEMONETARIO',
            'D_006_TIPOINCAPACIDAD',
            'D_006_DIASINCAPACIDAD',
            'D_007_PENSIÓNALIMENTICIA',
            'D_007_IMPORTE',
            'D_008_RENTA',
            'D_008_IMPORTE',
            'D_009_PRÉSTAMOSPROVENIENTESDELFONDONACIONALDELAVIVIENDAPARALOSTRABAJADORES',
            'D_009_IMPORTE',
            'D_010_PAGOPORCRÉDITODEVIVIENDA',
            'D_010_IMPORTE',
            'D_011_PAGODEABONOSINFONACOT',
            'D_011_IMPORTE',
            'D_012_ANTICIPODESALARIOS',
            'D_012_IMPORTE',
            'D_013_PAGOSHECHOSCONEXCESOALTRABAJADOR',
            'D_013_IMPORTE',
            'D_014_ERRORES',
            'D_014_IMPORTE',
            'D_015_PÉRDIDAS',
            'D_015_IMPORTE',
            'D_016_AVERÍAS',
            'D_016_IMPORTE',
            'D_017_ADQUISICIÓNDEARTÍCULOSPRODUCIDOSPORLAEMPRESAOESTABLECIMIENTO',
            'D_017_IMPORTE',
            'D_018_CUOTASPARALACONSTITUCIÓNYFOMENTODESOCIEDADESCOOPERATIVASYDECAJASDEAHORRO',
            'D_018_IMPORTE',
            'D_019_CUOTASSINDICALES',
            'D_019_IMPORTE',
            'D_020_AUSENCIA(AUSENTISMO)',
            'D_020_IMPORTE',
            'D_021_CUOTASOBREROPATRONALES',
            'D_021_IMPORTE',
            'D_022_IMPUESTOSLOCALES',
            'D_022_IMPORTE',
            'D_023_APORTACIONESVOLUNTARIAS',
            'D_023_IMPORTE',
            'D_024_AJUSTEENGRATIFICACIÓNANUAL(AGUINALDO)EXENTO',
            'D_024_IMPORTE',
            'D_025_AJUSTEENGRATIFICACIÓNANUAL(AGUINALDO)GRAVADO',
            'D_025_IMPORTE',
            'D_026_AJUSTEENPARTICIPACIÓNDELOSTRABAJADORESENLASUTILIDADESPTUEXENTO',
            'D_026_IMPORTE',
            'D_027_AJUSTEENPARTICIPACIÓNDELOSTRABAJADORESENLASUTILIDADESPTUGRAVADO',
            'D_027_IMPORTE',
            'D_028_AJUSTEENREEMBOLSODEGASTOSMÉDICOSDENTALESYHOSPITALARIOSEXENTO',
            'D_028_IMPORTE',
            'D_029_AJUSTEENFONDODEAHORROEXENTO',
            'D_029_IMPORTE',
            'D_030_AJUSTEENCAJADEAHORROEXENTO',
            'D_030_IMPORTE',
            'D_031_AJUSTEENCONTRIBUCIONESACARGODELTRABAJADORPAGADASPORELPATRÓNEXENTO',
            'D_031_IMPORTE',
            'D_032_AJUSTEENPREMIOSPORPUNTUALIDADGRAVADO',
            'D_032_IMPORTE',
            'D_033_AJUSTEENPRIMADESEGURODEVIDAEXENTO',
            'D_033_IMPORTE',
            'D_034_AJUSTEENSEGURODEGASTOSMÉDICOSMAYORESEXENTO',
            'D_034_IMPORTE',
            'D_035_AJUSTEENCUOTASSINDICALESPAGADASPORELPATRÓNEXENTO',
            'D_035_IMPORTE',
            'D_036_AJUSTEENSUBSIDIOSPORINCAPACIDADEXENTO',
            'D_036_IMPORTE',
            'D_037_AJUSTEENBECASPARATRABAJADORESY/OHIJOSEXENTO',
            'D_037_IMPORTE',
            'D_038_AJUSTEENHORASEXTRAEXENTO',
            'D_038_IMPORTE',
            'D_039_AJUSTEENHORASEXTRAGRAVADO',
            'D_039_IMPORTE',
            'D_040_AJUSTEENPRIMADOMINICALEXENTO',
            'D_040_IMPORTE',
            'D_041_AJUSTEENPRIMADOMINICALGRAVADO',
            'D_041_IMPORTE',
            'D_042_AJUSTEENPRIMAVACACIONALEXENTO',
            'D_042_IMPORTE',
            'D_043_AJUSTEENPRIMAVACACIONALGRAVADO',
            'D_043_IMPORTE',
            'D_044_AJUSTEENPRIMAPORANTIGÜEDADEXENTO',
            'D_044_IMPORTE',
            'D_045_AJUSTEENPRIMAPORANTIGÜEDADGRAVADO',
            'D_045_IMPORTE',
            'D_046_AJUSTEENPAGOSPORSEPARACIÓNEXENTO',
            'D_046_IMPORTE',
            'D_047_AJUSTEENPAGOSPORSEPARACIÓNGRAVADO',
            'D_047_IMPORTE',
            'D_048_AJUSTEENSEGURODERETIROEXENTO',
            'D_048_IMPORTE',
            'D_049_AJUSTEENINDEMNIZACIONESEXENTO',
            'D_049_IMPORTE',
            'D_050_AJUSTEENINDEMNIZACIONESGRAVADO',
            'D_050_IMPORTE',
            'D_051_AJUSTEENREEMBOLSOPORFUNERALEXENTO',
            'D_051_IMPORTE',
            'D_052_AJUSTEENCUOTASDESEGURIDADSOCIALPAGADASPORELPATRÓNEXENTO',
            'D_052_IMPORTE',
            'D_053_AJUSTEENCOMISIONESGRAVADO',
            'D_053_IMPORTE',
            'D_054_AJUSTEENVALESDEDESPENSAEXENTO',
            'D_054_IMPORTE',
            'D_055_AJUSTEENVALESDERESTAURANTEEXENTO',
            'D_055_IMPORTE',
            'D_056_AJUSTEENVALESDEGASOLINAEXENTO',
            'D_056_IMPORTE',
            'D_057_AJUSTEENVALESDEROPAEXENTO',
            'D_057_IMPORTE',
            'D_058_AJUSTEENAYUDAPARARENTAEXENTO',
            'D_058_IMPORTE',
            'D_059_AJUSTEENAYUDAPARAARTÍCULOSESCOLARESEXENTO',
            'D_059_IMPORTE',
            'D_060_AJUSTEENAYUDAPARAANTEOJOSEXENTO',
            'D_060_IMPORTE',
            'D_061_AJUSTEENAYUDAPARATRANSPORTEEXENTO',
            'D_061_IMPORTE',
            'D_062_AJUSTEENAYUDAPARAGASTOSDEFUNERALEXENTO',
            'D_062_IMPORTE',
            'D_063_AJUSTEENOTROSINGRESOSPORSALARIOSEXENTO',
            'D_063_IMPORTE',
            'D_064_AJUSTEENOTROSINGRESOSPORSALARIOSGRAVADO',
            'D_064_IMPORTE',
            'D_065_AJUSTEENJUBILACIONESPENSIONESOHABERESDERETIROENUNASOLAEXHIBICIÓNEXENTO',
            'D_065_IMPORTE',
            'D_066_AJUSTEENJUBILACIONESPENSIONESOHABERESDERETIROENUNASOLAEXHIBICIÓNGRAVADO',
            'D_066_IMPORTE',
            'D_067_AJUSTEENPAGOSPORSEPARACIÓNACUMULABLE',
            'D_067_IMPORTE',
            'D_068_AJUSTEENPAGOSPORSEPARACIÓNNOACUMULABLE',
            'D_068_IMPORTE',
            'D_069_AJUSTEENJUBILACIONESPENSIONESOHABERESDERETIROENPARCIALIDADESEXENTO',
            'D_069_IMPORTE',
            'D_070_AJUSTEENJUBILACIONESPENSIONESOHABERESDERETIROENPARCIALIDADESGRAVADO',
            'D_070_IMPORTE',
            'D_071_AJUSTEENSUBSIDIOPARAELEMPLEO(EFECTIVAMENTEENTREGADOALTRABAJADOR)',
            'D_071_IMPORTE',
            'D_072_AJUSTEENINGRESOSENACCIONESOTÍTULOSVALORQUEREPRESENTANBIENESEXENTO',
            'D_072_IMPORTE',
            'D_073_AJUSTEENINGRESOSENACCIONESOTÍTULOSVALORQUEREPRESENTANBIENESGRAVADO',
            'D_073_IMPORTE',
            'D_074_AJUSTEENALIMENTACIÓNEXENTO',
            'D_074_IMPORTE',
            'D_075_AJUSTEENALIMENTACIÓNGRAVADO',
            'D_075_IMPORTE',
            'D_076_AJUSTEENHABITACIÓNEXENTO',
            'D_076_IMPORTE',
            'D_077_AJUSTEENHABITACIÓNGRAVADO',
            'D_077_IMPORTE',
            'D_078_AJUSTEENPREMIOSPORASISTENCIA',
            'D_078_IMPORTE',
            'D_079_AJUSTEENPAGOSDISTINTOSALOSLISTADOSYQUENODEBENCONSIDERARSECOMOINGRESOPORSUELDOSSALARIOSOINGRESOSASIMILADOS.',
            'D_079_IMPORTE',
            'D_080_AJUSTEENVIÁTICOSGRAVADOS',
            'D_080_IMPORTE',
            'D_081_AJUSTEENVIÁTICOS(ENTREGADOSALTRABAJADOR)',
            'D_081_IMPORTE',
            'D_082_AJUSTEENFONDODEAHORROGRAVADO',
            'D_082_IMPORTE',
            'D_083_AJUSTEENCAJADEAHORROGRAVADO',
            'D_083_IMPORTE',
            'D_084_AJUSTEENPRIMADESEGURODEVIDAGRAVADO',
            'D_084_IMPORTE',
            'D_085_AJUSTEENSEGURODEGASTOSMÉDICOSMAYORESGRAVADO',
            'D_085_IMPORTE',
            'D_086_AJUSTEENSUBSIDIOSPORINCAPACIDADGRAVADO',
            'D_086_IMPORTE',
            'D_087_AJUSTEENBECASPARATRABAJADORESY/OHIJOSGRAVADO',
            'D_087_IMPORTE',
            'D_088_AJUSTEENSEGURODERETIROGRAVADO',
            'D_088_IMPORTE',
            'D_089_AJUSTEENVALESDEDESPENSAGRAVADO',
            'D_089_IMPORTE',
            'D_090_AJUSTEENVALESDERESTAURANTEGRAVADO',
            'D_090_IMPORTE',
            'D_091_AJUSTEENVALESDEGASOLINAGRAVADO',
            'D_091_IMPORTE',
            'D_092_AJUSTEENVALESDEROPAGRAVADO',
            'D_092_IMPORTE',
            'D_093_AJUSTEENAYUDAPARARENTAGRAVADO',
            'D_093_IMPORTE',
            'D_094_AJUSTEENAYUDAPARAARTÍCULOSESCOLARESGRAVADO',
            'D_094_IMPORTE',
            'D_095_AJUSTEENAYUDAPARAANTEOJOSGRAVADO',
            'D_095_IMPORTE',
            'D_096_AJUSTEENAYUDAPARATRANSPORTEGRAVADO',
            'D_096_IMPORTE',
            'D_097_AJUSTEENAYUDAPARAGASTOSDEFUNERALGRAVADO',
            'D_097_IMPORTE',
            'D_098_AJUSTEAINGRESOSASIMILADOSASALARIOSGRAVADOS',
            'D_098_IMPORTE',
            'D_099_AJUSTEAINGRESOSPORSUELDOSYSALARIOSGRAVADOS',
            'D_099_IMPORTE',
            'D_100_AJUSTEENVIÁTICOSEXENTOS',
            'D_100_IMPORTE',
            'D_101_ISRRETENIDODEEJERCICIOANTERIOR',
            'D_101_IMPORTE',
            'D_102_AJUSTEAPAGOSPORGRATIFICACIONESPRIMASCOMPENSACIONESRECOMPENSASUOTROSAEXTRABAJADORESDERIVADOSDEJUBILACIÓNENPARCIALIDADESGRAVADOS',
            'D_102_IMPORTE',
            'D_103_AJUSTEAPAGOSQUESEREALICENAEXTRABAJADORESQUEOBTENGANUNAJUBILACIÓNENPARCIALIDADESDERIVADOSDELAEJECUCIÓNDEUNARESOLUCIÓNJUDICIALODEUNLAUDOGRAVADOS',
            'D_103_IMPORTE',
            'D_104_AJUSTEAPAGOSQUESEREALICENAEXTRABAJADORESQUEOBTENGANUNAJUBILACIÓNENPARCIALIDADESDERIVADOSDELAEJECUCIÓNDEUNARESOLUCIÓNJUDICIALODEUNLAUDOEXENTOS',
            'D_104_IMPORTE',
            'D_105_AJUSTEAPAGOSQUESEREALICENAEXTRABAJADORESQUEOBTENGANUNAJUBILACIÓNENUNASOLAEXHIBICIÓNDERIVADOSDELAEJECUCIÓNDEUNARESOLUCIÓNJUDICIALODEUNLAUDOGRAVADOS',
            'D_105_IMPORTE',
            'D_106_AJUSTEAPAGOSQUESEREALICENAEXTRABAJADORESQUEOBTENGANUNAJUBILACIÓNENUNASOLAEXHIBICIÓNDERIVADOSDELAEJECUCIÓNDEUNARESOLUCIÓNJUDICIALODEUNLAUDOEXENTOS',
            'D_106_IMPORTE',
            'D_107_AJUSTE_AL_SUBSIDIO_CAUSADO',
            'O_001_REINTEGRODEISRPAGADOENEXCESO',
            'O_001_IMPORTE',
            'O_002_SUBSIDIOPARAELEMPLEO',
            'O_002_IMPORTE',
            'O_002_SUBSIDIOCAUSADO',
            'O_003_VIÁTICOS',
            'O_003_IMPORTE',
            'O_004_APLICACIÓNDESALDOAFAVORPORCOMPENSACIÓNANUAL.',
            'O_004_IMPORTE',
            'O_004_REMANENTESALFAV',
            'O_004_AÑO',
            'O_004_SALDOAFAVOR',
            'O_005_REINTEGRODEISRRETENIDOENEXCESODEEJERCICIOANTERIOR',
            'O_005_IMPORTE',
            'O_999_PAGOSDISTINTOSALOSLISTADOSYQUENODEBENCONSIDERARSECOMOINGRESOPORSUELDOSSALARIOSOINGRESOSASIMILADOS',
            'O_999_IMPORTE'
        ]