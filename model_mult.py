from fractions import Fraction

x = 0
y = 0

def init (a,b):
    global x
    global y
    x = Fraction(a)
    y = Fraction(b)
# init(11,12)

# print(x)
# print(y)
def do_it():
    return x * y

