import telebot
from config import keys,TOKEN
from exсeption import ConvertException, ValuteConvert
# основной исполняющий файл
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    text = ('Привет, эксперементальный бот, по переводу валют. \n Введите ваш запрос в формате \n \
<Имя вашей валюты> <Имя требуемой валюты <кол-во цифрами> \n \
Введите /values для получения всех валют')
    bot.reply_to(message, text) # реплей это выбрать ввод и ответить на него

@bot.message_handler(commands=['values'])
def values (message):
    text = 'Валюты с которыми я работаю'
    for key in keys.keys():
        text = '\n'.join((text,key,))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')  # получаем значения из чата в телеграмм
        if len(values) != 3:  # проверяем на соответсвие
            raise ConvertException('Cлишком много данных') #при не соответсвии сообщаем
        quote, base, amount = values # назначаем переменные
        total, price = ValuteConvert.convert(quote, base, amount) # возвращаем из exception Значения
    except ConvertException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалость обрботать команду \n {e}')
    else:
        text = f'За {amount} {quote} в получите  - {total} {base} , цена за один {quote} : {price} {base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)

