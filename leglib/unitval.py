"""
This module provides the Length class which keeps track of units for you.

>>> A = Length(12.875, feet)
>>> B = Length(9.5, inch)
>>> C = Length(180.75, feet)
>>> print(A)
12.88 ft
>>> print(B)
9.500 in
>>> print(C)
180.8 ft
>>> print(A+B)
13.67 ft
>>> print(C + 5.0)
185.8 ft
>>> print(C + 15)
195.8 ft
>>> print(15 + C)
195.8 ft
>>> print(5*A)
64.38 ft
>>> print(A*B)
611.6 ft^2
>>> A=A*B
>>> print(A*A)
33750000 ft^6
"""
import fmt
from decimal import *

getcontext().prec=5

class LengthUnit:
    def __init__(self, abbr, ratio):
        self.abbr = abbr
        self.ratio = Decimal(ratio)

inch = LengthUnit(abbr="in", ratio=25.4)
inches = inch
foot = LengthUnit(abbr="ft", ratio=25.4*12.0)
feet = foot

class Length:
    def __init__(self, value=1.0, unit=inch):
        self.value = Decimal(value)
        self.unit = unit
        self.power = 1

    def __str__(self):
        _val = fmt.sigdig(self.value, 4)
        if self.power > 1:
            return f"{_val} {self.unit.abbr}^{self.power}"
        else:
            return f"{_val} {self.unit.abbr}"

    def __add__(self, other):
        if type(other)==Length:
            assert other.power == self.power
            newval = (self.value*self.unit.ratio + other.value*other.unit.ratio)/self.unit.ratio
        elif type(other)==float:
            newval = (self.value + Decimal.from_float(other))
        else:
            newval = self.value + other
        return Length(value=newval, unit=self.unit)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if type(other)==Length:
            self.value = self.value*other.value
            self.power += other.power
        else:
            self.value = self.value*other
        return self

    def __rmul__(self, other):
        return self*other



if __name__ == "__main__":
    A = Length(12.875, feet)
    B = Length(9.5, inch)
    C = Length(180.75, feet)
    print(A)
    print(B)
    print(C)
    print(A+B)
    print(C + 5.0)
    print(C + 15)
    print(15 + C)
    print(5*A)
    print(A*B)
    A=A*B
    print(A*A)
