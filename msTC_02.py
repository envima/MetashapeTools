#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 09:08:10 2019

@author: um2
"""

import Metashape
import metashapeTools.msSparseCloud as mt
import metashapeTools.msOrtho as mo

for chunk in Metashape.app.document.chunks:
    mt.filterSparse(chunk)
    mt.exportSparse(chunk)
    
    mo.sparse2ortho(chunk)
    mo.exportOrtho(chunk)
