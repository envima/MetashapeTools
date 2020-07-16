#!/usr/bin/env python3
# -*- coding: utf-8 -*- 


import Metashape
from msFunctions.msSubsetImages import subsetImages
from msFunctions.msError import exportMarker


def menuSubsetImages():
	subsetImages()


def menuError():
	ac = Metashape.app.getBool("Process all chunks?")
	if ac:
		for chunk in Metashape.app.document.chunks:
			exportMarker(chunk)
	else:
		exportMarker(chunk)
	



Metashape.app.addMenuItem("MetashapeTools/Subset Images", menuSubsetImages)
Metashape.app.addMenuItem("MetashapeTools/Export Marker Error", menuError)










