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
    xmlns:tfd="http://www.sat.gob.mx/TimbreFiscalDigital" 
    version="2.0">

    <xsl:include href="utilerias.xslt"/>
    <!-- variables necesarias -->
    <xsl:key name="Impuestos-Traslados" match="/cfdi:Comprobante/cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado" use="@Impuesto" />
    <xsl:key name="Impuestos-Retenciones" match="/cfdi:Comprobante/cfdi:Impuestos/cfdi:Retenciones/cfdi:Retencion" use="@Impuesto" />    

    <!-- Con el siguiente método se establece que la salida deberá ser en texto -->
    <xsl:output method="text" version="1.0" encoding="UTF-8" indent="no"/>
    <xsl:template match="/">        
        <xsl:apply-templates select="/cfdi:Comprobante"/>
    </xsl:template>
    <xsl:template match="cfdi:Comprobante">
        <!-- Iniciamos el tratamiento de los atributos de comprobante -->
        <xsl:call-template name="OnlyData">
            <xsl:with-param name="valor" select="./@Version"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Serie"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Folio"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Fecha"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@NoCertificado"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@SubTotal"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Descuento"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Total"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Moneda"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@TipoCambio"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@TipoDeComprobante"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@MetodoPago"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@FormaPago"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@CondicionesDePago"/>
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
            <xsl:with-param name="valor" select="./@Rfc"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Nombre"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@RegimenFiscal"/>
        </xsl:call-template>
    </xsl:template>
    <!--  Manejador de nodos tipo Receptor  -->
    <xsl:template match="cfdi:Receptor">
        <!--Iniciamos el tratamiento de los atributos del Receptor -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Rfc"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Nombre"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@ResidenciaFiscal"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@NumRegIdTrib"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@UsoCFDI"/>
        </xsl:call-template>
    </xsl:template>

    <xsl:template match="cfdi:Impuestos">
        <xsl:apply-templates select="./cfdi:Traslados"/>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@TotalImpuestosTrasladados"/>
        </xsl:call-template>
        <xsl:apply-templates select="./cfdi:Retenciones"/>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@TotalImpuestosRetenidos"/>
        </xsl:call-template>
    </xsl:template>
    <xsl:template match="cfdi:Traslados">
        <xsl:apply-templates select="cfdi:Traslado[generate-id() = generate-id(key('Impuestos-Traslados', '002')[1])]" />
        <xsl:if test="not(key('Impuestos-Traslados', '002')[1])">
            <xsl:call-template name="Requerido">
                <xsl:with-param name="valor"/>
            </xsl:call-template>
        </xsl:if>
        <xsl:apply-templates select="cfdi:Traslado[generate-id() = generate-id(key('Impuestos-Traslados', '003')[1])]" />
        <xsl:if test="not(key('Impuestos-Traslados', '003')[1])">
            <xsl:call-template name="Requerido">
                <xsl:with-param name="valor"/>
            </xsl:call-template>
        </xsl:if>
    </xsl:template>
    <xsl:template match="cfdi:Traslado">
        <!-- Sum all the elements from the @Impuesto group -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="format-number(sum(key('Impuestos-Traslados', @Impuesto)/@Importe), '0.00')"/>
        </xsl:call-template>
    </xsl:template>

    <xsl:template match="cfdi:Retenciones">
        <xsl:apply-templates select="cfdi:Retencion[generate-id() = generate-id(key('Impuestos-Retenciones', '001')[1])]" />
        <xsl:if test="not(key('Impuestos-Retenciones', '001')[1])">
            <xsl:call-template name="Requerido">
                <xsl:with-param name="valor"/>
            </xsl:call-template>
        </xsl:if>
        <xsl:apply-templates select="cfdi:Retencion[generate-id() = generate-id(key('Impuestos-Retenciones', '002')[1])]" />
        <xsl:if test="not(key('Impuestos-Retenciones', '002')[1])">
            <xsl:call-template name="Requerido">
                <xsl:with-param name="valor"/>
            </xsl:call-template>
        </xsl:if>
        <xsl:apply-templates select="cfdi:Retencion[generate-id() = generate-id(key('Impuestos-Retenciones', '003')[1])]" />
        <xsl:if test="not(key('Impuestos-Retenciones', '003')[1])">
            <xsl:call-template name="Requerido">
                <xsl:with-param name="valor"/>
            </xsl:call-template>
        </xsl:if>
    </xsl:template>
    <xsl:template match="cfdi:Retencion">
        <!-- Sum all the elements from the @Impuesto group -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="format-number(sum(key('Impuestos-Retenciones', @Impuesto)/@Importe), '0.00')"/>
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
            <xsl:with-param name="valor" select="./@SelloCFD"/>
        </xsl:call-template>
    </xsl:template>
</xsl:stylesheet>