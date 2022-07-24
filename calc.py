import math
from numpy import arctan
from scipy import constants

# I infered that the stike height is always y1 = 0

g = constants.g
# The method gets the starting velocity, starting angale and starting height and returns the hit distance, hit height, hit velocity and hit angale as a dict


def calc(v0, alpha, h):
    # first option of answer for the quadratic equation
    t1 = ((2 * v0 * math.sin(math.radians(alpha))) + math.sqrt(math.pow(-2 *
          v0 * math.sin(math.radians(alpha)), 2) + 8 * g * h))/(2 * g)
    # second option of answer for the quadratic equation
    t2 = ((2 * v0 * math.sin(math.radians(alpha))) - math.sqrt(math.pow(-2 *
          v0 * math.sin(math.radians(alpha)), 2) + 8 * g * h))/(2 * g)
    # finding the bigger answer
    t = max(t1, t2)
    # horizontal velocity
    vx = v0 * math.cos(math.radians(alpha))
    # distance
    x = vx * t
    # vertical velocity
    vy = v0 * math.sin(math.radians(alpha)) - (g * t)
    # velocity at the hit
    v = math.sqrt(math.pow(vx, 2) + math.pow(vy, 2))
    # hit angle
    alpha1 = arctan(vy / vx)
    # dict to return
    output = {
        'Hit distance': x, 'Hit height': 0, 'Hit velocity': v, 'Hit angle': math.degrees(alpha1)
    }
    return output
