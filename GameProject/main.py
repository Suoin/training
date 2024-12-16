import telepot
from telepot.loop import MessageLoop
from config import bot
from data import player,save_players

from commands import start_game, on_callback_query
from player import Player


#Захватчик сообщения и преобразование в команды
def main(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        text = msg['text'].strip()
        if text in commands:
            commands[text](chat_id)
        else:
            # Если игрок уже в процессе создания персонажа, сохраняем его имя
            if chat_id in player and player[chat_id].name == 'Ты либо гений либо дурочек': #костыль, если игрок еще раз нажмет /start получит такой ник
                player[chat_id] = Player(text)  # Создаём объект класса Player
                save_players()  # Сохраняем состояние в модули
                bot.sendMessage(chat_id, f'Ваш персонаж, {text}, успешно создан!')
                start_game(chat_id)

            else:
                bot.sendMessage(chat_id, 'Используйте кнопки или команду /start для начала игры.') #защита от любителей не следовать инструкции


#Стратовое меню создания персонажа и запуска сцены игры из файла scenario
def start_menu(chat_id):
    if chat_id in player:
        bot.sendMessage(chat_id, f'Ваш персонаж {player[chat_id].name} жив, новая игра невозможна.')
    else:
        bot.sendMessage(chat_id, 'Введите имя своего персонажа:')
        player[chat_id] = Player('Ты либо гений либо дурочек')  # Включаем создание персонажа и флаг защита

def test(chat_id): #Это тестовая команда для отладки потом ее надо отключить
    if player:
        # Создаем список строк с chat_id и именами персонажей
        player_info = [f'Chat ID: {chat_id} - Имя персонажа: {player_obj.name}' for chat_id, player_obj in player.items()]
        # Отправляем сообщение с информацией о всех персонажах
        bot.sendMessage(chat_id, '\n'.join(player_info))
    else:
        bot.sendMessage(chat_id, 'В базе нет персонажей!')

def kill(chat_id): # отладочная команда, но не факт
    if chat_id in player:
        del player[chat_id]
        save_players()  # Сохраняем измененияФ
        bot.sendMessage(chat_id, 'Персонаж удалён.')
    else:
        bot.sendMessage(chat_id, 'У вас нет персонажа, для создания нового используйте команду /start')
def status(chat_id):
    if chat_id in player:
        player_stat = player[chat_id].show_stat()
        bot.sendMessage(chat_id,player_stat)
    else:
        bot.sendMessage(chat_id,'Персонажа нет, /start для запуска игры')
#словарь текстовых команд
commands = {'/start': start_menu,
            '/test': test,
            '/kill': kill,
            '/stat': status}

# Запуск бота с обработчиком сообщений и callback-запросов
MessageLoop(bot,{'chat': main,'callback_query': on_callback_query}).run_as_thread()
print("Игра запущена")
# Обработка событий
input("Нажмите Enter для завершения работы бота...")  # Ожидаем завершения работы
