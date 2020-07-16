#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:00:09 2019

@author: marvin


"""

import Metashape
# import sys
import glob
import os

# control: do with all chunks or just the active one
# allchunks = sys.argv[1]


def purgeImages(chunk,  doc = Metashape.app.document):
    
    
    
    
    # get list of all images in chunk
    usedImg = []
    for c in chunk.cameras:
        usedImg.append(c.photo.path)
    # get all images
    allImg = glob.glob(os.path.dirname(usedImg[0]) + "/*.JPG")
    rmImg = set(allImg) - set(usedImg)
    
    # confirmation prompt
    confirm_msg = "Remove unused Cameras from Harddrive? Yes = 1, No = 0"
    confirm = Metashape.app.getInt(confirm_msg ,0)
    
    
    if (confirm == 1):
        for i in rmImg:
            os.remove(i)
        print("Removed images")
    else:
        print("Deleting images needs confirmation!")


# run function    
purgeImages(chunk = Metashape.app.document.chunk)  
    
    






