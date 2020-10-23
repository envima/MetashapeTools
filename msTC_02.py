#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import Metashape

from msFunctions.msSparseCloud import *
from msFunctions.msOrtho import *
from msFunctions.msError import *


def Toolchain02():
  ac = Metashape.app.getBool("Process all Chunks?")
  if ac:
    for chunk in Metashape.app.document.chunks:
      sparse2ortho(chunk)
      exportOrtho(chunk)
      exportSeamlines(chunk)
      exportMarker(chunk)
  else:
      chunk = Metashape.app.document.chunk
      sparse2ortho(chunk)
      exportOrtho(chunk)
      exportSeamlines(chunk)
      exportMarker(chunk)


Metashape.app.addMenuItem("MetashapeTools/Toolchain Part 2", Toolchain02)
