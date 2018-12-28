# XCalibur Method File Reader

A simple command-line program for mass spectrometry researchers that extracts and converts data from Thermo XCalibur Method (.meth) files.

Uses the [olefile](https://olefile.readthedocs.io/en/latest/Howto.html) Python package to extract the data.

## Installation


## Usage

Help Text:
```
>>> XCaliburMethodReader --help

usage: XCaliburMethodReader.py [-h] [-s STREAM] [--to {text,xml,json}]
                               [--output OUTPUT]
                               FILENAME

Extracts and converts data from Thermo XCalibur Method (.meth) files.

positional arguments:
  FILENAME              The Thermo XCaliber .meth file to read.

optional arguments:
  -h, --help            show this help message and exit
  -s STREAM, --stream STREAM
                        the data source you want to view (e.g. "Thermo
                        Exactive")
  --to {text,xml,json}  the data type to convert to.
  --output OUTPUT, -o OUTPUT
                        File to save data into, if desired.


```

Print File's Directory:
```bash
>>> XCaliburMethodReader HelaStandard120.meth

Proxeon_EASY-nLC
LCQ Header
AuditData
Thermo Exactive
```

Pretty-Print Data
```bash
>>> XCaliburMethodReader HelaStandard120.meth -s "Thermo Exactive"

                           Method of Q Exactive HF-X

OVERALL METHOD SETTINGS

Global Settings
Use lock masses                                                         best
Lock mass injection                                                        ―
Chrom. peak width (FWHM)                                                  15 s
Time
Method duration                                                       120.00 min
...
```

Extract and/or convert Data to machine-readable formats

XML:
```bash
>>> XCaliburMethodReader HelaStandard120.meth -s "Thermo Exactive" --to xml

<?xml version="1.0" encoding="utf-16" standalone="yes"?>
<InstrumentSetupMethod guid="a0742e44-9001-4c98-ac3c-7e5e366c6196" TargetInstrument="Deukalion" version="1.1" FullInternalName="Framework.Method" date="2018-11-06 10:38:12Z">
  <Description>Method</Description>
  <Segments>
    <Segment FullInternalName="Framework.Segment" id="1">
      <ScanEvent guid="553826f1-95e1-4570-a984-c77b91722f6d" id="1" FullInternalName="Deukalion.TopN.4" DescendantType="Child">
        <Expanded FullInternalName="bool">false</Expanded>
...
```

JSON:
```bash
>>> XCaliburMethodReader HelaStandard120.meth -s "Thermo Exactive" --to json

{
   "InstrumentSetupMethod": {
      "@guid": "a0742e44-9001-4c98-ac3c-7e5e366c6196",
      "@TargetInstrument": "Deukalion",
      "@version": "1.1",
      "@FullInternalName": "Framework.Method",
...
```

Save output to a file:
```bash
>>> XCaliburMethodReader HelaStandard120.meth -s "Thermo Exactive" --to json -o myfile.json
```

## Todo

  - Get the header stream to read correctly
  - Provide a metadata extractor  