import sys
import json
import argparse
import olefile
import xmltodict

parser = argparse.ArgumentParser(description='Extracts and converts data from Thermo XCalibur Method (.meth) files.')
parser.add_argument('FILENAME', help='The Thermo XCaliber .meth file to read.')
parser.add_argument('-s', '--stream', help='the data source you want to view (e.g. "Thermo Exactive")')
parser.add_argument('--to', help='the data type to convert to.', choices=['text', 'xml', 'json'], default='text')
parser.add_argument('--output', '-o', help='File to save data into, if desired.')

args = parser.parse_args()

with olefile.OleFileIO(args.FILENAME) as f:

    if args.stream:
        try:
            stream = f.openstream(args.stream).read()
        except OSError:  # Thermo Method files organize data into "Text" and "Data" formats
            substream = 'Text' if args.to == 'text' else 'Data'
            stream = f.openstream([args.stream, substream]).read()

        data = stream.decode('utf16')

        if args.to in ['text', 'xml']:
            output = data
        elif args.to == 'json':
            as_dict = xmltodict.parse(data)
            output = json.dumps(as_dict, indent=3)

        print(output, file=open(args.output, 'w') if args.output else sys.stdout)

    else:
        stream_names = set(el[0] for el in f.listdir())
        print(*stream_names, sep='\n', file=open(args.output, 'w') if args.output else sys.stdout)

