#!/usr/bin/env python
# coding: utf-8

# # Syllabus
# 
# ## Course Name:
# CE 5361 Surface Water Hydrology
# 
# ## Course Catalog Description: 
# 
# (3) Advanced study of hydrologic cycle: hydrologic abstractions, surface-runoff mechanics, hydrographs, baseflow seperation, data analysis, reservoir and channel routing, and an introduction to rainfall-runoff modeling
# 
# ## Prerequisites: 
# CE 3305 or equivalent

# <!-- ## COVID-19 Important Guidelines:
# * If Texas Tech University campus operations are required to change because of health concerns related to the COVID-19 pandemic, it is possible that this course will move to a fully online delivery format.  Should that be necessary, students will be advised of technical and/or equipment requirements, including remote proctoring software.  
# 
# * Policy on absences resulting from illness: We anticipate that some students may have extended absences.  To avoid students feeling compelled to attend in-person class periods when having symptoms or feeling unwell, a standard policy is provided that holds students harmless for illness-related absences (see Section A below).
# 
# 
# ### A. Illness-Based Absence Policy (Face-to-Face Classes)
# If at any time during the semester you are ill, in the interest of your own health and safety as well as the health and safety of your instructors and classmates, you are encouraged not to attend face-to-face class meetings or events.  Please review the steps outlined below that you should follow to ensure your absence for illness will be excused.  These steps also apply to not participating in synchronous online class meetings if you feel too ill to do so and missing specified assignment due dates in asynchronous online classes because of illness.
# 
# 1. If you are ill and think the symptoms might be COVID-19-related:
# 
#     1. Call Student Health Services at 806.743.2848 or your health care provider.  During after-hours and on weekends, contact TTU COVID-19 Helpline at TBD.
#     2. Self-report as soon as possible using the Dean of Students COVID-19 webpage. This website has specific directions about how to upload documentation from a medical provider and what will happen if your illness renders you unable to participate in classes for more than one week.
#     3. If your illness is determined to be COVID-19-related, all remaining documentation and communication will be handled through the Office of the Dean of Students, including notification of your instructors of the time you may be absent from and may return to classes.
#     4. If your illness is determined not to be COVID-19-related, please follow steps 2.a-d below.
# 
# 
# 2. If you are ill and can attribute your symptoms to something other than COVID-19:
# 
#     1. If your illness renders you unable to attend face-to-face classes, participate in synchronous online classes, or miss specified assignment due dates in asynchronous online classes, you are encouraged to contact either Student Health Services at 806.743.2848 or your health care provider.  Note that Student Health Services and your own and other health care providers may arrange virtual visits.
#     2. During the health provider visit, request a “return to school” note.
#     3. E-mail the instructor a picture of that note.
#     4. Return to class by the next class period after the date indicated on your note.
# 
# Following the steps outlined above helps to keep your instructors informed about your absences and ensures your absence or missing an assignment due date because of illness will be marked excused.  You will still be responsible to complete within a week of returning to class any assignments, quizzes, or exams you miss because of illness.
# 
# ### B. Illness-Based Absence Policy (Telepresence/On-Line Classes)
# Same as above with respect potential to infect others; go to a health care provider if you are ill.  Telepresence courses are recorded and will be available on TTU MediaSite and/or YouTube (unlisted).  Exercises, Quizzes, and Examinations are all administered by a Learning Management System (Blackboard) and students need to allow enough time to complete and upload their work.  Due date adjustments/late submits on case-by-case basis; documentation required as in subsection **A** above. -->

# ## Course Sections
# Lesson time, days, and location: 
# 
# 1. Section 002; CRN 73373; 1100-1220 T-Th ; EE 00118
# 
# ## Course Instructor:
# 
# Instructor: Theodore G. Cleveland, Ph.D., P.E., M. ASCE, F. EWRI
# 
# Email: theodore.cleveland@ttu.edu  (put CE 5361 in subject line for email related to this class)
# 
# Office location: CECE 203F; but prefer Telepresence (Zoom)
# 
# Office hours: TBD (meetings will be by Zoom call)
# 
# ## Teaching Assistant:
# 
# Teaching Assistant: none authorized 
# 
# Email : N/A
# 
# Office location: N/A
# 
# Office hours: N/A

# ## Textbook(s): 
# - [Hydrology: An Introduction: (Wilfried Brutsaert). ISBN 978-0521824798 ](http://54.243.252.9/ce-5361-webroot/3-Readings/0HydrologyAnIntroduction) The book shows on the TTU Blackboard, the link is to a copy from the Ethopian National Library, Amazon has electronic copies cheaper that TTU Blackboard
# 
# :::{note}
# The above book is on Blackboard because we are required to select at least one textbook
# :::
# 
# - [Chow, V.T., Maidment,D.M., and Mays, L.W. (1998) Applied Hydrology, McGraw Hill](http://54.243.252.9/ce-5361-webroot/3-Readings/CMM1988) The link is to an international copy from Taiwan.  Physical copies from Amazon would be cheapest if you wish one.
# 
# - [Additional Readings](http://54.243.252.9/ce-5361-webroot/3-Readings/) are stored on the class server.  Many are linked in the notes; If you browse, you will need to open the target files to see the topic.

# ## Course Objectives: 
# Theory and practical application of hydrologic concepts in a civil and environmental engineering context at multiple scales.

# ## Knowledge, Skills, Abilities (KSA) :
# During this course the student will
# 1.  Read, synthesize, and communicate ideas presented in current and historical technical literature.
# 2.  Delineate  watersheds  from  maps  and  determine  common  metrics  (area,  slope,  mainchannel length) using digital planimetry.
# 3.  Perform hydrologic computations using JupyterLab, Excel, LibreOffice and similar tools.
# 4.  Perform hydrologic simulation using HEC-HMS.    
# 5.  Perform integrated hydrology and hydraulics simulation of Green Infrastructure using EPA SWMM.

# ## ABET Student Outcomes
# * Engineering:
#     1. An ability to identify, formulate, and solve complex engineering problems by applying principles of engineering, science, and mathematics.
#     2. An ability to acquire and apply new knowledge as needed, using appropriate learning strategies. 
#  

# ## Resources/Tools
# 
# Computational tools equivalent to those used in ENGR 1330 are expected.  Professional software is used in the course; these are downloaded from the original sources (USGS and COE)
# 
# ### Hardware Requirements
# The college of engineering has specific laptop requirements for courses that are listed at https://www.depts.ttu.edu/coe/dean/engineeringitservices/buyingtherightcomputer.php
# 
# A minimal AWS Lightsail Instance (use Windows Server 2000 template; lowest resource provision tier; AWS RDP client, or download and install own RDP client) is sufficient to run the course software if you are incapable of installation onto your own laptop.
# 
# ### Learning Management System
# Blackboard(BB) is used as the learning management system (LMS) for this class and all exercises are to be uploaded to BB.  Late submissions are accepted, but scores are be reduced by at least 50%. 
# 
# <!--### Instructor Notes 
# The instructor notes are located at [http://54.243.252.9/ce-3354-webroot/ce3354book/_build/html/intro.html](http://54.243.252.9/ce-3354-webroot/ce3354book/_build/html/intro.html) -->

# ## Course Schedule ##

# |date|lesson|topic|reading|homework|quiz|
# |:---|:---|:---|:---|:---|:---|
# |11Jan24|[Introduction](http://54.243.252.9/ce-5361-webroot/) <br> - Course Resources  <br> - Introductory Concepts |- [What is Hydrology?](http://54.243.252.9/ce-3354-webroot/3-Readings/HydrologyDefinitions/hydrology-define.pdf)<br> - [Hydrology Definition](http://54.243.252.9/ce-3354-webroot/3-Readings/OlderHydrologyDescription/reading-definition-hydrology.pdf)<br> - [What is Hydrology(Mays)?](http://54.243.252.9/ce-3354-webroot/3-Readings/Mays%20%20TOC%20and%20Chapters%207,%208,%209/MaysCh7.pdf)||
# |16Jan24|[Hydrologic Cycle](http://54.243.252.9/ce-5361-webroot/) <br> - Hydrologic Cycle <br> - Water Budgets <br>  |- [Water Budget - Wanilista](http://54.243.252.9/ce-5361-webroot/3-Readings/Wanilista-WaterBudget/wanilista-reading-water-budget.pdf) <br> - [Water Budget - McCuen](http://54.243.252.9/ce-5361-webroot/3-Readings/McCuen-WaterBudget/mccuen-reading-water-budget.pdf) <br> -||
# |18Jan24|[Watersheds](http://54.243.252.9/ce-3354-webroot/ce3354book/_build/html/lessons/lesson03/lesson03.html) <br> - Watershed Delineation <br> - Watershed Metrics <br>  | - [Watersheds - McCuen](http://54.243.252.9/ce-3354-webroot/3-Readings/McCuen-Watersheds/McCuen-Watersheds.pdf)<br>- [How to Delineate a Watershed](http://54.243.252.9/ce-3354-webroot/3-Readings/NewHampshire-Watersheds/Topowatershed.pdf)<br>- [Numerical Planimetry](http://54.243.252.9/ce-3354-webroot/3-Readings/NumericalPlanimetry/)<br>- [How To Measure Path](http://54.243.252.9/ce-3354-webroot/3-Readings/HowToMeasurePath/HowToMeasurePath.pdf)<br> - [How to use Topographic Maps](http://54.243.252.9/ce-3354-webroot/3-Readings/UsingTopographicMaps/Pages%20from%20USAF-Survival-Manual-644.pdf)<br>- ||
# |23Jan24|[GIS and Hydrology](http://54.243.252.9/ce-3354-webroot/ce3354book/_build/html/lessons/lesson03/lesson03.html) <br> - GIS overview  <br> - ArcGIS, QGIS, others <br> - Primary uses in hydrology <br>  |- [Installing QGIS](dummy) <br> - [GIS Watershed Delineation](dummy) <br> - [GIS Watershed Metrics](dummy) ||
# |25Jan24|[Precipitation](http://54.243.252.9/ce-3354-webroot/ce3354book/_build/html/lessons/lesson04/lesson04.html) <br> - Point Precipitation <br>-  Areal Precipitation <br>- Probability Estimation Modeling <br> -  Design Storms | - [Probability Estimation Modeling - I](http://54.243.252.9/ce-3354-webroot/3-Readings/ProbabilityEstimationModeling/cive6361_week_006_A.pdf)<br> - [Probability Estimation Modeling - II](http://54.243.252.9/ce-3354-webroot/3-Readings/ProbabilityEstimationModeling/cive6361_week_006_B.pdf)<br>- [Design Rainfall](http://54.243.252.9/ce-3354-webroot/3-Readings/DesignRainfallEssay/DesignRainfall.pdf)<br>- [Rainfall Intensity for Design](http://54.243.252.9/ce-3354-webroot/3-Readings/TRB-2008-Paper/TRB_2008_IntensityDesign_Rev2.pdf)<br>- [Empirical Hyetographs](http://54.243.252.9/ce-3354-webroot/3-Readings/EmpiricalHyetographs/sir2004-5075.pdf)<br>- [DDF-Texas](http://54.243.252.9/ce-3354-webroot/3-Readings/USGS-Texas-DDF-Theory/wri98-4044.pdf) <br>- [Texas DDF Atlas](http://54.243.252.9/ce-3354-webroot/3-Readings/USGS-Texas-DDF-Atlas/sir2004-5041.pdf)||
# |30Jan24|[Hydrologic Abstractions](http://54.243.252.9/ce-3305-webroot/ce3305s24book/_build/html/lessons/05aflowkinematics/0kinematics.html) <br> - Flow Patterns and Visualization <br> - Velocity Field <br> - Eulerian and Lagrangian Description | pp. XXX-XXX <br> -  |[ES-XX](dummy)|Quiz X|
# |01Feb24|[Infiltration](http://54.243.252.9/ce-3354-webroot/ce3354book/_build/html/lessons/lesson08/lesson08.html) <br> - Horton (infiltration Excess) <br> - Dunne (saturation excess) <br> - Green-Ampt (soil physics) <br> - HEC-HMS Implementations|Gupta 93-110<br> - [Infiltration Notes](http://54.243.252.9/ce-3354-webroot/3-Readings/MyInfiltrationNotes/InfiltrationNotes.pdf)<br>- [Green-Ampt Notes](http://54.243.252.9/ce-3354-webroot/3-Readings/MyGreenAmptNotes/GA-Notes.pdf)<br>- [Infiltration PBK](http://54.243.252.9/ce-3354-webroot/3-Readings/Green-Ampt-PBK/Polubarinova-Kochina.pdf)<br>- [Green-Ampt in Texas](http://54.243.252.9/ce-3354-webroot/3-Readings/Green-Ampt-Texas/Karki_Amit_Thesis.pdf)||
# 06Feb24|[Evaporation](http://54.243.252.9/ce-3354-webroot/ce3354book/_build/html/lessons/lesson07/lesson07.html)  <br> - Blaney-Criddle <br> - Thornwaithe <br> - Turk <br> - HEC-HMS Implementation(s)|Gupta pp. 65-89|[ES6 Flood Frequency Analysis](http://54.243.252.9/ce-3354-webroot/2-Exercises/ES-6/es6.html)|
# |08Feb24|[Interception ](http://54.243.252.9/ce-3354-webroot/ce3354book/_build/html/lessons/lesson08.1/lesson081.html) <br> - Interception <br> - Canopy Storage <br> - Throughfall  <br> - Depression Storage|Gupta ppXX-XX|[ES7 Rainfall Data for Hardin Creek Project](http://54.243.252.9/ce-3354-webroot/2-Exercises/ES-7/es7.html)|
# |13Feb24|[Streamflow](http://54.243.252.9/ce-3354-webroot/ce3354book/_build/html/lessons/lesson05/lesson05.html) <br> - Streamflow Measurement <br> - Flood Frequency Analysis (B17C) <br> - Flow Duration Curves <br> - Regional Regression Equations |- [What is Runoff?](http://54.243.252.9/ce-3354-webroot/3-Readings/BetsonRunoff/Betson_JGR_V69_N8_1964.pdf) <br> - [Bulletin 17B (deprecated)]() <br> - [Bulletin 17C (current)](https://pubs.usgs.gov/tm/04/b05/tm4b5.pdf)<br> - [PeakFQ]()<br>- [Regional Regression Equations](http://54.243.252.9/ce-3354-webroot/3-Readings/RegressionEquationMethod/Pages%20from%20txdot-hdm-2014.pdf)|[ES4 Web Soil Survey Tool](http://54.243.252.9/ce-3354-webroot/2-Exercises/ES-4/es4.html)|
# |15Feb24|[Runoff Mechanisms](http://54.243.252.9/ce-3354-webroot/ce3354book/_build/html/lessons/lesson06/lesson06.html) <br> - Rainfall-Runoff Process <br>  - Rational Equation (A simplistic model) | - [Hydrologic Processes - Mays](http://54.243.252.9/ce-3354-webroot/3-Readings/Mays%20%20TOC%20and%20Chapters%207,%208,%209/MaysCh7.pdf)<br>- [Surface Runoff - Mays](http://54.243.252.9/ce-3354-webroot/3-Readings/Mays%20%20TOC%20and%20Chapters%207,%208,%209/MaysCh8.pdf)<br>- [Rational Method for Design](http://54.243.252.9/ce-3354-webroot/3-Readings/0-6070/0-6070.pdf)<br>- [Rate-Based C](http://54.243.252.9/ce-3354-webroot/3-Readings/RateBasedC/Rate-Based-C-Texas.pdf)<br>- [Volume-Based C](http://54.243.252.9/ce-3354-webroot/3-Readings/VolumetricCValues/Volumetric_C_Nirajan2012.pdf)<br>- [Return Period Adjusted C](http://54.243.252.9/ce-3354-webroot/3-Readings/ReturnPeriodAdjustmentC/C(T)_2013.pdf)<br>- [Time-Parameter Estimation for Texas](http://54.243.252.9/ce-3354-webroot/3-Readings/0-4696/0-4696.pdf)<br>- [Low-Slope Tc Experiments](http://54.243.252.9/ce-3354-webroot/3-Readings/LowSlopeTc/time-concentration-experiments.pdf)<br>- [Low-Slope Tc Estimation](http://54.243.252.9/ce-3354-webroot/3-Readings/LowSlopeTcEstimate/asce-jhe-low-slope.pdf) |[ES5 Rainfall/Runoff Data Preparation](http://54.243.252.9/ce-3354-webroot/2-Exercises/ES-5/es5.html)|
# |20Feb24|11|<font color="orange">Momentum <br> - Linear Momentum  <br> - sub2  <br> - sub3 <br> - sub4 <br> - sub5| pp. XXX-XXX <br> -  |[ES-XX](dummy)|Quiz X|
# |22Feb24|12|<font color="orange">Momentum <br> - Angular Momentum  <br> - sub2  <br> - sub3 <br> - sub4 <br> - sub5| pp. XXX-XXX <br> -  |[ES-XX](dummy)|Quiz X|
# |27Feb24|13|<font color="brown">Dimensional Analysis<br> - Dimensionless ($\pi$) groups  <br> - Correlations <br> - Important dimensionless numbers  <br> - Buckingham Pi Theory | pp. 410-427 <br> -  |[ES-XX](dummy)|Quiz X|
# |<font color="red">**29Feb24**||<font color="orange">[Exam 2](http://54.243.252.9/ce-3305-webroot/5-Exams/EX2/spring24/EX2.html) <br> - Mass <br> - Energy <br> - Momentum |||</font>|
# |05Mar24|14|<font color="brown"><font color="brown">Similitude <br> - Prototype/Model  <br> - Geometric Similarity <br> - Kinematic Similarity <br> - Dynamic Similarity | pp. 427-449 <br> -  |[ES-XX](dummmy)|Quiz X|
# |07Mar24|15|<font color="brown">Viscous Internal Flows <br> - Laminar Flow <br> - Parallel Plates <br> - Smooth Circular Conduit |pp. 450-462|[ES-12](http://54.243.252.9/ce-3305-webroot/2-Exercises/ES12/ES12.html)|Quiz X|
# |<font color="green">**09-17Mar**|<font color="green">Spring Break|||</font>|
# |05Mar24|16|<font color="brown">Viscous Internal Flows <br> - Turbulent Flow <br> - Reynolds Number <br> - Frictional Losses|pp. 462-473|[ES-XX](dummy)|Quiz X|
# |07Mar24|17|<font color="brown">Closed Conduit Analysis <br> - Moody Chart <br> - Pipeline loss <br> - Fitting loss <br> - Single Pipeline Flow|pp. 473-524 |[ES-XX](dummy)|Quiz X|
# |19Mar24|18|<font color="brown">Closed Conduit Analysis <br> - Pipe Systems <br> - Flow Measurement |pp. 524-551|[ES-XX](dummy)|Quiz X|
# |21Mar24|19|<font color="brown">Fluid machines <br> - Pumps  <br> - Turbines <br> - Fans <br> - Compressors |pp. xxxxx |[ES-XX](dummy)|Quiz X|
# |26Mar24|20|<font color="brown">[Pump Selection](https://192.168.1.93/ce-3305-webroot/ce3305s24book/_build/html/lessons/19PumpSelection/1fluidmachines.html#)  <br> - Performance curves  <br> - System curves  <br> - Suction head|pp. 524-551|[ES-XX](dummy)|Quiz X|
# |28Mar24|21|[Pump Selection](https://192.168.1.93/ce-3305-webroot/ce3305s24book/_build/html/lessons/19PumpSelection/1fluidmachines.html#pump-affinity-laws)  <br> - Turbomachine similarity| pp. XXX-XXX <br> -  |[ES-XX](dummy)|Quiz X|
# |02Apr24|22|<font color="magenta">Computational Hydraulics <br> - Junction heads <br> - Conduit loss <br> - Equation systems<br> - Pipe Network Analysis <br> - Newton-Raphson Method| pp. XXX-XXX <br> -  |[ES-XX](dummy)|Quiz X|
# |<font color="red">**04Apr24**||<font color="brown">[Exam 3](http://54.243.252.9/ce-3305-webroot/5-Exams/EX3/spring24/EX3.html) <br> - Dimensional Analysis <br> - Similitude <br> - Closed Conduits <br> - Pumps |||</font>|
# |09Apr24|23|<font color="magenta">Open Channels <br> - Flow Types <br> - Specific Energy| pp. XXX-XXX <br> - |[ES-XX](dummy)|Quiz X|
# |11Apr24|24|<font color="magenta">Open Channels <br> - Bump <br> - Sluice Gate | pp. XXX-XXX <br> -  |[ES-XX](dummy)|Quiz X|
# |16Apr24|25|<font color="magenta">Open Channels <br> - Gradually Varied Flow <br> - Water Surface Profile |pp. xxx-xxx|[ES-XX](dummy)|Quiz X|
# |18Apr24|26|<font color="magenta">Open Channels <br> - Rapidly Varied Flow <br> - Hydraulic Jump <br> - Weirs| pp. XXX-XXX <br> -  |[ES-XX](dummy)|Quiz X|
# |23Apr24|27|<font color="magenta">Computational Hydraulics <br> - GVF Backwater Curves <br> - GVF Frontwater Curves|[ES-XX](dummy)|Quiz X|
# |25Apr24|28|<font color="magenta">Boundary Layers <br> – Laminar <br> - Turbulent <br> - Flow over Flat Plate |pp. xxxx |[ES-XX](dummy)|Quiz X|
# |30Apr24|29|<font color="magenta">Drag and Lift <br> - Form Drag <br> - Flow around Cylinder|pp. 596-647|[ES-XX](dummy)|Quiz X|
# |<font color="red">**XXMay24**||<font color="magenta">[Exam 4](http://54.243.252.9/ce-3305-webroot/5-Exams/EX4/spring24/EX4.html) <br> - Open Channels <br> - Boundary Layers <br> - Computational Hydraulics (Pipes) <br> - Computational Hydraulics (Channels)  |||</font>|

# ---
# ## Course Assessment and Grading Criteria:
# There will be 20 homework assignments, four tests, and a final project report and presentation for this course.  
# <strong>Late</strong> assignments will be scored at 50% reduced value 
# 
# Grades will be based on the following components; weighting is approximate:
# 
# |Assessment Instrument|Weight(%)|
# |---|---:|
# |Attendance|10|
# |Test-1|10|
# |Test-2|10|
# |Test-3|10|
# |Test-4|10|
# |Homework|30|
# |Final Project Report|10|
# |Final Project Presentation|10|
# |Overall total|100|
# 
# Letter grades will be assigned using the following proportions:
# 
# |Normalized Score Range|Letter Grade|
# |:-|---:|
# |≥ 90|A| 
# |80-89|B|
# |70-79|C|
# |55-69|D|
# |< 55|F|
# 
# <!-- Scores as Quantiles Ranges
# |81-100|A| 
# |61-80|B|
# |41-60|C|
# |21-40|D|
# |0-20|F|
# -->
# 

# ## Classroom Policy:
# The following activities are not allowed in the classroom: Texting or talking on the cellphone or other electronic devices, and reading non-course related materials.
# ### Telepresence (On-line) Courses
# Obviously electronic devices are vital; disrupting the conference is prohibited, please mute your microphone unless you have a question - consider typing your question into the chat window as well. Be aware of bandwidth issues and remember most lessons and laboratory sessions are recorded and posted on youtube.  Recording, editing, and rendering takes awhile, so expect 24-36 hour delay before video is available. 

# ---
# ## ADA Statement: 
# Any student who, because of a disability, may require special arrangements in order to meet the course requirements should contact the instructor as soon as possible to make necessary arrangements.  Students must present appropriate verification from Student Disability Services during the instructor's office hours.  Please note that instructors are not allowed to provide classroom accommodation to a student until appropriate verification from Student Disability Services has been provided.  For additional information, please contact Student Disability Services 
# office in 335 West Hall or call 806.742.2405.
# 
# ## Academic Integrity Statement:
# Academic integrity is taking responsibility for one’s own class and/or course work, being individually accountable, and demonstrating intellectual honesty and ethical behavior.  Academic integrity is a personal choice to abide by the standards of intellectual honesty and responsibility.  Because education is a shared effort to achieve learning through the exchange of ideas, students, faculty, and staff have the collective responsibility to build mutual trust and respect.  Ethical behavior and independent thought are essential for the highest level of academic achievement, which then must be measured.  Academic achievement includes scholarship, teaching, and learning, all of which are shared endeavors.  Grades are a device used to quantify the successful accumulation of knowledge through learning.  Adhering to the standards of academic integrity ensures grades are earned honestly.  Academic integrity is the foundation upon which students, faculty, and staff build their educational and professional careers.  [Texas Tech University (“University”) Quality Enhancement Plan, Academic Integrity Task Force, 2010].
# 
# ## Religious Holy Day Statement: 
# “Religious holy day” means a holy day observed by a religion whose places of worship are exempt from property taxation under Texas Tax Code §11.20.  A student who intends to observe a religious holy day should make that intention known to the instructor prior to the absence.  A student who is absent from classes for the observance of a religious holy day shall be allowed to take an examination or complete an assignment scheduled for that day within a reasonable time after the absence.  A student who is excused may not be penalized for the absence; however, the instructor may respond appropriately if the student fails to complete the assignment satisfactorily.
# 
# ## Ethical Conduct Policy:
# Cheating is prohibited, and the representation of the work of another person as your own will be grounds for receiving a failing grade in the course.
# 
# **DISCRIMINATION, HARASSMENT, AND SEXUAL VIOLENCE STATEMENT:**
# Texas Tech University is committed to providing and strengthening an educational, working, and living environment where students, faculty, staff, and visitors are free from gender and/or sex discrimination of any kind. Sexual assault, discrimination, harassment, and other Title IX violations are not tolerated by the University. Report any incidents to the Office for Student Rights & Resolution, (806)-742-SAFE (7233) or file a report online at titleix.ttu.edu/students. Faculty and staff members at TTU are committed to connecting you to resources on campus. Some of these available resources are: TTU Student Counseling Center, 806- 742-3674, https://www.depts.ttu.edu/scc/(Provides confidential support on campus.) TTU 24-hour Crisis Helpline, 806-742-5555, (Assists students who are experiencing a mental health or interpersonal violence crisis. If you call the helpline, you will speak with a mental health counselor.) Voice of Hope Lubbock Rape Crisis Center, 806-763-7273, voiceofhopelubbock.org (24-hour hotline that provides support for survivors of sexual violence.) The Risk, Intervention, Safety and Education (RISE) Office, 806-742-2110,  https://www.depts.ttu.edu/rise/ (Provides a range of resources and support options focused on prevention education and student wellness.) Texas Tech Police Department, 806-742- 3931,http://www.depts.ttu.edu/ttpd/ (To report criminal activity that occurs on or near Texas Tech campus.)
# 
# **CIVILITY IN THE CLASSROOM STATEMENT:**
# Texas Tech University is a community of faculty, students, and staff that enjoys an expectation of cooperation, professionalism, and civility during the conduct of all forms of university business, including the conduct of student–student and student–faculty interactions in and out of the classroom. Further, the classroom is a setting in which an exchange of ideas and creative thinking should be encouraged and where intellectual growth and development are fostered. Students who disrupt this classroom mission by rude, sarcastic, threatening, abusive or obscene language and/or behavior will be subject to appropriate sanctions according to university policy. Likewise, faculty members are expected to maintain the highest standards of professionalism in all interactions with all constituents of the university.
# To ensure that you are fully engaged in class discussions and account team meetings during class time, you are expected to do the following:
# - Maintain the same level of civility and professionalism that would be expected in a face-to-face classroom setting.
# - Attend all classes regularly.
# - Log into the video conference on time and remain logged in for the duration of the class period.
# - Activate your camera so that you are visible to the instructor and other students in the class. If you have concerns about leaving your camera on (such as childcare obligations, privacy issues, or a particular circumstance during a class period), please talk to the instructor.
# - Refrain from engaging in non-class related activities during class time that create a distraction for other students in the class and/or limit your ability to engage in the course.
# Failure to meet these expectations may result in the following consequences:
# 1. Being counted as absent for the class meeting.
# 2. Not receiving credit for class participation for that class period.
# 3. Other consequences as stipulated in the syllabus, Texas Tech Code of Student Conduct, or other university policy.
# Repeated failure to meet expectations (e.g., attendance, participation in class, etc.), in addition to the above consequences, may result in the one or more of the following consequences:
# 1. Referral to the appropriate Associate Dean.
# 2. Academic penalty, ranging from a warning to failure of the course.
# (www.depts.ttu.edu/ethics/matadorchallenge/ethicalprinciples.php).
# 
# <!--**LGBTQIA SUPPORT STATEMENT:**
# I identify as an ally to the lesbian, gay, bisexual, transgender, queer, intersex, and asexual (LGBTQIA) community, and I am available to listen and support you in an affirming manner. I can assist in connecting you with resources on campus to address problems you may face pertaining to sexual orientation and/or gender identity that could interfere with your success at Texas Tech. Please note that additional resources are available through the Office of LGBTQIA within the Center for Campus Life, Student Union Building Room 201, www.lgbtqia.ttu.edu, 806.742.5433.”
# 
# Office of LGBTQIA, Student Union Building Room 201, www.lgbtqia.ttu.edu, 806.742.5433
# Within the Center for Campus Life, the Office serves the Texas Tech community through facilitation and leadership of programming and advocacy efforts. This work is aimed at strengthening the lesbian, gay, bisexual, transgender, queer, intersex, and asexual (LGBTQIA) community and sustaining an inclusive campus that welcomes people of all sexual orientations, gender identities, and gender expressions.-->
# 

# In[ ]:




