#!/usr/bin/env python

#This script will introduce us to Scipy, a library useful for scientific computation
#Adapted from https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html

#Integration

#Using known function
from scipy.integrate import quad
def integrand(x, a, b):
    return a*x**2 + b

a = 2
b = 1
I = quad(integrand, 0, 1, args=(a,b))
print(I)

#Using arbitrarily spaced samples
import numpy as np
def f1(x):
   return x**2

def f2(x):
   return x**3

x = np.array([1,3,4])
y1 = f1(x)
from scipy.integrate import simps
I1 = simps(y1, x)
print(I1)


#Optimization
import numpy as np
from scipy.optimize import minimize
def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})

def rosen_der(x):
    xm = x[1:-1]
    xm_m1 = x[:-2]
    xm_p1 = x[2:]
    der = np.zeros_like(x)
    der[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
    der[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
    der[-1] = 200*(x[-1]-x[-2]**2)
    return der

res1 = minimize(rosen, x0, method='BFGS', jac=rosen_der,
               options={'disp': True})

#Linear Algebra

#inverse:
import numpy as np
from scipy import linalg
A = np.array([[1,3,5],[2,5,1],[2,3,8]])
linalg.inv(A)

#Systems solution
A = np.array([[1, 2], [3, 4]])
b = np.array([[5], [6]])
linalg.inv(A).dot(b)
linalg.det(A)
linalg.norm(A,np.inf)
