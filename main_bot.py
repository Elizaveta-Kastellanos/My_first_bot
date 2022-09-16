from ctypes import sizeof
import telebot
from telebot import types
import config
from Model_logic import calc
import exchange_methods 
import game_Tic
import time

bot = telebot.TeleBot(config.token)
# command /start

num_user_str = ''
paint_field = f'_1_2_3_\n_4_5_6_\n_7_8_9_'
count = ['1','2','3','4','5','6','7','8','9']


@bot.message_handler(commands=["start"]) 
def start_command(msg):
    butt = types.ReplyKeyboardRemove(selective=False)
    mess = f'Приветуствую тебя, {msg.from_user.first_name} {msg.from_user.last_name}'
    bot.send_message(msg.chat.id, mess, reply_markup=butt)
    

@bot.message_handler(commands=["calc"])
def calc_command(msg):
    butt = types.ReplyKeyboardRemove(selective=False)
    mess = f'Я простой калькулятор\nВведите выражение - Пример: 10+20, 30/10 и т.д.)'
    msg2 = bot.send_message(msg.chat.id, mess, reply_markup=butt)
    bot.register_next_step_handler(msg2, get_value)

def get_value(msg, result = None):
    try:
        global num_user_str
        if result == None:
            num_user_str = msg.text
        else:
            num_user_str = msg.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Результат')
        markup.add(btn1)
        msg2 = bot.send_message(msg.chat.id, 'Сейчас, я покажу ответ)))Жмакай на кнопку', reply_markup=markup)
        bot.register_next_step_handler(msg2,step_for_calc)
    except ValueError:
        bot.reply_to(msg, 'Упс!(Что-то пошло не так(Попродуй еще раз!)')
    
def step_for_calc(msg):
    try:
        global num_user_str
        answer_user = calc(num_user_str, msg.from_user.first_name, msg.from_user.last_name)
        butt = types.ReplyKeyboardRemove(selective=False)
        if msg.text == 'Результат':
            bot.send_message(msg.chat.id, answer_print(answer_user), reply_markup=butt)
    except ValueError:
        bot.reply_to(msg, 'Упс!(Что-то пошло не так(Попродуй еще раз!)')

def answer_print(answer_user):
    global num_user_str
    return f'Результат: {num_user_str} = {answer_user}'

@bot.message_handler(commands=["exchange"])
def exchange(msg):
    exg = exchange_methods.get_exchange()
    mess = f'Сейчас я открою сайт курса валют и выведу тебе курс евра и доллара:)))\nUSD: {exg[0]}\nEUR: {exg[1]}'
    bot.send_message(msg.chat.id, mess)

@bot.message_handler(commands=["help"])
def exchange(msg):
    mess = f'Я покажу тебе, все, что я могу.А могу, я очень мало:(((\nТы не обижайся, ведь, я только учусь\nЛови команды\n/calc\n/start\n/exchange'
    bot.send_message(msg.chat.id, mess)

@bot.message_handler(commands=["Game"])
def start_game(msg):
    mess = f'Игра крестики нолики\n\n{game_Tic.game_field()}'
    bot.send_message(msg.chat.id, mess)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('1')
    btn2 = types.KeyboardButton('2')
    btn3 = types.KeyboardButton('3')
    btn4 = types.KeyboardButton('4')
    btn5 = types.KeyboardButton('5')
    btn6 = types.KeyboardButton('6')
    btn7 = types.KeyboardButton('7')
    btn8 = types.KeyboardButton('8')
    btn9 = types.KeyboardButton('9')
    markup1.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9)
    mess = 'Выбери куда поставишь X или О'
    msg2 = bot.send_message(msg.chat.id, mess, reply_markup=markup1)
    bot.register_next_step_handler(msg2, continuation_game)

    

def continuation_game(msg):
    global paint_field
    global count
    how_walks = 1
    pos = 9
    markup1 = types.ReplyKeyboardRemove(selective=False)
    ans = ['1','2','3','4','5','6','7','8','9']
    while pos >= 1:
        if how_walks == 1 or how_walks == 2:
            for i in range(len(ans)):
                if msg.text == ans[i] and how_walks == 1:
                    paint_field1 = game_Tic.process_game(paint_field,msg.text, how_walks)
                    paint_field = paint_field1
                    how_walks += 1
                    count = [x for x in count if x != msg.text]
                    bot.send_message(msg.chat.id, paint_field, reply_markup=markup1)
                    time.sleep(1)
                    pos -= 1
                    break
                elif msg.text == ans[i] and how_walks == 2:
                    paint_field1 = game_Tic.process_game(paint_field,msg.text, how_walks)
                    paint_field = paint_field1
                    how_walks -= 1
                    count = [x for x in count if x != msg.text]
                    bot.send_message(msg.chat.id, paint_field, reply_markup=markup1)
                    time.sleep(1)
                    pos -= 1
                    break
        markup1 = get_btn()
        mess = 'Выбери куда поставишь X или О'
        msg2 = bot.send_message(msg.chat.id, mess, reply_markup=markup1)
        msg3 = bot.send_message(msg2.chat.id, '')
        msg.text = msg3.text
    bot.send_message(msg.chat.id, 'Ничья')
    
def get_btn():
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    for i in range(len(count)):
            btn = types.KeyboardButton(count[i])
            markup1.add(btn)
    return markup1


# def cont_game(msg):
#     markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
#     btn1 = types.KeyboardButton('1')
#     btn2 = types.KeyboardButton('2')
#     btn3 = types.KeyboardButton('3')
#     btn4 = types.KeyboardButton('4')
#     btn5 = types.KeyboardButton('5')
#     btn6 = types.KeyboardButton('6')
#     btn7 = types.KeyboardButton('7')
#     btn8 = types.KeyboardButton('8')
#     btn9 = types.KeyboardButton('9')
#     markup1.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9)
#     mess = 'Выбери куда поставишь X или О'
#     bot.send_message(msg.chat.id, mess, reply_markup=markup1)
               

            

    

# def continuation_game(msg):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     btn1 = types.KeyboardButton('1')
#     btn2 = types.KeyboardButton('2')
#     btn3 = types.KeyboardButton('3')
#     btn4 = types.KeyboardButton('4')
#     btn5 = types.KeyboardButton('5')
#     btn6 = types.KeyboardButton('6')
#     btn7 = types.KeyboardButton('7')
#     btn8 = types.KeyboardButton('8')
#     btn9 = types.KeyboardButton('9')
#     markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9)
#     mess = 'Выбери куда поставишь X или О'
#     bot.send_message(msg.chat.id, mess, reply_markup=markup)


bot.polling(none_stop=True)

