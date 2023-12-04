# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:43:48 2023

@author: eari
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from mpl_toolkits.mplot3d import *
from random import random, seed
from matplotlib import cm




fig, ax = plt.subplots(3,2,figsize=(15,20),subplot_kw=dict(projection='3d'))
plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

# ax = fig.add_subplot(1, 4, 1, projection='3d')

##############################
###### 3 billion gallon ######
##############################

### State Level Solution ###
fn = 'State Level Borg objective func 3b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall'] 
sequence_containing_z_vals = df_O['GHG_emission/MJ'] 
  
ax[0,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#023e8a',s=20, marker="o"); #,alpha=0.2  




### Clustered Level solution ###
fn = 'Cluster Level Borg objective func 3b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[0,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#ffbe0b',s=20, marker="o");



### District Level solution ###
fn = 'Borg objective func 3b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']


ax[0,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#6a4c93',s=20, marker="o");

### NSGA-II Level solution ### 
fn = 'NSGA_II objective func 3b 10M 0.01E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']


ax[0,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#8ac926',s=20, marker="v");



### NSGA-III Level solution ###
fn = 'NSGA_III objective func 3b 10M 0.01E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']


ax[0,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#d90429',s=20, marker="D");

ax[0,0].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[0,0].set_xlim(0.08,0.02)
ax[0,0].set_ylim(0)
ax[0,0].set_ylabel('Quota Shortfall(MJ) \n $\mathregular{10^{10}}$', fontsize=14,labelpad=20, fontweight='bold')
ax[0,0].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14,labelpad=10, fontweight='bold')
ax[0,0].tick_params(axis='both', which='major', labelsize=14)

# ax[0,0].view_init(30, 30)
# ax[0,0].set_title('3 Billion Gallon',  size=18, fontweight="bold")


### LP Level solution _cost ###
fn = 'Objective_functions_LP_crops_3' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[0,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#0d1b2a',s=20, marker="s");

ax[0,0].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[0,0].set_xlim(0.08,0.02)
ax[0,0].set_ylim(0,80)
ax[0,0].set_ylabel('Quota Shortfall(MJ) \n $\mathregular{10^{10}}$', fontsize=14 ,labelpad=18, fontweight='bold')
ax[0,0].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[0,0].tick_params(axis='both', which='major', labelsize=14)




### LP Level solution _GHG ###
fn = 'Objective_functions_LP_crops_GHG3' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[0,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#0d1b2a',s=20, marker="s");

ax[0,0].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[0,0].set_xlim(0.08,0.02)
ax[0,0].set_ylim(0,70)
ax[0,0].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[0,0].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[0,0].tick_params(axis='both', which='major', labelsize=14)



### Ideal point ###
fn = 'ideal_point' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[0,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#fb6107', s=500, marker="*");

ax[0,0].set_xlabel('MFSP ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[0,0].set_xlim(0.08,0)
ax[0,0].set_ylabel('Quota Shortfall(MJ) \n $\mathregular{10^{10}}$', fontsize=14 ,labelpad=18, fontweight='bold')
ax[0,0].set_zlabel('GHG Intensity \n $\mathregular{(gCO^{2}/MJ)}$', fontsize=14 ,labelpad=10, fontweight='bold')
ax[0,0].tick_params(axis='both', which='major', labelsize=14)

ax[0,0].view_init(45, 45)
ax[0,0].set_title('3 Billion Gallon',  size=18, fontweight="bold", x=0.5, y=0.2)


##############################
###### 6 billion gallon ######
##############################

# fig = plt.figure(figsize=(20,20))
# ax = fig.add_subplot(1, 2, 2, projection='3d')

### State Level Solution ###
fn = 'State Level Borg objective func 6b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']
  
ax[0,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#023e8a',s=20, marker="o");


### Clustered Level solution ###
fn = 'Cluster Level Borg objective func 6b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[0,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#ffbe0b',s=20, marker="o");


### District Level solution ###
fn = 'Borg objective func 6b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[0,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#6a4c93',s=20, marker="o"); 

### NSGA-II Level solution ###
fn = 'NSGA_II objective func 6b 10M 0.01E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[0,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#8ac926',s=20, marker="v");


## NSGA-III Level solution 
fn = 'NSGA_III objective func 6b 10M 0.01E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[0,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#d90429',s=20, marker="D");

ax[0,1].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[0,1].set_xlim(0.08,0.02)
ax[0,1].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[0,1].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[0,1].tick_params(axis='both', which='major', labelsize=14)

# ## LP Level solution _cost
fn = 'Objective_functions_LP_crops_6' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[0,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#0d1b2a',s=20, marker="s");

ax[0,1].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[0,1].set_xlim(0.08,0.02)
ax[0,1].set_ylim(0,70)
ax[0,1].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[0,1].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[0,1].tick_params(axis='both', which='major', labelsize=14)

# ## LP Level solution _GHG
fn = 'Objective_functions_LP_crops_GHG6' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[0,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#0d1b2a', s=20, marker="s");

ax[0,1].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[0,1].set_xlim(0.08,0.02)
ax[0,1].set_ylim(0)
ax[0,1].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[0,1].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[0,1].tick_params(axis='both', which='major', labelsize=14)
# ax[0,1].view_init(60, 60)
# ax[0,1].set_title('6 Billion Gallon',  size=18, fontweight="bold")

### Ideal point ###
fn = 'ideal_point' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[0,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#fb6107', s=500, marker="*");

ax[0,1].set_xlabel('MFSP ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[0,1].set_xlim(0.08,0)
ax[0,1].set_ylim(0)
ax[0,1].set_ylabel('Quota Shortfall(MJ) \n $\mathregular{10^{10}}$', fontsize=14 ,labelpad=18, fontweight='bold')
ax[0,1].set_zlabel('GHG Intensity \n $\mathregular{(gCO^{2}/MJ)}$', fontsize=14 ,labelpad=10, fontweight='bold')
ax[0,1].tick_params(axis='both', which='major', labelsize=14)

ax[0,1].view_init(45, 45)
ax[0,1].set_title('6 Billion Gallon',  size=18, fontweight="bold", x=0.5, y=0.2)


### 9 billion gallon 
# fig = plt.figure(figsize=(20,20))
# ax = fig.add_subplot(1, 3, 2, projection='3d')

## State Level Solution
fn = 'State Level Borg objective func 9b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']
  
ax[1,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#023e8a', s=20, marker="o");


## Clustered Level solution 
fn = 'Cluster Level Borg objective func 9b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[1,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#ffbe0b', s=20 , marker="o");


## District Level solution 
fn = 'Borg objective func 9b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[1,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#6a4c93', s=20, marker="o");

## NSGA-II Level solution 
fn = 'NSGA_II objective func 9b 10M 0.01E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[1,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#8ac926', s=20, marker="v");


## NSGA-III Level solution 
fn = 'NSGA_III objective func 9b 10M 0.01E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[1,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#d90429', s=20, marker="D");

ax[1,0].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[1,0].set_xlim(0.08,0.02)
ax[1,0].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[1,0].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[1,0].tick_params(axis='both', which='major', labelsize=14)

# ## LP Level solution _cost
fn = 'Objective_functions_LP_crops_9' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[1,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#0d1b2a', s=20, marker="s");

ax[1,0].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[1,0].set_xlim(0.08,0.02)
ax[1,0].set_ylim(0)
ax[1,0].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[1,0].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[1,0].tick_params(axis='both', which='major', labelsize=14)

# ## LP Level solution _GHG
fn = 'Objective_functions_LP_crops_GHG9' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[1,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#0d1b2a', s=20, marker="s");

ax[1,0].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[1,0].set_xlim(0.08,0.02)
ax[1,0].set_ylim(0,70)
ax[1,0].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[1,0].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[1,0].tick_params(axis='both', which='major', labelsize=14)
# ax[1,0].view_init(60, 60)


### Ideal point ###
fn = 'ideal_point' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[1,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#fb6107', s=500, marker="*");

ax[1,0].set_xlabel('MFSP ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[1,0].set_xlim(0.08,0)
ax[1,0].set_ylim(0)
ax[1,0].set_ylabel('Quota Shortfall(MJ) \n $\mathregular{10^{10}}$', fontsize=14 ,labelpad=18, fontweight='bold')
ax[1,0].set_zlabel('GHG Intensity \n $\mathregular{(gCO^{2}/MJ)}$', fontsize=14 ,labelpad=10, fontweight='bold')
ax[1,0].tick_params(axis='both', which='major', labelsize=14)

ax[1,0].view_init(45, 45)
ax[1,0].set_title('9 Billion Gallon',  size=18, fontweight="bold", x=0.5, y=0.2)



## 15 billion gallon 
## State Level Solution
fn = 'State Level Borg objective func 15b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']
  
ax[1,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#023e8a', s=20, marker="o");


## Clustered Level solution 
fn = 'Cluster Level Borg objective func 15b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[1,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#ffbe0b', s=20, marker="o");


## District Level solution 
fn = 'Borg objective func 15b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[1,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#6a4c93', s=20, marker="o");

## NSGA-II Level solution 
fn = 'NSGA_II objective func 15b 10M 0.01E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[1,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#8ac926', s=20, marker="v");


## NSGA-III Level solution 
fn = 'NSGA_III objective func 15b 10M 0.01E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[1,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#d90429', s=20, marker="D");

ax[1,1].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[1,1].set_xlim(0.08,0.02)
ax[1,1].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[1,1].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[1,1].tick_params(axis='both', which='major', labelsize=14)

# ## LP Level solution _cost
fn = 'Objective_functions_LP_crops_15' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[1,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#0d1b2a', s=20, marker="s");

ax[1,1].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[1,1].set_xlim(0.08,0.02)
ax[1,1].set_ylim(0)
ax[1,1].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[1,1].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[1,1].tick_params(axis='both', which='major', labelsize=14)

# ## LP Level solution _GHG
fn = 'Objective_functions_LP_crops_GHG15' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[1,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#0d1b2a', s=20, marker="s");

ax[1,1].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[1,1].set_xlim(0.08,0.02)
ax[1,1].set_ylim(0,70)
ax[1,1].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[1,1].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[1,1].tick_params(axis='both', which='major', labelsize=14)
# ax[1,1].view_init(60, 60)


### Ideal point ###
fn = 'ideal_point' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[1,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#fb6107', s=500, marker="*");

ax[1,1].set_xlabel('MFSP ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[1,1].set_xlim(0.08,0)
ax[1,1].set_ylim(0)
ax[1,1].set_ylabel('Quota Shortfall(MJ) \n $\mathregular{10^{10}}$', fontsize=14 ,labelpad=18, fontweight='bold')
ax[1,1].set_zlabel('GHG Intensity \n $\mathregular{(gCO^{2}/MJ)}$', fontsize=14 ,labelpad=10, fontweight='bold')
ax[1,1].tick_params(axis='both', which='major', labelsize=14)

ax[1,1].view_init(45, 45)
ax[1,1].set_title('15 Billion Gallon',  size=18, fontweight="bold", x=0.5, y=0.2)

### 18 billion gallon 
# fig = plt.figure(figsize=(20,20))
# ax = fig.add_subplot(1, 2, 2, projection='3d')

## State Level Solution
fn = 'State Level Borg objective func 18b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']
  
ax[2,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#023e8a', s=20, marker="o");


## Clustered Level solution 
fn = 'Cluster Level Borg objective func 18b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[2,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#ffbe0b', s=20, marker="o");


## District Level solution 
fn = 'Borg objective func 18b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[2,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#6a4c93', s=20, marker="o");

## NSGA-II Level solution 
fn = 'NSGA_II objective func 18b 10M 0.01E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[2,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#8ac926', s=20, marker="v");


## NSGA-III Level solution 
fn = 'NSGA_III objective func 18b 10M 0.01E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[2,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#d90429', s=20, marker="D");

ax[2,0].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[2,0].set_xlim(0.08,0.02)
ax[2,0].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[2,0].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[2,0].tick_params(axis='both', which='major', labelsize=14)


# ## LP Level solution _cost
fn = 'Objective_functions_LP_crops_18' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[2,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#0d1b2a', s=20, marker="s");

ax[2,0].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[2,0].set_xlim(0.08,0.02)
ax[2,0].set_ylim(0)
ax[2,0].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[2,0].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[2,0].tick_params(axis='both', which='major', labelsize=14)

# ## LP Level solution _GHG
fn = 'Objective_functions_LP_crops_GHG9' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[2,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#0d1b2a', s=20, marker="s");

ax[2,0].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[2,0].set_xlim(0.08,0.02)
ax[2,0].set_ylim(0,70)
ax[2,0].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[2,0].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[2,0].tick_params(axis='both', which='major', labelsize=14)
# ax[2,0].view_init(60, 60)


### Ideal point ###
fn = 'ideal_point' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[2,0].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#fb6107', s=500, marker="*");

ax[2,0].set_xlabel('MFSP ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[2,0].set_xlim(0.08,0)
ax[2,0].set_ylim(0)
ax[2,0].set_ylabel('Quota Shortfall(MJ) \n $\mathregular{10^{10}}$', fontsize=14 ,labelpad=18, fontweight='bold')
ax[2,0].set_zlabel('GHG Intensity \n $\mathregular{(gCO^{2}/MJ)}$', fontsize=14 ,labelpad=10, fontweight='bold')
ax[2,0].tick_params(axis='both', which='major', labelsize=14)

ax[2,0].view_init(45, 45)
ax[2,0].set_title('18 Billion Gallon',  size=18, fontweight="bold", x=0.5, y=0.2)


### 20 billion gallon 
# fig = plt.figure(figsize=(20,20))
# ax = fig.add_subplot(1, 3, 2, projection='3d')

## State Level Solution
fn = 'State Level Borg objective func 20b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']
  
ax[2,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#023e8a', s=20, marker="o");


## Clustered Level solution 
fn = 'Cluster Level Borg objective func 20b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[2,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#ffbe0b', s=20, marker="o");


## District Level solution 
fn = 'Borg objective func 20b 10M 0.001E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[2,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#6a4c93', s=20, marker="o");

## NSGA-II Level solution 
fn = 'NSGA_II objective func 20b 10M 0.01E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[2,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#8ac926', s=20, marker="v");


## NSGA-III Level solution 
fn = 'NSGA_III objective func 20b 10M 0.01E' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[2,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#d90429', s=20, marker="D");

ax[2,1].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[2,1].set_xlim(0.08,0.02)
ax[2,1].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[2,1].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[2,1].tick_params(axis='both', which='major', labelsize=14)

# ## LP Level solution _cost
fn = 'Objective_functions_LP_crops_20' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[2,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#0d1b2a', s=20, marker="s");

ax[2,1].set_xlabel('Cost ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[2,1].set_xlim(0.08,0.02)
ax[2,1].set_ylim(0)
ax[2,1].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[2,1].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[2,1].tick_params(axis='both', which='major', labelsize=14)

# ## LP Level solution _GHG
fn = 'Objective_functions_LP_crops_GHG20' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[2,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#0d1b2a', s=20, marker="s");

ax[2,1].set_xlabel('MFSP ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[2,1].set_xlim(0.08,0.02)
ax[2,1].set_ylim(0,70)
ax[2,1].set_ylabel('Quota Shortfall(MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[2,1].set_zlabel('GHG Intensity (gCO2/MJ)', fontsize=14 ,labelpad=10, fontweight='bold')
ax[2,1].tick_params(axis='both', which='major', labelsize=14)



### Ideal point ###
fn = 'ideal_point' +'.csv'

df_O = pd.read_csv(fn,header=0,index_col=0)
df_O.columns = ['cost','energy_shortfall','GHG_emission']
df_O['cost/MJ'] = df_O['cost']
df_O['GHG_emission/MJ'] = df_O['GHG_emission']
df_O['energy_shortfall'] = df_O['energy_shortfall']/10**10

sequence_containing_x_vals = df_O['cost/MJ']
sequence_containing_y_vals = df_O['energy_shortfall']
sequence_containing_z_vals = df_O['GHG_emission/MJ']

ax[2,1].scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c='#fb6107', s=500, marker="*");

ax[2,1].set_xlabel('MFSP ($/MJ)', fontsize=14 ,labelpad=15, fontweight='bold')
ax[2,1].set_xlim(0.08,0)
ax[2,1].set_ylim(0)
ax[2,1].set_ylabel('Quota Shortfall(MJ) \n $\mathregular{10^{10}}$', fontsize=14 ,labelpad=18, fontweight='bold')
ax[2,1].set_zlabel('GHG Intensity \n $\mathregular{(gCO^{2}/MJ)}$', fontsize=14 ,labelpad=10, fontweight='bold')
ax[2,1].tick_params(axis='both', which='major', labelsize=14)

ax[2,1].view_init(45, 45)
ax[2,1].set_title('20 Billion Gallon',  size=18, fontweight="bold", x=0.5, y=0.2)


plt.subplots_adjust(wspace=0, hspace=0.1)
plt.legend(["Borg State Level" ,"Borg Clustered District Level" , "Borg District Level" ,"NSGA-II","NSGA-III","LP", "Ideal_point"], bbox_to_anchor = (1.20,-0.1), ncol=7,handletextpad=-0.4 ,columnspacing = 0.001,fancybox=True, shadow=True,fontsize=16)

plt.savefig('Combined_3d_pareto.png',dpi=300, bbox_inches='tight')

        




