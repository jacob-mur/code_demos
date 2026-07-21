import pandas as pd
import numpy as np
import palmerpenguins as pp

# loading penguins data
penguins = pp.load_penguins()

penguins.info()

################################################################
# .loc --  data by label (the actual index value or column name)
################################################################

# selecting by row index
penguins.loc[0]
penguins.head(1)

# single cell
penguins.loc[0, 'species']

# selecting column (row,column)
penguins.loc[:, ['species']] 

penguins['species'] == 'Adelie'

penguins.loc[penguins['species'] == 'Adelie']

# checking index of penguins
penguins.index

penguins_index = penguins.set_index('species')

# checking index of penguins_index
penguins_index.index.unique()

# so now we can .loc two labels (index label string and column)
penguins_index.loc['Adelie', 'island']

penguins_index.loc['Adelie', 'island'].unique()

# check why this won't work!
penguins_index.loc[0]

# but this will!
penguins_index.head(1)

# index subsetting
string = 'hello'
string[2]

# syntax 'sugar' for dunder method (double under)
string.__getitem__(2)

penguins.__getitem__('species')

##########################################
# .iloc -- select data by integer position
##########################################

# select row
penguins.iloc[0]

## checking equivalent  
penguins.loc[0] == penguins.iloc[0]
all(penguins.loc[0]) == all(penguins.iloc[0])

# single cell
penguins.iloc[0, 0]

############################
# [] direct bracket indexing 
############################

penguins['species']

# good rule of thumb #
# read columns with df['col']
# select and set everything else with .loc (when you know the label) 
# or .iloc (when you know the position).


##############################
# additional ways to do things 
##############################

penguins[penguins['species'].isin(['Adelie', 'Chinstrap'])]

## again returns an array of bools
penguins['species'].isin(['Adelie', 'Chinstrap'])

# query -- pretty flexible! (just watch quotes)
penguins.query('species == "Adelie" and island == "Torgersen"')

penguins.query('species == "Adelie" & island == "Torgersen"')
