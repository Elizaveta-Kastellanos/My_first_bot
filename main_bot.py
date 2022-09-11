import telebot
from telebot import types
import config
from Model_logic import calc
from exchange_methods import *

bot = telebot.TeleBot(config.token)
# command /start

num_user_str = ''

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
    exg = get_exchange()
    mess = f'Сейчас я открою сайт курса валют и выведу тебе курс евра и доллара:)))\nUSD: {exg[0]}\nEUR: {exg[1]}'
    bot.send_message(msg.chat.id, mess)

@bot.message_handler(commands=["help"])
def exchange(msg):
    mess = f'Я покажу тебе, все, что я могу.А могу, я очень мало:(((\nТы не обижайся, ведь, я только учусь\nЛови команды\n/calc\n/start\n/exchange'
    bot.send_message(msg.chat.id, mess)

bot.polling(none_stop=True)

