# TerrainAnalyzer

## Purpose
This machine will accept CSV files from the JMARS "MOLA 128ppd Elevation" layer. It will then determine whether your route exceeds a slope angles of greater than 30 degrees. (Curiosity rover was able to reach 35 degrees then aborted the manuever) 

## Directions
Draw your route with that layer active. Then go to the chart tab on the dock. Right click on the chart and save the file as a "yourmission.csv". Place the saved file in the same folder as the python program and run.

## Steps
* How to draw in the MOLA 128pps layer:
* Select the cursor tool in the top right of JMARS.
* Left click on the map slowly and keep adding points to the route.
* When you're at the end of the route, double left click and the route  will turn from yellow to red. 
* Once this is done, go to the dock, select chart and right click to export your CSV.
* Place the exported file in the same directory as the python program.
* Change **line 14** to your file name.
* Run the **python slopes.py*
* Check output for great success. 

## Notes
Be careful with the MOLA 128pps layer as it is prone to accidentally losing your route. It is best to draw the route with the MOLA layer, then immediately change to a 3D shape layer and draw the route again. 

The purpose of 'modded' is to account for the fact that the 128 MOLA layer is not perfect and in some cases it could be useful to consider that the angle is not as bad as the data suggests. 


![Mission Area](https://github.com/rscinto/TerrainAnalyzer/blob/master/images/LZ3route.PNG)