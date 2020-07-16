#!/usr/bin/env python3
# -*- coding: utf-8 -*- 


import Metashape
from msFunctions.msSubsetImages import subsetImages
from msFunctions.msError import exportMarker


def menuSubsetImages():
	subsetImages()


def menuError():
	exportMarker()
	



Metashape.app.addMenuItem("MetashapeTools/Subset Images", menuSubsetImages)
Metashape.app.addMenuItem("MetashapeTools/Export Marker Error", menuError)










