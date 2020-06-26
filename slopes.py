#this program will take in a CSV file from JMARS and calculate the 
#route and determine if the slope angle exceeds 30 degrees
# 
#  
import csv
import math

#These arrays hold the data from the CSV
distances = []
elevations = []

#File processing
with open('lz1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter= ',')
    
    #skips over header
    next(readCSV)

    for row in readCSV:
        
        #everything after an 'N/A' is found will
        #be skipped
        if row[3] == 'N/A':
            break
        
        distHolder = float(row[0])
        distances.append(distHolder)
        elevHolder = float(row[3])
        elevations.append(elevHolder)




totalIndices = len(distances)
index = 0
eleDelta = 0.0
distDelta = 0.0
failure = False
angles = []
moddedAngle = []
moddedDistance = []

#Iterate through the elevations and distances
while index < (totalIndices - 1):

    #priming read
    distDelta = abs(distances[index + 1] - distances[index])
    #convert to meters
    distDelta = distDelta * 1000
    #initialization
    eleDelta = abs(elevations[index + 1] - elevations[index])
    #priming read and reset

    oneMeterAngle = math.degrees(math.atan(eleDelta/distDelta))

    #store values
    angles.append(oneMeterAngle)

    if oneMeterAngle > 30:
        oneMeterAngle = oneMeterAngle / 2
        moddedAngle.append(oneMeterAngle)
        moddedDistance.append(distances[index])

    #resets
    index = index + 1
    eleDelta = 0.0
    distDelta = 0.0
            

#Test values in the angles array for tolerance
badLines = []
badAngles = []


for x in range(len(angles)):
    if angles[x] > 30 or angles[x] < -30:
        print('Route out of tolerance at: ', x)
        print('Angle: ', angles[x])
        badLines.append(distances[x])
        badAngles.append(angles[x])
        failure = True
    else:
        print('In limits at ' + str(x) + ' csvLine.')
        print('Angle: ', angles[x])


for x in range(len(moddedAngle)):
    print('Modded at '+ str(moddedDistance[x]))
    print('Angle: ' + str(moddedAngle[x]))
    


#print yield
if failure:
    print('operational limits exceeded')
    print('Num Failures: ', len(badAngles))
    for x in range(len(badAngles)):
        print('km: ', badLines[x])
        print('Angle: ', badAngles[x])
else:
    print('Within operational limits')

        #print("Distance delta test: ", distDelta)
        #break 



