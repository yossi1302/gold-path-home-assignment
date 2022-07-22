import math
from numpy import arctan
from scipy import constants

# I infered that the stike height is always y1 = 0

g = constants.g

def calc(v0, alpha, h):
    t1 = ((2 * v0 * math.sin(math.radians(alpha))) + math.sqrt(math.pow(-2 *
          v0 * math.sin(math.radians(alpha)), 2) + 8 * g * h))/(2 * g)
    t2 = ((2 * v0 * math.sin(math.radians(alpha))) - math.sqrt(math.pow(-2 *
          v0 * math.sin(math.radians(alpha)), 2) + 8 * g * h))/(2 * g)
    t = max(t1, t2)
    vx = v0 * math.cos(math.radians(alpha))
    x = vx * t
    vy = v0 * math.sin(math.radians(alpha)) - (g * t)
    v = math.sqrt(math.pow(vx, 2) + math.pow(vy, 2))
    alpha1 = arctan(vy / vx)
    output = {
        'Hit distance': x, 'Hit height': 0, 'Hit velocity': v, 'Hit angles': math.degrees(alpha1)
    }
    return output


if __name__ == "__main__":
    print(calc(10, 45, 20))
