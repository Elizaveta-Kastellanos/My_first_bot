from datetime import datetime as dt
from time import time 


def answer_logger(data):
    file_log_answer = 'answer1.txt'
    time = dt.now().strftime("%d/%m/%Y Time %H:%M")
    with open(file_log_answer, 'a') as file:
        file.write(f'{time} Answer = {data}\n')

# def data_logger(data):
#     file_data = 'answer_only.txt'
#     with open(file_data, 'w') as file:
#         file.write(str(data))

# def dive_data_with_log():
#     file_data = 'answer_only.txt'
#     with open(file_data, 'r') as file:
#         answer = file.read()
#     return answer