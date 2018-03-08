from bot import bot

@bot.route('/')
def home():
    return 'hello world'