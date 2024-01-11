#!/usr/bin/env python
# coding: utf-8

# # 8.1 Baseflow Separation
# 
# Baseflow separation is a first step in analysis – several methods
# 
# ### Constant discharge method
# 
# ![](constantdischarge.png)
# 
# - When rising limb starts – declare that value to constant rate during the event, rejoin as recession limb.
# - All flow above the value is declared storm flow
# 
# ### Constant slope method
# 
# ![](constantslope.png)
# 
# - When rising limb starts – draw a segment from that value to the inflection point on the recession limb
# - All flow above the value is
# declared storm flow
# - Hard to implement for multiple peak hydrographs (real hydrographs may exhibit many peaks)
# 
# ### Concave method
# 
# ![](concave.png)
# 
# - When rising limb starts – draw a segment from that value following the recession curve to a point beneath the peak flow.
# - Then draw a segment from the point above to the inflection point
# - All flow above the segments are declared storm flow
# - Hard to implement for multiple peak hydrographs (real hydrographs exhibit many peaks)
# 
# There are a few more ways to accomplish baseflow separation
# - The master-depletion curve method is outlined in the readings
# - For many practical cases with multiple peaked hydrographs the constant discharge method is probably the most straightforward to apply (or use continuous simulation techniques – outside scope this course)
# 
# 
# 

# 
# 
# ## Summary concepts
# 
# - Base-flow separation isolates the total discharge from the storm-induced discharge

# ## References
# 
# cite pages of textbook
# 
# 
# 2. [Cleveland, T. G. (2015) *Surface Water Hydrology Notes (Unit-Hydrographs Analysis) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture13.pdf)
# 
# 3. [Cleveland, T. G. (2017) *Surface Water Hydrology Notes (Unit-Hydrographs in HEC-HMS) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture14.pdf)
# 
# 4. [FHWA-NHI-02-001 Highway Hydrology Chapter 6, Section 6.1](http://54.243.252.9/ce-3354-webroot/3-Readings/FHWAHighwayHydrology/FHWA-NHI-02-001.pdf)
# 
# ## Spreadsheets
# 
# Listed below are spreadsheets that implement simple UH examples.  They are Excel (circa 2009) spreadsheets, that work in current Excel, LibreOffice, and Numbers environments
# 1. [ExampleUH_BackSub1.xls](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/ExampleUH_BackSub1.xls)
# 2. [ExampleUH_BackSub2.xls](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/ExampleUH_BackSub2.xls)
# 3. [ExampleUH_LeastSquares.xls](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/ExampleUH_LeastSquares.xls)
# 4. [ExampleUH_TransferFn.xls](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/ExampleUH_TransferFn.xls)
# 5. [ExtendedBase_DifferentStorm.xls](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/ExtendedBase_DifferentStorm.xls)
# 6. [ExtendedBase.xls](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/ExtendedBase.xls)
# 

# 

# 

# 

# 
