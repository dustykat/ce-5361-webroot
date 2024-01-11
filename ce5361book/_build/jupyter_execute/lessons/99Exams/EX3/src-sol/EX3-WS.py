#!/usr/bin/env python
# coding: utf-8

# **Download** (right-click, save target as ...) this page as a Jupyterlab notebook from: [EX-1](http://54.243.252.9/ce-3354-webroot/4-Exams/EX3/EX3.ipynb)
# 
# ___

# # <font color=darkblue>CE 3354 Engineering Hydrology <br> Fall 2022 Exam 3 </font>
# 
# **LAST NAME, FIRST NAME**
# 
# **R00000000**
# 
# ___
# 
# ### Purpose : 
# Demonstrate ability to apply hydrologic and problem solving principles to simulate watershed response using HEC-HMS.
# 

# ---
# 
# ### Problem 1 - HEC-HMS Single Sub-Basin Simulation
# 
# Build a HEC HMS rainfall-runoff model for a single sub-basin watershed with the properties below. 
# 
# |Item|Value|Units|
# |:---|---:|---:|
# |Drainage Area |0.218 |Square Miles|
# |Composite CN |67|Dimensionless| 
# |Basin Lag |17.4|Minutes|
# |Rainfall Rate (Hour 0 – Hour 24)| 0.375|Inches per hour|
# |Rainfall Rate (Hour 25 – Hour 48)| 0.0|Inches per hour|
# 
# 
# Figure 1 below is a HEC-HMS model configuration that should give you an idea of what to build in HEC-HMS. 
# 
# ![](http://54.243.252.9/ce-3354-webroot/4-Exams/EX3/src-sol/figure1.png)
# 
# The HEC-HMS model should simulate a 48 hour period of interest. Use the output of your model to complete the table below:
# 
# **Solution**
# 
# Copy of model is located at
# 
# [http://54.243.252.9/ce-3354-webroot/4-Exams/EX3/src-sol/EX3HMS.zip](http://54.243.252.9/ce-3354-webroot/4-Exams/EX3/src-sol/EX3HMS.zip)
# 
# 
# |Item|Value|Units|
# |:---|---:|---:|
# |Peak Discharge Rate |44.5|Cubic Feet per Second|
# |Time of Peak Discharge|24 hrs|**Elapsed Hours** or Simulation Clock Time from HMS| 
# |Total Runoff|4.90|Watershed Inches|
# |Total Precipitation Depth|8.93|Inches|
# |Excess Precipitation Depth|4.90|Inches|

# # screen capture of your HEC-HMS solution here
# 
# ![](http://54.243.252.9/ce-3354-webroot/4-Exams/EX3/src-sol/HEC-HMS-Run.png)

# Sketch the output hydrograph from HEC-HMS for your subbasin below
# 
# ![](http://54.243.252.9/ce-3354-webroot/4-Exams/EX3/src-sol/Sketch1.png)
# 
# ---
# 
# ### Problem 2 HEC-HMS Single Sub-Basin to a Reservoir
# 
# Add a detention basin (reservoir) at the outlet of the small watershed that has the properties listed below.
# 
# |Storage (Acre-Feet)| Discharge (cfs)|
# |---:|---:|
# |0.0| 0.00| 
# |0.5| 1.50|
# |1.0| 2.25|
# |1.5| 2.75|
# |2.0| 3.26| 
# |2.5| 7.00| 
# |3.0| 18.00| 
# |3.5| 30.00| 
# |4.0| 90.00|
# 
# The HEC-HMS configuration should look similar to Figure 3 below:
# 
# ![](http://54.243.252.9/ce-3354-webroot/4-Exams/EX3/src-sol/figure3.png)
#  

# # screen capture of your HEC-HMS solution here
# 
# - Set up the storage discharge table <br> ![](http://54.243.252.9/ce-3354-webroot/4-Exams/EX3/src-sol/HEC-HMS-Detention.png)
# 
# - Run simulation capture output from detention pond <br> ![](http://54.243.252.9/ce-3354-webroot/4-Exams/EX3/src-sol/HEC-HMS-Detention-Plot.png)

# Sketch the output hydrograph from HEC-HMS from the detention pond (outflow from the pond after the sub-basin hydrograph is routed through the detention pond).
# 
# ![](http://54.243.252.9/ce-3354-webroot/4-Exams/EX3/src-sol/Sketch2.png)
# 
# 

# In[ ]:




