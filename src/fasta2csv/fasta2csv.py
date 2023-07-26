#! /usr/bin/env python3
"""
=============
+ fasta2csv +
=============

author: Josh Tompkin
contact: tompkinjo@gmail.com
home: https://github.com/jtompkin/fasta2csv
"""
import argparse
import sys
import os

def delim2fasta():
    pass

def fasta2delim():
    pass

def _main():
    """Parse arguments and call appropriate functions"""
    parser = argparse.ArgumentParser(prog='fasta2csv',
                                     description='Convert between fasta and delimited text')
    
    parser.add_argument('file', help="Path to file to be converted. Reads from stdin if '-' is given")

if __name__ == '__main__':
    _main()