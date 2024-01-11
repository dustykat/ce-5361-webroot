#!/usr/bin/env python
# coding: utf-8

# # 10. Data Analysis

# :::{admonition} Course Website
# [link to webster](http://54.243.252.9/)
# :::
# 
# 

# ## Readings

# ## Videos

# ## Outline
# 
# :::{note}
# Much of this lesson is adapted from a draft version of *FHWA HIF-22-NNN Highway Hydrology: Third Edition* authored by Roger Kilgore, A. Tamim Atayee, George “Rudy” Herrmann, and David B. Thompson.
# :::
# 
# 

# ## Purpose
# 
# A fundamental step in hydrologic study, is the identification of the data that will be needed. Data needs depend on whether the study is preliminary or detailed, the study’s scope and nature, the study’s degree of complexity, the source of study funding. Once engineering hydrologists determine the study purpose, they can usually select a method of analysis for which the type and amount of data can be readily determined.
# 
# engineering hydrologists likely need such data as details of the watershed topography, land use and cover, precipitation information for past storm events, and information on annual peak or partial-duration flood series, or other streamflow records. engineering hydrologists also sometimes use historical data on floods that occurred prior to the systematic streamflow record.
# 
# The availability of data online on websites and in government agency databases has reduced the effort involved in data collection and compilation, while enhancing project understanding. Data typically available in such online data repositories can include both current and historical data, maps, and imagery. Often, using a well-thought-out internet data search engineering hydrologists can find existing information that meets the needs of a project and reduces the project-specific data collection effort and cost. By acquainting the designer with the data sources available and the procedures involved in accessing the various data sources, subsequent data searches could often be significantly reduced.

# ## Collection and Compilation of Data
# 
# engineering hydrologists obtain most of the data and information for the design of highway stream crossings and other hydrologic analyses from some desktop evaluations using existing sources of information and field evaluations to collect site-specific information not otherwise available. engineering hydrologists use certain types of data so frequently that some State DOTs have compiled these data into a single document or location to facilitate access. Having data available in a single source supports retrieval of needed data and helps standardize the hydrologic analysis of highway drainage design.
# 
# Several data sources useful for hydrologic analysis and modeling are listed in the following subsections. Many databases are compiled and managed by agencies of the Federal Government. In addition, many States and localities maintain websites that include similar or identical data to that from the Federal sites. Some include additional State or local data, such as high-resolution urban aerial imagery, high-resolution LiDAR (Light Detection and Ranging) elevation data, or LiDAR-based digital elevation models (DEMs).

# #### Streamflow and Flood Data
# 
# The U.S. Geological Survey (USGS) collects and documents streamflow data and is the major source of this information. Their database holds mean daily-discharge data for tens of thousands of locations. USGS compiles and publishes these data in both print publications and on the USGS website. The database contains a peak flow data retrieval capability that provides pertinent characteristics of the station and drainage area and a listing of both peak annual and secondary floods by water year (October through September).
# The U.S. Army Corps of engineering hydrologists (USACE), the U.S. Bureau of Reclamation (USBR), and the International Boundary and Water Commission also collect streamflow data. Along with the USGS, these agencies account for about 90 percent of the streamflow data available in the United States. Other sources of this data are local governments, utility companies, water-intensive industries, and academic or research institutions.
# Historical records or accounts are another source of flood data. Floods are noteworthy events and, very often, after a flood occurs, specific information such as high water elevations are recorded. Other sources of such information include newspapers, magazines, State historical societies or universities, and publications by any of several Federal agencies. Previous storms or flood events of historic proportion have been very thoroughly documented by the USGS, the USACE, and the National Weather Service (NWS). USGS reports documenting historic floods are summarized by Thomas (1987).

# #### Precipitation Data
# The major source of precipitation data is the NWS which is part of the National Oceanic and Atmospheric Administration (NOAA). Precipitation and other measurements are taken at approximately 20,000 locations each day. The measurements are fed through the Weather Service Forecast Offices (WSFOs), which serve each of the 50 States and Puerto Rico. Each WSFO uses these data and information obtained via satellite and other means to forecast the weather for its area of responsibility. In addition to the WSFOs, the NWS maintains a network of River Forecast Centers that prepare river and flood forecasts for about 2,500 communities. The data collected by the NWS and other organizations within NOAA are sent to the National Climatic Data Center (NCDC), which is responsible for collecting, processing, and disseminating environmental data. Online data sources include, but are not limited to:
# 1. NOAA Atlas 14. Precipitation depth-duration-frequency (DDF) information.
# 2. NCDC. Historical climatic data.

# #### Land Use/Land Cover and Soils Data
# Land use data are available in different forms such as topographic maps, aerial photographs such as those available from the National Agricultural Imagery Program (NAIP), zoning maps, and Landsat images. These different forms of data are available, usually online, from many different sources such as State, regional, or municipal planning organizations, the USGS, and the Natural Resource Economic Division, Water Branch, of the Department of Agriculture.
# The Multi-Resolution Land Characteristics (MRLC) consortium developed and maintains the National Land Cover Database (NLCD), which is a collection of datasets of land cover types. The MRLC is a group of Federal agencies who coordinate and generate consistent and relevant land cover information at the national scale for a wide variety of environmental, land management, and modeling applications.
# Specific online soils datasets from the Natural Resource Conservation Service (NRCS) include:
# 1. Web Soil Survey. Web service offering detailed soil map data from the Soil Survey Geographic Database (SSURGO).
# 2. gSSURGO. A toolbox for ArcGIS that facilitates the detailed geographic information systems (GIS) mapping of many soil properties (e.g., saturated hydraulic conductivity, hydrologic soil group, detailed textural description) on a State-by-State basis.
# 3. STATSGO: a general soil map of the United States, less detailed than SSURGO.

# #### Topographic, Stream Hydrography, and Watershed Boundaries
# The USGS National Geospatial Program provides a general geospatial data management program that includes data sources of interest to engineering hydrologists and hydrologists:
# 1. National Elevation Dataset (NED). A DEM raster representing the ground surface at a minimum resolution of 1 arc-second of latitude/longitude (approximately 30 meters) of the entire United States.
# 2. USGS 3D Elevation Program- Nationwide LiDAR high-resolution elevation data collection program/
# 3. US Topo: Maps for America. Current and historical digital topographic maps.
# 4. National Hydrography Dataset (NHD). A GIS database of streams and stream data.
# 5. Watershed Boundary Dataset. Delineated major and minor stream watersheds as GIS polygons.

# #### Aerial Images
# Aerial images provide information on historical and current land cover and land use. Sources include:
# 1. NAIP. Georeferenced high-resolution digital aerial imagery acquired periodically (currently on a three-year cycle) from the U.S. Department of Agriculture (USDA) Farm Service Agency.
# 2. Historical Aerial Imagery from the Aerial Photography Field Office. Aerial photos with some available back into the 1950s.
# 3. NOAA satellite imagery.
# 4. NASA Landsat Thematic Mapper. Satellite imagery beginning in 1972 to the present. Used for land use/land cover and other data through remote sensing analysis.

# #### Environmental Resources
# Hydrologic analysis objectives may include assessment of the impacts on environmental resources such as wetlands, habitat, and others. Online data sources include:
# 1. National Wetlands Inventory from the U.S. Fish and Wildlife Service (USFWS).
# 2. Critical Habitat for endangered species from the USFWS.
# 3. U.S. Environmental Protection Agency (USEPA) Environmental Dataset Gateway.

# #### Drainage Complaints and Maintenance Records
# Another potential source of information for hydrologic analysis are drainage complaints and maintenance records. These records provide observational information about flood experiences of citizens and landowners as well as records of maintenance types and frequencies. Drainage complaints result from real or perceived deficiencies of stormwater management and flooding that can provide designers with insight into the performance of existing facilities.
# 
# >State and local Departments of Transportation (DOTs) address drainage complaints in a timely and professional manner both to maintain collaborative relationships with stakeholder and to ensure that accurate information is recorded. Complaints may come in the form of a telephone call, email, letter, or personal visit. Drainage complaints lodged by members of the general public are often not well documented by the complainant and may not be well described. It is helpful to have instructions in place for ensuring that the complaint is directed to an appropriate office in a timely manner.
# >
# >If an investigation is warranted, a qualified engineering hydrologist experienced in hydrologic and hydraulic design, preferably from another office or area, investigates the complaint. Familiarity with the drainage laws of the State, agency policies, and local issues that may have a bearing on the case are vital. The investigator may contact the complainant and collect details of the complaint to clarify the situation. Designers conduct a site reconnaissance, when appropriate, to preserve any perishable data such as debris lines, flooded structures, or damage. In this case, the investigator bears in mind that the results of the investigation may become evidence in court. Other evidence, such as rainfall or streamflow data from a particular time, may be gathered to enhance the understanding of a particular incident.
# >
# >The investigator may review design plans, as-built plans, and maintenance records for comparison with the site characteristics, as well as adjacent land development and use information. Depending on the characteristics of the situation, the investigator documents findings in a memorandum or report.

# ### Site Reconnaissance and Field Data Collection
# 
# Every engineering hydrologisting problem is unique, and relying on rote application of standardized procedures, without due appreciation of the characteristics of the site, is risky at best. Field surveys or site investigations provide valuable information, even for the most preliminary analysis or simplest designs. Designers use site reconnaissance as a primary source of site data and to gain firsthand experience with the site. Under all circumstances, safety of both the investigating person and the public is of paramount importance; standard safety protocols for site investigations may be developed by an agency if needed.
# 
# Before the site visit, a desktop search of the data sources introduced in the previous section typically results in acquiring maps, imagery, elevation and topographic information, information on vegetative cover, potential biological issues including protected animals and plants. With such information, the engineering hydrologist plans the site visit with less likelihood of surprises on arriving at the site. During a site visit, the designer identifies, observes, and documents hydrology-related factors including:
# - Highwater marks.
# - Assessments of the performance of drainage structures.
# - Assessments of stream stability and scour potential.
# - Location and nature of important physical and cultural features that could affect or be affected by the proposed project.
# - Land use compared to that indicated on available maps and imagery.
# 
# :::{admonition} Follow-up Reconnaissance
# During the field visit, the engineering hydrologist may identify additional data collection to determine precise measurements for:
# • The location of stream cross-sections.
# • Fluvial geomorphic features.
# • Bankfull indicators. 
# • Debris lines.
# • Other features.
# Marking and photographing features for subsequent measurement reduces uncertainty about the engineering hydrologist’s intent for follow-up data collection.
# :::
# 
# The designer may anticipate the need for an engineering hydrologisting survey to collect additional information as described in the box. In many cases, topographic surveys are now performed by photogrammetric or laser scanning technology, rather than by traditional survey practices; the site reconnaissance is conducted for information other than topography.
# 
# Many digital cameras, including those on many “smart phones,” have the capability to geotag photographs with GPS-based location data, along with date, time, and direction of view encoded in the photograph metadata. Geotagged photographs are useful in documenting site features and may be included in GIS maps or web-based map and imagery applications.
# To maximize the usefulness of field site survey data, suggested procedures might include:
# - Planning the visit to identify data collection objectives and needed equipment.
# - Selecting an individual to conduct the drainage aspects of the field site survey with a good working knowledge of drainage design at a minimum.
# - Documenting data with written reports and photographs.
# - Using a systematic approach to maximize efficiency.
# - When possible, having those responsible for the design attend the site visit.
# Though the site visit is important, the engineering hydrologist will wish to augment it with additional information from other reliable sources through desktop analyses before and after the site visit.

# ## Data Evaluation and Documentation
# 
# After collecting data, the engineering hydrologist evaluates the data for use in hydrologic analysis and design and documents the analysis. GIS tools such as raster maps, DEMs, and vector feature classes are integral to both evaluation and documentation.

# ### Data Evaluation
# 
# After data collection, the designer compiles the data into a usable format, evaluating the data for consistency and for unexplained anomalies that might lead to erroneous calculations or results. The aim of this process is to fit the data into a comprehensive and accurate representation of the hydrology at a particular site. For example, most geotagging cameras and phones record coordinates in one datum system (World Geodetic System of 1984, WGS84), while State plane coordinate systems are often in another—the North American Datum of 1983 (NAD83). Translation from one to the other is not difficult within GIS systems, but it is important to first document the datum used for any given dataset before the translation can be done.
# 
# Experience, knowledge, and judgment are an important part of data evaluation. The designer ranks the data for reliability and precision and combines historical data with data obtained from measurements. The designer also justifies or, if possible, fills in any gaps in the data record. Some of the methods and techniques discussed later in this manual are useful for this purpose. Statistics can be useful in data analysis, but an underlying knowledge of hydrology is important for prudent and meaningful application of statistical methods. The engineering hydrologist should also review previous studies and reports for types and sources of data, how the data were used, and any indications of accuracy and reliability. Reviewing historical data helps determine whether significant changes have occurred in the watershed that might affect its hydrology and whether these data can be used to possibly improve or extend the period of record.
# 
# The engineering hydrologist also evaluates basic data, such as streamflow and precipitation, for hydrologic homogeneity and summarizes them before use. Maps, aerial photographs, Landsat images, and land use studies are compared with each other and with field survey results to resolve inconsistencies. For example, the construction of small reservoirs (such as those constructed by the NRCS) or agricultural terraces may have changed the runoff characteristics of a watershed. A change from cultivation to rangeland or clearing of brush may be identifiable as a change in hydrologic condition. Such changes may be attributable to a given time period, allowing the consideration of runoff data before and after the change. Beginning or cessation of irrigation may have exerted an effect on hydrologic condition. While much research has been devoted to the effects of urbanization, many changes other than urbanization may occur within a watershed that affect the runoff generation process. The results of this type of data evaluation provides a description of the hydrology of the site within the allotted time and the resources committed to this effort. The designer will want to adequately select the appropriate parameters to design the drainage structures to the indicated reliability.

# ### Data Documentation
# 
# If the data needs have been clearly identified, the designer can readily prepare and use results of the analysis in the selected method of hydrologic analysis. The data needs of each method differ, so no single method of presenting the data applies to all situations. The results of the data collection and data evaluation phases should be documented to:
# - Provide a record of the data itself.
# - Provide references to data that have not been incorporated into the record because of its volume or for other reasons.
# - Provide references for the methods of data analysis used.
# - Document assumptions, recommendations, and conclusions.
# - Present the results in a form compatible with the analytical method used.
# - Index the data and analysis for ease of retrieval.
# - Provide support of expenditures of public funds by highway agencies.
# The format or method used to document the collected data or subsequent analysis may be standardized, so that, those unfamiliar with a specific project may readily refer to the needed information. This standardization is especially important where there are several different entities performing hydrologic analyses and design. The engineering hydrologisting hydrologist should either include all data collected in the documentation or adequately reference them for quick retrieval.
# 
# The engineering hydrologist also presents data analyses in the documentation. If several different methods were used, the engineering hydrologist reports and documents each analysis, even if the results were not included in the final recommendations. Comments explaining why results were either discounted or accepted should also be included in the documentation. (See Section 4.3 for selecting hydrologic methods.) The engineering hydrologist references sources such as a State drainage manual, textbook, or other publication, for the selection of methods.
# 
# Also important is recording assumptions, conclusions, and recommendations made during or as a result of the data collection and analysis. Since hydrology is not an exact science, it is impossible to adequately collect and analyze hydrologic data without using judgment and making assumptions. By recording these professional judgments, the designer provides a detailed and valuable record of the work.

# ### GIS Analysis and Presentation
# 
# Geographic information systems provide powerful tools for analyzing data and presenting the results. The rapid adoption of GIS and Global Positioning Systems (GPS) into the fields of engineering and data management has significantly altered the way State and Federal agencies conduct operations. Because GIS tools store and evaluate georeferenced information, the data can be visualized and processed in hundreds of useful ways. Data presented in georeferenced points, lines, and polygons are used to understand and evaluate watersheds.
# 
# Most digital data sources are georeferenced, that is, the location is tied to the image or information so that multiple sources can be overlain for analysis and presentation. For example, Figure 4.1 shows topographic information overlain with a watershed boundary and stream hydrography. Figure 4.2 displays aerial photography and the roadway network at the same location. Similarly, Figure 4.3 and Figure 4.4 illustrate georeferenced soils and topographic data, respectfully, for the same location. These figures illustrate a few of the many types of information readily available in GIS format that the designer of roadway hydraulic structures may find valuable. Section 4.1.1 introduces these and other digital data sources.
# Some data sources, such as the USGS quadrangle maps, are in a raster (pixel) format. This format facilitates pixel-by-pixel computations within GIS. Others, such as the elevation contours and hydrologic soil group maps, are stored in “vector” format (points, lines, and polygons) and have attributes that allow calculation of areas, lengths, and other quantities.
# 
# [IMAGE OF A TOPOGRAPHIC MAP GOES HERE]
# 
# [AREAL IMAGE HERE]
# 
# [SOIL MAP IMAGE HERE]
# 
# Like GIS in some ways, computer aided design and drafting (CADD) programs accept georeferenced data, and some State transportation DOTs require that project plans be developed in established coordinate systems (for example, State plane systems) for later inclusion in statewide mapping efforts. 

# ## Selecting Hydrologic Methods
# 
# Engineering hydrologists choose from a variety of different types of hydrologic methods for a given project and location. They may choose multiple methods and compare results for additional insight. Considerations include:
# - Hydrologic information needed, e.g., peak flows versus hydrographs for flooding or flow estimates related to wetlands, endangered species, water quality, or other non-flood criteria.
# - Applicability of hydrologic methods and State/local guidance for choosing methods.
# - Risk factors, e.g., potential consequences of flooding, regulatory floodplains, and impacts to adjacent properties.
# - Watershed characteristics such as size and main channel slope.
# - Climate characteristics such as precipitation and temperature (snow) patterns.
# - Flooding history of the site.
# - Land use and land cover (existing and future).
# - Availability of stream gages at or near the project.
# - Influence of controls in the watershed such as dams or detention storage.
# 
# ### Available Methods
# This manual describes several methods applicable to a variety of situations. Table 4.1 summarizes a simplified overview of the methods discussed. Numerous Federal, State, and regional manuals document other methods that may apply nationally or are particular to States, regions, or specific conditions. The FHWA’s Highway Hydrology: Evolving Methods, Tools, and Data (FHWA 2022) describes additional approaches for the growing need for hydrologic approaches in less traditional applications.
# Table 4.1. Hydrologic method overview. DRAFTOCUMNT Unit Hydrographs (see Depends on unit Are an appropriate unit hydrograph Section 8.1) hydrograph source and design storm available?
# 
# When one or more stream gages is available on the stream or nearby, gaged flow analysis is likely the method of greatest utility. The utility of gage analysis is greatest when the gage series includes a sufficiently long record that can be considered “homogeneous,” i.e., when watershed conditions over the gage series life has not been dramatically altered by changes in land use, urbanization, regulation by dams, or diversion for other purposes. Many gages record flow information from rural watershed though some record the runoff behavior from urban watersheds. Chapter 5 discusses gaged flow analysis.
# 
# |Method|Drainage Area Limits|Selection Considerations|
# |----|----|----|
# Gaged Flow Analysis/ Peak Flow Transposition (see Chapter 5)|Gage near or adaptable to design location|Does gage information include sufficient homogeneous record length?|
# |Regression Equations (see Section 6.1)|Limited by the applicable equation|Are the watershed and meteorological characteristics consistent with equation limits?|
# |Index Flood Method (see Section 6.3)|Dependent on the underlying method|Is there an acceptable source for a flood frequency curve to estimate AEP flows beyond the index flood?|
# |Rational Method (see Section 6.2)|Generally, less than 200 acres|Is it reasonable to assume uniform rainfall for a duration equal to the time of concentration?|
# 
# Nearby gages on similar streams may be suitable for transposition to the project site, or for information transfer by the index flood method. Transposition of gage analysis is most applicable within the same stream or stream system, allowing the designer to make good use of information from gages that are not directly located at the site of interest. Transposition of gage analysis may provide valuable information as a validation technique for other methods, as opposed to being used as a primary method of estimation. Transposition allows the designer to select gages based on proximity and similarity to the site of interest, as compared to the more general analysis of regression equations. Transposition is not limited to one gage, but several nearby gages can be used for comparison. Section 5.4 discusses peak flow transposition.
#    
# The USGS publications documenting the development of regression equations contain one or more sections discussing the range of explanatory variable used in the development of the equations and limitations of the equations. In particular, the USGS states the recommended drainage areas for application for each set of equations. Regression equations represent a pooling of information from many watersheds and are often a convenient tool for peak flow estimation. Since regression equations are based on gaged records, they primarily apply to more rural watersheds, but some equations apply to urban situations. Section 6.1 discusses regression equations.
# 
# The index flood method is conceptually related to regression equations. It can be considered less direct than gage analysis, but like transposition, allows for selection of gages based on proximity and similarity to the site of interest. Section 6.3 presents the index flood method.
# 
# Watersheds of less than 200 acres may be best analyzed using the Rational Method. The Rational Method is straight forward and is extensively used in urban situations for the design of storm drains, channels, and small culverts, though designers can apply it to smaller rural watersheds. The Rational Method is usually restricted to contributing areas of 200 acres. However, there may be situations where the Rational Method can be applied to larger areas. Section 6.2 presents the Rational Method.
# The modeling of the rainfall-runoff process using unit hydrographs strives to mimic the physical rainfall process and describe how it runs off through the watershed. It is among the most flexible methods available. Rainfall-runoff modeling allows extrapolation beyond the range of watershed characteristics of gaged watersheds, can fill the gaps in the range of contributing area and can simulate the effects of constructed features such as dams and reservoirs, detention basins, and urbanization. The method can be used to project discharges for anticipated changes in conditions such as land use and land cover, post-fire conditions, and changing rainfall. Rainfall-runoff modeling applies to both rural and urban watersheds and applies to watershed drainage areas consistent with underlying assumptions of the particular method. Section 8.1 describes unit hydrographs.

# ### Validation and Comparison
# 
# In cases of watersheds with contributing area larger than what is appropriate for the Rational Method (greater than 200 acres), it is advisable for the designer to compare the results of two or more methods of analysis. Such a comparison provides the designer validation on the approximate magnitude of discharge for the identification of gross errors, and validation of the appropriate selection of methods. Methods that might be considered indirect, such as index flood or gage transposition, often provide considerable value as independent check procedures. Even in cases that demand a hydrograph, independent check of the peak flow against other methods is informative to the designer. Owing to the variety of conditions encountered in hydrology, and the large degree of uncertainty involved, validation of the design discharge is advisable.
# For design criteria involving small annual exceedance probability (less than 0.04), validation is of even greater importance. Uncertainty is largest for rare events, and the consequences of the uncertainty may also be greater.

# 

# In[ ]:




