from flask import render_template
from app.home import home



@home.route('/', methods=['GET'])
def index():
    return render_template('index.html')