# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:42:17 2021

@author: chinjooern
"""

#pure chainage match implementation of binary search
def binary_search(df, ch_col_name, index_low, index_high, target_value, buffer = 1):
    index_middle = round((index_low + index_high)/2)
    
    if target_value == df[ch_col_name][index_middle]:
        return(index_middle)
    
    elif target_value > df[ch_col_name][index_middle]:
        binary_search(df, ch_col_name, index_middle, index_high, target_value, buffer = 1)
    
    else:
        binary_search(df, ch_col_name, index_low, index_middle, target_value, buffer = 1)
        
binary_search(df, 'Milage\n[m]', 0, len(df)-1, 30078)


def binary_search_plus_sector(df, ch_col_name, sector_col_name, index_low, index_high, target_value, target_sector, buffer = 1):
    for df_entry in range(0, len(df)):
        if df[sector_col_name][df_entry] == target_sector:
    
#chainage match and sector match implementation of binary search
# def binary_search_plus_sector(df, ch_col_name, sector_col_name, index_low, index_high, target_value, target_sector, buffer = 1):
#     for df_entry in range(0, len(df)):
#         if df[sector_col_name][df_entry] == target_sector:
#             binary_search(df, ch_col_name, index_low, index_high, target_value, buffer = 1)

def binary_search(df, ch_col_name, index_low, index_high, target_value, buffer = 1):
    
    index_middle = round((index_low + index_high)/2)

    if round(target_value) == round(df[ch_col_name][index_middle]) and index_middle != index_high:
        print(index_middle,index_high)
        print(round(target_value),round(df[ch_col_name][index_middle]))
        print("MATCH")
        return(index_middle)
    
    if index_middle == index_low or index_middle == index_high:
        print("MATCH WITH SELF")
        return('MATCH WITH SELF')

    
    elif target_value > df[ch_col_name][index_middle]:
        binary_search(df, ch_col_name, index_middle, index_high, target_value, buffer = 1)
    
    else:
        binary_search(df, ch_col_name, index_low, index_middle, target_value, buffer = 1)
        

def bottom_up_binary_search(df, ch_col_name, index_low, index_high, target_value, buffer = 1):
    
    index_middle = round((index_low + index_high)/2)

    if round(target_value) == round(df[ch_col_name][index_middle]) and index_middle != index_high:
        print(index_middle,index_high)
        print(round(target_value),round(df[ch_col_name][index_middle]))
        print("MATCH")
        return(index_middle)
    
    if index_middle == index_low or index_middle == index_high:
        print("MATCH WITH SELF")
        return('MATCH WITH SELF')

    
    elif target_value > df[ch_col_name][index_middle]:
        return(binary_search(df, ch_col_name, index_middle, index_high, target_value, buffer = 1))
    
    else:
        return(binary_search(df, ch_col_name, index_low, index_middle, target_value, buffer = 1))
        
        
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
        