import matplotlib.pyplot as plt
import  numpy as np


x1=[0,1,3,6,8,2,7,0]
y1=[87,67,32,47,57,38,92,100]
x2=[0,9,1,5,8,5,2,0]
y2=[78,76,23,74,75,83,29,50]

plt.scatter(x1,y1,alpha=0.7,color="black",s=200,label="a")
plt.scatter(x2,y2,alpha=0.7,color="red",s=200,label="b")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("scatter practice")
plt.legend()
plt.show()



