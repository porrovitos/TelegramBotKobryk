import telebot
from telebot.types import Message
from Game_engine import pile_of_stones, take_from_pile, game_over, get_pile, AI_bot

TOKEN = '1383178053:AAFaN0B0pzVp0bA73BJYj4UGgcm0iezIsYo'
bot = telebot.TeleBot(TOKEN)

pile_of_stones()
user = 1


@bot.message_handler(commands=['help'])
def about_game():
    pass


@bot.message_handler(commands=['start_play'])
def game_stat(message: Message):
    global chat_id, f
    f = message.text
    chat_id = message.chat.id
    bot.send_message(message.chat.id, 'Текущие позиции камней')
    k = str(get_pile())
    bot.send_message(message.chat.id, k)
    bot.send_message(message.from_user.id, 'Откуда берем камни?')
    bot.register_next_step_handler(message, get_pos)


def get_pos(message):
    global pos
    pos = message.text
    bot.send_message(message.chat.id, 'pos:')
    bot.send_message(message.chat.id, pos)
    bot.send_message(message.chat.id, 'Сколько берем?')
    bot.register_next_step_handler(message, get_qua)


def get_qua(message):
    global qua, k
    qua = message.text
    bot.send_message(message.chat.id, 'qua:')
    bot.send_message(message.chat.id, qua)
    take_from_pile(possition=int(pos), quantity=int(qua))
    game_over_test(message=message)


def game_over_test(message):
    if game_over():
        bot.send_message(message.chat.id, 'Конец игры. Выйграл игрок под номером {}'.format(user))
    else:
        bot.send_message(message.chat.id, 'Ход искуственного интеллекта')
        AI_bot()
        if game_over():
            bot.send_message(message.chat.id, 'Конец игры. Выйграл игрок под номером {}'.format(user))
        else:
            game_stat(message=message)


bot.polling()
