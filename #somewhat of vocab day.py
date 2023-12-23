#somewhat of vocab day
#f-ormal and actual paramters
#def method(variable):#the formal parameter in the defn
 #   return variable*2

#a=7
#method(a) #the actual parametr in the method call
#print (method(a))
from random import randint
mylist = []
for x in range(100):
    x = randint(0,99)
    x.append(x)
print(mylist)

   
c= 1
minvalue = mylist[0]
while(c<len(mylist)):
    if(mylist[c]<minvalue):
        minvalue = mylist[c]
        print("Min value thus far:",c)
        c +=1
print(minvalue)

target = 7
def find(target):
    c = 0
    isHere = False
    while(c<len(mylist)):
        if (mylist[c] == target):
            print("target found at index:", c)
            isHere = True
        c +=1
    return isHere








        
