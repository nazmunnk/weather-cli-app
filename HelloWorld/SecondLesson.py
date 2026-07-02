"""
name = input("tell me your name ")
print("my name is " + name)

b_year = input("tell me birth year ")
age = 2025 - int(b_year)
print(age)


num1 = input(" Number 1: ")
num2 = float(input("number 2: "))
sum = float(num1) + num2
print(sum)
print("sum is " + str(sum))
print( float(num1) + float(num2) )


myLine= 'my name is nnks'
print(myLine.upper())
print(myLine.find('y'))
print(myLine.replace('is','iz'))
print('my' in myLine)


print(10/3)
print(10//3)
print(10%3)
print(10**3)
x=10
x=x+3
x+=3

x = 3 > 2
print(x)
x = 3 == 2
print(x)
x = 3 != 2
print(x)


price = 25
print(price>10 and price<30)
price = 5
print(not price>10)


temp=25
if temp>30:
    print("it's a hot day")
    print("drink water")
elif temp>20:
    print("great")
elif temp>10
    print("low cold")
else:
    print("cold")
print("done")

"""

weight =  float(input("weight: "))
unit=  input("(k)g or (L)bs: ")


if unit.upper() == "K" :
    print( weight / 0.45)
elif unit == "l"or unit=="L":
    print(weight * 0.45 )
else:
    print("wrong input")














