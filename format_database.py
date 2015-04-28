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

    output_seqs = {}
    output_descriptors = {}
    for entry in open(args.input_fp, 'U'):
        ID = parse_ID(entry)
        tax = parse_taxonomy(entry)
        seq = parse_sequence(entry)
        if tax_filt(tax, number_levels) and seq_filt(seq, length_min):
            output_seqs[ID] = seq
            output_descriptors[ID] = tax



def parse_ID(line):
    if not line.startswith("processid"):
        columns = line.rstrip("\n").split("\t")
        return columns[0]


def parse_taxonomy(line):
    columns = line.rstrip("\n").split("\t")
    phylum = columns[8]
    classes = columns[10]
    order = columns[12]
    family = columns[14]
    subfamily = columns[16]
    genus = columns[18]
    species = columns[20]
    taxonomy_string = "p__" + phylum + ";c__" + classes + ";o__" + order + ";f__" + family + ";sf__" + subfamily + ";g__" + genus + ";s__" + species
    return taxonomy_string


def parse_sequence(line):
    if not line.startswith("processid"):
        columns = line.rstrip("\n").spit("\t")
        Nuc_Seq = columns[42]
        if Nuc_Seq =="":
            return "NA"
        if Nuc_Seq == " ":
            return "NA"
        else:
            return Nuc_Seq                                                                         


def tax_filt(tax):
    pass


def seq_filt(seq):
    pass


def format_taxonomy(tax):
    pass


if __name__ == "__main__":
    main()
