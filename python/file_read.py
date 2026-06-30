import pandas as pd
import glob
import os
import openpyxl
from pathlib import Path
from datetime import datetime
from pprint import pprint


"""
sample script to illustrate automated file processing
SETUP: create sample project structure with data folder

"""


# list current directory
os.listdir('sample_project/data')

# Getting all excel files from the folder
# lots of different ways to acomplish this based on specs
files = glob.glob('sample_project/data/*.xlsx')

# creating file metadata profile
files_list = []


# checking file creation time
for file in files: 

    print(file)
    file_path = Path(file)
    print(type(file_path))

    if file_path.exists():
        # get file stats
        file_stat = file_path.stat()
        print(file_stat)
        
        # 1. get modified time
        modification_time = datetime.fromtimestamp(file_stat.st_mtime)
        
        # 2. get created time (platform-dependent)
        try:
            # mac/linux (if supported by the filesystem)
            creation_time = datetime.fromtimestamp(file_stat.st_birthtime)
        except AttributeError:
            # fallback approach for Windows, or metadata change time on Unix
            creation_time = datetime.fromtimestamp(file_stat.st_ctime)

        # creting individual file dictionary
        file_info = {
            'file': file,
            'creation_time':f'{modification_time:%Y-%m-%d %H:%M:%S}',
            'modification_time':f'{creation_time:%Y-%m-%d %H:%M:%S}'
        }

        # output human-readable timestamps
        print(f"modified time: {modification_time:%Y-%m-%d %H:%M:%S}")
        print(f"created time:  {creation_time:%Y-%m-%d %H:%M:%S}")
    
        # appending file_info to files_dictionary
        files_list.append(file_info)
    
    else:
        print("file does not exist.")

pprint(files_list)

# last program run 
# I would generate this dynamically from latest case in database or newest file in an archive folder
last_run = '2026-06-16 16:51:00'

# checking files created past deadline
files_to_process = [
    x['file'] 
    for x in files_list 
    if x['creation_time'] is not None and x['creation_time'] > last_run
]

# initialize empty df
combined_df = pd.DataFrame()

# can do any individual file cleaning logic inside of this loop!
for file in files_to_process:
    print(file)
    file_read = pd.read_excel(file, header=1)
    print(file_read)
    combined_df = pd.concat([combined_df, file_read])

# display the combined data
print(combined_df.head())

# or we can now process / transform the entire set of files together
combined_df
