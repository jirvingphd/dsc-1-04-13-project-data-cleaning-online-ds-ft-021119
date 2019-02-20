# data cleaning with pandas - project -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:02:00 2019

@author: james
"""
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline


pd.set_option('display.max_columns',20)
#pd.set_option('display.max_rows',10)
##pd.set_option('display.width',160)
##pd.printoptions(max_columns=10)


os.chdir(r'd:')
os.chdir(r'D:\Users\James\Dropbox (Personal)\CODING\_FLATIRON\section04\dsc-1-04-13-project-data-cleaning-online-ds-ft-021119')


heroes_df = pd.read_csv('heroes_information.csv')
powers_df = pd.read_csv('super_hero_powers.csv')

# print('\n heroes_df header:\n')
#print(heroes_df.head(),'\n\n')
#print(heroes_df.info(),'\n\n\n')
#
##
#print('\n heroes_df header:\n')
#print(heroes_df.head(),'\n\n')
#print(heroes_df.info(),'\n\n\n')

# Display information about heroes_df
print('HEROES_DF INFORMATION:\n')
print(heroes_df.info())
heroes_df['name'].value_counts()
len(heroes_df['name'].unique())
print(heroes_df.isna().any())

print('Publisher missing values:')
print(heroes_df.Publisher.unique())
print(heroes_df.Publisher.isna().sum())

print('Weight missing values:')
print(heroes_df.Weight.isna().sum())


# Display information about powers_df
print('POWERS_DF INFORMATION:')
print(powers_df.info())
powers_df.head()
print(powers_df.isna().any(),'\n')


# Remove unnamed columns 
heroes_df.drop('Unnamed: 0',axis=1,inplace=True)
heroes_df.head(2)
