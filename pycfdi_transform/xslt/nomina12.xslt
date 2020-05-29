<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
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

<xsl:include href="utilerias.xslt"/>
<xsl:include href="common_cfdi.xslt"/>
<!-- variables necesarias -->
<xsl:key name="Percepciones-Nomina" match="/cfdi:Comprobante/cfdi:Complemento/nomina12:Nomina/nomina12:Percepciones/nomina12:Percepcion" use="@TipoPercepcion" />
<xsl:key name="Deducciones-Nomina" match="/cfdi:Comprobante/cfdi:Complemento/nomina12:Nomina/nomina12:Deducciones/nomina12:Deduccion" use="@TipoDeduccion" />
<xsl:key name="OtrosPagos-Nomina" match="/cfdi:Comprobante/cfdi:Complemento/nomina12:Nomina/nomina12:OtrosPagos/nomina12:OtroPago" use="@TipoOtroPago" />

<!-- Con el siguiente método se establece que la salida deberá ser en texto -->
    <xsl:output method="text" version="1.0" encoding="UTF-8" indent="no"/>    
    <xsl:template match="/">
      <xsl:if test="/cfdi:Comprobante/cfdi:Complemento/nomina12:Nomina">
      <xsl:for-each select="/cfdi:Comprobante/cfdi:Complemento/nomina12:Nomina">
        <!-- put separator on line if are the second or > complement in same line -->
        <xsl:if test="position() > 1">
          <xsl:call-template name="Requerido">
			      <xsl:with-param name="valor">
              <xsl:text>&#124;&#8225;&#124;</xsl:text>
            </xsl:with-param>
		      </xsl:call-template>
        </xsl:if>
        <!-- print data for CFDI -->
        <xsl:choose>
          <xsl:when test="/cfdi:Comprobante/@Version = '3.3'">
            <xsl:apply-templates select="/cfdi:Comprobante[1]" mode="v33"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:apply-templates select="/cfdi:Comprobante[1]" mode="v32"/>
          </xsl:otherwise>
        </xsl:choose>
        <!-- print data for TFD only first time -->
        <xsl:choose>
          <xsl:when test="position() = 1">
            <xsl:choose>
              <xsl:when test="/cfdi:Comprobante/cfdi:Complemento/tfd:TimbreFiscalDigital/@version = '1.0'">
                  <xsl:apply-templates select="/cfdi:Comprobante/cfdi:Complemento/tfd:TimbreFiscalDigital" mode="v10"/>
              </xsl:when>
              <xsl:when test="/cfdi:Comprobante/cfdi:Complemento/tfd:TimbreFiscalDigital/@Version = '1.1'">
                  <xsl:apply-templates select="/cfdi:Comprobante/cfdi:Complemento/tfd:TimbreFiscalDigital" mode="v11"/>
              </xsl:when>
              <xsl:otherwise>
                  <xsl:call-template name="block-generator">
                      <xsl:with-param name="N" select="4"/>
                  </xsl:call-template>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:when>
          <xsl:otherwise>
            <xsl:call-template name="block-generator">
              <xsl:with-param name="N" select="4"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
        <!-- call template for nomina -->
        <xsl:apply-templates select="." />
      </xsl:for-each>
      </xsl:if>
    </xsl:template>

	<xsl:template match="nomina12:Nomina">
		<xsl:call-template name="Requerido">
			<xsl:with-param name="valor" select="./@TipoNomina"/>
		</xsl:call-template>
		<xsl:call-template name="Requerido">
			<xsl:with-param name="valor" select="./@FechaPago"/>
		</xsl:call-template>
		<xsl:call-template name="Requerido">
			<xsl:with-param name="valor" select="./@FechaInicialPago"/>
		</xsl:call-template>
		<xsl:call-template name="Requerido">
			<xsl:with-param name="valor" select="./@FechaFinalPago"/>
		</xsl:call-template>
    <xsl:call-template name="Requerido">
			<xsl:with-param name="valor" select="./@NumDiasPagados"/>
		</xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@TotalPercepciones"/>
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@TotalDeducciones"/>
    </xsl:call-template>
    <xsl:call-template name="Requerido">
      <xsl:with-param name="valor" select="./@TotalOtrosPagos"/>
    </xsl:call-template>

    <!-- Call nodes nomina -->
    <xsl:apply-templates select="./nomina12:Emisor"/>
    <xsl:if test="not(./nomina12:Emisor)">
      <xsl:call-template name="block-generator">
        <xsl:with-param name="N" select="3"/>
      </xsl:call-template>
    </xsl:if>
    <xsl:apply-templates select="./nomina12:Receptor"/>
    <xsl:apply-templates select="./nomina12:Percepciones"/>
    <xsl:if test="not(./nomina12:Percepciones)">
      <xsl:call-template name="block-generator">
        <xsl:with-param name="N" select="5"/>
      </xsl:call-template>
    </xsl:if>
    <xsl:apply-templates select="./nomina12:Deducciones"/>
    <xsl:if test="not(./nomina12:Deducciones)">
      <xsl:call-template name="block-generator">
        <xsl:with-param name="N" select="2"/>
      </xsl:call-template>
    </xsl:if>
    <xsl:call-template name="Repetitive_values"/>
    </xsl:template>

    <xsl:template match="nomina12:Emisor">
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@Curp"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@RegistroPatronal"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@RfcPatronOrigen"/>
      </xsl:call-template>
    <!-- Call EntidadSNCF -->
    </xsl:template>

    <xsl:template match="nomina12:Receptor">
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@Curp"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@NumSeguridadSocial"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@FechaInicioRelLaboral"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@Sindicalizado"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@TipoJornada"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@TipoRegimen"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@NumEmpleado"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@Departamento"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@Puesto"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@RiesgoPuesto"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@Banco"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@CuentaBancaria"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@Antigüedad"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@TipoContrato"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@PeriodicidadPago"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@SalarioBaseCotApor"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@SalarioDiarioIntegrado"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@ClaveEntFed"/>
      </xsl:call-template>
      <!-- Call SubContratacion -->
    </xsl:template>

    <xsl:template match="nomina12:Percepciones">
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@TotalSueldos"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@TotalSeparacionIndemnizacion"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@TotalJubilacionPensionRetiro"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@TotalGravado"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@TotalExento"/>
      </xsl:call-template>
    </xsl:template>

    <xsl:template name="PercepcionesBlock">
      <xsl:param name="var"/>
      <xsl:param name="i" select="1"/>
      <xsl:param name="iFormated" select="format-number($i, '000')"/>
      <xsl:if test="$var >= $i">
        <!-- Apply template for $var -->
        <xsl:apply-templates select="/cfdi:Comprobante/cfdi:Complemento/nomina12:Nomina/nomina12:Percepciones/nomina12:Percepcion[generate-id() = generate-id(key('Percepciones-Nomina', $iFormated)[1])]" />

        <xsl:call-template name="PercepcionesBlock">
          <xsl:with-param name="var" select="$var"/>
          <xsl:with-param name="i" select="$i + 1"/>
        </xsl:call-template>
      </xsl:if>
    </xsl:template>

    <xsl:template match="nomina12:Percepcion">
        <!-- DEDUCCION_PERCEPCION_OTROS -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="'P'"/>
        </xsl:call-template>
        <!-- Clave -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Clave"/>
        </xsl:call-template>
        <!-- Tipo -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@TipoPercepcion"/>
        </xsl:call-template>
        <!-- CONCEPTO -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Concepto"/>
        </xsl:call-template>
        <!-- IMPORTEGRAVADO -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="format-number(sum(key('Percepciones-Nomina', @TipoPercepcion)/@ImporteGravado), '0.00')"/>
        </xsl:call-template>
        <!-- IMPORTEEXENTO -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="format-number(sum(key('Percepciones-Nomina', @TipoPercepcion)/@ImporteExento), '0.00')"/>
        </xsl:call-template>
    </xsl:template>

    <xsl:template match="nomina12:Deducciones">
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@TotalOtrasDeducciones"/>
      </xsl:call-template>
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@TotalImpuestosRetenidos"/>
      </xsl:call-template>
    </xsl:template>

    <xsl:template name="DeduccionesBlock">
      <xsl:param name="var"/>
      <xsl:param name="i" select="1"/>
      <xsl:param name="iFormated" select="format-number($i, '000')"/>
      <xsl:if test="$var >= $i">
        <!-- Apply template for $var -->
        <xsl:apply-templates select="/cfdi:Comprobante/cfdi:Complemento/nomina12:Nomina/nomina12:Deducciones/nomina12:Deduccion[generate-id() = generate-id(key('Deducciones-Nomina', $iFormated)[1])]" />

        <xsl:call-template name="DeduccionesBlock">
          <xsl:with-param name="var" select="$var"/>
          <xsl:with-param name="i" select="$i + 1"/>
        </xsl:call-template>
      </xsl:if>
    </xsl:template>

    <xsl:template match="nomina12:Deduccion">
        <!-- DEDUCCION_PERCEPCION_OTROS -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="'D'"/>
        </xsl:call-template>
        <!-- Clave -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Clave"/>
        </xsl:call-template>
        <!-- Tipo -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@TipoDeduccion"/>
        </xsl:call-template>
        <!-- Concepto -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="./@Concepto"/>
        </xsl:call-template>
        <!-- IMPORTEGRAVADO -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="format-number(sum(key('Deducciones-Nomina', @TipoDeduccion)/@Importe), '0.00')"/>
        </xsl:call-template>
        <!-- IMPORTEEXENTO -->
        <xsl:call-template name="Requerido">
            <xsl:with-param name="valor" select="'0.00'"/>
        </xsl:call-template>
    </xsl:template>

    <xsl:template match="nomina12:OtroPago">
      <!-- DEDUCCION_PERCEPCION_OTROS -->
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="'O'"/>
      </xsl:call-template>
      <!-- Clave -->
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@Clave"/>
      </xsl:call-template>
      <!-- Tipo -->
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@TipoOtroPago"/>
      </xsl:call-template>
      <!-- Concepto -->
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="./@Concepto"/>
      </xsl:call-template>
      <!-- IMPORTEGRAVADO -->
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="'0.00'"/>
      </xsl:call-template>
      <!-- IMPORTEEXENTO -->
      <xsl:call-template name="Requerido">
        <xsl:with-param name="valor" select="format-number(sum(key('OtrosPagos-Nomina', @TipoOtroPago)/@Importe), '0.00')"/>
      </xsl:call-template>
    </xsl:template>

    <xsl:template name="OtroPagoBlock">
      <xsl:param name="var"/>
      <xsl:param name="i" select="1"/>
      <xsl:param name="iFormated" select="format-number($i, '000')"/>
      <xsl:if test="$var >= $i">
        <!-- Apply template for $var -->
        <xsl:apply-templates select="/cfdi:Comprobante/cfdi:Complemento/nomina12:Nomina/nomina12:OtrosPagos/nomina12:OtroPago[generate-id() = generate-id(key('OtrosPagos-Nomina', $iFormated)[1])]" />

        <xsl:call-template name="OtroPagoBlock">
          <xsl:with-param name="var" select="$var"/>
          <xsl:with-param name="i" select="$i + 1"/>
        </xsl:call-template>
      </xsl:if>
    </xsl:template>

    <xsl:template name="Repetitive_values">
      <xsl:call-template name="OnlyData">
        <xsl:with-param name="valor">
          <xsl:text>&#00167;</xsl:text>
        </xsl:with-param>
      </xsl:call-template>
      <!-- Call each node of perceptions -->
      <xsl:call-template name="PercepcionesBlock">
          <xsl:with-param name="var" select="55"/>
      </xsl:call-template>

      <!-- Call each node of deductions -->
      <xsl:call-template name="DeduccionesBlock">
          <xsl:with-param name="var" select="106"/>
      </xsl:call-template>

      <!-- call each node of otros pagos -->
      <xsl:call-template name="OtroPagoBlock">
          <xsl:with-param name="var" select="5"/>
      </xsl:call-template>
      <!-- call otros pagos 999 -->
      <xsl:apply-templates select="/cfdi:Comprobante/cfdi:Complemento/nomina12:Nomina/nomina12:OtrosPagos/nomina12:OtroPago[generate-id() = generate-id(key('OtrosPagos-Nomina', '999')[1])]" />
    </xsl:template>

</xsl:stylesheet>
