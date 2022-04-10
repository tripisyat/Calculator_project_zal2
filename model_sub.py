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
    res=x-y
    log.log_model_sub(res) # обращаемся к модулю логирования и функции которая логирует умножение. Передаем этой функции полученный результат
    return res