#Code to take a data table of molar specific heat capacity of Aluminum
#  over a temperature range from 70 K to 298 K,
#  interpolate to a single-degree resolution grid,
#  and find the area under the curve between 77 K and 296 K

#Bring in numpy
import numpy as np

#Bring in the interp1d routine from scipy
from scipy.interpolate import interp1d

#The given data values:
T = np.array([70,100,150,200,250,298])
Cp = np.array([1.85,3.12,4.43,5.16,5.56,5.82])

#Make a new empty array running from 70 to 298, one slot for each 1 degree
Tnew = np.linspace(70,298,229)

#print(Tnew) #for sanity checking

#generate a function that interpolates from original grid to new grid,
#  using "cubic" spline routine
f = interp1d(T,Cp,kind='cubic')

#Get new Cp values using the fit function:
Cpnew = f(Tnew)

# Calculate the area under the curve using the trapezoidal rule
area = np.trapz(Cp, T)

print(f"The area under the full curve is: {area:.2f}")

#Slice the new arrays to just go from 77 K to 296 K:
TnewLim = Tnew[7:227]
CpnewLim = Cpnew[7:227]

#print("TnewLim: ",TnewLim)
#print("CpnewLim: ",CpnewLim)

# Calculate the area under the new curve using the trapezoidal rule
area = np.trapz(Cpnew, Tnew)

print(f"The area under the interpolated curve is: {area:.2f}")

area = np.trapz(CpnewLim, TnewLim)

print(f"The area under the interpolated curve from 77 K to 296 K is: {area:.2f}")    
