# LegLib

Leglib is just a bunch of utility modules that I wrote and like to use. One very handy one is a rounding function that rounds to significant digits: `leglib.fmt.sigdig`.

Source: <https://github.com/joelegner/leglib>

## Installation

```zsh
$ pipenv install leglib
```

## Using

```python
>>> from leglib.fmt import sigdig
>>> sigdig(3.843718473821748732184732)
'3.84'
>>> sigdig(3.843718473821748732184732, 5)
'3.84372'
```

## Testing

```bash
$ make test
```

## UnitVal

The UnitVal class represents an engineering quantity with units of either force, distance, or both. It is primarily intended for use in structural engineering applications but could later be extended to other knowledge areas.

> Important: Default units are **inches** for length and **pounds** for force.

Here are some usage examples. Let's initialize two variables: a distance and a force.

```python
>>> L = 42.0*inches
>>> P = 21.4*kips
>>> print(L)
42.000 in
>>> print(P)
21.400 k
```

Now we can calculate the moment which is the force applied over the distance.

``` python
>>> print(P*L)
898.80 k-in
```

When units are inconsistent between two variables, UnitVal resolves the conflict by retaining the units of the left-hand side of the expression. So if we reverse `P*L` to `L*P`, we get a different result.

```python
>>> print(L*P)
898800 lb-in
```

The fact that UnitVal converted the result to inches may not seem intuitive unless you understand that the _default_ units are pounds and inches. Thus, when we assigned `P = 21.4*kips` the UnitVal instance `P` had its units set to kips explicitly and inches by default.

You can multiply a UnitVal by a float, integer, or Decimal scalar.

```python
>>> print(L*P*0.5)
449400 lb-in
```

UnitVal keeps track of the exponents of its two unit types (distance and force) so that we can calculate areas, for example.

```python
>>> print(L*L)
1764.0 in^2
```

UnitVal will substitute psf, psi, ksi, Pa, kPa, MPa, etc. for the appropriate combination of units. For example, it replaces `lb/ft^2` with `psf`, which means "pounds per square foot." Division works as expected.

```python
>>> B = 17.5*feet
>>> A = B*L
>>> Q = P/A
>>> print(Q)
349.39 psf
```

You can also change the units of a UnitVal instance by passing the units you want to change to.

```python
>>> L = 24.5*feet
>>> L.change_units(inches)
>>> print(L)
294.00 in
```

Units can be changed to the special aggregate units too (psi, ksi, kPa, etc.).

```python
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
"""
