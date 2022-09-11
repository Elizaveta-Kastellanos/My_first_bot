import Logger 
import re


def frm_value(num_str):
    if num_str.find(',') != -1:
        num_str = re.sub(",",".",num_str)
    return num_str

def check_answer_calc(num):
    if float(num) == int(num):
        return int(num)
    else:
        num = ('{:.3f}'.format(num))
        return float(num)



def calc(num_str,firstname,lastname):

    try:
        num_str = frm_value(num_str)
        if num_str.find('+') != -1:
            a = float(num_str[0:num_str.find('+'):])
            b = float(num_str[num_str.find('+') + 1::])
            num = a + b
            answer = check_answer_calc(num)
            write_loger(answer, num_str,firstname,lastname)
            return answer
        elif num_str.find('-') != -1:
            a = float(num_str[0:num_str.find('-'):])
            b = float(num_str[num_str.find('-') + 1::])
            num = a - b
            answer = check_answer_calc(num)
            write_loger(answer, num_str, firstname,lastname)
            return answer
        elif num_str.find('*') != -1:
            a = float(num_str[0:num_str.find('*'):])
            b = float(num_str[num_str.find('*') + 1::])
            num = a * b
            answer = check_answer_calc(num)
            write_loger(answer, num_str, firstname,lastname)
            return answer
        elif num_str.find('/') != -1:
            a = float(num_str[0:num_str.find('/'):])
            b = float(num_str[num_str.find('/') + 1::])
            if b == 0:
                return 'На 0 делить нельзя'
            num = a / b
            answer = check_answer_calc(num)
            write_loger(answer, num_str, firstname,lastname)
            return answer
    except ValueError:
        return 'Упс, что-то пошло не так. Попробуй еще раз;)'
        
    
def write_loger(answer,num_str,firstname,lastname):
    answer_str = f'{firstname} {lastname}: {num_str} = {answer}'
    Logger.answer_logger(answer_str)
    
