"""
i=1
while i<=15:
    print(i * '*')
    i=i+1



n = ["j","k","d","a","e"]
#print(n)
n[0]="t"
#print(n[0])
#print(n[-2])
print(n[0:3])
print(n[0])


num=[1,2,3,4,5]
num.append(6)
num.insert(0,7)
#num.remove(4)
#num.clear()
print(1 in num)
print(len(num))


num=[1,2,3,4,5]


for i in num:
    print(i)
while i<len(num):
    print(num[i])
    i=i+1


#num=range(5,10,2)

#print(num)
for n in range(5):
    print(n)


x=3
print(type(x))








"""
#
#
#
#
#
# num = [[i for i in range(3)] for j in range(3)]
#
# for i in range(3):
#     for j in range(3):
#         if i==j:
#             print("#")
#
# print(num)
#
# for i in range(1):
#     print("#")
# else:
#     print("#")
#
#
"""
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


x=4
y=1
a= x&y
b= x|y
c=~x
d=x^5
e=x>>2
f=x<<2

print("a",a,"b",b,"c",c,"d",d,"e",e,"f",f)




user_word=input()# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word=user_word.upper()
for letter in user_word:

    if letter=="A":
        continue
    elif letter=="E":
        continue
    elif letter=="I":
        continue
    elif letter=="O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)
"""

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)
