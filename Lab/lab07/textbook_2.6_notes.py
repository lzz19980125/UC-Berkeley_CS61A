#python规定：所有对象都应该能够产生两种不同的字符串表示：一种是人类可解释的文本，另一种是 Python 可解释的表达式。
#str()返回人类可读的字符串。  repr(object) --> 返回一个 Python 表达式，它可以求值为等价的对象。
print(str(12e12))
print(repr(12e12))
print("****************")

from datetime import date
today = date(2011,9,12)
print(repr(today))
print(str(today))


print(today.__repr__())
print(today.__str__())
print("****************")

#多重表示（对应java的多态）
#特殊方法special methods：在类构建时，自动调用__init__,在print时自动调用__str__，
#在需要有交互式值显示的场景中，自动调用__repr__
#有时需要动态为object增加属性（所谓动态，就是在程序执行的过程中为object增加属性，而不是事先定义好的）。此时应该应用装饰器 @property
# @ property的作用是：在不使用括号表达式的情况下能够调用函数，请看如下ComplexRI以及ComplexMA的定义方法：

#class Number是针对泛型中的类型调度而重新进行书写的


def add_complex_and_rational(c,r):
    return ComplexRI(c.real+r.numer/r.denom,c.imag)
def mul_complex_and_rational(c,r):
    r_magnitude , r_angle = r.numer / r.denom , 0
    if r_magnitude <0:
        r_magnitude , r_angle = -r_magnitude ,pi
    return ComplexMA(c.magnitude*r_magnitude,c.angle+r_angle)
def add_rational_and_complex(r,c):
    return add_complex_and_rational(c,r)
def mul_rational_and_complex(r,c):
    return mul_complex_and_rational(c,r)

# class Number(object):
#     def __add__(self, other):
#         if(self.type_tag == other.type_tag):
#             return self.add(other)
#         elif (self.type_tag,other.type_tag) in self.adders:
#             return self.cross_apply(other,self.adders)
#     def __mul__(self, other):
#         if(self.type_tag == other.type_tag):
#             return self.mul(other)
#         elif (self.type_tag,other.type_tag) in self.multipliers:
#             return self.cross_apply(other,self.multipliers)
#     def cross_apply(self,other,cross_fns):
#         cross_fn = cross_fns[(self.type_tag , other.type_tag)]
#         return cross_fn(self,other)
#     adders = {('com','rat'):add_complex_and_rational,
#               ('rat','com'):add_rational_and_complex}
#     multipliers = {('com','rat'):mul_complex_and_rational,
#                 ('rat','com'):mul_rational_and_complex}

def rational_to_complex(r):
    return ComplexRI(r.numer / r.denom, 0)

class Number(object):
    def __add__(self, other):
        x,y = self.coerce(other)
        return x.add(y)
    def __mul__(self,other):
        x , y = self.coerce(other)
        return x.mul(y)
    def coerce(self,other):
        if self.type_tag == other.type_tag:
            return self , other
        elif (self.type_tag, other.type_tag) in self.coercions:
            return (self.coerce_to(other.type_tag),other)
        elif (other.type_tag , self.type_tag) in self.coercions:
            return (self,other.coerce_to(self.type_tag))
    def coerce_to(self,other_tag):
        coercion_fn = self.coercions[(self.type_tag ,other_tag)]
        return coercion_fn(self)
    coercions = {('rat','com'):rational_to_complex}

class Complex(Number):
    type_tag = ''
    def add(self,other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)
    def mul(self, other):
        magnitude = self.magnitude * other.magnitude
        return ComplexMA(magnitude, self.angle + other.angle)

from math import atan2
class ComplexRI(Complex):
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    @property
    def magnitude(self):
        return ((self.real **2 + self.imag **2)**(-0.5))
    @property
    def angle(self):
        return atan2(self.imag , self.real)
    def __repr__(self):
        return 'ComplexRI ({0} , {1})'.format(self.real , self.imag)

from math import sin,cos,pi
class ComplexMA(Complex):
    def __init__(self,magnitude,angle):
        self.magnitude = magnitude
        self.angle = angle
    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)
    def __repr__(self):
        return 'ComplexMA ({0} , {1})'.format(self.magnitude , self.angle)

#检验一下@property的调用方法
print(ComplexRI(1,2).magnitude)
print(ComplexRI(1,2) + ComplexMA(2,pi/2))
print(ComplexRI(0,1) * ComplexRI(0,1))

#特殊方法后续：
#可以对object的__bool__方法进行overide，以此改变默认object的bool认定方式
class Account(object):
    def __init__(self,name):
        self.name = name
        self.balance = 0
    def __bool__(self):
        return not self.balance

print(Account('jack').__bool__())
if  Account('jack'):
    print('Jack has nothing')
print("************************")

#__len__方法以及__getitem__ 方法
print(len('GO'))
print('GO'.__len__())
print(bool(''))
print(bool("GO"))
print(bool([]))
print('GO'.__getitem__(0))
print('GO'[0])

#Call objects object的__call__方法可以使得object如函数一般被调用
print("***********************")
class Adder(object):
    def __init__(self,n):
        self.n = n
    def __call__(self, k):
        return self.n+k

a = Adder(5)
print(a(4))
print("***********************")


#泛型函数
#首先尝试构造一个有理数Rational的类：
from math import gcd
class Rational(Number):
    type_tag = ''
    def __init__(self, numer, denom):
        number = gcd(numer,denom)
        self.numer = numer //number
        self.denom = denom //number
    def add(self,other):
        return Rational(self.numer*other.denom+self.denom*other.numer,self.denom*other.denom)
    def mul(self,other):
        return Rational(self.numer*other.numer,self.denom*other.denom)
    def __repr__(self):
        return 'Rational({0},{1})'.format(self.numer,self.denom)

print(Rational(2, 5) + Rational(1, 10))
print(Rational(1, 4) * Rational(2, 3))

#isinstace(object1,object2)函数为内建函数，输出bool值，判断object1是否是object2的子类
c = ComplexRI(1,1)
print(isinstance(c,ComplexRI))
print(isinstance(c,Complex))
print(isinstance(c,ComplexMA))

def is_real(c):
    if isinstance(c,ComplexRI):
        return c.real==0
    if isinstance(c,ComplexMA):
        return c.angle %pi ==0
print(is_real(ComplexRI(1,1)))
print(is_real(ComplexMA(2,pi)))

#泛型（第一种情况：类型调度（Type dispatching））
print("***********************")
Rational.type_tag = 'rat'
Complex.type_tag = 'com'
print(Rational(2,5).type_tag == Rational(1,2).type_tag)
print(ComplexRI(2,5).type_tag == ComplexMA(1,2).type_tag)
print(Rational(2,5).type_tag == ComplexRI(1,2).type_tag)


print("***********************")
print(ComplexRI(1.5,0)+Rational(3,2))
print(Rational(-1,2)*ComplexMA(4,pi/2))


#泛型（第二种情况：强制转换）：
#对class Number进行强制转换的重写(此文件最上方class Number中注释的一部分)：
print("***********************")
print(ComplexRI(1.5,0)+Rational(3,2))













































