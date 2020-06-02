<?xml version="1.0" encoding="UTF-8"?>
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

<xsl:include href="utilerias.xslt"/>
<!-- variables necesarias -->
<xsl:key name="Impuestos-Traslados" match="/cfdi:Comprobante/cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado" use="@impuesto" />
<xsl:key name="Impuestos-Retenciones" match="/cfdi:Comprobante/cfdi:Impuestos/cfdi:Retenciones/cfdi:Retencion" use="@impuesto" />

    <!-- Con el siguiente método se establece que la salida deberá ser en texto -->
    <xsl:output method="text" version="1.0" encoding="UTF-8" indent="no"/>    
    <xsl:template match="/">
        <xsl:apply-templates select="/cfdi:Comprobante"/>
    </xsl:template>
    <xsl:template match="cfdi:Comprobante">
        <!-- Iniciamos el tratamiento de los atributos de comprobante -->
        <xsl:call-template name="OnlyData">
            <xsl:with-param name="valor" select="./@version"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">            
            <xsl:with-param name="valor" select="./@serie"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@folio"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@fecha"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@noCertificado"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@subTotal"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@descuento"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@total"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Moneda"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@TipoCambio"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@tipoDeComprobante"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@metodoDePago"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@formaDePago"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@condicionesDePago"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@LugarExpedicion"/>
        </xsl:call-template>        
        <xsl:apply-templates select="./cfdi:Emisor"/>
        <xsl:apply-templates select="./cfdi:Receptor"/>
        <xsl:apply-templates select="./cfdi:Impuestos"/>
        <xsl:if test="not(./cfdi:Impuestos)">
            <!-- if node not exist then add the "-" on the fields TotalImpuestosTraslados & TotalImpuestosRetenidos -->
            <xsl:call-template name="block-generator">
                <xsl:with-param name="N" select="2"/>
            </xsl:call-template>
        </xsl:if>
        <xsl:if test="not(./cfdi:Impuestos/cfdi:Traslados)">
            <!-- if node not exist then add the "-" on the fields IVATraslado & IEPSTraslado -->
            <xsl:call-template name="block-generator">
                <xsl:with-param name="N" select="2"/>
            </xsl:call-template>
        </xsl:if>
        <xsl:if test="not(./cfdi:Impuestos/cfdi:Retenciones)">
            <!-- if node not exist then add the "-" on the fields ISRRetenido, IVARetenido & IEPSRetenido -->
            <xsl:call-template name="block-generator">
                <xsl:with-param name="N" select="3"/>
            </xsl:call-template>
        </xsl:if>
        <!-- Impuestos locales  -->
        <xsl:if test="./cfdi:Complemento/implocal:ImpuestosLocales">
            <xsl:call-template name="Opcional">
                <xsl:with-param name="valor" select="format-number(sum(./cfdi:Complemento/implocal:ImpuestosLocales/@TotaldeTraslados), '0.00')"/>
            </xsl:call-template>
            <xsl:call-template name="Opcional">
                <xsl:with-param name="valor" select="format-number(sum(./cfdi:Complemento/implocal:ImpuestosLocales/@TotaldeRetenciones), '0.00')"/>
            </xsl:call-template>
        </xsl:if>
        <xsl:if test="not(./cfdi:Complemento/implocal:ImpuestosLocales)">
            <xsl:call-template name="block-generator">
                <xsl:with-param name="N" select="2" />
            </xsl:call-template>
        </xsl:if>
        <!-- Complements used -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor">
                <xsl:apply-templates select="./cfdi:Complemento"/>
            </xsl:with-param>
        </xsl:call-template>

        <xsl:apply-templates select="./cfdi:Complemento/tfd:TimbreFiscalDigital"/>
        <xsl:if test="not(./cfdi:Complemento/tfd:TimbreFiscalDigital)">
            <xsl:call-template name="block-generator">
                <xsl:with-param name="N" select="4"/>
            </xsl:call-template>
        </xsl:if>
    </xsl:template>    
    <!--  Manejador de nodos tipo Emisor  -->
    <xsl:template match="cfdi:Emisor">
        <!--Iniciamos el tratamiento de los atributos del Emisor -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@rfc"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@nombre"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./cfdi:RegimenFiscal/@Regimen"/>
        </xsl:call-template>
    </xsl:template>
    <!--  Manejador de nodos tipo Receptor  -->
    <xsl:template match="cfdi:Receptor">
        <!--Iniciamos el tratamiento de los atributos del Receptor -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@rfc"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@nombre"/>
        </xsl:call-template>
        <!-- Call block generator becasuse ResidenciaFiscal, NumRegIdTrib, UsoCFDI does not exist in CFDI 3.2 -->
        <xsl:call-template name="block-generator">
            <xsl:with-param name="N" select="3"/>
        </xsl:call-template>
    </xsl:template>

    <xsl:template match="cfdi:Impuestos">
        <xsl:apply-templates select="./cfdi:Traslados"/>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@totalImpuestosTrasladados"/>
        </xsl:call-template>
        <xsl:apply-templates select="./cfdi:Retenciones"/>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@totalImpuestosRetenidos"/>
        </xsl:call-template>
    </xsl:template>
    <xsl:template match="cfdi:Traslados">
        <xsl:apply-templates select="cfdi:Traslado[generate-id() = generate-id(key('Impuestos-Traslados', 'IVA')[1])]" />
        <xsl:if test="not(key('Impuestos-Traslados', 'IVA')[1])">
            <xsl:call-template name="Requerido"><xsl:with-param name="valor"/></xsl:call-template>
        </xsl:if>
        <xsl:apply-templates select="cfdi:Traslado[generate-id() = generate-id(key('Impuestos-Traslados', 'IEPS')[1])]" />
        <xsl:if test="not(key('Impuestos-Traslados', 'IEPS')[1])">
            <xsl:call-template name="Requerido"><xsl:with-param name="valor"/></xsl:call-template>
        </xsl:if>
    </xsl:template>
    <xsl:template match="cfdi:Traslado">
        <!-- Sum all the elements from the @Impuesto group -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="format-number(sum(key('Impuestos-Traslados', @impuesto)/@importe), '0.00')"/>
        </xsl:call-template>
    </xsl:template>

    <xsl:template match="cfdi:Retenciones">
        <xsl:apply-templates select="cfdi:Retencion[generate-id() = generate-id(key('Impuestos-Retenciones', 'ISR')[1])]" />
        <xsl:if test="not(key('Impuestos-Retenciones', 'ISR')[1])">
            <xsl:call-template name="Requerido"><xsl:with-param name="valor"/></xsl:call-template>
        </xsl:if>
        <xsl:apply-templates select="cfdi:Retencion[generate-id() = generate-id(key('Impuestos-Retenciones', 'IVA')[1])]" />
        <xsl:if test="not(key('Impuestos-Retenciones', 'IVA')[1])">
            <xsl:call-template name="Requerido"><xsl:with-param name="valor"/></xsl:call-template>
        </xsl:if>
        <!-- Fill with - for IEPS because does not exist -->
        <xsl:call-template name="Requerido"><xsl:with-param name="valor"/></xsl:call-template>
    </xsl:template>
    <xsl:template match="cfdi:Retencion">
        <!-- Sum all the elements from the @Impuesto group -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="format-number(sum(key('Impuestos-Retenciones', @impuesto)/@importe), '0.00')"/>
        </xsl:call-template>
    </xsl:template>

    <xsl:template match="cfdi:Complemento">
		<xsl:for-each select="*">
            <xsl:if test="name()">
                <xsl:value-of select="substring-after(name(),':')"/>
                <xsl:if test="position() &lt; last()">,</xsl:if>
            </xsl:if>
        </xsl:for-each>
    </xsl:template>

    <xsl:template match="tfd:TimbreFiscalDigital">
		<xsl:call-template name="ToUpperCase">
			<xsl:with-param name="valor" select="./@UUID"/>
		</xsl:call-template>
		<xsl:call-template name="Requerido">
			<xsl:with-param name="valor" select="./@FechaTimbrado"/>
		</xsl:call-template>
		<xsl:call-template name="Requerido">
			<xsl:with-param name="valor" select="./@RfcProvCertif"/>
		</xsl:call-template>
		<xsl:call-template name="Requerido">
			<xsl:with-param name="valor" select="./@selloCFD"/>
		</xsl:call-template>
    </xsl:template>
</xsl:stylesheet>