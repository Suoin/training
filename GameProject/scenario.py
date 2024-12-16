from data import player,save_players
from config import bot
from bestiari import *
import telepot
def start_game_1 (chat_id,message_id):
    bot.deleteMessage((chat_id, message_id))
    keyboard = {'inline_keyboard': [
        [{'text': 'Удача', 'callback_data': 'luck'}, {'text': 'Навыки мечника', 'callback_data': 'melee'}],
        [{'text': 'Магические способности', 'callback_data': 'magic'}, {'text': 'Навыки стрелка', 'callback_data': 'range'}]
    ]
    }
    bot.sendMessage(chat_id, 'Открыв глаза, вы увидели сияние и странную женщину\n'
                             'Не повезло тебе, не переживай, вот тебе шанс переродится\n'
                             'Выберай способности и иди убей владыку тьмы, а то он обнаглел', reply_markup=keyboard)  # Отправляем клавиатуру пользователю

def choise_data (chat_id,message_id, data):

    if chat_id in player:
        if data == 'luck':
            player[chat_id].luck +=5
            player[chat_id].player_class.append('Везунчик')
            save_players()
            forest_star(chat_id, message_id)
        elif data == 'melee':
            player[chat_id].sila += 5
            player[chat_id].player_class.append('Воин')
            save_players()
            forest_star(chat_id, message_id)
        elif data == 'range':
            player[chat_id].agila += 5
            player[chat_id].player_class.append('Стрелок')
            save_players()
            forest_star(chat_id, message_id)
        elif data == 'magic':
            player[chat_id].intelect += 5
            player[chat_id].player_class.append('Маг')
            save_players()
            forest_star(chat_id, message_id)

def forest_star(chat_id, message_id):
    if 'Маг' in player[chat_id].player_class:
        text = 'Применить магию'
        callback = 'use_magic'
    elif 'Стрелок' in  player[chat_id].player_class:
        text = 'Сделать оружие'
        callback = 'craft_weapon'
    elif 'Воин' in player[chat_id].player_class:
        text ='Поискать оружие'
        callback = 'find_weapon'
    elif 'Удача' in player[chat_id].player_class:
        text = 'Внимательно осмотреться'
        callback = 'find_amul'

    keyboard = {'inline_keyboard': [
        [{'text': 'Идти прямо', 'callback_data': 'go_forward'}, {'text': 'Осмотреться', 'callback_data': 'osmotr'}],
        [{'text': text, 'callback_data': callback}]
    ]
    }
    bot.sendMessage(chat_id, 'Вы оказались на лесной опушке, ваши действия? Потом сделать описание и картинку',
                    reply_markup=keyboard)  # Отправляем клавиатуру пользователю

def find_weapon(chat_id,message_id,data):
    bot.deleteMessage((chat_id, message_id))
    if data == 'use_magic':
        player[chat_id].abillity.append('Стрела огня')
        save_players()
        bot.sendMessage(chat_id, 'Сделав пассы руками, и сложив кисть в форме пистолета, с кончика пальца\n'
                                 'вылетела огненная стрела')
    elif data == 'find_amul':
        player[chat_id].quest_invetary.append('Странный амулет')
        player[chat_id].use_hand.append('Стальной кинжал')
        save_players()
        bot.sendMessage(chat_id, 'Внимательно осмотрев поляну, в траве вы заметили что то блестящее\n'
                                 'это был странной формы амулет и какой то кинжал')
    elif data == 'find_weapon':
        player[chat_id].use_hand.append('Меч-палка')
        save_players()
        bot.sendMessage(chat_id, 'Осмотрев поляну и ближайщий куст, вы отломали ветку\n'
                                 'которая более менее была похоже на меч, лучше уж так, чем совсем без оружия')
    elif data == 'craft_weapon':
        player[chat_id].use_hand.append('Самодельный лук')
        save_players()
        bot.sendMessage(chat_id, 'Изучив местность и ближайщий куст обтянутый лозами и лианами, вы смастерили себе лук.\n'
                                 'Осмотрев его, вы задумались, что в детстве делали куда лучше')

    if 'Стрела огня' in player[chat_id].abillity:
        text ='По практиковатся в магии'
        callback = 'magic_practical'
    if 'Странный амулет' in player[chat_id].quest_invetary:
        text ='Рассмотреть амулет'
        callback = 'inspect_amulet'
    elif 'Самодельный лук'in player[chat_id].use_hand:
        text = 'По практиковатся в стрельбе'
        callback ='shot_bow'
    elif 'Меч-палка'in player[chat_id].use_hand:
        text = 'Сделать взмах мечом'
        callback = 'shot_sword'
    keyboard = {'inline_keyboard': [
        [{'text': 'Идти прямо', 'callback_data': 'go_forward'}, {'text': text, 'callback_data': callback}]
    ]
    }
    bot.sendMessage(chat_id, 'Вас удовлетворил результат',
                    reply_markup=keyboard)  # Отправляем клавиатуру пользователю


def go_forward(chat_id,message_id,data):
    bot.deleteMessage((chat_id,message_id))
    keyboard = {'inline_keyboard': [
        [{'text': 'Поискать гильдию', 'callback_data': 'find_guild'}, {'text': 'Осмотреть город', 'callback_data': 'town_osmotr'}],
        [{'text':'Поискать рынок','callback_data':'find_sell'}]
    ]
    }
    bot.sendMessage(chat_id, 'Некоторое время вы бродили по этому странному месту и на конец вышли к городским стенам\n'
                             'пройдя через главные ворота, вы вошли в средневековый фентезийный город\n'
                             'всюду ходят люди, в воздухе какофония разных ароматов, а из разных уголков города слышен шум', reply_markup=keyboard)  # Отправляем клавиатуру пользователю
def osmotr(chat_id,message_id,data):
    bot.sendMessage(chat_id, 'Вы стоите на обычной лесной поляне, вас окуржают деревья и кусы, судя по лианам и лозам\n'
                             'это место можно назвать даже тропическим лесом')
def goblin_fight(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    keyboard = {'inline_keyboard': [
        [{'text': 'Уйти', 'callback_data': 'go_forward'},
         {'text': 'Напасть на гоблина', 'callback_data': 'goblin_fight_start'}]
    ]}
    bot.sendMessage(chat_id, 'Вы слышите шум из кустов и заметили как из них задом пятится гоблин',
                    reply_markup=keyboard)
def goblin_fight_start(chat_id, message_id, data):
    bot.deleteMessage((chat_id, message_id))
    player[chat_id].goblin_flag = True
    save_players()

    goblin = Goblin('молодой гоблин')
    stat = goblin.show_stat()
    # Важное изменение: передаем в функцию универсального боя callback_function
    universal_fight(chat_id, message_id, goblin, callback_function=win_goblin)

def win_goblin(chat_id, message_id, data):
    bot.sendMessage(chat_id, 'Победа! Вы победили гоблина.')
    # После победы вызываем функцию, которая продолжит игру, например, возвращение в локацию
    continue_game(chat_id)

def continue_game(chat_id):
    # Пример следующей функции, которую вызываем после победы
    keyboard = {'inline_keyboard': [
        [{'text': 'Перейти к следующей локации', 'callback_data': 'go_to_next_location'}]
    ]}
    bot.sendMessage(chat_id, 'Что вы хотите сделать дальше?', reply_markup=keyboard)

def universal_fight(chat_id, message_id, target, callback_function):
    """
    Универсальная функция для проведения боя.
    После завершения боя вызовет callback_function, которая обработает следующий шаг.
    """
    stat = target.show_stat()
    keyboard = player_attack(chat_id, message_id, target)

    # Отправляем сообщение с характеристиками монстра
    sent_message = bot.sendMessage(
        chat_id,
        f"{stat}\n\nВыберите действие:",
        reply_markup=keyboard
    )

    # Убираем старое сообщение через callback после действия игрока
    def on_callback_query(msg):
        query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
        if from_id == chat_id:
            bot.deleteMessage((chat_id, message_id))  # Удаляем старое сообщение
            # Обрабатываем действия игрока
            process_action(chat_id, data, target, sent_message.message_id, callback_function)

def process_action(chat_id, data, target, message_id, callback_function):
    attack_response = ""

    # Проверяем, существует ли действие в каталоге `action`
    if data in player[chat_id].system['action']:
        # Получаем функцию действия из словаря
        action_function = player[chat_id].system['action'][data]
        attack_response = action_function(target)  # Выполняем действие
    else:
        attack_response = f'Действие {data} не найдено.'

    # Монстр наносит ответный удар
    monster_damage = target.attack
    player[chat_id].hp -= monster_damage
    attack_response += f"\nМонстр нанес вам {monster_damage} урона."

    # Обновляем статистику монстра и игрока
    stat = target.show_stat()
    player_stat = player[chat_id].show_stat()

    # Отправляем обновленные данные в сообщение
    bot.editMessageText(
        chat_id,
        message_id,
        f"{attack_response}\n\nВаши характеристики:\n{player_stat}\n\nХарактеристики противника:\n{stat}"
    )

    # Проверяем победу (если монстр мертв, вызываем callback_function)
    if target.hp <= 0:
        callback_function(chat_id, message_id, data)



#Генератор способностей в бою
def player_attack(chat_id, message_id, target):
    # Создаём список всех доступных элементов и кнопок для них
    buttons = [
        {'text': f"Использовать {item}", 'callback_data': f'action_{item}'}
        for items in [player[chat_id].abillity, player[chat_id].invetary, player[chat_id].use_hand]
        for item in items
    ]

    # Если кнопок нет, добавляем заглушку
    if not buttons:
        buttons = [{'text': "Нечего использовать", 'callback_data': 'no_action'}]

    # Группируем кнопки по 3 в ряд
    return {'inline_keyboard': [buttons[i:i + 3] for i in range(0, len(buttons), 3)]}







callback_commands ={
                'fight': universal_fight,
                # обработка каллбэков для чойз_дата
                'luck':choise_data,'melee':choise_data ,'range':choise_data ,'magic':choise_data,
                # обработка функции форест_старт
                'use_magic': find_weapon, 'craft_weapon':find_weapon, 'find_weapon':find_weapon, 'find_amul': find_weapon,
                # Обработка кнопки осмотрется и идти вперед
                'go_forward': go_forward, 'osmotr':osmotr,
                #Линия битвы с гоблином
                'magic_practical': goblin_fight , 'inspect_amulet':goblin_fight, 'shot_bow':goblin_fight, 'shot_sword':goblin_fight,
                'goblin_fight_start':goblin_fight_start, 'attack':goblin_fight_start}
