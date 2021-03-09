from flask import Flask
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
