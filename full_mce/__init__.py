# -*- coding: utf-8 -*-
"""
/***************************************************************************
 full_mce
                                 A QGIS plugin
 Full Multicriteria evaluation tool for Public Health
                             -------------------
        begin                : 2016-07-28
        copyright            : (C) 2016 by Mampionona RASAMIMALALA, Institut Pasteur de Madagascar
        email                : rasamimalala@gmail.com
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
    """Load full_mce class from file full_mce.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .fullmce import full_mce
    return full_mce(iface)
