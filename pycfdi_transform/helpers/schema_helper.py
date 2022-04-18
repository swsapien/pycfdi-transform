from lxml import etree


class SchemaHelper:
    @staticmethod
    def get_schema_validator_cfdi33() -> etree.XMLSchema:
        xml_schema = etree.XMLSchema(file='./pycfdi_transform/xsd/cfdi33/cfdv33.xsd')
        return xml_schema

    @staticmethod
    def get_schema_validator_cfdi32() -> etree.XMLSchema:
        raise NotImplementedError("Validator for cfdi32 is not implemented")
