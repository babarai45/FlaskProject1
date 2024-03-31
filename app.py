from flask import Flask

app = Flask(__name__)


@app.route('/')k
def hello_world():  # put application's code here
    return 'Well Come to Flask Project-1-10'

# and so on
@ app.route('/hello')
def hello():
    return 'Hello World!'
@ app.route('/hello/<name>')
def hello_name(name):
    return 'Hello ' + name + '!'
@ app.route('/hello/<int:id>')
def hello_id(id):
    return 'Hello ' + str(id) + '!'
if __name__ == '__main__':
    app.run()
