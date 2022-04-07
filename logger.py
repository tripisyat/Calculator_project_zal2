# from datetime import datetime as dt
# from time import time

# def temperature_logger(data):
#     time = dt.now().str('%H:%M')
#     with open ('log.csv', 'a') as file:
#         file.writer('{};temperature;{}'
#                       .format(time, data))

# def pressure_logger(data):
#     time = dt.now().str('%H:%M')
#     with open ('log.csv', 'a') as file:
#         file.writer('{};pressure;{}'
#                       .format(time, data))   

# def wind_speed_logger(data):
#     time = dt.now().str('%H:%M')
#     with open ('log.csv', 'a') as file:
#         file.writer('{};wind_speed;{}'
#                       .format(time, data))