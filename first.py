import math

# 1. is_even 
# 2. solve_quadratic 
# 3. to_hex
# 4. hex_code
# 5. my_range
# 6. my_reverse
# 7. big_fibonacci

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

hexidecimal_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

def to_hex(n):
    if (n // 16) > 0:
        remainder_1 = n % 16
        remainder_2 = (n // 16) % 16
        return hexidecimal_list[remainder_2] + hexidecimal_list[remainder_1]
    else: 
        return hexidecimal_list[n]

def hex_code(red,green,blue):
    if (red < 16):
        hex_r = '0' + to_hex(red)
    else:
        hex_r = to_hex(red)
    if (green < 16):
        hex_g = '0' + to_hex(green)
    else:
        hex_g = to_hex(green)
    if (blue < 16):
        hex_b = '0' + to_hex(blue)
    else:
        hex_b = to_hex(blue)
    return '#' + hex_r + hex_g + hex_b

def my_range(m,n):
    output = []
    while m < n:
        output.append(m)
        m+=1
    return output

def my_reverse(l):
    i = len(l) - 1
    output = []
    while i >= 0:
        output.append(l[i])
        i-=1
    return output

def big_fibonacci(n):
    loop = True
    fib1 = 1
    fib2 = 1
    while loop:
        num_digits = len(str(fib2))
        if n == num_digits:
            return fib2
            loop = False
        else:
            place_holder = fib2
            fib2 = fib1 + fib2
            fib1 = place_holder






