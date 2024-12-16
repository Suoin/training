import telepot
from data import player
from scenario import *

def on_callback_query(msg):

    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
    chat_id = msg['message']['chat']['id']  # Получаем chat_id из исходного сообщения
    message_id = msg['message']['message_id']
    data = msg['data']
    #Обработчик для цели



    #Обрабатываем навигацию

    if data == 'right' or data == 'left':
        start_game_1(chat_id,message_id)
    elif data in callback_commands:
        callback_commands[data](chat_id,message_id,data)

    #Обрабатываем боевую систему

    else:
        bot.sendMessage(chat_id,'Как ты это сделал? Напиши отзыв об этом')

def start_game(chat_id):

    buttons = [['/kill',"/start"],['/stat','Suo']] #Настраиваем нужные кнопки
    keyboard = {'keyboard': buttons, 'resize_keyboard': True} # Создаем Реплуклавиатуру , ставит размер пользователя
    keyboard_1 = {'inline_keyboard':[
        [{'text': 'Влево', 'callback_data': 'left'},{'text':'Вправо','callback_data':'right'}],

    ]
    }
    bot.sendMessage(chat_id,'Игра запущена', reply_markup =keyboard) # Отправляем клавиатуру пользователю
    bot.sendMessage(chat_id, 'На вас мчится грузовик, вы думаете куда отпрыгнуть, куда вы отпрыгните?', reply_markup=keyboard_1)


