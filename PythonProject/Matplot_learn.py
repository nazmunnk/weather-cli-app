import matplotlib.pyplot as matplt
import  numpy as np
from matplotlib.lines import lineStyles

x=np.array([10, 20, 30, 40 , 50])
y1=np.array([5,2,8,1,7])
y2=np.array([8,1,4,9,5])
y3=np.array([2,9,6,5,3])
#line_style=dict(marker="*",markersize=10,markerfacecolor="black",markeredgecolor="red",linestyle="dotted",linewidth=2)
matplt.title("class size",fontsize=30,family="arial",fontweight="bold",color="red")
matplt.xlabel("x axis",fontweight="bold")
matplt.ylabel("y axis")
matplt.tick_params(axis="x",color="orange")
matplt.plot(x,y1,color="red")
matplt.plot(x,y2, color="green")
matplt.plot(x,y3, color="blue")
matplt.subplots_adjust(bottom=0.15,left=0.14)
matplt.xticks(x)
matplt.show()