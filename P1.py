import matplotlib.pyplot as plt
import numpy as np

x=['may','june','july','aug','sep','oct','nov','dec']
y=[23,32,27,50,22,18,11,65]
x1=['may','june','july','aug','sep','oct','nov','dec']
y1=[12,10,9,15,5,2,3,12]
plt.xlabel('month')
plt.ylabel('visitors')

plt.plot(x,y, label = "line 1")
plt.plot(x1,y1, label = "line 2")
plt.legend()
plt.show()