import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN
import datetime

# Список вопросов и ответов для функции викторины
questions = [
    {
        "question": "Вопрос1: ",
        "answers": ["Ответ1", "Ответ2", "Ответ3", "Ответ4"],
        "points": [1, 2, 3, 4],
    },
    {
        "question": "Вопрос2: ",
        "answers": ["Ответ1", "Ответ2", "Ответ3", "Ответ4"],
        "points": [4, 1, 2, 3],
    },
    {
        "question": "Вопрос3: ",
        "answers": ["Ответ1", "Ответ2", "Ответ3", "Ответ4"],
        "points": [1, 3, 2, 4],
    },
    {
        "question": "Вопрос4: ",
        "answers": ["Ответ1", "Ответ2", "Ответ3", "Ответ4"],
        "points": [2, 4, 1, 3],
    },
]

# Данные по пользователям
user_scores = {}
user_questions = {}

admin_chat_id = "Введите ID администратора"  # Замените на реальный ID администратора
telegram_bot_link = "https://t.me/your_bot_link"  # Замените на ссылку на ваш бот


# Главная клавиатура
def show_start_keyboard(bot, chat_id):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='Узнать свое тотемное животное'),
                   KeyboardButton(text='Посмотреть программу опеки')],
                  [KeyboardButton(text='Оставить отзыв')]],
        resize_keyboard=True
    )
    with open('logo.jpg', 'rb') as photo:
        bot.sendPhoto(chat_id, photo=photo)
    bot.sendMessage(chat_id, 'Привет! Я бот Московского зоопарка! Вот краткая инструкция по работе со мной.\n'
                             '<b>Команда:</b> /start - запускает меня\n'
                             '<b>Команда:</b> /help - расскажет о всех командах',
                    reply_markup=keyboard, parse_mode='HTML')


# Сохранение отзыва в файл
def save_feedback(feedback, chat_id):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('feedbacks.txt', 'a', encoding='utf-8') as f:
        f.write(f"Дата: {date}, ID чата: {chat_id}, Отзыв: {feedback}\n")


# Викторина
def start_victorina(chat_id, bot):
    if chat_id not in user_scores:
        user_scores[chat_id] = {'score': 0, 'current_question': 0}

    if user_scores[chat_id]['current_question'] < len(questions):
        question = questions[user_scores[chat_id]['current_question']]
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=ans) for ans in question["answers"]],
                [KeyboardButton(text='Остановить викторину')]
            ],
            resize_keyboard=True
        )
        bot.sendMessage(chat_id, question["question"], reply_markup=keyboard)
    else:
        total_score = user_scores[chat_id]['score']
        if total_score <= 4:
            result = "Результат 1: Ваши баллы низкие, возможно, вам стоит больше узнать о животных!"
        elif total_score <= 8:
            result = "Результат 2: Вы хорошо разбираетесь в животных, но есть еще куда расти!"
        elif total_score <= 12:
            result = "Результат 3: Отлично! Вы хорошо понимаете природу и животных!"
        else:
            result = "Результат 4: Вы настоящий эксперт! Ваши знания о животных потрясающие!"

        # Сохраняем результат в user_scores
        user_scores[chat_id]['result'] = result

        social_buttons = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Поделиться в Facebook",
                                      url=f"https://www.facebook.com/sharer/sharer.php?u={telegram_bot_link}&quote={result}")],
                [InlineKeyboardButton(text="Поделиться в ВКонтакте",
                                      url=f"https://vk.com/share.php?url={telegram_bot_link}&title={result}")],
                [InlineKeyboardButton(text="Поделиться в Twitter",
                                      url=f"https://twitter.com/intent/tweet?url={telegram_bot_link}&text={result}")],
                [InlineKeyboardButton(text="Поделиться в Instagram",
                                      url=f"https://www.instagram.com/?url={telegram_bot_link}&caption={result}")],
            ]
        )

        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='Запустить вопросы заново')],
                [KeyboardButton(text='Вернуться в главное меню'),
                 KeyboardButton(text='Узнать подробнее')]
            ],
            resize_keyboard=True
        )

        bot.sendMessage(chat_id, result, reply_markup=social_buttons)
        bot.sendMessage(chat_id, "Вы можете перезапустить викторину или вернуться в главное меню.",
                        reply_markup=keyboard)

        # Сброс состояния викторины после завершения
        user_scores[chat_id]['score'] = 0
        user_scores[chat_id]['current_question'] = 0


# Обработка ответов администратора
def reply_to_user(admin_msg, bot):
    admin_chat_id = admin_msg['chat']['id']

    if 'reply_to_message' in admin_msg:
        reply_to_message = admin_msg['reply_to_message']
        reply_to_message_id = reply_to_message['message_id']

        for user_chat_id, question_info in user_questions.items():
            if question_info.get('question_msg_id') == reply_to_message_id:
                if admin_msg['text'].strip().lower() == '/end_dialog':
                    # Завершение диалога
                    bot.sendMessage(user_chat_id, "Администратор завершил диалог. Возвращаем вас в главное меню.")
                    show_start_keyboard(bot, user_chat_id)
                    del user_questions[user_chat_id]
                    bot.sendMessage(admin_chat_id, f"Диалог с пользователем {user_chat_id} завершён.")
                else:
                    # Отправка ответа пользователю
                    bot.sendMessage(user_chat_id, f"Ответ администратора: {admin_msg['text']}")
                    bot.sendMessage(admin_chat_id, f"Ответ отправлен пользователю с ID: {user_chat_id}")
                return

        bot.sendMessage(admin_chat_id, "Ошибка: не удалось найти пользователя для ответа.")
    else:
        bot.sendMessage(admin_chat_id, "Ошибка: это сообщение не является ответом на вопрос пользователя.")


# Обработчик сообщений
def navi(msg, bot):
    chat_id = msg['chat']['id']
    command = msg.get('text')

    if chat_id == int(admin_chat_id):
        reply_to_user(msg, bot)
        return
    #запуск викторины
    if command == 'Узнать свое тотемное животное':
        start_victorina(chat_id, bot)
    #запуск диалога с администратором
    elif command == 'Узнать подробнее':
        result = user_scores.get(chat_id, {}).get('result',
                                                  "Пользователь ещё не проходил викторину или результат был сброшен.")
        bot.sendMessage(chat_id, "Введите свой вопрос:", reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text='Остановить разговор')]], resize_keyboard=True))
        user_questions[chat_id] = {'state': 'active', 'question_msg_id': None, 'result': result}


    # Отправка вопроса администратору
    elif chat_id in user_questions and user_questions[chat_id]['state'] == 'active':
        if command == 'Остановить разговор':
            bot.sendMessage(admin_chat_id, f"Пользователь с ID {chat_id} завершил диалог.")
            show_start_keyboard(bot, chat_id)
            user_questions.pop(chat_id, None)
        else:
            # Отправка вопроса и результата викторины администратору
            user_question_text = msg.get('text')
            result = user_questions[chat_id].get('result', "Результат викторины не определён.")
            question_msg = bot.sendMessage(admin_chat_id, f"Вопрос от пользователя {chat_id}:\n"
                                                          f"{user_question_text}\n\n"
                                                          f"Результат викторины: {result}")
            user_questions[chat_id]['question_msg_id'] = question_msg['message_id']

            bot.sendMessage(chat_id, "Ваш вопрос отправлен администратору, ждите ответа.")
    elif command == 'Оставить отзыв':
        bot.sendMessage(chat_id, "Пожалуйста, оставьте свой отзыв:", reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text='Отмена')]], resize_keyboard=True))
        user_questions[chat_id] = {'state': 'waiting_for_feedback'}
    elif command == 'Отмена' and chat_id in user_questions:
        show_start_keyboard(bot, chat_id)
        user_questions.pop(chat_id, None)
    elif chat_id in user_questions and user_questions[chat_id].get('state') == 'waiting_for_feedback':
        feedback_text = msg.get('text')
        save_feedback(feedback_text, chat_id)
        bot.sendMessage(chat_id, "Ваш отзыв был отправлен. Спасибо!", reply_markup=show_start_keyboard(bot, chat_id))
        user_questions.pop(chat_id, None)  # Сброс состояния после отправки отзыва
    elif command == '/start':
        show_start_keyboard(bot, chat_id)
    elif command == 'Запустить вопросы заново':
        start_victorina(chat_id, bot)
    elif command == 'Остановить викторину':
        show_start_keyboard(bot, chat_id)
        user_scores[chat_id] = {'score': 0, 'current_question': 0}
    elif command == 'Вернуться в главное меню':
        show_start_keyboard(bot, chat_id)
    elif command == 'Посмотреть программу опеки':
        bot.sendMessage(chat_id, 'Тут будет подробная информация об опеке')
    #обработка блока викторины
    elif chat_id in user_scores and user_scores[chat_id]['current_question'] < len(questions) and command in \
            questions[user_scores[chat_id]['current_question']]["answers"]:
        # Обработка правильного ответа
        index = questions[user_scores[chat_id]['current_question']]["answers"].index(command)
        user_scores[chat_id]['score'] += questions[user_scores[chat_id]['current_question']]['points'][index]

        # Переход к следующему вопросу
        user_scores[chat_id]['current_question'] += 1
        start_victorina(chat_id, bot)


# Инициализация бота
bot = telepot.Bot(TOKEN)
MessageLoop(bot, lambda msg: navi(msg, bot)).run_as_thread()
print("Бот запущен..")

while True:
    pass



