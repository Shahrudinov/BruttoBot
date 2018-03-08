from flask import Flask

bot = Flask(__name__)

from bot import routes
