from fractions import Fraction

x = 0
y = 0

def init (a,b):
    global x
    global y
    x = Fraction(a)
    y = Fraction(b)

def do_it():
    return x + y