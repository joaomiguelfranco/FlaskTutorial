from flask import Flask
from src.featureA.featureA import featureA_bp

app = Flask(__name__)
app.register_blueprint(featureA_bp)


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
