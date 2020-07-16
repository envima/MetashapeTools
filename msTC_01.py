#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 09:06:49 2019

@author: um2
"""

import Metashape
import metashapeTools.msSparseCloud as mt

for chunk in Metashape.app.document.chunks:
    mt.createSparse(chunk)