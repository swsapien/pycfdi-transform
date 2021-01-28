from pycfdi_transform.sax.base_handler import BaseHandler


class Base33Handler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)
    
    def transform_comprobante(self, tag, attrs):
        self._version = attrs['Version']
        if ('Serie' in attrs):
            self._serie = attrs['Serie']
        if ('Folio' in attrs):
            self._folio = attrs['Folio']
        self._fecha = attrs['Fecha']
        self._no_certificado = attrs['NoCertificado']
        self._subtotal = attrs['SubTotal']
        if ('Descuento' in attrs):
            self._descuento = attrs['Descuento']
        self._total = attrs['Total']
        self._moneda = attrs['Moneda']
        if ('TipoCambio' in attrs):
            self._tipo_cambio = attrs['TipoCambio']
        self._tipo_comprobante = attrs['TipoDeComprobante']
        if ('MetodoPago' in attrs):
            self._metodo_pago = attrs['MetodoPago']
        if ('FormaPago' in attrs):
            self._forma_pago = attrs['FormaPago']
        if ('CondicionesDePago' in attrs):
            self._condiciones_pago = attrs['CondicionesDePago']
        self._lugar_expedicion = attrs['LugarExpedicion']
    
    def transform_emisor(self, tag, attrs):
        self._rfc_emisor = attrs['Rfc']
        if ('Nombre' in attrs):
            self._nombre_emisor = attrs['Nombre']
        self._regimen_fiscal_emisor = attrs['RegimenFiscal']

    def transform_receptor(self, tag, attrs):
        self._rfc_receptor = attrs['Rfc']
        if ('Nombre' in attrs):
            self._nombre_receptor = attrs['Nombre']
        if ('ResidenciaFiscal' in attrs):
            self._residencia_fiscal_emisor = attrs['ResidenciaFiscal']
        if ('NumRegIdTrib' in attrs):
            self._noum_reg_id_trib_receptor = attrs['NumRegIdTrib']
        self._uso_cfdi_receptor = attrs['UsoCFDI']
    
    def transform_tfd(self, tag, attrs):
        self._tfds.append( 
            {
            'UUID': str(attrs['UUID']).upper(),
            'FechaTimbrado': attrs['FechaTimbrado'],
            'RfcProvCertif': attrs['RfcProvCertif'],
            'SelloCFD': attrs['SelloCFD']
            }
        )
