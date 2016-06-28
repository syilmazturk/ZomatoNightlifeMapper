# Zomato Nightlife Mapper
A QGIS Plugin that generates nightlife popularity grid using Zomato API for the given area of interest and saves the result as SHP format. In order to be able to use in QGIS environment, please add http://yilmazturk.info/qgis/plugins.xml repository URL and download it.

Introduction
------------
Zomato is a restaurant search and discovery service and currently operates in 23 countries - https://en.wikipedia.org/wiki/Zomato (visit time: June, 2016) It provides plenty of information related to restaurants such as scanned menus and photos sourced by local street teams, as well as user reviews and ratings.

Zomato Nightlife Mapper generates nightlife popularity grid for the given area of interest in specified point interval. For each point; it sends request, fetches JSON data via Zomato API, parses "nightlife_index" value (between 0 and 5 - 5 is the best), and assigns to point geometry as attribute.

Thus, this point grid can be specially visualized via symbology options and/or an interpolation map can be produced using this point grid. Both of them can be overlaid on a basemap like OpenStreetMap for a rich cartographic view.

Requirements
------------
This plugin needs a Zomato API key. Before using it, a Zomato API key should be demanded. Daily limit of API access is up to 1000 calls.

Installation
------------
* To download the plugin; go to Plugins > Manage and Install Plugins... > Settings and press "Add" button. Write a name whatever you want and enter the repository URL http://yilmazturk.info/qgis/plugins.xml

* Once successfully connected to repo; go to Plugins | All tab, search "Zomato Nightlife Mapper" and press Install plugin button. Please make sure to exist Zomato's red icon on the panel.

Usage
-----
* It's quite simple as you can see. Firstly, press "Define AOI" button and specify your area of interest on Google Map using adjustable and draggable rectangle frame.

* Enter your Zomato API key.

* Specify your point interval in degree unit. For instance, 0.01 degree is approx. 1000 meters. If degree value is increased too much, less accurate maps will be produced. However, degree value is decreased, too many point can be generated. It means your daily API limit will be run out quickly and plugin will be crashed.

* Press "Generate Grid" button. Plugin will calculate how many point will be produced and ask to continue. If pressed "Yes", a path should be selected to save result as ESRI Shapefile (SHP) format. After path selection, point grid will be generated on map canvas. It can take a while depend on your internet connection. "NLINDEX" field that includes nightlife index value can be checked on attribute table.

* If you want to generate an interpolation map, go to Raster > Analysis > Grid. Later, a basemap can be added via "OpenLayers plugin" if you wish. (separate installation)

Caveat
------
* This plugin is tested only in Windows systems and if your Windows' user name includes any blank or special character, it won't be worked.

* In addition to above, it's not tested for all countries which are operated by Zomato.


