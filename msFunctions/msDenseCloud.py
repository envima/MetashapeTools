#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 13:32:25 2019

@author: um2
"""

# import markers

import Metashape




def createDenseCloud(chunk):
    
    # build depth maps with moderate filter
    chunk.buildDepthMaps(downscale = 4, filter_mode = Metashape.FilterMode.ModerateFiltering)
    # build dense cloud
    chunk.buildDenseCloud(point_colors=True, keep_depth=True, point_confidence = True)
    # export
    outpath = Metashape.app.document.path[:-4]
    chunk.exportPoints(path = str(outpath + "_" + str(chunk.label) + "_densecloud.laz"), sourceData = Metashape.DataSource.DenseCloudData, save_colors = True, save_confidence = True)
    

