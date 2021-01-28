import xml.sax
from pycfdi_transform.sax.base32_handler import Base32Handler


class CFDI32Handler (xml.sax.ContentHandler, Base32Handler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        Base32Handler.__init__(self)
        self._start_concept = False
        self._start_complement = False
        self._complement_profundity = 0
        
    def startElement(self, tag, attrs):
        if (tag == 'cfdi:Comprobante'):
            Base32Handler.transform_comprobante(self, tag, attrs)
        elif (tag == 'cfdi:Emisor'):
            self._start_emisor = True
            Base32Handler.transform_emisor(self, tag, attrs)
        elif (tag == 'cfdi:RegimenFiscal' and self._start_emisor):
            Base32Handler.transform_regimen_fiscal(self, tag, attrs)
        elif (tag == 'cfdi:Receptor'):
            Base32Handler.transform_receptor(self, tag, attrs)
        elif (tag == 'cfdi:Concepto'):
            self._start_concept = True
            self.__transform_conceptos(tag, attrs)
        elif (tag == 'cfdi:Impuestos' and self._start_concept == False):
             self.__transform_impuestos(tag, attrs)
        elif (tag == 'cfdi:Traslado' and self._start_concept == False):
            self.__transform_impuestos_traslados(tag, attrs)
        elif (tag == 'cfdi:Retencion' and self._start_concept == False):
            self.__transform_impuestos_retenciones(tag, attrs)
        elif (tag == 'cfdi:Complemento'):
            self._start_complement = True
        elif (tag == 'tfd:TimbreFiscalDigital'):
            self._complement_profundity += 1
            Base32Handler.transform_tfd(self, tag, attrs)
        elif (tag == 'implocal:ImpuestosLocales'):
            self._complement_profundity += 1
            self.__transform_imploc(tag, attrs)
        elif (self._start_complement):
            self._complement_profundity += 1
            
    def endElement(self, tag):
        if (tag == 'cfdi:Concepto'):
            self._start_concept = False
        elif (tag == 'cfdi:Emisor'):
            self._start_emisor = False
        elif (tag == 'cfdi:Complemento'):
            self._start_complement = False
        elif (self._start_complement):
            self._complement_profundity -= 1
            if(self._complement_profundity == 0):
                self.__transform_complementos(tag)

    def __transform_conceptos(self, tag, attrs):
        if ('noIdentificacion' in attrs):
            self._clave_prod_serv = Base32Handler.concatenate(self, 
                self._clave_prod_serv, attrs['noIdentificacion'].replace('|', ''))

    def __transform_impuestos(self, tag, attrs):
        if ('totalImpuestosTrasladados' in attrs):
            self._total_impuestos_traslado = Base32Handler.sum(self, 
                self._total_impuestos_traslado, attrs['totalImpuestosTrasladados'])
        if ('totalImpuestosRetenidos' in attrs):
            self._total_impuestos_retenidos = Base32Handler.sum(self, 
                self._total_impuestos_retenidos, attrs['totalImpuestosRetenidos'])
        
    def __transform_impuestos_traslados(self, tag, attrs):
        if ('impuesto' in attrs and 'importe' in attrs):
            if (attrs['impuesto'] == 'IVA'):
                self._iva_traslado = Base32Handler.sum(self, self._iva_traslado, attrs['importe'])
            elif (attrs['impuesto'] == 'IEPS'):
                self._ieps_traslado = Base32Handler.sum(self, self._ieps_traslado, attrs['importe'])
    
    def __transform_impuestos_retenciones(self, tag, attrs):
        if ('impuesto' in attrs and 'importe' in attrs):
            if(attrs['impuesto'] == 'ISR'):
                self._isr_retenido = Base32Handler.sum(self, self._isr_retenido , attrs['importe'])
            elif (attrs['impuesto'] == 'IVA'):
                self._iva_retenido = Base32Handler.sum(self, self._iva_retenido, attrs['importe'])

    def __transform_complementos(self, tag):
        complement_name = tag
        if (':' in tag):
            complement_name = tag[tag.rindex(':') + 1:]
        self._complementos = Base32Handler.concatenate(self, self._complementos, complement_name)
    
    def __transform_imploc(self, tag, attrs):
        if ('TotaldeTraslados' in attrs):
            self._total_traslados_impuestos_locales = Base32Handler.sum(self, self._total_traslados_impuestos_locales, attrs['TotaldeTraslados'])
        if ('TotaldeRetenciones' in attrs):
            self._total_retenciones_impuestos_locales = Base32Handler.sum(self, self._total_retenciones_impuestos_locales, attrs['TotaldeRetenciones'])
