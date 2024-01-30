import os
from io import BytesIO
import unittest
import xml.sax
from lxml import etree
from pycfdi_transform import CFDI33SAXHandler, EfiscoCorpCFDI33Formatter
import time

class TestCFDI33SAXHandlerBigFiles(unittest.TestCase):
    def test_transform_file_1(self):
        sax_handler = CFDI33SAXHandler(esc_delimiters="~").use_concepts_cfdi33().use_implocal10().use_nomina12().use_pagos10().use_related_cfdis()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_bigfile_1.xml")
        self.assertIsNotNone(cfdi_data)
        self.assertTrue('cfdi33' in cfdi_data,"cfdi33 not in cfdi_data")
        self.assertTrue('tfd11' in cfdi_data,"tfd11 not in cfdi_data")
        cfdi_formatter = EfiscoCorpCFDI33Formatter(cfdi_data, safe_numerics=True)
        self.assertTrue(cfdi_formatter.can_format(), "cfdi_formatter.can_format() is False")
        cfdi_formatted_data = cfdi_formatter.dict_to_columns()
        self.assertIsNotNone(cfdi_formatted_data)

    def test_transform_file_2(self):
        sax_handler = CFDI33SAXHandler(esc_delimiters="~").use_concepts_cfdi33().use_implocal10().use_nomina12().use_pagos10().use_related_cfdis()
        cfdi_data = sax_handler.transform_from_file("./tests/Resources/cfdi33/cfdi33_bigfile_2.xml")
        self.assertIsNotNone(cfdi_data)
        self.assertTrue('cfdi33' in cfdi_data, "cfdi33 not in cfdi_data")
        self.assertTrue('tfd11' in cfdi_data, "tfd11 not in cfdi_data")
        cfdi_formatter = EfiscoCorpCFDI33Formatter(cfdi_data, safe_numerics=True)
        self.assertTrue(cfdi_formatter.can_format())
        cfdi_formatted_data = cfdi_formatter.dict_to_columns()
        self.assertIsNotNone(cfdi_formatted_data)


    
    