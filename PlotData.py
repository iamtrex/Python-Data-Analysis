#
# @author: iamtrex
# A simple plotter that plots data from csv files.

import numpy as np
import matplotlib.pyplot as plt
#############################################################################
# Constants -- Modify these such that they make sense for the data being read
#############################################################################

# File name to be plotted. Assumes comma delimited, # commented csv file
    # Modify following lines to match csv file.
file_name = "res/test-data.csv"
delim = ','
comm = '#'

x_data_col = 0 # Column with data for x axis
y_data_col = 1 # Column with data for y axis

#Name and unit for respective axis
x_name = "Time"
x_unit = "s"

y_name = "Voltage"
y_unit = "V"


#############################################################################
# Plots the data from 'file_name'
#############################################################################

data = np.loadtxt(file_name, delimiter=delim, comments=comm)

# Assume x data in 1st column, y data in 2nd column
x = data[:,x_data_col]
y = data[:,y_data_col]

# Static uncertainty, currently none.
uncertainty = 0 # Default is no uncertainty
plt.errorbar(x, y, yerr=uncertainty, marker='o', linestyle='')

plt.xlabel('{} ({})'.format(x_name, x_unit))
plt.ylabel('{} ({})'.format(y_name, y_unit))

plt.show() # Show graph.
