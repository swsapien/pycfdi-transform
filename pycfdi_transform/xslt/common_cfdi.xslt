<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:xs="http://www.w3.org/2001/XMLSchema" 
    xmlns:fn="http://www.w3.org/2005/xpath-functions" 
    xmlns:cfdi="http://www.sat.gob.mx/cfd/3"
    xmlns:tfd="http://www.sat.gob.mx/TimbreFiscalDigital">
    
    <xsl:template match="cfdi:Comprobante" mode="v33">
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
        <xsl:apply-templates select="./cfdi:Emisor" mode="v33"/>
        <xsl:apply-templates select="./cfdi:Receptor" mode="v33"/>
    </xsl:template>
    <xsl:template match="cfdi:Comprobante" mode="v32">
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
        <xsl:apply-templates select="./cfdi:Emisor" mode="v32"/>
        <xsl:apply-templates select="./cfdi:Receptor" mode="v32"/>
    </xsl:template>
    <!-- Manejador de nodos tipo Emisor -->
    <xsl:template match="cfdi:Emisor" mode="v33">
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
    <xsl:template match="cfdi:Emisor" mode="v32">
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
    <!-- Manejador de nodos tipo Receptor -->
    <xsl:template match="cfdi:Receptor" mode="v33">
        <!--Iniciamos el tratamiento de los atributos del Receptor -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Rfc"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Nombre"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@UsoCFDI"/>
        </xsl:call-template>
    </xsl:template>
    <xsl:template match="cfdi:Receptor" mode="v32">
        <!--Iniciamos el tratamiento de los atributos del Receptor -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@rfc"/>
        </xsl:call-template>
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@nombre"/>
        </xsl:call-template>
        <!-- Call block generator UsoCFDI does not exist in CFDI 3.2 -->
        <xsl:call-template name="block-generator">
            <xsl:with-param name="N" select="1"/>
        </xsl:call-template>
    </xsl:template>
    <!-- Manejador de nodos tipo TimbreFiscalDigital -->
    <xsl:template match="tfd:TimbreFiscalDigital" mode="v11">
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
    <xsl:template match="tfd:TimbreFiscalDigital" mode="v10">
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
    <!-- Manejador de nodos tipo TimbreFiscalDigital -->
    <xsl:template match="tfd:TimbreFiscalDigital" mode="v11_simple">
		<xsl:call-template name="ToUpperCase">
			<xsl:with-param name="valor" select="./@UUID"/>
		</xsl:call-template>
		<xsl:call-template name="Requerido">
			<xsl:with-param name="valor" select="./@FechaTimbrado"/>
		</xsl:call-template>		
    </xsl:template>
</xsl:stylesheet>