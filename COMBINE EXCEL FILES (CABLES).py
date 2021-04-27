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

df = pd.DataFrame(columns = ["SECTOR", "DATE", "Event / Defect","Date","Position","Note","Typ"])

cable_list = [df]
count = 0

for f in files_xls:
    try:
        SECTOR = f.split("_")[2] + "_" + f.split("_")[3] 
        DATE = f.split("_")[0]
        data = pd.read_excel(f)      #data = pd.read_excel(f, skiprows=34) data = pd.read_excel(f, usecols=cols, skiprows=34)
        for i in range(0,len(data)):
            if (data.iloc[i][list(data.columns)[3]] == 'Event / Defect') == True:   #look for the top left corner of the data
                
                data = pd.read_excel(f, skiprows = i+1, usecols = [3,4,5,6,7,8,9,10,11]) #["Event / Defect","Date","Position","Note","Typ"]
                print("--", data.iloc[0][list(data.columns)[0]])
                data['SECTOR'] = SECTOR
                data['DATE'] = DATE
                cable_list.append(data)
                count += 1
                break
    except:
        print(f)
        #cols2skip = range(0,12)
        #cols = [i for i in range(3) if i not in cols2skip]
        
        #print(df.index[df[list(data.columns)[0]] == 'Milage\n[km]'].tolist()[0])  #for the first column in the file look for 'Milage'
        
print(count)        
        
       
                            

        #data.columns = ["Chainage", "Gauge", "Cant","Empty", "Twist", "Horizontal_Wear_L","Empty","Horizontal_Wear_R","Vertical_Wear_L","Empty", "Vertical_Wear_R", "45_Degree_Wear_L","Empty", "45_Degree_Wear_R","Empty","Events","Empty"]
 
        #df = pd.concat([df, data], axis = 0, sort = True)
        #df = df.append(data)
        
        #if "Unnamed" in list(data.columns)[0] or type(list(data.columns)[0]) == float:
         #   print(f)
        
        
   
    
df = pd.concat(cable_list, axis=0, sort = True) # reduces memory requirements compared to appending in for statement

#df = df.dropna()
#df = df.drop_duplicates('Chainage', keep='last')
df.to_excel("CABLE_MASTERLIST.xlsx")
   