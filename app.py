from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/cakes')
def cakes():
  return render_template('cakes.html')

@app.route('/hello/<name>')
def greet(name):
  now = datetime.datetime.now() # get current time and store it in `now`
  timeString = now.strftime('%d-%m-%Y %H:%M:%S') # create formatted stringn of date and time from `now` object
  templateData = { # create dictionary of keys and associated values (variables)
    'title': name,
    'time': timeString
  }
  return render_template('page.html', **templateData) # pass dictionary to template

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)


