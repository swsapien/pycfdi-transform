class BaseHandler():
    def __init__(self):
        self._version = '-'
        self._serie = '-'
        self._folio = '-'
        self._fecha = '-'
        self._no_certificado = '-'
        self._subtotal = '-'
        self._descuento = '-'
        self._total = '-'
        self._moneda = '-'
        self._tipo_cambio = '-'
        self._tipo_comprobante = '-'
        self._metodo_pago = '-'
        self._forma_pago = '-'
        self._condiciones_pago = '-'
        self._lugar_expedicion = '-'

        self._rfc_emisor = '-'
        self._nombre_emisor = '-'
        self._regimen_fiscal_emisor = '-'

        self._rfc_receptor = '-'
        self._nombre_receptor = '-'
        self._residencia_fiscal_receptor = '-'
        self._num_reg_id_trib_receptor = '-'
        self._uso_cfdi_receptor = '-'

        self._clave_prod_serv = '-'

        self._iva_traslado = '-'
        self._ieps_traslado = '-'
        self._total_impuestos_traslado = '-'
        self._isr_retenido = '-'
        self._iva_retenido = '-'
        self._ieps_retenido = '-'
        self._total_impuestos_retenidos = '-'
        self._total_traslados_impuestos_locales = '-'
        self._total_retenciones_impuestos_locales = '-'

        self._complementos = '-'

        self._tfds = list()
        self._uuid = '-'
        self._fecha_timbrado = '-'
        self._rfc_prov_cert = '-'
        self._sello_cfd = '-'

        self._addendas = '-'

    def concatenate(self, text, to_add):
        if (text == '' or text == '-'):
            text = to_add
        else:
            text = f'{text}, {to_add}'
        return text

    def sum(self, value, to_add):
        if (value == '' or value == '-'):
            value = to_add
        else:
            value = str(float(value) + float(to_add))
        return value
    
    def get_result(self):
        result = list()
        for tfd in self._tfds:
            result.append(
                [
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
                self._residencia_fiscal_receptor,
                self._num_reg_id_trib_receptor,
                self._uso_cfdi_receptor,
                self._clave_prod_serv,
                self._iva_traslado,
                self._ieps_traslado,
                self._total_impuestos_traslado,
                self._isr_retenido,
                self._iva_retenido,
                self._ieps_retenido,
                self._total_impuestos_retenidos,
                self._total_traslados_impuestos_locales,
                self._total_retenciones_impuestos_locales,
                self._complementos,
                tfd['UUID'],
                tfd['FechaTimbrado'],
                tfd['RfcProvCertif'],
                tfd['SelloCFD']
                ]
            )
        return result
