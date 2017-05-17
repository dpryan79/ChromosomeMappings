#!/usr/bin/env python
from __future__ import print_function

import argparse
import sys


def strip_chr_from_str(s):
    ret = s
    if s.startswith('CHR_'):
        ret = s[4:]
    elif s.startswith('chr'):
        ret = s[3:]
    return ret


def main():
    parser = argparse.ArgumentParser(description='Replace chromosome names in a tabular (e.g. VCF) file using a mapping file.')
    parser.add_argument('-m', dest='mapping_file', type=argparse.FileType(), required=True, help='mapping file. Must contain 2 tab-separated columns')
    parser.add_argument('--cols', required=True, help='comma-separated list of column indexes (starting from 1) on which to perform the replacement')
    parser.add_argument('--strip-chr', action='store_true', default=False, help='strip "CHR_" or "chr" after replacing')
    parser.add_argument('--comment-char', help='lines starting with this character will be directly printed to the output file')
    parser.add_argument('-o', dest='output', type=argparse.FileType('w'), default=sys.stdout, help='output file. If not specified, writes on standard output')
    parser.add_argument('input', metavar='INPUT', type=argparse.FileType(), help='tabular input file')
    args = parser.parse_args()

    map_hash = dict()
    for line in args.mapping_file:
        line = line.rstrip('\r\n')
        line_cols = line.split('\t')
        if len(line_cols) < 2:
            raise Exception("Line '%s' in mapping file does not contain 2 tab-separated columns" % line)
        line_col1 = line_cols[1]
        if args.strip_chr:
            line_col1 = strip_chr_from_str(line_col1)
        map_hash[line_cols[0]] = line_col1

    cols_to_map = [int(_) - 1 for _ in args.cols.split(',')]

    for line in args.input:
        line = line.rstrip('\r\n')
        if args.comment_char and line.startswith(args.comment_char):
            print(line, file=args.output)
        else:
            line_cols = line.split('\t')
            for col_to_map in cols_to_map:
                old_value = line_cols[col_to_map]
                new_value = map_hash.get(old_value)
                if new_value is None:
                    if args.strip_chr:
                        new_value = strip_chr_from_str(old_value)
                    else:
                        new_value = old_value
                line_cols[col_to_map] = new_value
            mapped_line = '\t'.join(line_cols)
            print(mapped_line, file=args.output)


if __name__ == "__main__":
    main()
