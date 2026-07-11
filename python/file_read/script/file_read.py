import pandas as pd
import glob
import os
import openpyxl
from pathlib import Path
from datetime import datetime
from pprint import pprint
import random
import uuid
import time
"""
sample script to illustrate automated file processing

"""
# TODO: set relative path
relative_data_path = 'python/file_read/data'

# generating sample files to then ingest
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis',
              'Murray', 'Kinney', 'McNamara', 'Jouard', 'Robinson', 'McCoy',
              'Thomas', 'Thompson', 'Philips', 'Corum', 'White', 'Jones', 'Stevens',
              'Handcock', 'Carpenter', 'Hadley', 'Smith', 'Geno', 'Fuller']

for i in range(10):
    cases = random.randint(1, 20)
    print(f'for file {i}, generating {cases} rows')

    df = pd.DataFrame({
        'department': [random.choice(['marketing', 'data science', 'hr', 'accounting']) for _ in range(cases)],
        'last_name' : [random.choice(last_names) for _ in range(cases)],
        'salary': [random.randint(60000, 150000) for _ in range(cases)],
        'uid': [uuid.uuid4() for _ in range(cases)],  
        'file_id': i  
        })
        
    df.to_csv(f'{relative_data_path}/data_{i}.csv')
    
    # sleeping 4 seconds so we can have different time stamps
    time.sleep(4)

# list current directory
os.listdir(relative_data_path)

# getting all excel files from the folder
# lots of different ways to acomplish this based on specs
files = glob.glob(f'{relative_data_path}/*.csv')

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
        print(f'modified time: {modification_time:%Y-%m-%d %H:%M:%S}')
        print(f'created time:  {creation_time:%Y-%m-%d %H:%M:%S}')
    
        # appending file_info to files_dictionary
        files_list.append(file_info)
    
    else:
        print('file does not exist.')

pprint(files_list)

# last program run 
# I would generate this dynamically from latest case in database or newest file in an archive folder
# for this example, I'll generate a time that excludes a few files

creation_times = []
for file in files_list:
    print(file['creation_time'])
    creation_times.append(file['creation_time'])
creation_times
# sorting
creation_times.sort()
last_run = creation_times[3]
print(f'last_run dummy will be {last_run}')

# checking files created past deadline
files_to_process = [
    x['file'] 
    for x in files_list 
    if x['creation_time'] is not None and x['creation_time'] > last_run
]

len(files_to_process)

# initialize empty df
combined_df = pd.DataFrame()

# can do any individual file cleaning logic inside of this loop!
for file in files_to_process:
    print(file)
    file_read = pd.read_csv(file)
    print(file_read)
    combined_df = pd.concat([combined_df, file_read])

# display the combined data
print(combined_df.head())

# or we can now process / transform the entire set of files together
combined_df
combined_df['file_id'].unique()
