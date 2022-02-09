from __future__ import annotations
from pycfdi_transform.sax.cfdi32.base_handler import BaseHandler
from pycfdi_transform.helpers.string_helper import StringHelper
from lxml import etree
import logging


class CFDI32SAXHandler(BaseHandler):
    def __init__(self, empty_char='', safe_numerics=False, schema_validator: etree.XMLSchema = None, esc_delimiters: str = "") -> CFDI32SAXHandler:
        super().__init__(empty_char, safe_numerics, esc_delimiters)
        self._schema_validator = schema_validator
        self._logger = logging.getLogger('CFDI32SAXHandler')
        self._inside_concepts = False

    def transform_from_file(self, file_path: str) -> dict:
        if ('.xml' in file_path):
            return self.transform_from_string(StringHelper.file_path_to_string(file_path))
        else:
            raise ValueError('Incorrect type of document, only support XML files')

    def transform_from_string(self, xml_str: str) -> dict:
        try:
            self._clean_data()
            xml_parser = etree.XMLParser(encoding='utf-8', recover=True)
            tree = etree.XML(xml_str.encode(), parser=xml_parser)
            if not 'cfdi' in tree.nsmap or tree.nsmap['cfdi'] != 'http://www.sat.gob.mx/cfd/3':
                raise ValueError('The CFDI does\'t have correct namespace for CFDI V3.2.')
            if self._schema_validator != None and isinstance(self._schema_validator, etree.XMLSchema):
                self._schema_validator.assertValid(tree)
            context = etree.iterwalk(tree, events=("start", "end"))
            self.__handle_events(context)
            return self._data
        except Exception as ex:
            self._logger.exception(f'Caugth Exception at tranforming xml string.')
            raise ex

    def __handle_events(self, context: etree.iterwalk) -> None:
        for action, elem in context:
            if action == 'start':
                if elem.prefix != 'cfdi':
                    context.skip_subtree()
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Comprobante':
                    self.__transform_comprobante(elem)
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Emisor':
                    self.__transform_emisor(elem)
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}RegimenFiscal':
                    self.__transform_regimen_fiscal(elem)
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Receptor':
                    self.__transform_receptor(elem)
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Conceptos':
                    self._inside_concepts = True
            elif action == 'end':
                if elem.tag == '{http://www.sat.gob.mx/cfd/3}Conceptos':
                    self._inside_concepts = False
                    elem.clear()
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Concepto' and self._config['concepts']:
                    self.__transform_concept(elem)
                    elem.clear()
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Impuestos' and not self._inside_concepts:
                    self.__transform_general_taxes(elem)
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Complemento':
                    self.__transform_complement(elem)
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Addenda':
                    self.__transform_addenda(elem)

    def __transform_comprobante(self, element: etree._Element) -> None:
        if not 'version' in element.attrib or element.attrib['version'] != '3.2':
            raise ValueError('Incorrect type of CFDI, this handler only support CFDI version 3.2')
        self._data['cfdi32']['version'] = element.attrib.get('version')
        self._data['cfdi32']['serie'] = StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('serie', self._config['empty_char']))
        self._data['cfdi32']['folio'] = StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('folio', self._config['empty_char']))
        self._data['cfdi32']['fecha'] = element.attrib.get('fecha')
        self._data['cfdi32']['no_certificado'] = element.attrib.get('noCertificado')
        self._data['cfdi32']['subtotal'] = element.attrib.get('subTotal')
        self._data['cfdi32']['descuento'] = element.attrib.get('descuento', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
        self._data['cfdi32']['total'] = element.attrib.get('total')
        self._data['cfdi32']['moneda'] = element.attrib.get('Moneda')
        self._data['cfdi32']['tipo_cambio'] = element.attrib.get('TipoCambio', StringHelper.DEFAULT_SAFE_NUMBER_ONE if self._config['safe_numerics'] else self._config['empty_char'])
        self._data['cfdi32']['tipo_comprobante'] = element.attrib.get('tipoDeComprobante')
        self._data['cfdi32']['metodo_pago'] = StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('metodoDePago', self._config['empty_char']))
        self._data['cfdi32']['forma_pago'] = StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('formaDePago', self._config['empty_char']))
        self._data['cfdi32']['condiciones_pago'] = StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('condicionesDePago', self._config['empty_char']))
        self._data['cfdi32']['lugar_expedicion'] = element.attrib.get('LugarExpedicion')
        self._data['cfdi32']['sello'] = StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('sello'))
        self._data['cfdi32']['certificado'] = StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('certificado'))

    def __transform_emisor(self, element: etree._Element) -> None:
        self._data['cfdi32']['emisor']['rfc'] = element.attrib.get('rfc')
        self._data['cfdi32']['emisor']['nombre'] = StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('nombre', self._config['empty_char']))

    def __transform_regimen_fiscal(self, element: etree._Element) -> None:
        self._data['cfdi32']['emisor']['regimen_fiscal'].append(StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('Regimen', self._config['empty_char'])))

    def __transform_receptor(self, element: etree._Element) -> None:
        self._data['cfdi32']['receptor'] = {
            'rfc': element.attrib.get('rfc'),
            'nombre': StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('nombre', self._config['empty_char']))
        }

    def __transform_concept(self, element: etree._Element) -> None:
        concept = {
            'no_identificacion': StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('noIdentificacion', self._config['empty_char'])),
            'cantidad': element.attrib.get('cantidad'),
            'unidad': StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('unidad', self._config['empty_char'])),
            'descripcion': StringHelper.compact_string(self._config['esc_delimiters'], element.attrib.get('descripcion')),
            'valor_unitario': element.attrib.get('valorUnitario'),
            'importe': element.attrib.get('importe')
        }
        self._data['cfdi32']['conceptos'].append(concept)

    def __transform_general_taxes(self, element: etree._Element) -> None:
        self._data['cfdi32']['impuestos']['total_impuestos_traslados'] = element.attrib.get('totalImpuestosTrasladados', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
        self._data['cfdi32']['impuestos']['total_impuestos_retenidos'] = element.attrib.get('totalImpuestosRetenidos', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
        for child in element.getchildren():
            if child.tag == '{http://www.sat.gob.mx/cfd/3}Traslados':
                self.__transform_taxes_traslados(child.getchildren())
            elif child.tag == '{http://www.sat.gob.mx/cfd/3}Retenciones':
                self.__transform_taxes_retenciones(child.getchildren())

    def __transform_taxes_traslados(self, list_elements: list[etree._Element]) -> None:
        self._data['cfdi32']['impuestos']['traslados'] = []
        for traslado in list_elements:
            self._data['cfdi32']['impuestos']['traslados'].append(
                {
                    'impuesto': traslado.attrib.get('impuesto'),
                    'tasa': traslado.attrib.get('tasa'),
                    'importe': traslado.attrib.get('importe')
                }
            )

    def __transform_taxes_retenciones(self, list_elements: list[etree._Element]) -> None:
        self._data['cfdi32']['impuestos']['retenciones'] = []
        for retencion in list_elements:
            self._data['cfdi32']['impuestos']['retenciones'].append(
                {
                    'impuesto': retencion.attrib.get('impuesto'),
                    'importe': retencion.attrib.get('importe')
                }
            )

    def __transform_complement(self, element: etree._Element) -> None:
        complements = []
        for complement in element.getchildren():
            # Transform complement
            if complement.tag in self._complements:
                # Forces new instance of class
                transformer = self._complements[complement.tag]['class'](self._config['empty_char'], self._config['safe_numerics'])
                complement_data = transformer.transform_from_string(etree.tostring(complement, encoding='utf-8'))
                if not self._complements[complement.tag]['key'] in self._data:
                    self._data[self._complements[complement.tag]['key']] = []
                self._data[self._complements[complement.tag]['key']].append(complement_data)
                del transformer, complement_data
            # Annotate in complement list
            try:
                qname = etree.QName(complement.tag)
                if not qname.localname in complements:
                    complements.append(qname.localname)
            except Exception:
                complements.append(str(complement.tag))
        if len(complements) > 0:
            self._data['cfdi32']['complementos'] = ' '.join(complements)

    # TODO ADAPTAR
    def __transform_addenda(self, element: etree._Element) -> None:
        addendas = []
        for addenda in element.getchildren():
            try:
                qname = etree.QName(addenda.tag)
                if not qname.localname in addendas:
                    addendas.append(qname.localname)
            except Exception:
                addendas.append(str(addenda.tag))
        if len(addendas) > 0:
            self._data['cfdi32']['addendas'] = ' '.join(addendas)
