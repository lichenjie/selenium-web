from flask import Flask
from app.src.core import logging
import os

app = Flask(__name__)

logger = logging.Logger(__name__).getlog()

@app.route('/')
def index():
    return 'index'



if __name__ == '__main__':
    app.run()
