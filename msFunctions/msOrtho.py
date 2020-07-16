#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 09:47:53 2019

@author: marvin
"""

import Metashape

# control: do with all chunks or just the active one
def sparse2ortho(chunk, doc = Metashape.app.document, orthoRes = 0.05):
    crs = Metashape.CoordinateSystem("EPSG::25832")
    
    # create mesh
    chunk.resetRegion()
    chunk.buildModel(surface=Metashape.SurfaceType.HeightField, source = Metashape.DataSource.PointCloudData,
                     interpolation = Metashape.Interpolation.EnabledInterpolation, face_count = Metashape.FaceCount.HighFaceCount)
    chunk.smoothModel(35)	
    doc.save()
    
    
    # build ortho
    chunk.resetRegion()
    chunk.buildOrthomosaic(surface=Metashape.ModelData, projection=crs, dx=orthoRes, dy=orthoRes)
    doc.save()
    

#def dense2ortho(chunk, doc = Metashape.app.document, orthoRes = 0.05):
    


def exportOrtho(chunk, doc = Metashape.app.document, orthoRes = 0.05):

    outpath = doc.path[:-4]  # project path without file extension
    crs = Metashape.CoordinateSystem("EPSG::25832")

     # export ortho
    chunk.resetRegion()
    chunk.exportOrthomosaic(str(outpath + "_" + str(chunk.label) + "_orthomosaic.tif"),
                            projection = crs, raster_transform = Metashape.RasterTransformNone,
				write_kml=False, write_world=False, write_alpha=False, tiff_big=True,
                tiff_compression=Metashape.TiffCompressionNone, white_background=True,dx=orthoRes,dy=orthoRes)
    # save document
    doc.read_only = False
    doc.save()
    # create report
    chunk.exportReport(outpath + "_" + chunk.label + "_report.pdf") 


