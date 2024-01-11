#!/usr/bin/env python
# coding: utf-8

# # Delineation (by Hand)
# 
# <hr><hr>
# 
# ## Readings 
# 1. [How to Delineate a Watershed](http://54.243.252.9/ce-3354-webroot/3-Readings/NewHampshire-Watersheds/Topowatershed.pdf)
# 2. [Cleveland, T. G. (2017) *Engineering Hydrology Notes (Hydrologic Data; Watershed Delineation) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture03.pdf)
# 
# <hr>

# ### Step 1.  Map of area of interest
# 
# Identify the pour point. 
# 
# ![](pourpoint.png)

# ### Step 2.  Superimpose a Grid
# 
# While not strictly necessary its helpful.  The grid serves two purposes, first a reference system and as a raster representation of the watershed (albeit at a coarse resolution) 
# 
# ![](gridoverlay.png)

# ### Step 3.  Cell Elevations
# 
# Use the grid to estimate average elevations in a grid cell, you use this information to help locate the boundary.  Water flows from high to low elevation.  Starting from the outlet work uphill until have high point, if its downhill as you cntinue in one direction beyond the point, its possibly the boundary (you are identifying "ridgeline" features).
# 
# Simultaneously identify internal water flow paths, these help identify the ridgeline features.
# 
# ![](estimatecellelev.png)

# ### Step 3.  Draw/Refine Boundary Estimates
# 
# Using the grid to estimate average elevations in a grid cell, you locate the coarse resolution boundary.  Water flows from high to low elevation.  Using the internal water flow paths, move upgradient along these paths to refine the boundary delineation.
# 
# ![](drawboundary.png)

# ### Step 4.  Tidy up Boundary
# 
# Tidy up your boundary and declare victory!
# 
# ![](completed-delineation.png)
