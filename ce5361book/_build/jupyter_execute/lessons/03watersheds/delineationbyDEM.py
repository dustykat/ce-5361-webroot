#!/usr/bin/env python
# coding: utf-8

# # Delineation (Homebrew DEM)
# 
# This method really refers to making your own DEM form a contour map then running python scripts to help identify the boundary.

# ## Example using Florida Training Watershed
# 
# Consider the image below, the point of interest is the blue dot.
# 
# ![](Florida-Training-Watershed.png)
# 
# To find the watershed boundary we can digitize the contours, then use a particle tracking algorithm to find points that drain to the blue dot (or close to the blue dot).
# 
# Digitize using [G3DATA](https://alternativeto.net/software/g3data/?platform=windows) or something similar to get XY coordinates of the level sets (contours)  Here is the graphic loaded into G3DATA.
# 
# ![](g3data-florida-training.png)
# 
# Next digitize some of the contours (should do all, but that takes too much time to illustrate).
# 
# Here is the manual digitize of the 160 contour line:
# 
# ![](g3data-florida-training-160.png)

# ### Collect the Data

# In[ ]:





# In[ ]:




