#!/usr/bin/env python
# coding: utf-8

# # Automated Data Retreival
# 
# The semi-automatic retrieval of data is valuable for documenting and reconstructing work related to hydrology.  What follows is scripting by a colleague that can be used for future efforts.
# 
# :::{note}
# I have modified his original work to render on my web server - main changes are to suppress interactive behavior, and to split the code up a bit.  Otherwise it is Moise's original Thesis work unchanged!
# :::

# ## A Hydrological Data Analysis and Visualization Toolkit
# 
# - *Author*: Moise Baraka, Ph.D. Student in CECE Water Resources, Texas Tech University
# - *Date*: 02/21/2024
# - *Supervised by* Theodore Cleveland, Ph.D. CECE Water Resources, Associate Professor, Texas Tech University
# - *class of* spring 2024 in Surface Water Hydrology
# 
# - Description:
# *This toolkit provides a collection of functions for retrieving, processing, analyzing, and visualizing hydrological data from the USGS web server. It includes modules for retrieving rating curve data, fitting it, computing statistical measures, generating histograms, and plotting various hydrological data attributes. The program allows users to input station codes to retrieve specific data and provides visualizations for any station monitored by the USGS program.*
# ---
# 
# ### STREAMFLOW DATA RETRIEVAL
# 
# - **Step 1: Input Collection**
# 
# The script prompts the user to input the USGS station ID, start date, and end date.
# 
# - **Step 2: Directory Selection**
# 
# The user is prompted to input the directory where the data will be saved. If no directory is provided, it defaults to a predefined directory, which must have been defined in the script.
# 
# - **Step 3: URL Construction**
# 
# The script constructs a URL using the provided station ID, start date, and end date. This URL is used to retrieve the data from the USGS website.
# 
# - **Step 4: Data Retrieval**
# 
# The script downloads the data from the constructed URL. During the download process, it displays a progress bar or percentage showing the download progress.
# 
# - **Step 5: Data Saving**
# 
# The downloaded data is saved to the specified directory with a filename indicating the station code and data type.

# :::{note}
# Here we load required modules
# :::

# In[1]:


import re
import urllib.request
import tqdm
import time
import os


# :::{note}
# Date parser function.  
# :::

# In[2]:


#------------------------------------------------------------------------
def get_date_input(prompt):
    while True:
        date_input = input(prompt)
        # Validate date format
        if re.match(r'^\d{4}-\d{2}-\d{2}$', date_input):
            return date_input
        else:
            print("Invalid date format. Please use yyyy-mm-dd format.")


# :::{note}
# Directory selector function
# :::

# In[3]:


#------------------------------------------------------------------------
def get_save_directory_input(default_directory):
    while True:
        save_directory = input(f"Enter the directory to save the data (press Enter to use default directory {default_directory}): ")
        if not save_directory:
            return default_directory
        # Validate directory exists
        elif os.path.isdir(save_directory):
            return save_directory
        else:
            print("Directory does not exist. Please enter a valid directory.")


# :::{note}
# Here we build the URL to generate the request to USGS server(s)
# :::

# In[4]:


#------------------------------------------------------------------------
def build_url1(station_code, start_date, end_date):
    base_url = 'https://nwis.waterdata.usgs.gov/nwis/dv?referred_module=sw&search_site_no='
    query_params = '&search_site_no_match_type=exact&site_tp_cd=OC&site_tp_cd=OC-CO&site_tp_cd=ES&site_tp_cd='                    'LK&site_tp_cd=ST&site_tp_cd=ST-CA&site_tp_cd=ST-DCH&site_tp_cd=ST-TS&index_pmcode_00060=1'                    '&group_key=NONE&sitefile_output_format=html_table&column_name=agency_cd&column_name=site_no'                    '&column_name=station_nm&range_selection=date_range&begin_date=' + start_date + '&end_date=' + end_date +                    '&format=rdb&date_format=YYYY-MM-DD&rdb_compression=value&list_of_search_criteria=search_site_no%2Csite_tp_cd%2Crealtime_parameter_selection'

    return base_url + station_code + query_params


# In[ ]:





# :::{note}
# Now the retreival step.  Some output is suppressed for JupyterBook
# :::

# In[5]:


#------------------------------------------------------------------------
# Retrieve and save data from a URL, and return the filename
def retrieve_and_save_data(url, filename):
    print("\nDownloading data from:", url , '\n')
    response = urllib.request.urlopen(url)
    total_size = int(response.headers.get('content-length', 0))
    downloaded = 0
    chunk_size = 1024
    start_time = time.time()  # Record start time
    with open(filename, 'wb') as file:
        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break
            file.write(chunk)
            downloaded += len(chunk)
            if total_size > 0:
                progress = downloaded / total_size * 100
            else:
                # Assume 1.2 seconds download time if total_size is zero
                elapsed_time = time.time() - start_time
                progress = min(100, elapsed_time / 1.2 * 100)
            print(f"Estimated downloading progress: {progress:.1f}%\r", end='')
    print("\nData saved to:", filename)
    return filename


# :::{note}
# Here is the batch request (deactivate for interactive)
# :::

# In[6]:


station_code = '07297910'
start_date = '1936-01-01'
end_date = '2024-02-01'
save_directory = './' # suppress and actiovate above for interactive


# :::{note}
# Here is the interactive part (activate for interactive)
# :::
#--------------------------------------------------------------------------
#                          Define the inputs
#--------------------------------------------------------------------------
print(" ------------------------------------------",
        "\n Please provide the following information:",
        "\n ------------------------------------------")


# activate code below and suppress above 3 lines for interactive
#station_code = input('- USGS station ID: ')
#start_date = get_date_input('- Start Date (yyyy-mm-dd): ')
#end_date = get_date_input('- End Date (yyyy-mm-dd): ')



#--------- !!! Define the directory where the data will be saved !!! -----------
default_directory = r"C:\Users\mbaraka\OneDrive - Texas Tech University\Thesis file"  # To be defined!

save_directory = get_save_directory_input(default_directory)
# :::{note}
# Here get the file from the remote
# :::

# In[7]:


#--------------------------------------------------------------------------
#        Define the base URLs for data retrieval from Website 1
#--------------------------------------------------------------------------
url1 = build_url1(station_code, start_date, end_date)

# Retrieve and save data from Website 1
filename1 = retrieve_and_save_data(url1, os.path.join(save_directory, f'USGS_Data_for_{station_code}.txt'))


# In[ ]:




