<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
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
    xmlns:tfd="http://www.sat.gob.mx/TimbreFiscalDigital" version="2.0">

    <xsl:include href="utilerias.xslt" />
    <xsl:include href="common_cfdi.xslt" />
    <!-- variables necesarias -->
    <xsl:key name="Impuestos-Traslados" match="/cfdi:Comprobante/cfdi:Conceptos/cfdi:Concepto/cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado" use="@Impuesto" />
    <xsl:key name="Impuestos-Retenciones" match="/cfdi:Comprobante/cfdi:Impuestos/cfdi:Retenciones/cfdi:Retencion" use="@Impuesto" />

    <!-- Con el siguiente método se establece que la salida deberá ser en texto -->
    <xsl:output method="text" version="1.0" encoding="UTF-8" indent="no" />
    <xsl:template match="/">
        <xsl:if test="/cfdi:Comprobante/cfdi:Conceptos">
            <xsl:for-each select="/cfdi:Comprobante/cfdi:Conceptos/cfdi:Concepto">
                <xsl:variable name="positionConcept" select="position()" />
                <xsl:text>&#8225;&#8225;</xsl:text>
                <xsl:apply-templates select=".">
                    <xsl:with-param name="positionConcept" select="$positionConcept" />
                </xsl:apply-templates>
            </xsl:for-each>
        </xsl:if>
    </xsl:template>
    <!-- Concept Detail cfdi 33-->
    <xsl:template match="cfdi:Concepto">
        <xsl:param name="positionConcept"/>
        <xsl:apply-templates select="/cfdi:Comprobante[1]" mode="v33" />
        <!-- TimbreFiscalDigital -->
        <xsl:apply-templates select="/cfdi:Comprobante/cfdi:Complemento/tfd:TimbreFiscalDigital[1]" mode="v11_simple" />
        <xsl:if test="not(/cfdi:Comprobante/cfdi:Complemento/tfd:TimbreFiscalDigital[1])">
            <xsl:call-template name="block-generator">
                <xsl:with-param name="N" select="2"/>
            </xsl:call-template>
        </xsl:if>
        <!-- C_CONCEPT_IDENTIFIER -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="$positionConcept" />
        </xsl:call-template>
        <!-- CONCEPT DETAIL -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@ClaveProdServ" />
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@NoIdentificacion" />
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Cantidad" />
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@ClaveUnidad" />
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Unidad" />
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Descripcion" />
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@ValorUnitario" />
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Descuento" />
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Importe" />
        </xsl:call-template>
    </xsl:template>
</xsl:stylesheet>