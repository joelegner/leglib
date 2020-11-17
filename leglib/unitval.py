import fmt
from decimal import *

getcontext().prec=5

class LengthUnit:
    def __init__(self, name, abbr, millimeters):
        self.name = name
        self.abbr = abbr
        self.millimeters = Decimal(millimeters)

inch = LengthUnit(name="inch", abbr="in", millimeters=25.4)
inches = inch
foot = LengthUnit(name="foot", abbr="ft", millimeters=25.4*12.0)
feet = foot

class Length:
    def __init__(self, value=1.0, unit=inch):
        self.value = Decimal(value)
        self.unit = unit

    def __str__(self):
        _val = fmt.sigdig(self.value, 4)
        return f"{_val} {self.unit.abbr}"

    def __add__(self, other):
        if type(other)==Length:
            newval = (self.value*self.unit.millimeters + other.value*other.unit.millimeters)/self.unit.millimeters
        elif type(other)==float:
            newval = (self.value + Decimal.from_float(other))
        else:
            newval = self.value + other
        return Length(value=newval, unit=self.unit)

    def __radd__(self, other):
        return self + other

if __name__ == "__main__":
    A = Length(12.875, feet)
    B = Length(9.5, inch)
    C = Length(180.75, feet)
    print(A)
    print(B)
    print(A+B)
    print(B+A)
    print(C)
    print(C + 5.0)
    print(C + 15)
    print(15 + C)
