import os
from pycfdi_transform.__t_base__ import TBase

class TNomina12(TBase):
  def __init__(self,xslt_file = 'nomina12.xslt'):
    super().__init__(xslt_file)
  
  def convert_to_columns(self,line):    
    lines = str(line).split("‡")
    lista = list()
    for line in lines:
      repetitive = str(line).split('§')
      if(len(repetitive) > 1):
        lst = str(repetitive[0]).split('~')
        lst_repetitive = str(repetitive[1]).split('~')
        for i in range(1, len(lst_repetitive), 6):
          insert = lst + [lst_repetitive[i], lst_repetitive[i+1], lst_repetitive[i+2], lst_repetitive[i+3], lst_repetitive[i+4], lst_repetitive[i+5]]
          lista.append(insert)
      else:
        lst = str(line).split('~')
        lista.append(lst)
    return lista
  
  def get_column_names(self):
    return [
      "VERSION",
      "SERIE",
      "FOLIO",
      "FECHA",
      "NOCERTIFICADO",
      "SUBTOTAL",
      "DESCUENTO",
      "TOTAL",
      "MONEDA",
      "TIPOCAMBIO",
      "TIPODECOMPROBANTE",
      "METODOPAGO",
      "FORMAPAGO",
      "CONDICIONESDEPAGO",
      "LUGAREXPEDICION",
      "EMISORRFC",
      "EMISORNOMBRE",
      "EMISORREGIMENFISCAL",
      "RECEPTORRFC",
      "RECEPTORNOMBRE",
      "RECEPTORUSOCFDI",
      "UUID",
      "FECHATIMBRADO",
      "RFCPROVCERTIF",
      "SELLOCFD",
      "TIPONOMINA",
      "FECHAPAGO",
      "FECHAINICIALPAGO",
      "FECHAFINALPAGO",
      "NUMDIASPAGADOS",
      "TOTALPERCEPCIONES",
      "TOTALDEDUCCIONES",
      "TOTALOTROSPAGOS",
      "CURPEMISOR",
      "REGISTROPATRONAL",
      "RFCPATRONORIGEN",
      "CURPRECEPTOR",
      "NUMSEGURIDADSOCIAL",
      "FECHAINICIORELLABORAL",
      "SINDICALIZADO",
      "TIPOJORNADA",
      "TIPOREGIMEN",
      "NUMEMPLEADO",
      "DEPARTAMENTO",
      "PUESTO",
      "RIESGOPUESTO",
      "BANCO",
      "CUENTABANCARIA",
      "ANTIGÜEDAD",
      "TIPOCONTRATO",
      "PERIODICIDADPAGO",
      "SALARIOBASECOTAPOR",
      "SALARIODIARIOINTEGRADO",
      "CLAVEENTFED",
      "TOTALSUELDOS",
      "TOTALSEPARACIONINDEMNIZACION",
      "TOTALJUBILACIONPENSIONRETIRO",
      "TOTALGRAVADO",
      "TOTALEXENTO",
      "TOTALOTRASDEDUCCIONES",
      "TOTALIMPUESTOSRETENIDOSN",
      "DEDUCCION_PERCEPCION_OTROS",
      "CLAVE_DEDUCCION_PERCEPCION",
      "TIPO_DEDUCCION_PERCEPCION",
      "CONCEPTO",
      "IMPORTEGRAVADO",
      "IMPORTEEXENTO"
    ]