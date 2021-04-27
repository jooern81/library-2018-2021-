# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 13:55:57 2021

@author: chinjooern
"""
import pandas as pd
import datetime

def binary_search(df, ch_col_name, index_low, index_high, target_value, buffer = 1):
    
    index_middle = round((index_low + index_high)/2)

    if index_middle == index_low or index_middle == index_high:     #exhausted all possibilities, no match
        # print("MATCH ITSELF")
        return("MATCH ITSELF")
    
    if round(target_value) == round(df[ch_col_name][index_middle]):
        # print(index_middle,index_high)
        # print(round(target_value),round(df[ch_col_name][index_middle]))
        # print("MATCH")
        return(index_middle)
    
    elif target_value > df[ch_col_name][index_middle]:
        return(binary_search(df, ch_col_name, index_middle, index_high, target_value, buffer = 1))
    
    else:
        return(binary_search(df, ch_col_name, index_low, index_middle, target_value, buffer = 1))
        

p7df = pd.read_pickle("./p7df.pkl")
p8df = pd.read_pickle("./p8df.pkl")

p7df = p7df.sort_values(by=['Milage\n[m]','Sector','Date'], ascending=[True,True,False])
p8df = p8df.sort_values(by=['Milage\n[m]','Sector','Date'], ascending=[True,True,False])

p7df = p7df.reset_index(drop=True)
p8df = p8df.reset_index(drop=True)
# p8df = pd.read_excel('Stacked_Phase8.xlsx')
# p8df.to_pickle("./p8df.pkl")

# cdf = pd.concat([p7df,p8df])
# cdf = cdf.sort_values(by=['Milage\n[m]','Sector','Date'], ascending=[True,True,False]) #descending dates to keep older entries below newer ones for a given chainage
# cdf = cdf.reset_index(drop=True)

            
# cdf.drop_duplicates(subset=['Sector', 'Milage\n[m]'], keep = 'first')

set_of_drops = set() #use set to prevent dupe indices

for p8df_entry in range(len(p8df)-1,0,-1):      #overwrite the p7df entries with newer p8df entries

    matched_index = binary_search(p7df, 'Milage\n[m]', 0, len(p7df), p8df['Milage\n[m]'][p8df_entry])
    print(matched_index)
    if matched_index != 'MATCH ITSELF': 
         
        if (p7df['Sector'][matched_index] == p8df['Sector'][p8df_entry]):
            set_of_drops.add(matched_index)
            print('MATCH AT: ' + str((p7df['Sector'][matched_index],p8df['Sector'][p8df_entry], p7df['Milage\n[m]'][matched_index],p8df['Milage\n[m]'][p8df_entry])))
            
            #carpet bomb section with same chainage to check for matches
            upward_counter = -1
            downward_counter = 1
            while p7df['Milage\n[m]'][matched_index + upward_counter] == p7df['Milage\n[m]'][matched_index]:
                upward_counter -= 1
                if matched_index != None and p7df['Sector'][matched_index] == p7df['Sector'][matched_index + upward_counter]:
                    set_of_drops.add(matched_index + upward_counter)
                    print('BOMBED UPWARDS: ' + str((p7df['Sector'][matched_index],p7df['Milage\n[m]'][matched_index],p7df['Sector'][matched_index + upward_counter],p7df['Milage\n[m]'][matched_index + upward_counter])))
            
            while p7df['Milage\n[m]'][matched_index + downward_counter] == p7df['Milage\n[m]'][matched_index]:
                downward_counter += 1
                if matched_index != None and p7df['Sector'][matched_index] == p7df['Sector'][matched_index + downward_counter]:
                    set_of_drops.add(matched_index + downward_counter)
                    print('BOMBED DOWNWARDS: ' + str((p7df['Sector'][matched_index],p7df['Milage\n[m]'][matched_index],p7df['Sector'][matched_index + downward_counter],p7df['Milage\n[m]'][matched_index + downward_counter])))
            
            

set_to_keep = set(range(p7df.shape[0])) - set_of_drops
p7df = p7df.take(list(set_to_keep))

#the above is a faster version of p7df.drop
# p7df.drop(p7df.index[list(set_of_drops)])
  

cdf = pd.concat([p7df,p8df])
cdf.to_excel("combined_files_xp2.xlsx")