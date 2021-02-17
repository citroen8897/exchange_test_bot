import telebot
import requests
import datetime
import save_rates_into_mysql
import get_time_from_mysql
import get_rates_from_mysql


bot = telebot.TeleBot("1662764914:AAGpW6XhGR96peWzGNDtvNyGwd-JhM0UTiY")

current_time = datetime.datetime.now()
last_time = get_time_from_mysql.get_time_db()
critical_time_delta = datetime.timedelta(minutes=10)

if current_time - last_time > critical_time_delta:
    rates_get = requests.get('https://api.exchangeratesapi.io/latest?base=USD')
    rates_dict = dict(rates_get.json())['rates']
    save_rates_into_mysql.save_rates(rates_dict)
    print('Rates from site...')
else:
    rates_dict = get_rates_from_mysql.get_rates_db()
    print('Rates from mySQL...')


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я Справочник обменных курсов "
                                      "валют!\nНажми /rates")


@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text == "/rates":
        bot.send_message(message.chat.id, 'Обменные курсы по отношению к USD '
                                          'на сегодня:')
        for k, v in rates_dict.items():
            bot.send_message(message.chat.id, f'{k}: {round(v, 2)}')
    else:
        bot.send_message(message.chat.id, "Нажми /help")


bot.polling()

