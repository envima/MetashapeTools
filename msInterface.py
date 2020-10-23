#!/usr/bin/env python3
# -*- coding: utf-8 -*- 


import Metashape
from msFunctions.msSubsetImages import subsetImages
from msFunctions.msError import exportMarker
from msFunctions.msExportTiepointError import *
from msFunctions.msOptimizeSparsecloud import *
from msFunctions.msReproducibility import *


# helper for optional all chunk processing:
def menuHelper(fun):
	def menuFunc():
		ac = Metashape.app.getBool("Process all chunks?")
		if ac:
			for chunk in Metashape.app.document.chunks:
				fun(chunk)
		else:
			fun(chunk)
	return menuFunc
	


menuSubsetImages = menuHelper(subsetImages)


def menuError():
	ac = Metashape.app.getBool("Process all chunks?")
	if ac:
		for chunk in Metashape.app.document.chunks:
			exportMarker(chunk)
	else:
		exportMarker(chunk)
	


def menuTiepoints():
	ac = Metashape.app.getBool("Process all chunks?")
	if ac:
		for chunk in Metashape.app.document.chunks:
			ExportTiepointError(chunk)
	else:
		ExportTiepointError(chunk)


def menuOptimizeSparsecloud():
	chunk = Metashape.app.document.chunk
	optimizeSparsecloud(chunk)



def menuReproducibility():
	RE = Metashape.app.getFloat(label = "Optimal Reprojection Error", value = 0)
	k = Metashape.app.getInt(label = "Times", value = 5)
	
	repro(chunk, RE = RE, k = k)


Metashape.app.addMenuItem("MetashapeTools/Subset Images", menuSubsetImages)
Metashape.app.addMenuItem("MetashapeTools/Export Marker Error", menuError)
Metashape.app.addMenuItem("MetashapeTools/Export Tiepoint Error", menuTiepoints)
Metashape.app.addMenuItem("MetashapeTools/Optimize Sparsecloud", menuOptimizeSparsecloud)
Metashape.app.addMenuItem("MetashapeTools/Reproducibility", menuReproducibility)








