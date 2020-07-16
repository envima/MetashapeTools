#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 13:32:25 2019

@author: um2
"""

# import markers

import Metashape
import sys

# control: do with all chunks or just the active one
allchunks = sys.argv[1]


# Here starts the process after the GCP were set and corrected.
# Start with point cloud filtering and then build the densecloud

def filterSparse(chunk, doc = Metashape.app.document):
    
    chunk.resetRegion() 
    MF = Metashape.PointCloud.Filter()
    
    # Reconstruction uncertanty
    MF.init(chunk, Metashape.PointCloud.Filter.ReconstructionUncertainty)		
    MF.selectPoints(50)
    chunk.point_cloud.removeSelectedPoints()
    chunk.optimizeCameras(fit_f=True, fit_cxcy=True, fit_aspect=True, fit_skew=True, fit_k1k2k3=True, fit_p1p2=True, fit_k4=True)
    chunk.resetRegion()  
    
    # Reprojection Error Filter
    MF.init(chunk, Metashape.PointCloud.Filter.ReprojectionError)		
    MF.selectPoints(0.9)
    chunk.point_cloud.removeSelectedPoints()
    chunk.optimizeCameras(fit_f=True, fit_cxcy=True, fit_aspect=True, fit_skew=True, fit_k1k2k3=True, fit_p1p2=True, fit_k4=True)
    chunk.resetRegion()
    
    # Projection Accuracy Filter    
    MF.init(chunk, Metashape.PointCloud.Filter.ProjectionAccuracy)		
    MF.selectPoints(10)
    chunk.point_cloud.removeSelectedPoints()	
    chunk.optimizeCameras(fit_f=True, fit_cxcy=True, fit_aspect=True, fit_skew=True, fit_k1k2k3=True, fit_p1p2=True, fit_k4=True)
    chunk.resetRegion()
     
    # save document
    doc.read_only = False
    doc.save()
    





def createDenseCloud(chunk, doc = Metashape.app.document):
    
    # build depth maps with moderate filter
    chunk.buildDepthMaps(quality = Metashape.Quality.HighQuality, filter = Metashape.FilterMode.ModerateFiltering, reuse_depth=True)
    # build dense cloud
    chunk.buildDenseCloud(point_colors=True, keep_depth=True)
    
    doc.read_only = False
    doc.save()
    
    
# control: do with all chunks or just the active one
def createDenseCloudControl(allchunks):  
    print(allchunks)
    if allchunks == "1": 
        for i in Metashape.app.document.chunks:
            filterSparse(chunk = i)
            createDenseCloud(chunk = i)
    else:
        filterSparse(chunk = Metashape.app.document.chunk)
        createDenseCloud(chunk = Metashape.app.document.chunk)

        
# RUN CONTROL

createDenseCloudControl(allchunks)

