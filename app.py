from flask import Flask
from datetime import datetime

app = Flask(__name__)

counter = 0

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/date')
def current_date():
    return f'Response time: {str(datetime.now())}'
# http://localhost:5000/date

@app.route('/date2')
def current_date2():
    return f'Response time: {str(datetime.now())}'

@app.route('/counter')
def counter_view():
    global counter
    counter += 1
    return f'Visit counter: {}'

if __name__ == '__main__':
    app.run()
