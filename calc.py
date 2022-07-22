import math
from numpy import arctan
from scipy import constants
import json


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
    print(vy / vx)
    output_dict = {
        "x1": x,
        "y1": 0,
        "v1": v,
        "alpha1": math.degrees(alpha1)
    }
    output_json = json.dumps(output_dict)
    return output_json


if __name__ == "__main__":
    print(calc(10, 45, 20))
