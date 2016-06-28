# Zomato Nightlife Mapper
A QGIS Plugin that generates nightlife popularity grid using Zomato API for the given area of interest and saves the result as SHP format. In order to be able to use in QGIS environment, please add http://yilmazturk.info/qgis/plugins.xml repository URL and download it.

Introduction
------------
Zomato is a restaurant search and discovery service and currently operates in 23 countries - https://en.wikipedia.org/wiki/Zomato (visit time: June, 2016) It provides plenty of information related to restaurants such as scanned menus and photos sourced by local street teams, as well as user reviews and ratings.

Zomato Nightlife Mapper generates nightlife popularity grid for the given area of interest in specified point interval. For each point; it sends request, fetches JSON data via Zomato API, parses "nightlife_index" value (between 0 and 5 - 5 is the best), and assigns to point geometry as attribute.

Thus, this point grid can be specially visualized via symbology options and/or an interpolation map can be produced using this point grid. Both of them can be overlaid on a basemap like OpenStreetMap for a rich cartographic view. 


