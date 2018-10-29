from leglib.structural.driftcalc import DriftCalc

# Create the calc instance
calc = DriftCalc(
        pg=70.0,                # ground snow load, psf
        lu=230,                 # tributary length of roof, feet
        hc=7.0,                 # height of obstruction, feet
        Ce=1.1,                 # exposure coefficient
        Ct=1.0,                 # thermal coefficient
        I=1.1,                  # importance factor
        is_leeward=False,       # True if leeward, False if windward
        project_number="198801125",
        project="7 Hazen Dr Cooling Tower",
        title="Drift Against Parapet",
        by="J. Legner")

# Creating the calc will run recalc() automatically to give results
# If you change a variable, you can explicitly run recalc() again
calc.pg = 75.0
calc.recalc()

# Call render to produce the report as a unicode string
print calc.render("txt")

