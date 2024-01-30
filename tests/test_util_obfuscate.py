import random
import string
import xml.etree.ElementTree as ET
from lxml import etree
from datetime import datetime, timedelta
from pycfdi_transform.helpers.string_helper import StringHelper

def random_string(length):
    ''' Generate a random string of fixed length '''
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_number(length):
    """ Generate a random integer number of fixed length """
    return ''.join(random.choices(string.digits, k=length))

def random_decimal(length):
    """ Generate a random decimal number of fixed length """
    # Assuming one digit for the decimal point
    integer_part_length = length // 2
    decimal_part_length = length - integer_part_length - 1  # minus 1 for the decimal point
    integer_part = ''.join(random.choices(string.digits, k=integer_part_length))
    decimal_part = ''.join(random.choices(string.digits, k=decimal_part_length))
    return f"{integer_part}.{decimal_part}"

def random_datetime():
    """ Generate a random datetime in ISO format """
    start = datetime(2000, 1, 1)
    end = datetime(2024, 12, 31)
    random_date = start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )
    return random_date.isoformat()

def is_number(s):
    """ Check if the string is a number (integer or decimal) """
    try:
        float(s)
        return True
    except ValueError:
        return False

def replace_attributes_xml(tree: ET,xml_path):
    root = tree.getroot()
    # Iterate over all the elements in the XML
    for elem in root.iter():
        for attr in elem.attrib:
            current_value = elem.attrib[attr]
            if "Version" in attr:
                continue
            if "Fecha" in attr:
                # Replace with a random datetime in ISO format
                elem.attrib[attr] = random_datetime()
            elif is_number(current_value):
                if '.' in current_value:
                    # Replace with a random decimal of the same length
                    elem.attrib[attr] = random_decimal(len(current_value))
                else:
                    # Replace with a random number of the same length
                    elem.attrib[attr] = random_number(len(current_value))
            else:
                # Replace with a random string of the same length
                elem.attrib[attr] = random_string(len(current_value))

    # Save the modified XML to a new file
    with open(xml_path.replace('.xml', '_obfuscated.xml'), "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)

def obfuscate_attributes_cfdi40(xml_path):
    xml_parser = etree.XMLParser(encoding='utf-8', recover=True, huge_tree=True)

    # Define your namespaces
    namespaces = {
        'cfdi':'http://www.sat.gob.mx/cfd/4',
        'cce11':'http://www.sat.gob.mx/ComercioExterior11',
        'cce20':'http://www.sat.gob.mx/ComercioExterior20',
        'donat':'http://www.sat.gob.mx/donat',
        'divisas':'http://www.sat.gob.mx/divisas',
        'implocal':'http://www.sat.gob.mx/implocal',
        'leyendasFisc':'http://www.sat.gob.mx/leyendasFiscales',
        'pfic':'http://www.sat.gob.mx/pfic',
        'tpe':'http://www.sat.gob.mx/TuristaPasajeroExtranjero',
        'nomina12':'http://www.sat.gob.mx/nomina12',
        'registrofiscal':'http://www.sat.gob.mx/registrofiscal',
        'pagoenespecie':'http://www.sat.gob.mx/pagoenespecie',
        'aerolineas':'http://www.sat.gob.mx/aerolineas',
        'valesdedespensa':'http://www.sat.gob.mx/valesdedespensa',
        'notariospublicos':'http://www.sat.gob.mx/notariospublicos',
        'vehiculousado':'http://www.sat.gob.mx/vehiculousado',
        'servicioparcial':'http://www.sat.gob.mx/servicioparcialconstruccion',
        'decreto':'http://www.sat.gob.mx/renovacionysustitucionvehiculos',
        'destruccion':'http://www.sat.gob.mx/certificadodestruccion',
        'obrasarte':'http://www.sat.gob.mx/arteantiguedades',
        'ine':'http://www.sat.gob.mx/ine',
        'iedu':'http://www.sat.gob.mx/iedu',
        'ventavehiculos':'http://www.sat.gob.mx/ventavehiculos',
        'detallista':'http://www.sat.gob.mx/detallista',
        'ecc12':'http://www.sat.gob.mx/EstadoDeCuentaCombustible12',
        'consumodecombustibles11':'http://www.sat.gob.mx/ConsumoDeCombustibles11',
        'gceh':'http://www.sat.gob.mx/GastosHidrocarburos10',
        'ieeh':'http://www.sat.gob.mx/IngresosHidrocarburos10',
        'cartaporte20':'http://www.sat.gob.mx/CartaPorte20',
        'pago20':'http://www.sat.gob.mx/Pagos20',
        'cartaporte30':'http://www.sat.gob.mx/CartaPorte30',
        'tfd':'http://www.sat.gob.mx/TimbreFiscalDigital'
    }
    for prefix, uri in namespaces.items():
        ET.register_namespace(prefix, uri)
    
    tree = ET.parse(xml_path, parser=xml_parser)
    replace_attributes_xml(tree,xml_path)

def obfuscate_attributes_cfdi33(xml_path):
    xml_parser = etree.XMLParser(encoding='utf-8', recover=True, huge_tree=True)

    # Define your namespaces
    namespaces = {
        'cfdi':'http://www.sat.gob.mx/cfd/3',
        'cce11':'http://www.sat.gob.mx/ComercioExterior11',
        'donat':'http://www.sat.gob.mx/donat',
        'divisas':'http://www.sat.gob.mx/divisas',
        'implocal':'http://www.sat.gob.mx/implocal',
        'leyendasFisc':'http://www.sat.gob.mx/leyendasFiscales',
        'pfic':'http://www.sat.gob.mx/pfic',
        'tpe':'http://www.sat.gob.mx/TuristaPasajeroExtranjero',
        'nomina12':'http://www.sat.gob.mx/nomina12',
        'registrofiscal':'http://www.sat.gob.mx/registrofiscal',
        'pagoenespecie':'http://www.sat.gob.mx/pagoenespecie',
        'aerolineas':'http://www.sat.gob.mx/aerolineas',
        'valesdedespensa':'http://www.sat.gob.mx/valesdedespensa',
        'consumodecombustibles':'http://www.sat.gob.mx/consumodecombustibles',
        'notariospublicos':'http://www.sat.gob.mx/notariospublicos',
        'vehiculousado':'http://www.sat.gob.mx/vehiculousado',
        'servicioparcial':'http://www.sat.gob.mx/servicioparcialconstruccion',
        'decreto':'http://www.sat.gob.mx/renovacionysustitucionvehiculos',
        'destruccion':'http://www.sat.gob.mx/certificadodestruccion',
        'obrasarte':'http://www.sat.gob.mx/arteantiguedades',
        'ine':'http://www.sat.gob.mx/ine',
        'iedu':'http://www.sat.gob.mx/iedu',
        'ventavehiculos':'http://www.sat.gob.mx/ventavehiculos',
        'terceros':'http://www.sat.gob.mx/terceros',
        'pago10':'http://www.sat.gob.mx/Pagos',
        'detallista':'http://www.sat.gob.mx/detallista',
        'ecc12':'http://www.sat.gob.mx/EstadoDeCuentaCombustible12',
        'consumodecombustibles11':'http://www.sat.gob.mx/ConsumoDeCombustibles11',
        'gceh':'http://www.sat.gob.mx/GastosHidrocarburos10',
        'ieeh':'http://www.sat.gob.mx/IngresosHidrocarburos10',
        'cartaporte':'http://www.sat.gob.mx/CartaPorte',
        'cartaporte20':'http://www.sat.gob.mx/CartaPorte20',
        'tfd':'http://www.sat.gob.mx/TimbreFiscalDigital'
    }
    for prefix, uri in namespaces.items():
        ET.register_namespace(prefix, uri)
    
    tree = ET.parse(xml_path, parser=xml_parser)
    replace_attributes_xml(tree,xml_path)


if __name__ == "__main__":
    # Replace with your file path
    xml_path = './tests/Resources/cfdi40/cfdi40_bigfile_1.xml'  # Replace with your file path
    obfuscate_attributes_cfdi40(xml_path)

    xml_path = './tests/Resources/cfdi40/cfdi40_bigfile_2.xml'  # Replace with your file path
    obfuscate_attributes_cfdi40(xml_path)

    xml_path = './tests/Resources/cfdi40/cfdi40_bigfile_3.xml'  # Replace with your file path
    obfuscate_attributes_cfdi40(xml_path)

    xml_path = './tests/Resources/cfdi33/cfdi33_bigfile_1.xml'  # Replace with your file path
    obfuscate_attributes_cfdi33(xml_path)

    xml_path = './tests/Resources/cfdi33/cfdi33_bigfile_2.xml'  # Replace with your file path
    obfuscate_attributes_cfdi33(xml_path)