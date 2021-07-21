import xml.sax
from pycfdi_transform.sax.base32_handler import Base32Handler
from pycfdi_transform.sax.base33_handler import Base33Handler

class Pagos10Handler (xml.sax.ContentHandler, Base32Handler, Base33Handler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        Base32Handler.__init__(self)
        Base33Handler.__init__(self)
        self._complemento_pago_counter = 1
        self._pago_counter = 1
        self._doc_relacionado_counter = 1

        self._doctos_relacionados = list()
        self._pagos = list()

        self.p_iva_traslado = '-'
        self.p_ieps_traslado = '-'
        self.p_total_impuestos_trasladados = '-'
        self.p_isr_retencion = '-'
        self.p_iva_retencion = '-'
        self.p_iesp_retencion = '-'
        self.p_total_impuestos_retenidos = '-'


    def startElement(self, tag, attrs):
        if (tag == 'cfdi:Comprobante'):
            if ('Version' in attrs):
                Base33Handler.transform_comprobante(self, tag, attrs)
            elif ('version' in attrs):
                Base32Handler.transform_comprobante(self, tag, attrs)
        elif (tag == 'cfdi:Emisor'):
            if (self._version == '3.3'):
                Base33Handler.transform_emisor(self, tag, attrs)
            else:
                self._start_emisor = True
                Base32Handler.transform_emisor(self, tag, attrs)
        elif (tag == 'cfdi:Receptor'):
            if (self._version == '3.3'):
                Base33Handler.transform_receptor(self, tag, attrs)
            else:
                Base32Handler.transform_receptor(self, tag, attrs)
        elif (tag == 'cfdi:RegimenFiscal' and self._start_emisor and self._version == '3.2'):
            Base32Handler.transform_regimen_fiscal(self, tag, attrs)
        elif (tag == 'tfd:TimbreFiscalDigital'):
            if (self._version == '3.3'):
                Base33Handler.transform_tfd(self, tag, attrs)
            else:
                Base32Handler.transform_tfd(self, tag, attrs)
        elif (tag == 'pago10:Pago'):
            self.__transform_pago(tag, attrs)
        elif (tag == 'pago10:DoctoRelacionado'):
            self.__transform_docto_relacionado(tag, attrs)
            
    def endElement(self, tag):
        if (tag == 'cfdi:Emisor'):
            self._start_emisor = False
        elif (tag == 'pago10:Pago'):
            self._doc_relacionado_counter = 1
            self._pago_counter += 1
        elif (tag == 'pago10:Pagos'):
            self._doc_relacionado_counter = 1
            self._pago_counter = 1
            self._complemento_pago_counter += 1
        elif (tag == 'pago10:DoctoRelacionado'):
            self._doc_relacionado_counter += 1

    def __transform_pago(self, tag, attrs):
        p_fecha_pago = attrs['FechaPago']
        p_forma_pago = attrs['FormaDePagoP']
        p_moneda_pago = attrs['MonedaP']
        p_monto = attrs['Monto']
        p_tipo_cambio = '-'
        p_num_operacion = '-'
        p_rfc_emisor_cta_ord = '-'
        p_nom_banco_ord_ext = '-'
        p_cta_ordenante = '-'
        p_rfc_emisor_cta_ben = '-'
        p_cta_beneficiario = '-'
        if ('TipoCambioP' in attrs):
            p_tipo_cambio = attrs['TipoCambioP']
        if ('NumOperacion' in attrs):
            p_num_operacion = attrs['NumOperacion']
        if ('RfcEmisorCtaOrd' in attrs):
            p_rfc_emisor_cta_ord = attrs['RfcEmisorCtaOrd']
        if ('NomBancoOrdExt' in attrs):
            p_nom_banco_ord_ext = attrs['NomBancoOrdExt']
        if ('CtaOrdenante' in attrs):
            p_cta_ordenante = attrs['CtaOrdenante']
        if ('RfcEmisorCtaBen' in attrs):
            p_rfc_emisor_cta_ben = attrs['RfcEmisorCtaBen']
        if ('CtaBeneficiario' in attrs):
            p_cta_beneficiario = attrs['CtaBeneficiario']
        pago = {
            'p_fecha_pago': p_fecha_pago,
            'p_forma_pago': p_forma_pago,
            'p_moneda_pago': p_moneda_pago,
            'p_tipo_cambio': p_tipo_cambio,
            'p_monto': p_monto,
            'p_num_operacion': p_num_operacion,
            'p_rfc_emisor_cta_ord': p_rfc_emisor_cta_ord,
            'p_nom_banco_ord_ext': p_nom_banco_ord_ext,
            'p_cta_ordenante': p_cta_ordenante,
            'p_rfc_emisor_cta_ben': p_rfc_emisor_cta_ben,
            'p_cta_beneficiario': p_cta_beneficiario
        }
        self._pagos.append(pago)
    
    def __transform_docto_relacionado(self, tag, attrs):
        p_identificador_pago = f'CP{str(self._complemento_pago_counter)}_P{str(self._pago_counter)}_DR{str(self._doc_relacionado_counter)}'
        p_dr_id_documento = attrs['IdDocumento']
        p_dr_serie = '-'
        p_dr_folio = '-'
        p_dr_monedadr = attrs['MonedaDR']
        p_dr_tipo_cambiodr = '-'
        p_dr_metodo_pagodr = attrs['MetodoDePagoDR']
        p_dr_num_parcialidaddr = '-'
        p_dr_imp_saldo_ant = '-'
        p_dr_imp_pagado = '-'
        p_dr_imp_saldo_insoluto = '-'
        if ('Serie' in attrs):
            p_dr_serie = attrs['Serie']
        if ('Folio' in attrs):
            p_dr_folio = attrs['Folio']
        if ('TipoCambioDR' in attrs):
            p_dr_tipo_cambiodr = attrs['TipoCambioDR']
        if ('NumParcialidad' in attrs):
            p_dr_num_parcialidaddr = attrs['NumParcialidad']
        if ('ImpSaldoAnt' in attrs):
            p_dr_imp_saldo_ant = attrs['ImpSaldoAnt']
        if ('ImpPagado' in attrs):
            p_dr_imp_pagado = attrs['ImpPagado']
        if ('ImpSaldoInsoluto' in attrs):
            p_dr_imp_saldo_insoluto = attrs['ImpSaldoInsoluto']
        
        docto = {
            'pago': self._pago_counter,
                'p_identificador_pago': p_identificador_pago,
                'p_dr_id_documento': p_dr_id_documento,
                'p_dr_serie': p_dr_serie,
                'p_dr_folio': p_dr_folio,
                'p_dr_monedadr': p_dr_monedadr,
                'p_dr_tipo_cambiodr': p_dr_tipo_cambiodr,
                'p_dr_metodo_pagodr': p_dr_metodo_pagodr,
                'p_dr_num_parcialidaddr': p_dr_num_parcialidaddr,
                'p_dr_imp_saldo_ant': p_dr_imp_saldo_ant,
                'p_dr_imp_pagado': p_dr_imp_pagado,
                'p_dr_imp_saldo_insoluto': p_dr_imp_saldo_insoluto
                }
        self._doctos_relacionados.append(docto)

    def get_result(self):
        list_result = list()
        for tfd in self._tfds:
            if len(self._doctos_relacionados) < 1:
                for p in range(len(self._pagos)):
                    docto_empty = {
                            'pago': p + 1,
                            'p_identificador_pago': "",
                            'p_dr_id_documento': "00000000-0000-0000-0000-000000000000",
                            'p_dr_serie': "",
                            'p_dr_folio': "",
                            'p_dr_monedadr': "",
                            'p_dr_tipo_cambiodr': 0,
                            'p_dr_metodo_pagodr': "",
                            'p_dr_num_parcialidaddr': 0,
                            'p_dr_imp_saldo_ant': 0,
                            'p_dr_imp_pagado': 0,
                            'p_dr_imp_saldo_insoluto': 0
                            }
                    self._doctos_relacionados.append(docto_empty)
            for docto in self._doctos_relacionados:
                pago = self._pagos[docto['pago'] - 1]
                list_result.append([
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
                    tfd['RfcProvCertif'],
                    tfd['SelloCFD'],
                    docto['p_identificador_pago'],
                    pago['p_fecha_pago'],
                    pago['p_forma_pago'],
                    pago['p_moneda_pago'],
                    pago['p_tipo_cambio'],
                    pago['p_monto'],
                    pago['p_num_operacion'],
                    pago['p_rfc_emisor_cta_ord'],
                    pago['p_nom_banco_ord_ext'],
                    pago['p_cta_ordenante'],
                    pago['p_rfc_emisor_cta_ben'],
                    pago['p_cta_beneficiario'],
                    self.p_iva_traslado,
                    self.p_ieps_traslado,
                    self.p_total_impuestos_trasladados,
                    self.p_isr_retencion,
                    self.p_iva_retencion,
                    self.p_iesp_retencion,
                    self.p_total_impuestos_retenidos,
                    docto['p_dr_id_documento'],
                    docto['p_dr_serie'],
                    docto['p_dr_folio'],
                    docto['p_dr_monedadr'],
                    docto['p_dr_tipo_cambiodr'],
                    docto['p_dr_metodo_pagodr'],
                    docto['p_dr_num_parcialidaddr'],
                    docto['p_dr_imp_saldo_ant'],
                    docto['p_dr_imp_pagado'],
                    docto['p_dr_imp_saldo_insoluto']
                    ])
        return list_result