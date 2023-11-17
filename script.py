import os
import sys
from glob import glob
import re
import csv
import collections
import shutil
import argparse

INPUT_PATH = './test_dirs/input_test'
OUTPUT_PATH = './test_dirs/output_test'
TMP_PATH = './test_dirs/tmp_test'

parser = argparse.ArgumentParser()
parser.add_argument( '-i', '--input_path', help='input folder', default=INPUT_PATH )
parser.add_argument( '-o', '--output_path', help='output folder', default=OUTPUT_PATH )
parser.add_argument( '-t', '--temp', help='temp folder', default=TMP_PATH )

args = parser.parse_args()

isbns_filepath = f'{args.input_path}/isbns.csv'
if( os.path.isfile( isbns_filepath ) ):
    shutil.copyfile( isbns_filepath, f'{args.output_path}/isbns.csv' )
        
filepaths = glob( f'{args.input_path}/*.txt' )

frequency_lists={}
for filepath in filepaths:
    with open( filepath, 'r', encoding='utf8' ) as text_file:
        text = text_file.read()
        text = text.lower()
        text = re.sub( '[\.,\'\":;\?\!\(\)]+', '', text )
        tokens = text.split()
        frequencies = collections.Counter( tokens )
        frequency_lists[filepath] = frequencies.most_common()

for file_name, frequencies in frequency_lists.items():
    file_name = file_name.split( '/' )[-1]
    file_name = file_name.replace( '.txt', '.csv' )
    file_path = f'{args.output_path}/{file_name}'
    with open( file_path, 'w', newline='', encoding='utf8' ) as csv_file:
        writer=csv.writer( csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC )
        writer.writerows( frequencies )
