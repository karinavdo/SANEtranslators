import os
import sys
from glob import glob
import re
import csv
import collections
import shutil

INPUT_PATH = './input_test'
OUTPUT_PATH = './output_test'

paths = { 
   'input_path': INPUT_PATH,
   'output_path': OUTPUT_PATH
   }

def set_paths( cmd_arg, paths ):
    if( len( cmd_arg ) == 2 ):
       if( cmd_arg[0] == '-i' ):
        paths['input_path'] = cmd_arg[1]
       if( cmd_arg[0] == '-o' ):
        paths['output_path'] = cmd_arg[1]

# As per spec, so I'm assuming no need for argparse
# or other over engineered thingies. 
args = sys.argv[1:]
for arg1, arg2 in zip( args[::2], args[1::2]):
   set_paths( (arg1, arg2), paths)

isbns_filepath = f'{paths["input_path"]}/isbns.csv'
if( os.path.isfile( isbns_filepath ) ):
    shutil.copyfile( isbns_filepath, f'{paths["output_path"]}/isbns.csv' )
        
filepaths = glob( f'{paths["input_path"]}/*.txt' )

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
    file_path = f'{paths["output_path"]}/{file_name}'
    with open( file_path, 'w', newline='', encoding='utf8' ) as csv_file:
        writer=csv.writer( csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC )
        writer.writerows( frequencies )
