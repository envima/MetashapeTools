#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:00:09 2019

@author: marvin


"""

import Metashape
import csv
import statistics



def pointcloudMetrics(chunk, outpath):
	# export original sparse cloud metrics
	MF = Metashape.PointCloud.Filter()
	MF.init(chunk, Metashape.PointCloud.Filter.ReconstructionUncertainty)
	RU = MF.values
	MF.init(chunk, Metashape.PointCloud.Filter.ReprojectionError)
	RE = MF.values
  
	MF.init(chunk, Metashape.PointCloud.Filter.ProjectionAccuracy)
	PA = MF.values
  
	 
	res = {"RU": [min(RU), max(RU), statistics.mean(RU)], "RE": [min(RE), max(RE), statistics.mean(RE)], "PA": [min(PA), max(PA), statistics.mean(PA)]}
	 
	# save results
	with open(outpath, 'w') as f:
		print(res, file=f)







def optimizeSparsecloud(chunk):
	
	 outpath = outpath = Metashape.app.document.path[:-4]  
	
	
	 # optimize camera
	 chunk.optimizeCameras(fit_f=True, fit_cx=True, fit_cy = True, fit_b1=True, fit_b2 = True, fit_k1 = True, fit_k2 = True, fit_k3 = True, fit_k4=True, fit_p1 = True, fit_p2 =True, adaptive_fitting=True)
	 
	 # export original marker errors
	 chunk.exportReference(path = str(outpath + "_" + str(chunk.label) + "_original_marker_error.txt"),
     format = Metashape.ReferenceFormatCSV, items = Metashape.ReferenceItemsMarkers, columns = "noxyzXYZuvwUVW", delimiter = ",")
     
     pointcloudMetrics(chunk, outpath = str(str(Metashape.app.document.path[:-4]) + "initial_pointcloud_errors.txt"))
     
     chunk.copy()
     chunk = Metashape.app.document.chunk
     chunk.label = "process"
     
     # # # Initial Filter
     
     MF = Metashape.PointCloud.Filter()
     MF.init(chunk, Metashape.PointCloud.Filter.ReconstructionUncertainty)
     MF.selectPoints(50)
     chunk.point_cloud.removeSelectedPoints()
     chunk.optimizeCameras(fit_f=True, fit_cx=True, fit_cy = True, fit_b1=True, fit_b2 = True, fit_k1 = True, fit_k2 = True, fit_k3 = True, fit_k4=True, fit_p1 = True, fit_p2 =True, adaptive_fitting=True)
     MF.init(chunk, Metashape.PointCloud.Filter.ReprojectionError)		
     MF.selectPoints(1)
     chunk.point_cloud.removeSelectedPoints()
     chunk.optimizeCameras(fit_f=True, fit_cx=True, fit_cy = True, fit_b1=True, fit_b2 = True, fit_k1 = True, fit_k2 = True, fit_k3 = True, fit_k4=True, fit_p1 = True, fit_p2 =True, adaptive_fitting=True)
     MF.init(chunk, Metashape.PointCloud.Filter.ProjectionAccuracy)		
     MF.selectPoints(10)
     chunk.point_cloud.removeSelectedPoints()	
     chunk.optimizeCameras(fit_f=True, fit_cx=True, fit_cy = True, fit_b1=True, fit_b2 = True, fit_k1 = True, fit_k2 = True, fit_k3 = True, fit_k4=True, fit_p1 = True, fit_p2 =True, adaptive_fitting=True)
     chunk.resetRegion()
     
     # calculation of checkpoint error
     
     
     
     
     
     
  
     
	 
