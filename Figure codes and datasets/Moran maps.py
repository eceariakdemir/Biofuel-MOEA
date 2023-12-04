# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 09:38:22 2023

@author: eari
"""


import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.io as pio
pio.renderers.default='browser'
from pysal.lib import weights
from pysal.explore import esda
# import seaborn as sns
# import contextily as ctx
# import contextily
from shapely.geometry import Point, Polygon
import matplotlib.colors as colors
# from matplotlib.cm import ScalarMappable
# from matplotlib.colors import TwoSlopeNorm
# from pysal.viz.splot.esda import moran_scatterplot, lisa_cluster, plot_local_autocorrelation
# from libpysal.weights import lat2W
# from esda.moran import Moran
# from random import randint
# import plotly.graph_objects as go
# import plotly.express as px
# import scipy.stats
# import seaborn
# from numpy.random import seed
# import matplotlib



plt.rcParams.update({'font.size': 15})

df = pd.read_csv('Platypus_codes/AgD_48g_cords_cb.csv',header=0)


crs = {'init':'epsg:4326'}
# crs = {"init": "epsg:2163"}
geometry = [Point(xy) for xy in zip(df['Longitude'],df['Latitude'])]
geo_df = gpd.GeoDataFrame(df,crs=crs,geometry=geometry)
geo_df = geo_df.to_crs(epsg=2163)

state_map = gpd.read_file('shapefiles/geo_export_9ef76f60-e019-451c-be6b-5a879a5e7c07.shp')
state_map = state_map.to_crs(epsg=2163)

district_map = gpd.read_file('shapefiles/AgD Corn belt.shp')
district_map = district_map.to_crs(epsg=2163)
districts = list(district_map['STASD_N'])

billion = ['3']
version = ['b 10M 0.01E']


df_geo_corn = pd.read_excel('Platypus_codes/combined_pivot_Corn.xlsx',header=0, engine='openpyxl')
del df_geo_corn['Unnamed: 0']



for b in billion:
    
    for v in version:

        fn_ha = 'NSGA_III decision variables ' + b + v +'.csv'
        df_decision_variables = pd.read_csv(fn_ha,header=0,index_col=0)
        
    
        fn = 'NSGA_III objective func ' + b + v + '.csv'
        df_O = pd.read_csv(fn,header=0,index_col=0)
        
        df_O.columns = ['cost','max_energy_shortfall','min_GHG_emission']
        
        num_c = len(df_geo_corn)

        fig,ax = plt.subplots()
        state_map.plot(ax=ax,color='gray',alpha=0.6,edgecolor='white',linewidth=0.5)
        district_map.plot(ax=ax,color='paleturquoise',alpha=1,edgecolor='black',linewidth=0.2)

        ax.set_box_aspect(1)
        ax.set_xlim(-750000,2000000)
        ax.set_ylim([-2000000,500000])
        plt.axis('off')
        # plt.savefig('districts.tiff',dpi=300)


        ######################### CORN/SOY ########################

        tc = df_decision_variables.iloc[:,0:num_c]
        t = tc.transpose(copy=False)
        to = t
        ind =  to.columns

        district_map.index = to.index
        map_c = pd.concat([district_map,to],axis=1)

        db = gpd.GeoDataFrame(map_c)
        db.info()

        Z1 = []

        for i in ind:
            # Generate W from the GeoDataFrame
            w = weights.KNN.from_dataframe(db, k=8)
            # Row-standardization
            w.transform = 'R'
            
            w.transform = 'R'
            moran = esda.moran.Moran(db[i], w)
            moran.I
            Z1.append(moran.I)

        Z2 = [x for x in Z1 if np.isnan(x) == False]
        print(Z2)
        Z3 = min(Z2)
        idx1c = Z2.index(Z3)

        Z4 = max(Z2)
        idx1c_c = Z2.index(Z4)


        ######################### GRASS_ML ########################

        tg = df_decision_variables.iloc[:,num_c:2*num_c]
        tg1 = tg.transpose(copy=False)
        indg =  tg1.columns

        district_map.index = tg1.index
        map_g = pd.concat([district_map,tg1],axis=1)

        dbg = gpd.GeoDataFrame(map_g)
        dbg.info()

        Z1_g = []

        for i in indg:
            # Generate W from the GeoDataFrame
            wg = weights.KNN.from_dataframe(dbg, k=8)
            # Row-standardization
            wg.transform = 'R'

            morang = esda.moran.Moran(dbg[i], wg)
            morang.I
            Z1_g.append(morang.I)

        Z2g = [x for x in Z1_g if np.isnan(x) == False]
        print(Z2g)
        Z3g = min(Z2g)
        idx1g = Z2g.index(Z3g)

        Z4g = max(Z2g)
        idx1g_c = Z2g.index(Z4g)
        
        ######################## ALGAE_ML #####################

        ta = df_decision_variables.iloc[:,2*num_c:3*num_c]
        ta1 = ta.transpose(copy=False)
        inda =  ta1.columns

        district_map.index = ta1.index
        map_a = pd.concat([district_map,ta1],axis=1)

        dba = gpd.GeoDataFrame(map_a)
        dba.info()

        Z1_a = []

        for i in inda:
            # Generate W from the GeoDataFrame
            wa = weights.KNN.from_dataframe(dba, k=8)
            # Row-standardization
            wa.transform = 'R'

            morana = esda.moran.Moran(dba[i], wa)
            morana.I
            Z1_a.append(morana.I)

        Z2a = [x for x in Z1_a if np.isnan(x) == False]
        print(Z2a)
        Z3a = min(Z2a)
        idx1a = Z2a.index(Z3a)

        Z4a = max(Z2a)
        idx1a_c = Z2a.index(Z4a)


        ######################### GRASS_AG ########################

        tg_ag = df_decision_variables.iloc[:,3*num_c:4*num_c]
        tg1_ag = tg_ag.transpose(copy=False)
        indg_ag =  tg1_ag.columns

        district_map.index = tg1_ag.index
        map_g_ag = pd.concat([district_map,tg1_ag],axis=1)

        dbg_ag = gpd.GeoDataFrame(map_g_ag)
        dbg_ag.info()

        Z1_g_ag = []

        for i in indg_ag:
            # Generate W from the GeoDataFrame
            wg_ag = weights.KNN.from_dataframe(dbg_ag, k=8)
            # Row-standardization
            wg_ag.transform = 'R'

            morang_ag = esda.moran.Moran(dbg_ag[i], wg_ag)
            morang_ag.I
            Z1_g_ag.append(morang_ag.I)

        Z2g_ag = [x for x in Z1_g_ag if np.isnan(x) == False]
        print(Z2g_ag)
        Z3g_ag = min(Z2g_ag)
        idx1g_ag = Z2g_ag.index(Z3g_ag)

        Z4g_ag = max(Z2g_ag)
        idx1g_ag_c = Z2g_ag.index(Z4g_ag)
        

        ######################## ALGAE_AG #####################

        ta_ag = df_decision_variables.iloc[:,4*num_c:]
        ta1_ag = ta_ag.transpose(copy=False)
        inda_ag =  ta1_ag.columns

        district_map.index = ta1_ag.index
        map_a_ag = pd.concat([district_map,ta1_ag],axis=1)

        dba_ag = gpd.GeoDataFrame(map_a_ag)
        dba_ag.info()

        Z1_a_ag = []

        for i in inda_ag:
            # Generate W from the GeoDataFrame
            wa_ag = weights.KNN.from_dataframe(dba_ag, k=8)
            # Row-standardization
            wa_ag.transform = 'R'

            morana_ag = esda.moran.Moran(dba_ag[i], wa_ag)
            morana_ag.I
            Z1_a_ag.append(morana_ag.I)

        Z2a_ag = [x for x in Z1_a_ag if np.isnan(x) == False]
        print(Z2a_ag)
        Z3a_ag = min(Z2a_ag)
        idx1a_ag = Z2a_ag.index(Z3a_ag)

        Z4a_ag = max(Z2a_ag)
        idx1a_ag_c = Z2a_ag.index(Z4a_ag)


        ######### COMBINED MORAN'S I #################

        com_c = to.reset_index(drop=True)
        com_g = tg1.reset_index(drop=True)
        com_a = ta1.reset_index(drop=True)
        com_g_ag = tg1_ag.reset_index(drop=True)
        com_a_ag = ta1_ag.reset_index(drop=True)


        comb = com_a.add(com_g)
        com_b = comb.reset_index(drop=True)
        com_f = com_c.add(com_b)
        com_f = com_f.reset_index(drop=True)
        com_ag = com_a_ag.add(com_g_ag)
        com_ag = com_ag.reset_index(drop=True)
        com = com_f.add(com_ag)

        ind_com =  com.columns

        district_map.index = com.index
        map_com = pd.concat([district_map,com],axis=1)

        db_com = gpd.GeoDataFrame(map_com)
        db_com.info()

        Z1_com = []

        for i in ind_com:
            # Generate W from the GeoDataFrame
            wcom = weights.KNN.from_dataframe(db_com, k=8)
            # Row-standardization
            wcom.transform = 'R'

            moran_com = esda.moran.Moran(db_com[i], wcom)
            moran_com.I
            Z1_com.append(moran_com.I)

        Z2_com = [x for x in Z1_com if np.isnan(x) == False]
        print(Z2_com)
        Z3_com = min(Z2_com)
        idx1_com = Z2_com.index(Z3_com)

        Z4_com = max(Z2_com)
        idx1_com_c = Z2_com.index(Z4_com)
        
        
        num_c = len(df_geo_corn)

        tc = df_decision_variables.iloc[:,0:num_c]    ## corn/soy
        tgml = df_decision_variables.iloc[:,num_c:2*num_c]  ## grass
        taml = df_decision_variables.iloc[:,2*num_c:3*num_c]  ## algae
        tgag = df_decision_variables.iloc[:,3*num_c:4*num_c]    ## grass on ag. land 
        taag = df_decision_variables.iloc[:,4*num_c:]     ## algae on ag. land
        
        ###################################
        ####   CORN/SOY Dispersed Solution  #####
        ###################################
        
        t = tc.transpose(copy=False)
        to = t  
        ind =  to.columns

        
        district_map.index = to.index
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
                
        # i = idx1c
        i = idx1_com
        
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
        
        f, axs = plt.subplots(2,5, figsize=(15, 7),constrained_layout = True)
        # f.suptitle( b + v, fontsize=16)
        
        state_map.plot(ax=axs[0,0],color='gray',alpha=0.6,edgecolor='black',linewidth=0.8)
      
        # normalize color
        vmin, vmax, vcenter = 0,300000, 1000
        norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
        
        # create a normalized colorbar
        cmap = 'cool'
        cbar = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
        
        db.plot(column= i, 
                cmap= 'cool', 
                # scheme='MaximumBreaks',
                k=20, 
                edgecolor='black', 
                linewidth=0.9, 
                alpha=0.9, 
                legend=False,
                # legend_kwds={"shrink": 0.75, "pad": 0.09},
                norm=norm,
                rasterized = True,
                ax=axs[0,0]
                )
        
        axs[0,0].set_axis_off()
        axs[0,0].set_box_aspect(1)
        axs[0,0].set_xlim(-750000,2000000)
        axs[0,0].set_ylim([-2000000,500000])
        plt.axis('off')
        
        
        ####################################
        #### CORN/SOY Clustered Solution ####
        ####################################
        
        t = tc.transpose(copy=False)
        to = t  
        ind =  to.columns

        
        district_map.index = to.index
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
            
        # i = idx1c_c
        i = idx1_com_c
        
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
        
        # f, ax = plt.subplots(1, figsize=(15, 7),constrained_layout = True)
        
        state_map.plot(ax=axs[1,0],color='gray',alpha=0.6,edgecolor='black',linewidth=0.8)
        
        # normalize color
        vmin, vmax, vcenter = 0,300000, 1000
        norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
        
        # create a normalized colorbar
        cmap = 'cool'
        cbar = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
        
        db.plot(column= i, 
                cmap= 'cool', 
                # scheme='MaximumBreaks',
                k=20, 
                edgecolor='black', 
                linewidth=0.9, 
                alpha=0.9, 
                legend=False,
                # legend_kwds={"shrink": 0.75, "pad": 0.09},
                norm=norm,
                rasterized = True,
                ax=axs[1,0]
                )
        
        axs[1,0].set_axis_off()
        axs[1,0].set_box_aspect(1)
        axs[1,0].set_xlim(-750000,2000000)
        axs[1,0].set_ylim([-2000000,500000])
        plt.axis('off')
        
        ##################################
        #### SWITCHGRASS Dispersed Solution ####
        ##################################
        
        t = tgml.transpose(copy=False)
        to = t  
        ind =  to.columns
 
        
        district_map.index = to.index
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()

        # i = idx1g
        i = idx1_com
        
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()

        state_map.plot(ax=axs[0,1],color='gray',alpha=0.6,edgecolor='black',linewidth=0.8)

        # normalize color
        vmin, vmax, vcenter = 0,300000, 1000
        norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
        
        # create a normalized colorbar
        cmap = 'cool'
        cbar = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
        
        db.plot(column= i, 
                cmap= 'cool', 
                # scheme='MaximumBreaks',
                k=20, 
                edgecolor='black', 
                linewidth=0.9, 
                alpha=0.9, 
                legend=False,
                # legend_kwds={"shrink": 0.75, "pad": 0.09},
                norm=norm,
                rasterized = True,
                ax=axs[0,1]
                )
        
        axs[0,1].set_axis_off()
        axs[0,1].set_box_aspect(1)
        axs[0,1].set_xlim(-750000,2000000)
        axs[0,1].set_ylim([-2000000,500000])
        plt.axis('off')
        
        
        
        #######################################
        #### SWITCHGRASS Clustered Solution ####
        #######################################
        
        t = tgml.transpose(copy=False)
        to = t  
        ind =  to.columns

        district_map.index = to.index
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
        
        # i = idx1g_c
        i = idx1_com_c
        
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
        
        
        state_map.plot(ax=axs[1,1],color='gray',alpha=0.6,edgecolor='black',linewidth=0.8)
        
        
        
        # normalize color
        vmin, vmax, vcenter = 0,300000, 1000
        norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
        
        # create a normalized colorbar
        cmap = 'cool'
        cbar = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
        
        db.plot(column= i, 
                cmap= 'cool', 
                # scheme='MaximumBreaks',
                k=20, 
                edgecolor='black', 
                linewidth=0.9, 
                alpha=0.9, 
                legend=False,
                # legend_kwds={"shrink": 0.75, "pad": 0.09},
                norm=norm,
                rasterized = True,
                ax=axs[1,1]
                )
        
        axs[1,1].set_axis_off()
        axs[1,1].set_box_aspect(1)
        axs[1,1].set_xlim(-750000,2000000)
        axs[1,1].set_ylim([-2000000,500000])
        plt.axis('off')
        
        #####################################################
        #### SWITCHGRASS AGRICULTURAL LAND Dispersed Solution #####
        #####################################################
        t = tgag.transpose(copy=False)
        to = t  
        ind =  to.columns

        
        district_map.index = to.index
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
        
        # i = idx1g_ag
        i = idx1_com
        
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
        
        state_map.plot(ax=axs[0,2],color='gray',alpha=0.6,edgecolor='black',linewidth=0.8)
       
        # normalize color
        vmin, vmax, vcenter = 0,300000, 1000
        norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
        
        # create a normalized colorbar
        cmap = 'cool'
        cbar = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
        
        db.plot(column= i, 
                cmap= 'cool', 
                # scheme='MaximumBreaks',
                k=20, 
                edgecolor='black', 
                linewidth=0.9, 
                alpha=0.9, 
                legend=False,
                # legend_kwds={"shrink": 0.75, "pad": 0.09},
                norm=norm,
                rasterized = True,
                ax=axs[0,2]
                )
        
        axs[0,2].set_axis_off()
        axs[0,2].set_box_aspect(1)
        axs[0,2].set_xlim(-750000,2000000)
        axs[0,2].set_ylim([-2000000,500000])
        plt.axis('off')
        
        ####################################################
        #### SWITCHGRASS AGRICULTURAL Clustered Solution ####
        ####################################################
        
        t = tgag.transpose(copy=False)
        to = t  
        ind =  to.columns

        
        district_map.index = to.index
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
        
        # i = idx1g_ag_c
        i = idx1_com_c
        
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
        
        state_map.plot(ax=axs[1,2],color='gray',alpha=0.6,edgecolor='black',linewidth=0.8)

        # normalize color
        vmin, vmax, vcenter = 0,300000, 1000
        norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
        
        # create a normalized colorbar
        cmap = 'cool'
        cbar = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
        
        db.plot(column= i, 
                cmap= 'cool', 
                # scheme='MaximumBreaks',
                k=20, 
                edgecolor='black', 
                linewidth=0.9, 
                alpha=0.9, 
                legend=False,
                # legend_kwds={"shrink": 0.75, "pad": 0.09},
                norm=norm,
                rasterized = True,
                ax=axs[1,2]
                )
        
        axs[1,2].set_axis_off()
        axs[1,2].set_box_aspect(1)
        axs[1,2].set_xlim(-750000,2000000)
        axs[1,2].set_ylim([-2000000,500000])
        plt.axis('off')
        
        
        ##################################
        #### ALGAE Dispersed Solution ####
        ##################################
        
        t = taml.transpose(copy=False)
        to = t  
        ind =  to.columns
     
        
        district_map.index = to.index
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
        
        # i = idx1a
        i = idx1_com
        
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()

        state_map.plot(ax=axs[0,3],color='gray',alpha=0.6,edgecolor='black',linewidth=0.8)

        # normalize color
        vmin, vmax, vcenter = 0,300000, 1000
        norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
        
        # create a normalized colorbar
        cmap = 'cool'
        cbar = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
        
        db.plot(column= i, 
                cmap= 'cool', 
                # scheme='MaximumBreaks',
                k=20, 
                edgecolor='black', 
                linewidth=0.9, 
                alpha=0.9, 
                legend=False,
                # legend_kwds={"shrink": 0.75, "pad": 0.09},
                norm=norm,
                rasterized = True,
                ax=axs[0,3]
                )
        
        axs[0,3].set_axis_off()
        axs[0,3].set_box_aspect(1)
        axs[0,3].set_xlim(-750000,2000000)
        axs[0,3].set_ylim([-2000000,500000])
        plt.axis('off')
        
        
        #######################################
        #### ALGAE Clustered Solution ####
        #######################################
        
        t = taml.transpose(copy=False)
        to = t  
        ind =  to.columns
    
        district_map.index = to.index
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
        
        # i = idx1a_c
        i = idx1_com_c
        
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
        
        state_map.plot(ax=axs[1,3],color='gray',alpha=0.6,edgecolor='black',linewidth=0.8)

        # normalize color
        vmin, vmax, vcenter = 0,300000, 1000
        norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
        
        # create a normalized colorbar
        cmap = 'cool'
        cbar = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
        
        db.plot(column= i, 
                cmap= 'cool', 
                # scheme='MaximumBreaks',
                k=20, 
                edgecolor='black', 
                linewidth=0.9, 
                alpha=0.9, 
                legend=False,
                # legend_kwds={"shrink": 0.75, "pad": 0.09},
                norm=norm,
                rasterized = True,
                ax=axs[1,3]
                )
        
        axs[1,3].set_axis_off()
        axs[1,3].set_box_aspect(1)
        axs[1,3].set_xlim(-750000,2000000)
        axs[1,3].set_ylim([-2000000,500000])
        plt.axis('off')
        
        #####################################################
        #### ALGAE AGRICULTURAL LAND Dispersed Solution #####
        #####################################################
        t = taag.transpose(copy=False)
        to = t  
        ind =  to.columns
        
        district_map.index = to.index
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
        
        # i = idx1a_ag
        i = idx1_com
        
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()

        state_map.plot(ax=axs[0,4],color='gray',alpha=0.6,edgecolor='black',linewidth=0.8)

        # normalize color
        vmin, vmax, vcenter = 0,300000, 1000
        norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
        
        # create a normalized colorbar
        cmap = 'cool'
        cbar = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
        
        db.plot(column= i, 
                cmap= 'cool', 
                # scheme='MaximumBreaks',
                k=20, 
                edgecolor='black', 
                linewidth=0.9, 
                alpha=0.9, 
                legend=False,
                # legend_kwds={"shrink": 0.75, "pad": 0.09},
                norm=norm,
                rasterized = True,
                ax=axs[0,4]
                )
        
        axs[0,4].set_axis_off()
        axs[0,4].set_box_aspect(1)
        axs[0,4].set_xlim(-750000,2000000)
        axs[0,4].set_ylim([-2000000,500000])
        plt.axis('off')
        
        ####################################################
        #### ALGAE AGRICULTURAL Clustered Solution ####
        ####################################################
        
        t = taag.transpose(copy=False)
        to = t  
        ind =  to.columns

        district_map.index = to.index
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()
        
        # i = idx1a_ag_c
        i = idx1_com_c
        
        map_c = pd.concat([district_map,to],axis=1)
        
        db = gpd.GeoDataFrame(map_c)
        db.info()

        state_map.plot(ax=axs[1,4],color='gray',alpha=0.6,edgecolor='black',linewidth=0.8)

        # normalize color
        vmin, vmax, vcenter = 0,300000, 1000
        norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
        
        # create a normalized colorbar
        cmap = 'cool'
        cbar = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
        
        db.plot(column= i, 
                cmap= 'cool', 
                # scheme='MaximumBreaks',
                k=20, 
                edgecolor='black', 
                linewidth=0.9, 
                alpha=0.9, 
                legend=True,
                legend_kwds={"shrink": 0.75, "pad": 0.09},
                norm=norm,
                rasterized = True,
                ax=axs[1,4]
                )
        
        axs[1,4].set_axis_off()
        axs[1,4].set_box_aspect(1)
        axs[1,4].set_xlim(-750000,2000000)
        axs[1,4].set_ylim([-2000000,500000])
        plt.axis('off')
        
        plt.savefig('Compressed_map' + b + v + '.png',dpi=150, bbox_inches='tight')














