#
# @author: iamtrex
# A simple plotter that plots a function on a given domain with some number of points.

import numpy as np
import matplotlib.pyplot as plt

##################################################################################
# Constants.
##################################################################################
# Names of axis and graph
TITLE = r'Voltage (V) vs Frequency (Hz)'
x_name = 'Voltage'
x_units = 'v'
y_name = 'Frequency'
y_units = 'Hz'

# define the domain of f(x) that we wish to plot: from xmin to xmax with npoints
xmin = 0
xmax = 10
npoints = 500

# Plotting parameters. len(params) must be 1 less than # of arguments for function.
params = (10, -1, 5)


# Function to plot as well as its parameters
def func(x, a, b, c):
    return a * np.sin(x - b) + c


##################################################################################
# Plot the function
##################################################################################

# define x as an array  of points  from 0, 100
x = np.linspace(xmin, xmax, npoints)
# get y values from function
y = func(x, *params)


# Two methods of plotting - line or dots. Uncomment whichever you want to use
plt.plot(x, y, marker="", linestyle="-", linewidth=2, color="b", label=" function")  # a continuous line
# plt.plot(x, y, 'bo')  # dots

plt.xlabel('{} ({})'.format(x_name, x_units))
plt.ylabel('{} ({})'.format(y_name, y_units))
plt.title(TITLE)
plt.show()
