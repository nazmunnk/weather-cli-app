import matplotlib.pyplot as plt
import  numpy as np

categories=np.array(["apple","mango","lichi","papaya","coconut"])
values=np.array([4,7,2,9,1])
#plt.bar(categories,values,color="green",width=1-0.7)
plt.barh(categories,values,color="green")
plt.title("Fruits")
plt.xlabel("fruits name")
plt.ylabel("amount")
plt.show()