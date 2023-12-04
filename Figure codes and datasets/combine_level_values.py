# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:40:02 2023

@author: eari
"""

# importing the modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

# ### Importing excels ###
### Combined LEVEL ###
###### MFSP ######

plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams.update({'font.size': 30})

df_state = pd.read_excel('Combined_cost_d.xlsx',header=0, engine='openpyxl')
# state_column = np.zeros((len(df_state),1))
# state_column ='State'
# df_state.insert(loc=0,column='Level',value=state_column)

fig,ax = plt.subplots(2, figsize =(30,25))
plt.subplots_adjust(wspace=0, hspace=0.01)
## Graph format
#Borg_State=shading red
#Borg_Cluster=shading orange
#Borg_District=shading yellow
#Borg_Fractured=shading green
#NSGAII_Fractured=shading purple
#NSGAIII_Fractured=shading blue
#LP=black
sns.barplot(ax=ax[0],data=df_state, x="Billion", y="cost", hue="Version",palette={'100k_0.001_S':'#641220',
                                                                                    '1M_0.1_S':'#6e1423',
                                                                                    '1M_0.001_S':'#85182a',
                                                                                    '10M_0.001_S':'#a11d33',
                                                                                    
                                                                                    '100k_0.001_C':'#ff7b00',
                                                                                    '1M_0.1_C':'#ff8800',
                                                                                    '1M_0.001_C':'#ff9500',
                                                                                    '10M_0.001_C':'#ffa200',
                                                                                    
                                                                                    '100k_0.001_D':'#ffd900',
                                                                                    '1M_0.1_D':'#ffe600',
                                                                                    '1M_0.001_D':'#fff200',
                                                                                    '10M_0.001_D':'#eeef20',
                                                                                    
                                                                                    '100k_II':'#55a630',
                                                                                    '1M_II':'#2b9348',
                                                                                    '10M_II':'#007f5f',
                                                                                    
                                                                                    '100k_III':'#00509d',
                                                                                    '1M_III':'#003f88',
                                                                                    '10M_III':'#00296b',
                                                                                    
                                                                                    'LP_District':'#0b090a'},edgecolor ='black')

# plt.show()


# sns.barplot(ax=ax,data=df_state, x="Billion", y="cost", hue="Version",palette={'100k_0.001_S':'#023e8a',
#                                                                                     '1M_0.1_S':'#0077b6',
#                                                                                     '1M_0.001_S':'#0096c7',
#                                                                                     '10M_0.001_S':'#00b4d8',
                                                                                    
#                                                                                     '100k_0.001_C':'#007f5f',
#                                                                                     '1M_0.1_C':'#2b9348',
#                                                                                     '1M_0.001_C':'#55a630',
#                                                                                     '10M_0.001_C':'#80b918',
                                                                                    
#                                                                                     '100k_0.001_D':'#660708',
#                                                                                     '1M_0.1_D':'#a4161a',
#                                                                                     '1M_0.001_D':'#ba181b',
#                                                                                     '10M_0.001_D':'#e5383b',
#                                                                                     'LP_District':'#0b090a'},edgecolor ='black')

# Adding Xticks
# plt.xlabel('Version (Billion Gallon Biofuel Production)', fontweight ='bold', fontsize = 30)
ax[0].set_ylabel('Cost ($/MJ)', fontweight ='bold', fontsize = 30)
ax[0].set(xlabel=None)

# plt.title('Combined Level Scenario Comparison for MFSP',fontsize=20,fontweight="bold")
# plt.xticks(fontsize=30, rotation=0)
# plt.yticks(fontsize=30, rotation=0)

ax[0].get_legend().remove()
  

# ax.legend(loc='buttom center', bbox_to_anchor=(0.5, -0.07),
#           ncol=5, fancybox=True, shadow=True, fontsize=30)

# plt.show()
# plt.savefig('Combined Level Scenario Comparison for MFSP.png',dpi=150, bbox_inches='tight')
# plt.clf()


###### GHG ######
df_state = pd.read_excel('Combined_GHG.xlsx',header=0, engine='openpyxl')
# state_column = np.zeros((len(df_state),1))
# state_column ='State'
# fig,ax = plt.subplots(figsize =(35,18))
sns.barplot(ax=ax[1],data=df_state, x="Billion", y="min_GHG_emission", hue="Version",palette={'100k_0.001_S':'#641220',
                                                                                    '1M_0.1_S':'#6e1423',
                                                                                    '1M_0.001_S':'#85182a',
                                                                                    '10M_0.001_S':'#a11d33',
                                                                                    
                                                                                    '100k_0.001_C':'#ff7b00',
                                                                                    '1M_0.1_C':'#ff8800',
                                                                                    '1M_0.001_C':'#ff9500',
                                                                                    '10M_0.001_C':'#ffa200',
                                                                                    
                                                                                    '100k_0.001_D':'#ffd900',
                                                                                    '1M_0.1_D':'#ffe600',
                                                                                    '1M_0.001_D':'#fff200',
                                                                                    '10M_0.001_D':'#eeef20',
                                                                                    
                                                                                    '100k_0.01_II':'#55a630',
                                                                                    '1M_0.01_II':'#2b9348',
                                                                                    '10M_0.01_II':'#007f5f',
                                                                                    
                                                                                    '100k_0.01_III':'#00509d',
                                                                                    '1M_0.01_III':'#003f88',
                                                                                    '10M_0.01_III':'#00296b',
                                                                                    
                                                                                    'LP_District':'#0b090a'},edgecolor ='black')
# plt.show()


# Adding Xticks
plt.xlabel('Version (Billion Gallon Biofuel Production)', fontweight ='bold', fontsize = 30)
plt.ylabel(r'GHG Intensity (g $CO_{2}$ / MJ)', fontweight ='bold', fontsize = 30)


# plt.title('Combined Level Scenario Comparison for GHG Intensity',fontsize=18,fontweight="bold")
plt.xticks(fontsize=30, rotation=0)
plt.yticks(fontsize=30, rotation=0)
   
# ax[1].get_legend().remove()
# labels =["State Level Borg:","Clustered Level Borg:","District Level Borg:","District Level NSGA-II:", "District Level NSGA-III:", "District Level LP:"]


# ax[1].legend(labels, loc='upper center',bbox_to_anchor=(0.5, -0.10),
#           ncol=6, fancybox=True, shadow=True, fontsize=30)

ax[1].legend(loc='upper center',bbox_to_anchor=(0.5, -0.10),
          ncol=6, fancybox=True, shadow=True, fontsize=30)
# plt.show()
# plt.savefig('Combined Level Scenario Comparison for GHG Intensity.png',dpi=150, bbox_inches='tight')
plt.savefig('Combined Level Scenario Comparison for both.png',dpi=150, bbox_inches='tight')
plt.clf()




# ### STATE LEVEL ###
# ###### MFSP ######
# df_state = pd.read_excel('State_Borg_cost.xlsx',header=0, engine='openpyxl')
# state_column = np.zeros((len(df_state),1))
# state_column ='State'
# df_state.insert(loc=0,column='Level',value=state_column)
# fig,ax = plt.subplots(figsize =(12,8))
# sns.barplot(ax=ax,data=df_state, x="Billion", y="cost", hue="Version",palette={'100k_0.001':'#448aff',
#                                                                                     '1M_0.1':'#1565c0',
#                                                                                     '1M_0.001':'#8bc34a',
#                                                                                     '10M_0.001':'#ffc107',
#                                                                                     'LP':'#f44336'},edgecolor ='black')
# # plt.show()

# # Adding Xticks
# plt.xlabel('Version (Billion Gallon Biofuel Production)', fontweight ='bold', fontsize = 18)
# plt.ylabel('Cost ($/MJ)', fontweight ='bold', fontsize = 18)


# plt.title('State Level Scenario Comparison for MFSP',fontsize=18,fontweight="bold")
# plt.xticks(fontsize=18, rotation=0)
# plt.yticks(fontsize=18, rotation=0)
  
# # plt.legend()
# # plt.show()
# plt.savefig('State Level Scenario Comparison for MFSP.png',dpi=150, bbox_inches='tight')
# plt.clf()


# ###### GHG ######
# df_state = pd.read_excel('State_Borg_GHG.xlsx',header=0, engine='openpyxl')
# state_column = np.zeros((len(df_state),1))
# state_column ='State'
# df_state.insert(loc=0,column='Level',value=state_column)
# fig,ax = plt.subplots(figsize =(12,8))
# sns.barplot(ax=ax,data=df_state, x="Billion", y="min_GHG_emission", hue="Version",palette={'100k_0.001':'#448aff',
#                                                                                     '1M_0.1':'#1565c0',
#                                                                                     '1M_0.001':'#8bc34a',
#                                                                                     '10M_0.001':'#ffc107',
#                                                                                     'LP':'#f44336'},edgecolor ='black')
# # plt.show()

# # Adding Xticks
# plt.xlabel('Version (Billion Gallon Biofuel Production)', fontweight ='bold', fontsize = 18)
# plt.ylabel(r'GHG Intensity (g $CO_{2}$ / MJ)', fontweight ='bold', fontsize = 18)


# plt.title('State Level Scenario Comparison for GHG Intensity',fontsize=18,fontweight="bold")
# plt.xticks(fontsize=18, rotation=0)
# plt.yticks(fontsize=18, rotation=0)
  
# # plt.legend()
# # plt.show()
# plt.savefig('State Level Scenario Comparison for GHG Intensity.png',dpi=150, bbox_inches='tight')
# plt.clf()







# ### CLUSTER LEVEL ###
# ###### MFSP ###### 
# df_cluster = pd.read_excel('Cluster_Borg_cost.xlsx',header=0, engine='openpyxl')
# cluster_column = np.zeros((len(df_cluster),1))
# cluster_column ='Cluster'
# df_cluster.insert(loc=0,column='Level',value=cluster_column)
# fig,ax = plt.subplots(figsize =(12,8))
# sns.barplot(ax=ax,data=df_cluster, x="Billion", y="cost", hue="Version",palette={'100k_0.001':'#448aff',
#                                                                                     '1M_0.1':'#1565c0',
#                                                                                     '1M_0.001':'#8bc34a',
#                                                                                     '10M_0.001':'#ffc107',
#                                                                                     'LP':'#f44336'},edgecolor ='black')
# # plt.show()

# # Adding Xticks
# plt.xlabel('Version (Billion Gallon Biofuel Production)', fontweight ='bold', fontsize = 18)
# plt.ylabel('Cost ($/MJ)', fontweight ='bold', fontsize = 18)


# plt.title('Cluster Level Scenario Comparison for MFSP',fontsize=18,fontweight="bold")
# plt.xticks(fontsize=18, rotation=0)
# plt.yticks(fontsize=18, rotation=0)
  
# # plt.legend()
# # plt.show()
# plt.savefig('Cluster Level Scenario Comparison for MFSP.png',dpi=150, bbox_inches='tight')
# plt.clf()


# ###### GHG ###### 
# df_cluster = pd.read_excel('Cluster_Borg_GHG.xlsx',header=0, engine='openpyxl')
# cluster_column = np.zeros((len(df_cluster),1))
# cluster_column ='Cluster'
# df_cluster.insert(loc=0,column='Level',value=cluster_column)
# fig,ax = plt.subplots(figsize =(12,8))
# sns.barplot(ax=ax,data=df_cluster, x="Billion", y="min_GHG_emission", hue="Version",palette={'100k_0.001':'#448aff',
#                                                                                     '1M_0.1':'#1565c0',
#                                                                                     '1M_0.001':'#8bc34a',
#                                                                                     '10M_0.001':'#ffc107',
#                                                                                     'LP':'#f44336'},edgecolor ='black')
# # plt.show()

# # Adding Xticks
# plt.xlabel('Version (Billion Gallon Biofuel Production)', fontweight ='bold', fontsize = 18)
# plt.ylabel(r'GHG Intensity (g $CO_{2}$ / MJ)', fontweight ='bold', fontsize = 18)


# plt.title('Cluster Level Scenario Comparison for GHG Intensity',fontsize=18,fontweight="bold")
# plt.xticks(fontsize=18, rotation=0)
# plt.yticks(fontsize=18, rotation=0)
  
# # plt.legend()
# # plt.show()
# plt.savefig('Cluster Level Scenario Comparison for GHG Intensity.png',dpi=150, bbox_inches='tight')
# plt.clf()




# ### DISTRICT LEVEL ### 
# ###### MFSP ###### 
# df_district = pd.read_excel('District_Borg_cost.xlsx',header=0, engine='openpyxl')
# district_column = np.zeros((len(df_district),1))
# district_column ='District'
# df_district.insert(loc=0,column='Level',value=district_column)
# fig,ax = plt.subplots(figsize =(12,8))
# sns.barplot(ax=ax,data=df_district, x="Billion", y="cost", hue="Version",palette={'100k_0.001':'#448aff',
#                                                                                     '1M_0.1':'#1565c0',
#                                                                                     '1M_0.001':'#8bc34a',
#                                                                                     '10M_0.001':'#ffc107',
#                                                                                     'LP':'#f44336'},edgecolor ='black')
# # sns.barplot(ax=ax,data=df_district, x="Billion", y="cost", hue="Version",palette=['blue','red','red','red','red'])
# # plt.show()

# # Adding Xticks
# plt.xlabel('Version (Billion Gallon Biofuel Production)', fontweight ='bold', fontsize = 18)
# plt.ylabel('Cost ($/MJ)', fontweight ='bold', fontsize = 18)


# plt.title('District Level Scenario Comparison for MFSP',fontsize=18,fontweight="bold")
# plt.xticks(fontsize=18, rotation=0)
# plt.yticks(fontsize=18, rotation=0)
  
# # plt.legend()
# # plt.show()
# plt.savefig('District Level Scenario Comparison for MFSP.png',dpi=150, bbox_inches='tight')
# plt.clf()


# ###### GHG ###### 
# df_district = pd.read_excel('District_Borg_GHG.xlsx',header=0, engine='openpyxl')
# district_column = np.zeros((len(df_district),1))
# district_column ='District'
# df_district.insert(loc=0,column='Level',value=district_column)
# fig,ax = plt.subplots(figsize =(12,8))
# sns.barplot(ax=ax,data=df_district, x="Billion", y="min_GHG_emission", hue="Version",palette={'100k_0.001':'#448aff',
#                                                                                     '1M_0.1':'#1565c0',
#                                                                                     '1M_0.001':'#8bc34a',
#                                                                                     '10M_0.001':'#ffc107',
#                                                                                     'LP':'#f44336'},edgecolor ='black')
# # sns.barplot(ax=ax,data=df_district, x="Billion", y="cost", hue="Version",palette=['blue','red','red','red','red'])
# # plt.show()

# # Adding Xticks
# plt.xlabel('Version (Billion Gallon Biofuel Production)', fontweight ='bold', fontsize = 18)
# plt.ylabel(r'GHG Intensity (g $CO_{2}$ / MJ)', fontweight ='bold', fontsize = 18)


# plt.title('District Level Scenario Comparison for GHG Intensity',fontsize=18,fontweight="bold")
# plt.xticks(fontsize=18, rotation=0)
# plt.yticks(fontsize=18, rotation=0)
  
# # plt.legend()
# # plt.show()
# plt.savefig('District Level Scenario Comparison for GHG Intensity.png',dpi=150, bbox_inches='tight')
# plt.clf()














