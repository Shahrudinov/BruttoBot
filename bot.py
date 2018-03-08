from bot import bot
import configparser
import telepot

config = configparser.ConfigParser()
config.read('env.ini')

TelegramBot = telepot.Bot(config.get('TELEGRAM', 'token'))

