# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:03:48 2021

@author: chinjooern
"""


import pandas as pd
import csv
import datetime
import math
from pandas._libs.tslibs.timestamps import Timestamp
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



n_df = pd.read_excel('PWY NOMINAL ROLL.xlsx')

ck_df = pd.read_excel('CLEARED KAIZEN.xlsx')

name_list1 = list(n_df['name'])
name_list2 = list(ck_df['name'])

for name_id in range(0,len(name_list2)):
    split_name = name_list2[name_id].split('(')
    split_name.pop(len(split_name)-1) 
    new_name = ''
    for sub_name in split_name:
        new_name = new_name + sub_name
        
    name_list2[name_id] = new_name

output = []
fuzzy_check = []

for df_entry in range(0,len(n_df)):
    for name2 in name_list2:
        if fuzz.token_sort_ratio(n_df['name'][df_entry],name2) > n_df['fuzzy_score'][df_entry]:
            n_df['fuzzy_score'][df_entry] = fuzz.token_sort_ratio(n_df['name'][df_entry],name2)
            n_df['fuzzy_name'][df_entry] = name2

df = n_df.drop(n_df[n_df.fuzzy_score > 90].index)

df.to_excel('NEVER CLEAR KAIZEN.xlsx')

