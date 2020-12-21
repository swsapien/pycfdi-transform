import xml.sax


class TSaxBase:

    def __init__(self):
        super().__init__()

    def parse_file(self, handler, xml_file):
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(xml_file)

    def parse_string(self, handler, string_xml):
        xml.sax.parseString(string_xml, handler)

