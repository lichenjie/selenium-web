from flask import render_template

from app.core import run
from app.home import home


@home.route('/', methods=['GET'])
def index():
    return render_template('index.html')



@home.route('/selenium', methods=['GET'])
def selenium():
    return render_template('selenium.html')



@home.route('/baidu_search', methods=['GET'])
def baidu_search():
    filename = run.run()
    return render_template("result/" + filename)