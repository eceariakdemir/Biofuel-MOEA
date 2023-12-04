# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:56:39 2023

@author: eari
"""


import matplotlib.patches as mpatches
import seaborn as sns
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import plotly.io as pio
pio.renderers.default = 'browser'


labels = ['1998', '1999', '2000', '2001', '2002', '2003', '2004',
          '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013']

plt.rcParams.update({'font.size': 14})
plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

# import excel sheet
df_geo_corn = pd.read_excel('Platypus_codes/combined_pivot_Corn.xlsx', header=0, engine='openpyxl')
df_geo_soy = pd.read_excel('Platypus_codes/combined_pivot_Soy.xlsx', header=0, engine='openpyxl')
df_geo_grass_L = pd.read_excel('Platypus_codes/combined_pivot_AG_Switchgrass.xlsx', header=0, engine='openpyxl')
df_geo_grass = pd.read_excel('Platypus_codes/combined_pivot_ML_Switchgrass.xlsx', header=0, engine='openpyxl')
df_geo_algae_L = pd.read_excel('Platypus_codes/combined_pivot_AG_Algae.xlsx', header=0, engine='openpyxl')
df_geo_algae = pd.read_excel('Platypus_codes/combined_pivot_ML_Algae.xlsx', header=0, engine='openpyxl')


##########################################################################################
######################## 3 billion gallon biofuel production MFSP - LP ########################
##########################################################################################

fn_ha = 'Decision_Variables_LP_crops_' + 'MFSP' +'_' + '3' + '.csv'
df_ha = pd.read_csv(fn_ha, header=0, index_col=0)

fn = 'Objective_functions_LP_crops_' + 'MFSP' +'_' + '3' + '.csv'
df_O = pd.read_csv(fn, header=0, index_col=0)

num_c = len(df_geo_corn)

## Dividing corn, soy, grass and algae yield data.
C_ha = np.transpose(df_ha).iloc[0:num_c].values # used hectare for corn (107)
S_ha = np.transpose(df_ha).iloc[num_c:2*num_c].values # used hectare for soy (214)
G_ha = np.transpose(df_ha).iloc[2*num_c:3*num_c].values # used hectare for grass (321)
G_ha_L = np.transpose(df_ha).iloc[3*num_c:4*num_c].values # used hectare for algae (428)
A_ha = np.transpose(df_ha).iloc[4*num_c:5*num_c].values # used hectare for grass (535)
A_ha_L = np.transpose(df_ha).iloc[5*num_c:].values # used hectare for algae (642)

LL = df_geo_corn['land_limits_ha'].values

years = range(1998, 2014)

# Corn Grain yield
C_yield = df_geo_corn.loc[:, 1998:2013].values  # yield in kg/ha

# Soybean yield
S_yield = df_geo_soy.loc[:, 1998:2013].values  # yield in kg/ha

# Grass yield
G_yield_L = df_geo_grass_L.loc[:, 1998:2013].values  # yield in kg/ha

G_yield = df_geo_grass.loc[:, 1998:2013].values  # yield in kg/ha

# Algea yield
A_yield_L = df_geo_algae_L.loc[:, 1998:2013].values  # yield in kg/ha

A_yield = df_geo_algae.loc[:, 1998:2013].values  # yield in kg/ha

num_c = np.size(LL)  # size of land cost
Energy_total = np.zeros((len(years), 1))

CG_ethanol_total_MJ = np.zeros((len(years)))
SB_oil_total_MJ = np.zeros((len(years)))
CS_total_MJ = np.zeros((len(years)))
G_energy_total_MJ = np.zeros((len(years)))
A_energy_total_MJ = np.zeros((len(years)))
G_energy_total_MJ_L = np.zeros((len(years)))
A_energy_total_MJ_L = np.zeros((len(years)))

CS_ethanol_avg = np.zeros((len(df_ha), 1))
SB_oil_avg = np.zeros((len(df_ha), 1))
CS_avg = np.zeros((len(df_ha), 1))
G_energy_avg = np.zeros((len(df_ha), 1))
A_energy_avg = np.zeros((len(df_ha), 1))
G_energy_avg_L = np.zeros((len(df_ha), 1))
A_energy_avg_L = np.zeros((len(df_ha), 1))

for year in years:
    i = years.index(year)
    Y = C_yield[:, i]   # corn yield kg/ha
    S = S_yield[:, i]   # soy yield kg/ha
    G = G_yield[:, i]   # grass yield kg/ha
    A = A_yield[:, i]   # algae yield kg/ha
    G_L = G_yield_L[:, i]   # grass yield kg/ha
    A_L = A_yield_L[:, i]   # algae yield kg/ha
    
    Hadi = G_ha[:,0]*G

    CG_prod = sum(C_ha[:,0]*Y) #Based on each year and each state total corn biomass production (kg) calculated

    SB_prod = sum(S_ha[:,0]*S) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod = sum(G_ha[:,0]*G) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod = sum(A_ha[:,0]*A) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod_L = sum(G_ha_L[:,0]*G_L) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod_L = sum(A_ha_L[:,0]*A_L) #Based on each year and each state total corn biomass production (kg) calculated
    
    CG_MJ = CG_prod*9.42 #MJ/kg
    S_MJ = SB_prod*8.02 #MJ/kg
    CS_MJ = CG_MJ + S_MJ
    G_MJ = G_prod*8.35 #MJ/kg
    A_MJ = A_prod*20.82 #MJ/kg
    G_AG_MJ = G_prod_L*8.35 #MJ/kg
    A_AG_MJ = A_prod_L*20.82 #MJ/kg
        
    CG_ethanol_total_MJ[i] = CG_MJ
    SB_oil_total_MJ[i] = S_MJ
    CS_total_MJ[i] = CS_MJ
    G_energy_total_MJ[i] = G_MJ
    A_energy_total_MJ[i] = A_MJ
    G_energy_total_MJ_L[i] = G_AG_MJ
    A_energy_total_MJ_L[i] = A_AG_MJ
    
    CC_corn = min(CS_total_MJ)
    GG_grass_ML = min(G_energy_total_MJ)
    AA_algae_ML = min(A_energy_total_MJ)
    GG_grass_AG = min(G_energy_total_MJ_L)
    AA_algae_AG = min(A_energy_total_MJ_L)
    
    columns = ['version','Corn/Soy', 'Switchgrass on ML', 'Algae on ML','Switchgrass on AG', 'Algae on AG']
    df_MFSP3 = pd.DataFrame(columns = columns) 
    df_MFSP3.loc[len(df_MFSP3)]= ['MFSP',(CC_corn),(GG_grass_ML),(AA_algae_ML),(GG_grass_AG),(AA_algae_AG)]  


##########################################################################################
######################## 3 billion gallon biofuel production MFSP - NSGA-III ########################
##########################################################################################

fn_ha = 'Decision_Variables_NSGA_III_' + 'MFSP' +'_' + '3' + '.csv'
df_ha = pd.read_csv(fn_ha, header=0, index_col=0)

fn = 'Objective_functions_NSGA_III_' + 'MFSP' +'_' + '3' + '.csv'
df_O = pd.read_csv(fn, header=0, index_col=0)

num_c = len(df_geo_corn)

## Dividing corn, soy, grass and algae yield data.
CS_ha = np.transpose(df_ha).iloc[0:num_c].values
C_ha = CS_ha/2 # used hectare for corn (107)
S_ha = CS_ha/2# used hectare for soy ()
G_ha_L = np.transpose(df_ha).iloc[num_c:2*num_c].values # used hectare for grass (214)
A_ha_L = np.transpose(df_ha).iloc[2*num_c:3*num_c].values # used hectare for grass (321)
G_ha = np.transpose(df_ha).iloc[3*num_c:4*num_c].values # used hectare for algae (428)
A_ha = np.transpose(df_ha).iloc[4*num_c:5*num_c].values # used hectare for algae (535)

LL = df_geo_corn['land_limits_ha'].values

years = range(1998, 2014)

# Corn Grain yield
C_yield = df_geo_corn.loc[:, 1998:2013].values  # yield in kg/ha

# Soybean yield
S_yield = df_geo_soy.loc[:, 1998:2013].values  # yield in kg/ha

# Grass yield
G_yield_L = df_geo_grass_L.loc[:, 1998:2013].values  # yield in kg/ha

G_yield = df_geo_grass.loc[:, 1998:2013].values  # yield in kg/ha

# Algea yield
A_yield_L = df_geo_algae_L.loc[:, 1998:2013].values  # yield in kg/ha

A_yield = df_geo_algae.loc[:, 1998:2013].values  # yield in kg/ha

num_c = np.size(LL)  # size of land cost
Energy_total = np.zeros((len(years), 1))

CG_ethanol_total_MJ = np.zeros((len(years)))
SB_oil_total_MJ = np.zeros((len(years)))
CS_total_MJ = np.zeros((len(years)))
G_energy_total_MJ = np.zeros((len(years)))
A_energy_total_MJ = np.zeros((len(years)))
G_energy_total_MJ_L = np.zeros((len(years)))
A_energy_total_MJ_L = np.zeros((len(years)))

CS_ethanol_avg = np.zeros((len(df_ha), 1))
SB_oil_avg = np.zeros((len(df_ha), 1))
CS_avg = np.zeros((len(df_ha), 1))
G_energy_avg = np.zeros((len(df_ha), 1))
A_energy_avg = np.zeros((len(df_ha), 1))
G_energy_avg_L = np.zeros((len(df_ha), 1))
A_energy_avg_L = np.zeros((len(df_ha), 1))

for year in years:
    i = years.index(year)
    Y = C_yield[:, i]   # corn yield kg/ha
    S = S_yield[:, i]   # soy yield kg/ha
    G = G_yield[:, i]   # grass yield kg/ha
    A = A_yield[:, i]   # algae yield kg/ha
    G_L = G_yield_L[:, i]   # grass yield kg/ha
    A_L = A_yield_L[:, i]   # algae yield kg/ha
    
    Hadi = G_ha[:,0]*G

    CG_prod = sum(C_ha[:,0]*Y) #Based on each year and each state total corn biomass production (kg) calculated

    SB_prod = sum(S_ha[:,0]*S) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod = sum(G_ha[:,0]*G) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod = sum(A_ha[:,0]*A) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod_L = sum(G_ha_L[:,0]*G_L) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod_L = sum(A_ha_L[:,0]*A_L) #Based on each year and each state total corn biomass production (kg) calculated
    
    CG_MJ = CG_prod*9.42 #MJ/kg
    S_MJ = SB_prod*8.02 #MJ/kg
    CS_MJ = CG_MJ + S_MJ
    G_MJ = G_prod*8.35 #MJ/kg
    A_MJ = A_prod*20.82 #MJ/kg
    G_AG_MJ = G_prod_L*8.35 #MJ/kg
    A_AG_MJ = A_prod_L*20.82 #MJ/kg
        
    CG_ethanol_total_MJ[i] = CG_MJ
    SB_oil_total_MJ[i] = S_MJ
    CS_total_MJ[i] = CS_MJ
    G_energy_total_MJ[i] = G_MJ
    A_energy_total_MJ[i] = A_MJ
    G_energy_total_MJ_L[i] = G_AG_MJ
    A_energy_total_MJ_L[i] = A_AG_MJ
    
    CC_corn = min(CS_total_MJ)
    GG_grass_ML = min(G_energy_total_MJ)
    AA_algae_ML = min(A_energy_total_MJ)
    GG_grass_AG = min(G_energy_total_MJ_L)
    AA_algae_AG = min(A_energy_total_MJ_L)
    
    columns = ['version','Corn/Soy', 'Switchgrass on ML', 'Algae on ML','Switchgrass on AG', 'Algae on AG']
    df_MFSP3_NSGA = pd.DataFrame(columns = columns) 
    df_MFSP3_NSGA.loc[len(df_MFSP3_NSGA)]= ['MFSP',(CC_corn),(GG_grass_ML),(AA_algae_ML),(GG_grass_AG),(AA_algae_AG)]  


    
##########################################################################################
######################## 3 billion gallon biofuel production GHG - LP  ########################
########################################################################################## 

fn_ha = 'Decision_Variables_LP_crops_' + 'GHG' +'_' + '3' + '.csv'
df_ha = pd.read_csv(fn_ha, header=0, index_col=0)

fn = 'Objective_functions_LP_crops_' + 'GHG' +'_' + '3' + '.csv'
df_O = pd.read_csv(fn, header=0, index_col=0)

num_c = len(df_geo_corn)

## Dividing corn, soy, grass and algae yield data.
C_ha = np.transpose(df_ha).iloc[0:num_c].values # used hectare for corn (107)
S_ha = np.transpose(df_ha).iloc[num_c:2*num_c].values # used hectare for soy (214)
G_ha = np.transpose(df_ha).iloc[2*num_c:3*num_c].values # used hectare for grass (321)
G_ha_L = np.transpose(df_ha).iloc[3*num_c:4*num_c].values # used hectare for algae (428)
A_ha = np.transpose(df_ha).iloc[4*num_c:5*num_c].values # used hectare for grass (535)
A_ha_L = np.transpose(df_ha).iloc[5*num_c:].values # used hectare for algae (642)

LL = df_geo_corn['land_limits_ha'].values

years = range(1998, 2014)

# Corn Grain yield
C_yield = df_geo_corn.loc[:, 1998:2013].values  # yield in kg/ha

# Soybean yield
S_yield = df_geo_soy.loc[:, 1998:2013].values  # yield in kg/ha

# Grass yield
G_yield_L = df_geo_grass_L.loc[:, 1998:2013].values  # yield in kg/ha

G_yield = df_geo_grass.loc[:, 1998:2013].values  # yield in kg/ha

# Algea yield
A_yield_L = df_geo_algae_L.loc[:, 1998:2013].values  # yield in kg/ha

A_yield = df_geo_algae.loc[:, 1998:2013].values  # yield in kg/ha

num_c = np.size(LL)  # size of land cost
Energy_total = np.zeros((len(years), 1))

CG_ethanol_total_MJ = np.zeros((len(years)))
SB_oil_total_MJ = np.zeros((len(years)))
CS_total_MJ = np.zeros((len(years)))
G_energy_total_MJ = np.zeros((len(years)))
A_energy_total_MJ = np.zeros((len(years)))
G_energy_total_MJ_L = np.zeros((len(years)))
A_energy_total_MJ_L = np.zeros((len(years)))
Total_MJ = np.zeros((len(years)))

CS_ethanol_avg = np.zeros((len(df_ha), 1))
SB_oil_avg = np.zeros((len(df_ha), 1))
CS_avg = np.zeros((len(df_ha), 1))
G_energy_avg = np.zeros((len(df_ha), 1))
A_energy_avg = np.zeros((len(df_ha), 1))
G_energy_avg_L = np.zeros((len(df_ha), 1))
A_energy_avg_L = np.zeros((len(df_ha), 1))

# Energy_total = np.zeros((len(solution),1))

for year in years:
    i = years.index(year)
    Y = C_yield[:, i]   # corn yield kg/ha
    S = S_yield[:, i]   # soy yield kg/ha
    G = G_yield[:, i]   # grass yield kg/ha
    A = A_yield[:, i]   # algae yield kg/ha
    G_L = G_yield_L[:, i]   # grass yield kg/ha
    A_L = A_yield_L[:, i]   # algae yield kg/ha
    
    Hadi = G_ha[:,0]*G

    CG_prod = sum(C_ha[:,0]*Y) #Based on each year and each state total corn biomass production (kg) calculated

    SB_prod = sum(S_ha[:,0]*S) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod = sum(G_ha[:,0]*G) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod = sum(A_ha[:,0]*A) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod_L = sum(G_ha_L[:,0]*G_L) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod_L = sum(A_ha_L[:,0]*A_L) #Based on each year and each state total corn biomass production (kg) calculated
    
    CG_MJ = CG_prod*9.42 #MJ/kg
    S_MJ = SB_prod*8.02 #MJ/kg
    CS_MJ = CG_MJ + S_MJ
    G_MJ = G_prod*8.35 #MJ/kg
    A_MJ = A_prod*20.82 #MJ/kg
    G_AG_MJ = G_prod_L*8.35 #MJ/kg
    A_AG_MJ = A_prod_L*20.82 #MJ/kg
        
    CG_ethanol_total_MJ[i] = CG_MJ
    SB_oil_total_MJ[i] = S_MJ
    CS_total_MJ[i] = CS_MJ
    G_energy_total_MJ[i] = G_MJ
    A_energy_total_MJ[i] = A_MJ
    G_energy_total_MJ_L[i] = G_AG_MJ
    A_energy_total_MJ_L[i] = A_AG_MJ
    
    Total_MJ[i] =CS_total_MJ[i] + G_energy_total_MJ[i] + A_energy_total_MJ[i] + G_energy_total_MJ_L[i] + A_energy_total_MJ_L[i]
    
    CC_corn = min(CS_total_MJ)
    GG_grass_ML = min(G_energy_total_MJ)
    AA_algae_ML = min(A_energy_total_MJ)
    GG_grass_AG = min(G_energy_total_MJ_L)
    AA_algae_AG = min(A_energy_total_MJ_L)
    
    
    columns = ['version','Corn/Soy', 'Switchgrass on ML', 'Algae on ML','Switchgrass on AG', 'Algae on AG']
    df_GHG3 = pd.DataFrame(columns = columns) 
    df_GHG3.loc[len(df_GHG3)]= ['GHG',(CC_corn),(GG_grass_ML),(AA_algae_ML),(GG_grass_AG),(AA_algae_AG)]  
    
##########################################################################################
######################## 3 billion gallon biofuel production GHG - NSGA-III ########################
##########################################################################################

fn_ha = 'Decision_Variables_NSGA_III_' + 'GHG' +'_' + '3' + '.csv'
df_ha = pd.read_csv(fn_ha, header=0, index_col=0)

fn = 'Objective_functions_NSGA_III_' + 'GHG' +'_' + '3' + '.csv'
df_O = pd.read_csv(fn, header=0, index_col=0)

num_c = len(df_geo_corn)

## Dividing corn, soy, grass and algae yield data.
CS_ha = np.transpose(df_ha).iloc[0:num_c].values
C_ha = CS_ha/2 # used hectare for corn (107)
S_ha = CS_ha/2# used hectare for soy ()
G_ha_L = np.transpose(df_ha).iloc[num_c:2*num_c].values # used hectare for grass (214)
A_ha_L = np.transpose(df_ha).iloc[2*num_c:3*num_c].values # used hectare for grass (321)
G_ha = np.transpose(df_ha).iloc[3*num_c:4*num_c].values # used hectare for algae (428)
A_ha = np.transpose(df_ha).iloc[4*num_c:5*num_c].values # used hectare for algae (535)

LL = df_geo_corn['land_limits_ha'].values

years = range(1998, 2014)

# Corn Grain yield
C_yield = df_geo_corn.loc[:, 1998:2013].values  # yield in kg/ha

# Soybean yield
S_yield = df_geo_soy.loc[:, 1998:2013].values  # yield in kg/ha

# Grass yield
G_yield_L = df_geo_grass_L.loc[:, 1998:2013].values  # yield in kg/ha

G_yield = df_geo_grass.loc[:, 1998:2013].values  # yield in kg/ha

# Algea yield
A_yield_L = df_geo_algae_L.loc[:, 1998:2013].values  # yield in kg/ha

A_yield = df_geo_algae.loc[:, 1998:2013].values  # yield in kg/ha

num_c = np.size(LL)  # size of land cost
Energy_total = np.zeros((len(years), 1))

CG_ethanol_total_MJ = np.zeros((len(years)))
SB_oil_total_MJ = np.zeros((len(years)))
CS_total_MJ = np.zeros((len(years)))
G_energy_total_MJ = np.zeros((len(years)))
A_energy_total_MJ = np.zeros((len(years)))
G_energy_total_MJ_L = np.zeros((len(years)))
A_energy_total_MJ_L = np.zeros((len(years)))

CS_ethanol_avg = np.zeros((len(df_ha), 1))
SB_oil_avg = np.zeros((len(df_ha), 1))
CS_avg = np.zeros((len(df_ha), 1))
G_energy_avg = np.zeros((len(df_ha), 1))
A_energy_avg = np.zeros((len(df_ha), 1))
G_energy_avg_L = np.zeros((len(df_ha), 1))
A_energy_avg_L = np.zeros((len(df_ha), 1))

for year in years:
    i = years.index(year)
    Y = C_yield[:, i]   # corn yield kg/ha
    S = S_yield[:, i]   # soy yield kg/ha
    G = G_yield[:, i]   # grass yield kg/ha
    A = A_yield[:, i]   # algae yield kg/ha
    G_L = G_yield_L[:, i]   # grass yield kg/ha
    A_L = A_yield_L[:, i]   # algae yield kg/ha
    
    Hadi = G_ha[:,0]*G

    CG_prod = sum(C_ha[:,0]*Y) #Based on each year and each state total corn biomass production (kg) calculated

    SB_prod = sum(S_ha[:,0]*S) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod = sum(G_ha[:,0]*G) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod = sum(A_ha[:,0]*A) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod_L = sum(G_ha_L[:,0]*G_L) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod_L = sum(A_ha_L[:,0]*A_L) #Based on each year and each state total corn biomass production (kg) calculated
    
    CG_MJ = CG_prod*9.42 #MJ/kg
    S_MJ = SB_prod*8.02 #MJ/kg
    CS_MJ = CG_MJ + S_MJ
    G_MJ = G_prod*8.35 #MJ/kg
    A_MJ = A_prod*20.82 #MJ/kg
    G_AG_MJ = G_prod_L*8.35 #MJ/kg
    A_AG_MJ = A_prod_L*20.82 #MJ/kg
        
    CG_ethanol_total_MJ[i] = CG_MJ
    SB_oil_total_MJ[i] = S_MJ
    CS_total_MJ[i] = CS_MJ
    G_energy_total_MJ[i] = G_MJ
    A_energy_total_MJ[i] = A_MJ
    G_energy_total_MJ_L[i] = G_AG_MJ
    A_energy_total_MJ_L[i] = A_AG_MJ
    
    CC_corn = min(CS_total_MJ)
    GG_grass_ML = min(G_energy_total_MJ)
    AA_algae_ML = min(A_energy_total_MJ)
    GG_grass_AG = min(G_energy_total_MJ_L)
    AA_algae_AG = min(A_energy_total_MJ_L)
    
    columns = ['version','Corn/Soy', 'Switchgrass on ML', 'Algae on ML','Switchgrass on AG', 'Algae on AG']
    df_GHG3_NSGA = pd.DataFrame(columns = columns) 
    df_GHG3_NSGA.loc[len(df_GHG3_NSGA)]= ['MFSP',(CC_corn),(GG_grass_ML),(AA_algae_ML),(GG_grass_AG),(AA_algae_AG)]  

# frames = [df_MFSP3, df_GHG3]
# df = pd.concat(frames)

# #plotting the stacked bar chart
# plt.rcParams.update({'font.size': 15})
# plt.rcParams['font.sans-serif'] = "Arial"
# # axis_label_pad = 10
# tick_pad = 2
# fig, ax = plt.subplots(figsize=(8,8))
# df.plot(kind='bar', stacked=True, ax=ax, color = ["#023e8a","#ffbe0b","#d90429","#8ac926","#6a4c93"],label= "3 Billion" )

# ax.set_ylabel('TotalEnergy Prodcution (MJ)', weight='bold',fontsize=20)
# ax.set_xlabel('3 Billion gallon biofuel production scenarios', weight='bold',fontsize=20)
# ax.set_xticklabels(['MFSP','GHG'],rotation=360, weight='bold',fontsize=20)




##########################################################################################
######################## 12 billion gallon biofuel production MFSP #######################
##########################################################################################

# import excel sheet
df_geo_corn = pd.read_excel('Platypus_codes/combined_pivot_Corn.xlsx', header=0, engine='openpyxl')
df_geo_soy = pd.read_excel('Platypus_codes/combined_pivot_Soy.xlsx', header=0, engine='openpyxl')
df_geo_grass_L = pd.read_excel('Platypus_codes/combined_pivot_AG_Switchgrass.xlsx', header=0, engine='openpyxl')
df_geo_grass = pd.read_excel('Platypus_codes/combined_pivot_ML_Switchgrass.xlsx', header=0, engine='openpyxl')
df_geo_algae_L = pd.read_excel('Platypus_codes/combined_pivot_AG_Algae.xlsx', header=0, engine='openpyxl')
df_geo_algae = pd.read_excel('Platypus_codes/combined_pivot_ML_Algae.xlsx', header=0, engine='openpyxl')

########### MFSP
fn_ha = 'Decision_Variables_LP_crops_' + 'MFSP' +'_' + '12' + '.csv'
df_ha = pd.read_csv(fn_ha, header=0, index_col=0)

fn = 'Objective_functions_LP_crops_' + 'MFSP' +'_' + '12' + '.csv'
df_O = pd.read_csv(fn, header=0, index_col=0)

num_c = len(df_geo_corn)

## Dividing corn, soy, grass and algae yield data.
C_ha = np.transpose(df_ha).iloc[0:num_c].values # used hectare for corn (107)
S_ha = np.transpose(df_ha).iloc[num_c:2*num_c].values # used hectare for soy (214)
G_ha = np.transpose(df_ha).iloc[2*num_c:3*num_c].values # used hectare for grass (321)
G_ha_L = np.transpose(df_ha).iloc[3*num_c:4*num_c].values # used hectare for algae (428)
A_ha = np.transpose(df_ha).iloc[4*num_c:5*num_c].values # used hectare for grass (535)
A_ha_L = np.transpose(df_ha).iloc[5*num_c:].values # used hectare for algae (642)

LL = df_geo_corn['land_limits_ha'].values

years = range(1998, 2014)

# Corn Grain yield
C_yield = df_geo_corn.loc[:, 1998:2013].values  # yield in kg/ha

# Soybean yield
S_yield = df_geo_soy.loc[:, 1998:2013].values  # yield in kg/ha

# Grass yield
G_yield_L = df_geo_grass_L.loc[:, 1998:2013].values  # yield in kg/ha

G_yield = df_geo_grass.loc[:, 1998:2013].values  # yield in kg/ha

# Algea yield
A_yield_L = df_geo_algae_L.loc[:, 1998:2013].values  # yield in kg/ha

A_yield = df_geo_algae.loc[:, 1998:2013].values  # yield in kg/ha

num_c = np.size(LL)  # size of land cost
Energy_total = np.zeros((len(years), 1))

CG_ethanol_total_MJ = np.zeros((len(years)))
SB_oil_total_MJ = np.zeros((len(years)))
CS_total_MJ = np.zeros((len(years)))
G_energy_total_MJ = np.zeros((len(years)))
A_energy_total_MJ = np.zeros((len(years)))
G_energy_total_MJ_L = np.zeros((len(years)))
A_energy_total_MJ_L = np.zeros((len(years)))

CS_ethanol_avg = np.zeros((len(df_ha), 1))
SB_oil_avg = np.zeros((len(df_ha), 1))
CS_avg = np.zeros((len(df_ha), 1))
G_energy_avg = np.zeros((len(df_ha), 1))
A_energy_avg = np.zeros((len(df_ha), 1))
G_energy_avg_L = np.zeros((len(df_ha), 1))
A_energy_avg_L = np.zeros((len(df_ha), 1))

# Energy_total = np.zeros((len(solution),1))

for year in years:
    i = years.index(year)
    Y = C_yield[:, i]   # corn yield kg/ha
    S = S_yield[:, i]   # soy yield kg/ha
    G = G_yield[:, i]   # grass yield kg/ha
    A = A_yield[:, i]   # algae yield kg/ha
    G_L = G_yield_L[:, i]   # grass yield kg/ha
    A_L = A_yield_L[:, i]   # algae yield kg/ha
    
    Hadi = G_ha[:,0]*G

    CG_prod = sum(C_ha[:,0]*Y) #Based on each year and each state total corn biomass production (kg) calculated

    SB_prod = sum(S_ha[:,0]*S) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod = sum(G_ha[:,0]*G) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod = sum(A_ha[:,0]*A) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod_L = sum(G_ha_L[:,0]*G_L) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod_L = sum(A_ha_L[:,0]*A_L) #Based on each year and each state total corn biomass production (kg) calculated
    
    CG_MJ = CG_prod*9.42 #MJ/kg
    S_MJ = SB_prod*8.02 #MJ/kg
    CS_MJ = CG_MJ + S_MJ
    G_MJ = G_prod*8.35 #MJ/kg
    A_MJ = A_prod*20.82 #MJ/kg
    G_AG_MJ = G_prod_L*8.35 #MJ/kg
    A_AG_MJ = A_prod_L*20.82 #MJ/kg
        
    CG_ethanol_total_MJ[i] = CG_MJ
    SB_oil_total_MJ[i] = S_MJ
    CS_total_MJ[i] = CS_MJ
    G_energy_total_MJ[i] = G_MJ
    A_energy_total_MJ[i] = A_MJ
    G_energy_total_MJ_L[i] = G_AG_MJ
    A_energy_total_MJ_L[i] = A_AG_MJ
    
    CC_corn = min(CS_total_MJ)
    GG_grass_ML = min(G_energy_total_MJ)
    AA_algae_ML = min(A_energy_total_MJ)
    GG_grass_AG = min(G_energy_total_MJ_L)
    AA_algae_AG = min(A_energy_total_MJ_L)
    
    

    columns = ['version','Corn/Soy', 'Switchgrass on ML', 'Algae on ML','Switchgrass on AG', 'Algae on AG']
    df_MFSP12 = pd.DataFrame(columns = columns) 
    df_MFSP12.loc[len(df_MFSP12)]= ['MFSP',(CC_corn),(GG_grass_ML),(AA_algae_ML),(GG_grass_AG),(AA_algae_AG)]  


##########################################################################################
######################## 12 billion gallon biofuel production MFSP - NSGA-III ########################
##########################################################################################

fn_ha = 'Decision_Variables_NSGA_III_' + 'MFSP' +'_' + '12' + '.csv'
df_ha = pd.read_csv(fn_ha, header=0, index_col=0)

fn = 'Objective_functions_NSGA_III_' + 'MFSP' +'_' + '12' + '.csv'
df_O = pd.read_csv(fn, header=0, index_col=0)

num_c = len(df_geo_corn)

## Dividing corn, soy, grass and algae yield data.
CS_ha = np.transpose(df_ha).iloc[0:num_c].values
C_ha = CS_ha/2 # used hectare for corn (107)
S_ha = CS_ha/2# used hectare for soy ()
G_ha_L = np.transpose(df_ha).iloc[num_c:2*num_c].values # used hectare for grass (214)
A_ha_L = np.transpose(df_ha).iloc[2*num_c:3*num_c].values # used hectare for grass (321)
G_ha = np.transpose(df_ha).iloc[3*num_c:4*num_c].values # used hectare for algae (428)
A_ha = np.transpose(df_ha).iloc[4*num_c:5*num_c].values # used hectare for algae (535)

LL = df_geo_corn['land_limits_ha'].values

years = range(1998, 2014)

# Corn Grain yield
C_yield = df_geo_corn.loc[:, 1998:2013].values  # yield in kg/ha

# Soybean yield
S_yield = df_geo_soy.loc[:, 1998:2013].values  # yield in kg/ha

# Grass yield
G_yield_L = df_geo_grass_L.loc[:, 1998:2013].values  # yield in kg/ha

G_yield = df_geo_grass.loc[:, 1998:2013].values  # yield in kg/ha

# Algea yield
A_yield_L = df_geo_algae_L.loc[:, 1998:2013].values  # yield in kg/ha

A_yield = df_geo_algae.loc[:, 1998:2013].values  # yield in kg/ha

num_c = np.size(LL)  # size of land cost
Energy_total = np.zeros((len(years), 1))

CG_ethanol_total_MJ = np.zeros((len(years)))
SB_oil_total_MJ = np.zeros((len(years)))
CS_total_MJ = np.zeros((len(years)))
G_energy_total_MJ = np.zeros((len(years)))
A_energy_total_MJ = np.zeros((len(years)))
G_energy_total_MJ_L = np.zeros((len(years)))
A_energy_total_MJ_L = np.zeros((len(years)))

CS_ethanol_avg = np.zeros((len(df_ha), 1))
SB_oil_avg = np.zeros((len(df_ha), 1))
CS_avg = np.zeros((len(df_ha), 1))
G_energy_avg = np.zeros((len(df_ha), 1))
A_energy_avg = np.zeros((len(df_ha), 1))
G_energy_avg_L = np.zeros((len(df_ha), 1))
A_energy_avg_L = np.zeros((len(df_ha), 1))

for year in years:
    i = years.index(year)
    Y = C_yield[:, i]   # corn yield kg/ha
    S = S_yield[:, i]   # soy yield kg/ha
    G = G_yield[:, i]   # grass yield kg/ha
    A = A_yield[:, i]   # algae yield kg/ha
    G_L = G_yield_L[:, i]   # grass yield kg/ha
    A_L = A_yield_L[:, i]   # algae yield kg/ha
    
    Hadi = G_ha[:,0]*G

    CG_prod = sum(C_ha[:,0]*Y) #Based on each year and each state total corn biomass production (kg) calculated

    SB_prod = sum(S_ha[:,0]*S) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod = sum(G_ha[:,0]*G) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod = sum(A_ha[:,0]*A) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod_L = sum(G_ha_L[:,0]*G_L) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod_L = sum(A_ha_L[:,0]*A_L) #Based on each year and each state total corn biomass production (kg) calculated
    
    CG_MJ = CG_prod*9.42 #MJ/kg
    S_MJ = SB_prod*8.02 #MJ/kg
    CS_MJ = CG_MJ + S_MJ
    G_MJ = G_prod*8.35 #MJ/kg
    A_MJ = A_prod*20.82 #MJ/kg
    G_AG_MJ = G_prod_L*8.35 #MJ/kg
    A_AG_MJ = A_prod_L*20.82 #MJ/kg
        
    CG_ethanol_total_MJ[i] = CG_MJ
    SB_oil_total_MJ[i] = S_MJ
    CS_total_MJ[i] = CS_MJ
    G_energy_total_MJ[i] = G_MJ
    A_energy_total_MJ[i] = A_MJ
    G_energy_total_MJ_L[i] = G_AG_MJ
    A_energy_total_MJ_L[i] = A_AG_MJ
    
    CC_corn = min(CS_total_MJ)
    GG_grass_ML = min(G_energy_total_MJ)
    AA_algae_ML = min(A_energy_total_MJ)
    GG_grass_AG = min(G_energy_total_MJ_L)
    AA_algae_AG = min(A_energy_total_MJ_L)
    
    columns = ['version','Corn/Soy', 'Switchgrass on ML', 'Algae on ML','Switchgrass on AG', 'Algae on AG']
    df_MFSP12_NSGA = pd.DataFrame(columns = columns) 
    df_MFSP12_NSGA.loc[len(df_MFSP12_NSGA)]= ['MFSP',(CC_corn),(GG_grass_ML),(AA_algae_ML),(GG_grass_AG),(AA_algae_AG)] 

    
##########################################################################################
######################## 12 billion gallon biofuel production GHG #######################
########################################################################################## 
fn_ha = 'Decision_Variables_LP_crops_' + 'GHG' +'_' + '12' + '.csv'
df_ha = pd.read_csv(fn_ha, header=0, index_col=0)

fn = 'Objective_functions_LP_crops_' + 'GHG' +'_' + '12' + '.csv'
df_O = pd.read_csv(fn, header=0, index_col=0)

num_c = len(df_geo_corn)

## Dividing corn, soy, grass and algae yield data.
C_ha = np.transpose(df_ha).iloc[0:num_c].values # used hectare for corn (107)
S_ha = np.transpose(df_ha).iloc[num_c:2*num_c].values # used hectare for soy (214)
G_ha = np.transpose(df_ha).iloc[2*num_c:3*num_c].values # used hectare for grass (321)
G_ha_L = np.transpose(df_ha).iloc[3*num_c:4*num_c].values # used hectare for algae (428)
A_ha = np.transpose(df_ha).iloc[4*num_c:5*num_c].values # used hectare for grass (535)
A_ha_L = np.transpose(df_ha).iloc[5*num_c:].values # used hectare for algae (642)

LL = df_geo_corn['land_limits_ha'].values

years = range(1998, 2014)

# Corn Grain yield
C_yield = df_geo_corn.loc[:, 1998:2013].values  # yield in kg/ha

# Soybean yield
S_yield = df_geo_soy.loc[:, 1998:2013].values  # yield in kg/ha

# Grass yield
G_yield_L = df_geo_grass_L.loc[:, 1998:2013].values  # yield in kg/ha

G_yield = df_geo_grass.loc[:, 1998:2013].values  # yield in kg/ha

# Algea yield
A_yield_L = df_geo_algae_L.loc[:, 1998:2013].values  # yield in kg/ha

A_yield = df_geo_algae.loc[:, 1998:2013].values  # yield in kg/ha

num_c = np.size(LL)  # size of land cost
Energy_total = np.zeros((len(years), 1))

CG_ethanol_total_MJ = np.zeros((len(years)))
SB_oil_total_MJ = np.zeros((len(years)))
CS_total_MJ = np.zeros((len(years)))
G_energy_total_MJ = np.zeros((len(years)))
A_energy_total_MJ = np.zeros((len(years)))
G_energy_total_MJ_L = np.zeros((len(years)))
A_energy_total_MJ_L = np.zeros((len(years)))

CS_ethanol_avg = np.zeros((len(df_ha), 1))
SB_oil_avg = np.zeros((len(df_ha), 1))
CS_avg = np.zeros((len(df_ha), 1))
G_energy_avg = np.zeros((len(df_ha), 1))
A_energy_avg = np.zeros((len(df_ha), 1))
G_energy_avg_L = np.zeros((len(df_ha), 1))
A_energy_avg_L = np.zeros((len(df_ha), 1))

# Energy_total = np.zeros((len(solution),1))

for year in years:
    i = years.index(year)
    Y = C_yield[:, i]   # corn yield kg/ha
    S = S_yield[:, i]   # soy yield kg/ha
    G = G_yield[:, i]   # grass yield kg/ha
    A = A_yield[:, i]   # algae yield kg/ha
    G_L = G_yield_L[:, i]   # grass yield kg/ha
    A_L = A_yield_L[:, i]   # algae yield kg/ha
    
    Hadi = G_ha[:,0]*G

    CG_prod = sum(C_ha[:,0]*Y) #Based on each year and each state total corn biomass production (kg) calculated

    SB_prod = sum(S_ha[:,0]*S) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod = sum(G_ha[:,0]*G) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod = sum(A_ha[:,0]*A) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod_L = sum(G_ha_L[:,0]*G_L) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod_L = sum(A_ha_L[:,0]*A_L) #Based on each year and each state total corn biomass production (kg) calculated
    
    CG_MJ = CG_prod*9.42 #MJ/kg
    S_MJ = SB_prod*8.02 #MJ/kg
    CS_MJ = CG_MJ + S_MJ
    G_MJ = G_prod*8.35 #MJ/kg
    A_MJ = A_prod*20.82 #MJ/kg
    G_AG_MJ = G_prod_L*8.35 #MJ/kg
    A_AG_MJ = A_prod_L*20.82 #MJ/kg
        
    CG_ethanol_total_MJ[i] = CG_MJ
    SB_oil_total_MJ[i] = S_MJ
    CS_total_MJ[i] = CS_MJ
    G_energy_total_MJ[i] = G_MJ
    A_energy_total_MJ[i] = A_MJ
    G_energy_total_MJ_L[i] = G_AG_MJ
    A_energy_total_MJ_L[i] = A_AG_MJ
    
    CC_corn = min(CS_total_MJ)
    GG_grass_ML = min(G_energy_total_MJ)
    AA_algae_ML = min(A_energy_total_MJ)
    GG_grass_AG = min(G_energy_total_MJ_L)
    AA_algae_AG = min(A_energy_total_MJ_L)
    
    
    columns = ['version','Corn/Soy', 'Switchgrass on ML', 'Algae on ML','Switchgrass on AG', 'Algae on AG']
    df_GHG12 = pd.DataFrame(columns = columns) 
    df_GHG12.loc[len(df_GHG12)]= ['GHG',(CC_corn),(GG_grass_ML),(AA_algae_ML),(GG_grass_AG),(AA_algae_AG)]  

##########################################################################################
######################## 12 billion gallon biofuel production GHG - NSGA-III ########################
##########################################################################################

fn_ha = 'Decision_Variables_NSGA_III_' + 'GHG' +'_' + '12' + '.csv'
df_ha = pd.read_csv(fn_ha, header=0, index_col=0)

fn = 'Objective_functions_NSGA_III_' + 'GHG' +'_' + '12' + '.csv'
df_O = pd.read_csv(fn, header=0, index_col=0)

num_c = len(df_geo_corn)

## Dividing corn, soy, grass and algae yield data.
CS_ha = np.transpose(df_ha).iloc[0:num_c].values
C_ha = CS_ha/2 # used hectare for corn (107)
S_ha = CS_ha/2# used hectare for soy ()
G_ha_L = np.transpose(df_ha).iloc[num_c:2*num_c].values # used hectare for grass (214)
A_ha_L = np.transpose(df_ha).iloc[2*num_c:3*num_c].values # used hectare for grass (321)
G_ha = np.transpose(df_ha).iloc[3*num_c:4*num_c].values # used hectare for algae (428)
A_ha = np.transpose(df_ha).iloc[4*num_c:5*num_c].values # used hectare for algae (535)

LL = df_geo_corn['land_limits_ha'].values

years = range(1998, 2014)

# Corn Grain yield
C_yield = df_geo_corn.loc[:, 1998:2013].values  # yield in kg/ha

# Soybean yield
S_yield = df_geo_soy.loc[:, 1998:2013].values  # yield in kg/ha

# Grass yield
G_yield_L = df_geo_grass_L.loc[:, 1998:2013].values  # yield in kg/ha

G_yield = df_geo_grass.loc[:, 1998:2013].values  # yield in kg/ha

# Algea yield
A_yield_L = df_geo_algae_L.loc[:, 1998:2013].values  # yield in kg/ha

A_yield = df_geo_algae.loc[:, 1998:2013].values  # yield in kg/ha

num_c = np.size(LL)  # size of land cost
Energy_total = np.zeros((len(years), 1))

CG_ethanol_total_MJ = np.zeros((len(years)))
SB_oil_total_MJ = np.zeros((len(years)))
CS_total_MJ = np.zeros((len(years)))
G_energy_total_MJ = np.zeros((len(years)))
A_energy_total_MJ = np.zeros((len(years)))
G_energy_total_MJ_L = np.zeros((len(years)))
A_energy_total_MJ_L = np.zeros((len(years)))

CS_ethanol_avg = np.zeros((len(df_ha), 1))
SB_oil_avg = np.zeros((len(df_ha), 1))
CS_avg = np.zeros((len(df_ha), 1))
G_energy_avg = np.zeros((len(df_ha), 1))
A_energy_avg = np.zeros((len(df_ha), 1))
G_energy_avg_L = np.zeros((len(df_ha), 1))
A_energy_avg_L = np.zeros((len(df_ha), 1))

for year in years:
    i = years.index(year)
    Y = C_yield[:, i]   # corn yield kg/ha
    S = S_yield[:, i]   # soy yield kg/ha
    G = G_yield[:, i]   # grass yield kg/ha
    A = A_yield[:, i]   # algae yield kg/ha
    G_L = G_yield_L[:, i]   # grass yield kg/ha
    A_L = A_yield_L[:, i]   # algae yield kg/ha
    
    Hadi = G_ha[:,0]*G

    CG_prod = sum(C_ha[:,0]*Y) #Based on each year and each state total corn biomass production (kg) calculated

    SB_prod = sum(S_ha[:,0]*S) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod = sum(G_ha[:,0]*G) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod = sum(A_ha[:,0]*A) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod_L = sum(G_ha_L[:,0]*G_L) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod_L = sum(A_ha_L[:,0]*A_L) #Based on each year and each state total corn biomass production (kg) calculated
    
    CG_MJ = CG_prod*9.42 #MJ/kg
    S_MJ = SB_prod*8.02 #MJ/kg
    CS_MJ = CG_MJ + S_MJ
    G_MJ = G_prod*8.35 #MJ/kg
    A_MJ = A_prod*20.82 #MJ/kg
    G_AG_MJ = G_prod_L*8.35 #MJ/kg
    A_AG_MJ = A_prod_L*20.82 #MJ/kg
        
    CG_ethanol_total_MJ[i] = CG_MJ
    SB_oil_total_MJ[i] = S_MJ
    CS_total_MJ[i] = CS_MJ
    G_energy_total_MJ[i] = G_MJ
    A_energy_total_MJ[i] = A_MJ
    G_energy_total_MJ_L[i] = G_AG_MJ
    A_energy_total_MJ_L[i] = A_AG_MJ
    
    CC_corn = min(CS_total_MJ)
    GG_grass_ML = min(G_energy_total_MJ)
    AA_algae_ML = min(A_energy_total_MJ)
    GG_grass_AG = min(G_energy_total_MJ_L)
    AA_algae_AG = min(A_energy_total_MJ_L)
    
    columns = ['version','Corn/Soy', 'Switchgrass on ML', 'Algae on ML','Switchgrass on AG', 'Algae on AG']
    df_GHG12_NSGA = pd.DataFrame(columns = columns) 
    df_GHG12_NSGA.loc[len(df_GHG12_NSGA)]= ['MFSP',(CC_corn),(GG_grass_ML),(AA_algae_ML),(GG_grass_AG),(AA_algae_AG)]  

# frames = [df_MFSP12, df_GHG12]
# df = pd.concat(frames)

# #plotting the stacked bar chart
# plt.rcParams.update({'font.size': 15})
# plt.rcParams['font.sans-serif'] = "Arial"
# # axis_label_pad = 10
# tick_pad = 2
# fig, ax = plt.subplots(figsize=(8,8))
# df.plot(kind='bar', stacked=True, ax=ax, color = ["#023e8a","#ffbe0b","#d90429","#8ac926","#6a4c93"],label= "3 Billion" )

# ax.set_ylabel('TotalEnergy Prodcution (MJ)', weight='bold',fontsize=20)
# ax.set_xlabel('12 Billion gallon biofuel production scenarios', weight='bold',fontsize=20)
# ax.set_xticklabels(['MFSP','GHG'],rotation=360, weight='bold',fontsize=20)




##########################################################################################
######################## 20 billion gallon biofuel production MFSP #######################
##########################################################################################

# import excel sheet
df_geo_corn = pd.read_excel('Platypus_codes/combined_pivot_Corn.xlsx', header=0, engine='openpyxl')
df_geo_soy = pd.read_excel('Platypus_codes/combined_pivot_Soy.xlsx', header=0, engine='openpyxl')
df_geo_grass_L = pd.read_excel('Platypus_codes/combined_pivot_AG_Switchgrass.xlsx', header=0, engine='openpyxl')
df_geo_grass = pd.read_excel('Platypus_codes/combined_pivot_ML_Switchgrass.xlsx', header=0, engine='openpyxl')
df_geo_algae_L = pd.read_excel('Platypus_codes/combined_pivot_AG_Algae.xlsx', header=0, engine='openpyxl')
df_geo_algae = pd.read_excel('Platypus_codes/combined_pivot_ML_Algae.xlsx', header=0, engine='openpyxl')

########### MFSP
fn_ha = 'Decision_Variables_LP_crops_' + 'MFSP' +'_' + '20' + '.csv'
df_ha = pd.read_csv(fn_ha, header=0, index_col=0)
# df_ha = pd.read_csv('Results/Decision_Variables_borg_crops_GHG3_10000000_0.001district.csv', header=0, index_col=0)

fn = 'Objective_functions_LP_crops_' + 'MFSP' +'_' + '20' + '.csv'
df_O = pd.read_csv(fn, header=0, index_col=0)
# df_O = pd.read_csv('Results/Objective_functions_borg_crops_GHG3_10000000_0.001district.csv', header=0, index_col=0)

num_c = len(df_geo_corn)

## Dividing corn, soy, grass and algae yield data.
C_ha = np.transpose(df_ha).iloc[0:num_c].values # used hectare for corn (107)
S_ha = np.transpose(df_ha).iloc[num_c:2*num_c].values # used hectare for soy (214)
G_ha = np.transpose(df_ha).iloc[2*num_c:3*num_c].values # used hectare for grass (321)
G_ha_L = np.transpose(df_ha).iloc[3*num_c:4*num_c].values # used hectare for algae (428)
A_ha = np.transpose(df_ha).iloc[4*num_c:5*num_c].values # used hectare for grass (535)
A_ha_L = np.transpose(df_ha).iloc[5*num_c:].values # used hectare for algae (642)

LL = df_geo_corn['land_limits_ha'].values

years = range(1998, 2014)

# Corn Grain yield
C_yield = df_geo_corn.loc[:, 1998:2013].values  # yield in kg/ha

# Soybean yield
S_yield = df_geo_soy.loc[:, 1998:2013].values  # yield in kg/ha

# Grass yield
G_yield_L = df_geo_grass_L.loc[:, 1998:2013].values  # yield in kg/ha

G_yield = df_geo_grass.loc[:, 1998:2013].values  # yield in kg/ha

# Algea yield
A_yield_L = df_geo_algae_L.loc[:, 1998:2013].values  # yield in kg/ha

A_yield = df_geo_algae.loc[:, 1998:2013].values  # yield in kg/ha

num_c = np.size(LL)  # size of land cost
Energy_total = np.zeros((len(years), 1))

CG_ethanol_total_MJ = np.zeros((len(years)))
SB_oil_total_MJ = np.zeros((len(years)))
CS_total_MJ = np.zeros((len(years)))
G_energy_total_MJ = np.zeros((len(years)))
A_energy_total_MJ = np.zeros((len(years)))
G_energy_total_MJ_L = np.zeros((len(years)))
A_energy_total_MJ_L = np.zeros((len(years)))

CS_ethanol_avg = np.zeros((len(df_ha), 1))
SB_oil_avg = np.zeros((len(df_ha), 1))
CS_avg = np.zeros((len(df_ha), 1))
G_energy_avg = np.zeros((len(df_ha), 1))
A_energy_avg = np.zeros((len(df_ha), 1))
G_energy_avg_L = np.zeros((len(df_ha), 1))
A_energy_avg_L = np.zeros((len(df_ha), 1))

# Energy_total = np.zeros((len(solution),1))

for year in years:
    i = years.index(year)
    Y = C_yield[:, i]   # corn yield kg/ha
    S = S_yield[:, i]   # soy yield kg/ha
    G = G_yield[:, i]   # grass yield kg/ha
    A = A_yield[:, i]   # algae yield kg/ha
    G_L = G_yield_L[:, i]   # grass yield kg/ha
    A_L = A_yield_L[:, i]   # algae yield kg/ha
    
    Hadi = G_ha[:,0]*G

    CG_prod = sum(C_ha[:,0]*Y) #Based on each year and each state total corn biomass production (kg) calculated

    SB_prod = sum(S_ha[:,0]*S) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod = sum(G_ha[:,0]*G) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod = sum(A_ha[:,0]*A) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod_L = sum(G_ha_L[:,0]*G_L) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod_L = sum(A_ha_L[:,0]*A_L) #Based on each year and each state total corn biomass production (kg) calculated
    
    CG_MJ = CG_prod*9.42 #MJ/kg
    S_MJ = SB_prod*8.02 #MJ/kg
    CS_MJ = CG_MJ + S_MJ
    G_MJ = G_prod*8.35 #MJ/kg
    A_MJ = A_prod*20.82 #MJ/kg
    G_AG_MJ = G_prod_L*8.35 #MJ/kg
    A_AG_MJ = A_prod_L*20.82 #MJ/kg
        
    CG_ethanol_total_MJ[i] = CG_MJ
    SB_oil_total_MJ[i] = S_MJ
    CS_total_MJ[i] = CS_MJ
    G_energy_total_MJ[i] = G_MJ
    A_energy_total_MJ[i] = A_MJ
    G_energy_total_MJ_L[i] = G_AG_MJ
    A_energy_total_MJ_L[i] = A_AG_MJ
    
    CC_corn = min(CS_total_MJ)
    GG_grass_ML = min(G_energy_total_MJ)
    AA_algae_ML = min(A_energy_total_MJ)
    GG_grass_AG = min(G_energy_total_MJ_L)
    AA_algae_AG = min(A_energy_total_MJ_L)
    
    

    columns = ['version','Corn/Soy', 'Switchgrass on ML', 'Algae on ML','Switchgrass on AG', 'Algae on AG']
    df_MFSP20 = pd.DataFrame(columns = columns) 
    df_MFSP20.loc[len(df_MFSP20)]= ['MFSP',(CC_corn),(GG_grass_ML),(AA_algae_ML),(GG_grass_AG),(AA_algae_AG)]  
    
##########################################################################################
######################## 20 billion gallon biofuel production MFSP - NSGA-III ########################
##########################################################################################

fn_ha = 'Decision_Variables_NSGA_III_' + 'MFSP' +'_' + '20' + '.csv'
df_ha = pd.read_csv(fn_ha, header=0, index_col=0)

fn = 'Objective_functions_NSGA_III_' + 'MFSP' +'_' + '20' + '.csv'
df_O = pd.read_csv(fn, header=0, index_col=0)

num_c = len(df_geo_corn)

## Dividing corn, soy, grass and algae yield data.
CS_ha = np.transpose(df_ha).iloc[0:num_c].values
C_ha = CS_ha/2 # used hectare for corn (107)
S_ha = CS_ha/2# used hectare for soy ()
G_ha_L = np.transpose(df_ha).iloc[num_c:2*num_c].values # used hectare for grass (214)
A_ha_L = np.transpose(df_ha).iloc[2*num_c:3*num_c].values # used hectare for grass (321)
G_ha = np.transpose(df_ha).iloc[3*num_c:4*num_c].values # used hectare for algae (428)
A_ha = np.transpose(df_ha).iloc[4*num_c:5*num_c].values # used hectare for algae (535)

LL = df_geo_corn['land_limits_ha'].values

years = range(1998, 2014)

# Corn Grain yield
C_yield = df_geo_corn.loc[:, 1998:2013].values  # yield in kg/ha

# Soybean yield
S_yield = df_geo_soy.loc[:, 1998:2013].values  # yield in kg/ha

# Grass yield
G_yield_L = df_geo_grass_L.loc[:, 1998:2013].values  # yield in kg/ha

G_yield = df_geo_grass.loc[:, 1998:2013].values  # yield in kg/ha

# Algea yield
A_yield_L = df_geo_algae_L.loc[:, 1998:2013].values  # yield in kg/ha

A_yield = df_geo_algae.loc[:, 1998:2013].values  # yield in kg/ha

num_c = np.size(LL)  # size of land cost
Energy_total = np.zeros((len(years), 1))

CG_ethanol_total_MJ = np.zeros((len(years)))
SB_oil_total_MJ = np.zeros((len(years)))
CS_total_MJ = np.zeros((len(years)))
G_energy_total_MJ = np.zeros((len(years)))
A_energy_total_MJ = np.zeros((len(years)))
G_energy_total_MJ_L = np.zeros((len(years)))
A_energy_total_MJ_L = np.zeros((len(years)))

CS_ethanol_avg = np.zeros((len(df_ha), 1))
SB_oil_avg = np.zeros((len(df_ha), 1))
CS_avg = np.zeros((len(df_ha), 1))
G_energy_avg = np.zeros((len(df_ha), 1))
A_energy_avg = np.zeros((len(df_ha), 1))
G_energy_avg_L = np.zeros((len(df_ha), 1))
A_energy_avg_L = np.zeros((len(df_ha), 1))

for year in years:
    i = years.index(year)
    Y = C_yield[:, i]   # corn yield kg/ha
    S = S_yield[:, i]   # soy yield kg/ha
    G = G_yield[:, i]   # grass yield kg/ha
    A = A_yield[:, i]   # algae yield kg/ha
    G_L = G_yield_L[:, i]   # grass yield kg/ha
    A_L = A_yield_L[:, i]   # algae yield kg/ha
    
    Hadi = G_ha[:,0]*G

    CG_prod = sum(C_ha[:,0]*Y) #Based on each year and each state total corn biomass production (kg) calculated

    SB_prod = sum(S_ha[:,0]*S) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod = sum(G_ha[:,0]*G) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod = sum(A_ha[:,0]*A) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod_L = sum(G_ha_L[:,0]*G_L) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod_L = sum(A_ha_L[:,0]*A_L) #Based on each year and each state total corn biomass production (kg) calculated
    
    CG_MJ = CG_prod*9.42 #MJ/kg
    S_MJ = SB_prod*8.02 #MJ/kg
    CS_MJ = CG_MJ + S_MJ
    G_MJ = G_prod*8.35 #MJ/kg
    A_MJ = A_prod*20.82 #MJ/kg
    G_AG_MJ = G_prod_L*8.35 #MJ/kg
    A_AG_MJ = A_prod_L*20.82 #MJ/kg
        
    CG_ethanol_total_MJ[i] = CG_MJ
    SB_oil_total_MJ[i] = S_MJ
    CS_total_MJ[i] = CS_MJ
    G_energy_total_MJ[i] = G_MJ
    A_energy_total_MJ[i] = A_MJ
    G_energy_total_MJ_L[i] = G_AG_MJ
    A_energy_total_MJ_L[i] = A_AG_MJ
    
    CC_corn = min(CS_total_MJ)
    GG_grass_ML = min(G_energy_total_MJ)
    AA_algae_ML = min(A_energy_total_MJ)
    GG_grass_AG = min(G_energy_total_MJ_L)
    AA_algae_AG = min(A_energy_total_MJ_L)
    
    columns = ['version','Corn/Soy', 'Switchgrass on ML', 'Algae on ML','Switchgrass on AG', 'Algae on AG']
    df_MFSP20_NSGA = pd.DataFrame(columns = columns) 
    df_MFSP20_NSGA.loc[len(df_MFSP20_NSGA)]= ['MFSP',(CC_corn),(GG_grass_ML),(AA_algae_ML),(GG_grass_AG),(AA_algae_AG)]     
    
    
##########################################################################################
######################## 20 billion gallon biofuel production GHG #######################
##########################################################################################
fn_ha = 'Decision_Variables_LP_crops_' + 'GHG' +'_' + '20' + '.csv'
df_ha = pd.read_csv(fn_ha, header=0, index_col=0)
# df_ha = pd.read_csv('Results/Decision_Variables_borg_crops_GHG3_10000000_0.001district.csv', header=0, index_col=0)

fn = 'Objective_functions_LP_crops_' + 'GHG' +'_' + '20' + '.csv'
df_O = pd.read_csv(fn, header=0, index_col=0)
# df_O = pd.read_csv('Results/Objective_functions_borg_crops_GHG3_10000000_0.001district.csv', header=0, index_col=0)

num_c = len(df_geo_corn)

## Dividing corn, soy, grass and algae yield data.
C_ha = np.transpose(df_ha).iloc[0:num_c].values # used hectare for corn (107)
S_ha = np.transpose(df_ha).iloc[num_c:2*num_c].values # used hectare for soy (214)
G_ha = np.transpose(df_ha).iloc[2*num_c:3*num_c].values # used hectare for grass (321)
G_ha_L = np.transpose(df_ha).iloc[3*num_c:4*num_c].values # used hectare for algae (428)
A_ha = np.transpose(df_ha).iloc[4*num_c:5*num_c].values # used hectare for grass (535)
A_ha_L = np.transpose(df_ha).iloc[5*num_c:].values # used hectare for algae (642)

LL = df_geo_corn['land_limits_ha'].values

years = range(1998, 2014)

# Corn Grain yield
C_yield = df_geo_corn.loc[:, 1998:2013].values  # yield in kg/ha

# Soybean yield
S_yield = df_geo_soy.loc[:, 1998:2013].values  # yield in kg/ha

# Grass yield
G_yield_L = df_geo_grass_L.loc[:, 1998:2013].values  # yield in kg/ha

G_yield = df_geo_grass.loc[:, 1998:2013].values  # yield in kg/ha

# Algea yield
A_yield_L = df_geo_algae_L.loc[:, 1998:2013].values  # yield in kg/ha

A_yield = df_geo_algae.loc[:, 1998:2013].values  # yield in kg/ha

num_c = np.size(LL)  # size of land cost
Energy_total = np.zeros((len(years), 1))

CG_ethanol_total_MJ = np.zeros((len(years)))
SB_oil_total_MJ = np.zeros((len(years)))
CS_total_MJ = np.zeros((len(years)))
G_energy_total_MJ = np.zeros((len(years)))
A_energy_total_MJ = np.zeros((len(years)))
G_energy_total_MJ_L = np.zeros((len(years)))
A_energy_total_MJ_L = np.zeros((len(years)))

CS_ethanol_avg = np.zeros((len(df_ha), 1))
SB_oil_avg = np.zeros((len(df_ha), 1))
CS_avg = np.zeros((len(df_ha), 1))
G_energy_avg = np.zeros((len(df_ha), 1))
A_energy_avg = np.zeros((len(df_ha), 1))
G_energy_avg_L = np.zeros((len(df_ha), 1))
A_energy_avg_L = np.zeros((len(df_ha), 1))

# Energy_total = np.zeros((len(solution),1))

for year in years:
    i = years.index(year)
    Y = C_yield[:, i]   # corn yield kg/ha
    S = S_yield[:, i]   # soy yield kg/ha
    G = G_yield[:, i]   # grass yield kg/ha
    A = A_yield[:, i]   # algae yield kg/ha
    G_L = G_yield_L[:, i]   # grass yield kg/ha
    A_L = A_yield_L[:, i]   # algae yield kg/ha
    
    Hadi = G_ha[:,0]*G

    CG_prod = sum(C_ha[:,0]*Y) #Based on each year and each state total corn biomass production (kg) calculated

    SB_prod = sum(S_ha[:,0]*S) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod = sum(G_ha[:,0]*G) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod = sum(A_ha[:,0]*A) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod_L = sum(G_ha_L[:,0]*G_L) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod_L = sum(A_ha_L[:,0]*A_L) #Based on each year and each state total corn biomass production (kg) calculated
    
    CG_MJ = CG_prod*9.42 #MJ/kg
    S_MJ = SB_prod*8.02 #MJ/kg
    CS_MJ = CG_MJ + S_MJ
    G_MJ = G_prod*8.35 #MJ/kg
    A_MJ = A_prod*20.82 #MJ/kg
    G_AG_MJ = G_prod_L*8.35 #MJ/kg
    A_AG_MJ = A_prod_L*20.82 #MJ/kg
        
    CG_ethanol_total_MJ[i] = CG_MJ
    SB_oil_total_MJ[i] = S_MJ
    CS_total_MJ[i] = CS_MJ
    G_energy_total_MJ[i] = G_MJ
    A_energy_total_MJ[i] = A_MJ
    G_energy_total_MJ_L[i] = G_AG_MJ
    A_energy_total_MJ_L[i] = A_AG_MJ
    
    CC_corn = min(CS_total_MJ)
    GG_grass_ML = min(G_energy_total_MJ)
    AA_algae_ML = min(A_energy_total_MJ)
    GG_grass_AG = min(G_energy_total_MJ_L)
    AA_algae_AG = min(A_energy_total_MJ_L)
    
    
    columns = ['version','Corn/Soy', 'Switchgrass on ML', 'Algae on ML','Switchgrass on AG', 'Algae on AG']
    df_GHG20 = pd.DataFrame(columns = columns) 
    df_GHG20.loc[len(df_GHG20)]= ['GHG',(CC_corn),(GG_grass_ML),(AA_algae_ML),(GG_grass_AG),(AA_algae_AG)]  

##########################################################################################
######################## 20 billion gallon biofuel production GHG - NSGA-III ########################
##########################################################################################

fn_ha = 'Decision_Variables_NSGA_III_' + 'GHG' +'_' + '20' + '.csv'
df_ha = pd.read_csv(fn_ha, header=0, index_col=0)

fn = 'Objective_functions_NSGA_III_' + 'GHG' +'_' + '20' + '.csv'
df_O = pd.read_csv(fn, header=0, index_col=0)

num_c = len(df_geo_corn)



## Dividing corn, soy, grass and algae yield data.
CS_ha = np.transpose(df_ha).iloc[0:num_c].values
C_ha = CS_ha/2 # used hectare for corn (107)
S_ha = CS_ha/2# used hectare for soy ()
G_ha_L = np.transpose(df_ha).iloc[num_c:2*num_c].values # used hectare for grass (214)
A_ha_L = np.transpose(df_ha).iloc[2*num_c:3*num_c].values # used hectare for grass (321)
G_ha = np.transpose(df_ha).iloc[3*num_c:4*num_c].values # used hectare for algae (428)
A_ha = np.transpose(df_ha).iloc[4*num_c:5*num_c].values # used hectare for algae (535)

LL = df_geo_corn['land_limits_ha'].values

years = range(1998, 2014)

# Corn Grain yield
C_yield = df_geo_corn.loc[:, 1998:2013].values  # yield in kg/ha

# Soybean yield
S_yield = df_geo_soy.loc[:, 1998:2013].values  # yield in kg/ha

# Grass yield
G_yield_L = df_geo_grass_L.loc[:, 1998:2013].values  # yield in kg/ha

G_yield = df_geo_grass.loc[:, 1998:2013].values  # yield in kg/ha

# Algea yield
A_yield_L = df_geo_algae_L.loc[:, 1998:2013].values  # yield in kg/ha

A_yield = df_geo_algae.loc[:, 1998:2013].values  # yield in kg/ha

num_c = np.size(LL)  # size of land cost
Energy_total = np.zeros((len(years), 1))

CG_ethanol_total_MJ = np.zeros((len(years)))
SB_oil_total_MJ = np.zeros((len(years)))
CS_total_MJ = np.zeros((len(years)))
G_energy_total_MJ = np.zeros((len(years)))
A_energy_total_MJ = np.zeros((len(years)))
G_energy_total_MJ_L = np.zeros((len(years)))
A_energy_total_MJ_L = np.zeros((len(years)))

CS_ethanol_avg = np.zeros((len(df_ha), 1))
SB_oil_avg = np.zeros((len(df_ha), 1))
CS_avg = np.zeros((len(df_ha), 1))
G_energy_avg = np.zeros((len(df_ha), 1))
A_energy_avg = np.zeros((len(df_ha), 1))
G_energy_avg_L = np.zeros((len(df_ha), 1))
A_energy_avg_L = np.zeros((len(df_ha), 1))

for year in years:
    i = years.index(year)
    Y = C_yield[:, i]   # corn yield kg/ha
    S = S_yield[:, i]   # soy yield kg/ha
    G = G_yield[:, i]   # grass yield kg/ha
    A = A_yield[:, i]   # algae yield kg/ha
    G_L = G_yield_L[:, i]   # grass yield kg/ha
    A_L = A_yield_L[:, i]   # algae yield kg/ha
    
    Hadi = G_ha[:,0]*G

    CG_prod = sum(C_ha[:,0]*Y) #Based on each year and each state total corn biomass production (kg) calculated

    SB_prod = sum(S_ha[:,0]*S) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod = sum(G_ha[:,0]*G) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod = sum(A_ha[:,0]*A) #Based on each year and each state total corn biomass production (kg) calculated

    G_prod_L = sum(G_ha_L[:,0]*G_L) #Based on each year and each state total corn biomass production (kg) calculated

    A_prod_L = sum(A_ha_L[:,0]*A_L) #Based on each year and each state total corn biomass production (kg) calculated
    
    CG_MJ = CG_prod*9.42 #MJ/kg
    S_MJ = SB_prod*8.02 #MJ/kg
    CS_MJ = CG_MJ + S_MJ
    G_MJ = G_prod*8.35 #MJ/kg
    A_MJ = A_prod*20.82 #MJ/kg
    G_AG_MJ = G_prod_L*8.35 #MJ/kg
    A_AG_MJ = A_prod_L*20.82 #MJ/kg
        
    CG_ethanol_total_MJ[i] = CG_MJ
    SB_oil_total_MJ[i] = S_MJ
    CS_total_MJ[i] = CS_MJ
    G_energy_total_MJ[i] = G_MJ
    A_energy_total_MJ[i] = A_MJ
    G_energy_total_MJ_L[i] = G_AG_MJ
    A_energy_total_MJ_L[i] = A_AG_MJ
    
    CC_corn = min(CS_total_MJ)
    GG_grass_ML = min(G_energy_total_MJ)
    AA_algae_ML = min(A_energy_total_MJ)
    GG_grass_AG = min(G_energy_total_MJ_L)
    AA_algae_AG = min(A_energy_total_MJ_L)
    
    columns = ['version','Corn/Soy', 'Switchgrass on ML', 'Algae on ML','Switchgrass on AG', 'Algae on AG']
    df_GHG20_NSGA = pd.DataFrame(columns = columns) 
    df_GHG20_NSGA.loc[len(df_GHG20_NSGA)]= ['MFSP',(CC_corn),(GG_grass_ML),(AA_algae_ML),(GG_grass_AG),(AA_algae_AG)]  
# frames = [df_MFSP20, df_GHG20]
# df = pd.concat(frames)

# #plotting the stacked bar chart
# plt.rcParams.update({'font.size': 15})
# plt.rcParams['font.sans-serif'] = "Arial"
# # axis_label_pad = 10
# tick_pad = 2
# fig, ax = plt.subplots(figsize=(8,8))
# df.plot(kind='bar', stacked=True, ax=ax, color = ["#023e8a","#ffbe0b","#d90429","#8ac926","#6a4c93"])

# ax.set_ylabel('TotalEnergy Prodcution (MJ)', weight='bold',fontsize=20)
# ax.set_xlabel('20 Billion gallon biofuel production scenarios', weight='bold',fontsize=20)
# ax.set_xticklabels(['MFSP','GHG'],rotation=360, weight='bold',fontsize=20)



frames = [df_MFSP3,df_MFSP3_NSGA, df_GHG3,df_GHG3_NSGA, 
          df_MFSP12, df_MFSP12_NSGA, df_GHG12,df_GHG12_NSGA,
          df_MFSP20,df_MFSP20_NSGA, df_GHG20, df_GHG20_NSGA]
df = pd.concat(frames)

#plotting the stacked bar chart
plt.rcParams.update({'font.size': 15})
plt.rcParams['font.sans-serif'] = "Arial"
# axis_label_pad = 10
tick_pad = 2
fig, ax = plt.subplots(figsize=(8,8))
df.plot(kind='bar', stacked=True, ax=ax, color = ["#023e8a","#ffbe0b","#d90429","#8ac926","#6a4c93"])

ax.set_ylabel('Total Energy Production (MJ)', weight='bold',fontsize=20)
ax.set_xlabel('Billion gallon biofuel production scenarios', weight='bold',fontsize=20)
ax.set_xticklabels(['3','3','3','3','12','12','12','12','20','20','20','20'],rotation=360, weight='bold',fontsize=20)

        
