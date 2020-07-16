#!/usr/bin/env python
# -*- coding: utf-8 -*-
# script version 0.2.1


# source:  https://www.agisoft.com/forum/index.php?topic=5681.0

import Metashape


def subsetImages():
	chunk = Metashape.app.document.chunk
	step = Metashape.app.getInt("Specify the selection step:" ,2)
	index = 1
	for camera in chunk.cameras:
		if not (index % step):
				camera.selected = True
		else:
				camera.selected = False
		index += 1


Metashape.app.addMenuItem("Custom/Subset", subsetImages)
