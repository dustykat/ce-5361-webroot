#!/usr/bin/env python
# coding: utf-8

# # Evaporation Models
# 
# Review of evaporation processes and common models in 
# 
# [Cleveland, T. G. (2020) *Surface Water Hydrology Notes (Evaporation) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2020/lesson06/Lesson06.pdf)
# 
# ## HEC-HMS ET Models
# 
# A fully provisioned Windows Implementation of HEC-HMS is located at:
# 
# - server_name: **kittyinthewindow.ddns.net**
# - user_name: **texas-skew**
# - passwd: **peakfq73$hare**
# 
# Users must access using Remote Desktop Protocol (Built into Windows, Apple Store has a free Mac application).
# 
# Use the Hardin Creek Project to explore evaporation models.
# 
# Evapotranspiration is the second of the three components of a **meteorologic** model.
# It is the combination of evaporation from the ground surface and transpiration by
# vegetation. 
# > If a continuous simulation loss rate method is used and no
# evapotranspiration is specified in the meteorologic model, then zero
# evapotranspiration is used in the subbasins. However, evapotranspiration is often
# responsible for returning 50 or even 60\% of precipitation back to the atmosphere. In
# general there should be a selected evapotranspiration method for continuous
# simulation. In all cases, the meteorologic model is computing the potential
# evapotranspiration and subbasins will calculate actual evapotranspiration based on
# soil water limitations.
# 
# 

# Changes to Hardin Creek for ET exploration.
# 
# - Change loss method to deficit-constant
# - Choose ET method in Meterological Model Manager
# 
# Demonstrate effect

# ## References
# 
# 1. Gupta pp 65-92.
# 2. [Cleveland, T. G. (2020) *Surface Water Hydrology Notes (Evaporation) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2020/lesson06/Lesson06.pdf)
# 3. [Blaney-Criddle Spreadsheet (Excel)](http://54.243.252.9/ce-3354-webroot/1-Lectures-2020/lesson06/BlaneyCriddle.xlsx) Right-Click "Save As..."
# 4. [Thornwaithe Spreadsheet (Excel)](http://54.243.252.9/ce-3354-webroot/1-Lectures-2020/lesson06/Thornwaithe.xls) Right-Click "Save As..."

# In[ ]:




