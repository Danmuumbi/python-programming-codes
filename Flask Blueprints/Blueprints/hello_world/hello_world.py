from flask import Blueprint,render_template

helloworld_Bp = Blueprint('helloworld', __name__, template_folder="templates")

@helloworld_Bp.route('/')
def index():
    return "Hello, World!"

@helloworld_Bp.route('/hello')
def hello():
    return "Hello, World again!"

@helloworld_Bp.route('/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'

@helloworld_Bp.route('/hellohtml')
def hello_html():
    return render_template("helloword/hello.html")
