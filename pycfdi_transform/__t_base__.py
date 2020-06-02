import os
import lxml.etree as ET
import xlsxwriter
import pkg_resources


class TBase:
  def __init__(self,xslt_file):
    xslt_file = pkg_resources.resource_filename(__name__,'xslt/%s' % xslt_file)
    with open(xslt_file, 'r', encoding='utf-8') as f_xslt:
      xslt = ET.parse(f_xslt)
    if xslt == None:
      raise UnicodeError("Cannot read xslt files. XSLT transformers are empty")

    self.transformer = ET.XSLT(xslt)    
    self.parser = ET.XMLParser(recover=True, encoding='utf-8')
    self.parser_from_str = ET.XMLParser(recover=True)
  
  def to_columns_from_file(self, xml_file):
    if '.xml' in xml_file:
      try:        
        xml = ET.parse(xml_file, parser=self.parser)
        return self.convert_to_columns(str(self.transformer(xml)))
      except Exception as ex:
        print(ex)
        return
  
  def to_columns_from_bytes(self, bytes_xml):   
    try:        
      xml = ET.XML(bytes_xml, parser=self.parser)
      return self.convert_to_columns(str(self.transformer(xml)))
    except Exception as ex:
      print(ex)
      return
  
  def convert_to_columns(self,line):
    return [str(line).split("~")]