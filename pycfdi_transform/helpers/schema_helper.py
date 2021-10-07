from lxml import etree

class SchemaHelper:
    @staticmethod
    def get_schema_validator_cfdi33() -> etree.XMLSchema:
        xml_schema = etree.XMLSchema(file='./pycfdi_transform/xsd/cfdi33/cfdv33.xsd')
        return xml_schema