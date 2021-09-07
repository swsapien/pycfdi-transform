class BaseHandler():
    def __init__(self, empty_char = ''):
        self._empty_char = empty_char
        self._version = self._empty_char
        self._serie = self._empty_char
        self._folio = self._empty_char
        self._fecha = self._empty_char
        self._no_certificado = self._empty_char
        self._subtotal = self._empty_char
        self._descuento = self._empty_char
        self._total = self._empty_char
        self._moneda = self._empty_char
        self._tipo_cambio = self._empty_char
        self._tipo_comprobante = self._empty_char
        self._metodo_pago = self._empty_char
        self._forma_pago = self._empty_char
        self._condiciones_pago = self._empty_char
        self._lugar_expedicion = self._empty_char

        self._rfc_emisor = self._empty_char
        self._nombre_emisor = self._empty_char
        self._regimen_fiscal_emisor = self._empty_char

        self._rfc_receptor = self._empty_char
        self._nombre_receptor = self._empty_char
        self._residencia_fiscal_receptor = self._empty_char
        self._num_reg_id_trib_receptor = self._empty_char
        self._uso_cfdi_receptor = self._empty_char

        self._clave_prod_serv = self._empty_char

        self._iva_traslado = self._empty_char
        self._ieps_traslado = self._empty_char
        self._total_impuestos_traslado = self._empty_char
        self._isr_retenido = self._empty_char
        self._iva_retenido = self._empty_char
        self._ieps_retenido = self._empty_char
        self._total_impuestos_retenidos = self._empty_char
        self._total_traslados_impuestos_locales = self._empty_char
        self._total_retenciones_impuestos_locales = self._empty_char

        self._complementos = self._empty_char

        self._tfds = list()
        self._uuid = self._empty_char
        self._fecha_timbrado = self._empty_char
        self._rfc_prov_cert = self._empty_char
        self._sello_cfd = self._empty_char

        self._addendas = self._empty_char

    def concatenate(self, text, to_add):
        if (text == '' or text == self._empty_char):
            text = to_add
        else:
            text = f'{text}, {to_add}'
        return text
    @staticmethod
    def remove_breaks(value):
        return value.strip().replace("\n","").replace('"',"").replace("\r","").replace("&#xA;","").replace("&#xD;","").replace("~","")
    def sum(self, value, to_add):
        if (value == '' or value == self._empty_char):
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
