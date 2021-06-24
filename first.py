import math

# 1. is_even assignment
# 2. solve_quadratic assignment

def is_even(x):
    if (x % 2) == 1:
        return False
    else:
        return True

def solve_quadratic(a,b,c):
    if math.pow(b,2) >= (4 * a * c):
        x = (-b + math.sqrt(math.pow(b,2) - 4 * a * c))/2
        y = (-b - math.sqrt(math.pow(b,2) - 4 * a * c))/2
        if (x != y):
            return (x,y)
        else:
            return x
    else:
        return None