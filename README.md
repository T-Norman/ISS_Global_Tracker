# ISS_Global_Tracker
 This project overlays the GPS position of the ISS over a map of the globe
 (Does not account for altitude)
 
 Requires Cartopy, which can be installed from the miniconda python environment
 Requires Requests
 (conda install -c conda-forge cartopy)
 (pip install requests)
 
 All data is taken directly from NASA's public API.
 Data is pulled every 5 seconds and auto-updates the ISS position on the map
