from pycfdi_transform.sax.base_handler import BaseHandler


class Base32Handler(BaseHandler):
    def __init__(self):
        self._start_emisor = False
        BaseHandler.__init__(self)

    def transform_comprobante(self, tag, attrs):
        self._version = attrs['version']
        if ('serie' in attrs):
            self._serie = attrs['serie']
        if ('folio' in attrs):
            self._folio = attrs['folio']
        self._fecha = attrs['fecha']
        self._no_certificado = attrs['noCertificado']
        self._subtotal = attrs['subTotal']
        if ('descuento' in attrs):
            self._descuento = attrs['descuento']
        self._total = attrs['total']
        if ('Moneda' in attrs):
            self._moneda = attrs['Moneda'].replace('|', '')
        if ('TipoCambio' in attrs):
            self._tipo_cambio = attrs['TipoCambio']
        if ('tipoDeComprobante' in attrs):
            self._tipo_comprobante = attrs['tipoDeComprobante'].replace(
                '|', '')
        if ('metodoDePago' in attrs):
            self._metodo_pago = attrs['metodoDePago'].replace('|', '')
        if ('formaDePago' in attrs):
            self._forma_pago = attrs['formaDePago'].replace('|', '')
        if ('condicionesDePago' in attrs):
            self._condiciones_pago = attrs['condicionesDePago'].replace(
                '|', '')
        if ('LugarExpedicion' in attrs):
            self._lugar_expedicion = attrs['LugarExpedicion'].replace('|', '')
    
    def transform_emisor(self, tag, attrs):
        self._rfc_emisor = attrs['rfc']
        if ('nombre' in attrs):
            self._nombre_emisor = attrs['nombre'].replace('|', '')
    
    def transform_regimen_fiscal(self, tag, attrs):
        self._regimen_fiscal_emisor = attrs['Regimen']
    
    def transform_receptor(self, tag, attrs):
        self._rfc_receptor = attrs['rfc']
        if ('nombre' in attrs):
            self._nombre_receptor = attrs['nombre']
    
    def transform_tfd(self, tag, attrs):
        rfc_prov_cert = attrs['RfcProvCertif'] if 'RfcProvCertif' in attrs else None
        self._tfds.append( 
            {
            'UUID': str(attrs['UUID']).upper(),
            'FechaTimbrado': attrs['FechaTimbrado'],
            'RfcProvCertif': rfc_prov_cert,
            'SelloCFD': attrs['selloCFD']
            }
        )
    
    
