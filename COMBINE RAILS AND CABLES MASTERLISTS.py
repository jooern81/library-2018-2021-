# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:52:12 2020

@author: chinjooern
"""

import pandas as pd

cdf = pd.read_excel('CABLE_MASTERLIST.xlsx')
cdf = cdf.dropna(axis=0, subset=['Position']) #drop rows with 'Position' Column entry empty
rdf = pd.read_excel('RAIL_MASTERLIST.xlsx')
rdf = rdf.dropna(axis=0, subset=['Milage\n[km]']) #drop rows with 'Milage\n[km]' Column entry empty
rdf['Milage\n[km]'] = rdf['Milage\n[km]'].apply(str) 
rdf['Milage\n[km]'] = rdf['Milage\n[km]'].str.replace(r'#', '')

def fix_cdf_chainage(bad_chainage):
    split_chainage = str(bad_chainage['Position']).split(" ")
    split_chainage = split_chainage[0]
    correct_chainage = round(float(split_chainage) * 1000)
    bad_chainage = correct_chainage
    
    return(bad_chainage) 
    

def cdf_chainage_processing(df):
    df.fillna("0", inplace = True)
    df_chainage = df.apply(fix_cdf_chainage, axis=1) #this creates a new dataframe with only one column
    df = pd.concat([df,df_chainage], axis=1)
    df.columns.values[len(df.columns)-1] = "CORRECT_CHAINAGE"
    
    return(df,df_chainage)

def fix_rdf_chainage(bad_chainage):
    bad_chainage = float(bad_chainage['Milage\n[km]'])
    correct_chainage = round(float(bad_chainage) * 1000)
    bad_chainage = correct_chainage
    return(bad_chainage) 
    

def rdf_chainage_processing(df):
    df.fillna("0", inplace = True)
    df_chainage = df.apply(fix_rdf_chainage, axis=1) #this creates a new dataframe with only one column
    df = pd.concat([df,df_chainage], axis=1)
    df.columns.values[len(df.columns)-1] = "CORRECT_CHAINAGE" 
    return(df,df_chainage)

    
(cdf, cdf_chainage) = cdf_chainage_processing(cdf)
(rdf, rdf_chainage) = rdf_chainage_processing(rdf)

cdf = cdf.sort_values(by=['DATE'])
cdf = cdf.drop_duplicates(subset = ['CORRECT_CHAINAGE', 'SECTOR'], keep="last")
cdf.to_excel("PROCESSED_CABLE_MASTERLIST.xlsx")

rdf = rdf.sort_values(by=['DATE'])
rdf = rdf.drop_duplicates(subset = ['CORRECT_CHAINAGE', 'SECTOR'], keep="last")
rdf.to_excel("PROCESSED_RAIL_MASTERLIST.xlsx")

mergedStuff = pd.merge(cdf, rdf, on=['CORRECT_CHAINAGE', 'SECTOR'], how='right')

mergedStuff.to_excel("RAILS_AND_CABLES.xlsx")