
from __future__ import annotations
from pycfdi_transform.sax.cfdi33.base_handler import BaseHandler
from pycfdi_transform.helpers.string_helper import StringHelper
from lxml import etree
import logging

from pycfdi_transform.sax.terceros11.sax_handler import Terceros11SAXHandler


class CFDI33SAXHandler(BaseHandler):
    def __init__(self, empty_char='', safe_numerics=False, schema_validator:etree.XMLSchema = None,esc_delimiters:str = "") -> CFDI33SAXHandler:
        super().__init__(empty_char, safe_numerics,esc_delimiters)
        self._schema_validator = schema_validator
        self._logger = logging.getLogger('CFDI33SAXHandler')
        self._inside_concepts = False

    def transform_from_file(self, file_path:str) -> dict:
        if ('.xml' in file_path):
            return self.transform_from_string(StringHelper.file_path_to_string(file_path))
        else:
            raise ValueError('Incorrect type of document, only support XML files')
    def transform_from_string(self, xml_str:str) -> dict:
        try:
            self._clean_data()
            xml_parser = etree.XMLParser(encoding='utf-8', recover=True)
            tree = etree.XML(xml_str.encode(), parser=xml_parser)
            if not 'cfdi' in tree.nsmap or tree.nsmap['cfdi'] != 'http://www.sat.gob.mx/cfd/3':
                raise ValueError('The CFDI does\'t have correct namespace for CFDI V3.3.')
            if self._schema_validator != None and isinstance(self._schema_validator, etree.XMLSchema):
                self._schema_validator.assertValid(tree)
            context = etree.iterwalk(tree, events=("start", "end"))
            self.__handle_events(context)
            return self._data
        except Exception as ex:
            self._logger.exception(f'Caugth Exception at tranforming xml string.')
            raise ex

    def __handle_events(self, context:etree.iterwalk) -> None:
        for action, elem in context:
            if action == 'start':
                if elem.prefix != 'cfdi':
                    context.skip_subtree()
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Comprobante':
                    self.__transform_comprobante(elem)
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Emisor':
                    self.__transform_emisor(elem)
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
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}CfdiRelacionados' and self._config['cfdis_relacionados']:
                    self.__transform_related_cfdi(elem)
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Impuestos' and not self._inside_concepts:
                    self.__transform_general_taxes(elem)
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Complemento':
                    self.__transform_complement(elem)
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Addenda':
                    self.__transform_addenda(elem)

    def __transform_comprobante(self, element:etree._Element) -> None:
        if not 'Version' in element.attrib or element.attrib['Version'] != '3.3':
            raise ValueError('Incorrect type of CFDI, this handler only support CFDI version 3.3')
        self._data['cfdi33']['version'] = element.attrib.get('Version')
        self._data['cfdi33']['serie'] = StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Serie', self._config['empty_char']))
        self._data['cfdi33']['folio'] = StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Folio', self._config['empty_char']))
        self._data['cfdi33']['fecha'] = element.attrib.get('Fecha')
        self._data['cfdi33']['no_certificado'] = element.attrib.get('NoCertificado')
        self._data['cfdi33']['subtotal'] = element.attrib.get('SubTotal')
        self._data['cfdi33']['descuento'] = element.attrib.get('Descuento', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
        self._data['cfdi33']['total'] = element.attrib.get('Total')
        self._data['cfdi33']['moneda'] = element.attrib.get('Moneda')
        self._data['cfdi33']['tipo_cambio'] = element.attrib.get('TipoCambio', StringHelper.DEFAULT_SAFE_NUMBER_ONE if self._config['safe_numerics'] else self._config['empty_char'])
        self._data['cfdi33']['tipo_comprobante'] = element.attrib.get('TipoDeComprobante')
        self._data['cfdi33']['metodo_pago'] = StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('MetodoPago', self._config['empty_char']))
        self._data['cfdi33']['forma_pago'] = StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('FormaPago', self._config['empty_char']))
        self._data['cfdi33']['condiciones_pago'] = StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('CondicionesDePago', self._config['empty_char']))
        self._data['cfdi33']['lugar_expedicion'] = element.attrib.get('LugarExpedicion')
        self._data['cfdi33']['sello'] = StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Sello'))
        self._data['cfdi33']['certificado'] = StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Certificado'))
        self._data['cfdi33']['confirmacion'] = element.attrib.get('Confirmacion', self._config['empty_char'])

    def __transform_emisor(self, element:etree._Element) -> None:
        self._data['cfdi33']['emisor'] = {
            'rfc': element.attrib.get('Rfc'),
            'nombre': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Nombre', self._config['empty_char'])),
            'regimen_fiscal': element.attrib.get('RegimenFiscal')
        }

    def __transform_receptor(self, element:etree._Element) -> None:
        self._data['cfdi33']['receptor'] = {
            'rfc': element.attrib.get('Rfc'),
            'nombre': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Nombre', self._config['empty_char'])),
            'residencia_fiscal': element.attrib.get('ResidenciaFiscal', self._config['empty_char']),
            'num_reg_id_trib': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('NumRegIdTrib', self._config['empty_char'])),
            'uso_cfdi': element.attrib.get('UsoCFDI'),
        }

    def __transform_concept(self, element:etree._Element) -> None:
        concept = {
            'clave_prod_serv': element.attrib.get('ClaveProdServ'),
            'no_identificacion': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('NoIdentificacion', self._config['empty_char'])),
            'cantidad': element.attrib.get('Cantidad'),
            'clave_unidad': element.attrib.get('ClaveUnidad'),
            'unidad': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Unidad', self._config['empty_char'])),
            'descripcion': StringHelper.compact_string(self._config['esc_delimiters'],element.attrib.get('Descripcion')),
            'valor_unitario': element.attrib.get('ValorUnitario'),
            'importe': element.attrib.get('Importe'),
            'descuento': element.attrib.get('Descuento', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
            'terceros': self.__transform_terceros(element)
        }
        self._data['cfdi33']['conceptos'].append(concept)

    def __transform_terceros(self, element: etree._Element):
        terceros_data = dict()
        for child in element.getchildren():
            if child.tag == '{http://www.sat.gob.mx/cfd/3}ComplementoConcepto':
                terceros_data = Terceros11SAXHandler(self._config['empty_char'], self._config['safe_numerics']).transform_from_string(etree.tostring(child, encoding='utf-8'))
        return terceros_data

    def __transform_general_taxes(self, element:etree._Element) -> None:
        self._data['cfdi33']['impuestos']['total_impuestos_traslados'] = element.attrib.get('TotalImpuestosTrasladados', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
        self._data['cfdi33']['impuestos']['total_impuestos_retenidos'] = element.attrib.get('TotalImpuestosRetenidos', StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char'])
        for child in element.getchildren():
            if child.tag == '{http://www.sat.gob.mx/cfd/3}Traslados':
                self.__transform_taxes_traslados(child.getchildren())
            elif child.tag == '{http://www.sat.gob.mx/cfd/3}Retenciones':
                self.__transform_taxes_retenciones(child.getchildren())

    def __transform_taxes_traslados(self, list_elements:list[etree._Element]) -> None:
        self._data['cfdi33']['impuestos']['traslados'] = []
        for traslado in list_elements:
            self._data['cfdi33']['impuestos']['traslados'].append(
                {
                    'impuesto': traslado.attrib.get('Impuesto'),
                    'tipo_factor': traslado.attrib.get('TipoFactor'),
                    'tasa_o_cuota': traslado.attrib.get('TasaOCuota'),
                    'importe': traslado.attrib.get('Importe')
                }
            )

    def __transform_taxes_retenciones(self, list_elements:list[etree._Element]) -> None:
        self._data['cfdi33']['impuestos']['retenciones'] = []
        for retencion in list_elements:
            self._data['cfdi33']['impuestos']['retenciones'].append(
                {
                    'impuesto': retencion.attrib.get('Impuesto'),
                    'importe': retencion.attrib.get('Importe')
                }
            )

    def __transform_complement(self, element:etree._Element) -> None:
        complements = []
        for complement in element.getchildren():
            # Transform complement
            if complement.tag in self._complements:
                #Forces new instance of class
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
            self._data['cfdi33']['complementos'] = ' '.join(complements)

    def __transform_addenda(self, element:etree._Element) -> None:
        addendas = []
        for addenda in element.getchildren():
            try:
                qname = etree.QName(addenda.tag)
                if not qname.localname in addendas:
                    addendas.append(qname.localname)
            except Exception:
                addendas.append(str(addenda.tag))
        if len(addendas) > 0:
            self._data['cfdi33']['addendas'] = ' '.join(addendas)

    def __transform_related_cfdi(self, elem) -> None:
        self._data['cfdi33']['cfdis_relacionados'] = [] if 'cfdis_relacionados' not in self._data['cfdi33'] else self._data['cfdi33']['cfdis_relacionados']
        for related_cfdi in elem.getchildren():
            self._data['cfdi33']['cfdis_relacionados'].append(
                {
                    'uuid': str(related_cfdi.attrib.get('UUID')).upper(),
                    'tipo_relacion': elem.attrib.get('TipoRelacion')
                }
            )