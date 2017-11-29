from flask import Flask
from app.src.core import logging
from flask import current_app
import os

app = Flask(__name__)

logger = logging.Logger(__name__).getlog()

@app.route('/')
def index():
    return 'index'



if __name__ == '__main__':
    app.run()
