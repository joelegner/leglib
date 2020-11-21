"""
Engineering math classes and functions
"""

import unitval


class EngVar:
    "Engineering variable with a value that is a UnitVal."

    def __init__(self, name, value):
        assert isinstance(value, unitval.UnitVal)
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name} = {self.value}"

    def name_as_latex(self):
        if "_" in self.name:
            base, subscript = self.name.split("_")
        else:
            base, subscript = self.name, ""
        if not len(subscript):
            return "%s" % (self.name)
        else:
            return "%s_{%s}" % (base, subscript)

    def value_as_latex(self):
        num, units = self.value.__str__().split(" ")
        if "^" in units:
            baseunit, superscript = units.split("^")
            return "%s \\text{ %s}^{%s}" % (num, baseunit, superscript)
        else:
            return "%s \\text{ %s}" % (num, units)

    def as_latex(self):
        return self.name_as_latex() + " = " + self.value_as_latex()


class Equation:

    def __init__(self, expression, latex):
        self.expression = expression
        self.latex = latex


if __name__ == "__main__":
    from unitval import inches, kips
    P = EngVar(name="P", value=21.5*kips)
    print(P)
    print(P.as_latex())

    Ab = EngVar("A_b", 0.44*inches*inches)
    print(Ab)
    print(Ab.as_latex())

    # Let's try some wishful thinking
    eq1 = Equation("(w*L**2)/8.0", r"\dfrac{w L^2}{8}"
    eq1.as_latex()
    eq1.as_latex_expand()
