from flask import Flask
from app.core.framework import logger
from app.core.framework import base

app = Flask(__name__)

log = logger.Logger(__name__).getlog()

@app.route('/')
def hello_world():
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
