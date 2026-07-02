import matplotlib.pyplot as plt
import  numpy as np


sc=np.random.normal(loc=80,scale=50,size=100)
sc=np.clip(sc,0,100)

plt.hist(sc,bins=10,edgecolor="black")
plt.show()