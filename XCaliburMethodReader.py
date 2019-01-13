#!/usr/bin/env python
import sys
import json
import argparse
import olefile
import xmltodict
import pandas as pd
import numpy as np


def load_lc_data(filename):
    """Returns dict of LC data, given a Thermo Methods (.meth) filename."""
    with olefile.OleFileIO(filename) as f:
        lc_stream = [name for name in f.listdir() if len(name) == 2 and 'LC' in name[0] and 'Data' in name[1]]
        assert len(lc_stream) == 1
        lc_stream = lc_stream[0]
        lc_data = f.openstream(lc_stream).read().decode('utf-8')
        return xmltodict.parse(lc_data)


def get_lc_gradient(lc_data):
    """Returns Pandas DataFrame with the LC Gradient sequence."""
    gradient = pd.DataFrame(lc_data['gradients']['methodgradient'])
    gradient = gradient.astype(int)
    gradient.set_index('order', inplace=True)
    gradient['time (min)'] = gradient['duration'].cumsum() / 60
    return gradient


def get_lc_settings(lc_data):
    """Returns Pandas DataFrame with LC Flow, MaxPressure, etc settings, given dict of lc data."""
    lcp = {key: val for key, val in lc_data.items() if not 'wash' in key and any(['Flow' in key, 'Volume' in key, 'MaxPressure' in key])}
    prefixes = [key[:-4] for key in lcp if 'Flow' in key]
    data = []
    for prefix in prefixes:
        dd = {'step': prefix}
        for value in ['Volume', 'Flow', 'MaxPressure']:
            try:
                dd[value] = lcp[prefix + value]
            except KeyError:
                pass
        data.append(dd)

    df = pd.DataFrame(data)
    df.set_index('step', inplace=True, )
    df.replace('Not set', np.nan, inplace=True)
    df = df.astype(float)
    return df


def main(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(description='Extracts and converts data from Thermo XCalibur Method (.meth) files.')
    parser.add_argument('FILENAME', help='The Thermo XCaliber .meth file to read.')
    parser.add_argument('-s', '--stream', help='the data source you want to view (e.g. "Thermo Exactive")')
    parser.add_argument('--to', help='the data type to convert to.', choices=['text', 'xml', 'json'], default='text')
    parser.add_argument('--output', '-o', help='File to save data into, if desired.')

    args = parser.parse_args(args=args)

    with olefile.OleFileIO(args.FILENAME) as f:

        if args.stream:
            try:
                stream = f.openstream(args.stream).read()
            except OSError:  # Thermo Method files organize data into "Text" and "Data" formats
                substream = 'Text' if args.to == 'text' else 'Data'
                stream = f.openstream([args.stream, substream]).read()

            try:
                data = stream.decode('utf16')
            except UnicodeDecodeError:
                data = stream.decode('utf8')


            # Remove garbage characters at front of some strings if parsing xml data.
            if args.to in ['xml', 'json']:
                data = data[data.index('<?xml'):]

            if args.to in ['text', 'xml']:
                output = data
            elif args.to == 'json':
                as_dict = xmltodict.parse(data)
                output = json.dumps(as_dict, indent=3)

            print(output, file=open(args.output, 'w') if args.output else sys.stdout)

        else:
            stream_names = set(el[0] for el in f.listdir())
            print(*stream_names, sep='\n', file=open(args.output, 'w') if args.output else sys.stdout)


if __name__ == '__main__':
    main(sys.argv[1:])