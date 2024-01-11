#!/usr/bin/env python
# coding: utf-8

# # <font color=darkblue>Exam 1 </font>
# 
# **LAST NAME, FIRST NAME**
# 
# **R00000000**
# 
# ___
# 
# ## Purpose : 
# Demonstrate ability to apply hydrologic and problem solving principles with respect to water balance, watershed delineation and measurements, and precipitation and streamflow.
# 

# ---
# 
# ### Problem 1 Water Budget Concepts
# 
# A river reach has an initial inflow of 350 cfs and an initial outflow of 285 cfs. The volume in storage is 10.8 acre-ft.  90 minutes later the inflow and outflow are 250 cfs and 200 cfs, respectively, and the volume in storage is 10.8 acre-ft. Determine:
# 
# 1. The change in storage over the 90 minute interval, and
# 2. The initial storage volume

# In[1]:


# solution here


# ---
# 
# ### Problem 2 Volume and Flow Concepts
# 
# 1. If water flows past an observation location at 1.0 cubic feet per second, for one hour, what incremental volume in cubic feet has passed the observation location?
# 2. If a basin has a surface area of 1 acre, and water is uniformily ponded at a depth of 1 foot, what is the total volume of water in cubic feet?
# 3. A reservoir with a constant surface area of 500 acres has an evaporation rate of 3.6 inches per day. The average outflow from the reservoir is 50 cubic feet per second, what is the change in water level in one day?

# In[2]:


# solution here


# ---
# 
# ### Problem 3. Watershed Metrics
# 
# Figure 1 is a topographic map of a small drainage basin. The drawn contour interval is
# 20 feet. Many of the contours are labeled. A culvert structure is located on the Eastern
# portion of the basin, near the outlet shown on Figure 3. 
# <figure align="center">
# <!--<img src="./topoMap.png" width="500" > -->
# <img src="http://54.243.252.9/ce-3354-webroot/4-Exams/EX1/topoMap.png" width="700" >
# <figcaption>Figure 1. Topographic Map of a portion of the Earth. Elevations and linear distances are in
# f eet. North (by convention) is up. </figcaption>
# </figure>
# 
# The red line is a highway alignment, beneath which the culvert structure is placed. Figure 2 is a photograph
# of the culvert system that is comprised of 4-parallel , 4-foot diameter, 100-foot long
# culverts. The lowest portion of the road near the culverts is at elevation 595 feet. The
# culverts are laid on a dimensionless slope of 0.02.
# <figure align="center">
# <!--<img src="./culvert-system.png" width="600" > -->
# <img src="http://54.243.252.9/ce-3354-webroot/4-Exams/EX1/culvert-system.png" width="600" >
# <figcaption>Figure 2. Multiple-barrel outlet structure </figcaption>
# </figure>
# 
# The watershed is delineated and the boundary is already drawn on the map.
# 
# The water surface area when the culvert system (like a dam, with 4 holes in the wall) impounds water to a water surface elevation of $565~feet$ is zero. (Zero pool area when the WSE is at 565 feet).  Figure 3 is a schematic sketch (elevation view) of a culvert barrel.
# 
# <figure align="center">
# <!-- <img src="./CulvertSystemElevation.png" width="600" > -->
# <img src="http://54.243.252.9/ce-3354-webroot/4-Exams/EX1/CulvertSystemElevation.png" width="700" >
# <figcaption>Figure 3. Culvert system elevation view sketch </figcaption>
# </figure>
#    
# - Estimate the basin drainage area that drains to the culvert structure.  Report the results in
#   1. Square feet,
#   2. Acres, and
#   3. Square miles
# - Complete the elevation (side) view sketch of the road embankment and culvert system by indicating the missing elevations on the sketch of (show computations for the outlet elevation)
#   1. The roadway crest in feet, 
#   2. The culvert outlet elevation in feet, and
#   3. The culvert barrel length in feet.
# - Estimate the water surface area (area of the pool on the upstream side of the road embankment) when the embankment impounds water to a water surface elevation of $590~feet$.  Show how you made the estimate.
# - Estimate the main channel length in feet. Show how you made the estimate.
# - Estimate the elevation at the most upstream portion of the main channel (where the main channel would intersect the watershed boundary), in feet.
# - Estimate the elevation of the outlet point of the watershed (the culvert invert elevations).
# - Using these two elevation values, estimate the average watershed slope along the main channel.   Express the result in
#    1. Dimensionless slope, and 
#    2. Percent slope.
# 

# In[3]:


# solution here


# ---
# 
# ### Problem 4. Rainfall and Runoff Data Reduction
# 
# A tabulation of an observed storm and associated runoff for the drainage area depicted by the map in Figure 1 is listed below.  The runoff was measured at the culvert system and indicated by the blue circle on the map.
# 
# |Time (hrs)|Accumulated Rain (inches)|Observed Discharge (cfs)|Incremental Volume (ft$^3$)|Cumulative Volume (ft$^3$)|
# |---:|---:|---:|---:|---:|
# | 0|0.000|0.00|||
# |1|0.000|0.00|||
# |2|0.000|0.00|||
# |3|0.000|0.00|||
# |4|0.000|0.00|||
# |5|0.000|0.00|||
# |6|0.000|0.00|||
# |7|0.000|0.00|||
# |8|0.101|1.40|||
# |9|0.106|0.31|||
# |10|0.111|0.31|||
# |11|0.115|0.31|||
# |12|0.120|0.31|||
# |13|0.120|0.40|||
# |14|0.150|0.40|||
# |15|0.750|24.66|||
# |16|2.750|588.23|||
# |17|2.940|808.70|||
# |18|3.030|154.28|||
# |19|3.030|94.68|||
# |20|3.030|27.56|||
# |21|3.090|36.13|||
# |22|3.210|19.65|||
# |23|3.300|7.00|||
# |24|3.300|0.00|||
# 
# 
# 
# Build a Jupyter Notebook (or use Excel) to:
# 
# 1. Complete the column labeled Incremental Volume (ft$^3$). 
# 2. Complete the column labeled Cumulative Volume (ft$^3$).
# 3. Determine the total **volume** of runoff in cubic feet from the storm (e.g. the Cumulative Volume at hour 24) 
# 4. Convert the runoff volume from cubic feet into watershed feet (i.e divide by the watershed area), then from watershed feet into watershed inches.  
# 5. Determine the fraction (percent) of rainfall that becomes runoff.
# 6. Plot the cumulative precipitation in inches and the cumulative runoff in watershed inches on the same plot.  Use the time for the x-axis, and the respective cumulative depths for the y-axis.  Plot precipitation in BLUE and runoff in RED.

# In[4]:


# solution here

