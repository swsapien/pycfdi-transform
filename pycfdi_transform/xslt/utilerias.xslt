<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
	xmlns:xs="http://www.w3.org/2001/XMLSchema" 
	xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<xsl:variable name="separator" select="'~'" />
	<!-- Manejador de datos requeridos -->
	<xsl:template name="Requerido">
		<xsl:param name="valor"/>
		<xsl:value-of select="$separator" />
		<xsl:call-template name="ManejaEspacios">
			<xsl:with-param name="s" select="$valor"/>
		</xsl:call-template>
	</xsl:template>
	<xsl:template name="RequeridoFirstElement">
		<xsl:param name="valor"/>		
		<xsl:call-template name="ManejaEspacios">
			<xsl:with-param name="s" select="$valor"/>
		</xsl:call-template>
	</xsl:template>
	<xsl:template name="Opcional">
		<xsl:param name="valor"/>
		<xsl:value-of select="$separator" />
		<xsl:call-template name="ManejaEspacios">
			<xsl:with-param name="s" select="$valor"/>
		</xsl:call-template>
	</xsl:template>
	<xsl:template name="OpcionalFirstElement">
		<xsl:param name="valor"/>		
		<xsl:call-template name="ManejaEspacios">
			<xsl:with-param name="s" select="$valor"/>
		</xsl:call-template>
	</xsl:template>

	<!-- Dato sin pipe. Uso para primer dato -->
	<xsl:template name="OnlyData">
		<xsl:param name="valor"/>
		<xsl:call-template name="ManejaEspacios">
			<xsl:with-param name="s" select="$valor"/>
		</xsl:call-template>
	</xsl:template>

	<!-- Normalizador de espacios en blanco -->
	<xsl:template name="ManejaEspacios">
		<xsl:param name="s"/>
		<xsl:value-of select="normalize-space(string($s))"/>
	</xsl:template>

	<!-- Generador de "" para nodos no existentes. Recibe un valor N y genera ese número de "~" llamando al template Requerido -->
	<xsl:template name="block-generator">
		<xsl:param name="N"/>
		<xsl:param name="i" select="0"/>
		<xsl:if test="$N > $i">
			<!-- generate a block -->
			<xsl:call-template name="Requerido">
				<xsl:with-param name="valor"/>
			</xsl:call-template>
			<!-- recursive call -->
			<xsl:call-template name="block-generator">
				<xsl:with-param name="N" select="$N"/>
				<xsl:with-param name="i" select="$i + 1"/>
			</xsl:call-template>
		</xsl:if>
	</xsl:template>

	<!--  Concatenador de Listas  -->
	<xsl:template name="join">
		<xsl:param name="list" />
		<xsl:param name="separator"/>

		<xsl:for-each select="$list">
			<xsl:value-of select="." />
			<xsl:if test="position() != last()">
				<xsl:value-of select="$separator" />
			</xsl:if>
		</xsl:for-each>
	</xsl:template>

	<xsl:template name="join_ns">
		<xsl:param name="list" />
		<xsl:param name="separator"/>

		<xsl:for-each select="$list">
			<xsl:value-of select="substring-after(name(), ':')" />
			<xsl:if test="position() != last()">
				<xsl:value-of select="$separator" />
			</xsl:if>
		</xsl:for-each>
	</xsl:template>

	<xsl:template name="ToUpperCase">
		<xsl:param name="valor" />
		<xsl:variable name="smallcase" select="'abcdefghijklmnopqrstuvwxyz&quot;~'" />
		<xsl:variable name="uppercase" select="'ABCDEFGHIJKLMNOPQRSTUVWXYZ&quot;¬'" />

		<xsl:call-template name="Opcional">
			<xsl:with-param name="valor">
				<xsl:value-of select="translate($valor, $smallcase, $uppercase)" />
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	<xsl:template name="ToUpperCaseFirstElement">
		<xsl:param name="valor" />
		<xsl:variable name="smallcase" select="'abcdefghijklmnopqrstuvwxyz&quot;~'" />
		<xsl:variable name="uppercase" select="'ABCDEFGHIJKLMNOPQRSTUVWXYZ&quot;¬'" />
		<xsl:call-template name="OpcionalFirstElement">
			<xsl:with-param name="valor">
				<xsl:value-of select="translate($valor, $smallcase, $uppercase)" />
			</xsl:with-param>
		</xsl:call-template>
	</xsl:template>

</xsl:stylesheet>
