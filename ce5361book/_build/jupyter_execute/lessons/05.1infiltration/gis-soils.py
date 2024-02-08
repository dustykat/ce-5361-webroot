#!/usr/bin/env python
# coding: utf-8

# # GIS Soils Properties
# 
# From the discussion regarding infiltration, it should be apparent that soil properties are important.  There 
# 

# ## Paper-Based Maps
# 
# Well just kidding, the old soils maps (of my generation) are archived at [USDA Soil Surveys](https://archive.org/details/usda-soil-surveys)
# 
# Our study watershed is in Briscoe Co. Texas
# 
# Here is the soils map [Briscoe Co. Tx Soils Maps (with text)](http://54.243.252.9/ce-5361-webroot/ce5361book/lessons/05.1infiltration/briscoeTX1977.pdf)
# 
# Our study location is Map sheet 51 in the document.
# 
# The main mapped soils are QBG,BeB, and BeC.  In the same document are tables that reference these codes back to soil descriptions.
# 
# From the tables we obtain various estimates as:
# 
# |Soil|$K_{sat}$(in/hr)|$\approx~n$ (from AWC value)|$\approx~D_{50}$ (from sieve data)(mm)|
# |---|---|---|---|
# |QBG|2.0-6.0|0.10-0.20|0.074|
# |BeB|0.6-2.0|0.14-0.17|0.42-0.074|
# |BeC|0.6-2.0|0.14-0.17|0.42-0.074|
# 
# As you will see in the in-class demonstration; the process to find these values is a bit slow - one can imagine the difficulties over larger areas, however it does provide meaningful values to parameterize one of the various infiltration models.  We still need some way to approximate soil suction (or mean pore size) we can certainly use a guess of $D_{50}$ we can estimate from the soils map as a surogate for pore size to estimate a suction value.
# 
# Now we recall from our Fluids class something like:
# 
# ![](CE5361-capillary.png)
# 
# So with some guess of the $D_{50}$ we can estimate the suction from a capillary rise approximation.  
# 
# $h_c = \frac{4 \sigma}{\gamma d}$

# In[1]:


surface_tension = 0.0728 # N/m
sp_weight = 9790 #N/cu.m.
diameter = 0.074e-3 #meters
capillary_rise = (4*surface_tension)/(sp_weight*diameter)
print("  Surface Tension ",round(surface_tension,3)," N/m")
print("  Specific Weight (of liquid) ",round(sp_weight,3)," N/cu.m.")
print("  Mean Pore Diameter ",round(1000*diameter,3)," mm\n ")
print("Capillary Rise ",round(capillary_rise,3)," m")


# This capillary rise is a useful surrogate for the suction pressure in the infiltration models.  For instance a Green-Ampt model for these soils would be something like:
# 
# $I(t)=K_{sat}t + (H+h_c)ln(1+\frac{I(t)}{(H+h_c)n})$
# 
# In our case $h_c\approx 15~in.$; $K_{sat} \approx 2.0~\frac{in.}{hr}$; and $n \approx 0.20$ or something to this effect.  So later on we can use this to estimate loss (and potential runoff).

# ## GIS Data
# 
# There is a soil survey geographic database at [USDA Soils Data Gateway](https://gdg.sc.egov.usda.gov/)
# 
# You can also access from WSS in the navigation column [USDA Web Soil Survey](https://websoilsurvey.nrcs.usda.gov/app/)

# In[ ]:




