
#
#
#

import numpy as np

"""
Created on Mon Mar 12 18:30:50 2018

Given arbitrary data-set, can find the extremas (local maxes and mins) of the dataset. Recording down when and the max values
    This works even when the data is 'messy', when some data may be slightly out of position. 
    Program currently cannot deal with extreme outliers, and may accidentally count them as an extra max/min. 

Finds maxes and mins by following basic law that one cannot have two mins or maxes in a row. 
#   Mins and maxes should be locally min/max. "Locally" defined by the 'seekThreshold' which goes forward and backward
#       that many steps to ensure that it is indeed a local max/min. 
#   Records these maxes and mins and then outputs them at the end. 
@author: Rex Lin
"""

###############################################################
#Config Variables
###############################################################
outputOther = True
# True if we want the corresponding 2nd variable values to be printed out
# Change to false if only finding extrema in y vs t.

initialUp = True
seekThreshold = 20
thresholdMax = 3  # threshold intensity in x coord to be considered a max.
thresholdMin = -3

fileName = 'res/extrema.csv'
timeColumn = 0
extremaColumn = 1  # Column where extrema data is held
compareColumn = 2  # Column with data to compare with

# Start and end time domain values
start = 0
end = 1000000


###############################################################
# Program Start
###############################################################
# Load file
data = np.loadtxt(fileName, delimiter=',', comments='#')


t = data[:, timeColumn]
x = data[:, compareColumn]
y = data[:, extremaColumn]
length = len(x)

bUp = initialUp
last = -100

# Maxes and mins not high/low enough
insufficientMax = 0
insufficientMin = 0
falsePositive2 = 0


count = 0

# Arrays for max and min
maxes = []
mins = []

skip = False

# For loop goes across all values, and finds the extremas as explained above.

for i in range(0, length - seekThreshold):
    if start <= t[i] <= end:  # Only consider if in domain.

        # Dataset going up
        if bUp:
            if y[i] < y[i - 1]:
                skip = False
                for j in range(i, i + seekThreshold):  # Make sure larger than recent future and history
                    if not (y[j] <= y[i - 1]):
                        skip = True
                for k in range(i - seekThreshold, i - 1):
                    if not (y[k] <= y[i - 1]):
                        skip = True

                if not skip:  # We have found a local max, now going down.
                    bUp = False
                    if y[i - 1] >= thresholdMax:  # Only count if
                        maxes.append(str(t[i - 1]) + "," + str(x[i - 1]) + "," + str(y[i - 1]))
                    else:
                        insufficientMax += 1
                    last = i - 1
        # Dataset going down
        else:
            if y[i] > y[i - 1]:
                skip = False
                for j in range(i, i + 20):  # Make sure larger than recent future and history
                    if not (y[j] >= y[i - 1]):
                        skip = True
                for k in range(i - 20, i - 1):
                    if not (y[k] >= y[i - 1]):
                        skip = True

                if not skip:  # At least 5 datapoints since drop, discounts random immediate peaks.
                    bUp = True
                    if y[i - 1] <= thresholdMin:  # Only count if
                        mins.append(str(t[i - 1]) + "," + str(x[i - 1]) + "," + str(y[i - 1]))
                    else:
                        insufficientMin += 1

print("Maxes")
for i in maxes:
    print(i)

print("Mins")
for i in mins:
    print(i)

print("Count Max = " + str(len(maxes)))
print("Insufficient = " + str(insufficientMax))
print("Count Min = " + str(len(mins)))
print("Insufficient = " + str(insufficientMin))
