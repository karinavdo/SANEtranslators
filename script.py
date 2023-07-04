import os
from glob import glob
import re
import csv
import collections

INPUT_PATH = './input_test'
OUTPUT_PATH = './output_test'

environ = os.getenv( 'PYENV' )

if environ is not None and environ=='production':
    INPUT_PATH = '/input'
    OUTPUT_PATH = '/output'

filepaths = glob( f'{INPUT_PATH}/*.txt' )


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
    file_path = f'{OUTPUT_PATH}/{file_name}'
    with open( file_path, 'w', newline='', encoding='utf8' ) as csv_file:
        writer=csv.writer( csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC )
        writer.writerows( frequencies )
