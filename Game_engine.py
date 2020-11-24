import time
from random import randint

_holder = []
MAX_PILE = 5
MAX_STONES = 20


def pile_of_stones():
    global _holder
    _holder = []
    for i in range(5):
        _holder.append(randint(1, MAX_STONES))


def take_from_pile(possition, quantity):
    global _holder
    if 1 <= possition <= len(_holder):
        if quantity > _holder[possition - 1]:
            print('Вы хотите забрать больше камней чем есть. Попробуйте еще раз')
            pos = input('Откуда берем камни?')
            qua = input('Сколько берем?')
            take_from_pile(possition=int(pos), quantity=int(qua))
        else:
            _holder[possition - 1] -= quantity


def get_pile():
    return _holder


def game_over():
    return sum(_holder) == 0


def AI_bot():
    global pos_AI, qua_AI
    pos_AI = randint(0, MAX_PILE) - 1
    if _holder[pos_AI] == 0:
        AI_bot()
    else:
        qua_AI = randint(1, _holder[pos_AI])
        _holder[pos_AI] -= qua_AI
        time.sleep(2)
        # if game_over():
            # @bot.message_handler(content_types=['text'])
            # def loos(message):
            #     bot.send_message(message.chat.id, 'Конец игры. Выйграл игрок под номером {}'.format(user))
