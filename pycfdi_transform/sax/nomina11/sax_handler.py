from __future__ import annotations
import logging
from lxml import etree
from pycfdi_transform.helpers.string_helper import StringHelper
from pycfdi_transform.sax.nomina11.base_handler import BaseHandler

class Nomina11SAXHandler(BaseHandler):
    def __init__(self, empty_char = '', safe_numerics = False,esc_delimiters:str = "") -> Nomina11SAXHandler:
        super().__init__(empty_char, safe_numerics,esc_delimiters)
        self._logger = logging.getLogger('Nomina11SAXHandler')

    def transform_from_string(self, xml_str:str) -> dict:
        try:
            xml_parser = etree.XMLParser(encoding='utf-8', recover=True)
            tree = etree.XML(xml_str, parser=xml_parser)
            context = etree.iterwalk(tree, events=("start",))
            self.__handle_events(context)
            return self._data
        except Exception as ex:
            self._logger.exception(f'Caugth Exception at tranforming xml string.')
            raise ex

    def __handle_events(self, context:etree.iterwalk) -> None:
        for action, elem in context:
            if action == 'start':
                if elem.prefix != 'nomina':
                    context.skip_subtree()
                elif elem.tag == '{http://www.sat.gob.mx/nomina}Nomina':
                    self.__transform_nomina(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina}Percepciones':
                    self.__transform_percepciones(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina}Percepcion':
                    self.__transform_percepcion(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina}Deducciones':
                    self.__transform_deducciones(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina}Deduccion':
                    self.__transform_deduccion(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina}Incapacidades':
                    self.__transform_incapacidades()
                elif elem.tag == '{http://www.sat.gob.mx/nomina}Incapacidad':
                    self.__transform_incapacidad(elem)
                elif elem.tag == '{http://www.sat.gob.mx/nomina}HorasExtras':
                    self.__transform_horas_extras()
                elif elem.tag == '{http://www.sat.gob.mx/nomina}HorasExtra':
                    self.__transform_horas_extra(elem)
                else:
                    context.skip_subtree()

    def __transform_nomina(self, element:etree._Element) -> None:
        if not 'Version' in element.attrib or element.attrib['Version'] != '1.1':
            raise ValueError('Incorrect type of Nomina, this handler only support Nomina version 1.1')
        self._data['version'] = element.attrib.get('Version')
        self._data['registro_patronal'] = element.attrib.get('RegistroPatronal', self._config['empty_char'])
        self._data['num_empleado'] = element.attrib.get('NumEmpleado')
        self._data['curp'] = element.attrib.get('CURP')
        self._data['tipo_regimen'] = element.attrib.get('TipoRegimen')
        self._data['num_seguridad_social'] = element.attrib.get('NumSeguridadSocial', self._config['empty_char'])
        self._data['fecha_pago'] = element.attrib.get('FechaPago')
        self._data['fecha_inicial_pago'] = element.attrib.get('FechaInicialPago')
        self._data['fecha_final_pago'] = element.attrib.get('FechaFinalPago')
        self._data['num_dias_pagados'] = element.attrib.get('NumDiasPagados')
        self._data['departamento'] = element.attrib.get('Departamento')
        self._data['clabe'] = element.attrib.get('CLABE')
        self._data['banco'] = element.attrib.get('Banco')
        self._data['fecha_inicio_rel_laboral'] = element.attrib.get('FechaInicioRelLaboral', self._config['empty_char'])
        self._data['antiguedad'] = element.attrib.get('Antiguedad', self._config['empty_char'])
        self._data['puesto'] = element.attrib.get('Puesto', self._config['empty_char'])
        self._data['tipo_contrato'] = element.attrib.get('TipoContrato', self._config['empty_char'])
        self._data['tipo_jornada'] = element.attrib.get('TipoJornada', self._config['empty_char'])
        self._data['periodicidad_pago'] = element.attrib.get('PeriodicidadPago')
        self._data['salario_base_cot_apor'] = element.attrib.get('SalarioBaseCotApor', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
        self._data['riesgo_puesto'] = element.attrib.get('RiesgoPuesto', self._config['empty_char'])
        self._data['salario_diario_integrado'] = element.attrib.get('SalarioDiarioIntegrado', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])

    def __transform_percepciones(self, element:etree._Element) -> None:
        self._data['percepciones'] = {
            'total_gravado': element.attrib.get('TotalGravado', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_exento': element.attrib.get('TotalExento', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'percepcion': []
        }

    def __transform_percepcion(self, element: etree._Element) -> None:
        self._data['percepciones']['percepcion'].append(
            {
                'tipo_percepcion': element.attrib.get('TipoPercepcion'),
                'clave': StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('Clave')),
                'concepto': StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('Concepto')),
                'importe_gravado': element.attrib.get('ImporteGravado', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
                'importe_exento': element.attrib.get('ImporteExento', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
            }
        )

    def __transform_deducciones(self, element:etree._Element) -> None:
        self._data['deducciones'] = {
            'total_gravado': element.attrib.get('TotalGravado', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'total_exento': element.attrib.get('TotalExento', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'deduccion': []
        }

    def __transform_deduccion(self, element: etree._Element) -> None:
        self._data['deducciones']['deduccion'].append(
            {
                'tipo_deduccion': element.attrib.get('TipoDeduccion'),
                'clave': StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('Clave')),
                'concepto': StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('Concepto')),
                'importe_gravado': element.attrib.get('ImporteGravado', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
                'importe_exento': element.attrib.get('ImporteExento', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
            }
        )

    def __transform_incapacidades(self) -> None:
        self._data['incapacidades'] = {
            'incapacidad': []
        }

    def __transform_incapacidad(self, element: etree._Element) -> None:
        self._data['incapacidades']['incapacidad'].append(
            {
                'dias_incapacidad': element.attrib.get('DiasIncapacidad'),
                'tipo_incapacidad': element.attrib.get('TipoIncapacidad'),
                'descuento': element.attrib.get('Descuento', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
            }
        )

    def __transform_horas_extras(self) -> None:
        self._data['horas_extras'] = {
            'horas_extra': []
        }

    def __transform_horas_extra(self, element: etree._Element) -> None:
        self._data['horas_extras']['horas_extra'].append(
            {
                'dias': element.attrib.get('Dias'),
                'tipo_horas': element.attrib.get('TipoHoras'),
                'horas_extra': element.attrib.get('HorasExtra'),
                'importe_pagado': element.attrib.get('ImportePagado', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
            }
        )