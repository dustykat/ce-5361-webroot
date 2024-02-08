#!/usr/bin/env python
# coding: utf-8

# # 5. Hydrologic Abstractions
# 
# :::{admonition} Course Website
# [ce-5361-webroot](http://54.243.252.9/ce-5361-webroot/)
# :::
# 
# Hydrologic abstractions refer to the various processes through which water is removed from the precipitation signal (or land surface) and eventually returning to the atmosphere compartment. The difference between input and abstraction, is the runoff.

# <hr>
# 
# ## Reading(s)
# 1. [Brutsaert,  W.  2005.  Hydrology  :   An  Introduction  (8th  printing),  Cambridge  University Press. NewYork. pp. 318-362 (Infiltration and Related Saturated Flows](http://54.243.252.9/ce-5361-webroot/3-Readings/00HydrologyAnIntroduction/1096-1.pdf)
# 3. [Polubarinova-Kochina, 1962. Theory of Groundwater Movement, (Translated from Russian by R. De Wiest), Princeton University Press, New Jersey.](http://54.243.252.9/ce-5361-webroot/3-Readings/Green-Ampt-PBK/Polubarinova-Kochina.pdf)
# 3. [Karki, A (2007) *Parameters for the Green-Ampt Loss-Rate Function for Select Texas Watersheds*. Master's Thesis, Department of Civil Engineering, College of Engineering, Texas Tech University](http://54.243.252.9/ce-5361-webroot/3-Readings/Green-Ampt-Texas/Karki_Amit_Thesis.pdf) 
# 
# 2. [Brutsaert,  W.  2005.  Hydrology  :   An  Introduction  (8th  printing),  Cambridge  University Press. NewYork. pp. 130-170 (Evaporation)](http://54.243.252.9/ce-5361-webroot/3-Readings/00HydrologyAnIntroduction/1096-1.pdf)
# 1. [Brutsaert,  W.  2005.  Hydrology  :   An  Introduction  (8th  printing),  Cambridge  University Press. NewYork. pp. 106-112 (Interception)](http://54.243.252.9/ce-5361-webroot/3-Readings/00HydrologyAnIntroduction/1096-1.pdf)
# 
# 1. [Cleveland, T. G. (2020) *Surface Water Hydrology Notes (Infiltration) to accompany CE-5361*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2020/lesson07/Lesson07.pdf)
# 2. [Green-Ampt Spreadsheet (Excel)](http://54.243.252.9/ce-3354-webroot/1-Lectures-2020/lesson07/ce5361_green_ampt.xlsx) Right-Click "Save As..."
# 
# 3. Chow, V. T., 1964. Handbook of Applied Hydrology. McGraw Hill, New York. Sec. 14., 2pp.
# 
# 4. Fang, X., Asquith, W.H., Garcia , C.A., Cleveland, T.G., Thompson, D.B., Malla, R. 2004 Literature Review on Time Parameters for Hydrographs. Project Report 4696-1. Texas Department of Transportation.
# 5. USDA National Engineering Handbook, Chapters 4,5, and 10.
# 6. Wurbs and James, 2002. Water Resources Engineering. Prentice-Hall, New Jersey. Pp 462-483.
# 8. [An Initial-Abstraction, Constant-Loss Model for Unit Hydrograph Modeling for Applicable Watersheds in Texas](http://54.243.252.9/ce-5361-webroot/3-Readings/USGS-Texas-IaCl/sir2007-5243.pdf)
# 
# <hr>
# 
# ## Videos
# 
# - [Introduction to Infiltration](https://www.youtube.com/watch?v=alEEY5rr2Kk)
# - [Horton's Infiltration Equation](https://www.youtube.com/watch?v=GMTWEqz-Osg)
# - [Phi-Index Infiltration Model](https://www.youtube.com/watch?v=AtYvETHm_og)
# - [Green-Ampt Infiltration Model](https://www.youtube.com/watch?v=IflajC5xz8o)
# - [Infiltration: Green-Ampt Model](https://www.youtube.com/watch?v=A-7huDPfKkU)
# - [Initial Abstraction Constant Rate Loss Model in HEC-HMS](https://www.youtube.com/watch?v=7AziPWlLCqU)
# - [Estimating Evaporation](https://www.youtube.com/watch?v=QVhid4qHw38)
# - [Evaporation (Aerodynamic Method)](https://www.youtube.com/watch?v=2rDt-fJvaNA)
# 
# 
# ## Outline
# 
# - Infiltration
# - Evapotranspiration
# - Interception

# Hydrologic abstractions refer to the various processes through which water is removed from the precipitation signal (or land surface) and eventually returning to the atmosphere compartment. These abstractions play a crucial role in the water cycle. 
# 
# - Loss to the soil column comprised of:
#   - Infiltration: The process by which water on the ground surface enters the soil. It is a key component of groundwater recharge.  
#   - Percolation: The downward movement of water through soil and rock layers beyond the root zone of plants. This contributes to the recharge of aquifers.
# 
# - Evapotranspiration comprised of:
#   - Evaporation: The process by which water changes from a liquid to a gas (water vapor) and enters the atmosphere. This occurs from open water surfaces, soil, and vegetation.
#   - Transpiration: The release of water vapor from plants into the atmosphere through small pores in their leaves, stems, and other parts. It is essentially the plant version of evaporation.
#   - Sublimation: The direct transition of water from a solid (ice or snow) to a gas without passing through the liquid phase. This can occur in cold climates with significant snow cover.
# 
# - Temporary storage on or near the surface comprised of:
#   - Interception: The capture of precipitation by vegetation before it reaches the ground. This water can later evaporate or be released to the ground surface.
#   - Surface Water Storage: The temporary storage of water in depressions, ponds, lakes, and other surface water bodies before it is evaporated, infiltrated, or discharged (to the runoff component).
# 
# The remainder in the water balance between precipitation (the input) and abstractions (the losses) is watershed runoff (the output).  It typically represents the flow of water over the land surface when the rate of precipitation exceeds the rate of abstraction. It includes surface water runoff and subsurface flow. 

# In[ ]:




