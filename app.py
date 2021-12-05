from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/cakes')
def cakes():
  return render_template('cakes.html')

@app.route('/hello/<name>')
def greet(name):
  return render_template('page.html', name=name)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)


