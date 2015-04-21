#!/usr/bin/env python

__author__ = 'Jonathan Leff'
__email__ = 'jonthan.leff@colorado.edu'
__version__ = ''

import argparse


parser = argparse.ArgumentParser(description='Format marker gene sequences from online '
                                             'database so that they can be used with a '
                                             'sequence classifier such as the RDP classifier')
parser.add_argument('-i', '--input_fp', required=True,
                    help='The sequences from the database in their native format')
parser.add_argument('-t', '--format_type',
                    help='The format type of the input sequences')
parser.add_argument('-o', '--output_dir', required=True,
                    help='The output directory')

def main():
    args = parser.parse_args()




if __name__ == "__main__":
    main()