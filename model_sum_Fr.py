from fractions import Fraction
import logger as log # импортируем модуль логирования

x = 0
y = 0

def init (a,b):
    global x
    global y
    x = Fraction(a)
    y = Fraction(b)

def do_it():
    res = x+y
    log.log_model_sum(res)
    return res