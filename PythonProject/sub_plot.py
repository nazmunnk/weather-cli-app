import matplotlib.pyplot as plt
import  numpy as np


x=np.array(([1,2,3,4,5]))

fg,ax=plt.subplots(2,2)
ax[0,0].plot(x,x*2)
ax[0,0].set_title("x*2")

ax[0,1].plot(x,x**2)
ax[0,1].set_title("x**2")

ax[1,0].plot(x,x*3)
ax[1,0].set_title("x*3")

ax[1,1].plot(x,x**3)
ax[1,1].set_title("x**3")

plt.show()