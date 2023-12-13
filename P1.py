import matplotlib.pyplot as plt
import numpy as np

x=np.array(['may','june','july','aug','sep','oct','nov','dec'])
y=np.array(['23','32','27','50','22','18','11','65'])
y1=np.array(['12','10','9','15','5','2','3','12'])

plt.plot(x,y, label = "line 1")
plt.plot(x,y1, label = "line 2")
plt.legend()
plt.show()