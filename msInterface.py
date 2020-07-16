#!/usr/bin/env python3
# -*- coding: utf-8 -*- 



import Metashape
import msFunctions.msSubsetImages
import msFunctions.msError


def menuSubsetImages():
	msSubsetImages()


def menuError():
	msError()
	



Metashape.app.addMenuItem("MetashapeTools/Subset Images", menuSubsetImages)
Metashape.app.addMenuItem("MetashapeTools/Export Marker Error", menuError)









