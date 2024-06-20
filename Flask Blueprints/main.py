from flask import Flask
from Blueprints.hello_world.hello_world import helloworld_Bp

app = Flask(__name__)
app.register_blueprint(helloworld_Bp)

@app.route('/')
def index():
    return ""

if __name__ == '__main__':
    app.run(debug=True)
