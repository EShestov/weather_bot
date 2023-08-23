import telebot
import requests
import json



bot = telebot.TeleBot('6559299135:AAH1GbA_qLDRW8EIHq9n9ZGAQe5-GLyPC1g')
API = 'b88e6721c3226eba42b6922270301139'



@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую! Напиши название города')




@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        feels = data["main"]['feels_like']
        bot.reply_to(message, f'На данный момент погода: {temp}°C, по ощущениям {feels}°C')
        if temp > 20:
            image = 'summer.jpg'
        elif 10<temp<=20:
            image = 'autumn.jpg'
        elif 0<temp<=10:
            image = 'spring.jpg'
        elif temp < 0:
            image = 'winter.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Такого города не существует')

    

bot.polling(none_stop=True)