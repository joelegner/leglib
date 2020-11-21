"leglib math routines"

from util import almost_equal
import math

def fabsmax(list_of_values):
    "Returns the maximum absolute value of a list of values."
    return max([math.fabs(i) for i in list_of_values])


def roundsig(value, digits = 3):
    """Rounds a float value to the specified number of significant digits and
    returns the rounded value"""
    if value:
        order = int(math.floor(math.log10(math.fabs(value))))
        places = digits - order - 1
    else:
        places = 0
    if places > 0:
        return round(value, places)
    else:
        fmtstr = "%.0f"
        return float("%.0f" % (round(value, places)))

