import xml.sax
from pycfdi_transform.sax import catalogs
from pycfdi_transform.sax.base32_handler import Base32Handler
from pycfdi_transform.sax.base33_handler import Base33Handler


class Nomina12Handler (xml.sax.ContentHandler, Base32Handler, Base33Handler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        Base32Handler.__init__(self)
        Base33Handler.__init__(self)
        self._start_emisor = False
        
        #Datos nodo nomina
        self._tipo_nomina = '-'
        self._fecha_pago = '-'
        self._fecha_inicial_pago = '-'
        self._fecha_final_pago = '-'
        self._num_dias_pagados = '-'
        self._total_percepciones = 0
        self._total_deducciones = 0
        self._total_otros_pagos = 0

        #Datos nodo emisor
        self._curp_emisor = '-'
        self._registro_patronal = '-'
        self._rfc_patron_origen = '-'

        #Datos nodo percepciones
        self._total_sueldos = 0
        self._total_separacion_indemnizacion = 0
        self._total_jubilacion_pension_retiro = 0
        self._total_gravado = 0
        self._total_excento = 0

        #Datos nodo receptor
        self._curp_receptor = '-'
        self._num_seguridad_social = '-'
        self._fecha_inicio_relacion_laboral = '-'
        self._sindicalizado = '-'
        self._tipo_jornada = '-'
        self._tipo_regimen = '-'
        self._num_empleado = '-'
        self._departamento = '-'
        self._puesto = '-'
        self._riesgo_puesto = '-'
        self._banco = '-'
        self._cuenta_bancaria = '-'
        self._antiguedad = '-'
        self._tipo_contrato = '-'
        self._periodicidad_pago = '-'
        self._salario_base_cot_apor = '-'
        self._salario_diario_integrado = '-'
        self._clave_ent_fed = '-'

        #datos nodos percepcion
        self._percepciones = {}

        #Datos nodo horas extra
        self._p19_dias = '-'
        self._p19_tipo_horas = '-'
        self._p19_horas_extra = '-'
        self._p19_importe_pagado = '-'

        #datos nodo JubilacionPensionRetiro
        self._p39_ingreso_no_acumulable = '-'
        self._p39_ingreso_acumulable = '-'
        self._p39_total_una_exhibicion = '-'
        self._p39_monto_diario = '-'
        self._p39_total_parcialidad = '-'

        #Datos nodo deducciones
        self._total_otras_deducciones = 0
        self._total_impuestos_retenidos = 0

        #datos nodos deduccion
        self._deducciones = {}

        #datos nodo incapacidad
        self._d006_dias_incapacidad = '-'
        self._d006_tipo_incapacidad = '-'
        self._d006_importe_monetario = '-'

        #datos otro pago
        self._otros_pagos = {}

        #datos otro SubsidioAlEmpleo
        self._o002_subsidio_causado = '-'

        #datos otro SubsidioAlEmpleo
        self._o004_saldo_favor = '-'
        self._o004_ano = '-'
        self._o004_remanente_saldo_favor = '-'
        
    def startElement(self, tag, attrs):
        if (tag == 'cfdi:Comprobante'):
            if ('Version' in attrs):
                Base33Handler.transform_comprobante(self, tag, attrs)
            elif ('version' in attrs):
                Base32Handler.transform_comprobante(self, tag, attrs)
        elif (tag == 'cfdi:Emisor'):
            if (self._version == '3.3'):
                Base33Handler.transform_emisor(self, tag, attrs)
            else:
                self._start_emisor = True
                Base32Handler.transform_emisor(self, tag, attrs)
        elif (tag == 'cfdi:Receptor'):
            if (self._version == '3.3'):
                Base33Handler.transform_receptor(self, tag, attrs)
            else:
                Base32Handler.transform_receptor(self, tag, attrs)
        elif (tag == 'cfdi:RegimenFiscal' and self._start_emisor and self._version == '3.2'):
            Base32Handler.transform_regimen_fiscal(self, tag, attrs)
        elif (tag == 'tfd:TimbreFiscalDigital'):
            if (self._version == '3.3'):
                Base33Handler.transform_tfd(self, tag, attrs)
            else:
                Base32Handler.transform_tfd(self, tag, attrs)
        elif (tag == 'nomina12:Nomina'):
            self.__transform_nomina12(tag, attrs)
        elif (tag == 'nomina12:Emisor'):
            self.__transform_nomina12_emisor(tag, attrs)
        elif (tag == 'nomina12:Receptor'):
            self.__transform_nomina12_receptor(tag, attrs)
        elif (tag == 'nomina12:Percepciones'):
            self.__transform_nomina12_percepciones(tag, attrs)
        elif (tag == 'nomina12:Percepcion'):
            self.__transform_nomina12_percepcion(tag, attrs)
        elif (tag == 'nomina12:HorasExtra'):
            self.__transform_horas_extra(tag, attrs)
        elif (tag == 'nomina12:JubilacionPensionRetiro'):
            self.__transform_jubilacion_pension_retiro(tag, attrs)
        elif (tag == 'nomina12:Deducciones'):
            self.__transform_nomina12_deducciones(tag, attrs)
        elif (tag == 'nomina12:Deduccion'):
            self.__transform_nomina12_deduccion(tag, attrs)
        elif (tag == 'nomina12:Incapacidad'):
            self.__transform_incapacidad(tag, attrs)
        elif (tag == 'nomina12:OtroPago'):
            self.__transform_otro_pago(tag, attrs)
        elif (tag == 'nomina12:SubsidioAlEmpleo'):
            self.__transform_subsidio_causado(tag, attrs)
        elif (tag == 'nomina12:CompensacionSaldosAFavor'):
            self.__transform_compensaciones_saldos_a_favor(tag, attrs)


    def endElement(self, tag):
        if (tag == 'cfdi:Emisor'):
            self._start_emisor = False

    def __transform_nomina12(self, tag, attrs):
        self._tipo_nomina = attrs['TipoNomina']
        self._fecha_pago = attrs['FechaPago']
        self._fecha_inicial_pago = attrs['FechaInicialPago']
        self._fecha_final_pago = attrs['FechaFinalPago']
        self._num_dias_pagados = attrs['NumDiasPagados']
        if ('TotalPercepciones' in attrs):
            self._total_percepciones += float(attrs['TotalPercepciones'])
        if ('TotalDeducciones' in attrs):
            self._total_deducciones += float(attrs['TotalDeducciones'])
        if ('TotalOtrosPagos' in attrs):
            self._total_otros_pagos += float(attrs['TotalOtrosPagos'])
    
    def __transform_nomina12_emisor(self, tag, attrs):
        if ('Curp' in attrs):
            self._curp_emisor = attrs['Curp']
        if ('RegistroPatronal' in attrs):
            self._registro_patronal = attrs['RegistroPatronal']
        if ('RfcPatronOrigen' in attrs):
            self._rfc_patron_origen = attrs['RfcPatronOrigen']
    
    def __transform_nomina12_receptor(self, tag, attrs):
        if ('Curp' in attrs):
            self._curp_receptor = attrs['Curp']
        if ('NumSeguridadSocial' in attrs):
            self._num_seguridad_social = attrs['NumSeguridadSocial']
        if ('FechaInicioRelLaboral' in attrs):
            self._fecha_inicio_relacion_laboral = attrs['FechaInicioRelLaboral']
        if ('Sindicalizado' in attrs):
            self._sindicalizado = attrs['Sindicalizado']
        if ('TipoJornada' in attrs):
            self._tipo_jornada = attrs['TipoJornada']
        if ('TipoRegimen' in attrs):
            self._tipo_regimen = attrs['TipoRegimen']
        if ('NumEmpleado' in attrs):
            self._num_empleado = attrs['NumEmpleado']
        if ('Departamento' in attrs):
            self._departamento = attrs['Departamento']
        if ('Puesto' in attrs):
            self._puesto = attrs['Puesto']
        if ('RiesgoPuesto' in attrs):
            self._riesgo_puesto = attrs['RiesgoPuesto']
        if ('Banco' in attrs):
            self._banco = attrs['Banco']
        if ('CuentaBancaria' in attrs):
            self._cuenta_bancaria = attrs['CuentaBancaria']
        if ('Antigüedad' in attrs):
            self._antiguedad = attrs['Antigüedad']
        if ('TipoContrato' in attrs):
            self._tipo_contrato = attrs['TipoContrato']
        if ('PeriodicidadPago' in attrs):
            self._periodicidad_pago = attrs['PeriodicidadPago']
        if ('SalarioBaseCotApor' in attrs):
            self._salario_base_cot_apor= attrs['SalarioBaseCotApor']
        if ('SalarioDiarioIntegrado' in attrs):
            self._salario_diario_integrado = attrs['SalarioDiarioIntegrado']
        if ('ClaveEntFed' in attrs):
            self._clave_ent_fed = attrs['ClaveEntFed']

    def __transform_nomina12_percepciones(self, tag, attrs):
        if ('TotalSueldos' in attrs):
            self._total_sueldos += float(attrs['TotalSueldos'])
        if ('TotalSeparacionIndemnizacion' in attrs):
            self._total_separacion_indemnizacion += float(attrs['TotalSeparacionIndemnizacion'])
        if ('TotalJubilacionPensionRetiro' in attrs):
            self._total_jubilacion_pension_retiro += float(attrs['TotalJubilacionPensionRetiro'])
        if ('TotalGravado' in attrs):
            self._total_gravado += float(attrs['TotalGravado'])
        if ('TotalExento' in attrs):
            self._total_excento += float(attrs['TotalExento'])
    
    def __transform_nomina12_percepcion(self, tag, attrs):
        if ('TipoPercepcion' in attrs):
            tipo_percepcion = attrs['TipoPercepcion']
            importe_excento = '0.00'
            importe_gravado = '0.00'
            if ('ImporteExento' in attrs):
                importe_excento = attrs['ImporteExento']
            if ('ImporteGravado' in attrs):
                importe_gravado = attrs['ImporteGravado']
            if (tipo_percepcion in self._percepciones):
                percepcion = self._percepciones[tipo_percepcion]
                importe_excento = Base33Handler.sum(self, percepcion[1], importe_excento)
                importe_gravado = Base33Handler.sum(self, percepcion[2], importe_gravado)
            self._percepciones[tipo_percepcion] = [tipo_percepcion,
                                                   importe_excento, importe_gravado]
    
    def __transform_horas_extra(self, tag, attrs):
        if ('Dias' in attrs):
            self._p19_dias = attrs['Dias']
        if ('TipoHoras' in attrs):
            self._p19_tipo_horas = attrs['TipoHoras']
        if ('HorasExtra' in attrs):
            self._p19_horas_extra = attrs['HorasExtra']
        if ('ImportePagado' in attrs):
            self._p19_importe_pagado = attrs['ImportePagado']
    
    def __transform_jubilacion_pension_retiro(self, tag, attrs):
        if ('IngresoNoAcumulable' in attrs):
            self._p39_ingreso_no_acumulable = attrs['IngresoNoAcumulable']
        if ('IngresoAcumulable' in attrs):
            self._p39_ingreso_acumulable = attrs['IngresoAcumulable']
        if ('TotalUnaExhibicion' in attrs):
            self._p39_total_una_exhibicion = attrs['TotalUnaExhibicion']
        if ('MontoDiario' in attrs):    
            self._p39_monto_diario = attrs['MontoDiario']
        if ('TotalParcialidad' in attrs):
            self._p39_total_parcialidad = attrs['TotalParcialidad']
            
    
    def __transform_nomina12_deducciones(self, tag, attrs):
        if ('TotalOtrasDeducciones' in attrs):
            self._total_otras_deducciones += float(attrs['TotalOtrasDeducciones'])
        if ('TotalImpuestosRetenidos' in attrs):
            self._total_impuestos_retenidos += float(attrs['TotalImpuestosRetenidos'])

    def __transform_nomina12_deduccion(self, tag, attrs):
        if ('TipoDeduccion' in attrs):
            tipo_deduccion = attrs['TipoDeduccion']
            importe = '0.00'
            if ('Importe' in attrs): 
                importe = attrs['Importe']
            if (tipo_deduccion in self._deducciones):
                deduccion= self._deducciones[tipo_deduccion]
                importe = Base33Handler.sum(self, deduccion[1], importe)

            self._deducciones[tipo_deduccion] = [tipo_deduccion, importe]

    def __transform_incapacidad(self, tag, attrs):
        if ('DiasIncapacidad' in attrs):
            self._d006_dias_incapacidad = attrs['DiasIncapacidad']
        if ('TipoIncapacidad' in attrs):
            self._d006_tipo_incapacidad = attrs['TipoIncapacidad']
        if ('ImporteMonetario' in attrs):
            self._d006_importe_monetario = attrs['ImporteMonetario']
    
    def __transform_otro_pago(self, tag, attrs):
        if ('TipoOtroPago' in attrs):
            tipo_otro_pago = attrs['TipoOtroPago']
            importe = '0.00'
            if ('Importe' in attrs):
                importe = attrs['Importe']
            self._otros_pagos[tipo_otro_pago] = [tipo_otro_pago, importe]
    
    def __transform_subsidio_causado(self, tag, attrs):
        if ('SubsidioCausado' in attrs):
            self._o002_subsidio_causado = attrs['SubsidioCausado']
        else:
            self._o002_subsidio_causado = '0.00'

    def __transform_compensaciones_saldos_a_favor(self, tag, attrs):
        if ('SaldoAFavor' in attrs):
            self._o004_saldo_favor = attrs['SaldoAFavor']
        if ('Año' in attrs):
            self._o004_ano = attrs['Año']
        if ('RemanenteSalFav' in attrs):
            self._o004_remanente_saldo_favor = attrs['RemanenteSalFav']

    def get_result(self):
        self._total_sueldos = str(self._total_sueldos)
        self._total_gravado = str(self._total_gravado)
        self._total_excento = str(self._total_excento)
        self._total_separacion_indemnizacion = str(self._total_separacion_indemnizacion)
        self._total_jubilacion_pension_retiro = str(self._total_jubilacion_pension_retiro)
        self._total_percepciones = str(self._total_percepciones)
        self._total_deducciones = str(self._total_deducciones )
        self._total_otros_pagos = str(self._total_otros_pagos)
        self._total_otras_deducciones = str(self._total_otras_deducciones)
        self._total_impuestos_retenidos = str(self._total_impuestos_retenidos)
        list_result = list()
        for tfd in self._tfds:
            row = [
                self._version,
                self._serie,
                self._folio,
                self._fecha,
                self._no_certificado,
                self._subtotal,
                self._descuento,
                self._total,
                self._moneda,
                self._tipo_cambio,
                self._tipo_comprobante,
                self._metodo_pago,
                self._forma_pago,
                self._condiciones_pago,
                self._lugar_expedicion,
                self._rfc_emisor,
                self._nombre_emisor,
                self._regimen_fiscal_emisor,
                self._rfc_receptor,
                self._nombre_receptor,
                self._uso_cfdi_receptor,
                tfd['UUID'],
                tfd['FechaTimbrado'],
                tfd['RfcProvCertif'],
                tfd['SelloCFD'],
                self._tipo_nomina,
                self._fecha_pago,
                self._fecha_inicial_pago,
                self._fecha_final_pago,
                self._num_dias_pagados,
                self._total_percepciones,
                self._total_deducciones,
                self._total_otros_pagos,
                self._curp_emisor,
                self._registro_patronal,
                self._rfc_patron_origen,
                self._curp_receptor,
                self._num_seguridad_social,
                self._fecha_inicio_relacion_laboral,
                self._sindicalizado,
                self._tipo_jornada,
                self._tipo_regimen,
                self._num_empleado,
                self._departamento,
                self._puesto,
                self._riesgo_puesto,
                self._banco,
                self._cuenta_bancaria,
                self._antiguedad,
                self._tipo_contrato,
                self._periodicidad_pago,
                self._salario_base_cot_apor,
                self._salario_diario_integrado,
                self._clave_ent_fed,
                self._total_sueldos,
                self._total_separacion_indemnizacion,
                self._total_jubilacion_pension_retiro,
                self._total_gravado,
                self._total_excento
            ]

            for percepcion_codigo in catalogs.PERCEPCIONES:
                if (percepcion_codigo in self._percepciones):
                    percepcion = self._percepciones[percepcion_codigo]
                    row.extend(percepcion)
                else:
                    row.extend(['-', '-', '-'])
                
                if (percepcion_codigo == '019'):
                        row.extend([self._p19_dias,
                                    self._p19_tipo_horas,
                                    self._p19_horas_extra,
                                    self._p19_importe_pagado])
                elif (percepcion_codigo == '039'):
                        row.extend([self._p39_ingreso_no_acumulable,
                                    self._p39_ingreso_acumulable,
                                    self._p39_total_una_exhibicion,
                                    self._p39_monto_diario,
                                    self._p39_total_parcialidad])
                elif (percepcion_codigo == '044'):
                        row.extend([self._p39_ingreso_no_acumulable,
                                    self._p39_ingreso_acumulable,
                                    self._p39_total_una_exhibicion,
                                    self._p39_monto_diario,
                                    self._p39_total_parcialidad])
            
            row.append(self._total_otras_deducciones)
            row.append(self._total_impuestos_retenidos)

            for deduccion_codigo in catalogs.DEDUCCIONES:
                if (deduccion_codigo in self._deducciones):
                    deduccion = self._deducciones[deduccion_codigo]
                    row.extend(deduccion)
                else:
                    row.extend(['-', '-'])

                if (deduccion_codigo == '006'):
                    row.extend([self._d006_importe_monetario,
                                self._d006_tipo_incapacidad,
                                self._d006_dias_incapacidad])

            for otros_codigo in catalogs.OTROS_PAGOS:
                if (otros_codigo in self._otros_pagos):
                    otro_pago = self._otros_pagos[otros_codigo]
                    row.extend(otro_pago)
                else:
                    row.extend(['-', '-'])
                
                if (otros_codigo == '002'):
                    row.extend([self._o002_subsidio_causado])
                elif (otros_codigo == '004'):
                    row.extend([self._o004_remanente_saldo_favor,
                                self._o004_ano,
                                self._o004_saldo_favor])
            list_result.append(row)
        return list_result
