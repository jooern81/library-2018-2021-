# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:27:59 2020

@author: chinjooern
"""
#assumes all files in folder are excel files and that excel files in folder are desired in the final sheet

import os
import pandas as pd

path = os.getcwd()
files = os.listdir(path)
files_xls = [f for f in files if f[-4:] == 'xlsx']

df = pd.DataFrame()

for f in files_xls:
    k = f.split("_")
    data = pd.read_excel(f, "EventsReportTemplate")
    df = df.append(data)

df.to_excel("CABLE_MASTERLIST.xlsx")
   