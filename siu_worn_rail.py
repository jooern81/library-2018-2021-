# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:14:25 2021

@author: jooer
"""

import pandas as pd
import datetime

# p6df = pd.read_excel('Stacked_Phase6.xlsx')
# p6df.to_pickle("./p6df.pkl")

# p7df = pd.read_excel('Stacked_Phase7.xlsx')
# p7df.to_pickle("./p7df.pkl")

# p8df = pd.read_excel('Stacked_Phase8.xlsx')
# p8df.to_pickle("./p8df.pkl")

# trdf = pd.read_excel('TR_Works.xlsx')
# trdf.to_pickle("./trdf.pkl")

p6df = pd.read_pickle("./p6df.pkl")
p7df = pd.read_pickle("./p7df.pkl")
p8df = pd.read_pickle("./p8df.pkl")
trdf = pd.read_pickle("./trdf.pkl")
trdf = trdf.reset_index(drop=True)

def extract_columns_ltt(df):

            
    df = df[['Sector','Milage\n[m]','Hor. wear 45° l\n[mm]','Hor. wear 45° r\n[mm]','Vert. wear l\n[mm]','Vert. wear r\n[mm]','Sum L (horz 45deg + vert)',
           'Sum R (horz 45deg + vert)','Date','SI L (PWY)','SI R (PWY)'  ]]
       
    dfl = df[df['SI L (PWY)'] == 'SI U']
    dfr = df[df['SI R (PWY)'] == 'SI U']
    df = pd.concat([dfl,dfr],ignore_index=True)
    df = pd.DataFrame.drop_duplicates(df)
    
    df = df.reset_index(drop=True)
    
    for df_entry in range(0,len(df)):
        if type(df['Sector'][df_entry]) == str:
            df['Sector'][df_entry] = df['Sector'][df_entry][:-3]


            df['Date'][df_entry] = str(df['Date'][df_entry])
            
    return(df)

def extract_columns_tr(df):
    

    df = df[['Date','Sector','Chainage Low','Chainage High','Left/Right']]

    for trdf_entry in range(0,len(df)):

        if type(df['Sector'][trdf_entry]) == str:
            df['Sector'][trdf_entry] = df['Sector'][trdf_entry].replace(" ", "")
        df['Date'][trdf_entry] = int(df['Date'][trdf_entry].strftime('%Y%m%d'))


    return(df)

p6df = extract_columns_ltt(p6df)
p7df = extract_columns_ltt(p7df)
p8df = extract_columns_ltt(p8df)
trdf = extract_columns_tr(trdf)

cdf = pd.concat([p6df,p7df,p8df])
cdf = cdf.sort_values(by=['Date','Sector','Milage\n[m]'])
cdf = cdf.reset_index(drop=True)
cdf['TR REPLACED DATE L'] = 'NEVER'
cdf['TR REPLACED DATE R'] = 'NEVER'
cdf['AGE L'] = 'N/A'
cdf['AGE R'] = 'N/A'
cdf['EARLIEST EARLIER RECORD L'] = 'N/A'
cdf['EARLIEST EARLIER RECORD R'] = 'N/A'
cdf['EARLIEST Hor. wear 45° l\n[mm]'] = 'N/A'
cdf['EARLIEST Hor. wear 45° r\n[mm]'] = 'N/A'
cdf['EARLIEST Vert. wear l\n[mm]'] = 'N/A'
cdf['EARLIEST Vert. wear r\n[mm]'] = 'N/A'
cdf['EARLIEST Sum L (horz 45deg + vert)'] = 'N/A'
cdf['EARLIEST Sum R (horz 45deg + vert)'] = 'N/A'

for cdf_entry in range(0,len(cdf)):
    for trdf_entry in range(0,len(trdf)):
        if cdf['Sector'][cdf_entry] == trdf['Sector'][trdf_entry] and cdf['Date'][cdf_entry] < trdf['Date'][trdf_entry]:

            if cdf['Milage\n[m]'][cdf_entry] > trdf['Chainage Low'][trdf_entry] - 3 and cdf['Milage\n[m]'][cdf_entry] < trdf['Chainage High'][trdf_entry] + 3:

                if (cdf['SI R (PWY)'][cdf_entry] == 'SI U' and (trdf['Left/Right'][trdf_entry] == 'Right') ):
                    cdf['TR REPLACED DATE R'][cdf_entry] = trdf['Date'][trdf_entry]
                    days = int(str(trdf['Date'][trdf_entry])[6:8]) - int(str(cdf['Date'][cdf_entry])[6:8])
                    months = int(str(trdf['Date'][trdf_entry])[4:6]) - int(str(cdf['Date'][cdf_entry])[4:6])
                    years = int(str(trdf['Date'][trdf_entry])[:4]) - int(str(cdf['Date'][cdf_entry])[:4])
                    cdf['AGE R'][cdf_entry] =   days + months*30 + years*365
   
    if (cdf['SI R (PWY)'][cdf_entry] == 'SI U' and (cdf['TR REPLACED DATE R'][cdf_entry] == 'NEVER') ):
          days = int(datetime.datetime.now().strftime('%Y%m%d')[6:8]) - int(str(cdf['Date'][cdf_entry])[6:8])
          months = int(datetime.datetime.now().strftime('%Y%m%d')[4:6]) - int(str(cdf['Date'][cdf_entry])[4:6])
          years = int(datetime.datetime.now().strftime('%Y%m%d')[:4]) - int(str(cdf['Date'][cdf_entry])[:4])
          cdf['AGE R'][cdf_entry] = days + months*30 + years*365


for cdf_entry in range(0,len(cdf)):
    for trdf_entry in range(0,len(trdf)):
        if cdf['Sector'][cdf_entry] == trdf['Sector'][trdf_entry] and cdf['Date'][cdf_entry] < trdf['Date'][trdf_entry]:

            if cdf['Milage\n[m]'][cdf_entry] > trdf['Chainage Low'][trdf_entry] - 3 and cdf['Milage\n[m]'][cdf_entry] < trdf['Chainage High'][trdf_entry] + 3:

                if (cdf['SI L (PWY)'][cdf_entry] == 'SI U' and trdf['Left/Right'][trdf_entry] == 'Left'):
                    cdf['TR REPLACED DATE L'][cdf_entry] = trdf['Date'][trdf_entry]
                    days = int(str(trdf['Date'][trdf_entry])[6:8]) - int(str(cdf['Date'][cdf_entry])[6:8])
                    months = int(str(trdf['Date'][trdf_entry])[4:6]) - int(str(cdf['Date'][cdf_entry])[4:6])
                    years = int(str(trdf['Date'][trdf_entry])[:4]) - int(str(cdf['Date'][cdf_entry])[:4])
                    cdf['AGE L'][cdf_entry] =   days + months*30 + years*365
    if (cdf['SI L (PWY)'][cdf_entry] == 'SI U' and (cdf['TR REPLACED DATE L'][cdf_entry] == 'NEVER') ):
          days = int(datetime.datetime.now().strftime('%Y%m%d')[6:8]) - int(str(cdf['Date'][cdf_entry])[6:8])
          months = int(datetime.datetime.now().strftime('%Y%m%d')[4:6]) - int(str(cdf['Date'][cdf_entry])[4:6])
          years = int(datetime.datetime.now().strftime('%Y%m%d')[:4]) - int(str(cdf['Date'][cdf_entry])[:4])
          cdf['AGE L'][cdf_entry] = days + months*30 + years*365

for cdf_entry in range(0,len(cdf)):
    for later_cdf_entry in range(cdf_entry,len(cdf)):
        if cdf['EARLIEST EARLIER RECORD L'][later_cdf_entry] == 'N/A' or cdf['EARLIEST EARLIER RECORD R'][later_cdf_entry] == 'N/A' :

            if cdf['Sector'][cdf_entry] ==  cdf['Sector'][later_cdf_entry]:     

                if (cdf['SI L (PWY)'][cdf_entry] == 'SI U' and cdf['SI L (PWY)'][later_cdf_entry] == 'SI U'):

                    if cdf['Milage\n[m]'][cdf_entry] > cdf['Milage\n[m]'][later_cdf_entry] - 3 and cdf['Milage\n[m]'][cdf_entry] < cdf['Milage\n[m]'][later_cdf_entry] + 3:

                        if cdf['Date'][cdf_entry] < cdf['Date'][later_cdf_entry] and cdf['TR REPLACED DATE L'][cdf_entry] == 'NEVER':
                            cdf['EARLIEST EARLIER RECORD L'][later_cdf_entry] = cdf['Date'][cdf_entry]
                            days = int(datetime.datetime.now().strftime('%Y%m%d')[6:8]) - int(str(cdf['Date'][cdf_entry])[6:8])
                            months = int(datetime.datetime.now().strftime('%Y%m%d')[4:6]) - int(str(cdf['Date'][cdf_entry])[4:6])
                            years = int(datetime.datetime.now().strftime('%Y%m%d')[:4]) - int(str(cdf['Date'][cdf_entry])[:4])
                            cdf['AGE L'][later_cdf_entry] =   days + months*30 + years*365
                            cdf['EARLIEST Hor. wear 45° l\n[mm]'][later_cdf_entry] = cdf['Hor. wear 45° l\n[mm]'][cdf_entry]
                            cdf['EARLIEST Vert. wear l\n[mm]'][later_cdf_entry] = cdf['Vert. wear l\n[mm]'][cdf_entry]
                            cdf['EARLIEST Sum L (horz 45deg + vert)'][later_cdf_entry] = cdf['Sum L (horz 45deg + vert)'][cdf_entry] 
                        if cdf['Date'][cdf_entry] < cdf['Date'][later_cdf_entry] and cdf['TR REPLACED DATE L'][cdf_entry] != 'NEVER':
                            cdf['EARLIEST EARLIER RECORD L'][later_cdf_entry] = cdf['Date'][cdf_entry]
                            days = int(str(cdf['TR REPLACED DATE L'][later_cdf_entry])[6:8]) - int(str(cdf['Date'][cdf_entry])[6:8])
                            months = int(str(cdf['TR REPLACED DATE L'][later_cdf_entry])[4:6]) - int(str(cdf['Date'][cdf_entry])[4:6])
                            years = int(str(cdf['TR REPLACED DATE L'][later_cdf_entry])[:4]) - int(str(cdf['Date'][cdf_entry])[:4])
                            cdf['AGE L'][later_cdf_entry] =   days + months*30 + years*365  
                            cdf['EARLIEST Hor. wear 45° l\n[mm]'][later_cdf_entry] = cdf['Hor. wear 45° l\n[mm]'][cdf_entry]
                            cdf['EARLIEST Vert. wear l\n[mm]'][later_cdf_entry] = cdf['Vert. wear l\n[mm]'][cdf_entry]
                            cdf['EARLIEST Sum L (horz 45deg + vert)'][later_cdf_entry] = cdf['Sum L (horz 45deg + vert)'][cdf_entry] 
                
                if (cdf['SI R (PWY)'][cdf_entry] == 'SI U' and cdf['SI R (PWY)'][later_cdf_entry] == 'SI U'):
                    if cdf['Milage\n[m]'][cdf_entry] > cdf['Milage\n[m]'][later_cdf_entry] - 3 and cdf['Milage\n[m]'][cdf_entry] < cdf['Milage\n[m]'][later_cdf_entry] + 3:
                        if cdf['Date'][cdf_entry] < cdf['Date'][later_cdf_entry] and cdf['TR REPLACED DATE R'][cdf_entry] == 'NEVER':
                            cdf['EARLIEST EARLIER RECORD R'][later_cdf_entry] = cdf['Date'][cdf_entry]
                            days = int(datetime.datetime.now().strftime('%Y%m%d')[6:8]) - int(str(cdf['Date'][cdf_entry])[6:8])
                            months = int(datetime.datetime.now().strftime('%Y%m%d')[4:6]) - int(str(cdf['Date'][cdf_entry])[4:6])
                            years = int(datetime.datetime.now().strftime('%Y%m%d')[:4]) - int(str(cdf['Date'][cdf_entry])[:4])
                            cdf['AGE R'][later_cdf_entry] =   days + months*30 + years*365 
                            cdf['EARLIEST Hor. wear 45° r\n[mm]'][later_cdf_entry] = cdf['Hor. wear 45° r\n[mm]'][cdf_entry]
                            cdf['EARLIEST Vert. wear r\n[mm]'][later_cdf_entry] = cdf['Vert. wear r\n[mm]'][cdf_entry]
                            cdf['EARLIEST Sum R (horz 45deg + vert)'][later_cdf_entry] = cdf['Sum R (horz 45deg + vert)'][cdf_entry] 
                        if cdf['Date'][cdf_entry] < cdf['Date'][later_cdf_entry] and cdf['TR REPLACED DATE R'][cdf_entry] != 'NEVER':
                            cdf['EARLIEST EARLIER RECORD R'][later_cdf_entry] = cdf['Date'][cdf_entry]
                            days = int(str(cdf['TR REPLACED DATE R'][later_cdf_entry])[6:8]) - int(str(cdf['Date'][cdf_entry])[6:8])
                            months = int(str(cdf['TR REPLACED DATE R'][later_cdf_entry])[4:6]) - int(str(cdf['Date'][cdf_entry])[4:6])
                            years = int(str(cdf['TR REPLACED DATE R'][later_cdf_entry])[:4]) - int(str(cdf['Date'][cdf_entry])[:4])
                            cdf['AGE R'][later_cdf_entry] =   days + months*30 + years*365  
                            cdf['EARLIEST Hor. wear 45° r\n[mm]'][later_cdf_entry] = cdf['Hor. wear 45° r\n[mm]'][cdf_entry]
                            cdf['EARLIEST Vert. wear r\n[mm]'][later_cdf_entry] = cdf['Vert. wear r\n[mm]'][cdf_entry]
                            cdf['EARLIEST Sum R (horz 45deg + vert)'][later_cdf_entry] = cdf['Sum R (horz 45deg + vert)'][cdf_entry] 


cdf = cdf.sort_values(by=['Date','Sector','Milage\n[m]'],ascending=[0,1,1])
cdf.reset_index(drop=True, inplace=True)
cdf = cdf.reset_index(drop=True)
for earlier_cdf_entry in range(len(cdf)-1,0,-1):
    for later_cdf_entry in range(earlier_cdf_entry,0,-1):
        if cdf['Date'][earlier_cdf_entry] < cdf['Date'][later_cdf_entry]:
            if cdf['EARLIEST Sum R (horz 45deg + vert)'][later_cdf_entry] == 'N/A' or cdf['EARLIEST Sum L (horz 45deg + vert)'][later_cdf_entry] == 'N/A' :

                if cdf['Sector'][earlier_cdf_entry] ==  cdf['Sector'][later_cdf_entry]:     

                    if (cdf['SI L (PWY)'][earlier_cdf_entry] == 'SI U' and cdf['SI L (PWY)'][later_cdf_entry] == 'SI U'):

                        if cdf['Milage\n[m]'][earlier_cdf_entry] > cdf['Milage\n[m]'][later_cdf_entry] - 1 and cdf['Milage\n[m]'][earlier_cdf_entry] < cdf['Milage\n[m]'][later_cdf_entry] + 1:
                            print('Earlier Ch.: ' + str(cdf['Milage\n[m]'][earlier_cdf_entry]))
                            print('Later Ch.: ' + str(cdf['Milage\n[m]'][later_cdf_entry]))
                            print(earlier_cdf_entry,later_cdf_entry)

                            cdf = cdf.drop(cdf.index[earlier_cdf_entry])
                            break
                            
                            
                    if (cdf['SI R (PWY)'][earlier_cdf_entry] == 'SI U' and cdf['SI R (PWY)'][later_cdf_entry] == 'SI U'):

                        if cdf['Milage\n[m]'][earlier_cdf_entry] > cdf['Milage\n[m]'][later_cdf_entry] - 1 and cdf['Milage\n[m]'][earlier_cdf_entry] < cdf['Milage\n[m]'][later_cdf_entry] + 1:
                            print('Earlier Ch.: ' + str(cdf['Milage\n[m]'][earlier_cdf_entry]))
                            print('Later Ch.: ' + str(cdf['Milage\n[m]'][later_cdf_entry]))
                            print(earlier_cdf_entry,later_cdf_entry)

                            cdf = cdf.drop(cdf.index[earlier_cdf_entry])
                            break

   
        
cdf.to_excel("combined_files.xlsx")

