#!/usr/bin/env python
# coding: utf-8

# # HEC-HMS Introduction
# 
# This section covers
# 
# - Install HEC-HMS
#    - Verify Install when GUI loads
# - Build a minimal model
#    - Project Create
#      - Basin Model
#      - Meteorological Model
#      - Control Specifications
#    - Simulation Run Manager
#      - Run Simulation
# - Examine the output
# 
# A fully provisioned Windows Implementation of HEC-HMS is located at:
# 
# - server_name: **kittyinthewindow.ddns.net**
# - user_name: **texas-skew**
# - passwd: **peakfq73$hare**
# 
# Users must access using Remote Desktop Protocol (Built into Windows, Apple Store has a free Mac application).  The examples in the class will use this server.
# 
# ## HEC-HMS Project
# 
# The `project` is the structure to contain all the files related to some particular project.  Think of it as a model directory.
# 
# To create a new project simply select NEW from the file menu :
# 
# ![](hms-newproject.png)
# 
# and then select units (SI or Imperial) and name the project:
# 
# ![](hms-projectname.png)

# ### HEC-HMS Minimal Model
# 
# A minimal model consists of 
# 
# - Basin Model
# - Meteorological Model
# - Control Specifications
# 
# #### Basin Model Specification
# 
# For this example we will use the Hardin Creek basin which is about 17 square miles.  For the example we will neglect the reservoirs and model the whole thing as a singe watershed.
# 
# To create a basin model, select Components from the menu then Basin Manager 
# 
# ![](hms-basinmanager.png)
# 
# As with most HMS creator dialogs, you next name the basin.
# 
# ![](hms-basinname.png)
# 
# #### Meterological Model Specification
# 
# To create a meterological model, select Components from the menu then Meterological Model Manager 
# 
# ![](hms-metmodel.png)
# 
# As with most HMS creator dialogs, you next name the model.
# 
# ![](hms-metmodelname.png)
# 
# #### Control Model Specification
# 
# The last component is the control specification model (with dates and times for the simulation period).  To create a control model, select Components from the menu then Control Model Manager 
# 
# ![](hms-controlspecs.png)
# 
# Then next name the model.
# 
# ![](hms-controlspecsname.png)
# 
# #### Parameterizing the models
# 
# Now that the pieces are built, we need to supply watershed and rainfall characteristics to the components for a useable model.  First we will simulate the entire watershed as a single basin, with CN=98, and all other watershed-based model components disabled (i.e. None)
# 
# First build the single **basin**
# 
# ![](hms-subbasinselect.png)
# 
# Then supply the inputs, first area and the CN model.  Disable all the remaining methods (choose --None--)
# 
# ![](hms-nwebasins1.png)
# 
# Then the CN parameters (same as in class)
# 
# ![](hms-nwebasins2.png)
# 
# Then supply the **meterological** model inputs, for the example we will use an SCS design storm, in HMS its called "hypothetical" storm.
# 
# ![](hms-hypothetical1.png)
# 
# Then be sure the correct basins are attached to the precipitation input signal
# 
# ![](hms-hypothetical2.png)
# 
# Next select the storm itself and supply model inputs
# 
# ![](hms-hypothetical3.png)
# 
# Now select the **control** specifications and provide needed time values (must be calendar/clock time, HMS does not easily handle elapsed times - you can use fake dates as needed)
# 
# ![](hms-control1.png)
# 
# Now one can select simulation run builder
# 
# ![](hms-sim1.png)
# 
# ![](hms-sim2.png)
# 
# ![](hms-sim3.png)
# 
# ![](hms-sim4.png)
# 
# Once these are complete select Finish and the run manager is loaded, next select the particular run to active the compute engine
# 
# ![](hms-sim5.png)
# 
# At this point it should be ready, this is a good time to save the project, then reload the saved project from the file menu. Now attempt to run the simulation by selecting the exploding raindrop!
# 
# ![](hms-sim6.png)
# 
# With some luck it works like
# 
# ![](hms-sim7.png)
# 
# With a suseccful run we can examine various output features - to complete this notebook section we will just use a default chart of runoff from the watershed.  Select the Results/Element_Graph to get:
# 
# ![](hms-sim8.png)
# 
# There are tutorials and examples in the User Manual for the software.
# 
# 
# The first reference below is a pdf slide presentation of a training example for Ash Creek in Dallas Texas.

# ## References
# 1. [Cleveland, T. G. (2022) *Engineering Hydrology Notes to Accompany CE 3354 (Introduction to HEC-HMS)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson06/Lesson09ug.pdf)
# 
# 2. [HEC-HMS User Manual 3.5](http://54.243.252.9/ce-3354-webroot/3-Readings/HEC-HMS-Documentation/HEC-HMS_Users_Manual_3.5.pdf)
# 
# 3. [HEC-HMS Applications Guide](http://54.243.252.9/ce-3354-webroot/3-Readings/HEC-HMS-Documentation/HEC-HMS_Applications_Guide_March2008.pdf)
# 
# 4. [HEC_HMS Quick Start Guide 3.5](http://54.243.252.9/ce-3354-webroot/3-Readings/HEC-HMS-Documentation/HEC-HMS_QuickStart_Guide_3.5.pdf)
# 
# 5. [HEC-HMS Release Notes 3.5](http://54.243.252.9/ce-3354-webroot/3-Readings/HEC-HMS-Documentation/HEC-HMS_Release_Notes_3.5.pdf)
# 
# 6. [HEC-HMS Technical Reference Manual](http://54.243.252.9/ce-3354-webroot/3-Readings/HEC-HMS-Documentation/HEC-HMS_TechnicalReferenceManual_(CPD-74B).pdf)
# 
# 7. [NRCS TP-149 CN estimation](http://54.243.252.9/ce-3354-webroot/3-Readings/NRCS-CN-TP149/methodforestimat149kent.pdf)
# 
# 8. [Cleveland, T. G. (2022) *Engineering Hydrology Notes to Accompany CE 3354 (Introduction to HEC-HMS)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson06/Lesson09ug.pdf)
# 
# 9. [AshCreek Data (zip)](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson06.1/AshCreekData.zip)

# In[ ]:




