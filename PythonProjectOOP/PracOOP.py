class Vehicle:
    def __init__(self,model,brand,rental_price):
     self.model=model
     self.brand=brand
     self.price=rental_price
    def show(self):
     print(self.brand,self.price, self.model)
    def rent(self):
        print("done")


class Car(Vehicle):
    def rent(self):
        print("car rented")


class Bike(Vehicle):
    def rent(self):
        print("bike rented")

class Truck(Vehicle):
    def rent(self):
        print("truck rented")

c=Car('x5','toyota',200)
b=Bike('t5','runner',100)
t=Truck('n5','bmw',500)
# for x in (c,b,t):
#     x.show()
#     x.rent()
list=[c,b,t]
for x in range(len(list)):
    #print(list[x])
    list[x].show()
    list[x].rent()


