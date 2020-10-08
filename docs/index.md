## Metashape Toolbox

This Toolbox provides basic workflow scripts and optimizations for Agisoft Metashape.
Follow the installation guide and there will be a new Menu Point in Metashape available to start the Workflow.



## The Workflow

1. Add the images you want to process to the Chunk.
2. Give the chunk a usefull name.
3. Start the script `Toolchain Part 1`

This will align the images with sensefull default parameters.

* Key Point Limit: 40000
* Tie Point Limit: 4000
* Downsampling: 1

After the script is finished, import your Ground Control Points (GCP) and align them manually in at least 4 images.
Use about 30 % of the GCP as independent Checkpoints by unticking the checkbox in the Reference Pane.

Now you can optimize the georeferencing of the product with the script `Optimize Sparsecloud`.
This will print out a Reprojection Error for wich the checkpoint error is at its minimum.

Now use `Toolchain Part 2`. This includes the following steps:

* create 2.5D Mesh
* smooth Mesh with factor 35
* create Orthomosaic
	* surface: mesh
	* refine seamlines = True
* export of Orthomosaic, Seamlines and Marker error


## Orthomosaic Reproducibility

1. Add the images you want to process to the Chunk.
2. Import the GCP and align them.
3. Start the script `Reproducibility`


This will compute a set amount of orthomosaics (default is 5), which later can be analysed in R.













