from datetime import datetime as dt
import model_mult  # импортируем модуль умножения
import model_div # импортируем модуль деления
import model_sum # импортируем модуль сложения
import model_sub # импортируем модуль вычитания

def log_model_mult(result): #описываем логирование в файл результатов умножения   
    time = dt.now().strftime('%H:%M')# получаем время начала операции
    first_value = model_mult.x # первое введенное значение
    second_value = model_mult.y # второе введенное значение
    with open('log.cvs', 'a') as file: #открываем/создаем файл log.cvs
        file.write('{} first_value = {}; second_value = {}; multy = {}\n' # записываем в файл в таком формате
                    .format(time, first_value, second_value, result)) # порядок переменных в строчке выше

def log_model_div(result): #описываем логирование в файл результатов деления
    time = dt.now().strftime('%H:%M')
    first_value=model_div.x
    second_value=model_div.y
    with open('log.cvs', 'a') as file: 
        file.write('{} first_value = {}; second_value = {}; division = {}\n'
                    .format(time, first_value, second_value, result))
                    
def log_model_sum(result):   #описываем логирование в файл результатов сложения
    time = dt.now().strftime('%H:%M')
    first_value = model_sum.x 
    second_value = model_sum.y
    with open('log.cvs', 'a') as file: 
        file.write('{} first_value = {}; second_value = {}; sum = {}\n'
                    .format(time, first_value, second_value, result))

def log_model_sub(result):   #описываем логирование в файл результатов вычитания
    time = dt.now().strftime('%H:%M')
    first_value = model_sub.x 
    second_value = model_sub.y
    with open('log.cvs', 'a') as file: 
        file.write('{} first_value = {}; second_value = {}; subtraction = {}\n'
                    .format(time, first_value, second_value, result))