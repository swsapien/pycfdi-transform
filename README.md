# PyCfdi

PyCfdi Transform es un paquete de python que te permite convertir un Xml CFDI México a formato columnar.

Cfdi 3.3 y 3.2 con complementos:
    Nomina12 ( cfdi 3.3 )
    Nomina ( cfdi 3.2 )}
    Pagos10 ( cfdi 3.3)

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
### XSLT Transformation
```python
import pycfdi_transform as ct

path_xml = "./tests/Resources/cfdi33_01.xml" #path xml que queremos transformar
transformer = ct.TCfdi33() # Cfdi 3.3
result_columns = transformer.to_columns_from_file(path_xml)
print(result_columns[0]) # Contenido del xml
print(transformer.get_column_names()) # Cabeceras del contenido del xml
```
### SAX Transformation
```python
import pycfdi_transform as ct

path_xml = "./tests/Resources/cfdi33_01.xml" #path xml que queremos transformar
transformer = ct.TSaxCfdi33() # Cfdi 3.3
result_columns = transformer.to_columns_from_file(path_xml)
print(result_columns[0]) # Contenido del xml
print(transformer.get_column_names()) # Cabeceras del contenido del xml
```

## Contributing
Pull requests son bienvenidos. Para cambios mayores, por favor abre un issue primero para poder discutir que deseas cambiar.

Asegurate de actualizar los tests de acuerdo a tus cambios.

### Testing
```python
 python -m unittest discover
```

## License
[GNU](https://www.gnu.org/licenses/gpl-3.0.html)
