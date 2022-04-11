from numbers import Complex
from numbers import Number
import logger as log # импортируем модуль логирования

x = 0
y = 0

def init (a,b):
    global x
    global y
    x = a
    y = b

def do_it():
    res = x / y
    log.log_model_div(res) # обращаемся к модулю логирования и функции которая логирует умножение. Передаем этой функции полученный результат
    return res