from __future__ import annotations
import logging
from lxml import etree
from pycfdi_transform.helpers.string_helper import StringHelper
from pycfdi_transform.sax.nomina12.base_handler import BaseHandler

class Nomina12SAXHandler(BaseHandler):
    def __init__(self, empty_char = '', safe_numerics = False,esc_delimiters:str = "") -> Nomina12SAXHandler:
        super().__init__(empty_char, safe_numerics,esc_delimiters)
        self._logger = logging.getLogger('Nomina12SAXHandler')
    
    def transform_from_string(self, xml_str:str) -> dict:
        try:
            xml_parser = etree.XMLParser(encoding='utf-8', recover=True)
            tree = etree.XML(xml_str, parser=xml_parser)
            context = etree.iterwalk(tree, events=("start", "end"))
            self.__handle_events(context)
            return self._data
        except Exception as ex:
            self._logger.exception(f'Caugth Exception at tranforming xml string.')
            raise ex
    
    def __handle_events(self, context:etree.iterwalk) -> None:
        for action, elem in context:
            if action == 'start':
                if elem.prefix != 'nomina12':
                    context.skip_subtree()
                elif elem.tag == '{http://www.sat.gob.mx/nomina12}Nomina':
                    self.__transform_nomina(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina12}Emisor':
                    self.__transform_emisor(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina12}Receptor':
                    self.__transform_receptor(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina12}SubContratacion':
                    self.__transform_receptor_subcontratacion(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina12}EntidadSNCF':
                    self.__transform_emisor_snfc(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina12}Percepciones':
                    self.__transform_percepciones(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina12}JubilacionPensionRetiro':
                    self.__transform_jubilacion(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina12}SeparacionIndemnizacion':
                    self.__transform_separacion(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina12}Deducciones':
                    self.__transform_deducciones(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina12}Deduccion':
                    self.__transform_deduccion(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina12}OtrosPagos':
                    self.__transform_otros_pagos()
                elif elem.tag == '{http://www.sat.gob.mx/nomina12}Incapacidades':
                    self.__transform_incapacidades()
                elif elem.tag == '{http://www.sat.gob.mx/nomina12}Incapacidad':
                    self.__transform_incapacidad(elem)
            elif action == 'end':
                if elem.tag == '{http://www.sat.gob.mx/nomina12}Percepcion':
                    self.__transform_percepcion(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina12}OtroPago':
                    self.__transform_otro_pago(elem)
    
    def __transform_nomina(self, element:etree._Element) -> None:
        if not 'Version' in element.attrib or element.attrib['Version'] != '1.2':
            raise ValueError('Incorrect type of Nomina, this handler only support Nomina version 1.2')
        self._data['version'] = element.attrib.get('Version')
        self._data['tipo_nomina'] = element.attrib.get('TipoNomina')
        self._data['fecha_pago'] = element.attrib.get('FechaPago')
        self._data['fecha_inicial_pago'] = element.attrib.get('FechaInicialPago')
        self._data['fecha_final_pago'] = element.attrib.get('FechaFinalPago')
        self._data['num_dias_pagados'] = element.attrib.get('NumDiasPagados')
        self._data['total_percepciones'] = element.attrib.get('TotalPercepciones', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
        self._data['total_deducciones'] = element.attrib.get('TotalDeducciones', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
        self._data['total_otros_pagos'] = element.attrib.get('TotalOtrosPagos', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
    
    def __transform_emisor(self, element:etree._Element) -> None:
        self._data['emisor']['curp'] = element.attrib.get('Curp', self._config['empty_char'])
        self._data['emisor']['registro_patronal'] = StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('RegistroPatronal', self._config['empty_char']))
        self._data['emisor']['rfc_patron_origen'] = element.attrib.get('RfcPatronOrigen', self._config['empty_char'])
    
    def __transform_emisor_snfc(self, element:etree._Element) -> None:
        self._data['emisor']['entidad_SNCF']['origen_recurso'] = element.attrib.get('OrigenRecurso')
        self._data['emisor']['entidad_SNCF']['monto_recurso_propio'] = element.attrib.get('MontoRecursoPropio', self._config['empty_char'])
    
    def __transform_receptor(self, element:etree._Element) -> None:
        self._data['receptor']['curp'] = element.attrib.get('Curp')
        self._data['receptor']['num_seguridad_social'] = element.attrib.get('NumSeguridadSocial', self._config['empty_char'])
        self._data['receptor']['fecha_inicio_rel_laboral'] = element.attrib.get('FechaInicioRelLaboral', self._config['empty_char'])
        self._data['receptor']['antigüedad'] = element.attrib.get('Antigüedad', self._config['empty_char'])
        self._data['receptor']['tipo_contrato'] = element.attrib.get('TipoContrato')
        self._data['receptor']['sindicalizado'] = element.attrib.get('Sindicalizado', self._config['empty_char'])
        self._data['receptor']['tipo_jornada'] = element.attrib.get('TipoJornada', self._config['empty_char'])
        self._data['receptor']['tipo_regimen'] = element.attrib.get('TipoRegimen')
        self._data['receptor']['num_empleado'] = StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('NumEmpleado'))
        self._data['receptor']['departamento'] = StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Departamento', self._config['empty_char']))
        self._data['receptor']['puesto'] = StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Puesto', self._config['empty_char']))
        self._data['receptor']['riesgo_puesto'] = element.attrib.get('RiesgoPuesto', self._config['empty_char'])
        self._data['receptor']['periodicidad_pago'] = element.attrib.get('PeriodicidadPago')
        self._data['receptor']['banco'] = element.attrib.get('Banco', self._config['empty_char'])
        self._data['receptor']['cuenta_bancaria'] = element.attrib.get('CuentaBancaria', self._config['empty_char'])
        self._data['receptor']['salario_base_cot_apor'] = element.attrib.get('SalarioBaseCotApor', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
        self._data['receptor']['salario_diario_integrado'] = element.attrib.get('SalarioDiarioIntegrado', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
        self._data['receptor']['clave_ent_fed'] = element.attrib.get('ClaveEntFed')
        self._data['receptor']['subcontratacion'] = []

    def __transform_receptor_subcontratacion(self, element:etree._Element) -> None:
        self._data['receptor']['subcontratacion'].append(
            {
                'rfc_labora': element.attrib.get('RfcLabora'),
                'porcentaje_tiempo': element.attrib.get('PorcentajeTiempo')
            }
        )
    def __transform_percepciones(self, element:etree._Element) -> None:
        self._data['percepciones'] = {
            'total_sueldos': element.attrib.get('TotalSueldos', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_separacion_indemnizacion': element.attrib.get('TotalSeparacionIndemnizacion', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_jubilacion_pension_retiro': element.attrib.get('TotalJubilacionPensionRetiro', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_gravado': element.attrib.get('TotalGravado'),
            'total_exento': element.attrib.get('TotalExento'),
            'percepcion': []
        }
    def __transform_percepcion(self, element:etree._Element) -> None:
        percepcion = {
            'tipo_percepcion': element.attrib.get('TipoPercepcion'),
            'clave': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Clave')),
            'concepto': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Concepto')),
            'importe_gravado': element.attrib.get('ImporteGravado'),
            'importe_exento': element.attrib.get('ImporteExento'),
            'horas_extra': []
        }
        for child in element.getchildren():
            if child.tag == '{http://www.sat.gob.mx/nomina12}HorasExtra':
                percepcion['horas_extra'].append(
                    {
                        'dias': child.attrib.get('Dias'),
                        'tipo_horas': child.attrib.get('TipoHoras'),
                        'horas_extra': child.attrib.get('HorasExtra'),
                        'importe_pagado': child.attrib.get('ImportePagado')
                    }
                )
            elif child.tag == '{http://www.sat.gob.mx/nomina12}AccionesOTitulos':
                percepcion['acciones_o_titulos'] = {
                    'valor_mercado': child.attrib.get('ValorMercado'),
                    'precio_al_otorgarse': child.attrib.get('PrecioAlOtorgarse')
                }
        self._data['percepciones']['percepcion'].append(percepcion)
    
    def __transform_jubilacion(self, element:etree._Element) -> None:
        self._data['percepciones']['jubilacion_pension_retiro'] = {
            'total_una_exhibicion': element.attrib.get('TotalUnaExhibicion', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_parcialidad': element.attrib.get('TotalParcialidad', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'monto_diario': element.attrib.get('MontoDiario', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'ingreso_acumulable': element.attrib.get('IngresoAcumulable'),
            'ingreso_no_acumulable': element.attrib.get('IngresoNoAcumulable')
        }

    def __transform_separacion(self, element:etree._Element) -> None:
        self._data['percepciones']['separacion_indemnizacion'] = {
            'total_pagado': element.attrib.get('TotalPagado'),
            'num_años_servicio': element.attrib.get('NumAñosServicio'),
            'ultimo_sueldo_mens_ord': element.attrib.get('UltimoSueldoMensOrd'),
            'ingreso_acumulable': element.attrib.get('IngresoAcumulable'),
            'ingreso_no_acumulable': element.attrib.get('IngresoNoAcumulable'),
        }
    
    def __transform_deducciones(self, element:etree._Element) -> None:
        self._data['deducciones'] = {
            'total_otras_deducciones': element.attrib.get('TotalOtrasDeducciones', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_impuestos_retenidos': element.attrib.get('TotalImpuestosRetenidos', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'deduccion': []
        }
    
    def __transform_deduccion(self, element:etree._Element) -> None:
        self._data['deducciones']['deduccion'].append(
            {
                'tipo_deduccion': element.attrib.get('TipoDeduccion'),
                'clave': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Clave')),
                'concepto': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Concepto')),
                'importe': element.attrib.get('Importe')
            }
        )

    def __transform_otros_pagos(self) -> None:
        self._data['otros_pagos'] = {
            'otro_pago': []
        }
    
    def __transform_otro_pago(self, element:etree._Element) -> None:
        otro_pago = {
            'tipo_otro_pago': element.attrib.get('TipoOtroPago'),
            'clave': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Clave')),
            'concepto': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Concepto')),
            'importe': element.attrib.get('Importe'),
        }
        for child in element.getchildren():
            if child.tag == '{http://www.sat.gob.mx/nomina12}SubsidioAlEmpleo':
                otro_pago['subsidio_al_empleo'] = {
                    'subsidio_causado': child.attrib.get('SubsidioCausado')
                }
            elif child.tag == '{http://www.sat.gob.mx/nomina12}CompensacionSaldosAFavor':
                otro_pago['compensacion_saldos_a_favor'] = {
                    'saldo_a_favor': child.attrib.get('SaldoAFavor'),
                    'año': child.attrib.get('Año'),
                    'remanente_sal_fav': child.attrib.get('RemanenteSalFav')
                }
        self._data['otros_pagos']['otro_pago'].append(otro_pago)
    
    def __transform_incapacidades(self) -> None:
        self._data['incapacidades'] = {
            'incapacidad': []
        }
    
    def __transform_incapacidad(self, element:etree._Element) -> None:
        self._data['incapacidades']['incapacidad'].append(
            {
                'dias_incapacidad': element.attrib.get('DiasIncapacidad'),
                'tipo_incapacidad': element.attrib.get('TipoIncapacidad'),
                'importe_monetario': element.attrib.get('ImporteMonetario', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
            }
        )