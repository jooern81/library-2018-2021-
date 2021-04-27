# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:15:42 2021

@author: chinjooern

Instructions: 
    Ensure pandas library is installed
    Put this python file in the same folder as all the 'xlsx' files you want to combine and run the script
    If you have different file types that are tables that you want to combine, refer to the comments in the code to add additional extensions to be considered


"""

import os
import pandas as pd
import xlrd

path = os.getcwd()
files = os.listdir(path)
files_xls = [f for f in files if f[-4:] == 'xlsx' or f[-4:] == 'xlsm']      #check the file type/extension, for multiple extensions, use files_xls = [f for f in files if (f[-4:] == 'xlsx' or f[-4:] == 'xlsm' or f[-3:] == 'csv' or f[-3:] == 'xls'] 

df = pd.DataFrame()

for f in files_xls:
    xls = xlrd.open_workbook(path + '\\' + f)
    for sheet_name in xls.sheet_names():
        print(f,sheet_name)
        try:
            string_int = int(sheet_name)
            if type(string_int) == int:
                print('INCLUDED SHEET: ' + str(string_int))
                df = df.append(pd.read_excel(f, sheet_name=sheet_name, skiprows=14), ignore_index=True)
        except:
            print('EXCLUDED SHEET: ' + sheet_name)


df.to_excel("combined_files.xlsx")      #assign name of the excel file you want to output the combined files as
   

