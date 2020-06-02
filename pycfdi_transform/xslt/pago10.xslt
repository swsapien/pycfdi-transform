<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet version="2.0" 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
  xmlns:xs="http://www.w3.org/2001/XMLSchema" 
  xmlns:fn="http://www.w3.org/2005/xpath-functions" 
  xmlns:cfdi="http://www.sat.gob.mx/cfd/3" 
  xmlns:cce11="http://www.sat.gob.mx/ComercioExterior11" 
  xmlns:donat="http://www.sat.gob.mx/donat" 
  xmlns:divisas="http://www.sat.gob.mx/divisas" 
  xmlns:implocal="http://www.sat.gob.mx/implocal" 
  xmlns:leyendasFisc="http://www.sat.gob.mx/leyendasFiscales" 
  xmlns:pfic="http://www.sat.gob.mx/pfic" 
  xmlns:tpe="http://www.sat.gob.mx/TuristaPasajeroExtranjero" 
  xmlns:nomina12="http://www.sat.gob.mx/nomina12" 
  xmlns:registrofiscal="http://www.sat.gob.mx/registrofiscal" 
  xmlns:pagoenespecie="http://www.sat.gob.mx/pagoenespecie" 
  xmlns:aerolineas="http://www.sat.gob.mx/aerolineas" 
  xmlns:valesdedespensa="http://www.sat.gob.mx/valesdedespensa" 
  xmlns:consumodecombustibles="http://www.sat.gob.mx/consumodecombustibles" 
  xmlns:notariospublicos="http://www.sat.gob.mx/notariospublicos" 
  xmlns:vehiculousado="http://www.sat.gob.mx/vehiculousado" 
  xmlns:servicioparcial="http://www.sat.gob.mx/servicioparcialconstruccion" 
  xmlns:decreto="http://www.sat.gob.mx/renovacionysustitucionvehiculos" 
  xmlns:destruccion="http://www.sat.gob.mx/certificadodestruccion" 
  xmlns:obrasarte="http://www.sat.gob.mx/arteantiguedades" 
  xmlns:ine="http://www.sat.gob.mx/ine" 
  xmlns:iedu="http://www.sat.gob.mx/iedu" 
  xmlns:ventavehiculos="http://www.sat.gob.mx/ventavehiculos" 
  xmlns:terceros="http://www.sat.gob.mx/terceros" 
  xmlns:pago10="http://www.sat.gob.mx/Pagos" 
  xmlns:detallista="http://www.sat.gob.mx/detallista" 
  xmlns:ecc12="http://www.sat.gob.mx/EstadoDeCuentaCombustible12" 
  xmlns:consumodecombustibles11="http://www.sat.gob.mx/ConsumoDeCombustibles11" 
  xmlns:gceh="http://www.sat.gob.mx/GastosHidrocarburos10" 
  xmlns:ieeh="http://www.sat.gob.mx/IngresosHidrocarburos10" 
  xmlns:tfd="http://www.sat.gob.mx/TimbreFiscalDigital">

  <xsl:include href="utilerias.xslt" />
  <xsl:include href="common_cfdi.xslt" />
  <xsl:key name="Impuestos-Traslados" match="/cfdi:Comprobante/cfdi:Complemento/pago10:Pagos/pago10:Pago/pago10:Impuestos/pago10:Traslados/pago10:Traslado" use="@Impuesto" />
  <xsl:key name="Impuestos-Retenciones" match="/cfdi:Comprobante/cfdi:Complemento/pago10:Pagos/pago10:Pago/pago10:Impuestos/pago10:Retenciones/pago10:Retencion" use="@Impuesto" />
  <!-- Con el siguiente método se establece que la salida deberá ser en texto -->
  <xsl:output method="text" version="1.0" encoding="UTF-8" indent="no" />
  <xsl:template match="/">
    <xsl:if test="/cfdi:Comprobante/cfdi:Complemento/pago10:Pagos/pago10:Pago">
      <xsl:for-each select="/cfdi:Comprobante/cfdi:Complemento/pago10:Pagos">
        <xsl:variable name="positionPagos" select="position()" />
        <xsl:apply-templates select=".">
          <xsl:with-param name="positionPagos" select="$positionPagos"/>
        </xsl:apply-templates>
      </xsl:for-each>

    </xsl:if>
  </xsl:template>

  <xsl:template match="tfd:TimbreFiscalDigital" mode="v11UUID">
    <xsl:call-template name="ToUpperCase">
      <xsl:with-param name="valor" select="./@UUID" />
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="pago10:Pagos">
    <xsl:param name="positionPagos"/>
    <xsl:for-each select="pago10:Pago">
      <xsl:variable name="positionPago" select="position()" />
      <xsl:apply-templates select="." mode="pago10general">
        <xsl:with-param name="positionPagos" select="$positionPagos"/>
        <xsl:with-param name="positionPago" select="$positionPago"/>
      </xsl:apply-templates>
    </xsl:for-each>

  </xsl:template>


  <xsl:template match="pago10:Pago" mode="pago10general">
    <xsl:param name="positionPagos"/>
    <xsl:param name="positionPago"/>
    <xsl:for-each select="pago10:DoctoRelacionado">
      <xsl:variable name="positionDR" select="position()" />
      <xsl:variable name="idPago" select="concat('CP',$positionPagos,'_P',$positionPago,'_DR',$positionDR)" />
      <xsl:text>&#8225;&#8225;</xsl:text>
      <!-- Cfdi General -->
      <xsl:apply-templates select="/cfdi:Comprobante[1]" mode="v33" />
      <!-- TimbreFiscalDigital -->
      <xsl:apply-templates select="/cfdi:Comprobante/cfdi:Complemento/tfd:TimbreFiscalDigital[1]" mode="v11" />
      <xsl:if test="not(/cfdi:Comprobante/cfdi:Complemento/tfd:TimbreFiscalDigital[1])">
          <xsl:call-template name="block-generator">
              <xsl:with-param name="N" select="4"/>
          </xsl:call-template>
      </xsl:if>
      <!-- P_IDENTIFICADOR_PAGO -->
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="$idPago" />
      </xsl:call-template>
      <!-- PAGO_DATA_DETAIL -->
      <xsl:apply-templates select="ancestor::pago10:Pago" mode="pago10detail"/>
      <!-- PAGO_DOCTOREL_DATA_DETAIL -->
      <xsl:apply-templates select="." />
    </xsl:for-each>
  </xsl:template>
  <xsl:template match="pago10:Pago" mode="pago10detail">
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@FechaPago" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@FormaDePagoP" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@MonedaP" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@TipoCambioP" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@Monto" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@NumOperacion" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@RfcEmisorCtaOrd" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@NomBancoOrdExt" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@CtaOrdenante" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@RfcEmisorCtaBen" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@CtaBeneficiario" />
    </xsl:call-template>
    <xsl:apply-templates select="pago10:Impuestos" />
    <xsl:if test="not(pago10:Impuestos)">
        <xsl:call-template name="block-generator">
            <xsl:with-param name="N" select="7"/>
        </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <xsl:template match="pago10:DoctoRelacionado">
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@IdDocumento" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@Serie" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@Folio" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@MonedaDR" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@TipoCambioDR" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@MetodoDePagoDR" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@NumParcialidad" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@ImpSaldoAnt" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@ImpPagado" />
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@ImpSaldoInsoluto" />
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="pago10:Impuestos">
        <xsl:apply-templates select="./pago10:Traslados"/>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@TotalImpuestosTrasladados"/>
        </xsl:call-template>
        <xsl:apply-templates select="./pago10:Retenciones"/>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@TotalImpuestosRetenidos"/>
        </xsl:call-template>
    </xsl:template>
    <xsl:template match="pago10:Traslados">
        <xsl:apply-templates select="pago10:Traslado[generate-id() = generate-id(key('Impuestos-Traslados', '002')[1])]" />
        <xsl:if test="not(key('Impuestos-Traslados', '002')[1])">
            <xsl:call-template name="Requerido">
                <xsl:with-param name="valor"/>
            </xsl:call-template>
        </xsl:if>
        <xsl:apply-templates select="pago10:Traslado[generate-id() = generate-id(key('Impuestos-Traslados', '003')[1])]" />
        <xsl:if test="not(key('Impuestos-Traslados', '003')[1])">
            <xsl:call-template name="Requerido">
                <xsl:with-param name="valor"/>
            </xsl:call-template>
        </xsl:if>
    </xsl:template>
    <xsl:template match="pago10:Traslado">
        <!-- Sum all the elements from the @Impuesto group -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="format-number(sum(key('Impuestos-Traslados', @Impuesto)/@Importe), '0.00')"/>
        </xsl:call-template>
    </xsl:template>

    <xsl:template match="pago10:Retenciones">
        <xsl:apply-templates select="pago10:Retencion[generate-id() = generate-id(key('Impuestos-Retenciones', '001')[1])]" />
        <xsl:if test="not(key('Impuestos-Retenciones', '001')[1])">
            <xsl:call-template name="Requerido">
                <xsl:with-param name="valor"/>
            </xsl:call-template>
        </xsl:if>
        <xsl:apply-templates select="pago10:Retencion[generate-id() = generate-id(key('Impuestos-Retenciones', '002')[1])]" />
        <xsl:if test="not(key('Impuestos-Retenciones', '002')[1])">
            <xsl:call-template name="Requerido">
                <xsl:with-param name="valor"/>
            </xsl:call-template>
        </xsl:if>
        <xsl:apply-templates select="pago10:Retencion[generate-id() = generate-id(key('Impuestos-Retenciones', '003')[1])]" />
        <xsl:if test="not(key('Impuestos-Retenciones', '003')[1])">
            <xsl:call-template name="Requerido">
                <xsl:with-param name="valor"/>
            </xsl:call-template>
        </xsl:if>
    </xsl:template>
    <xsl:template match="pago10:Retencion">
        <!-- Sum all the elements from the @Impuesto group -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="format-number(sum(key('Impuestos-Retenciones', @Impuesto)/@Importe), '0.00')"/>
        </xsl:call-template>
    </xsl:template>

</xsl:stylesheet>
