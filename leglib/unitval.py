"""
This module provides the UnitVal class which keeps track of units for you.

>>> L = 42.0*inches
>>> P = 21.4*kips
>>> print(L)
42.000 in
>>> print(P)
21.400 k
>>> print(P*L)
898.80 k-in
>>> print(L*P)
898800 lb-in
>>> print(L*P*0.5)
449400 lb-in
>>> print(L*L)
1764.0 in^2
>>> B = 17.5*feet
>>> A = B*L
>>> Q = P/A
>>> print(Q)
349.39 psf
>>> w = 4.5*kips/(18.3*feet)
>>> print(w)
245.90 plf
>>> L = 24.5*feet
>>> W = w*L
>>> print(W)
6024.6 lb
>>> W.unitnames[1] = "k"
>>> print(W)
6.0246 k
>>> L.change_units(inches)
>>> print(L)
294.00 in
>>> pressure = 1000.0*psi
>>> print(pressure)
1000.0 psi
>>> pressure.change_units(kilonewtons)
>>> print(pressure)
6894.6 kPa
>>> stress = 60*ksi
>>> print(stress)
60.000 ksi
>>> stress.change_units(megapascals)
>>> print(stress)
413.68 MPa
>>> # Try dividing by an integer and float
>>> print(pressure/2)
3447.3 kPa
>>> print(pressure/2.0)
3447.3 kPa
>>> L1 = 36.5*inches
>>> L2 = 1.75*feet
>>> # Test addition
>>> print(L1 + L2)
57.500 in
>>> print(bool(L1))
True
>>> print(L1 != L2)
True
>>> print(L1 == L2)
False
>>> print(L1 < L2)
False
>>> print(L1 > L2)
True
>>> L3 = 0*inches
>>> print(bool(L3))
False
>>> area = L2**2
>>> print(area)
3.0625 ft^2
>>> L3 = area**(0.5)        # square root of area is length
>>> print(L3)
1.7500 ft
"""
import fmt
import math
from decimal import *
from typing import List

DIGITS = 5
getcontext().prec = DIGITS

force_units = {
    "lb": Decimal(1.0),
    "k": Decimal(1000.0),
    "N": Decimal(0.22480894244319),
    "kN": Decimal(224.80894387096),
    "MN": Decimal(1000.0*224.80894387096),
}

length_units = {
    "in": Decimal(1.0),
    "ft": Decimal(12.0),
    "mm": Decimal(1/25.4),
    "m": Decimal(1/25.4*1000.0),
}

special_units = {
    "lb/ft^2": "psf",
    "lb/ft": "plf",
    "k/ft^2": "ksf",
    "k/ft": "klf",
    "lb/in^2": "psi",
    "k/in^2": "ksi",
    "kN/m^2": "kPa",
    "MN/m^2": "MPa",
}


class UnitVal:
    def __init__(self, value, power: List[int], unitnames: List[str]):
        assert type(power) == list
        assert type(value) == Decimal
        self.value = Decimal(value)
        self.power = power
        self.unitnames = unitnames

    def __str__(self):
        _val = self.value/(length_units[self.unitnames[0]]**self.power[0]
                           * force_units[self.unitnames[1]]**self.power[1])
        _val = fmt.sigdig(_val, DIGITS)
        return f"{_val} {self._abbr()}"

    def normalize(self):
        "Return normalized value considering ratios and powers"
        lrat, lpow = length_units[self.unitnames[0]], self.power[0]
        frat, fpow = force_units[self.unitnames[1]], self.power[1]
        return self.value*(Decimal(lrat)**lpow)*(Decimal(frat)**fpow)

    def change_units(self, other):
        assert hasattr(other, "unitnames")
        self.unitnames = tuple(other.unitnames)

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
            raise ValueError(
                f"type(other)={type(other)} not permitted. Use float, integer, or Decimal.")
        unitnames = self.unitnames
        return UnitVal(value=value, power=power, unitnames=self.unitnames)

    def __truediv__(self, other):
        unitnames = self.unitnames
        if isinstance(other, UnitVal):
            # First normalize the value to inches, pounds
            value = self.value/other.value
            power = [self.power[i] - other.power[i] for i in (0, 1)]
            for i in (0, 1):
                if self.power[i] == i and not other.power[i] == i:
                    unitnames[i] = other.unitnames[i]
        elif type(other) in (float, int, Decimal):
            value = self.value/Decimal(other)
            power = self.power
        else:
            raise ValueError(
                f"type(other)={type(other)} not permitted. Use float, integer, or Decimal.")
        return UnitVal(value=value, power=power, unitnames=unitnames)

    def __add__(self, other):
        unitnames = self.unitnames
        if isinstance(other, UnitVal):
            # First normalize the value to inches, pounds
            assert other.power == self.power
            return UnitVal(value=self.value+other.value, power=self.power, unitnames=self.unitnames)
        else:
            raise ValueError(
                f"Addition only permitted with other UnitVal instances having compatible units.")

    def __eq__(self, other):
        if isinstance(other, UnitVal):
            # First normalize the value to inches, pounds
            assert other.power == self.power
            return self.value == other.value
        else:
            return TypeError("Equality operator only works with two UnitVal instances")

    def __neq__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, UnitVal):
            # First normalize the value to inches, pounds
            assert other.power == self.power
            return self.value < other.value
        else:
            return TypeError("Comparison operators (<, <=, ==, >=, >) only work with two UnitVal instances")

    def __gt__(self, other):
        if isinstance(other, UnitVal):
            # First normalize the value to inches, pounds
            assert other.power == self.power
            return self.value > other.value
        else:
            return TypeError("Comparison operators (<, <=, ==, >=, >) only work with two UnitVal instances")

    def __rmul__(self, other):
        return self.__mul__(other)

    def _abbr(self):
        dabbr = self._abbr_dist()
        fabbr = self._abbr_force()
        if len(dabbr) and len(fabbr):
            if self.power[0] >= 1:
                retval = fabbr + "-" + dabbr
                retval = special_units.get(retval, retval)
            else:
                retval = fabbr + "/" + dabbr
                retval = special_units.get(retval, retval)
            return retval
        else:
            return fabbr + dabbr

    def _abbr_dist(self):
        p = abs(self.power[0])
        if p == 0:
            return ""
        elif p == 1:
            return self.unitnames[0]
        else:
            return f"{self.unitnames[0]}^{p}"

    def _abbr_force(self):
        p = abs(self.power[1])
        if p == 0:
            return ""
        elif p == 1:
            return self.unitnames[1]
        else:
            return f"{self.unitnames[1]}^{p}"

    def __bool__(self):
        return bool(self.value)

    def __pow__(self, other):
        value = self.value**Decimal(other)
        power = [int(p*other) for p in self.power]
        unitnames = self.unitnames
        return UnitVal(value=value, power=power, unitnames=unitnames)


# Base unit for length is the inch
inches = UnitVal(value=Decimal(1.0), unitnames=["in", "lb"], power=[1, 0])
feet = UnitVal(value=Decimal(12.0), unitnames=["ft", "lb"], power=[1, 0])
mm = UnitVal(value=Decimal(1.0/25.4), unitnames=["mm", "N"], power=[1, 0])
m = UnitVal(value=Decimal(1000.0*1.0/25.4), unitnames=["m", "N"], power=[1, 0])

# Base unit for force is the pound
pounds = UnitVal(value=Decimal(1.0), unitnames=["ft", "lb"], power=[0, 1])
kips = UnitVal(value=Decimal(1000.0), unitnames=["in", "k"], power=[0, 1])
newtons = UnitVal(value=Decimal(0.2248089), unitnames=["m", "N"], power=[0, 1])
kilonewtons = UnitVal(value=Decimal(1000.0*0.2248089),
                      unitnames=["m", "kN"], power=[0, 1])
meganewtons = UnitVal(value=Decimal(1000000.0*0.2248089),
                      unitnames=["m", "MN"], power=[0, 1])

# Base unit for pressure unit is derived from the above as pounds per square inch, psi.
psi = UnitVal(value=Decimal(1.0), unitnames=["in", "lb"], power=[-2, 1])
ksi = UnitVal(value=Decimal(1000.0), unitnames=["in", "k"], power=[-2, 1])
kilopascals = UnitVal(value=Decimal(0.1450377), unitnames=[
                      "m", "kN"], power=[-2, 1])
megapascals = UnitVal(value=Decimal(1000.0*0.1450377),
                      unitnames=["m", "MN"], power=[-2, 1])
