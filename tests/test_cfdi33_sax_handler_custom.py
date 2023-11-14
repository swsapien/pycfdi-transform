import unittest
from pycfdi_transform import CFDI33SAXHandler
from lxml import etree
import time

class TestCFDI33SAXHandlerCustom(unittest.TestCase):

    def test_transform_file_custom_01(self):
        sax_handler = CFDI33SAXHandler()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/custom/custom_01.xml")
        self.assertIsNotNone(cfdi_data)
        self.assertIsNotNone(cfdi_data)
        self.assertIsNotNone(cfdi_data['tfd11'])
        self.assertIsNotNone(cfdi_data['cfdi33']['version'])
        self.assertEqual(len(cfdi_data['tfd11']),1)
        self.assertEqual(cfdi_data['tfd11'][0]['uuid'],'11X11X0X-XX1X-1010-11X1-111X1XXXXX11')