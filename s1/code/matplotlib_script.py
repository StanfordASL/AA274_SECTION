#!/usr/bin/env python

#This script will introduce us to Matplotlib, a library used for visualization
import numpy as np
import matplotlib.pyplot as plt

x = range(100)
y = np.sin(x)

plt.plot(x,y)
plt.title("sin(x)")
plt.xlabel("x")
plt.xlabel("y")
plt.show()

plt.scatter(x,y)
plt.show()

#Adapted from https://matplotlib.org/tutorials/introductory/sample_plots.html
data = np.random.randn(2, 100)
plt.hist(data[0])
plt.show()
plt.hist2d(data[0], data[1])
plt.show()
