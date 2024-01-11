#!/usr/bin/env python
# coding: utf-8

# # 1. Introduction

# :::{admonition} Course Website
# [link to ce-5361-webroot](http://54.243.252.9/ce-5361-webroot/)
# :::
# 
# This section displays the typical layout of the instructor notes.
# 
# :::{note}
# The chapters are arranged with a landing page that contains readings, videos, and the outline.  This landing page is followed by chapter specific content. Exercises (if any) are at the end of the notes. 
# :::
# 

# ## Readings
# 
# Hydrology and Hydrologic Systems
# 
# 1. [Chow, V.T., Maidment, D.R., Mays, L.W., 1988, Applied Hydrology:  New York, McGraw-Hill. **pp. 1-12** ](http://54.243.252.9/ce-5361-webroot/3-Readings/01CMM1988/Applied%20Hydrology%20VT%20Chow%201988.pdf) 
# 
# 2. [Brutsaert,  W.  2005.  Hydrology  :   An  Introduction  (8th  printing),  Cambridge  University Press. NewYork.](http://54.243.252.9/ce-5361-webroot/3-Readings/00HydrologyAnIntroduction/1096-1.pdf)
# 
# 3. [Kilgore, R.,Atayee, A. T., Curtis, D., Harris, J.,  Herrmann, G. R., Thompson D. B., 2023. Highway Hydrology:
# Evolving Methods, Tools, and Data. Publication No. FHWA-HIF-23-050. FHWA Hydraulic Engineering Circular No. 19 ](http://54.243.252.9/ce-5361-webroot/3-Readings/1HighwayHydrologyEmergingTools/highway-hydrology-hif23050.pdf)
# 
# 3. [Dooge, J.C.I. 1973. Linear Theory of Hydrologic Systems. ARS Technical Bulletin No. 1468.US Department of Agriculture, Washington, D.C. **pp. 1-40**](https://3.137.111.182/ce-3354-webbook/3-Readings/LS1973/linear-systems-hydrology-dooge.pdf) 
# 
# 4. [Richard H. McCuen, Peggy A. Johnson, Robert M. Ragan, 2002. Highway Hydrology; Hydraulic  Design  Series  Number  2,  Second  Edition.  Federal  Highway  Administration,  National Highway Institute, 4600 North Fairfax Drive, Suite 800, Arlington, Virginia 22203. **pp. 1-1 to 1-9**](https://3.137.111.182/ce-3354-webbook/3-Readings/FHWAHighwayHydrology/FHWA-NHI-02-001.pdf) 
# 
# ---
# 
# Hydrology "Definitions"
# 
# 5. [Excerpts from various sources](https://3.137.111.182/ce-3354-webbook/3-Readings/HydrologyDefinitions/hydrology-define.pdf)
# 
# 6. [Wisler, C.O, and Brater, E.F. 1949. "Hydrology" John Wiley and Sons, New York **pp. 1-14**](https://3.137.111.182/ce-3354-webbook/3-Readings/OlderHydrologyDescription/reading-definition-hydrology.pdf) 
# 
# ---
# 
# Water Budget
# 
# 7. [McCuen XXXX. Hydrologic Analysis and Design ... **pp. 2-12** ](https://3.137.111.182/ce-3354-webbook/3-Readings/McCuen-WaterBudget/mccuen-reading-water-budget.pdf)
# 
# --- 
# 
# Groundwater
# 
# 8. [Heath, R.C., 1983. Basic ground-waterhydrology: U.S. Geological Survey Water-SupplyPaper 2220, **pp. 1-5**](https://3.137.111.182/ce-3354-webbook/3-Readings/USGS-WSP2020-GroundwaterHydrology/usgs-wsp-2020.pdf) 
# 
# 9. [Viessman,W., Knapp, J.W., Lewis, G. L., and Harbaugh, T.E. 1977. "Groundwater Hydrology – Chapter 8" in *Introduction to Hydrology* 2ed. IEP Publishers, New York, **pp. 291-342**](https://3.137.111.182/ce-3354-webbook/3-Readings/Groundwater-Viessman/GroundwaterHydrology.pdf) 
# 
# 10. [Wisler, C.O, and Brater, E.F. 1949. "Hydrology" John Wiley and Sons, New York **pp. 198-272**](https://3.137.111.182/ce-3354-webbook/3-Readings/Groundwater-Wisler&Brater/Groundwater-Wisler.pdf) 
# 

# ## Videos

# ## Outline
# 
# 1. Course Resources
# 2. Review of Hydrology Concepts

# ## Course Resources
# - [Syllabus](http://54.243.252.9/ce-3354-webroot/0-Syllabus/)
# 
# - Software 
# 
# - Tour of Blackboard:
# 

# ---
# ## Introductory Hydrologic Concepts
# 
# ### What is hydrology?
# - Study of the occurrence, circulation, storage, and distribution of surface and groundwater on the Earth.
# - Engineering hydrology is the quantification of amounts of water at various locations (spatially) as a function of time (temporally) for surface water applications.
# 
# ### What is a watershed (catchment)?
# Here are a couple of definitions of watersheds.
# 
# - Topographic area that collects and discharges surface streamflow through one outlet or mouth (pour point)
# - The area on the surface of the Earth that drains to a specific location
# - In groundwater a similar concept is called a groundwater basin – only the boundaries can move depending on relative rates of recharge and discharge 
# 
# The topographic definition omits that there could be subsurface sewer systems that can cross topographic boundaries.   It’s a big deal in urban areas.
# 
# ### What is a hydrologic system?
# A hydrologic system is just a collection of parts that interact.   
#  
# - A hydrologic system is simply the collection of connected components that form the <strong>hydrologic cycle</strong>
# - These components can be grouped into subsystems, treated separately, and the results combined according to interactions between the subsystems (CMM pg 5) 
# 
# Like in fluid mechanics, the system has boundaries (the control volume) and fluxes into/out of the boundaries.   
# The entire planet is usually considered a closed system (hydrologically) and only the energy fluxes cross the boundary.   
# At more practical scales (parking lot) the mass fluxes matter a lot.  
# 
# ### What is the hydrologic cycle?
# Here is a typical diagram depicting the hydrologic cycle.  
# 
# ![](hydrologic_cycle.png)
# 
# The driving force for the cycle (not shown) is solar energy that provides the energy to vaporize liquid water that then rises into clouds, moves onshore, and rains (or snow, sleet, $\dots$.  and other forms of <strong>precipitation</strong>)
# A portion of the rain becomes runoff, another portion returns to the atmosphere as evaporation, another portion infiltrates into the ground and becomes groundwater.
# 
# The surface water system would be the part of the diagram that lies above the plane defined by the ocean and infiltration line.
# The subsurface system is the part that is below this plane.
# 
# Expressed as a simple system diagram it would be depicted in the figure below
# 
# ![](system_diagram.png)

# ---
# ## Hydrologic Balance 
# 
# ### Water Budget
# The water budget, or <strong>hydrologic balance</strong> is simply the expression of the conservation of mass in hydrologic terms for a hydrologic system.  
# Generally it is expressed as a rate (or volume) balance.
# The hydrologic equation is the fundamental tool in hydrology to describe amounts of water in storage in different compartments at different scales.  
# 
# The equation expressed in “words” is
# 
# Rate of inflow - Rate of outflow =  Rate of change of storage + Rate of internal mass generation.
# 
# Symbolically it is exrepssed as:
# 
# $$ \frac{dI}{dt} - \frac{dO}{dt} = \frac{dS}{dt} + \frac{dG}{dt}$$
# 
# where
# 
# $I$ is inflow volume, $O$ is outflow volume, $S$ is storage volume (i.e. within a watershed), and $G$ is generated volume.
# $G$ is generally zero, but is included to be consistent with the balance equations you have learned elsewhere (i.e. environmental engineering, chemistry, $\dots$)

# ### Surface Hydrologic System
# 
# Here is the surface water system broken into its own sub-system.
# 
# ![](surface_system_diagram.png)
# 
# Notice the dashed line is the boundary – exactly like a control volume in fluids.
# 
# ### Surface Water Budget
# 
# From the surface water system diagram, appropriate budget components are:
# 
# - Inflows:  Rainfall; Surface water from outside boundary, recharge from Groundwater.
# - Outflows: Evapotranspiration; Surface water leaving boundary; Infiltration to groundwater.
# - Storage:  Water levels in lakes, rivers, ponds within the boundary; water stored on leaves and other surfaces.

# ### Sub-surface Hydrologic System
# 
# Here is the sub-surface water system broken into its own sub-system.
# 
# ![](subsurface_system_diagram.png)
# 
# Notice the dashed line is the boundary – exactly like a control volume in fluids.
# 
# ### Sub-surface Water Budget
# 
# From the sub-surface water system diagram, appropriate budget components are:
# 
# - Inflows:  Groundwater flow from outside boundary; Recharge from surface system (via infiltration)
# - Outflows: Groundwater flow out of the boundary; Discharge (pumping; springs) to surface system
# - Storage:  Water levels in aquifers within the boundary

# ### Combined Hydrologic System
# Here are the two systems “combined.”
# Communication is by the two shaded paths on the figure. 
# 
# ![](combined_system_diagram.png)
# 
# Loss from the surface system becomes gain to the ground system.
# Loss from the ground system becomes gain to the surface system.
