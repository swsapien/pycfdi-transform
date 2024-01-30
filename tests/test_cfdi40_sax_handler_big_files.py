import os
from io import BytesIO
import unittest
import xml.sax
from lxml import etree
from pycfdi_transform import CFDI40SAXHandler, EfiscoCorpCFDI40Formatter
from pycfdi_transform.helpers.string_helper import StringHelper
import time

class TestCFDI40SAXHandlerBigFiles(unittest.TestCase):
    def test_transform_file_1(self):
        sax_handler = CFDI40SAXHandler(esc_delimiters="~").use_concepts_cfdi40().use_implocal10().use_nomina12().use_pagos20().use_related_cfdis()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_bigfile_1.xml")
        self.assertIsNotNone(cfdi_data)
        self.assertTrue('cfdi40' in cfdi_data)
        self.assertTrue('tfd11' in cfdi_data)
        cfdi_formatter = EfiscoCorpCFDI40Formatter(cfdi_data, safe_numerics=True)
        self.assertTrue(cfdi_formatter.can_format())
        cfdi_formatted_data = cfdi_formatter.dict_to_columns()
        self.assertIsNotNone(cfdi_formatted_data)
    
    def test_transform_file_2(self):
        sax_handler = CFDI40SAXHandler(esc_delimiters="~").use_concepts_cfdi40().use_implocal10().use_nomina12().use_pagos20().use_related_cfdis()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_bigfile_2.xml")
        self.assertIsNotNone(cfdi_data)
        self.assertTrue('cfdi40' in cfdi_data)
        self.assertTrue('tfd11' in cfdi_data)
        cfdi_formatter = EfiscoCorpCFDI40Formatter(cfdi_data, safe_numerics=True)
        self.assertTrue(cfdi_formatter.can_format())
        cfdi_formatted_data = cfdi_formatter.dict_to_columns()
        self.assertIsNotNone(cfdi_formatted_data)
    
    def test_transform_file_3(self):
        sax_handler = CFDI40SAXHandler(esc_delimiters="~").use_concepts_cfdi40().use_implocal10().use_nomina12().use_pagos20().use_related_cfdis()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi40/cfdi40_bigfile_3.xml")
        self.assertIsNotNone(cfdi_data)
        self.assertTrue('cfdi40' in cfdi_data)
        self.assertTrue('tfd11' in cfdi_data)
        cfdi_formatter = EfiscoCorpCFDI40Formatter(cfdi_data, safe_numerics=True)
        self.assertTrue(cfdi_formatter.can_format())
        cfdi_formatted_data = cfdi_formatter.dict_to_columns()
        self.assertIsNotNone(cfdi_formatted_data)

    


    
    