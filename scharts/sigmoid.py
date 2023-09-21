import numpy as np
import matplotlib.pyplot as plt
import math

def sig(x,t,min,max):
 x=(x-t/2)+1
 k=10/t
 a=1.5
 #min = 0.05
 #max = 0.90
 return min + (max - min) * (1 / (1 + np.exp(-x*k)) ** a)
t=20
s=2013
x = np.linspace(s, t+s, t)
p = sig(x-s,t,0.02,20)
plt.xlabel("x") 
plt.ylabel("Sigmoid(x)")  
plt.plot(x, p, label = "curve 1")
#plt.plot(y,q, label = "curve 2")
plt.legend()
plt.show()

#10 -- 1,2
#20 -- 0.5 1