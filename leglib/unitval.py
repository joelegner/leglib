"""
This module provides the UnitVal class which keeps track of units for you.

>>> A = 12.875*feet
>>> B = 9.5*inches
>>> C = 180.75*feet
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
>>> L = 42*inches
>>> print(L)
42.00 in
"""
import fmt
from decimal import *

DIGITS = 5
getcontext().prec=DIGITS

force_units = {
    "lb" : Decimal(1.0),
    "k" : Decimal(1000.0),
    "N" : Decimal(0.22480894244319),
    "kN" : Decimal(224.80894387096),
}

length_units = {
    "in" : Decimal(1.0),
    "ft" : Decimal(12.0),
    "mm" : Decimal(1/25.4),
    "m" : Decimal(1/25.4*1000.0),
}


class UnitVal:
    def __init__(self, value, power, unitnames):
        assert type(power)==list
        assert type(value)==Decimal
        self.value = Decimal(value)
        self.power = power
        self.unitnames = unitnames

    def __str__(self):
        _val = self.value/(length_units[self.unitnames[0]]**self.power[0]*force_units[self.unitnames[1]]**self.power[1])
        _val = fmt.sigdig(_val, DIGITS)
        return f"{_val} {self._abbr()}"

    def normalize(self):
        "Return normalized value considering ratios and powers"
        lrat, lpow = length_units[self.unitnames[0]], self.power[0]
        frat, fpow = force_units[self.unitnames[1]], self.power[1]
        return self.value*(Decimal(lrat)**lpow)*(Decimal(frat)**fpow)

    def __mul__(self, other):
        if isinstance(other, UnitVal):
            # First normalize the value to inches, pounds
            value = self.value*other.value
            power = [self.power[i] + other.power[i] for i in (0, 1)]
            unitnames = [self.unitnames[i] for i in (0, 1)]
            
        elif type(other) in (float, int, Decimal):
            value = self.value*Decimal(other)
            power = self.power
        else:
            raise ValueError(f"type(other)={type(other)} not permitted. Use float, integer, or Decimal.")
        unitnames = self.unitnames
        return UnitVal(value=value, power=power, unitnames=self.unitnames)

    def __rmul__(self, other):
        return self.__mul__(other)

    def _abbr(self):
        dabbr = self._abbr_dist()
        fabbr = self._abbr_force()
        if len(dabbr) and len(fabbr):
            return fabbr + "-" + dabbr
        else:
            return fabbr + dabbr

    def _abbr_dist(self):
        p = self.power[0]
        if p == 0:
            return ""
        elif p == 1:
            return self.unitnames[0]
        else:
            return f"{self.unitnames[0]}^{p}"

    def _abbr_force(self):
        p = self.power[1]
        if p == 0:
            return ""
        elif p == 1:
            return self.unitnames[1]
        else:
            return f"{self.unitnames[1]}^{p}"
        


# Base unit for length is the inch
inches = UnitVal(value=Decimal(1.0), unitnames=("in", "lb"), power=[1, 0])
feet = UnitVal(value=Decimal(12.0), unitnames=("ft", "lb"), power=[1, 0])

# Base unit for force is the pound
pounds = UnitVal(value=Decimal(1.0), unitnames=("ft", "lb"), power=[0, 1])
kips = UnitVal(value=Decimal(1000.0), unitnames=("in", "k"), power=[0, 1])

if __name__ == "__main__":
    L = 42.0*inches
    P = 21.4*kips
    print(L)
    print(P)
    print(P*L)
    print(L*P)
    print(L*P*0.5)
    print(L*L)
    B = 17.5*feet
    print(B*B)
    print((B*B).value)