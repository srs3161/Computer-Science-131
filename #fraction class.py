#let's make a new claaaaaaaass

#fraction class
class Fraction:
    def __init__(self,n=0,d=1):     
        #a fraction has a numerator
        self.num = n
        #a fraction has a denominator
        self.setDen(d)
        self.reduce()

    @property
    def getNum(self):
        return self._num

    
    @setattr
    def setNum(self,value):
        self.num = value

    @property
    def getDen(self):
        return self._den

    @setattr
    def setDen(self,value):
        if(value != 0):
            self.den = value
        else:
            self.den = 1

    #__add__
    #__sub__
    #__mul__
    #__truediv__

    #a fraction can be represented as a decimal number
    def getReal(self):
        return (self.getNum()/self.getDen())

    def __str__(self):
        s = "{}/{} ({})".format(self.num,self.den,self.getReal())
        return s

    def __add__(self,other):
        resNum = ((self.getNum()*other.getDen())+(self.getDen()*other.getNum()))
        resDen = self.getDen()*other.getDen()

        result = Fraction(resNum,resDen)
        return result

    def __sub__(self,other):
        resNum = ((self.getNum()*other.getDen())-(self.getDen()*other.getNum()))
        resDen = self.getDen()*other.getDen()
        result = Fraction(resNum,resDen)
        return result

    def mul(self,other):
        resNum = ((self.getNum())*other.getNum())
        resDen = self.getDen()*other.getDen()
        result = Fraction(resNum,resDen)
        return result
   

    def __truediv__(self,other):
        resDen = ((self.getNum()*other.getDen())*(self.getDen()*other.getNum()))
        resNum = self.getDen()*other.getDen()
        result = Fraction(resNum,resDen)
        return result

    def reduce(self):
        gcd = self.getGCD()
        self.setNum(self.getNum()//gcd)
        self.setDen(self.getDen()//gcd)

    def getGCD(self):
        n = self.getNum()
        d = self.getDen()
        if (n<d):
            mini = n
        else:
            mini =d
        GCD = 1
        i = 2
        while(i<=mini):
            if(n%i==0 and d%i==0):
                GCD = i
            i+=1
        return GCD
    
        
        


        
        
f1 = Fraction(1,2)
f2 = Fraction(1,4)
print(f1)
print(f2)

f3 = f2.__add__(f2)
print(f3)
f4 = f1.__sub__(f2)
print(f4)

f5=f1.__truediv__(f2)
print(f5)
#a fraction can (add, multiply, subtract divide) other fractions

#reduce aka simplify
