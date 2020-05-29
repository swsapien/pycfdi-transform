import os 
from pycfdi_transform.__t_base__ import TBase

class TCfdi32(TBase):
  def __init__(self,xslt_file = 'cfdi32.xslt'):
    super().__init__(xslt_file)
  
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
      "RECEPTORRESIDENCIAFISCAL",
      "RECEPTORNUMREGIDTRIB",
      "RECEPTORUSOCFDI",
      "IVATRASLADO",
      "IEPSTRASLADO",
      "TOTALIMPUESTOSTRASLADOS",
      "ISRRETENIDO",
      "IVARETENIDO",
      "IEPSRETENIDO",
      "TOTALIMPUESTOSRETENIDOS",
      "TOTALTRASLADOSIMPUESTOSLOCALES",
      "TOTALRETENCIONESIMPUESTOSLOCALES",
      "COMPLEMENTOS",
      "UUID",
      "FECHATIMBRADO",
      "RFCPROVCERTIF",
      "SELLOCFD"     
    ]