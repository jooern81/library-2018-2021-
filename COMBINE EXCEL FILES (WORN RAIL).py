# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:16:15 2020

@author: chinjooern
"""

import os
import pandas as pd

path = os.getcwd()
files = os.listdir(path)
files_xls = [f for f in files if f[-4:] == 'xlsx']

df = pd.DataFrame(columns = ["SECTOR", "DATE", "Milage\n[km]","Gauge\n[mm]","Vert. wear r.\n[mm]","Hor. wear 45° l\n[mm]","Hor. wear 45° r\n[mm]","Events", "Cant\n[mm]","Twist\n[mm]","Hor. wear l.\n[mm]","Hor. wear r.\n[mm]","Vert. wear l.\n[mm]"])

cable_list = []

for f in files_xls:
    try:
        SECTOR = f.split("_")[2] + "_" + f.split("_")[3]
        DATE = f.split("_")[0]
        data = pd.read_excel(f)      #data = pd.read_excel(f, skiprows=34) data = pd.read_excel(f, usecols=cols, skiprows=34)
        for i in range(0,len(data)):
            if (data.iloc[i][list(data.columns)[0]] == 'Milage\n[km]') == True:
                data = pd.read_excel(f, skiprows=i+1)
                data['SECTOR'] = SECTOR
                data['DATE'] = DATE
                cable_list.append(data)
                break
                
    except:
        print(f)


df = pd.concat(cable_list, axis=0, sort = True) # reduces memory requirements compared to appending in for statement


# for col_name in col_names: 
#     try:
#         if "None" in str(col_name) == True:
#             unname_cols_list.append(col_names.index(col_name))
#             print("COL NAME APPENDED")
#     except:
#         print("NO NAME COLUMN")
    
# df = df.drop(unnamed_cols_list)

#df = df.dropna()
#df = df.drop_duplicates('Chainage', keep='last')
df.to_excel("RAIL_MASTERLIST.xlsx")
   