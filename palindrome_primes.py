import first
from first import is_prime
from first import my_reverse

output = []
n = 99999

while n > 10000:
    if is_prime(n) and str(n)[0] == str(n)[4] and str(n)[1] == str(n)[3]:
        output.append(n)
    n-=1

print(my_reverse(output))
