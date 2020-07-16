import Metashape
import csv


# export the coordinates into a python list X Y Z
def getPointCoords(chunk):
  
  # source: https://www.agisoft.com/forum/index.php?topic=11218.0
  
  
    # init result lists
    pX, pY, pZ, = [],[],[]
    
    for point in chunk.point_cloud.points:
      cov = point.cov
      coord = point.coord
      V = chunk.transform.matrix * point.coord
      V.size = 3
      X, Y, Z = chunk.crs.project(V)
     
      pX.append(X)
      pY.append(Y)
      pZ.append(Z)
     
      
    return([pX,pY,pZ])


def getErrors(chunk):
  MF = Metashape.PointCloud.Filter()
  
  MF.init(chunk, Metashape.PointCloud.Filter.ReconstructionUncertainty)
  RU = MF.values
  
  MF.init(chunk, Metashape.PointCloud.Filter.ReprojectionError)
  RE = MF.values
  
  MF.init(chunk, Metashape.PointCloud.Filter.ProjectionAccuracy)
  PA = MF.values
  
  MF.init(chunk, Metashape.PointCloud.Filter.ImageCount)
  IC = MF.values
  
  return([RU,RE,PA,IC])



def writeErrors(chunk, filename):
  
  # create file header colnames
  fheader = ["x","y","z","RU","RE","PA","IC"]
  
  # call both functions for values
  res = getPointCoords(chunk) + getErrors(chunk)
  
  # transpose output for csv writing
  res = list(map(list, zip(*res)))
  
  # open file connection and write line by line
  f = open(filename, "w")
  w = csv.writer(f)
  
  w.writerow(fheader)
  w.writerows(res)
  f.flush()
  f.close()



def msExportTiepointError(chunk, filename = None):
  
  # create a filename of not specified
  if not filename:
    filename = str(Metashape.app.document.path[:-4] + "_" + str(chunk.label) + "tiepoint_errors.txt")
    
  writeErrors(chunk, filename)



msExportTiepointError(chunk = Metashape.app.document.chunk)

