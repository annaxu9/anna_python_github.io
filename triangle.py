import math

class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a  + self.b + self.c

    def area(self):
        return math.sqrt((self.perimeter() / 2) * ((self.perimeter() / 2) - self.a) * ((self.perimeter() / 2) - self.b) * ((self.perimeter() / 2) - self.c))

    def scale(self, scale_factor):
        return Triangle(scale_factor * self.a, scale_factor * self.b, scale_factor * self.c)

    def is_valid(self):
        if (self.a + self.b) > self.c and (self.c + self.b) > self.a and (self.a + self.c) > self.b:
            return True
        else:
            return False

    def is_right(self):
        if (math.pow(self.a, 2) + math.pow(self.b, 2) == math.pow(self.c, 2)) or (math.pow(self.c, 2) + math.pow(self.b, 2) == math.pow(self.a, 2)) or (math.pow(self.a, 2) + math.pow(self.c, 2) == math.pow(self.b, 2)):
            return True
        else: 
            return False


"""""
t = Triangle(3,4,5)

print("Area = %d" % t.area())
print("Perimeter = %d" % t.perimeter())
q = t.scale(3)
print(q.a, q.b, q.c)

print("Triangle? %r" % t.is_valid())
print("Right? %r" % t.is_right())

"""
