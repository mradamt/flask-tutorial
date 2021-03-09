from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Your face is an index page'

@app.route('/monkeys')
def get_monkeys():
    return 'Arr here be monkeys'

@app.route('/rando/<panda>')
def rando_panda(panda):
    return f'The URL you entered, {escape(panda)}, is silly. Do better.'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('get_monkeys'))
    print(url_for('rando_panda', panda='wonkysocks'))

@app.route('/projects/')
def projects():
    return 'The project page. Accessing this URL without the trailing slash will redirect to "/projects/" WITH a trailing slash.'

@app.route('/about')
def about():
    return 'The about page. Accessing this URL with a trailing slash will produce a 404.'
