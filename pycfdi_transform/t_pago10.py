import os
from pycfdi_transform.__t_base__ import TBase

class TPago10(TBase):
  def __init__(self,xslt_file = 'pago10.xslt'):
    super().__init__(xslt_file)
  
  def convert_to_columns(self,line):
    lista = list()
    if len(line) <= 2:
      return lista
    line = line[2:]
    rows = str(line).split('‡‡')    
    for row in rows:
      columns_data = str(row).split('~')
      lista.append(columns_data)
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
      "P_IDENTIFICADOR_PAGO",
      "FECHAPAGO",
      "FORMADEPAGOP",
      "MONEDAP",
      "TIPOCAMBIOP",
      "MONTO",
      "NUMOPERACION",
      "RFCEMISORCTAORD",
      "NOMBANCOORDEXT",
      "CTAORDENANTE",
      "RFCEMISORCTABEN",
      "CTABENEFICIARIO",
      "IVATRASLADO",
      "IEPSTRASLADO",
      "TOTALIMPUESTOSTRASLADADOS",
      "ISRRETENCION",
      "IVARETENCION",
      "IEPSRETENCION",
      "TOTALIMPUESTOSRETENIDOS",
      "DR_IDDOCUMENTO",
      "DR_SERIE",
      "DR_FOLIO",
      "DR_MONEDADR",
      "DR_TIPOCAMBIODR",
      "DR_METODODEPAGODR",
      "DR_NUMPARCIALIDAD",
      "DR_IMPSALDOANT",
      "DR_IMPPAGADO",
      "DR_IMPSALDOINSOLUTO" 
    ]