
from __future__ import annotations
from pycfdi_transform.v2.sax.cfdi33.base_handler import BaseHandler
from pycfdi_transform.v2.helpers.string_helper import StringHelper
from lxml import etree
import logging

class SAXHandler(BaseHandler):
    def __init__(self, empty_char='', safe_numerics=False) -> SAXHandler:
        super().__init__(empty_char, safe_numerics)
        self._logger = logging.getLogger('SAXHandler')
        self._inside_concepts = False
    
    def transform_from_file(self, file_path:str) -> object:
        if ('.xml' in file_path):
            try:
                xml_parser = etree.XMLParser(encoding='utf-8', recover=True)
                tree = etree.XML(StringHelper.file_path_to_string(file_path).encode(), parser=xml_parser)
                context = etree.iterwalk(tree, events=("start", "end"))
                self.__handle_events(context)
                return self._data
            except Exception as ex:
                self._logger.exception(f'Caugth Exception at tranforming file {file_path}.')
                raise ex
        else:
            raise ValueError('Incorrect type of document, only support XML files')
    def transform_from_string(self, xml_str:str) -> object:
        try:
            xml_parser = etree.XMLParser(encoding='utf-8', recover=True)
            tree = etree.XML(xml_str.encode(), parser=xml_parser)
            context = etree.iterwalk(tree, events=("start", "end"))
            self.__handle_events(context)
            return self._data
        except Exception as ex:
            self._logger.exception(f'Caugth Exception at tranforming xml string.')
            raise ex

    def __handle_events(self, context:etree.iterwalk) -> None:
        for action, elem in context:
            print(f"{elem.tag} - {action}")
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
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Concepto' and self._config['concepts']:
                    self.__transform_concept(elem)
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Impuestos' and not self._inside_concepts:
                    self.__transform_general_taxes(elem)
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Complemento':
                    self.__transform_complement(elem)
                elif elem.tag == '{http://www.sat.gob.mx/cfd/3}Addenda':
                    self.__transform_addenda(elem)

    def __transform_comprobante(self, element:etree._Element) -> None:
        if not 'Version' in element.attrib or element.attrib['Version'] != '3.3':
            raise ValueError('Incorrect type of CFDI, this handler only support CFDI version 3.3')
        self._data['cfdi33']['version'] = element.attrib['Version']
        if ('Serie' in element.attrib):
            self._data['cfdi33']['serie'] = element.attrib['Serie']
        if ('Folio' in element.attrib):
            self._data['cfdi33']['folio'] = element.attrib['Folio']
        self._data['cfdi33']['fecha'] = element.attrib['Fecha']
        self._data['cfdi33']['no_certificado'] = element.attrib['NoCertificado']
        self._data['cfdi33']['subtotal'] = element.attrib['SubTotal']
        if ('Descuento' in element.attrib):
            self._data.cfdi33['cfdi33']['descuento'] = element.attrib['Descuento']
        self._data['cfdi33']['total'] = element.attrib['Total']
        self._data['cfdi33']['moneda'] = element.attrib['Moneda']
        if ('TipoCambio' in element.attrib):
            self._data['cfdi33']['tipo_cambio'] = element.attrib['TipoCambio']
        self._data['cfdi33']['tipo_comprobante'] = element.attrib['TipoDeComprobante']
        if ('MetodoPago' in element.attrib):
            self._data['cfdi33']['metodo_pago'] = element.attrib['MetodoPago']
        if ('FormaPago' in element.attrib):
            self._data['cfdi33']['forma_pago'] = element.attrib['FormaPago']
        if ('CondicionesDePago' in element.attrib):
            self._data['cfdi33']['condiciones_pago'] = StringHelper.compact_string(element.attrib['CondicionesDePago'])
        self._data['cfdi33']['lugar_expedicion'] = element.attrib['LugarExpedicion']
    
    def __transform_emisor(self, element:etree._Element) -> None:
        self._data['cfdi33']['rfc_emisor'] = element.attrib['Rfc']
        if ('Nombre' in element.attrib):
            self._data['cfdi33']['nombre_emisor'] = StringHelper.compact_string(element.attrib['Nombre'])
        self._data['cfdi33']['regimen_fiscal_emisor'] = element.attrib['RegimenFiscal']

    def __transform_receptor(self, element:etree._Element) -> None:
        self._data['cfdi33']['rfc_receptor'] = element.attrib['Rfc']
        if ('Nombre' in element.attrib):
            self._data['cfdi33']['nombre_receptor'] = StringHelper.compact_string(element.attrib['Nombre'])
        if ('ResidenciaFiscal' in element.attrib):
            self._data['cfdi33']['residencia_fiscal_receptor'] = element.attrib['ResidenciaFiscal']
        if ('NumRegIdTrib' in element.attrib):
            self._data['cfdi33']['num_reg_id_trib_receptor'] = element.attrib['NumRegIdTrib']
        self._data['cfdi33']['uso_cfdi_receptor'] = element.attrib['UsoCFDI']
    
    def __transform_concept(self, element:etree._Element) -> None:
        concept = {
            'clave_prod_serv': element.attrib['ClaveProdServ'],
            'no_identificacion': element.attrib['NoIdentificacion'] if 'NoIdentificacion' in element.attrib else self._config['empty_char'],
            'cantidad': element.attrib['Cantidad'],
            'clave_unidad': element.attrib['ClaveUnidad'],
            'unidad': element.attrib['Unidad'] if 'Unidad' in element.attrib else self._config['empty_char'],
            'descripcion': StringHelper.compact_string(element.attrib['Descripcion']),
            'valor_unitario': element.attrib['ValorUnitario'],
            'importe': element.attrib['Importe'],
            'descuento': element.attrib['Descuento'] if 'Descuento' in element.attrib else (StringHelper.DEFAULT_SAFE_NUMBER_CERO if self._config['safe_numerics'] else self._config['empty_char']),
        }
        self._data['cfdi33']['conceptos'].append(concept)
    
    def __transform_general_taxes(self, element:etree._Element) -> None:
        if ('TotalImpuestosTrasladados' in element.attrib):
            self._data['cfdi33']['total_impuestos_traslados'] = element.attrib['TotalImpuestosTrasladados']
        if ('TotalImpuestosRetenidos' in element.attrib):
            self._data['cfdi33']['total_impuestos_retenidos'] = element.attrib['TotalImpuestosRetenidos']
        for child in element.getchildren():
            if child.tag == '{http://www.sat.gob.mx/cfd/3}Traslados':
                self.__transform_taxes_traslados(child.getchildren())
            elif child.tag == '{http://www.sat.gob.mx/cfd/3}Retenciones':
                self.__transform_taxes_retenciones(child.getchildren())

    def __transform_taxes_traslados(self, list_elements:list) -> None:
        for traslado in list_elements:
            if traslado.attrib['Impuesto'] == '002':
                #IVA
                self._data['cfdi33']['iva_traslado'] = StringHelper.sum_strings(self._data['cfdi33']['iva_traslado'], traslado.attrib['Importe'])
            elif traslado.attrib['Impuesto'] == '003':
                #IEPS
                self._data['cfdi33']['ieps_traslado'] = StringHelper.sum_strings(self._data['cfdi33']['ieps_traslado'], traslado.attrib['Importe'])

    def __transform_taxes_retenciones(self, list_elements:list) -> None:
        for retencion in list_elements:
            if retencion.attrib['Impuesto'] == '001':
                #ISR
                self._data['cfdi33']['isr_retenido'] = StringHelper.sum_strings(self._data['cfdi33']['isr_retenido'], retencion.attrib['Importe'])
            elif retencion.attrib['Impuesto'] == '002':
                #IVA
                self._data['cfdi33']['iva_retenido'] = StringHelper.sum_strings(self._data['cfdi33']['iva_retenido'], retencion.attrib['Importe'])
            elif retencion.attrib['Impuesto'] == '003':
                #IEPS
                self._data['cfdi33']['ieps_retenido'] = StringHelper.sum_strings(self._data['cfdi33']['ieps_retenido'], retencion.attrib['Importe'])
    
    def __transform_complement(self, element:etree._Element) -> None:
        complements = []
        for complement in element.getchildren():
            # Transform complement
            if complement.tag in self._complements:
                transformer = self._complements[complement.tag]['class']()
                complement_data = transformer.transform_from_string(etree.tostring(complement))
                if not self._complements[complement.tag]['key'] in self._data:
                    self._data[self._complements[complement.tag]['key']] = []
                self._data[self._complements[complement.tag]['key']].append(complement_data)
            # Annotate in complement list
            try:
                qname = etree.QName(complement.tag)
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
                addendas.append(qname.localname)
            except Exception:
                addendas.append(str(addenda.tag))
        if len(addendas) > 0:
            self._data['cfdi33']['addendas'] = ' '.join(addendas)