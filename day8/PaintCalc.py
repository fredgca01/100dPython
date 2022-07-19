# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 ✖️ 4) ÷ 5 = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

import math


def nb_of_cans(height, width, coverage=5):
    nb = height*width/coverage
    print(f"You will need {math.ceil(nb)} paint cans")

nb_of_cans(2,4)
nb_of_cans(3,9)
nb_of_cans(3,9,2)