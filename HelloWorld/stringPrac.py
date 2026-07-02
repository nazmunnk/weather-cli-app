
"""

str=input()
upperCheck=""
0lowerCheck=""
numCheck=""
extraCheck=""
for c in  str:
    if c.isupper():
        upperCheck +=c
    elif c.islower():
        lowerCheck+=c
    elif c.isnumeric():
        numCheck+=c
    else:
        extraCheck+=c


print(upperCheck)
print(lowerCheck)
print(numCheck)
print(extraCheck.strip())

str=list(input())
result="".join(str)
#print(result)
str.reverse()
newResult="".join(str)
#print(newResult)
if result==newResult:
    print("yes")
else:
    print("no")

  """

str=input()
newList=[]

for i in range(len(str)-1):
    if i%2 ==0:
     newList.append(str[i+1])
     newList.append(str[i])

Fstr="".join(newList)
print(Fstr)







