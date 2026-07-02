import matplotlib.pyplot as plt
import  numpy as np

categories=["apple","mango","lichi","papaya","coconut"]
values=np.array([4,7,2,9,1])
plt.pie(values,labels=categories,autopct="%1.1f%%",explode=[0,0,0,0,0.1],shadow=True,startangle=180)
#plt.barh(categories,values,color="green")

plt.show()