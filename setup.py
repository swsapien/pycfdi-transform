import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycfdi_transform",
    version="0.1.8.1",
    author="SW sapien",
    description="Cfdi Xml Transformation column format/csv",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swsapien/pycfdi-transform",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'XlsxWriter',
          'xlwt',
          'lxml'
    ],
    python_requires='>=3.7',
)