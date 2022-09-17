import Logger


def game_field():
   mas_game = f'_1_2_3_\n_4_5_6_\n_7_8_9_'
   return mas_game


def process_game(field,num, how_walks):
   mas_game = field
   sign_x = 'X'
   sign_o = 'O'
   if how_walks == 1:
      if mas_game.find(num) != -1:
         mas_game = mas_game.replace(num, sign_x)
         return mas_game
   elif how_walks == 2:
      if mas_game.find(num) != -1:
         mas_game = mas_game.replace(num, sign_o)
         return mas_game

def check_win(field, user_name):
   mas_game = field.split(f'\n')
   sign_x = 'X'
   sign_o = 'O'
   for i in range(len(mas_game)):
      tmp = str(mas_game[i])
      if tmp.count('X') == 3:
         Logger.game_tik_logger(f'Победил {sign_x} он же {user_name}')
         return sign_x
      elif tmp.count('O') == 3:
         Logger.game_tik_logger(f'Победил {sign_o} он же {user_name}')
         return sign_o
   if mas_game[0][1] == mas_game[1][1] == mas_game[2][1]:
      Logger.game_tik_logger(f'Победил {mas_game[0][1]} он же {user_name}')
      return mas_game[0][1]
   if mas_game[0][3] == mas_game[1][3] == mas_game[2][3]:
      Logger.game_tik_logger(f'Победил {mas_game[0][3]} он же {user_name}')
      return mas_game[0][3]
   if mas_game[0][5] == mas_game[1][5] == mas_game[2][5]:
      Logger.game_tik_logger(f'Победил {mas_game[0][5]} он же {user_name}')
      return mas_game[0][5]
   if mas_game[0][1] == mas_game[1][3] == mas_game[2][5]:
      Logger.game_tik_logger(f'Победил {mas_game[0][1]} он же {user_name}')
      return mas_game[0][1]
   if mas_game[0][5] == mas_game[1][3] == mas_game[2][1]:
      Logger.game_tik_logger(f'Победил {mas_game[0][5]} он же {user_name}')
      return mas_game[0][5]
      
        
      

   # print(mas_game)

# print(check_win(f'_1_2_3_\n_4_5_6_\n_7_8_9_'))

# field = list(range(1,10))

# def Draw_and_refresh_field():
#    global field
#    stroka = ''
#    print('\n')
#    for i in range(3):
#       stroka = (f'{field[0+i*3]} | {field[1+i*3]} | {field[2+i*3]}')
#       if i != 2:
#         stroka = stroka + ('-' * 10)
#       else:
#         stroka = stroka + ('\n')
#     return stroka
    
      
        
# def Answer_player(x_or_o):
#    check = False
#    while not check:
#       player_answer = input(f'Куда поставим {x_or_o}: ')
#       try:
#             player_answer = int(player_answer) 
#       except:
#          print('Попробуй еще раз ввести целое число: ')
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(field[player_answer-1]) not in "XO"):
#             field[player_answer-1] = x_or_o
#             check = True
#          else:
#             print('Эта клетка уже занята.Будь внимательней!')

# def Win():
#    global field
#    winning_values = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for cell in winning_values:
#        if field[cell[0]] == field[cell[1]] == field[cell[2]]:
#           return field[cell[0]]
#    return False

# def Game_tic_tac_toe():
#    global field
#    move = 0
#    count = 0
#    win = False
#    while not win:
#         Draw_and_refresh_field()
#         if move == 0:
#            Answer_player('X')
#            move = 1
#            count += 1
#         else:
#            Answer_player('O')
#            move = 0
#            count += 1
#         if count > 4:
#            Draw_and_refresh_field()
#            tmp = Win()
#            if tmp:
#               win = True
#               return ('ВЫИГРАЛ: ', tmp)
#               break
#         if count == 9:
#             return 'ПОБЕДИЛА ДРУЖБА'
#             break

# Game_tic_tac_toe()