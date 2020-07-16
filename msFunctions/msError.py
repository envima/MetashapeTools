 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  13 2020

@author: marvin
"""

import Metashape


def exportMarker(chunk, doc = Metashape.app.document):
	outpath = doc.path[:-4]
	
	chunk.exportReference(path = str(outpath + "_" + str(chunk.label) + "_marker_error.txt"),
	 format = Metashape.ReferenceFormatCSV, items = Metashape.ReferenceItemsMarkers, columns = "noxyzXYZuvwUVW", delimiter = ",")
	
	

