#!/usr/bin/env python
# coding: utf-8

# # 5.3 Interception/Depression Storage
# 
# Storage on the watershed is distributed among depression and canopy storage, and explicit storage in things large enough to be treated as reservoirs.  In this section we are considering just the first two components.

# Examination of various process models at
# 
# [Cleveland, T. G. (2020) *Surface Water Hydrology Notes (Depression and Canopy Storage) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson08.1/Lesson08ug.pdf)
# 
# ## HEC-HMS Storage Models
# 
# >A sub**basin** element conceptually represents infiltration, surface runoff, and
# subsurface processes interacting together, the actual infiltration calculations are
# performed by a loss method contained within the subbasin. A total of twelve different
# loss methods are provided. Some of the methods are designed primarily for
# simulating events while others are intended for continuous simulation. All of the
# methods conserve mass. That is, the sum of infiltration and precipitation left on the
# surface will always be equal to total incoming precipitation.
# 
# >The inputs for each loss method are presented on a separate Component Editor
# from the subbasin element editor. The "Loss" editor is always shown next to the
# "Subbasin" editor. If the kinematic wave transform method is selected, there may be
# two loss editors, one for each runoff plane. The information shown on the loss editor
# will depend on which method is currently selected
# 
# A fully provisioned Windows Implementation of HEC-HMS is located at:
# 
# - server_name: **kittyinthewindow.ddns.net**
# - user_name: **texas-skew**
# - passwd: **peakfq73$hare**
# 
# Users must access using Remote Desktop Protocol (Built into Windows, Apple Store has a free Mac application).
# 
# - Use the Hardin Creek Project to explore different loss models.
# 
# Recomended Loss models for semester project are CN model or Green-Ampt.  These are easiest to parameterize from available data sources for the project and should be adequate for the problem statement.

# 

# 

# ## References
# 
# 1. [Cleveland, T. G. (2020) *Surface Water Hydrology Notes (Infiltration) to accompany CE-5361*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2020/lesson07/Lesson07.pdf)
# 2. [Green-Ampt Spreadsheet (Excel)](http://54.243.252.9/ce-3354-webroot/1-Lectures-2020/lesson07/ce5361_green_ampt.xlsx) Right-Click "Save As..."
# 3. Chow, V. T., 1964. Handbook of Applied Hydrology. McGraw Hill, New York. Sec. 14., 2pp.
# 4. Fang, X., Asquith, W.H., Garcia , C.A., Cleveland, T.G., Thompson, D.B., Malla, R. 2004 Literature Review on Time Parameters for Hydrographs. Project Report 4696-1. Texas Department of Transportation.
# 5. USDA National Engineering Handbook, Chapters 4,5, and 10.
# 6. Wurbs and James, 2002. Water Resources Engineering. Prentice-Hall, New Jersey. Pp 462-483.
# 7. Polubarinova-Kochina, 1962. Theory of Groundwater Movement, (Translated from Russian by R. De Wiest), Princeton University Press, New Jersey.
# 8. [An Initial-Abstraction, Constant-Loss Model for Unit Hydrograph Modeling for Applicable Watersheds in Texas](http://54.243.252.9/ce-3354-webroot/3-Readings/USGS-Texas-IaCl/sir2007-5243.pdf)

# In[ ]:




