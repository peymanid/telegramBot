import telebot
from pyowm import OWM

# Telegram Bot API Token
TELEGRAM_TOKEN = '6644952772:AAHYGce96OFXdUAFtFH34wL1F2Vye0Q94ZQ'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# OpenWeatherMap API Key
OWM_API_KEY = 'b4f115acbf899abca86c215156e80167'
owm = OWM(OWM_API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I can provide you with weather updates. Just ask!")

@bot.message_handler(func=lambda message: True)
def send_weather(message):
    try:
        observation = owm.weather_at_place(message.text)
        w = observation.get_weather()
        temperature = w.get_temperature('celsius')['temp']
        bot.reply_to(message, f"The temperature in {message.text} is {temperature}°C.")
    except:
        bot.reply_to(message, f"Unable to find {message.text}")

bot.polling()

print("Done")
