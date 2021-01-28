import xml.sax
from pycfdi_transform.sax.base32_handler import Base32Handler


class CFDI32DetailHandler (xml.sax.ContentHandler, Base32Handler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        Base32Handler.__init__(self)
        self._position_concept = 0

        self._concepts = list()

    def startElement(self, tag, attrs):
        if (tag == 'cfdi:Comprobante'):
            Base32Handler.transform_comprobante(self, tag, attrs)
        elif (tag == 'cfdi:Emisor'):
            Base32Handler.transform_emisor(self, tag, attrs)
        elif (tag == 'cfdi:Receptor'):
            Base32Handler.transform_receptor(self, tag, attrs)
        elif (tag == 'cfdi:Concepto'):
            self._position_concept += 1
            self.__transform_conceptos(tag, attrs)
        elif (tag == 'tfd:TimbreFiscalDigital'):
            Base32Handler.transform_tfd(self, tag, attrs)

    def __transform_conceptos(self, tag, attrs):
        concepto = {
            'position_concept': str(self._position_concept),
            'clave_pro_serv': '-',
            'no_identificacion': '-',
            'cantidad': '-',
            'clave_unidad': '-',
            'unidad': '-',
            'descripcion': '-',
            'valor_unitario': '-',
            'descuento': '-',
            'importe': '-',
        }
        if ('claveProdServ' in attrs):
            concepto['clave_pro_serv'] = attrs['claveProdServ']
        if ('noIdentificacion' in attrs):
            concepto['no_identificacion'] = attrs['noIdentificacion']
        if ('cantidad' in attrs):
            concepto['cantidad'] = attrs['cantidad']
        if ('claveUnidad' in attrs):
            concepto['clave_unidad'] = attrs['claveUnidad']
        if ('unidad' in attrs):
            concepto['unidad'] = attrs['unidad']
        if ('descripcion' in attrs):
            concepto['descripcion'] = attrs['descripcion']
        if ('valorUnitario' in attrs):
            concepto['valor_unitario'] = attrs['valorUnitario']
        if ('descuento' in attrs):
            concepto['descuento'] = attrs['descuento']
        if ('importe' in attrs):
            concepto['importe'] = attrs['importe']
        self._concepts.append(concepto)

    def get_result(self):
        result_list = list()
        for tfd in self._tfds:
            for concepto in self._concepts:
                result_list.append([
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
                    concepto['position_concept'],
                    concepto['clave_pro_serv'],
                    concepto['no_identificacion'],
                    concepto['cantidad'],
                    concepto['clave_unidad'],
                    concepto['unidad'],
                    concepto['descripcion'],
                    concepto['valor_unitario'],
                    concepto['descuento'],
                    concepto['importe']
                ])
            return result_list

