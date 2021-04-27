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

lh_df = pd.read_excel('LEARNING HISTORY2.xlsx', skiprows = 2)

n_df = pd.read_excel('NAMES.xlsx')

name_list = list(n_df['Personnel Number'])

output = []

for df_entry in range(1,len(lh_df)):
    if lh_df['Name'][df_entry] in name_list:
        output.append([lh_df['Name'][df_entry], lh_df['Department'][df_entry], lh_df['Division'][df_entry], lh_df['completion_id'][df_entry], lh_df['completion_status'][df_entry], lh_df['completion_date'][df_entry], lh_df['credit_hours'][df_entry]])
        
df = pd.DataFrame(output, columns = ['Name', 'Department', 'Division', 'completion_id', 'completion_status', 'completion_date', 'credit_hours'])
df.to_excel('FILTERED LEARNING HISTORY.xlsx')

