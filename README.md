
# PyCfdi
PyCfdi Transform es un paquete de python que te permite convertir un Xml CFDI México a formato columnar.

Cfdi 3.3 con complementos:
- [x] Nomina 1.2
- [x] Pagos 1.0
- [x] ImpuestosLocales 1.0
- [x] TimbreFiscalDigital 1.1
  
# SW sapien
Queremos compartir la experiencia que tenemos en Facturación Electrónica con la comunidad. Nuestro objetivo es facilitar la implementación y mantenimiento del Cfdi en México.
  
## Build and Release status
[![Build Status](https://dev.azure.com/smarterwebci/SW%20sapien%20Open%20Source/_apis/build/status/swsapien.pycfdi-transform?branchName=master)](https://dev.azure.com/smarterwebci/SW%20sapien%20Open%20Source/_build/latest?definitionId=219&branchName=master)
  
[![Release Status](https://vsrm.dev.azure.com/smarterwebci/_apis/public/Release/badge/936fc2c5-c28f-4b30-9352-b4605790fdc8/1/1)](https://vsrm.dev.azure.com/smarterwebci/_apis/public/Release/badge/936fc2c5-c28f-4b30-9352-b4605790fdc8/1/1)
  
## Installation
  
Utiliza el package manager [pip](https://pip.pypa.io/en/stable/) para instalar pycfdi-transform.
  
```bash
pip install pycfdi-transform
```
  
## Usage
Para poder transformar un archivo XML a un objeto de tipo dictionary que contiene toda la información del XML es necesario usar un **Handler** de CFDI de la siguiente manera
```python
from  pycfdi_transform import CFDI33SAXHandler

path_xml = "./tests/Resources/cfdi33/cfdi33_01.xml"  #path xml que queremos transformar
transformer = CFDI33SAXHandler() # Cfdi 3.3
cfdi_data = transformer.transform_from_file(path_xml)
print(cfdi_data) 
```
*Contenido del xml mostrado*
```
{
  "cfdi33": {
    "version": "3.3",
    "serie": "VF",
    "folio": "001002004",
    "fecha": "2020-04-30T22:36:13",
    "no_certificado": "30001000000400002434",
    "subtotal": "10.00",
    "descuento": "",
    "total": "11.60",
    "moneda": "MXN",
    "tipo_cambio": "",
    "tipo_comprobante": "I",
    "metodo_pago": "PPD",
    "forma_pago": "01",
    "condiciones_pago": "NET15",
    "lugar_expedicion": "84094",
    "emisor": {
      "rfc": "EKU9003173C9",
      "nombre": "ESCUELA KEMPER URGATE SA DE CV",
      "regimen_fiscal": "601"
    },
    "receptor": {
      "rfc": "XAXX010101000",
      "nombre": "PUBLICO EN GENERAL",
      "residencia_fiscal": "",
      "num_reg_id_trib": "",
      "uso_cfdi": "G03"
    },
    "conceptos": [],
    "impuestos": {
      "retenciones": [],
      "traslados": [
        {
          "impuesto": "002",
          "tipo_factor": "Tasa",
          "tasa_o_cuota": "0.160000",
          "importe": "1.60"
        }
      ],
      "total_impuestos_traslados": "1.60",
      "total_impuestos_retenidos": ""
    },
    "complementos": "TimbreFiscalDigital",
    "addendas": ""
  },
  "tfd11": [
    {
      "version": "1.1",
      "no_certificado_sat": "20001000000300022323",
      "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
      "fecha_timbrado": "2020-05-02T00:36:50",
      "rfc_prov_cert": "AAA010101AAA",
      "sello_cfd": "SKndhzlakx2g1ykM73KJ8O0F02/ibJxmNqpEG6/878pu/8BUX/cgxWyh9O2EHhtITNlBZHD73Qgq9E7fuNOO/1xKuM9tgtzKrXqUmQ5bxhz2OfvynQ6Tmq6nzO+2FF6lyPmi2yxoeoGNtKjDIjnXNPAVYTS7n9V94dsciZaSmSGtT5LTIGTmA5QJQ5t3NzxL5+mkKqxc57W9PO9GRWybzsWnQwvG0XBoMU0n00qXMiVjGfCdzGcdku80qRtNTbL5OWPSgiR5Sc45X5V7Y8lUpaHk7a3zgQ/+haITyAlqux7bJtVGK4Zo78leiex3YbpcLH/gJ12jCqvPmFVJNAPZhw=="
    }
  ]
}
```

Una vez que tengamos la información de la transformación del CFDI, entonces usaremos un Formatter para presentar esta información en el formato columnar. Ejemplo
```python
from  pycfdi_transform.formatters import CFDI33Formatter
formatter = CFDI33Formatter(cfdi_data)
result_columns = formatter.format_object()
columns = formatter.get_columns_names()
print(result_columns) # Contenido del xml Ej: ['3.3', 'A5', '5511', ...]
print(columns) # Nombre de las columnas Ej: ['VERSION', 'SERIE', 'FOLIO', ...]
```
### Complements
La configuración de complementos para la clase **CFDI33SAXHandler** se define a través de *method chaining* que se obtiene a través de contruir una nueva instancia del Handler. Por defecto se encuentra activado el complemento de TimbreFiscalDigital 1.1, por lo que solo tendremos que configurar complementos adicionales de los cuales queramos obtener información.

**NOTA**: En caso de que declaremos un complemento y este no se encuentre en el XML no pasa nada, simplemente la llave del dictionary de python no se encontrará en el resultado obtenido, así entonces podemos tener una configuración avanzada para con el mismo código obtener multiples complementos según sea el caso.

**NOTA2**: Por temas de optimización en CFDI globales, se expone un método adicional para obtener la información de los conceptos.

#### Conceptos CFDI 3.3
En el caso de los conceptos del CFDI 3.3, por defecto estos campos no se obtienen ya que pocas veces se utilizan, sin embargo es posible obtener la información de los conceptos de la siguiente manera
```python
from  pycfdi_transform import CFDI33SAXHandler

path_xml = "./tests/Resources/cfdi33/cfdi33_01_utf8chars.xml"  #path xml que queremos transformar
transformer = CFDI33SAXHandler().use_concepts_cfdi33() # Cfdi 3.3 con obtención de conceptos.
cfdi_data = transformer.transform_from_file(path_xml)
print(cfdi_data) 
```
Así entonces nuestro resultado en caso de contener conceptos sería
```
{
  "cfdi33": {
    "version": "3.3",
    "serie": "VF",
    "folio": "001002004",
    ...
    "conceptos": [
      {
        "clave_prod_serv": "01010101",
        "no_identificacion": "prodüctoInventarió",
        "cantidad": "1.0000",
        "clave_unidad": "3G",
        "unidad": "",
        "descripcion": "Detalle factura",
        "valor_unitario": "10.0000",
        "importe": "10.00",
        "descuento": ""
      }
    ],
  },
  "tfd11": [
    {
      "version": "1.1",
      "no_certificado_sat": "20001000000300022323",
      "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
      ...
  ]
}
```

#### Nomina 1.2
Ejemplo para extraer adicionalmente la información del complemento de nomina 1.2, entonces al crear nuestra instancia podemos usar la siguiente configuración
```python
from  pycfdi_transform import CFDI33SAXHandler

path_xml = "./tests/Resources/nomina12/double_nomina01.xml"  #path xml que queremos transformar
transformer = CFDI33SAXHandler().use_nomina12() # Cfdi 3.3 con soporte para nomina12
cfdi_data = transformer.transform_from_file(path_xml)
print(cfdi_data) 
```
Así entonces nuestro resultado en caso de contener un complemento de nómina sería
```
{
  "cfdi33": {
    "version": "3.3",
    "serie": "VF",
    "folio": "001002004",
    ...
  },
  "tfd11": [
    {
      "version": "1.1",
      "no_certificado_sat": "20001000000300022323",
      "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
      ...
  ]
  "nomina12": [
    {
      "version": "1.2",
      "tipo_nomina": "E",
      ...
  ]
}
```

#### Pagos 1.0
Para el caso del complemento de pagos 1.0, entonces al crear nuestra instancia podemos usar la siguiente configuración
```python
from  pycfdi_transform import CFDI33SAXHandler

path_xml = "./tests/Resources/pagos10/pago10_01.xml"  #path xml que queremos transformar
transformer = CFDI33SAXHandler().use_pagos10() # Cfdi 3.3 con soporte para pagos10
cfdi_data = transformer.transform_from_file(path_xml)
print(cfdi_data) 
```
Así entonces nuestro resultado en caso de contener un complemento de pagos sería
```
{
  "cfdi33": {
    "version": "3.3",
    "serie": "VF",
    "folio": "001002004",
    ...
  },
  "tfd11": [
    {
      "version": "1.1",
      "no_certificado_sat": "20001000000300022323",
      "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
      ...
  ]
  "pagos10": [
    {
      "version": "1.0",
      "pago": [
        {
          "fecha_pago": "2019-03-29T16:14:52",
          ...
     ]
  ]
}
```

#### Impuestos Locales 1.0
Para el caso del complemento de Impuestos Locales 1.0, entonces al crear nuestra instancia podemos usar la siguiente configuración
```python
from  pycfdi_transform import CFDI33SAXHandler

path_xml = "./tests/Resources/implocal/cfdi33_implocal01.xml"  #path xml que queremos transformar
transformer = CFDI33SAXHandler().use_implocal10() # Cfdi 3.3 con soporte para impuestos locales 1.0
cfdi_data = transformer.transform_from_file(path_xml)
print(cfdi_data) 
```
Así entonces nuestro resultado en caso de contener un complemento de impuestos locales sería
```
{
  "cfdi33": {
    "version": "3.3",
    "serie": "VF",
    "folio": "001002004",
    ...
  },
  "tfd11": [
    {
      "version": "1.1",
      "no_certificado_sat": "20001000000300022323",
      "uuid": "9D81C696-0401-4F85-B703-6E0D3AFD6056",
      ...
  ]
  "implocal10": [
    {
      "total_traslados_impuestos_locales": "0.000000",
      "total_retenciones_impuestos_locales: "77.400000"
    }
  ]
}
```


### Configurations
La clase **CFDI33SAXHandler** contiene parámetros con los cuales se puede configurar el comportamiento al encontrar un valor opcional del XML que no se encuentra definido en el XML así como si debería utilizar numeros para cuando no se encuentre algún atributo numérico opcional. Estas opciones de configuración son 

 - **empty_char**: Valor para atributos opcionales en caso de no encontrarse en el XML.
 - **safe_numerics**: True o False para definir si utilizar el empty_char o no en los atributos de tipo númerico, por ejemplo Descuento.
 - **schema_validator**: Clase de tipo *lxml.etree.XMLSchema* para validar la estructura del XML antes de realizar la tranformación. Arroja excepcion de tipo *lxml.etree.DocumentInvalid* en caso de que no cumpla con la validación de XSD.

#### empty_char
Al definir un **empty_char** cuando se trate de un campo opcional entonces se mostrará este valor en caso de no contener algún valor en el XML. Ejemplo un XML que no contiene el atributo *Serie*. Este valor por  defecto está definido como un string vacio ''.
```python
from  pycfdi_transform import CFDI33SAXHandler

path_xml = "./tests/Resources/cfdi33/cfdi33_01.xml"  #path xml que queremos transformar
transformer = CFDI33SAXHandler(empty_char='#') # Cfdi 3.3
cfdi_data = transformer.transform_from_file(path_xml)
print(cfdi_data) 
```
```
{
  "cfdi33": {
    "version": "3.3",
    "serie": "#",
    "folio": "001002004",
...
```

#### safe_numerics
El atributo de la configuración safe_numerics tiene el objetivo de definir si se utiliza el empty_char en los atributos númericos, por ejemplo el Descuento, TipoCambio, entre otros.
```python
from  pycfdi_transform import CFDI33SAXHandler

path_xml = "./tests/Resources/cfdi33/cfdi33_01.xml"  #path xml que queremos transformar
transformer = CFDI33SAXHandler(safe_numerics=True) # Cfdi 3.3
cfdi_data = transformer.transform_from_file(path_xml)
print(cfdi_data) 
```
```
{
  "cfdi33": {
    ...,
    "descuento": "0.00",
    "total": "11.60",
    "moneda": "MXN",
    "tipo_cambio": "1.00",
    "tipo_comprobante": "I"
    
...
```
#### schema_validator
Para poder hacer uso de las validaciones de XSD es necesario construir un objeto de tipo  *lxml.etree.XMLSchema* para validar la estructura del XML antes de realizar la tranformación. 
Dentro de la librería existe un helper que construye una instancia de esta clase con todos los XSD de complementos del SAT para CFDI 3.3.

**Nota**: Arroja excepcion de tipo *lxml.etree.DocumentInvalid* en caso de que no cumpla con la validación de XSD.

Ejemplo de uso

```python
from pycfdi_transform import CFDI33SAXHandler, SchemaHelper
from lxml.etree import DocumentInvalid

xsd_validator = SchemaHelper.get_schema_validator_cfdi33() # Obtiene una instancia de clase lxml.etree.XMLSchema con los XSD del SAT.
path_xml = "./tests/Resources/cfdi33/cfdi33_01.xml"  #path xml que queremos transformar
transformer = CFDI33SAXHandler(schema_validator=xsd_validator, empty_char='#') # Cfdi 3.3 con validador de XSD.
try:
	cfdi_data = transformer.transform_from_file(path_xml)
	#CFDI válido, resultado en la variable cfdi_data
	print(cfdi_data) 
except DocumentInvalid as ex:
	print(f"Document invalid, error: {ex}")
```
NOTA: Se puede construir el objeto *lxml.etree.XMLSchema* de manera custom a manera de solo soportar algunos complementos y no todos, la documentación sobre esta clase la encuentras en la página de lxml [aquí](https://lxml.de/validation.html#xmlschema).
  
## Contributing
Pull requests son bienvenidos. Para cambios mayores, por favor abre un issue primero para poder discutir que deseas cambiar.
  
Asegurate de actualizar los tests de acuerdo a tus cambios.
  
### Testing
```python
python -m unittest discover
```
  
## License
[GNU](https://www.gnu.org/licenses/gpl-3.0.html)