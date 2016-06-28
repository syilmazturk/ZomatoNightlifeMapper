# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ZomatoNightlifeMapper
                                 A QGIS plugin
 The plugin generates nightlife popularity grid for the given area of interest using Zomato's Nightlife Index.
                             -------------------
        begin                : 2016-06-16
        copyright            : (C) 2016 by Serhat YILMAZTURK
        email                : serhat@yilmazturk.info
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ZomatoNightlifeMapper class from file ZomatoNightlifeMapper.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .zomato_mapper import ZomatoNightlifeMapper
    return ZomatoNightlifeMapper(iface)
